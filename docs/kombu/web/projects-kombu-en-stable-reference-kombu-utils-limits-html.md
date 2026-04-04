# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.limits.html

Title: kombu.utils.limits — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.limits.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.utils.limits.html).

Rate limiting - `kombu.utils.limits`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.limits.html#rate-limiting-kombu-utils-limits "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Token bucket implementation for rate limiting.

_class_ kombu.utils.limits.TokenBucket(_fill\_rate_, _capacity=1_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/limits.html#TokenBucket)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.limits.html#kombu.utils.limits.TokenBucket "Link to this definition")
Token Bucket Algorithm.

See also

`https`
//en.wikipedia.org/wiki/Token_Bucket Most of this code was stolen from an entry in the ASPN Python Cookbook:

`https`
//code.activestate.com/recipes/511490/

Warning:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.limits.html#warning "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

> Thread Safety: This implementation is not thread safe. Access to a TokenBucket instance should occur within the critical section of any multithreaded code.

add(_item_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/limits.html#TokenBucket.add)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.limits.html#kombu.utils.limits.TokenBucket.add "Link to this definition")can_consume(_tokens=1_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/limits.html#TokenBucket.can_consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.limits.html#kombu.utils.limits.TokenBucket.can_consume "Link to this definition")
Check if one or more tokens can be consumed.

Returns:
**bool** – from the bucket. If they can be consumed, a call will also consume the requested number of tokens from the bucket. Calls will only consume tokens (the number requested) or zero tokens – it will never consume a partial number of tokens.

Return type:
true if the number of tokens can be consumed

capacity _=1_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.limits.html#kombu.utils.limits.TokenBucket.capacity "Link to this definition")
Maximum number of tokens in the bucket.

clear_pending()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/limits.html#TokenBucket.clear_pending)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.limits.html#kombu.utils.limits.TokenBucket.clear_pending "Link to this definition")expected_time(_tokens=1_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/limits.html#TokenBucket.expected_time)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.limits.html#kombu.utils.limits.TokenBucket.expected_time "Link to this definition")
Return estimated time of token availability.

Returns:
**float**

Return type:
the time in seconds.

fill_rate _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.limits.html#kombu.utils.limits.TokenBucket.fill_rate "Link to this definition")
The rate in tokens/second that the bucket will be refilled.

pop()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/limits.html#TokenBucket.pop)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.limits.html#kombu.utils.limits.TokenBucket.pop "Link to this definition")timestamp _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.limits.html#kombu.utils.limits.TokenBucket.timestamp "Link to this definition")
Timestamp of the last time a token was taken out of the bucket.
