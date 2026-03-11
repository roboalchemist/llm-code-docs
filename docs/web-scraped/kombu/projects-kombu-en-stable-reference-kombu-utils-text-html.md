# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.text.html

Title: kombu.utils.text — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.text.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.utils.text.html).

Text utilitites - `kombu.utils.text`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.text.html#text-utilitites-kombu-utils-text "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Text Utilities.

kombu.utils.text.escape_regex(_p:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _white:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")=''_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/text.html#escape_regex)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.text.html#kombu.utils.text.escape_regex "Link to this definition")
Escape string for use within a regular expression.

kombu.utils.text.fmatch_best(_needle:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _haystack:Iterable[[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")]_, _min\_ratio:[float](https://docs.python.org/dev/library/functions.html#float "(in Python v3.15)")=0.6_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/text.html#fmatch_best)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.text.html#kombu.utils.text.fmatch_best "Link to this definition")
Fuzzy match - Find best match (scalar).

kombu.utils.text.fmatch_iter(_needle:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _haystack:[Iterable](https://docs.python.org/dev/library/typing.html#typing.Iterable "(in Python v3.15)")[[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")]_, _min\_ratio:[float](https://docs.python.org/dev/library/functions.html#float "(in Python v3.15)")=0.6_)→[Iterator](https://docs.python.org/dev/library/typing.html#typing.Iterator "(in Python v3.15)")[[tuple](https://docs.python.org/dev/library/stdtypes.html#tuple "(in Python v3.15)")[[float](https://docs.python.org/dev/library/functions.html#float "(in Python v3.15)"),[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")]][[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/text.html#fmatch_iter)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.text.html#kombu.utils.text.fmatch_iter "Link to this definition")
Fuzzy match: iteratively.

Yields:
**Tuple** (_of ratio and key._)

kombu.utils.text.version_string_as_tuple(_s:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_)→version_info_t[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/text.html#version_string_as_tuple)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.text.html#kombu.utils.text.version_string_as_tuple "Link to this definition")
Convert version string to version info tuple.
