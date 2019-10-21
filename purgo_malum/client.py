"""
A client library for the the PurgoMalum REST API.
https://www.purgomalum.com/index.html.
"""
import requests
from future.standard_library import install_aliases
install_aliases()
from urllib.parse import urlencode

PURGO_MALUM_BASE_URL = 'https://www.purgomalum.com/service/'
FILTER_REQUEST_TYPES = ['json', 'plain', 'xml']
VALID_REQUEST_TYPES = FILTER_REQUEST_TYPES + ['containsprofanity']


class ResultError(Exception):
    """Raised when the server returns an unexpected error."""
    pass


def build_url(text, request_type, add=None, fill_text=None, fill_char=None):
    """
    Builds the query string to use for an PurgoMalum API call
    See https://www.purgomalum.com for details

    Args:
        text (string): The text that will be submitted
        request_type (string): The type of request that will be sent to the PurgoMalum service
            Must be one of 'json', 'plain', 'xml'.
        add (string): A comma separated list of words to be added to the profanity list.
            Accepts letters, numbers, underscores (_) and commas (,). Accepts up to 10 words
            (or 200 maximum characters in length). The PurgoMalum filter is case-insensitive,
            so the case of you entry is not important.
        fill_text (string): Text used to replace any words matching the profanity list.
            Accepts letters, numbers, underscores (_) tildes (~), exclamation points (!),
            dashes/hyphens (-), equal signs (=), pipes (|), single quotes ('), double quotes ("),
            asterisks (\*), open and closed curly brackets ({ }), square brackets ([ ]) and
            parentheses ().  Maximum length of 20 characters. When not used, the default is an
            asterisk (\*) fill.
        fill_char (string): Single character used to replace any words matching the profanity
            list. Fills designated character to length of word replaced. Accepts underscore (_)
            tilde (~), dash/hyphen (-), equal sign (=), pipe (|) and asterisk (\*). When not used,
            the default is an asterisk (\*) fill.

    Returns:
        string: The URL for the specified request.
            Ex: https://www.purgomalum.com/service/json?text=test+text&add=test&f&fill_char=%7C

    Raises:
        ValueError: If an input parameter is invalid
    """
    if not isinstance(text, str):
        raise ValueError("Input param 'text' is a {} (must be a str)".format(type(text)))

    if not text:
        raise ValueError('No input string provided')

    if request_type not in VALID_REQUEST_TYPES:
        raise ValueError("Input param 'request_type' is invalid - must be one of {}"
                         .format(VALID_REQUEST_TYPES))

    query_string_params = [('text', text)]

    if add:
        if not isinstance(add, str):
            raise ValueError("Input param 'add' is a {} (must be a str)".format(type(add)))
        query_string_params.append(('add', add))

    if fill_text:
        if not isinstance(fill_text, str):
            raise ValueError("Input param 'fill_text' is a {} (must be a str)"
                             .format(type(fill_text)))
        query_string_params.append(('fill_text', fill_text))

    if fill_char:
        if not isinstance(fill_char, str):
            raise ValueError("Input param 'fill_char' is a {} (must be a str)"
                             .format(type(fill_char)))
        query_string_params.append(('fill_char', fill_char))

    query_string = urlencode(query_string_params)

    return ''.join([PURGO_MALUM_BASE_URL, request_type, '?', query_string])


def contains_profanity(text, add=None):
    """
    Use the PurgoMalum API to check if the specified text contains profanity
    See https://www.purgomalum.com for details

    Args:
        text (string): Text to filter
        add (string): A comma separated list of words to be added to the profanity list.
            Accepts letters, numbers, underscores (_) and commas (,). Accepts up to 10 words
            (or 200 maximum characters in length). The PurgoMalum filter is case-insensitive,
            so the case of you entry is not important.

    Returns:
        boolean: Indicates whether the string does or does not contain profanity

    Raises:
        ResultError: Client received an unexpected result
    """
    full_url = build_url(text, 'containsprofanity', add)
    response = requests.get(url=full_url)
    result = response.content.decode()

    # The response should be a string of 'true' or 'false' but we handle case sensitivity to be safe
    if result not in ('true', 'True', 'false', 'False'):
        raise ResultError(result)

    return result.lower() == 'true'


def retrieve_filtered_text_raw(text, request_type, add=None, fill_text=None, fill_char=None):
    """
    Use the PurgoMalum API to filter profanity from the specified text
    This function returns the raw data returned by the REST API
    See https://www.purgomalum.com for details

    Args:
        text (string): Text to filter
        request_type (string): The type of request that will be sent to the PurgoMalum service
            Must be one of 'json', 'plain', 'xml'.
        add (string): A comma separated list of words to be added to the profanity list.
            Accepts letters, numbers, underscores (_) and commas (,). Accepts up to 10 words
            (or 200 maximum characters in length). The PurgoMalum filter is case-insensitive,
            so the case of you entry is not important.
        fill_text (string): Text used to replace any words matching the profanity list.
            Accepts letters, numbers, underscores (_) tildes (~), exclamation points (!),
            dashes/hyphens (-), equal signs (=), pipes (|), single quotes ('), double quotes ("),
            asterisks (\*), open and closed curly brackets ({ }), square brackets ([ ]) and
            parentheses (). Maximum length of 20 characters. When not used, the default is an
            asterisk (\*) fill.
        fill_char (string): Single character used to replace any words matching the profanity
            list. Fills designated character to length of word replaced. Accepts underscore (_)
            tilde (~), dash/hyphen (-), equal sign (=), pipe (|) and asterisk (\*). When not used,
            the default is an asterisk (\*) fill.

    Returns:
        string: The response returned by the PurgoMalum REST API

    Raises:
        ValueError: Invalid request_type was passed in
    """
    full_url = build_url(text, request_type, add, fill_text, fill_char)
    response = requests.get(url=full_url)

    if request_type == 'json':
        response_content = response.json()
    elif request_type in ('plain', 'xml'):
        response_content = response.content.decode()
    else:
        raise ValueError("Input param 'request_type' is invalid - must be one of {}"
                         .format(FILTER_REQUEST_TYPES))
    return response_content


def retrieve_filtered_text(text, add=None, fill_text=None, fill_char=None):
    """
    Use the PurgoMalum API to filter profanity from the specified text
    This call defaults to using the 'json' request type
    See https://www.purgomalum.com for details

    Args:
        text (string): Text to filter
        add (string): A comma separated list of words to be added to the profanity list.
            Accepts letters, numbers, underscores (_) and commas (,). Accepts up to 10 words
            (or 200 maximum characters in length). The PurgoMalum filter is case-insensitive,
            so the case of you entry is not important.
        fill_text (string): Text used to replace any words matching the profanity list.
            Accepts letters, numbers, underscores (_) tildes (~), exclamation points (!),
            dashes/hyphens (-), equal signs (=), pipes (|), single quotes ('), double quotes ("),
            asterisks (\*), open and closed curly brackets ({ }), square brackets ([ ]) and
            parentheses (). Maximum length of 20 characters. When not used, the default is an
            asterisk (\*) fill.
        fill_char (string): Single character used to replace any words matching the profanity
            list. Fills designated character to length of word replaced. Accepts underscore (_)
            tilde (~), dash/hyphen (-), equal sign (=), pipe (|) and asterisk (\*). When not used,
            the default is an asterisk (\*) fill.

    Returns:
        string: The filtered text

    Raises:
        ResultError: Client received an error from the server
    """
    response_content = retrieve_filtered_text_raw(text, 'json', add, fill_text, fill_char)

    if 'error' in response_content:
        raise ResultError(response_content['error'])

    return response_content['result']
