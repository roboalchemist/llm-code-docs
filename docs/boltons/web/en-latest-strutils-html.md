# Source: https://boltons.readthedocs.io/en/latest/strutils.html

Title: Text manipulation — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/strutils.html

Markdown Content:
`strutils` - Text manipulation[](https://boltons.readthedocs.io/en/latest/strutils.html#module-boltons.strutils "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

So much practical programming involves string manipulation, which Python readily accommodates. Still, there are dozens of basic and common capabilities missing from the standard library, several of them provided by `strutils`.

_class_ boltons.strutils.MultiReplace(_sub\_map_, _**kwargs_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#MultiReplace)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.MultiReplace "Link to this definition")
MultiReplace is a tool for doing multiple find/replace actions in one pass.

Given a mapping of values to be replaced it allows for all of the matching values to be replaced in a single pass which can save a lot of performance on very large strings. In addition to simple replace, it also allows for replacing based on regular expressions.

Keyword Arguments:

Parameters:
*   **regex** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Treat search keys as regular expressions [Default: False]

*   **flags** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – flags to pass to the regex engine during compile

Dictionary Usage:

from boltons import strutils
s = strutils.MultiReplace({
    'foo': 'zoo',
    'cat': 'hat',
    'bat': 'kraken'
})
new = s.sub('The foo bar cat ate a bat')
new == 'The zoo bar hat ate a kraken'

Iterable Usage:

from boltons import strutils
s = strutils.MultiReplace([
    ('foo', 'zoo'),
    ('cat', 'hat'),
    ('bat', 'kraken)'
])
new = s.sub('The foo bar cat ate a bat')
new == 'The zoo bar hat ate a kraken'

The constructor can be passed a dictionary or other mapping as well as an iterable of tuples. If given an iterable, the substitution will be run in the order the replacement values are specified in the iterable. This is also true if it is given an OrderedDict. If given a dictionary then the order will be non-deterministic:

>>> 'foo bar baz'.replace('foo', 'baz').replace('baz', 'bar')
'bar bar bar'
>>> m = MultiReplace({'foo': 'baz', 'baz': 'bar'})
>>> m.sub('foo bar baz')
'baz bar bar'

This is because the order of replacement can matter if you’re inserting something that might be replaced by a later substitution. Pay attention and if you need to rely on order then consider using a list of tuples instead of a dictionary.

sub(_text_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#MultiReplace.sub)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.MultiReplace.sub "Link to this definition")
Run substitutions on the input text.

Given an input string, run all substitutions given in the constructor.

boltons.strutils.a10n(_string_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#a10n)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.a10n "Link to this definition")
That thing where “internationalization” becomes “i18n”, what’s it called? Abbreviation? Oh wait, no: `a10n`. (It’s actually a form of [numeronym](http://en.wikipedia.org/wiki/Numeronym).)

>>> a10n('abbreviation')
'a10n'
>>> a10n('internationalization')
'i18n'
>>> a10n('')
''

boltons.strutils.args2cmd(_args_, _sep=''_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#args2cmd)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.args2cmd "Link to this definition")
Return a shell-escaped string version of _args_, separated by _sep_, using the same rules as the Microsoft C runtime.

>>> print(args2cmd(['aa', '[bb]', "cc'cc", 'dd"dd']))
aa [bb] cc'cc dd\"dd

As you can see, escaping is through backslashing and not quoting, and double quotes are the only special character. See the comment in the code for more details. Based on internal code from the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "(in Python v3.14)") module.

boltons.strutils.args2sh(_args_, _sep=''_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#args2sh)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.args2sh "Link to this definition")
Return a shell-escaped string version of _args_, separated by _sep_, based on the rules of sh, bash, and other shells in the Linux/BSD/MacOS ecosystem.

>>> print(args2sh(['aa', '[bb]', "cc'cc", 'dd"dd']))
aa '[bb]' 'cc'"'"'cc' 'dd"dd'

As you can see, arguments with no special characters are not escaped, arguments with special characters are quoted with single quotes, and single quotes themselves are quoted with double quotes. Double quotes are handled like any other special character.

Based on code from the [`pipes`](https://docs.python.org/3/library/pipes.html#module-pipes "(in Python v3.14)")/[`shlex`](https://docs.python.org/3/library/shlex.html#module-shlex "(in Python v3.14)") modules. Also note that [`shlex`](https://docs.python.org/3/library/shlex.html#module-shlex "(in Python v3.14)") and [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "(in Python v3.14)") have functions to split and parse strings escaped in this manner.

boltons.strutils.asciify(_text_, _ignore=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#asciify)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.asciify "Link to this definition")
Converts a unicode or bytestring, _text_, into a bytestring with just ascii characters. Performs basic deaccenting for all you Europhiles out there.

Also, a gentle reminder that this is a **utility**, primarily meant for slugification. Whenever possible, make your application work **with** unicode, not against it.

Parameters:
*   **text** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The string to be asciified.

*   **ignore** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Configures final encoding to ignore remaining unasciified string instead of replacing it.

>>> asciify('Beyoncé') == b'Beyonce'
True

boltons.strutils.bytes2human(_nbytes_, _ndigits=0_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#bytes2human)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.bytes2human "Link to this definition")
Turns an integer value of _nbytes_ into a human readable format. Set _ndigits_ to control how many digits after the decimal point should be shown (default `0`).

>>> bytes2human(128991)
'126K'
>>> bytes2human(100001221)
'95M'
>>> bytes2human(0, 2)
'0.00B'

boltons.strutils.camel2under(_camel\_string_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#camel2under)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.camel2under "Link to this definition")
Converts a camelcased string to underscores. Useful for turning a class name into a function name.

>>> camel2under('BasicParseTest')
'basic_parse_test'

boltons.strutils.cardinalize(_unit\_noun_, _count_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#cardinalize)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.cardinalize "Link to this definition")
Conditionally pluralizes a singular word _unit\_noun_ if _count_ is not one, preserving case when possible.

>>> vowels = 'aeiou'
>>> print(len(vowels), cardinalize('vowel', len(vowels)))
5 vowels
>>> print(3, cardinalize('Wish', 3))
3 Wishes

boltons.strutils.complement_int_list(_range\_string_, _range\_start=0_, _range\_end=None_, _delim=','_, _range\_delim='-'_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#complement_int_list)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.complement_int_list "Link to this definition")
Returns range string that is the complement of the one provided as _range\_string_ parameter.

These range strings are of the kind produce by [`format_int_list()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.format_int_list "boltons.strutils.format_int_list"), and parseable by [`parse_int_list()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.parse_int_list "boltons.strutils.parse_int_list").

Parameters:
*   **range_string** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – String of comma separated positive integers or ranges (e.g. ‘1,2,4-6,8’). Typical of a custom page range string used in printer dialogs.

*   **range_start** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – A positive integer from which to start the resulting range. Value is inclusive. Defaults to `0`.

*   **range_end** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – A positive integer from which the produced range is stopped. Value is exclusive. Defaults to the maximum value found in the provided `range_string`.

*   **delim** (_char_) – Defaults to ‘,’. Separates integers and contiguous ranges of integers.

*   **range_delim** (_char_) – Defaults to ‘-’. Indicates a contiguous range of integers.

>>> complement_int_list('1,3,5-8,10-11,15')
'0,2,4,9,12-14'

>>> complement_int_list('1,3,5-8,10-11,15', range_start=0)
'0,2,4,9,12-14'

>>> complement_int_list('1,3,5-8,10-11,15', range_start=1)
'2,4,9,12-14'

>>> complement_int_list('1,3,5-8,10-11,15', range_start=2)
'2,4,9,12-14'

>>> complement_int_list('1,3,5-8,10-11,15', range_start=3)
'4,9,12-14'

>>> complement_int_list('1,3,5-8,10-11,15', range_end=15)
'0,2,4,9,12-14'

>>> complement_int_list('1,3,5-8,10-11,15', range_end=14)
'0,2,4,9,12-13'

>>> complement_int_list('1,3,5-8,10-11,15', range_end=13)
'0,2,4,9,12'

>>> complement_int_list('1,3,5-8,10-11,15', range_end=20)
'0,2,4,9,12-14,16-19'

>>> complement_int_list('1,3,5-8,10-11,15', range_end=0)
''

>>> complement_int_list('1,3,5-8,10-11,15', range_start=-1)
'0,2,4,9,12-14'

>>> complement_int_list('1,3,5-8,10-11,15', range_end=-1)
''

>>> complement_int_list('1,3,5-8', range_start=1, range_end=1)
''

>>> complement_int_list('1,3,5-8', range_start=2, range_end=2)
''

>>> complement_int_list('1,3,5-8', range_start=2, range_end=3)
'2'

>>> complement_int_list('1,3,5-8', range_start=-10, range_end=-5)
''

>>> complement_int_list('1,3,5-8', range_start=20, range_end=10)
''

>>> complement_int_list('')
''

boltons.strutils.escape_shell_args(_args_, _sep=''_, _style=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#escape_shell_args)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.escape_shell_args "Link to this definition")
Returns an escaped version of each string in _args_, according to _style_.

Parameters:
*   **args** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A list of arguments to escape and join together

*   **sep** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The separator used to join the escaped arguments.

*   **style** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The style of escaping to use. Can be one of `cmd` or `sh`, geared toward Windows and Linux/BSD/etc., respectively. If _style_ is `None`, then it is picked according to the system platform.

See [`args2cmd()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.args2cmd "boltons.strutils.args2cmd") and [`args2sh()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.args2sh "boltons.strutils.args2sh") for details and example output for each style.

boltons.strutils.find_hashtags(_string_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#find_hashtags)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.find_hashtags "Link to this definition")
Finds and returns all hashtags in a string, with the hashmark removed. Supports full-width hashmarks for Asian languages and does not false-positive on URL anchors.

>>> find_hashtags('#atag http://asite/#ananchor')
['atag']

`find_hashtags` also works with unicode hashtags.

boltons.strutils.format_int_list(_int\_list_, _delim=','_, _range\_delim='-'_, _delim\_space=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#format_int_list)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.format_int_list "Link to this definition")
Returns a sorted range string from a list of positive integers (_int\_list_). Contiguous ranges of integers are collapsed to min and max values. Reverse of [`parse_int_list()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.parse_int_list "boltons.strutils.parse_int_list").

Parameters:
*   **int_list** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – List of positive integers to be converted into a range string (e.g. [1,2,4,5,6,8]).

*   **delim** (_char_) – Defaults to ‘,’. Separates integers and contiguous ranges of integers.

*   **range_delim** (_char_) – Defaults to ‘-’. Indicates a contiguous range of integers.

*   **delim_space** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Defaults to `False`. If `True`, adds a space after all _delim_ characters.

>>> format_int_list([1,3,5,6,7,8,10,11,15])
'1,3,5-8,10-11,15'

boltons.strutils.gunzip_bytes(_bytestring_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#gunzip_bytes)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.gunzip_bytes "Link to this definition")
The [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "(in Python v3.14)") module is great if you have a file or file-like object, but what if you just have bytes. StringIO is one possibility, but it’s often faster, easier, and simpler to just use this one-liner. Use this tried-and-true utility function to decompress gzip from bytes.

>>> gunzip_bytes(_EMPTY_GZIP_BYTES) == b''
True
>>> gunzip_bytes(_NON_EMPTY_GZIP_BYTES).rstrip() == b'bytesahoy!'
True

boltons.strutils.gzip_bytes(_bytestring_, _level=6_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#gzip_bytes)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.gzip_bytes "Link to this definition")
Turn some bytes into some compressed bytes.

>>> len(gzip_bytes(b'a' * 10000))
46

Parameters:
*   **bytestring** ([_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")) – Bytes to be compressed

*   **level** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – An integer, 1-9, controlling the speed/compression. 1 is fastest, least compressed, 9 is slowest, but most compressed.

Note that all levels of gzip are pretty fast these days, though it’s not really a competitor in compression, at any level.

boltons.strutils.html2text(_html_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#html2text)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.html2text "Link to this definition")
Strips tags from HTML text, returning markup-free text. Also, does a best effort replacement of entities like “&nbsp;”

>>> r = html2text(u'<a href="#">Test &amp;<em>(Δ&#x03b7;&#956;&#x03CE;)</em></a>')
>>> r == u'Test &(Δημώ)'
True

boltons.strutils.human_readable_list(_items:[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]_, _delimiter:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")=','_, _conjunction:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='and'_, _*_, _oxford:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=True_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#human_readable_list)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.human_readable_list "Link to this definition")
Given a list of strings, return a human readable string with appropriate delimiters and the conjunction word.

Parameters:
*   **items** – The list of strings to join.

*   **delimiter** (_optional_) – The delimiter to use between items.

*   **conjunction** (_optional_) – The word to use before the last item.

*   **oxford** (_optional_) – Whether to use the Oxford comma/delimiter before the conjunction in lists of 3+ items.

Returns:
The human readable string.

Return type:
[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

boltons.strutils.indent(_text_, _margin_, _newline='\n'_, _key=<class'bool'>_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#indent)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.indent "Link to this definition")
The missing counterpart to the built-in [`textwrap.dedent()`](https://docs.python.org/3/library/textwrap.html#textwrap.dedent "(in Python v3.14)").

Parameters:
*   **text** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The text to indent.

*   **margin** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The string to prepend to each line.

*   **newline** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The newline used to rejoin the lines (default: `\n`)

*   **key** (_callable_) – Called on each line to determine whether to indent it. Default: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"), to ensure that empty lines do not get whitespace added.

boltons.strutils.int_ranges_from_int_list(_range\_string_, _delim=','_, _range\_delim='-'_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#int_ranges_from_int_list)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.int_ranges_from_int_list "Link to this definition")
Transform a string of ranges (_range\_string_) into a tuple of tuples.

Parameters:
*   **range_string** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – String of comma separated positive integers or ranges (e.g. ‘1,2,4-6,8’). Typical of a custom page range string used in printer dialogs.

*   **delim** (_char_) – Defaults to ‘,’. Separates integers and contiguous ranges of integers.

*   **range_delim** (_char_) – Defaults to ‘-’. Indicates a contiguous range of integers.

>>> int_ranges_from_int_list('1,3,5-8,10-11,15')
((1, 1), (3, 3), (5, 8), (10, 11), (15, 15))

>>> int_ranges_from_int_list('1')
((1, 1),)

>>> int_ranges_from_int_list('')
()

boltons.strutils.is_ascii(_text_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#is_ascii)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.is_ascii "Link to this definition")
Check if a string or bytestring, _text_, is composed of ascii characters only. Raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") if argument is not text.

Parameters:
**text** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The string to be checked.

>>> is_ascii('Beyoncé')
False
>>> is_ascii('Beyonce')
True

boltons.strutils.is_uuid(_obj_, _version=4_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#is_uuid)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.is_uuid "Link to this definition")
Check the argument is either a valid UUID object or string.

Parameters:
*   **obj** ([_object_](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")) – The test target. Strings and UUID objects supported.

*   **version** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The target UUID version, set to 0 to skip version check.

>>> is_uuid('e682ccca-5a4c-4ef2-9711-73f9ad1e15ea')
True
>>> is_uuid('0221f0d9-d4b9-11e5-a478-10ddb1c2feb9')
False
>>> is_uuid('0221f0d9-d4b9-11e5-a478-10ddb1c2feb9', version=1)
True

boltons.strutils.iter_splitlines(_text_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#iter_splitlines)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.iter_splitlines "Link to this definition")
Like [`str.splitlines()`](https://docs.python.org/3/library/stdtypes.html#str.splitlines "(in Python v3.14)"), but returns an iterator of lines instead of a list. Also similar to `file.next()`, as that also lazily reads and yields lines from a file.

This function works with a variety of line endings, but as always, be careful when mixing line endings within a file.

>>> list(iter_splitlines('\nhi\nbye\n'))
['', 'hi', 'bye', '']
>>> list(iter_splitlines('\r\nhi\rbye\r\n'))
['', 'hi', 'bye', '']
>>> list(iter_splitlines(''))
[]

boltons.strutils.multi_replace(_text_, _sub\_map_, _**kwargs_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#multi_replace)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.multi_replace "Link to this definition")
Shortcut function to invoke MultiReplace in a single call.

Example Usage:

from boltons.strutils import multi_replace
new = multi_replace(
    'The foo bar cat ate a bat',
    {'foo': 'zoo', 'cat': 'hat', 'bat': 'kraken'}
)
new == 'The zoo bar hat ate a kraken'

boltons.strutils.ordinalize(_number_, _ext\_only=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#ordinalize)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.ordinalize "Link to this definition")
Turns _number_ into its cardinal form, i.e., 1st, 2nd, 3rd, 4th, etc. If the last character isn’t a digit, it returns the string value unchanged.

Parameters:
*   **number** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")_or_[_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Number to be cardinalized.

*   **ext_only** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether to return only the suffix. Default `False`.

>>> print(ordinalize(1))
1st
>>> print(ordinalize(3694839230))
3694839230th
>>> print(ordinalize('hi'))
hi
>>> print(ordinalize(1515))
1515th

boltons.strutils.parse_int_list(_range\_string_, _delim=','_, _range\_delim='-'_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#parse_int_list)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.parse_int_list "Link to this definition")
Returns a sorted list of positive integers based on _range\_string_. Reverse of [`format_int_list()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.format_int_list "boltons.strutils.format_int_list").

Parameters:
*   **range_string** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – String of comma separated positive integers or ranges (e.g. ‘1,2,4-6,8’). Typical of a custom page range string used in printer dialogs.

*   **delim** (_char_) – Defaults to ‘,’. Separates integers and contiguous ranges of integers.

*   **range_delim** (_char_) – Defaults to ‘-’. Indicates a contiguous range of integers.

>>> parse_int_list('1,3,5-8,10-11,15')
[1, 3, 5, 6, 7, 8, 10, 11, 15]

boltons.strutils.pluralize(_word_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#pluralize)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.pluralize "Link to this definition")
Semi-intelligently converts an English _word_ from singular form to plural, preserving case pattern.

>>> pluralize('friend')
'friends'
>>> pluralize('enemy')
'enemies'
>>> pluralize('Sheep')
'Sheep'

boltons.strutils.removeprefix(_text:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _prefix:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#removeprefix)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.removeprefix "Link to this definition")
Remove prefix from start of text if present.

Backport of str.removeprefix for Python versions less than 3.9.

Parameters:
*   **text** – A string to remove the prefix from.

*   **prefix** – The string to remove from the beginning of text.

boltons.strutils.singularize(_word_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#singularize)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.singularize "Link to this definition")
Semi-intelligently converts an English plural _word_ to its singular form, preserving case pattern.

>>> singularize('chances')
'chance'
>>> singularize('Activities')
'Activity'
>>> singularize('Glasses')
'Glass'
>>> singularize('FEET')
'FOOT'

boltons.strutils.slugify(_text_, _delim='\_'_, _lower=True_, _ascii=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#slugify)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.slugify "Link to this definition")
A basic function that turns text full of scary characters (i.e., punctuation and whitespace), into a relatively safe lowercased string separated only by the delimiter specified by _delim_, which defaults to `_`.

The _ascii_ convenience flag will [`asciify()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.asciify "boltons.strutils.asciify") the slug if you require ascii-only slugs.

>>> slugify('First post! Hi!!!!~1 ')
'first_post_hi_1'

>>> slugify("Kurt Gödel's pretty cool.", ascii=True) ==         b'kurt_goedel_s_pretty_cool'
True

boltons.strutils.split_punct_ws(_text_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#split_punct_ws)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.split_punct_ws "Link to this definition")
While [`str.split()`](https://docs.python.org/3/library/stdtypes.html#str.split "(in Python v3.14)") will split on whitespace, [`split_punct_ws()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.split_punct_ws "boltons.strutils.split_punct_ws") will split on punctuation and whitespace. This used internally by [`slugify()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.slugify "boltons.strutils.slugify"), above.

>>> split_punct_ws('First post! Hi!!!!~1 ')
['First', 'post', 'Hi', '1']

boltons.strutils.strip_ansi(_text_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#strip_ansi)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.strip_ansi "Link to this definition")
Strips ANSI escape codes from _text_. Useful for the occasional time when a log or redirected output accidentally captures console color codes and the like.

>>> strip_ansi('[0m[1;36mart[46;34m')
'art'

Supports str, bytes and bytearray content as input. Returns the same type as the input.

There’s a lot of ANSI art available for testing on [sixteencolors.net](http://sixteencolors.net/). This function does not interpret or render ANSI art, but you can do so with [ansi2img](http://www.bedroomlan.org/projects/ansi2img) or [escapes.js](https://github.com/atdt/escapes.js).

boltons.strutils.under2camel(_under\_string_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#under2camel)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.under2camel "Link to this definition")
Converts an underscored string to camelcased. Useful for turning a function name into a class name.

>>> under2camel('complex_tokenizer')
'ComplexTokenizer'

boltons.strutils.unit_len(_sized\_iterable_, _unit\_noun='item'_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#unit_len)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.unit_len "Link to this definition")
Returns a plain-English description of an iterable’s [`len()`](https://docs.python.org/3/library/functions.html#len "(in Python v3.14)"), conditionally pluralized with [`cardinalize()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.cardinalize "boltons.strutils.cardinalize"), detailed below.

>>> print(unit_len(range(10), 'number'))
10 numbers
>>> print(unit_len('aeiou', 'vowel'))
5 vowels
>>> print(unit_len([], 'worry'))
No worries

boltons.strutils.unwrap_text(_text_, _ending='\n\n'_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/strutils.html#unwrap_text)[](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.unwrap_text "Link to this definition")
Unwrap text, the natural complement to [`textwrap.wrap()`](https://docs.python.org/3/library/textwrap.html#textwrap.wrap "(in Python v3.14)").

>>> text = "Short \n lines \nwrapped\nsmall.\n\nAnother\nparagraph."
>>> unwrap_text(text)
'Short lines wrapped small.\n\nAnother paragraph.'

Parameters:
*   **text** – A string to unwrap.

*   **ending** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The string to join all unwrapped paragraphs by. Pass `None` to get the list. Defaults to ‘nn’ for compatibility with Markdown and RST.
