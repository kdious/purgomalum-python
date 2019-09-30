PurgoMalum Client
=================

This is a Python client for the
`PurgoMalum <https://www.purgomalum.com/index.html>`__ web service.

Installation
------------

::

    pip install purgomalum

or

::

    python setup.py install

Usage
-----

To use the basic filtering you can call the ``contains_profanity`` or
the ``retrieve_filtered_text`` methods from the client:

::

    >>> from purgo_malum import client
    >>> client.contains_profanity('You are an @a$$hole')
    True

    >>> client.retrieve_filtered_text('You are an @a$$hole')
    u'You are an ********'

The client functions also support adding words to the profanity list,
setting your own filter text, and setting your own filter characters:

::

    >>> from purgo_malum import client
    >>> client.contains_profanity('You are a good friend', add='you')
    True

    >>> client.retrieve_filtered_text('You are a good friend', add='you,are', fill_text='[filtered]')
    u'[filtered]  [filtered] a good friend'

    >>> client.retrieve_filtered_text('You are a good friend', add='you,are', fill_char='|')
    u'||| ||| a good friend'

You can also get the raw data that the PurgoMalum API returns by calling
the ``raw`` version of the APIs:

::

    >>> from purgo_malum import client
    >>> client.retrieve_filtered_text_raw('You are an @a$$hole', 'json')
    {u'result': u'You are an ********'}
    >>> client.retrieve_filtered_text_raw('You are an @a$$hole', 'plain')
    u'You are an ********'
    >>> client.retrieve_filtered_text_raw('You are an @a$$hole', 'xml')
    u'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><PurgoMalum xmlns="http://www.purgomalum.com"><result>You are an ********</result></PurgoMalum>'

This can be helpful in the event that the API changes and/or you feel
you can use the raw data in some manner.

You can also see the URL that is created for a specific request by using
the ``build_url`` method (mainly helpful for testing):

::

    >>> client.build_url('test text', 'json', add='test', fill_text='[filtered]')
    u'https://www.purgomalum.com/service/json?text=test+text&add=test&fill_text=%5Bfiltered%5D'

Testing
-------

Tests have been for python 2.7 and python 3 using ``pytest``. The unit
tests do call the actual PurgoMalum production API in order to test
against potential API changes.

Before running tests make sure to install
`pytest <https://pypi.org/project/pytest/>`__,
`pytest-cov <https://pypi.org/project/pytest-cov/>`__,
`pytest-mock <https://pypi.org/project/pytest-mock/>`__, and
`mock <https://pypi.org/project/mock/>`__ (already included in
`requirements.txt <requirements.txt>`__).

To execute the tests and generate a code coverage report run the
following:

::

    pytest --cov-report term-missing --cov=purgo_malum/

You should see:

::

    Name                      Stmts   Miss  Cover   Missing
    -------------------------------------------------------
    purgo_malum/__init__.py       0      0   100%
    purgo_malum/client.py        54      0   100%
    -------------------------------------------------------
    TOTAL                        54      0   100%

Miscellaneous
-------------

This is my first offering to the open source community. If you see any
issues with this client library and/or potential improvements please let
me know and I will make the necessary updates.

Donation
--------

If this is helpful to you in any please consider a small donation.

|paypal|

.. |paypal| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GFDDW292XZVDJ&source=url
