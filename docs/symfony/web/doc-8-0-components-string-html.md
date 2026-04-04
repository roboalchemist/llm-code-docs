# Source: https://symfony.com/doc/8.0/components/string.html

Title: Creating and Manipulating Strings (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/components/string.html

Markdown Content:
Creating and Manipulating Strings (Symfony Docs)
===============

[Skip to content](https://symfony.com/doc/8.0/components/string.html#main-content)

[Symfony Hub](https://symfony.com/doc/8.0/components/string.html# "Toggle Symfony menu")[SF H](https://symfony.com/doc/8.0/components/string.html# "Toggle Symfony menu")

[![Image 2](https://connect.symfony.com/uploads/sln/9dcfe3b7-4ac7-4fd7-bdaa-d690f48b40da/48b70252-5e84-4200-ab44-fed8cd091b60.png) Learn Symfony today](https://symfony.com/book)[![Image 3](https://connect.symfony.com/uploads/sln/9dcfe3b7-4ac7-4fd7-bdaa-d690f48b40da/48b70252-5e84-4200-ab44-fed8cd091b60.png) "Symfony: The Fast Track", a new book to learn Symfony](https://symfony.com/book)[![Image 4](https://connect.symfony.com/uploads/sln/9dcfe3b7-4ac7-4fd7-bdaa-d690f48b40da/48b70252-5e84-4200-ab44-fed8cd091b60.png) "Symfony: The Fast Track", a new book to learn Symfony](https://symfony.com/book)

[](https://symfony.com/doc/8.0/components/string.html# "Search")

[](https://symfony.com/doc/8.0/components/string.html# "Search")Search

[Connect](https://symfony.com/connect/login?target=https://symfony.com/doc/current/string.html)

![Image 5: SensioLabs](https://connect.symfony.com/assets/images/sln-v2/sensiolabs-9Agct9D.png)
SensioLabs is the creator of Symfony and plays a pivotal role in supporting its growth. With a passionate team pushing the boundaries of PHP, SensioLabs helps organizations get the most out of Symfony through quality, high-performance, software vendor-level training and consulting services.

* [International](https://sensiolabs.com/en)
* [France](https://sensiolabs.com/fr)

In the Spotlight
----------------

[![Image 6: SymfonyInsight](https://connect.symfony.com/assets/images/sln-v2/symfonyinsight-HwpmiQ3.png)](https://insight.symfony.com/)

[![Image 7: Blackfire](https://connect.symfony.com/assets/images/sln-v2/blackfire-ca6NfRp.png)](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)

Open Source
-----------

* [Symfony - Web framework](https://symfony.com/)
* [Twig - Templating](https://twig.symfony.com/)
* [PHP Polyfills](https://github.com/symfony/polyfill)

Products
--------

* [Insight: PHP Quality](https://insight.symfony.com/)
* [Blackfire: Web App performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)
* [SymfonyCloud powered by Upsun](https://symfony.com/cloud)

Solutions & Services
--------------------

* [Training](https://training.sensiolabs.com/)
* [Certification](https://certification.symfony.com/)
* [Technical Solutions](https://sensiolabs.com/solutions)
* [SensioLabs University](https://university.sensiolabs.com/)
* [Experts](https://expert.sensiolabs.com/)

Community
---------

* [Community](https://connect.symfony.com/)
* [Conferences](https://live.symfony.com/)
* [Videos](https://www.youtube.com/symfonytv)
* [Partners](https://network.sensiolabs.com/en/partenaires)

Blogs
-----

[Symfony](https://symfony.com/blog/), [SensioLabs](https://blog.sensiolabs.com/), [Insight](https://blog.insight.symfony.com/), and [Blackfire](https://blog.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler).

[](https://symfony.com/)

Close

* About

  * [What is Symfony?](https://symfony.com/what-is-symfony)
  * [Community](https://symfony.com/community)
  * [News](https://symfony.com/blog/)
  * [Contributing](https://symfony.com/doc/current/contributing/index.html)
  * [Support](https://symfony.com/support)

* Documentation

  * [Symfony Docs](https://symfony.com/doc)
  * [Symfony Book](https://symfony.com/book)
  * [Screencasts](https://symfonycasts.com/)
  * [Symfony Bundles](https://symfony.com/bundles)
  * [Symfony Cloud](https://symfony.com/doc/cloud/)
  * [Training](https://sensiolabs.com/training?utm_source=symfony&utm_medium=symfony_submenu&utm_campaign=permanent_referral)

* Services

  * [Upsun for Symfony](https://symfony.com/cloud/)Best platform to deploy Symfony apps
  * [SymfonyInsight](https://insight.symfony.com/)Automatic quality checks for your apps
  * [Symfony Certification](https://certification.symfony.com/)Prove your knowledge and boost your career
  * [SensioLabs](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_submenu&utm_campaign=permanent_referral)Professional services to help you with Symfony
  * [Blackfire](https://www.blackfire.io/?utm_source=symfony&utm_medium=symfonycom_footer&utm_campaign=profiler)Profile and monitor performance of your apps

* Other
* [Blog](https://symfony.com/blog/)
* [Download](https://symfony.com/download)

sponsored by[](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_sponsoredby&utm_campaign=permanent_referral "SensioLabs, PHP services and software solutions for enterprise and community.")

[SymfonyDay Montreal 2026](https://live.symfony.com/2026-montreal)

June 4, 2026

+20 talks and workshops

Register now

1. [Home](https://symfony.com/)
2. [Documentation](https://symfony.com/doc)
3. Creating and Manipulating Strings

 Search Symfony Docs

Version:

Table of Contents

* [What is a String?](https://symfony.com/doc/8.0/components/string.html#what-is-a-string)
* [Usage](https://symfony.com/doc/8.0/components/string.html#usage)
* [Method Reference](https://symfony.com/doc/8.0/components/string.html#method-reference)
  * [Methods to Create String Objects](https://symfony.com/doc/8.0/components/string.html#methods-to-create-string-objects)
  * [Methods to Transform String Objects](https://symfony.com/doc/8.0/components/string.html#methods-to-transform-string-objects)
  * [Methods Related to Length and Whitespace Characters](https://symfony.com/doc/8.0/components/string.html#methods-related-to-length-and-whitespace-characters)
  * [Methods to Change Case](https://symfony.com/doc/8.0/components/string.html#methods-to-change-case)
  * [Methods to Append and Prepend](https://symfony.com/doc/8.0/components/string.html#methods-to-append-and-prepend)
  * [Methods to Pad and Trim](https://symfony.com/doc/8.0/components/string.html#methods-to-pad-and-trim)
  * [Methods to Search and Replace](https://symfony.com/doc/8.0/components/string.html#methods-to-search-and-replace)
  * [Methods to Join, Split, Truncate and Reverse](https://symfony.com/doc/8.0/components/string.html#methods-to-join-split-truncate-and-reverse)
  * [Methods Added by ByteString](https://symfony.com/doc/8.0/components/string.html#methods-added-by-bytestring)
  * [Methods Added by CodePointString and UnicodeString](https://symfony.com/doc/8.0/components/string.html#methods-added-by-codepointstring-and-unicodestring)

* [Lazy-loaded Strings](https://symfony.com/doc/8.0/components/string.html#lazy-loaded-strings)
* [Working with Emojis](https://symfony.com/doc/8.0/components/string.html#working-with-emojis)
* [Slugger](https://symfony.com/doc/8.0/components/string.html#slugger)
  * [Slug Emojis](https://symfony.com/doc/8.0/components/string.html#slug-emojis)

* [Inflector](https://symfony.com/doc/8.0/components/string.html#inflector)

Creating and Manipulating Strings
=================================

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/string.rst)

Symfony provides an object-oriented API to work with Unicode strings (as bytes, code points and grapheme clusters). This API is available via the String component, which you must first install in your application:

 Copy

1`$ composer require symfony/string`

Note

If you install this component outside of a Symfony application, you must require the `vendor/autoload.php` file in your code to enable the class autoloading mechanism provided by Composer. Read [this article](https://symfony.com/doc/8.0/components/components/using_components.html) for more details.

[What is a String?](https://symfony.com/doc/8.0/components/string.html#what-is-a-string "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------

You can skip this section if you already know what a _"code point"_ or a _"grapheme cluster"_ are in the context of handling strings. Otherwise, read this section to learn about the terminology used by this component.

Languages like English require a very limited set of characters and symbols to display any content. Each string is a series of characters (letters or symbols) and they can be encoded even with the most limited standards (e.g. [ASCII](https://en.wikipedia.org/wiki/ASCII)).

However, other languages require thousands of symbols to display their contents. They need complex encoding standards such as [Unicode](https://en.wikipedia.org/wiki/Unicode) and concepts like "character" no longer make sense. Instead, you have to deal with these terms:

* [Code points](https://en.wikipedia.org/wiki/Code_point): they are the atomic units of information. A string is a series of code points. Each code point is a number whose meaning is given by the [Unicode](https://en.wikipedia.org/wiki/Unicode) standard. For example, the English letter `A` is the `U+0041` code point and the Japanese _kana_`の` is the `U+306E` code point.
* [Grapheme clusters](https://en.wikipedia.org/wiki/Grapheme): they are a sequence of one or more code points which are displayed as a single graphical unit. For example, the Spanish letter `ñ` is a grapheme cluster that contains two code points: `U+006E` = `n` (_"latin small letter N"_) + `U+0303` = `◌̃` (_"combining tilde"_).
* Bytes: they are the actual information stored for the string contents. Each code point can require one or more bytes of storage depending on the standard being used (UTF-8, UTF-16, etc.).

The following image displays the bytes, code points and grapheme clusters for the same word written in English (`hello`) and Hindi (`नमस्ते`):

![Image 8: Each letter in "hello" is made up of one byte, one code point and one grapheme cluster. In the Hindi translation, the first two letters ("नम") take up three bytes, one code point and one grapheme cluster. The last letters ("स्ते") each take up six bytes, two code points and one grapheme cluster.](https://symfony.com/doc/8.0/_images/bytes-points-graphemes.png)

[Usage](https://symfony.com/doc/8.0/components/string.html#usage "Permalink to this headline")
----------------------------------------------------------------------------------------------

Create a new object of type [ByteString](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/String/ByteString.php "Symfony\Component\String\ByteString"), [CodePointString](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/String/CodePointString.php "Symfony\Component\String\CodePointString") or [UnicodeString](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/String/UnicodeString.php "Symfony\Component\String\UnicodeString"), pass the string contents as their arguments and then use the object-oriented API to work with those strings:

1
2
3
4
5
6
7
8
9
10
11
12

```
use Symfony\Component\String\UnicodeString;

$text = (new UnicodeString('This is a déjà-vu situation.'))
    ->trimEnd('.')
    ->replace('déjà-vu', 'jamais-vu')
    ->append('!');
// $text = 'This is a jamais-vu situation!'

$content = new UnicodeString('नमस्ते दुनिया');
if ($content->ignoreCase()->startsWith('नमस्ते')) {
    // ...
}
```

[Method Reference](https://symfony.com/doc/8.0/components/string.html#method-reference "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------

### [Methods to Create String Objects](https://symfony.com/doc/8.0/components/string.html#methods-to-create-string-objects "Permalink to this headline")

First, you can create objects prepared to store strings as bytes, code points and grapheme clusters with the following classes:

1
2
3
4
5
6
7
8

```
use Symfony\Component\String\ByteString;
use Symfony\Component\String\CodePointString;
use Symfony\Component\String\UnicodeString;

$foo = new ByteString('hello');
$bar = new CodePointString('hello');
// UnicodeString is the most commonly used class
$baz = new UnicodeString('hello');
```

Use the `wrap()` static method to instantiate more than one string object:

1
2
3
4
5
6
7

```
$contents = ByteString::wrap(['hello', 'world']);        // $contents = ByteString[]
$contents = UnicodeString::wrap(['I', '❤️', 'Symfony']); // $contents = UnicodeString[]

// use the unwrap method to make the inverse conversion
$contents = UnicodeString::unwrap([
    new UnicodeString('hello'), new UnicodeString('world'),
]); // $contents = ['hello', 'world']
```

If you work with lots of String objects, consider using the shortcut functions to make your code more concise:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22

```
// the b() function creates byte strings
use function Symfony\Component\String\b;

// both lines are equivalent
$foo = new ByteString('hello');
$foo = b('hello');

// the u() function creates Unicode strings
use function Symfony\Component\String\u;

// both lines are equivalent
$foo = new UnicodeString('hello');
$foo = u('hello');

// the s() function creates a byte string or Unicode string
// depending on the given contents
use function Symfony\Component\String\s;

// creates a ByteString object
$foo = s("\xfe\xff");
// creates a UnicodeString object
$foo = s('अनुच्छेद');
```

There are also some specialized constructors:

1
2
3
4
5
6
7
8
9
10

```
// ByteString can create a random string of the given length
$foo = ByteString::fromRandom(12);
// by default, random strings use base58 characters; you can set
// the characters to use with the second optional argument
$foo = ByteString::fromRandom(6, 'AEIOU0123456789');
$foo = ByteString::fromRandom(10, 'qwertyuiop');

// CodePointString and UnicodeString can create a string from code points
$foo = UnicodeString::fromCodePoints(0x928, 0x92E, 0x938, 0x94D, 0x924, 0x947);
// equivalent to: $foo = new UnicodeString('नमस्ते');
```

### [Methods to Transform String Objects](https://symfony.com/doc/8.0/components/string.html#methods-to-transform-string-objects "Permalink to this headline")

Each string object can be transformed into the other two types of objects:

1
2
3
4
5
6
7
8

```
$foo = ByteString::fromRandom(12)->toCodePointString();
$foo = (new CodePointString('hello'))->toUnicodeString();
$foo = UnicodeString::fromCodePoints(0x68, 0x65, 0x6C, 0x6C, 0x6F)->toByteString();

// the optional $toEncoding argument defines the encoding of the target string
$foo = (new CodePointString('hello'))->toByteString('Windows-1252');
// the optional $fromEncoding argument defines the encoding of the original string
$foo = (new ByteString('さよなら'))->toCodePointString('ISO-2022-JP');
```

If the conversion is not possible for any reason, you'll get an [InvalidArgumentException](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/String/Exception/InvalidArgumentException.php "Symfony\Component\String\Exception\InvalidArgumentException").

There is also a method to get the bytes stored at some position:

1
2
3
4
5
6
7

```
// ('नमस्ते' bytes = [224, 164, 168, 224, 164, 174, 224, 164, 184,
//                  224, 165, 141, 224, 164, 164, 224, 165, 135])
b('नमस्ते')->bytesAt(0);   // [224]
u('नमस्ते')->bytesAt(0);   // [224, 164, 168]

b('नमस्ते')->bytesAt(1);   // [164]
u('नमस्ते')->bytesAt(1);   // [224, 164, 174]
```

### [Methods Related to Length and Whitespace Characters](https://symfony.com/doc/8.0/components/string.html#methods-related-to-length-and-whitespace-characters "Permalink to this headline")

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28

```
// returns the number of graphemes, code points or bytes of the given string
$word = 'नमस्ते';
(new ByteString($word))->length();      // 18 (bytes)
(new CodePointString($word))->length(); // 6 (code points)
(new UnicodeString($word))->length();   // 4 (graphemes)

// some symbols require double the width of others to represent them when using
// a monospaced font (e.g. in a console). This method returns the total width
// needed to represent the entire word
$word = 'नमस्ते';
(new ByteString($word))->width();      // 18
(new CodePointString($word))->width(); // 4
(new UnicodeString($word))->width();   // 4
// if the text contains multiple lines, it returns the max width of all lines
$text = "<<<END
This is a
multiline text
END";
u($text)->width(); // 14

// only returns TRUE if the string is exactly an empty string (not even whitespace)
u('hello world')->isEmpty();  // false
u('     ')->isEmpty();        // false
u('')->isEmpty();             // true

// removes all whitespace (' \n\r\t\x0C') from the start and end of the string and
// replaces two or more consecutive whitespace characters with a single space (' ') character
u("  \n\n   hello \t   \n\r   world \n    \n")->collapseWhitespace(); // 'hello world'
```

### [Methods to Change Case](https://symfony.com/doc/8.0/components/string.html#methods-to-change-case "Permalink to this headline")

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36

```
// changes all graphemes/code points to lower case
u('FOO Bar Brİan')->lower();  // 'foo bar bri̇an'
// changes all graphemes/code points to lower case according to locale-specific case mappings
u('FOO Bar Brİan')->localeLower('en');  // 'foo bar bri̇an'
u('FOO Bar Brİan')->localeLower('lt');  // 'foo bar bri̇̇an'

// when dealing with different languages, uppercase/lowercase is not enough
// there are three cases (lower, upper, title), some characters have no case,
// case is context-sensitive and locale-sensitive, etc.
// this method returns a string that you can use in case-insensitive comparisons
u('FOO Bar')->folded();             // 'foo bar'
u('Die O\'Brian Straße')->folded(); // "die o'brian strasse"

// changes all graphemes/code points to upper case
u('foo BAR bάz')->upper(); // 'FOO BAR BΆZ'
// changes all graphemes/code points to upper case according to locale-specific case mappings
u('foo BAR bάz')->localeUpper('en'); // 'FOO BAR BΆZ'
u('foo BAR bάz')->localeUpper('el'); // 'FOO BAR BAZ'

// changes all graphemes/code points to "title case"
u('foo ijssel')->title();               // 'Foo ijssel'
u('foo ijssel')->title(allWords: true); // 'Foo Ijssel'
// changes all graphemes/code points to "title case" according to locale-specific case mappings
u('foo ijssel')->localeTitle('en'); // 'Foo ijssel'
u('foo ijssel')->localeTitle('nl'); // 'Foo IJssel'

// changes all graphemes/code points to camelCase
u('Foo: Bar-baz.')->camel(); // 'fooBarBaz'
// changes all graphemes/code points to snake_case
u('Foo: Bar-baz.')->snake(); // 'foo_bar_baz'
// changes all graphemes/code points to kebab-case
u('Foo: Bar-baz.')->kebab(); // 'foo-bar-baz'
// changes all graphemes/code points to PascalCase
u('Foo: Bar-baz.')->pascal(); // 'FooBarBaz'
// other cases can be achieved by chaining methods, e.g. :
u('Foo: Bar-baz.')->camel()->upper(); // 'FOOBARBAZ'
```

The methods of all string classes are case-sensitive by default. You can perform case-insensitive operations with the `ignoreCase()` method:

1
2

```
u('abc')->indexOf('B');               // null
u('abc')->ignoreCase()->indexOf('B'); // 1
```

### [Methods to Append and Prepend](https://symfony.com/doc/8.0/components/string.html#methods-to-append-and-prepend "Permalink to this headline")

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32

```
// adds the given content (one or more strings) at the beginning/end of the string
u('world')->prepend('hello');      // 'helloworld'
u('world')->prepend('hello', ' '); // 'hello world'

u('hello')->append('world');      // 'helloworld'
u('hello')->append(' ', 'world'); // 'hello world'

// adds the given content at the beginning of the string (or removes it) to
// make sure that the content starts exactly with that content
u('Name')->ensureStart('get');       // 'getName'
u('getName')->ensureStart('get');    // 'getName'
u('getgetName')->ensureStart('get'); // 'getName'
// this method is similar, but works on the end of the content instead of on the beginning
u('User')->ensureEnd('Controller');           // 'UserController'
u('UserController')->ensureEnd('Controller'); // 'UserController'
u('UserControllerController')->ensureEnd('Controller'); // 'UserController'

// returns the contents found before/after the first occurrence of the given string
u('hello world')->before('world');                  // 'hello '
u('hello world')->before('o');                      // 'hell'
u('hello world')->before('o', includeNeedle: true); // 'hello'

u('hello world')->after('hello');                  // ' world'
u('hello world')->after('o');                      // ' world'
u('hello world')->after('o', includeNeedle: true); // 'o world'

// returns the contents found before/after the last occurrence of the given string
u('hello world')->beforeLast('o');                      // 'hello w'
u('hello world')->beforeLast('o', includeNeedle: true); // 'hello wo'

u('hello world')->afterLast('o');                      // 'rld'
u('hello world')->afterLast('o', includeNeedle: true); // 'orld'
```

### [Methods to Pad and Trim](https://symfony.com/doc/8.0/components/string.html#methods-to-pad-and-trim "Permalink to this headline")

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27

```
// makes a string as long as the first argument by adding the given
// string at the beginning, end or both sides of the string
u(' Lorem Ipsum ')->padBoth(20, '-'); // '--- Lorem Ipsum ----'
u(' Lorem Ipsum')->padStart(20, '-'); // '-------- Lorem Ipsum'
u('Lorem Ipsum ')->padEnd(20, '-');   // 'Lorem Ipsum --------'

// repeats the given string the number of times passed as argument
u('_.')->repeat(10); // '_._._._._._._._._._.'

// removes the given characters (default: whitespace characters) from the beginning and end of a string
u('   Lorem Ipsum   ')->trim(); // 'Lorem Ipsum'
u('Lorem Ipsum   ')->trim('m'); // 'Lorem Ipsum   '
u('Lorem Ipsum')->trim('m');    // 'Lorem Ipsu'

u('   Lorem Ipsum   ')->trimStart(); // 'Lorem Ipsum   '
u('   Lorem Ipsum   ')->trimEnd();   // '   Lorem Ipsum'

// removes the given content from the start/end of the string
u('file-image-0001.png')->trimPrefix('file-');           // 'image-0001.png'
u('file-image-0001.png')->trimPrefix('image-');          // 'file-image-0001.png'
u('file-image-0001.png')->trimPrefix('file-image-');     // '0001.png'
u('template.html.twig')->trimSuffix('.html');            // 'template.html.twig'
u('template.html.twig')->trimSuffix('.twig');            // 'template.html'
u('template.html.twig')->trimSuffix('.html.twig');       // 'template'
// when passing an array of prefix/suffix, only the first one found is trimmed
u('file-image-0001.png')->trimPrefix(['file-', 'image-']); // 'image-0001.png'
u('template.html.twig')->trimSuffix(['.twig', '.html']);   // 'template.html'
```

### [Methods to Search and Replace](https://symfony.com/doc/8.0/components/string.html#methods-to-search-and-replace "Permalink to this headline")

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47

```
// checks if the string starts/ends with the given string
u('https://symfony.com')->startsWith('https'); // true
u('report-1234.pdf')->endsWith('.pdf');        // true

// checks if the string contents are exactly the same as the given contents
u('foo')->equalsTo('foo'); // true

// checks if the string content match the given regular expression.
u('avatar-73647.png')->match('/avatar-(\d+)\.png/');
// result = ['avatar-73647.png', '73647', null]

// You can pass flags for preg_match() as second argument. If PREG_PATTERN_ORDER
// or PREG_SET_ORDER are passed, preg_match_all() will be used.
u('206-555-0100 and 800-555-1212')->match('/\d{3}-\d{3}-\d{4}/', \PREG_PATTERN_ORDER);
// result = [['206-555-0100', '800-555-1212']]

// checks if the string contains any of the other given strings
u('aeiou')->containsAny('a');                 // true
u('aeiou')->containsAny(['ab', 'efg']);       // false
u('aeiou')->containsAny(['eio', 'foo', 'z']); // true

// finds the position of the first occurrence of the given string
// (the second argument is the position where the search starts and negative
// values have the same meaning as in PHP functions)
u('abcdeabcde')->indexOf('c');     // 2
u('abcdeabcde')->indexOf('c', 2);  // 2
u('abcdeabcde')->indexOf('c', -4); // 7
u('abcdeabcde')->indexOf('eab');   // 4
u('abcdeabcde')->indexOf('k');     // null

// finds the position of the last occurrence of the given string
// (the second argument is the position where the search starts and negative
// values have the same meaning as in PHP functions)
u('abcdeabcde')->indexOfLast('c');     // 7
u('abcdeabcde')->indexOfLast('c', 2);  // 7
u('abcdeabcde')->indexOfLast('c', -4); // 2
u('abcdeabcde')->indexOfLast('eab');   // 4
u('abcdeabcde')->indexOfLast('k');     // null

// replaces all occurrences of the given string
u('http://symfony.com')->replace('http://', 'https://'); // 'https://symfony.com'
// replaces all occurrences of the given regular expression
u('(+1) 206-555-0100')->replaceMatches('/[^A-Za-z0-9]++/', ''); // '12065550100'
// you can pass a callable as the second argument to perform advanced replacements
u('123')->replaceMatches('/\d/', function (string $match): string {
    return '['.$match[0].']';
}); // result = '[1][2][3]'
```

### [Methods to Join, Split, Truncate and Reverse](https://symfony.com/doc/8.0/components/string.html#methods-to-join-split-truncate-and-reverse "Permalink to this headline")

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29

```
// uses the string as the "glue" to merge all the given strings
u(', ')->join(['foo', 'bar']); // 'foo, bar'

// breaks the string into pieces using the given delimiter
u('template_name.html.twig')->split('.');    // ['template_name', 'html', 'twig']
// you can set the maximum number of pieces as the second argument
u('template_name.html.twig')->split('.', 2); // ['template_name', 'html.twig']

// returns a substring which starts at the first argument and has the length of the
// second optional argument (negative values have the same meaning as in PHP functions)
u('Symfony is great')->slice(0, 7);  // 'Symfony'
u('Symfony is great')->slice(0, -6); // 'Symfony is'
u('Symfony is great')->slice(11);    // 'great'
u('Symfony is great')->slice(-5);    // 'great'

// reduces the string to the length given as argument (if it's longer)
u('Lorem Ipsum')->truncate(3);             // 'Lor'
u('Lorem Ipsum')->truncate(80);            // 'Lorem Ipsum'
// the second argument is the character(s) added when a string is cut
// (the total length includes the length of this character(s))
// (note that '…' is a single character that includes three dots; it's not '...')
u('Lorem Ipsum')->truncate(8, '…');        // 'Lorem I…'
// the third optional argument defines how to cut words when the length is exceeded
// the default value is TruncateMode::Char which cuts the string at the exact given length
u('Lorem ipsum dolor sit amet')->truncate(8, cut: TruncateMode::Char);       // 'Lorem ip'
// returns up to the last complete word that fits in the given length without surpassing it
u('Lorem ipsum dolor sit amet')->truncate(8, cut: TruncateMode::WordBefore); // 'Lorem'
// returns up to the last complete word that fits in the given length, surpassing it if needed
u('Lorem ipsum dolor sit amet')->truncate(8, cut: TruncateMode::WordAfter);   // 'Lorem ipsum'
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

```
// breaks the string into lines of the given length
u('Lorem Ipsum')->wordwrap(4);                  // 'Lorem\nIpsum'
// by default it breaks by white space; pass TRUE to break unconditionally
u('Lorem Ipsum')->wordwrap(4, "\n", cut: true); // 'Lore\nm\nIpsu\nm'

// replaces a portion of the string with the given contents:
// the second argument is the position where the replacement starts;
// the third argument is the number of graphemes/code points removed from the string
u('0123456789')->splice('xxx');       // 'xxx'
u('0123456789')->splice('xxx', 0, 2); // 'xxx23456789'
u('0123456789')->splice('xxx', 0, 6); // 'xxx6789'
u('0123456789')->splice('xxx', 6);    // '012345xxx'

// breaks the string into pieces of the length given as argument
u('0123456789')->chunk(3);  // ['012', '345', '678', '9']

// reverses the order of the string contents
u('foo bar')->reverse();  // 'rab oof'
u('さよなら')->reverse(); // 'らなよさ'
```

### [Methods Added by ByteString](https://symfony.com/doc/8.0/components/string.html#methods-added-by-bytestring "Permalink to this headline")

These methods are only available for `ByteString` objects:

1
2
3

```
// returns TRUE if the string contents are valid UTF-8 contents
b('Lorem Ipsum')->isUtf8(); // true
b("\xc3\x28")->isUtf8();    // false
```

### [Methods Added by CodePointString and UnicodeString](https://symfony.com/doc/8.0/components/string.html#methods-added-by-codepointstring-and-unicodestring "Permalink to this headline")

These methods are only available for `CodePointString` and `UnicodeString` objects:

1
2
3
4
5
6
7
8
9
10
11

```
// transliterates any string into the latin alphabet defined by the ASCII encoding
// (don't use this method to build a slugger because this component already provides
// a slugger, as explained later in this article)
u('नमस्ते')->ascii();    // 'namaste'
u('さよなら')->ascii(); // 'sayonara'
u('спасибо')->ascii(); // 'spasibo'

// returns an array with the code point or points stored at the given position
// (code points of 'नमस्ते' graphemes = [2344, 2350, 2360, 2340]
u('नमस्ते')->codePointsAt(0); // [2344]
u('नमस्ते')->codePointsAt(2); // [2360]
```

[Unicode equivalence](https://en.wikipedia.org/wiki/Unicode_equivalence) is the specification by the Unicode standard that different sequences of code points represent the same character. For example, the Swedish letter `å` can be a single code point (`U+00E5` = _"latin small letter A with ring above"_) or a sequence of two code points (`U+0061` = _"latin small letter A"_ + `U+030A` = _"combining ring above"_). The `normalize()` method allows you to pick the normalization mode:

1
2
3
4
5
6

```
// these encode the letter as a single code point: U+00E5
u('å')->normalize(UnicodeString::NFC);
u('å')->normalize(UnicodeString::NFKC);
// these encode the letter as two code points: U+0061 + U+030A
u('å')->normalize(UnicodeString::NFD);
u('å')->normalize(UnicodeString::NFKD);
```

[Lazy-loaded Strings](https://symfony.com/doc/8.0/components/string.html#lazy-loaded-strings "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------

Sometimes, creating a string with the methods presented in the previous sections is not optimal. For example, consider a hash value that requires certain computation to obtain and which you might end up not using it.

In those cases, it's better to use the [LazyString](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/String/LazyString.php "Symfony\Component\String\LazyString") class that allows storing a string whose value is only generated when you need it:

1
2
3
4
5
6
7
8
9

```
use Symfony\Component\String\LazyString;

$lazyString = LazyString::fromCallable(function (): string {
    // Compute the string value...
    $value = ...;

    // Then return the final value
    return $value;
});
```

The callback will only be executed when the value of the lazy string is requested during the program execution. You can also create lazy strings from a `Stringable` object:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

```
class Hash implements \Stringable
{
    public function __toString(): string
    {
        return $this->computeHash();
    }

    private function computeHash(): string
    {
        // Compute hash value with potentially heavy processing
        $hash = ...;

        return $hash;
    }
}

// Then create a lazy string from this hash, which will trigger
// hash computation only if it's needed
$lazyHash = LazyString::fromStringable(new Hash());
```

[Working with Emojis](https://symfony.com/doc/8.0/components/string.html#working-with-emojis "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------

These contents have been moved to the [Emoji component docs](https://symfony.com/doc/8.0/components/emoji.html).

[Slugger](https://symfony.com/doc/8.0/components/string.html#slugger "Permalink to this headline")
--------------------------------------------------------------------------------------------------

In some contexts, such as URLs and file/directory names, it's not safe to use any Unicode character. A _slugger_ transforms a given string into another string that only includes safe ASCII characters:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21

```
use Symfony\Component\String\Slugger\AsciiSlugger;

$slugger = new AsciiSlugger();
$slug = $slugger->slug('Wôrķšƥáçè ~~sèťtïñğš~~');
// $slug = 'Workspace-settings'

// you can also pass an array with additional character substitutions
$slugger = new AsciiSlugger('en', ['en' => ['%' => 'percent', '€' => 'euro']]);
$slug = $slugger->slug('10% or 5€');
// $slug = '10-percent-or-5-euro'

// if there is no symbols map for your locale (e.g. 'en_GB') then the parent locale's symbols map
// will be used instead (i.e. 'en')
$slugger = new AsciiSlugger('en_GB', ['en' => ['%' => 'percent', '€' => 'euro']]);
$slug = $slugger->slug('10% or 5€');
// $slug = '10-percent-or-5-euro'

// for more dynamic substitutions, pass a PHP closure instead of an array
$slugger = new AsciiSlugger('en', function (string $string, string $locale): string {
    return str_replace('❤️', 'love', $string);
});
```

The separator between words is a dash (`-`) by default, but you can define another separator as the second argument:

1
2

```
$slug = $slugger->slug('Wôrķšƥáçè ~~sèťtïñğš~~', '/');
// $slug = 'Workspace/settings'
```

The slugger transliterates the original string into the Latin script before applying the other transformations. The locale of the original string is detected automatically, but you can define it explicitly:

1
2
3
4
5
6

```
// this tells the slugger to transliterate from Korean ('ko') language
$slugger = new AsciiSlugger('ko');

// you can override the locale as the third optional parameter of slug()
// e.g. this slugger transliterates from Persian ('fa') language
$slug = $slugger->slug('...', '-', 'fa');
```

In a Symfony application, you don't need to create the slugger yourself. Thanks to [service autowiring](https://symfony.com/doc/8.0/components/service_container/autowiring.html), you can inject a slugger by type-hinting a service constructor argument with the [SluggerInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/String/Slugger/SluggerInterface.php "Symfony\Component\String\Slugger\SluggerInterface"). The locale of the injected slugger is the same as the request locale:

1
2
3
4
5
6
7
8
9
10
11
12
13
14

```
use Symfony\Component\String\Slugger\SluggerInterface;

class MyService
{
    public function __construct(
        private SluggerInterface $slugger,
    ) {
    }

    public function someMethod(): void
    {
        $slug = $this->slugger->slug('...');
    }
}
```

### [Slug Emojis](https://symfony.com/doc/8.0/components/string.html#slug-emojis "Permalink to this headline")

You can also combine the [emoji transliterator](https://symfony.com/doc/8.0/components/emoji.html#emoji-transliteration) with the slugger to transform any emojis into their textual representation:

1
2
3
4
5
6
7
8
9
10

```
use Symfony\Component\String\Slugger\AsciiSlugger;

$slugger = new AsciiSlugger();
$slugger = $slugger->withEmoji();

$slug = $slugger->slug('a 😺, 🐈‍⬛, and a 🦁 go to 🏞️', '-', 'en');
// $slug = 'a-grinning-cat-black-cat-and-a-lion-go-to-national-park';

$slug = $slugger->slug('un 😺, 🐈‍⬛, et un 🦁 vont au 🏞️', '-', 'fr');
// $slug = 'un-chat-qui-sourit-chat-noir-et-un-tete-de-lion-vont-au-parc-national';
```

If you want to use a specific locale for the emoji, or to use the short codes from GitHub, Gitlab or Slack, use the first argument of `withEmoji()` method:

1
2
3
4
5
6
7

```
use Symfony\Component\String\Slugger\AsciiSlugger;

$slugger = new AsciiSlugger();
$slugger = $slugger->withEmoji('github'); // or "en", or "fr", etc.

$slug = $slugger->slug('a 😺, 🐈‍⬛, and a 🦁');
// $slug = 'a-smiley-cat-black-cat-and-a-lion';
```

[Inflector](https://symfony.com/doc/8.0/components/string.html#inflector "Permalink to this headline")
------------------------------------------------------------------------------------------------------

In some scenarios such as code generation and code introspection, you need to convert words from/to singular/plural. For example, to know the property associated with an _adder_ method, you must convert from plural (`addStories()` method) to singular (`$story` property).

Most human languages have simple pluralization rules, but at the same time they define lots of exceptions. For example, the general rule in English is to add an `s` at the end of the word (`book` ->`books`) but there are lots of exceptions even for common words (`woman` ->`women`, `life` ->`lives`, `news` ->`news`, `radius` ->`radii`, etc.)

This component provides an [EnglishInflector](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/String/Inflector/EnglishInflector.php "Symfony\Component\String\Inflector\EnglishInflector") class to convert English words from/to singular/plural with confidence:

1
2
3
4
5
6
7
8
9
10
11

```
use Symfony\Component\String\Inflector\EnglishInflector;

$inflector = new EnglishInflector();

$result = $inflector->singularize('teeth');   // ['tooth']
$result = $inflector->singularize('radii');   // ['radius']
$result = $inflector->singularize('leaves');  // ['leaf', 'leave', 'leaff']

$result = $inflector->pluralize('bacterium'); // ['bacteria']
$result = $inflector->pluralize('news');      // ['news']
$result = $inflector->pluralize('person');    // ['persons', 'people']
```

The value returned by both methods is always an array because sometimes it's not possible to determine a unique singular/plural form for the given word.

Symfony also provides inflectors for other languages:

1
2
3
4
5
6
7
8
9
10
11

```
use Symfony\Component\String\Inflector\FrenchInflector;

$inflector = new FrenchInflector();
$result = $inflector->singularize('souris'); // ['souris']
$result = $inflector->pluralize('hôpital');  // ['hôpitaux']

use Symfony\Component\String\Inflector\SpanishInflector;

$inflector = new SpanishInflector();
$result = $inflector->singularize('aviones'); // ['avión']
$result = $inflector->pluralize('miércoles'); // ['miércoles']
```

Note

Symfony provides an [InflectorInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/String/Inflector/InflectorInterface.php "Symfony\Component\String\Inflector\InflectorInterface") in case you need to implement your own inflector.

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

 TOC

 Search

 Version

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 9: ads via Carbon](https://srv.carbonads.net/static/30242/84dc127dd611279d2e1851401dca56a0f28ebfa8)](https://srv.carbonads.net/ads/click/x/GTND427UCKYILKQNF67LYKQUCA7I553IFTBD5Z3JCASIC5QJCWBDE5QKCEBD4KJNCVYILK37CVYIC5QJCKBIC2JKC6SI5K7JF6YDEK3EHJNCLSIZ)[Start an annual website plan, and get a free domain name with Squarespace.](https://srv.carbonads.net/ads/click/x/GTND427UCKYILKQNF67LYKQUCA7I553IFTBD5Z3JCASIC5QJCWBDE5QKCEBD4KJNCVYILK37CVYIC5QJCKBIC2JKC6SI5K7JF6YDEK3EHJNCLSIZ)[ads via Carbon](http://carbonads.net/?utm_source=symfonycom&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

![Image 10: ads via Carbon](https://ad.doubleclick.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B34445489.438308384;dc_trk_aid=631459208;dc_trk_cid=248949291;ord=177319318;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1?)

[![Image 11: Be trained by SensioLabs experts (2 to 6 day sessions -- French or English).](https://symfony.com/images/network/sltraining_01.webp)](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_ads&utm_campaign=permanent_referral)
[Be trained by SensioLabs experts (2 to 6 day sessions -- French or English).](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_ads&utm_campaign=permanent_referral)

[![Image 12: Put the code quality back at the heart of your project](https://symfony.com/images/network/sfinsight_01.png)](https://insight.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=insight&utm_content=quality)
[Put the code quality back at the heart of your project](https://insight.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=insight&utm_content=quality)

Symfony footer
--------------

![Image 13: Avatar of Grayson Koonce, a Symfony contributor](https://www.gravatar.com/avatar/c4635cd7f47b7c581e295f57d5864e0d?size=48&rating=g&default=retro)

Thanks **Grayson Koonce** for being a Symfony contributor

**4** commits • **30** lines changed

[View all contributors](https://symfony.com/contributors) that help us make Symfony

### Become a Symfony contributor

Be an active part of the community and contribute ideas, code and bug fixes. Both experts and newcomers are welcome.

[Learn how to contribute](https://symfony.com/doc/current/contributing/index.html)

![Image 14](https://symfony.com/assets/icons/logos/sf-20years-wordmark-dark--dFsFxh.webp)
[Celebrating 20 years of Symfony](https://symfony.com/20years)

**Symfony**™ is a trademark of Symfony SAS. [All rights reserved](https://symfony.com/trademark).

* [What is Symfony?](https://symfony.com/what-is-symfony)

  * [What is Symfony?](https://symfony.com/what-is-symfony)
  * [Symfony at a Glance](https://symfony.com/at-a-glance)
  * [Symfony Packages](https://symfony.com/packages)
  * [Symfony Releases](https://symfony.com/releases)
  * [Security Policy](https://symfony.com/doc/current/contributing/code/security.html)
  * [Logo & Screenshots](https://symfony.com/logo)
  * [Trademark & Licenses](https://symfony.com/license)
  * [symfony1 Legacy](https://symfony.com/legacy)

* [Learn Symfony](https://symfony.com/doc)

  * [Symfony Docs](https://symfony.com/doc)
  * [Symfony Book](https://symfony.com/book)
  * [Reference](https://symfony.com/doc/current/reference/index.html)
  * [Bundles](https://symfony.com/bundles)
  * [Best Practices](https://symfony.com/doc/current/best_practices.html)
  * [Training](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [eLearning Platform](https://university.sensiolabs.com/e-learning-platform?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [Certification](https://certification.symfony.com/)

* [Screencasts](https://symfonycasts.com/)

  * [Learn Symfony](https://symfonycasts.com/tracks/symfony)
  * [Learn PHP](https://symfonycasts.com/tracks/php)
  * [Learn JavaScript](https://symfonycasts.com/tracks/javascript)
  * [Learn Drupal](https://symfonycasts.com/tracks/drupal)
  * [Learn RESTful APIs](https://symfonycasts.com/tracks/rest)

* [Community](https://symfony.com/community)

  * [Symfony Community](https://symfony.com/community)
  * [SymfonyConnect](https://connect.symfony.com/)
  * [Events & Meetups](https://symfony.com/events/)
  * [Projects using Symfony](https://symfony.com/projects)
  * [Contributors](https://symfony.com/contributors)
  * [Symfony Jobs](https://symfony.com/jobs)
  * [Backers](https://symfony.com/backers)
  * [Code of Conduct](https://symfony.com/doc/current/contributing/code_of_conduct/code_of_conduct.html)
  * [Downloads Stats](https://symfony.com/stats/downloads)
  * [Support](https://symfony.com/support)

* [Blog](https://symfony.com/blog/)

  * [All Blog Posts](https://symfony.com/blog/)
  * [A Week of Symfony](https://symfony.com/blog/category/a-week-of-symfony)
  * [Case Studies](https://symfony.com/blog/category/case-studies)
  * [Cloud](https://symfony.com/blog/category/cloud)
  * [Community](https://symfony.com/blog/category/community)
  * [Conferences](https://symfony.com/blog/category/conferences)
  * [Diversity](https://symfony.com/blog/category/diversity)
  * [Living on the edge](https://symfony.com/blog/category/living-on-the-edge)
  * [Releases](https://symfony.com/blog/category/releases)
  * [Security Advisories](https://symfony.com/blog/category/security-advisories)
  * [Symfony Insight](https://symfony.com/blog/category/symfony-insight)
  * [Twig](https://symfony.com/blog/category/twig)
  * [SensioLabs Blog](https://sensiolabs.com/blog?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)

* [Services](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)

  * [SensioLabs services](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [Train developers](https://sensiolabs.com/training?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [Manage your project quality](https://insight.symfony.com/)
  * [Improve your project performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=symfonycom_footer&utm_campaign=profiler)
  * [Host Symfony projects](https://symfony.com/cloud/)

[Powered by](https://symfony.com/cloud/)

[](https://symfony.com/cloud/ "Upsun, a Platform-as-a-Service optimized for Symfony developers")

### Follow Symfony

[](https://github.com/symfony "Symfony on GitHub")[](https://symfony.com/slack "Symfony on Slack")[](https://twitter.com/symfony "Symfony on Twitter")[](https://mastodon.social/@symfony "Symfony on Mastodon")[](https://www.linkedin.com/company/symfony-sas/ "Symfony on LinkedIn")[](https://www.facebook.com/SymfonyFramework "Symfony on Facebook")[](https://www.youtube.com/symfonytv "Symfony on YouTube")[](https://bsky.app/profile/symfony.com "Symfony on BlueSky")[](https://www.threads.net/@symfony "Symfony on Threads")[](https://symfonycasts.com/ "Symfony Screencasts")[](https://feeds.feedburner.com/symfony/blog "Symfony Blog RSS")

Site appearance:

CLOSE

Search Symfony Docs

Search
