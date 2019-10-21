Module purgo_malum.client
=========================
A client library for the the PurgoMalum REST API

https://www.purgomalum.com/index.html

Functions
---------

```python
build_url(text, request_type, add=None, fill_text=None, fill_char=None)
```
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
            asterisks (*), open and closed curly brackets ({ }), square brackets ([ ]) and
            parentheses ().  Maximum length of 20 characters. When not used, the default is an
            asterisk (*) fill.
        fill_char (string): Single character used to replace any words matching the profanity
            list. Fills designated character to length of word replaced. Accepts underscore (_)
            tilde (~), dash/hyphen (-), equal sign (=), pipe (|) and asterisk (*). When not used,
            the default is an asterisk (*) fill.
    
    Returns:
        string: The URL for the specified request.
                Ex: https://www.purgomalum.com/service/json?text=test+text&add=test&f&fill_char=%7C
    
    Raises:
        ValueError: If an input parameter is invalid

---
```python
contains_profanity(text, add=None)
```
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
        
---
```python
retrieve_filtered_text(text, add=None, fill_text=None, fill_char=None)
```
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
            asterisks (*), open and closed curly brackets ({ }), square brackets ([ ]) and
            parentheses (). Maximum length of 20 characters. When not used, the default is an
            asterisk (*) fill.
        fill_char (string): Single character used to replace any words matching the profanity
            list. Fills designated character to length of word replaced. Accepts underscore (_)
            tilde (~), dash/hyphen (-), equal sign (=), pipe (|) and asterisk (*). When not used,
            the default is an asterisk (*) fill.
    
    Returns:
        string: The filtered text
    
    Raises:
        ResultError: Client received an error from the server

---    
```python
retrieve_filtered_text_raw(text, request_type, add=None, fill_text=None, fill_char=None)
```    
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
            asterisks (*), open and closed curly brackets ({ }), square brackets ([ ]) and
            parentheses (). Maximum length of 20 characters. When not used, the default is an
            asterisk (*) fill.
        fill_char (string): Single character used to replace any words matching the profanity
            list. Fills designated character to length of word replaced. Accepts underscore (_)
            tilde (~), dash/hyphen (-), equal sign (=), pipe (|) and asterisk (*). When not used,
            the default is an asterisk (*) fill.
    
    Returns:
        string: The response returned by the PurgoMalum REST API
    
    Raises:
        ValueError: Invalid request_type was passed in

Classes
-------
```python
ResultError(*args, **kwargs)
```    
    Raised when the server returns an unexpected error.

    Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException