# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html

Title: Pattern matching registry - kombu.matcher — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.matcher.html).

Pattern matching registry.

_exception_ kombu.matcher.MatcherNotInstalled[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/matcher.html#MatcherNotInstalled)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html#kombu.matcher.MatcherNotInstalled "Link to this definition")
Matcher not installed/found.

_class_ kombu.matcher.MatcherRegistry[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/matcher.html#MatcherRegistry)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html#kombu.matcher.MatcherRegistry "Link to this definition")
Pattern matching function registry.

_exception_ MatcherNotInstalled[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html#kombu.matcher.MatcherRegistry.MatcherNotInstalled "Link to this definition")
Matcher not installed/found.

match(_data:[bytes](https://docs.python.org/dev/library/stdtypes.html#bytes "(in Python v3.15)")_, _pattern:[bytes](https://docs.python.org/dev/library/stdtypes.html#bytes "(in Python v3.15)")_, _matcher:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_, _matcher\_kwargs:[dict](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")[[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)"),[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")]|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_)→[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/matcher.html#MatcherRegistry.match)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html#kombu.matcher.MatcherRegistry.match "Link to this definition")
Call the matcher.

matcher_pattern_first _=['pcre']_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html#kombu.matcher.MatcherRegistry.matcher_pattern_first "Link to this definition")register(_name:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _matcher:[Callable](https://docs.python.org/dev/library/typing.html#typing.Callable "(in Python v3.15)")[[[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)"),[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")],[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")]_)→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/matcher.html#MatcherRegistry.register)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html#kombu.matcher.MatcherRegistry.register "Link to this definition")
Add matcher by name to the registry.

unregister(_name:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_)→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/matcher.html#MatcherRegistry.unregister)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html#kombu.matcher.MatcherRegistry.unregister "Link to this definition")
Remove matcher by name from the registry.

kombu.matcher.match(_data:[bytes](https://docs.python.org/dev/library/stdtypes.html#bytes "(in Python v3.15)")_, _pattern:[bytes](https://docs.python.org/dev/library/stdtypes.html#bytes "(in Python v3.15)")_, _matcher:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_, _matcher\_kwargs:[dict](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")[[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)"),[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")]|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_)→[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html#kombu.matcher.match "Link to this definition")register(name,matcher):Register a new matching method.Parameters:
*   **name** – A convenient name for the matching method.

*   **matcher** – A method that will be passed data and pattern.

kombu.matcher.register(_name:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _matcher:[Callable](https://docs.python.org/dev/library/typing.html#typing.Callable "(in Python v3.15)")[[[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)"),[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")],[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")]_)→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html#kombu.matcher.register "Link to this definition")unregister(name):Unregister registered matching method.Parameters:
**name** – Registered matching method name.

kombu.matcher.register_glob()→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/matcher.html#register_glob)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html#kombu.matcher.register_glob "Link to this definition")
Register glob into default registry.

kombu.matcher.register_pcre()→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/matcher.html#register_pcre)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html#kombu.matcher.register_pcre "Link to this definition")
Register pcre into default registry.

kombu.matcher.registry _=<kombu.matcher.MatcherRegistry object>_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html#kombu.matcher.registry "Link to this definition")match(data,pattern,matcher=default_matcher,matcher_kwargs=None):
Match data by pattern using matcher.

Parameters:
*   **data** – The data that should be matched. Must be string.

*   **pattern** – The pattern that should be applied. Must be string.

Keyword Arguments:
*   **matcher** –

An optional string representing the matching method (for example, glob or pcre).

If `None` (default), then glob will be used.

*   **matcher_kwargs** – Additional keyword arguments that will be passed to the specified matcher.

Returns:
`True` if data matches pattern, `False` otherwise.

Raises:
[**MatcherNotInstalled**](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html#kombu.matcher.MatcherNotInstalled "kombu.matcher.MatcherNotInstalled") – If the matching method requested is not available.

kombu.matcher.unregister(_name:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_)→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html#kombu.matcher.unregister "Link to this definition")
Remove matcher by name from the registry.
