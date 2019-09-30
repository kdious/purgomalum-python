"""
File:           test_client.py
Description:    Unit tests for all functions within purgo_malgum.client.py
                Theses unit tests do call the actual PurgoMalum production
                API in order to test against potential API changes.
"""
from mock import Mock
import pytest

from purgo_malum.client import (
    build_url,
    ClientError,
    contains_profanity,
    retrieve_filtered_text,
    retrieve_filtered_text_raw,
)


# Test contains_profanity function

def test_contains_profanity_true():
    assert contains_profanity('@$$hole hello') is True, "Should be True"


def test_contains_profanity_false():
    assert contains_profanity('Nice bunny') is False, "Should be False"


def test_contains_profanity_invalid_result(mocker):
    response = Mock()
    response.content = b'invalid'
    mocker.patch('requests.get', return_value=response)
    with pytest.raises(ClientError):
        contains_profanity('Invalid text test')


# Test retrieve_filtered_text function

def test_retrieve_filtered_text():
    assert retrieve_filtered_text('@$$hole') == '*******', "Should be '*******'"


def test_retrieve_filtered_text_with_add():
    assert retrieve_filtered_text('hello, test', add='test') == 'hello, ****', "Should be 'hello, ****'"


def test_retrieve_filtered_text_fill_text():
    assert retrieve_filtered_text('@$$hole', fill_text='[filtered]') == '[filtered]', "Should be '[filtered]'"


def test_retrieve_filtered_text_fill_char():
    assert retrieve_filtered_text('@$$hole', fill_char='|') == '|||||||', "Should be '|||||||'"


def test_retrieve_filtered_text_json_error(mocker):
    url = 'https://www.purgomalum.com/service/json?text='
    mocker.patch('purgo_malum.client.build_url', return_value=url)
    with pytest.raises(ClientError):
        retrieve_filtered_text('')


# Test retrieve_filtered_text_raw function

def test_retrieve_filtered_text_raw_json(mocker):
    url = 'https://www.purgomalum.com/service/json?text=test+text'
    expected_response = {'result': 'test text'}
    mocker.patch('purgo_malum.client.build_url', return_value=url)
    filtered_text = retrieve_filtered_text_raw('test text', request_type='json')
    assert filtered_text == expected_response


def test_retrieve_filtered_text_raw_plain(mocker):
    url = 'https://www.purgomalum.com/service/plain?text=test+text'
    expected_response = 'test text'
    mocker.patch('purgo_malum.client.build_url', return_value=url)
    filtered_text = retrieve_filtered_text_raw('test text', request_type='plain')
    assert filtered_text == expected_response


def test_retrieve_filtered_text_raw_xml(mocker):
    url = 'https://www.purgomalum.com/service/xml?text=test+text'
    expected_response = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                         '<PurgoMalum xmlns="http://www.purgomalum.com">'
                         '<result>test text</result>'
                         '</PurgoMalum>')
    mocker.patch('purgo_malum.client.build_url', return_value=url)
    filtered_text = retrieve_filtered_text_raw('test text', request_type='xml')
    assert filtered_text == expected_response


def test_retrieve_filtered_text_raw_invalid(mocker):
    url = 'https://www.purgomalum.com/service/invalid?text=test+text'
    mocker.patch('purgo_malum.client.build_url', return_value=url)
    with pytest.raises(ValueError):
        retrieve_filtered_text_raw('test text', request_type='invalid')


# Test build_url function

def test_build_url():
    full_url = build_url('test text', 'json', add='test', fill_text='[filtered]', fill_char='|')
    expected_url = 'https://www.purgomalum.com/service/json?text=test+text&add=test&fill_text=%5Bfiltered%5D&fill_char=%7C'
    assert full_url == expected_url, "Should be '{}".format(expected_url)


def test_build_url_text_incorrect_type():
    with pytest.raises(ValueError):
        build_url(None, 'invalid')


def test_build_url_no_text():
    with pytest.raises(ValueError):
        build_url('', 'json')


def test_build_url_invalid_request_type():
    with pytest.raises(ValueError):
        build_url('test text', 'invalid')


def test_build_url_invalid_add():
    with pytest.raises(ValueError):
        build_url('test text', 'json', add=3)


def test_build_url_invalid_fill_text():
    with pytest.raises(ValueError):
        build_url('test text', 'json', fill_text=3)


def test_build_url_invalid_fill_char():
    with pytest.raises(ValueError):
        build_url('test text', 'json', fill_char=3)
