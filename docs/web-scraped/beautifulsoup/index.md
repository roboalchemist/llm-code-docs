# Beautiful Soup Documentation
# Source: https://beautiful-soup-4.readthedocs.io/en/latest/

## Beautiful Soup DocumentationÂ¶

Beautiful Soup Documentation

Beautiful Soupis a
Python library for pulling data out of HTML and XML files. It works
with your favorite parser to provide idiomatic ways of navigating,
searching, and modifying the parse tree. It commonly saves programmers
hours or days of work.

Beautiful Soup
is a
Python library for pulling data out of HTML and XML files. It works
with your favorite parser to provide idiomatic ways of navigating,
searching, and modifying the parse tree. It commonly saves programmers
hours or days of work.

These instructions illustrate all major features of Beautiful Soup 4,
with examples. I show you what the library is good for, how it works,
how to use it, how to make it do what you want, and what to do when it
violates your expectations.

These instructions illustrate all major features of Beautiful Soup 4,
with examples. I show you what the library is good for, how it works,
how to use it, how to make it do what you want, and what to do when it
violates your expectations.

This document covers Beautiful Soup version 4.8.1. The examples in
this documentation should work the same way in Python 2.7 and Python
3.2.

This document covers Beautiful Soup version 4.8.1. The examples in
this documentation should work the same way in Python 2.7 and Python
3.2.

You might be looking for the documentation forBeautiful Soup 3.
If so, you should know that Beautiful Soup 3 is no longer being
developed and that support for it will be dropped on or after December
31, 2020. If you want to learn about the differences between Beautiful
Soup 3 and Beautiful Soup 4, seePorting code to BS4.

You might be looking for the documentation for
Beautiful Soup 3
.
If so, you should know that Beautiful Soup 3 is no longer being
developed and that support for it will be dropped on or after December
31, 2020. If you want to learn about the differences between Beautiful
Soup 3 and Beautiful Soup 4, see
Porting code to BS4

This documentation has been translated into other languages by
Beautiful Soup users:

This documentation has been translated into other languages by
Beautiful Soup users:

- è¿ç¯ææ¡£å½ç¶è¿æä¸­æç.
- ãã®ãã¼ã¸ã¯æ¥æ¬èªã§å©ç¨ã§ãã¾ã(å¤é¨ãªã³ã¯)
- ì´ ë¬¸ìë íêµ­ì´ ë²ì­ë ê°ë¥í©ëë¤.
- Este documento tambÃ©m estÃ¡ disponÃ­vel em PortuguÃªs do Brasil.

è¿ç¯ææ¡£å½ç¶è¿æä¸­æç.
ãã®ãã¼ã¸ã¯æ¥æ¬èªã§å©ç¨ã§ãã¾ã(
å¤é¨ãªã³ã¯
ì´ ë¬¸ìë íêµ­ì´ ë²ì­ë ê°ë¥í©ëë¤.
Este documento tambÃ©m estÃ¡ disponÃ­vel em PortuguÃªs do Brasil.

### Getting helpÂ¶

Getting help

If you have questions about Beautiful Soup, or run into problems,send mail to the discussion group. If
your problem involves parsing an HTML document, be sure to mentionwhat the diagnose() function saysabout
that document.

If you have questions about Beautiful Soup, or run into problems,
send mail to the discussion group
. If
your problem involves parsing an HTML document, be sure to mention
what the diagnose() function says
about
that document.

## Quick StartÂ¶

Quick Start

Hereâs an HTML document Iâll be using as an example throughout this
document. Itâs part of a story fromAlice in Wonderland:

Hereâs an HTML document Iâll be using as an example throughout this
document. Itâs part of a story from
Alice in Wonderland

```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

```

html_doc
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>

Running the âthree sistersâ document through Beautiful Soup gives us aBeautifulSoupobject, which represents the document as a nested
data structure:

Running the âthree sistersâ document through Beautiful Soup gives us a
BeautifulSoup
object, which represents the document as a nested
data structure:

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
# <html>
# <head>
# <title>
# The Dormouse's story
# </title>
# </head>
# <body>
# <p class="title">
# <b>
# The Dormouse's story
# </b>
# </p>
# <p class="story">
# Once upon a time there were three little sisters; and their names were
# <a class="sister" href="http://example.com/elsie" id="link1">
# Elsie
# </a>
# ,
# <a class="sister" href="http://example.com/lacie" id="link2">
# Lacie
# </a>
# and
# <a class="sister" href="http://example.com/tillie" id="link2">
# Tillie
# </a>
# ; and they lived at the bottom of a well.
# </p>
# <p class="story">
# ...
# </p>
# </body>
# </html>

```

from
import
BeautifulSoup
soup
BeautifulSoup
html_doc
'html.parser'
print
soup
prettify
# <html>
# <head>
# <title>
# The Dormouse's story
# </title>
# </head>
# <body>
# <p class="title">
# <b>
# The Dormouse's story
# </b>
# </p>
# <p class="story">
# Once upon a time there were three little sisters; and their names were
# <a class="sister" href="http://example.com/elsie" id="link1">
# Elsie
# </a>
# ,
# <a class="sister" href="http://example.com/lacie" id="link2">
# Lacie
# </a>
# and
# <a class="sister" href="http://example.com/tillie" id="link2">
# Tillie
# </a>
# ; and they lived at the bottom of a well.
# </p>
# <p class="story">
# ...
# </p>
# </body>
# </html>

Here are some simple ways to navigate that data structure:

Here are some simple ways to navigate that data structure:

```python
soup.title
# <title>The Dormouse's story</title>

soup.title.name
# u'title'

soup.title.string
# u'The Dormouse's story'

soup.title.parent.name
# u'head'

soup.p
# <p class="title"><b>The Dormouse's story</b></p>

soup.p['class']
# u'title'

soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

```

soup
title
# <title>The Dormouse's story</title>
soup
title
name
# u'title'
soup
title
string
# u'The Dormouse's story'
soup
title
parent
name
# u'head'
soup
# <p class="title"><b>The Dormouse's story</b></p>
soup
'class'
# u'title'
soup
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
soup
find_all
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup
find
"link3"
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

One common task is extracting all the URLs found within a pageâs <a> tags:

One common task is extracting all the URLs found within a pageâs <a> tags:

```python
for link in soup.find_all('a'):
 print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie

```

link
soup
find_all
print
link
'href'
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie

Another common task is extracting all the text from a page:

Another common task is extracting all the text from a page:

```python
print(soup.get_text())
# The Dormouse's story
#
# The Dormouse's story
#
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
#
# ...

```

print
soup
get_text
# The Dormouse's story
# The Dormouse's story
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
# ...

Does this look like what you need? If so, read on.

Does this look like what you need? If so, read on.

## Installing Beautiful SoupÂ¶

Installing Beautiful Soup

If youâre using a recent version of Debian or Ubuntu Linux, you can
install Beautiful Soup with the system package manager:

If youâre using a recent version of Debian or Ubuntu Linux, you can
install Beautiful Soup with the system package manager:

$ apt-get install python-bs4(for Python 2)

$ apt-get install python-bs4
(for Python 2)

$ apt-get install python3-bs4(for Python 3)

$ apt-get install python3-bs4
(for Python 3)

Beautiful Soup 4 is published through PyPi, so if you canât install it
with the system packager, you can install it witheasy_installorpip. The package name isbeautifulsoup4, and the same package
works on Python 2 and Python 3. Make sure you use the right version ofpiporeasy_installfor your Python version (these may be namedpip3andeasy_install3respectively if youâre using Python 3).

Beautiful Soup 4 is published through PyPi, so if you canât install it
with the system packager, you can install it with
easy_install
. The package name is
beautifulsoup4
, and the same package
works on Python 2 and Python 3. Make sure you use the right version of
easy_install
for your Python version (these may be named
pip3
easy_install3
respectively if youâre using Python 3).

$ easy_install beautifulsoup4

$ easy_install beautifulsoup4

$ pip install beautifulsoup4

$ pip install beautifulsoup4

(TheBeautifulSouppackage is probablynotwhat you want. Thatâs
the previous major release,Beautiful Soup 3. Lots of software uses
BS3, so itâs still available, but if youâre writing new code you
should installbeautifulsoup4.)

(The
BeautifulSoup
package is probably
Beautiful Soup 3
. Lots of software uses
BS3, so itâs still available, but if youâre writing new code you
should install
beautifulsoup4

If you donât haveeasy_installorpipinstalled, you candownload the Beautiful Soup 4 source tarballand
install it withsetup.py.

If you donât have
easy_install
installed, you can
download the Beautiful Soup 4 source tarball
and
install it with
setup.py

$ python setup.py install

$ python setup.py install

If all else fails, the license for Beautiful Soup allows you to
package the entire library with your application. You can download the
tarball, copy itsbs4directory into your applicationâs codebase,
and use Beautiful Soup without installing it at all.

If all else fails, the license for Beautiful Soup allows you to
package the entire library with your application. You can download the
tarball, copy its
directory into your applicationâs codebase,
and use Beautiful Soup without installing it at all.

I use Python 2.7 and Python 3.2 to develop Beautiful Soup, but it
should work with other recent versions.

I use Python 2.7 and Python 3.2 to develop Beautiful Soup, but it
should work with other recent versions.

### Problems after installationÂ¶

Problems after installation

Beautiful Soup is packaged as Python 2 code. When you install it for
use with Python 3, itâs automatically converted to Python 3 code. If
you donât install the package, the code wonât be converted. There have
also been reports on Windows machines of the wrong version being
installed.

Beautiful Soup is packaged as Python 2 code. When you install it for
use with Python 3, itâs automatically converted to Python 3 code. If
you donât install the package, the code wonât be converted. There have
also been reports on Windows machines of the wrong version being
installed.

If you get theImportErrorâNo module named HTMLParserâ, your
problem is that youâre running the Python 2 version of the code under
Python 3.

If you get the
ImportError
âNo module named HTMLParserâ, your
problem is that youâre running the Python 2 version of the code under
Python 3.

If you get theImportErrorâNo module named html.parserâ, your
problem is that youâre running the Python 3 version of the code under
Python 2.

If you get the
ImportError
âNo module named html.parserâ, your
problem is that youâre running the Python 3 version of the code under
Python 2.

In both cases, your best bet is to completely remove the Beautiful
Soup installation from your system (including any directory created
when you unzipped the tarball) and try the installation again.

In both cases, your best bet is to completely remove the Beautiful
Soup installation from your system (including any directory created
when you unzipped the tarball) and try the installation again.

If you get theSyntaxErrorâInvalid syntaxâ on the lineROOT_TAG_NAME=u'[document]', you need to convert the Python 2
code to Python 3. You can do this either by installing the package:

If you get the
SyntaxError
âInvalid syntaxâ on the line
ROOT_TAG_NAME
u'[document]'
, you need to convert the Python 2
code to Python 3. You can do this either by installing the package:

$ python3 setup.py install

$ python3 setup.py install

or by manually running Pythonâs2to3conversion script on thebs4directory:

or by manually running Pythonâs
2to3
conversion script on the
directory:

$ 2to3-3.2 -w bs4

$ 2to3-3.2 -w bs4

### Installing a parserÂ¶

Installing a parser

Beautiful Soup supports the HTML parser included in Pythonâs standard
library, but it also supports a number of third-party Python parsers.
One is thelxml parser. Depending on your setup,
you might install lxml with one of these commands:

Beautiful Soup supports the HTML parser included in Pythonâs standard
library, but it also supports a number of third-party Python parsers.
One is the
lxml parser
. Depending on your setup,
you might install lxml with one of these commands:

$ apt-get install python-lxml

$ apt-get install python-lxml

$ easy_install lxml

$ easy_install lxml

$ pip install lxml

$ pip install lxml

Another alternative is the pure-Pythonhtml5lib parser, which parses HTML the way a
web browser does. Depending on your setup, you might install html5lib
with one of these commands:

Another alternative is the pure-Python
html5lib parser
, which parses HTML the way a
web browser does. Depending on your setup, you might install html5lib
with one of these commands:

$ apt-get install python-html5lib

$ apt-get install python-html5lib

$ easy_install html5lib

$ easy_install html5lib

$ pip install html5lib

$ pip install html5lib

This table summarizes the advantages and disadvantages of each parser library:

This table summarizes the advantages and disadvantages of each parser library:
Parser
Typical usage
Advantages
Disadvantages
Pythonâs html.parser
BeautifulSoup(markup,
"html.parser")

- Batteries included
- Decent speed
- Lenient (As of Python 2.7.3
and 3.2.)

Batteries included
Decent speed
Lenient (As of Python 2.7.3
and 3.2.)

- Not as fast as lxml,
less lenient than
html5lib.

Not as fast as lxml,
less lenient than
html5lib.
lxmlâs HTML parser
BeautifulSoup(markup,
"lxml")

- Very fast
- Lenient

Very fast
Lenient

- External C dependency

External C dependency
lxmlâs XML parser
BeautifulSoup(markup,
"lxml-xml")
BeautifulSoup(markup,
"xml")

- Very fast
- The only currently supported
XML parser

Very fast
The only currently supported
XML parser

- External C dependency

External C dependency
html5lib
BeautifulSoup(markup,
"html5lib")

- Extremely lenient
- Parses pages the same way a
web browser does
- Creates valid HTML5

Extremely lenient
Parses pages the same way a
web browser does
Creates valid HTML5

- Very slow
- External Python
dependency

Very slow
External Python
dependency

If you can, I recommend you install and use lxml for speed. If youâre
using a version of Python 2 earlier than 2.7.3, or a version of Python
3 earlier than 3.2.2, itâsessentialthat you install lxml or
html5libâPythonâs built-in HTML parser is just not very good in older
versions.

If you can, I recommend you install and use lxml for speed. If youâre
using a version of Python 2 earlier than 2.7.3, or a version of Python
3 earlier than 3.2.2, itâs
essential
that you install lxml or
html5libâPythonâs built-in HTML parser is just not very good in older
versions.

Note that if a document is invalid, different parsers will generate
different Beautiful Soup trees for it. SeeDifferences
between parsersfor details.

Note that if a document is invalid, different parsers will generate
different Beautiful Soup trees for it. See
Differences
between parsers
for details.

## Making the soupÂ¶

Making the soup

To parse a document, pass it into theBeautifulSoupconstructor. You can pass in a string or an open filehandle:

To parse a document, pass it into the
BeautifulSoup
constructor. You can pass in a string or an open filehandle:

```python
from bs4 import BeautifulSoup

with open("index.html") as fp:
 soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>data</html>")

```

from
import
BeautifulSoup
with
open
"index.html"
soup
BeautifulSoup
soup
BeautifulSoup
"<html>data</html>"

First, the document is converted to Unicode, and HTML entities are
converted to Unicode characters:

First, the document is converted to Unicode, and HTML entities are
converted to Unicode characters:

```python
BeautifulSoup("Sacr&eacute; bleu!")
<html><head></head><body>SacrÃ© bleu!</body></html>

```

BeautifulSoup("Sacr&eacute; bleu!")
<html><head></head><body>SacrÃ© bleu!</body></html>

Beautiful Soup then parses the document using the best available
parser. It will use an HTML parser unless you specifically tell it to
use an XML parser. (SeeParsing XML.)

Beautiful Soup then parses the document using the best available
parser. It will use an HTML parser unless you specifically tell it to
use an XML parser. (See
Parsing XML

## Kinds of objectsÂ¶

Kinds of objects

Beautiful Soup transforms a complex HTML document into a complex tree
of Python objects. But youâll only ever have to deal with about fourkindsof objects:Tag,NavigableString,BeautifulSoup,
andComment.

Beautiful Soup transforms a complex HTML document into a complex tree
of Python objects. But youâll only ever have to deal with about four
kinds
of objects:
NavigableString
BeautifulSoup
,
and
Comment

### TagÂ¶

ATagobject corresponds to an XML or HTML tag in the original document:

object corresponds to an XML or HTML tag in the original document:

```python
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
type(tag)
# <class 'bs4.element.Tag'>

```

soup
BeautifulSoup
'<b class="boldest">Extremely bold</b>'
soup
type
# <class 'bs4.element.Tag'>

Tags have a lot of attributes and methods, and Iâll cover most of them
inNavigating the treeandSearching the tree. For now, the most
important features of a tag are its name and attributes.

Tags have a lot of attributes and methods, and Iâll cover most of them
in
Navigating the tree
Searching the tree
. For now, the most
important features of a tag are its name and attributes.

#### NameÂ¶

Name

Every tag has a name, accessible as.name:

Every tag has a name, accessible as
.name

```python
tag.name
# u'b'

```

name
# u'b'

If you change a tagâs name, the change will be reflected in any HTML
markup generated by Beautiful Soup:

If you change a tagâs name, the change will be reflected in any HTML
markup generated by Beautiful Soup:

```python
tag.name = "blockquote"
tag
# <blockquote class="boldest">Extremely bold</blockquote>

```

name
"blockquote"
# <blockquote class="boldest">Extremely bold</blockquote>

#### AttributesÂ¶

Attributes

A tag may have any number of attributes. The tag<bid="boldest">has an attribute âidâ whose value is
âboldestâ. You can access a tagâs attributes by treating the tag like
a dictionary:

A tag may have any number of attributes. The tag
id="boldest">
has an attribute âidâ whose value is
âboldestâ. You can access a tagâs attributes by treating the tag like
a dictionary:

```python
tag['id']
# u'boldest'

```

'id'
# u'boldest'

You can access that dictionary directly as.attrs:

You can access that dictionary directly as
.attrs

```python
tag.attrs
# {u'id': 'boldest'}

```

attrs
# {u'id': 'boldest'}

You can add, remove, and modify a tagâs attributes. Again, this is
done by treating the tag as a dictionary:

You can add, remove, and modify a tagâs attributes. Again, this is
done by treating the tag as a dictionary:

```python
tag['id'] = 'verybold'
tag['another-attribute'] = 1
tag
# <b another-attribute="1" id="verybold"></b>

del tag['id']
del tag['another-attribute']
tag
# <b></b>

tag['id']
# KeyError: 'id'
print(tag.get('id'))
# None

```

'id'
'verybold'
'another-attribute'
# <b another-attribute="1" id="verybold"></b>
'id'
'another-attribute'
# <b></b>
'id'
# KeyError: 'id'
print
'id'
# None

##### Multi-valued attributesÂ¶

Multi-valued attributes

HTML 4 defines a few attributes that can have multiple values. HTML 5
removes a couple of them, but defines a few more. The most common
multi-valued attribute isclass(that is, a tag can have more than
one CSS class). Others includerel,rev,accept-charset,headers, andaccesskey. Beautiful Soup presents the value(s)
of a multi-valued attribute as a list:

HTML 4 defines a few attributes that can have multiple values. HTML 5
removes a couple of them, but defines a few more. The most common
multi-valued attribute is
class
(that is, a tag can have more than
one CSS class). Others include
accept-charset
headers
, and
accesskey
. Beautiful Soup presents the value(s)
of a multi-valued attribute as a list:

```python
css_soup = BeautifulSoup('<p class="body"></p>')
css_soup.p['class']
# ["body"]

css_soup = BeautifulSoup('<p class="body strikeout"></p>')
css_soup.p['class']
# ["body", "strikeout"]

```

css_soup
BeautifulSoup
'<p class="body"></p>'
css_soup
'class'
# ["body"]
css_soup
BeautifulSoup
'<p class="body strikeout"></p>'
css_soup
'class'
# ["body", "strikeout"]

If an attributelookslike it has more than one value, but itâs not
a multi-valued attribute as defined by any version of the HTML
standard, Beautiful Soup will leave the attribute alone:

If an attribute
looks
like it has more than one value, but itâs not
a multi-valued attribute as defined by any version of the HTML
standard, Beautiful Soup will leave the attribute alone:

```python
id_soup = BeautifulSoup('<p id="my id"></p>')
id_soup.p['id']
# 'my id'

```

id_soup
BeautifulSoup
'<p id="my id"></p>'
id_soup
'id'
# 'my id'

When you turn a tag back into a string, multiple attribute values are
consolidated:

When you turn a tag back into a string, multiple attribute values are
consolidated:

```python
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
rel_soup.a['rel']
# ['index']
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
# <p>Back to the <a rel="index contents">homepage</a></p>

```

rel_soup
BeautifulSoup
'<p>Back to the <a rel="index">homepage</a></p>'
rel_soup
'rel'
# ['index']
rel_soup
'rel'
'index'
'contents'
print
rel_soup
# <p>Back to the <a rel="index contents">homepage</a></p>

You can disable this by passingmulti_valued_attributes=Noneas a
keyword argument into theBeautifulSoupconstructor:

You can disable this by passing
multi_valued_attributes=None
as a
keyword argument into the
BeautifulSoup
constructor:

```python
no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html', multi_valued_attributes=None)
no_list_soup.p['class']
# u'body strikeout'

```

no_list_soup
BeautifulSoup
'<p class="body strikeout"></p>'
'html'
multi_valued_attributes
None
no_list_soup
'class'
# u'body strikeout'

You can use`get_attribute_listto get a value thatâs always a
list, whether or not itâs a multi-valued atribute:

You can use
`get_attribute_list
to get a value thatâs always a
list, whether or not itâs a multi-valued atribute:

```python
id_soup.p.get_attribute_list('id')
# ["my id"]

```

id_soup
get_attribute_list
'id'
# ["my id"]

If you parse a document as XML, there are no multi-valued attributes:

If you parse a document as XML, there are no multi-valued attributes:

```python
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
xml_soup.p['class']
# u'body strikeout'

```

xml_soup
BeautifulSoup
'<p class="body strikeout"></p>'
'xml'
xml_soup
'class'
# u'body strikeout'

Again, you can configure this using themulti_valued_attributesargument:

Again, you can configure this using the
multi_valued_attributes
argument:

```python
class_is_multi= { '*' : 'class'}
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml', multi_valued_attributes=class_is_multi)
xml_soup.p['class']
# [u'body', u'strikeout']

```

class_is_multi
'class'
xml_soup
BeautifulSoup
'<p class="body strikeout"></p>'
'xml'
multi_valued_attributes
class_is_multi
xml_soup
'class'
# [u'body', u'strikeout']

You probably wonât need to do this, but if you do, use the defaults as
a guide. They implement the rules described in the HTML specification:

You probably wonât need to do this, but if you do, use the defaults as
a guide. They implement the rules described in the HTML specification:

```python
from bs4.builder import builder_registry
builder_registry.lookup('html').DEFAULT_CDATA_LIST_ATTRIBUTES

```

from
bs4.builder
import
builder_registry
builder_registry
lookup
'html'
DEFAULT_CDATA_LIST_ATTRIBUTES

### NavigableStringÂ¶

NavigableString

A string corresponds to a bit of text within a tag. Beautiful Soup
uses theNavigableStringclass to contain these bits of text:

A string corresponds to a bit of text within a tag. Beautiful Soup
uses the
NavigableString
class to contain these bits of text:

```python
tag.string
# u'Extremely bold'
type(tag.string)
# <class 'bs4.element.NavigableString'>

```

string
# u'Extremely bold'
type
string
# <class 'bs4.element.NavigableString'>

ANavigableStringis just like a Python Unicode string, except
that it also supports some of the features described inNavigating
the treeandSearching the tree. You can convert aNavigableStringto a Unicode string withunicode():

NavigableString
is just like a Python Unicode string, except
that it also supports some of the features described in
Navigating
the tree
Searching the tree
. You can convert a
NavigableString
to a Unicode string with
unicode()

```python
unicode_string = unicode(tag.string)
unicode_string
# u'Extremely bold'
type(unicode_string)
# <type 'unicode'>

```

unicode_string
unicode
string
unicode_string
# u'Extremely bold'
type
unicode_string
# <type 'unicode'>

You canât edit a string in place, but you can replace one string with
another, usingreplace_with():

You canât edit a string in place, but you can replace one string with
another, using
replace_with()

```python
tag.string.replace_with("No longer bold")
tag
# <blockquote>No longer bold</blockquote>

```

string
replace_with
"No longer bold"
# <blockquote>No longer bold</blockquote>

NavigableStringsupports most of the features described inNavigating the treeandSearching the tree, but not all of
them. In particular, since a string canât contain anything (the way a
tag may contain a string or another tag), strings donât support the.contentsor.stringattributes, or thefind()method.

NavigableString
supports most of the features described in
Navigating the tree
Searching the tree
, but not all of
them. In particular, since a string canât contain anything (the way a
tag may contain a string or another tag), strings donât support the
.contents
.string
attributes, or the
find()
method.

If you want to use aNavigableStringoutside of Beautiful Soup,
you should callunicode()on it to turn it into a normal Python
Unicode string. If you donât, your string will carry around a
reference to the entire Beautiful Soup parse tree, even when youâre
done using Beautiful Soup. This is a big waste of memory.

If you want to use a
NavigableString
outside of Beautiful Soup,
you should call
unicode()
on it to turn it into a normal Python
Unicode string. If you donât, your string will carry around a
reference to the entire Beautiful Soup parse tree, even when youâre
done using Beautiful Soup. This is a big waste of memory.

### BeautifulSoupÂ¶

BeautifulSoup

TheBeautifulSoupobject represents the parsed document as a
whole. For most purposes, you can treat it as aTagobject. This means it supports most of the methods described inNavigating the treeandSearching the tree.

BeautifulSoup
object represents the parsed document as a
whole. For most purposes, you can treat it as a
object. This means it supports most of the methods described in
Navigating the tree
Searching the tree

You can also pass aBeautifulSoupobject into one of the methods
defined inModifying the tree, just as you would aTag. This
lets you do things like combine two parsed documents:

You can also pass a
BeautifulSoup
object into one of the methods
defined in
Modifying the tree
, just as you would a
. This
lets you do things like combine two parsed documents:

```python
doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
doc.find(text="INSERT FOOTER HERE").replace_with(footer)
# u'INSERT FOOTER HERE'
print(doc)
# <?xml version="1.0" encoding="utf-8"?>
# <document><content/><footer>Here's the footer</footer></document>

```

BeautifulSoup
"<document><content/>INSERT FOOTER HERE</document"
"xml"
footer
BeautifulSoup
"<footer>Here's the footer</footer>"
"xml"
find
text
"INSERT FOOTER HERE"
replace_with
footer
# u'INSERT FOOTER HERE'
print
# <?xml version="1.0" encoding="utf-8"?>
# <document><content/><footer>Here's the footer</footer></document>

Since theBeautifulSoupobject doesnât correspond to an actual
HTML or XML tag, it has no name and no attributes. But sometimes itâs
useful to look at its.name, so itâs been given the special.nameâ[document]â:

Since the
BeautifulSoup
object doesnât correspond to an actual
HTML or XML tag, it has no name and no attributes. But sometimes itâs
useful to look at its
.name
, so itâs been given the special
.name
â[document]â:

```python
soup.name
# u'[document]'

```

soup
name
# u'[document]'

### Comments and other special stringsÂ¶

Comments and other special strings

Tag,NavigableString, andBeautifulSoupcover almost
everything youâll see in an HTML or XML file, but there are a few
leftover bits. The only one youâll probably ever need to worry about
is the comment:

NavigableString
, and
BeautifulSoup
cover almost
everything youâll see in an HTML or XML file, but there are a few
leftover bits. The only one youâll probably ever need to worry about
is the comment:

```python
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup)
comment = soup.b.string
type(comment)
# <class 'bs4.element.Comment'>

```

markup
"<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup
BeautifulSoup
markup
comment
soup
string
type
comment
# <class 'bs4.element.Comment'>

TheCommentobject is just a special type ofNavigableString:

Comment
object is just a special type of
NavigableString

```python
comment
# u'Hey, buddy. Want to buy a used parser'

```

comment
# u'Hey, buddy. Want to buy a used parser'

But when it appears as part of an HTML document, aCommentis
displayed with special formatting:

But when it appears as part of an HTML document, a
Comment
is
displayed with special formatting:

```python
print(soup.b.prettify())
# <b>
# <!--Hey, buddy. Want to buy a used parser?-->
# </b>

```

print
soup
prettify
# <b>
# <!--Hey, buddy. Want to buy a used parser?-->
# </b>

Beautiful Soup defines classes for anything else that might show up in
an XML document:CData,ProcessingInstruction,Declaration, andDoctype. Just likeComment, these classes
are subclasses ofNavigableStringthat add something extra to the
string. Hereâs an example that replaces the comment with a CDATA
block:

Beautiful Soup defines classes for anything else that might show up in
an XML document:
CData
ProcessingInstruction
Declaration
, and
Doctype
. Just like
Comment
, these classes
are subclasses of
NavigableString
that add something extra to the
string. Hereâs an example that replaces the comment with a CDATA
block:

```python
from bs4 import CData
cdata = CData("A CDATA block")
comment.replace_with(cdata)

print(soup.b.prettify())
# <b>
# <![CDATA[A CDATA block]]>
# </b>

```

from
import
CData
cdata
CData
"A CDATA block"
comment
replace_with
cdata
print
soup
prettify
# <b>
# <![CDATA[A CDATA block]]>
# </b>

## Navigating the treeÂ¶

Navigating the tree

Hereâs the âThree sistersâ HTML document again:

Hereâs the âThree sistersâ HTML document again:

```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

```

html_doc
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
from
import
BeautifulSoup
soup
BeautifulSoup
html_doc
'html.parser'

Iâll use this as an example to show you how to move from one part of
a document to another.

Iâll use this as an example to show you how to move from one part of
a document to another.

### Going downÂ¶

Going down

Tags may contain strings and other tags. These elements are the tagâschildren. Beautiful Soup provides a lot of different attributes for
navigating and iterating over a tagâs children.

Tags may contain strings and other tags. These elements are the tagâs
children
. Beautiful Soup provides a lot of different attributes for
navigating and iterating over a tagâs children.

Note that Beautiful Soup strings donât support any of these
attributes, because a string canât have children.

Note that Beautiful Soup strings donât support any of these
attributes, because a string canât have children.

#### Navigating using tag namesÂ¶

Navigating using tag names

The simplest way to navigate the parse tree is to say the name of the
tag you want. If you want the <head> tag, just saysoup.head:

The simplest way to navigate the parse tree is to say the name of the
tag you want. If you want the <head> tag, just say
soup.head

```python
soup.head
# <head><title>The Dormouse's story</title></head>

soup.title
# <title>The Dormouse's story</title>

```

soup
head
# <head><title>The Dormouse's story</title></head>
soup
title
# <title>The Dormouse's story</title>

You can do use this trick again and again to zoom in on a certain part
of the parse tree. This code gets the first <b> tag beneath the <body> tag:

You can do use this trick again and again to zoom in on a certain part
of the parse tree. This code gets the first <b> tag beneath the <body> tag:

```python
soup.body.b
# <b>The Dormouse's story</b>

```

soup
body
# <b>The Dormouse's story</b>

Using a tag name as an attribute will give you only thefirsttag by that
name:

Using a tag name as an attribute will give you only the
first
tag by that
name:

```python
soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

```

soup
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

If you need to getallthe <a> tags, or anything more complicated
than the first tag with a certain name, youâll need to use one of the
methods described inSearching the tree, such asfind_all():

If you need to get
the <a> tags, or anything more complicated
than the first tag with a certain name, youâll need to use one of the
methods described in
Searching the tree
, such as
find_all()

```python
soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

```

soup
find_all
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

#### .contentsand.childrenÂ¶

.contents
.children

A tagâs children are available in a list called.contents:

A tagâs children are available in a list called
.contents

```python
head_tag = soup.head
head_tag
# <head><title>The Dormouse's story</title></head>

head_tag.contents
[<title>The Dormouse's story</title>]

title_tag = head_tag.contents[0]
title_tag
# <title>The Dormouse's story</title>
title_tag.contents
# [u'The Dormouse's story']

```

head_tag
soup
head
head_tag
# <head><title>The Dormouse's story</title></head>
head_tag
contents
title
Dormouse
's story</title>]
title_tag
head_tag
contents
title_tag
# <title>The Dormouse's story</title>
title_tag
contents
# [u'The Dormouse's story']

TheBeautifulSoupobject itself has children. In this case, the
<html> tag is the child of theBeautifulSoupobject.:

BeautifulSoup
object itself has children. In this case, the
<html> tag is the child of the
BeautifulSoup
object.:

```python
len(soup.contents)
# 1
soup.contents[0].name
# u'html'

```

soup
contents
soup
contents
name
# u'html'

A string does not have.contents, because it canât contain
anything:

A string does not have
.contents
, because it canât contain
anything:

```python
text = title_tag.contents[0]
text.contents
# AttributeError: 'NavigableString' object has no attribute 'contents'

```

text
title_tag
contents
text
contents
# AttributeError: 'NavigableString' object has no attribute 'contents'

Instead of getting them as a list, you can iterate over a tagâs
children using the.childrengenerator:

Instead of getting them as a list, you can iterate over a tagâs
children using the
.children
generator:

```python
for child in title_tag.children:
 print(child)
# The Dormouse's story

```

child
title_tag
children
print
child
# The Dormouse's story

#### .descendantsÂ¶

.descendants

The.contentsand.childrenattributes only consider a tagâsdirectchildren. For instance, the <head> tag has a single direct
childâthe <title> tag:

.contents
.children
attributes only consider a tagâs
direct
children. For instance, the <head> tag has a single direct
childâthe <title> tag:

```python
head_tag.contents
# [<title>The Dormouse's story</title>]

```

head_tag
contents
# [<title>The Dormouse's story</title>]

But the <title> tag itself has a child: the string âThe Dormouseâs
storyâ. Thereâs a sense in which that string is also a child of the
<head> tag. The.descendantsattribute lets you iterate overallof a tagâs children, recursively: its direct children, the children of
its direct children, and so on:

But the <title> tag itself has a child: the string âThe Dormouseâs
storyâ. Thereâs a sense in which that string is also a child of the
<head> tag. The
.descendants
attribute lets you iterate over
of a tagâs children, recursively: its direct children, the children of
its direct children, and so on:

```python
for child in head_tag.descendants:
 print(child)
# <title>The Dormouse's story</title>
# The Dormouse's story

```

child
head_tag
descendants
print
child
# <title>The Dormouse's story</title>
# The Dormouse's story

The <head> tag has only one child, but it has two descendants: the
<title> tag and the <title> tagâs child. TheBeautifulSoupobject
only has one direct child (the <html> tag), but it has a whole lot of
descendants:

The <head> tag has only one child, but it has two descendants: the
<title> tag and the <title> tagâs child. The
BeautifulSoup
object
only has one direct child (the <html> tag), but it has a whole lot of
descendants:

```python
len(list(soup.children))
# 1
len(list(soup.descendants))
# 25

```

list
soup
children
list
soup
descendants
# 25

#### .stringÂ¶

.string

If a tag has only one child, and that child is aNavigableString,
the child is made available as.string:

If a tag has only one child, and that child is a
NavigableString
,
the child is made available as
.string

```python
title_tag.string
# u'The Dormouse's story'

```

title_tag
string
# u'The Dormouse's story'

If a tagâs only child is another tag, andthattag has a.string, then the parent tag is considered to have the same.stringas its child:

If a tagâs only child is another tag, and
that
tag has a
.string
, then the parent tag is considered to have the same
.string
as its child:

```python
head_tag.contents
# [<title>The Dormouse's story</title>]

head_tag.string
# u'The Dormouse's story'

```

head_tag
contents
# [<title>The Dormouse's story</title>]
head_tag
string
# u'The Dormouse's story'

If a tag contains more than one thing, then itâs not clear what.stringshould refer to, so.stringis defined to beNone:

If a tag contains more than one thing, then itâs not clear what
.string
should refer to, so
.string
is defined to be
None

```python
print(soup.html.string)
# None

```

print
soup
html
string
# None

#### .stringsandstripped_stringsÂ¶

.strings
stripped_strings

If thereâs more than one thing inside a tag, you can still look at
just the strings. Use the.stringsgenerator:

If thereâs more than one thing inside a tag, you can still look at
just the strings. Use the
.strings
generator:

```python
for string in soup.strings:
 print(repr(string))
# u"The Dormouse's story"
# u'\n\n'
# u"The Dormouse's story"
# u'\n\n'
# u'Once upon a time there were three little sisters; and their names were\n'
# u'Elsie'
# u',\n'
# u'Lacie'
# u' and\n'
# u'Tillie'
# u';\nand they lived at the bottom of a well.'
# u'\n\n'
# u'...'
# u'\n'

```

string
soup
strings
print
repr
string
# u"The Dormouse's story"
# u'\n\n'
# u"The Dormouse's story"
# u'\n\n'
# u'Once upon a time there were three little sisters; and their names were\n'
# u'Elsie'
# u',\n'
# u'Lacie'
# u' and\n'
# u'Tillie'
# u';\nand they lived at the bottom of a well.'
# u'\n\n'
# u'...'
# u'\n'

These strings tend to have a lot of extra whitespace, which you can
remove by using the.stripped_stringsgenerator instead:

These strings tend to have a lot of extra whitespace, which you can
remove by using the
.stripped_strings
generator instead:

```python
for string in soup.stripped_strings:
 print(repr(string))
# u"The Dormouse's story"
# u"The Dormouse's story"
# u'Once upon a time there were three little sisters; and their names were'
# u'Elsie'
# u','
# u'Lacie'
# u'and'
# u'Tillie'
# u';\nand they lived at the bottom of a well.'
# u'...'

```

string
soup
stripped_strings
print
repr
string
# u"The Dormouse's story"
# u"The Dormouse's story"
# u'Once upon a time there were three little sisters; and their names were'
# u'Elsie'
# u','
# u'Lacie'
# u'and'
# u'Tillie'
# u';\nand they lived at the bottom of a well.'
# u'...'

Here, strings consisting entirely of whitespace are ignored, and
whitespace at the beginning and end of strings is removed.

Here, strings consisting entirely of whitespace are ignored, and
whitespace at the beginning and end of strings is removed.

### Going upÂ¶

Going up

Continuing the âfamily treeâ analogy, every tag and every string has aparent: the tag that contains it.

Continuing the âfamily treeâ analogy, every tag and every string has a
parent
: the tag that contains it.

#### .parentÂ¶

.parent

You can access an elementâs parent with the.parentattribute. In
the example âthree sistersâ document, the <head> tag is the parent
of the <title> tag:

You can access an elementâs parent with the
.parent
attribute. In
the example âthree sistersâ document, the <head> tag is the parent
of the <title> tag:

```python
title_tag = soup.title
title_tag
# <title>The Dormouse's story</title>
title_tag.parent
# <head><title>The Dormouse's story</title></head>

```

title_tag
soup
title
title_tag
# <title>The Dormouse's story</title>
title_tag
parent
# <head><title>The Dormouse's story</title></head>

The title string itself has a parent: the <title> tag that contains
it:

The title string itself has a parent: the <title> tag that contains
it:

```python
title_tag.string.parent
# <title>The Dormouse's story</title>

```

title_tag
string
parent
# <title>The Dormouse's story</title>

The parent of a top-level tag like <html> is theBeautifulSoupobject
itself:

The parent of a top-level tag like <html> is the
BeautifulSoup
object
itself:

```python
html_tag = soup.html
type(html_tag.parent)
# <class 'bs4.BeautifulSoup'>

```

html_tag
soup
html
type
html_tag
parent
# <class 'bs4.BeautifulSoup'>

And the.parentof aBeautifulSoupobject is defined as None:

And the
.parent
of a
BeautifulSoup
object is defined as None:

```python
print(soup.parent)
# None

```

print
soup
parent
# None

#### .parentsÂ¶

.parents

You can iterate over all of an elementâs parents with.parents. This example uses.parentsto travel from an <a> tag
buried deep within the document, to the very top of the document:

You can iterate over all of an elementâs parents with
.parents
. This example uses
.parents
to travel from an <a> tag
buried deep within the document, to the very top of the document:

```python
link = soup.a
link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
for parent in link.parents:
 if parent is None:
 print(parent)
 else:
 print(parent.name)
# p
# body
# html
# [document]
# None

```

link
soup
link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
parent
link
parents
parent
None
print
parent
else
print
parent
name
# body
# html
# [document]
# None

### Going sidewaysÂ¶

Going sideways

Consider a simple document like this:

Consider a simple document like this:

```python
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
print(sibling_soup.prettify())
# <html>
# <body>
# <a>
# <b>
# text1
# </b>
# <c>
# text2
# </c>
# </a>
# </body>
# </html>

```

sibling_soup
BeautifulSoup
"<a><b>text1</b><c>text2</c></b></a>"
print
sibling_soup
prettify
# <html>
# <body>
# <a>
# <b>
# text1
# </b>
# <c>
# text2
# </c>
# </a>
# </body>
# </html>

The <b> tag and the <c> tag are at the same level: theyâre both direct
children of the same tag. We call themsiblings. When a document is
pretty-printed, siblings show up at the same indentation level. You
can also use this relationship in the code you write.

The <b> tag and the <c> tag are at the same level: theyâre both direct
children of the same tag. We call them
siblings
. When a document is
pretty-printed, siblings show up at the same indentation level. You
can also use this relationship in the code you write.

#### .next_siblingand.previous_siblingÂ¶

You can use.next_siblingand.previous_siblingto navigate
between page elements that are on the same level of the parse tree:

You can use
to navigate
between page elements that are on the same level of the parse tree:

```python
sibling_soup.b.next_sibling
# <c>text2</c>

sibling_soup.c.previous_sibling
# <b>text1</b>

```

sibling_soup
# <c>text2</c>
sibling_soup
# <b>text1</b>

The <b> tag has a.next_sibling, but no.previous_sibling,
because thereâs nothing before the <b> tagon the same level of the
tree. For the same reason, the <c> tag has a.previous_siblingbut no.next_sibling:

The <b> tag has a
, but no
,
because thereâs nothing before the <b> tag
on the same level of the
tree
. For the same reason, the <c> tag has a
but no

```python
print(sibling_soup.b.previous_sibling)
# None
print(sibling_soup.c.next_sibling)
# None

```

print
sibling_soup
# None
print
sibling_soup
# None

The strings âtext1â and âtext2â arenotsiblings, because they donât
have the same parent:

The strings âtext1â and âtext2â are
siblings, because they donât
have the same parent:

```python
sibling_soup.b.string
# u'text1'

print(sibling_soup.b.string.next_sibling)
# None

```

sibling_soup
string
# u'text1'
print
sibling_soup
string
# None

In real documents, the.next_siblingor.previous_siblingof a
tag will usually be a string containing whitespace. Going back to the
âthree sistersâ document:

In real documents, the
of a
tag will usually be a string containing whitespace. Going back to the
âthree sistersâ document:

```python
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>

```

href
"http://example.com/elsie"
class
"sister"
"link1"
Elsie
href
"http://example.com/lacie"
class
"sister"
"link2"
Lacie
href
"http://example.com/tillie"
class
"sister"
"link3"
Tillie

You might think that the.next_siblingof the first <a> tag would
be the second <a> tag. But actually, itâs a string: the comma and
newline that separate the first <a> tag from the second:

You might think that the
of the first <a> tag would
be the second <a> tag. But actually, itâs a string: the comma and
newline that separate the first <a> tag from the second:

```python
link = soup.a
link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

link.next_sibling
# u',\n'

```

link
soup
link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
link
# u',\n'

The second <a> tag is actually the.next_siblingof the comma:

The second <a> tag is actually the
of the comma:

```python
link.next_sibling.next_sibling
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>

```

link
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>

#### .next_siblingsand.previous_siblingsÂ¶

You can iterate over a tagâs siblings with.next_siblingsor.previous_siblings:

You can iterate over a tagâs siblings with

```python
for sibling in soup.a.next_siblings:
 print(repr(sibling))
# u',\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# u' and\n'
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# u'; and they lived at the bottom of a well.'
# None

for sibling in soup.find(id="link3").previous_siblings:
 print(repr(sibling))
# ' and\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# u',\n'
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# u'Once upon a time there were three little sisters; and their names were\n'
# None

```

sibling
soup
print
repr
sibling
# u',\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# u' and\n'
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# u'; and they lived at the bottom of a well.'
# None
sibling
soup
find
"link3"
print
repr
sibling
# ' and\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# u',\n'
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# u'Once upon a time there were three little sisters; and their names were\n'
# None

### Going back and forthÂ¶

Going back and forth

Take a look at the beginning of the âthree sistersâ document:

Take a look at the beginning of the âthree sistersâ document:

```python
<html><head><title>The Dormouse's story</title></head>
<p class="title"><b>The Dormouse's story</b></p>

```

html
head
title
Dormouse
's story</title></head>
class
"title"
Dormouse
's story</b></p>

An HTML parser takes this string of characters and turns it into a
series of events: âopen an <html> tagâ, âopen a <head> tagâ, âopen a
<title> tagâ, âadd a stringâ, âclose the <title> tagâ, âopen a <p>
tagâ, and so on. Beautiful Soup offers tools for reconstructing the
initial parse of the document.

An HTML parser takes this string of characters and turns it into a
series of events: âopen an <html> tagâ, âopen a <head> tagâ, âopen a
<title> tagâ, âadd a stringâ, âclose the <title> tagâ, âopen a <p>
tagâ, and so on. Beautiful Soup offers tools for reconstructing the
initial parse of the document.

#### .next_elementand.previous_elementÂ¶

The.next_elementattribute of a string or tag points to whatever
was parsed immediately afterwards. It might be the same as.next_sibling, but itâs usually drastically different.

attribute of a string or tag points to whatever
was parsed immediately afterwards. It might be the same as
, but itâs usually drastically different.

Hereâs the final <a> tag in the âthree sistersâ document. Its.next_siblingis a string: the conclusion of the sentence that was
interrupted by the start of the <a> tag.:

Hereâs the final <a> tag in the âthree sistersâ document. Its
is a string: the conclusion of the sentence that was
interrupted by the start of the <a> tag.:

```python
last_a_tag = soup.find("a", id="link3")
last_a_tag
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

last_a_tag.next_sibling
# '; and they lived at the bottom of a well.'

```

last_a_tag
soup
find
"link3"
last_a_tag
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
last_a_tag
# '; and they lived at the bottom of a well.'

But the.next_elementof that <a> tag, the thing that was parsed
immediately after the <a> tag, isnotthe rest of that sentence:
itâs the word âTillieâ:

But the
of that <a> tag, the thing that was parsed
immediately after the <a> tag, is
the rest of that sentence:
itâs the word âTillieâ:

```python
last_a_tag.next_element
# u'Tillie'

```

last_a_tag
# u'Tillie'

Thatâs because in the original markup, the word âTillieâ appeared
before that semicolon. The parser encountered an <a> tag, then the
word âTillieâ, then the closing </a> tag, then the semicolon and rest of
the sentence. The semicolon is on the same level as the <a> tag, but the
word âTillieâ was encountered first.

Thatâs because in the original markup, the word âTillieâ appeared
before that semicolon. The parser encountered an <a> tag, then the
word âTillieâ, then the closing </a> tag, then the semicolon and rest of
the sentence. The semicolon is on the same level as the <a> tag, but the
word âTillieâ was encountered first.

The.previous_elementattribute is the exact opposite of.next_element. It points to whatever element was parsed
immediately before this one:

attribute is the exact opposite of
. It points to whatever element was parsed
immediately before this one:

```python
last_a_tag.previous_element
# u' and\n'
last_a_tag.previous_element.next_element
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

```

last_a_tag
# u' and\n'
last_a_tag
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

#### .next_elementsand.previous_elementsÂ¶

You should get the idea by now. You can use these iterators to move
forward or backward in the document as it was parsed:

You should get the idea by now. You can use these iterators to move
forward or backward in the document as it was parsed:

```python
for element in last_a_tag.next_elements:
 print(repr(element))
# u'Tillie'
# u';\nand they lived at the bottom of a well.'
# u'\n\n'
# <p class="story">...</p>
# u'...'
# u'\n'
# None

```

element
last_a_tag
print
repr
element
# u'Tillie'
# u';\nand they lived at the bottom of a well.'
# u'\n\n'
# <p class="story">...</p>
# u'...'
# u'\n'
# None

## Searching the treeÂ¶

Searching the tree

Beautiful Soup defines a lot of methods for searching the parse tree,
but theyâre all very similar. Iâm going to spend a lot of time explaining
the two most popular methods:find()andfind_all(). The other
methods take almost exactly the same arguments, so Iâll just cover
them briefly.

Beautiful Soup defines a lot of methods for searching the parse tree,
but theyâre all very similar. Iâm going to spend a lot of time explaining
the two most popular methods:
find()
find_all()
. The other
methods take almost exactly the same arguments, so Iâll just cover
them briefly.

Once again, Iâll be using the âthree sistersâ document as an example:

Once again, Iâll be using the âthree sistersâ document as an example:

```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

```

html_doc
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
from
import
BeautifulSoup
soup
BeautifulSoup
html_doc
'html.parser'

By passing in a filter to an argument likefind_all(), you can
zoom in on the parts of the document youâre interested in.

By passing in a filter to an argument like
find_all()
, you can
zoom in on the parts of the document youâre interested in.

### Kinds of filtersÂ¶

Kinds of filters

Before talking in detail aboutfind_all()and similar methods, I
want to show examples of different filters you can pass into these
methods. These filters show up again and again, throughout the
search API. You can use them to filter based on a tagâs name,
on its attributes, on the text of a string, or on some combination of
these.

Before talking in detail about
find_all()
and similar methods, I
want to show examples of different filters you can pass into these
methods. These filters show up again and again, throughout the
search API. You can use them to filter based on a tagâs name,
on its attributes, on the text of a string, or on some combination of
these.

#### A stringÂ¶

A string

The simplest filter is a string. Pass a string to a search method and
Beautiful Soup will perform a match against that exact string. This
code finds all the <b> tags in the document:

The simplest filter is a string. Pass a string to a search method and
Beautiful Soup will perform a match against that exact string. This
code finds all the <b> tags in the document:

```python
soup.find_all('b')
# [<b>The Dormouse's story</b>]

```

soup
find_all
# [<b>The Dormouse's story</b>]

If you pass in a byte string, Beautiful Soup will assume the string is
encoded as UTF-8. You can avoid this by passing in a Unicode string instead.

If you pass in a byte string, Beautiful Soup will assume the string is
encoded as UTF-8. You can avoid this by passing in a Unicode string instead.

#### A regular expressionÂ¶

A regular expression

If you pass in a regular expression object, Beautiful Soup will filter
against that regular expression using itssearch()method. This code
finds all the tags whose names start with the letter âbâ; in this
case, the <body> tag and the <b> tag:

If you pass in a regular expression object, Beautiful Soup will filter
against that regular expression using its
search()
method. This code
finds all the tags whose names start with the letter âbâ; in this
case, the <body> tag and the <b> tag:

```python
import re
for tag in soup.find_all(re.compile("^b")):
 print(tag.name)
# body
# b

```

import
soup
find_all
compile
"^b"
print
name
# body

This code finds all the tags whose names contain the letter âtâ:

This code finds all the tags whose names contain the letter âtâ:

```python
for tag in soup.find_all(re.compile("t")):
 print(tag.name)
# html
# title

```

soup
find_all
compile
print
name
# html
# title

#### A listÂ¶

A list

If you pass in a list, Beautiful Soup will allow a string match
againstanyitem in that list. This code finds all the <a> tagsandall the <b> tags:

If you pass in a list, Beautiful Soup will allow a string match
against
item in that list. This code finds all the <a> tags
all the <b> tags:

```python
soup.find_all(["a", "b"])
# [<b>The Dormouse's story</b>,
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

```

soup
find_all
# [<b>The Dormouse's story</b>,
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

#### TrueÂ¶

True

The valueTruematches everything it can. This code findsallthe tags in the document, but none of the text strings:

The value
True
matches everything it can. This code finds
the tags in the document, but none of the text strings:

```python
for tag in soup.find_all(True):
 print(tag.name)
# html
# head
# title
# body
# p
# b
# p
# a
# a
# a
# p

```

soup
find_all
True
print
name
# html
# head
# title
# body

#### A functionÂ¶

A function

If none of the other matches work for you, define a function that
takes an element as its only argument. The function should returnTrueif the argument matches, andFalseotherwise.

If none of the other matches work for you, define a function that
takes an element as its only argument. The function should return
True
if the argument matches, and
False
otherwise.

Hereâs a function that returnsTrueif a tag defines the âclassâ
attribute but doesnât define the âidâ attribute:

Hereâs a function that returns
True
if a tag defines the âclassâ
attribute but doesnât define the âidâ attribute:

```python
def has_class_but_no_id(tag):
 return tag.has_attr('class') and not tag.has_attr('id')

```

has_class_but_no_id
return
has_attr
'class'
has_attr
'id'

Pass this function intofind_all()and youâll pick up all the <p>
tags:

Pass this function into
find_all()
and youâll pick up all the <p>
tags:

```python
soup.find_all(has_class_but_no_id)
# [<p class="title"><b>The Dormouse's story</b></p>,
# <p class="story">Once upon a time there were...</p>,
# <p class="story">...</p>]

```

soup
find_all
has_class_but_no_id
# [<p class="title"><b>The Dormouse's story</b></p>,
# <p class="story">Once upon a time there were...</p>,
# <p class="story">...</p>]

This function only picks up the <p> tags. It doesnât pick up the <a>
tags, because those tags define both âclassâ and âidâ. It doesnât pick
up tags like <html> and <title>, because those tags donât define
âclassâ.

This function only picks up the <p> tags. It doesnât pick up the <a>
tags, because those tags define both âclassâ and âidâ. It doesnât pick
up tags like <html> and <title>, because those tags donât define
âclassâ.

If you pass in a function to filter on a specific attribute likehref, the argument passed into the function will be the attribute
value, not the whole tag. Hereâs a function that finds allatags
whosehrefattributedoes notmatch a regular expression:

If you pass in a function to filter on a specific attribute like
href
, the argument passed into the function will be the attribute
value, not the whole tag. Hereâs a function that finds all
tags
whose
href
attribute
does not
match a regular expression:

```python
def not_lacie(href):
 return href and not re.compile("lacie").search(href)
soup.find_all(href=not_lacie)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

```

not_lacie
href
return
href
compile
"lacie"
search
href
soup
find_all
href
not_lacie
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

The function can be as complicated as you need it to be. Hereâs a
function that returnsTrueif a tag is surrounded by string
objects:

The function can be as complicated as you need it to be. Hereâs a
function that returns
True
if a tag is surrounded by string
objects:

```python
from bs4 import NavigableString
def surrounded_by_strings(tag):
 return (isinstance(tag.next_element, NavigableString)
 and isinstance(tag.previous_element, NavigableString))

for tag in soup.find_all(surrounded_by_strings):
 print tag.name
# p
# a
# a
# a
# p

```

from
import
NavigableString
surrounded_by_strings
return
isinstance
NavigableString
isinstance
NavigableString
soup
find_all
surrounded_by_strings
print
name

Now weâre ready to look at the search methods in detail.

Now weâre ready to look at the search methods in detail.

### find_all()Â¶

find_all()

Signature: find_all(name,attrs,recursive,string,limit,**kwargs)

Signature: find_all(
name
attrs
recursive
string
limit
**kwargs

Thefind_all()method looks through a tagâs descendants and
retrievesalldescendants that match your filters. I gave several
examples inKinds of filters, but here are a few more:

find_all()
method looks through a tagâs descendants and
retrieves
descendants that match your filters. I gave several
examples in
Kinds of filters
, but here are a few more:

```python
soup.find_all("title")
# [<title>The Dormouse's story</title>]

soup.find_all("p", "title")
# [<p class="title"><b>The Dormouse's story</b></p>]

soup.find_all("a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(id="link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

import re
soup.find(string=re.compile("sisters"))
# u'Once upon a time there were three little sisters; and their names were\n'

```

soup
find_all
"title"
# [<title>The Dormouse's story</title>]
soup
find_all
"title"
# [<p class="title"><b>The Dormouse's story</b></p>]
soup
find_all
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup
find_all
"link2"
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
import
soup
find
string
compile
"sisters"
# u'Once upon a time there were three little sisters; and their names were\n'

Some of these should look familiar, but others are new. What does it
mean to pass in a value forstring, orid? Why doesfind_all("p","title")find a <p> tag with the CSS class âtitleâ?
Letâs look at the arguments tofind_all().

Some of these should look familiar, but others are new. What does it
mean to pass in a value for
string
, or
? Why does
find_all("p",
"title")
find a <p> tag with the CSS class âtitleâ?
Letâs look at the arguments to
find_all()

#### ThenameargumentÂ¶

name
argument

Pass in a value fornameand youâll tell Beautiful Soup to only
consider tags with certain names. Text strings will be ignored, as
will tags whose names that donât match.

Pass in a value for
name
and youâll tell Beautiful Soup to only
consider tags with certain names. Text strings will be ignored, as
will tags whose names that donât match.

This is the simplest usage:

This is the simplest usage:

```python
soup.find_all("title")
# [<title>The Dormouse's story</title>]

```

soup
find_all
"title"
# [<title>The Dormouse's story</title>]

Recall fromKinds of filtersthat the value tonamecan bea
string,a regular expression,a list,a function, orthe value
True.

Recall from
Kinds of filters
that the value to
name
can be
a
string
a regular expression
a list
a function
, or
the value
True

#### The keyword argumentsÂ¶

The keyword arguments

Any argument thatâs not recognized will be turned into a filter on one
of a tagâs attributes. If you pass in a value for an argument calledid,
Beautiful Soup will filter against each tagâs âidâ attribute:

Any argument thatâs not recognized will be turned into a filter on one
of a tagâs attributes. If you pass in a value for an argument called
,
Beautiful Soup will filter against each tagâs âidâ attribute:

```python
soup.find_all(id='link2')
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

```

soup
find_all
'link2'
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

If you pass in a value forhref, Beautiful Soup will filter
against each tagâs âhrefâ attribute:

If you pass in a value for
href
, Beautiful Soup will filter
against each tagâs âhrefâ attribute:

```python
soup.find_all(href=re.compile("elsie"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

```

soup
find_all
href
compile
"elsie"
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

You can filter an attribute based ona string,a regular
expression,a list,a function, orthe value True.

You can filter an attribute based on
a string
a regular
expression
a list
a function
, or
the value True

This code finds all tags whoseidattribute has a value,
regardless of what the value is:

This code finds all tags whose
attribute has a value,
regardless of what the value is:

```python
soup.find_all(id=True)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

```

soup
find_all
True
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

You can filter multiple attributes at once by passing in more than one
keyword argument:

You can filter multiple attributes at once by passing in more than one
keyword argument:

```python
soup.find_all(href=re.compile("elsie"), id='link1')
# [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]

```

soup
find_all
href
compile
"elsie"
'link1'
# [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]

Some attributes, like the data-* attributes in HTML 5, have names that
canât be used as the names of keyword arguments:

Some attributes, like the data-* attributes in HTML 5, have names that
canât be used as the names of keyword arguments:

```python
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(data-foo="value")
# SyntaxError: keyword can't be an expression

```

data_soup
BeautifulSoup
'<div data-foo="value">foo!</div>'
data_soup
find_all
data
"value"
# SyntaxError: keyword can't be an expression

You can use these attributes in searches by putting them into a
dictionary and passing the dictionary intofind_all()as theattrsargument:

You can use these attributes in searches by putting them into a
dictionary and passing the dictionary into
find_all()
as the
attrs
argument:

```python
data_soup.find_all(attrs={"data-foo": "value"})
# [<div data-foo="value">foo!</div>]

```

data_soup
find_all
attrs
"data-foo"
"value"
# [<div data-foo="value">foo!</div>]

You canât use a keyword argument to search for HTMLâs ânameâ element,
because Beautiful Soup uses thenameargument to contain the name
of the tag itself. Instead, you can give a value to ânameâ in theattrsargument:

You canât use a keyword argument to search for HTMLâs ânameâ element,
because Beautiful Soup uses the
name
argument to contain the name
of the tag itself. Instead, you can give a value to ânameâ in the
attrs
argument:

```python
name_soup = BeautifulSoup('<input name="email"/>')
name_soup.find_all(name="email")
# []
name_soup.find_all(attrs={"name": "email"})
# [<input name="email"/>]

```

name_soup
BeautifulSoup
'<input name="email"/>'
name_soup
find_all
name
"email"
# []
name_soup
find_all
attrs
"name"
"email"
# [<input name="email"/>]

#### Searching by CSS classÂ¶

Searching by CSS class

Itâs very useful to search for a tag that has a certain CSS class, but
the name of the CSS attribute, âclassâ, is a reserved word in
Python. Usingclassas a keyword argument will give you a syntax
error. As of Beautiful Soup 4.1.2, you can search by CSS class using
the keyword argumentclass_:

Itâs very useful to search for a tag that has a certain CSS class, but
the name of the CSS attribute, âclassâ, is a reserved word in
Python. Using
class
as a keyword argument will give you a syntax
error. As of Beautiful Soup 4.1.2, you can search by CSS class using
the keyword argument
class_

```python
soup.find_all("a", class_="sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

```

soup
find_all
class_
"sister"
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

As with any keyword argument, you can passclass_a string, a regular
expression, a function, orTrue:

As with any keyword argument, you can pass
class_
a string, a regular
expression, a function, or
True

```python
soup.find_all(class_=re.compile("itl"))
# [<p class="title"><b>The Dormouse's story</b></p>]

def has_six_characters(css_class):
 return css_class is not None and len(css_class) == 6

soup.find_all(class_=has_six_characters)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

```

soup
find_all
class_
compile
"itl"
# [<p class="title"><b>The Dormouse's story</b></p>]
has_six_characters
css_class
return
css_class
None
css_class
soup
find_all
class_
has_six_characters
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

Rememberthat a single tag can have multiple
values for its âclassâ attribute. When you search for a tag that
matches a certain CSS class, youâre matching againstanyof its CSS
classes:

Remember
that a single tag can have multiple
values for its âclassâ attribute. When you search for a tag that
matches a certain CSS class, youâre matching against
of its CSS
classes:

```python
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
css_soup.find_all("p", class_="strikeout")
# [<p class="body strikeout"></p>]

css_soup.find_all("p", class_="body")
# [<p class="body strikeout"></p>]

```

css_soup
BeautifulSoup
'<p class="body strikeout"></p>'
css_soup
find_all
class_
"strikeout"
# [<p class="body strikeout"></p>]
css_soup
find_all
class_
"body"
# [<p class="body strikeout"></p>]

You can also search for the exact string value of theclassattribute:

You can also search for the exact string value of the
class
attribute:

```python
css_soup.find_all("p", class_="body strikeout")
# [<p class="body strikeout"></p>]

```

css_soup
find_all
class_
"body strikeout"
# [<p class="body strikeout"></p>]

But searching for variants of the string value wonât work:

But searching for variants of the string value wonât work:

```python
css_soup.find_all("p", class_="strikeout body")
# []

```

css_soup
find_all
class_
"strikeout body"
# []

If you want to search for tags that match two or more CSS classes, you
should use a CSS selector:

If you want to search for tags that match two or more CSS classes, you
should use a CSS selector:

```python
css_soup.select("p.strikeout.body")
# [<p class="body strikeout"></p>]

```

css_soup
select
"p.strikeout.body"
# [<p class="body strikeout"></p>]

In older versions of Beautiful Soup, which donât have theclass_shortcut, you can use theattrstrick mentioned above. Create a
dictionary whose value for âclassâ is the string (or regular
expression, or whatever) you want to search for:

In older versions of Beautiful Soup, which donât have the
class_
shortcut, you can use the
attrs
trick mentioned above. Create a
dictionary whose value for âclassâ is the string (or regular
expression, or whatever) you want to search for:

```python
soup.find_all("a", attrs={"class": "sister"})
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

```

soup
find_all
attrs
"class"
"sister"
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

#### ThestringargumentÂ¶

string
argument

Withstringyou can search for strings instead of tags. As withnameand the keyword arguments, you can pass ina string,a
regular expression,a list,a function, orthe value True.
Here are some examples:

With
string
you can search for strings instead of tags. As with
name
and the keyword arguments, you can pass in
a string
a
regular expression
a list
a function
, or
the value True
.
Here are some examples:

```python
soup.find_all(string="Elsie")
# [u'Elsie']

soup.find_all(string=["Tillie", "Elsie", "Lacie"])
# [u'Elsie', u'Lacie', u'Tillie']

soup.find_all(string=re.compile("Dormouse"))
[u"The Dormouse's story", u"The Dormouse's story"]

def is_the_only_string_within_a_tag(s):
 """Return True if this string is the only child of its parent tag."""
 return (s == s.parent.string)

soup.find_all(string=is_the_only_string_within_a_tag)
# [u"The Dormouse's story", u"The Dormouse's story", u'Elsie', u'Lacie', u'Tillie', u'...']

```

soup
find_all
string
"Elsie"
# [u'Elsie']
soup
find_all
string
"Tillie"
"Elsie"
"Lacie"
# [u'Elsie', u'Lacie', u'Tillie']
soup
find_all
string
compile
"Dormouse"
"The Dormouse's story"
"The Dormouse's story"
is_the_only_string_within_a_tag
"""Return True if this string is the only child of its parent tag."""
return
parent
string
soup
find_all
string
is_the_only_string_within_a_tag
# [u"The Dormouse's story", u"The Dormouse's story", u'Elsie', u'Lacie', u'Tillie', u'...']

Althoughstringis for finding strings, you can combine it with
arguments that find tags: Beautiful Soup will find all tags whose.stringmatches your value forstring. This code finds the <a>
tags whose.stringis âElsieâ:

Although
string
is for finding strings, you can combine it with
arguments that find tags: Beautiful Soup will find all tags whose
.string
matches your value for
string
. This code finds the <a>
tags whose
.string
is âElsieâ:

```python
soup.find_all("a", string="Elsie")
# [<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>]

```

soup
find_all
string
"Elsie"
# [<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>]

Thestringargument is new in Beautiful Soup 4.4.0. In earlier
versions it was calledtext:

string
argument is new in Beautiful Soup 4.4.0. In earlier
versions it was called
text

```python
soup.find_all("a", text="Elsie")
# [<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>]

```

soup
find_all
text
"Elsie"
# [<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>]

#### ThelimitargumentÂ¶

limit
argument

find_all()returns all the tags and strings that match your
filters. This can take a while if the document is large. If you donât
needallthe results, you can pass in a number forlimit. This
works just like the LIMIT keyword in SQL. It tells Beautiful Soup to
stop gathering results after itâs found a certain number.

find_all()
returns all the tags and strings that match your
filters. This can take a while if the document is large. If you donât
need
the results, you can pass in a number for
limit
. This
works just like the LIMIT keyword in SQL. It tells Beautiful Soup to
stop gathering results after itâs found a certain number.

There are three links in the âthree sistersâ document, but this code
only finds the first two:

There are three links in the âthree sistersâ document, but this code
only finds the first two:

```python
soup.find_all("a", limit=2)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

```

soup
find_all
limit
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

#### TherecursiveargumentÂ¶

recursive
argument

If you callmytag.find_all(), Beautiful Soup will examine all the
descendants ofmytag: its children, its childrenâs children, and
so on. If you only want Beautiful Soup to consider direct children,
you can pass inrecursive=False. See the difference here:

If you call
mytag.find_all()
, Beautiful Soup will examine all the
descendants of
mytag
: its children, its childrenâs children, and
so on. If you only want Beautiful Soup to consider direct children,
you can pass in
recursive=False
. See the difference here:

```python
soup.html.find_all("title")
# [<title>The Dormouse's story</title>]

soup.html.find_all("title", recursive=False)
# []

```

soup
html
find_all
"title"
# [<title>The Dormouse's story</title>]
soup
html
find_all
"title"
recursive
False
# []

Hereâs that part of the document:

Hereâs that part of the document:

```python
<html>
 <head>
 <title>
 The Dormouse's story
 </title>
 </head>
...

```

html
head
title
Dormouse
's story
title
head

The <title> tag is beneath the <html> tag, but itâs notdirectlybeneath the <html> tag: the <head> tag is in the way. Beautiful Soup
finds the <title> tag when itâs allowed to look at all descendants of
the <html> tag, but whenrecursive=Falserestricts it to the
<html> tagâs immediate children, it finds nothing.

The <title> tag is beneath the <html> tag, but itâs not
directly
beneath the <html> tag: the <head> tag is in the way. Beautiful Soup
finds the <title> tag when itâs allowed to look at all descendants of
the <html> tag, but when
recursive=False
restricts it to the
<html> tagâs immediate children, it finds nothing.

Beautiful Soup offers a lot of tree-searching methods (covered below),
and they mostly take the same arguments asfind_all():name,attrs,string,limit, and the keyword arguments. But therecursiveargument is different:find_all()andfind()are
the only methods that support it. Passingrecursive=Falseinto a
method likefind_parents()wouldnât be very useful.

Beautiful Soup offers a lot of tree-searching methods (covered below),
and they mostly take the same arguments as
find_all()
name
attrs
string
limit
, and the keyword arguments. But the
recursive
argument is different:
find_all()
find()
are
the only methods that support it. Passing
recursive=False
into a
method like
find_parents()
wouldnât be very useful.

### Calling a tag is like callingfind_all()Â¶

Calling a tag is like calling
find_all()

Becausefind_all()is the most popular method in the Beautiful
Soup search API, you can use a shortcut for it. If you treat theBeautifulSoupobject or aTagobject as though it were a
function, then itâs the same as callingfind_all()on that
object. These two lines of code are equivalent:

Because
find_all()
is the most popular method in the Beautiful
Soup search API, you can use a shortcut for it. If you treat the
BeautifulSoup
object or a
object as though it were a
function, then itâs the same as calling
find_all()
on that
object. These two lines of code are equivalent:

```python
soup.find_all("a")
soup("a")

```

soup
find_all
soup

These two lines are also equivalent:

These two lines are also equivalent:

```python
soup.title.find_all(string=True)
soup.title(string=True)

```

soup
title
find_all
string
True
soup
title
string
True

### find()Â¶

find()

Signature: find(name,attrs,recursive,string,**kwargs)

Signature: find(
name
attrs
recursive
string
**kwargs

Thefind_all()method scans the entire document looking for
results, but sometimes you only want to find one result. If you know a
document only has one <body> tag, itâs a waste of time to scan the
entire document looking for more. Rather than passing inlimit=1every time you callfind_all, you can use thefind()method. These two lines of code arenearlyequivalent:

find_all()
method scans the entire document looking for
results, but sometimes you only want to find one result. If you know a
document only has one <body> tag, itâs a waste of time to scan the
entire document looking for more. Rather than passing in
limit=1
every time you call
find_all
, you can use the
find()
method. These two lines of code are
nearly
equivalent:

```python
soup.find_all('title', limit=1)
# [<title>The Dormouse's story</title>]

soup.find('title')
# <title>The Dormouse's story</title>

```

soup
find_all
'title'
limit
# [<title>The Dormouse's story</title>]
soup
find
'title'
# <title>The Dormouse's story</title>

The only difference is thatfind_all()returns a list containing
the single result, andfind()just returns the result.

The only difference is that
find_all()
returns a list containing
the single result, and
find()
just returns the result.

Iffind_all()canât find anything, it returns an empty list. Iffind()canât find anything, it returnsNone:

find_all()
canât find anything, it returns an empty list. If
find()
canât find anything, it returns
None

```python
print(soup.find("nosuchtag"))
# None

```

print
soup
find
"nosuchtag"
# None

Remember thesoup.head.titletrick fromNavigating using tag
names? That trick works by repeatedly callingfind():

Remember the
soup.head.title
trick from
Navigating using tag
names
? That trick works by repeatedly calling
find()

```python
soup.head.title
# <title>The Dormouse's story</title>

soup.find("head").find("title")
# <title>The Dormouse's story</title>

```

soup
head
title
# <title>The Dormouse's story</title>
soup
find
"head"
find
"title"
# <title>The Dormouse's story</title>

### find_parents()andfind_parent()Â¶

find_parents()
find_parent()

Signature: find_parents(name,attrs,string,limit,**kwargs)

Signature: find_parents(
name
attrs
string
limit
**kwargs

Signature: find_parent(name,attrs,string,**kwargs)

Signature: find_parent(
name
attrs
string
**kwargs

I spent a lot of time above coveringfind_all()andfind(). The Beautiful Soup API defines ten other methods for
searching the tree, but donât be afraid. Five of these methods are
basically the same asfind_all(), and the other five are basically
the same asfind(). The only differences are in what parts of the
tree they search.

I spent a lot of time above covering
find_all()
find()
. The Beautiful Soup API defines ten other methods for
searching the tree, but donât be afraid. Five of these methods are
basically the same as
find_all()
, and the other five are basically
the same as
find()
. The only differences are in what parts of the
tree they search.

First letâs considerfind_parents()andfind_parent(). Remember thatfind_all()andfind()work
their way down the tree, looking at tagâs descendants. These methods
do the opposite: they work their wayupthe tree, looking at a tagâs
(or a stringâs) parents. Letâs try them out, starting from a string
buried deep in the âthree daughtersâ document:

First letâs consider
find_parents()
find_parent()
. Remember that
find_all()
find()
work
their way down the tree, looking at tagâs descendants. These methods
do the opposite: they work their way
the tree, looking at a tagâs
(or a stringâs) parents. Letâs try them out, starting from a string
buried deep in the âthree daughtersâ document:

```python
a_string = soup.find(string="Lacie")
a_string
# u'Lacie'

a_string.find_parents("a")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

a_string.find_parent("p")
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

a_string.find_parents("p", class="title")
# []

```

a_string
soup
find
string
"Lacie"
a_string
# u'Lacie'
a_string
find_parents
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
a_string
find_parent
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
a_string
find_parents
class
"title"
# []

One of the three <a> tags is the direct parent of the string in
question, so our search finds it. One of the three <p> tags is an
indirect parent of the string, and our search finds that as
well. Thereâs a <p> tag with the CSS class âtitleâsomewherein the
document, but itâs not one of this stringâs parents, so we canât find
it withfind_parents().

One of the three <a> tags is the direct parent of the string in
question, so our search finds it. One of the three <p> tags is an
indirect parent of the string, and our search finds that as
well. Thereâs a <p> tag with the CSS class âtitleâ
somewhere
in the
document, but itâs not one of this stringâs parents, so we canât find
it with
find_parents()

You may have made the connection betweenfind_parent()andfind_parents(), and the.parentand.parentsattributes
mentioned earlier. The connection is very strong. These search methods
actually use.parentsto iterate over all the parents, and check
each one against the provided filter to see if it matches.

You may have made the connection between
find_parent()
find_parents()
, and the
.parent
.parents
attributes
mentioned earlier. The connection is very strong. These search methods
actually use
.parents
to iterate over all the parents, and check
each one against the provided filter to see if it matches.

### find_next_siblings()andfind_next_sibling()Â¶

Signature: find_next_siblings(name,attrs,string,limit,**kwargs)

name
attrs
string
limit
**kwargs

Signature: find_next_sibling(name,attrs,string,**kwargs)

name
attrs
string
**kwargs

These methods use.next_siblingsto
iterate over the rest of an elementâs siblings in the tree. Thefind_next_siblings()method returns all the siblings that match,
andfind_next_sibling()only returns the first one:

These methods use
to
iterate over the rest of an elementâs siblings in the tree. The
method returns all the siblings that match,
and
only returns the first one:

```python
first_link = soup.a
first_link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

first_link.find_next_siblings("a")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

first_story_paragraph = soup.find("p", "story")
first_story_paragraph.find_next_sibling("p")
# <p class="story">...</p>

```

first_link
soup
first_link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
first_link
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
first_story_paragraph
soup
find
"story"
first_story_paragraph
# <p class="story">...</p>

### find_previous_siblings()andfind_previous_sibling()Â¶

Signature: find_previous_siblings(name,attrs,string,limit,**kwargs)

name
attrs
string
limit
**kwargs

Signature: find_previous_sibling(name,attrs,string,**kwargs)

name
attrs
string
**kwargs

These methods use.previous_siblingsto iterate over an elementâs
siblings that precede it in the tree. Thefind_previous_siblings()method returns all the siblings that match, andfind_previous_sibling()only returns the first one:

These methods use
to iterate over an elementâs
siblings that precede it in the tree. The
method returns all the siblings that match, and
only returns the first one:

```python
last_link = soup.find("a", id="link3")
last_link
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

last_link.find_previous_siblings("a")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

first_story_paragraph = soup.find("p", "story")
first_story_paragraph.find_previous_sibling("p")
# <p class="title"><b>The Dormouse's story</b></p>

```

last_link
soup
find
"link3"
last_link
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
last_link
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
first_story_paragraph
soup
find
"story"
first_story_paragraph
# <p class="title"><b>The Dormouse's story</b></p>

### find_all_next()andfind_next()Â¶

Signature: find_all_next(name,attrs,string,limit,**kwargs)

name
attrs
string
limit
**kwargs

Signature: find_next(name,attrs,string,**kwargs)

name
attrs
string
**kwargs

These methods use.next_elementsto
iterate over whatever tags and strings that come after it in the
document. Thefind_all_next()method returns all matches, andfind_next()only returns the first match:

These methods use
to
iterate over whatever tags and strings that come after it in the
document. The
method returns all matches, and
only returns the first match:

```python
first_link = soup.a
first_link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

first_link.find_all_next(string=True)
# [u'Elsie', u',\n', u'Lacie', u' and\n', u'Tillie',
# u';\nand they lived at the bottom of a well.', u'\n\n', u'...', u'\n']

first_link.find_next("p")
# <p class="story">...</p>

```

first_link
soup
first_link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
first_link
string
True
# [u'Elsie', u',\n', u'Lacie', u' and\n', u'Tillie',
# u';\nand they lived at the bottom of a well.', u'\n\n', u'...', u'\n']
first_link
# <p class="story">...</p>

In the first example, the string âElsieâ showed up, even though it was
contained within the <a> tag we started from. In the second example,
the last <p> tag in the document showed up, even though itâs not in
the same part of the tree as the <a> tag we started from. For these
methods, all that matters is that an element match the filter, and
show up later in the document than the starting element.

In the first example, the string âElsieâ showed up, even though it was
contained within the <a> tag we started from. In the second example,
the last <p> tag in the document showed up, even though itâs not in
the same part of the tree as the <a> tag we started from. For these
methods, all that matters is that an element match the filter, and
show up later in the document than the starting element.

### find_all_previous()andfind_previous()Â¶

Signature: find_all_previous(name,attrs,string,limit,**kwargs)

name
attrs
string
limit
**kwargs

Signature: find_previous(name,attrs,string,**kwargs)

name
attrs
string
**kwargs

These methods use.previous_elementsto
iterate over the tags and strings that came before it in the
document. Thefind_all_previous()method returns all matches, andfind_previous()only returns the first match:

These methods use
to
iterate over the tags and strings that came before it in the
document. The
method returns all matches, and
only returns the first match:

```python
first_link = soup.a
first_link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

first_link.find_all_previous("p")
# [<p class="story">Once upon a time there were three little sisters; ...</p>,
# <p class="title"><b>The Dormouse's story</b></p>]

first_link.find_previous("title")
# <title>The Dormouse's story</title>

```

first_link
soup
first_link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
first_link
# [<p class="story">Once upon a time there were three little sisters; ...</p>,
# <p class="title"><b>The Dormouse's story</b></p>]
first_link
"title"
# <title>The Dormouse's story</title>

The call tofind_all_previous("p")found the first paragraph in
the document (the one with class=âtitleâ), but it also finds the
second paragraph, the <p> tag that contains the <a> tag we started
with. This shouldnât be too surprising: weâre looking at all the tags
that show up earlier in the document than the one we started with. A
<p> tag that contains an <a> tag must have shown up before the <a>
tag it contains.

The call to
found the first paragraph in
the document (the one with class=âtitleâ), but it also finds the
second paragraph, the <p> tag that contains the <a> tag we started
with. This shouldnât be too surprising: weâre looking at all the tags
that show up earlier in the document than the one we started with. A
<p> tag that contains an <a> tag must have shown up before the <a>
tag it contains.

### CSS selectorsÂ¶

CSS selectors

As of version 4.7.0, Beautiful Soup supports most CSS4 selectors via
theSoupSieveproject. If you installed Beautiful Soup throughpip, SoupSieve
was installed at the same time, so you donât have to do anything extra.

As of version 4.7.0, Beautiful Soup supports most CSS4 selectors via
the
SoupSieve
project. If you installed Beautiful Soup through
, SoupSieve
was installed at the same time, so you donât have to do anything extra.

BeautifulSouphas a.select()method which uses SoupSieve to
run a CSS selector against a parsed document and return all the
matching elements.Taghas a similar method which runs a CSS
selector against the contents of a single tag.

BeautifulSoup
has a
.select()
method which uses SoupSieve to
run a CSS selector against a parsed document and return all the
matching elements.
has a similar method which runs a CSS
selector against the contents of a single tag.

(Earlier versions of Beautiful Soup also have the.select()method, but only the most commonly-used CSS selectors are supported.)

(Earlier versions of Beautiful Soup also have the
.select()
method, but only the most commonly-used CSS selectors are supported.)

The SoupSievedocumentationlists all the currently
supported CSS selectors, but here are some of the basics:

The SoupSieve
documentation
lists all the currently
supported CSS selectors, but here are some of the basics:

You can find tags:

You can find tags:

```python
soup.select("title")
# [<title>The Dormouse's story</title>]

soup.select("p:nth-of-type(3)")
# [<p class="story">...</p>]

```

soup
select
"title"
# [<title>The Dormouse's story</title>]
soup
select
"p:nth-of-type(3)"
# [<p class="story">...</p>]

Find tags beneath other tags:

Find tags beneath other tags:

```python
soup.select("body a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select("html head title")
# [<title>The Dormouse's story</title>]

```

soup
select
"body a"
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup
select
"html head title"
# [<title>The Dormouse's story</title>]

Find tagsdirectlybeneath other tags:

Find tags
directly
beneath other tags:

```python
soup.select("head > title")
# [<title>The Dormouse's story</title>]

soup.select("p > a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select("p > a:nth-of-type(2)")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

soup.select("p > #link1")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.select("body > a")
# []

```

soup
select
"head > title"
# [<title>The Dormouse's story</title>]
soup
select
"p > a"
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup
select
"p > a:nth-of-type(2)"
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
soup
select
"p > #link1"
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
soup
select
"body > a"
# []

Find the siblings of tags:

Find the siblings of tags:

```python
soup.select("#link1 ~ .sister")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select("#link1 + .sister")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

```

soup
select
"#link1 ~ .sister"
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup
select
"#link1 + .sister"
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

Find tags by CSS class:

Find tags by CSS class:

```python
soup.select(".sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select("[class~=sister]")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

```

soup
select
".sister"
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup
select
"[class~=sister]"
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

Find tags by ID:

Find tags by ID:

```python
soup.select("#link1")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.select("a#link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

```

soup
select
"#link1"
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
soup
select
"a#link2"
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

Find tags that match any selector from a list of selectors:

Find tags that match any selector from a list of selectors:

```python
soup.select("#link1,#link2")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

```

soup
select
"#link1,#link2"
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

Test for the existence of an attribute:

Test for the existence of an attribute:

```python
soup.select('a[href]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

```

soup
select
'a[href]'
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

Find tags by attribute value:

Find tags by attribute value:

```python
soup.select('a[href="http://example.com/elsie"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.select('a[href^="http://example.com/"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select('a[href$="tillie"]')
# [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select('a[href*=".com/el"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

```

soup
select
'a[href="http://example.com/elsie"]'
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
soup
select
'a[href^="http://example.com/"]'
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup
select
'a[href$="tillie"]'
# [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup
select
'a[href*=".com/el"]'
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

Thereâs also a method calledselect_one(), which finds only the
first tag that matches a selector:

Thereâs also a method called
select_one()
, which finds only the
first tag that matches a selector:

```python
soup.select_one(".sister")
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

```

soup
select_one
".sister"
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

If youâve parsed XML that defines namespaces, you can use them in CSS
selectors.:

If youâve parsed XML that defines namespaces, you can use them in CSS
selectors.:

```python
from bs4 import BeautifulSoup
xml = """<tag xmlns:ns1="http://namespace1/" xmlns:ns2="http://namespace2/">
 <ns1:child>I'm in namespace 1</ns1:child>
 <ns2:child>I'm in namespace 2</ns2:child>
</tag> """
soup = BeautifulSoup(xml, "xml")

soup.select("child")
# [<ns1:child>I'm in namespace 1</ns1:child>, <ns2:child>I'm in namespace 2</ns2:child>]

soup.select("ns1|child", namespaces=namespaces)
# [<ns1:child>I'm in namespace 1</ns1:child>]

```

from
import
BeautifulSoup
"""<tag xmlns:ns1="http://namespace1/" xmlns:ns2="http://namespace2/">
<ns1:child>I'm in namespace 1</ns1:child>
<ns2:child>I'm in namespace 2</ns2:child>
</tag> """
soup
BeautifulSoup
"xml"
soup
select
"child"
# [<ns1:child>I'm in namespace 1</ns1:child>, <ns2:child>I'm in namespace 2</ns2:child>]
soup
select
"ns1|child"
namespaces
namespaces
# [<ns1:child>I'm in namespace 1</ns1:child>]

When handling a CSS selector that uses namespaces, Beautiful Soup
uses the namespace abbreviations it found when parsing the
document. You can override this by passing in your own dictionary of
abbreviations:

When handling a CSS selector that uses namespaces, Beautiful Soup
uses the namespace abbreviations it found when parsing the
document. You can override this by passing in your own dictionary of
abbreviations:

```python
namespaces = dict(first="http://namespace1/", second="http://namespace2/")
soup.select("second|child", namespaces=namespaces)
# [<ns1:child>I'm in namespace 2</ns1:child>]

```

namespaces
dict
first
"http://namespace1/"
second
"http://namespace2/"
soup
select
"second|child"
namespaces
namespaces
# [<ns1:child>I'm in namespace 2</ns1:child>]

All this CSS selector stuff is a convenience for people who already
know the CSS selector syntax. You can do all of this with the
Beautiful Soup API. And if CSS selectors are all you need, you should
parse the document with lxml: itâs a lot faster. But this lets youcombineCSS selectors with the Beautiful Soup API.

All this CSS selector stuff is a convenience for people who already
know the CSS selector syntax. You can do all of this with the
Beautiful Soup API. And if CSS selectors are all you need, you should
parse the document with lxml: itâs a lot faster. But this lets you
combine
CSS selectors with the Beautiful Soup API.

## Modifying the treeÂ¶

Modifying the tree

Beautiful Soupâs main strength is in searching the parse tree, but you
can also modify the tree and write your changes as a new HTML or XML
document.

Beautiful Soupâs main strength is in searching the parse tree, but you
can also modify the tree and write your changes as a new HTML or XML
document.

### Changing tag names and attributesÂ¶

Changing tag names and attributes

I covered this earlier, inAttributes, but it bears repeating. You
can rename a tag, change the values of its attributes, add new
attributes, and delete attributes:

I covered this earlier, in
Attributes
, but it bears repeating. You
can rename a tag, change the values of its attributes, add new
attributes, and delete attributes:

```python
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b

tag.name = "blockquote"
tag['class'] = 'verybold'
tag['id'] = 1
tag
# <blockquote class="verybold" id="1">Extremely bold</blockquote>

del tag['class']
del tag['id']
tag
# <blockquote>Extremely bold</blockquote>

```

soup
BeautifulSoup
'<b class="boldest">Extremely bold</b>'
soup
name
"blockquote"
'class'
'verybold'
'id'
# <blockquote class="verybold" id="1">Extremely bold</blockquote>
'class'
'id'
# <blockquote>Extremely bold</blockquote>

### Modifying.stringÂ¶

Modifying
.string

If you set a tagâs.stringattribute to a new string, the tagâs contents are
replaced with that string:

If you set a tagâs
.string
attribute to a new string, the tagâs contents are
replaced with that string:

```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)

tag = soup.a
tag.string = "New link text."
tag
# <a href="http://example.com/">New link text.</a>

```

markup
'<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup
BeautifulSoup
markup
soup
string
"New link text."
# <a href="http://example.com/">New link text.</a>

Be careful: if the tag contained other tags, they and all their
contents will be destroyed.

Be careful: if the tag contained other tags, they and all their
contents will be destroyed.

### append()Â¶

append()

You can add to a tagâs contents withTag.append(). It works just
like calling.append()on a Python list:

You can add to a tagâs contents with
Tag.append()
. It works just
like calling
.append()
on a Python list:

```python
soup = BeautifulSoup("<a>Foo</a>")
soup.a.append("Bar")

soup
# <html><head></head><body><a>FooBar</a></body></html>
soup.a.contents
# [u'Foo', u'Bar']

```

soup
BeautifulSoup
"<a>Foo</a>"
soup
append
"Bar"
soup
# <html><head></head><body><a>FooBar</a></body></html>
soup
contents
# [u'Foo', u'Bar']

### extend()Â¶

extend()

Starting in Beautiful Soup 4.7.0,Tagalso supports a method
called.extend(), which works just like calling.extend()on a
Python list:

Starting in Beautiful Soup 4.7.0,
also supports a method
called
.extend()
, which works just like calling
.extend()
on a
Python list:

```python
soup = BeautifulSoup("<a>Soup</a>")
soup.a.extend(["'s", " ", "on"])

soup
# <html><head></head><body><a>Soup's on</a></body></html>
soup.a.contents
# [u'Soup', u''s', u' ', u'on']

```

soup
BeautifulSoup
"<a>Soup</a>"
soup
extend
"'s"
"on"
soup
# <html><head></head><body><a>Soup's on</a></body></html>
soup
contents
# [u'Soup', u''s', u' ', u'on']

### NavigableString()and.new_tag()Â¶

NavigableString()
.new_tag()

If you need to add a string to a document, no problemâyou can pass a
Python string in toappend(), or you can call theNavigableStringconstructor:

If you need to add a string to a document, no problemâyou can pass a
Python string in to
append()
, or you can call the
NavigableString
constructor:

```python
soup = BeautifulSoup("<b></b>")
tag = soup.b
tag.append("Hello")
new_string = NavigableString(" there")
tag.append(new_string)
tag
# <b>Hello there.</b>
tag.contents
# [u'Hello', u' there']

```

soup
BeautifulSoup
"<b></b>"
soup
append
"Hello"
new_string
NavigableString
" there"
append
new_string
# <b>Hello there.</b>
contents
# [u'Hello', u' there']

If you want to create a comment or some other subclass ofNavigableString, just call the constructor:

If you want to create a comment or some other subclass of
NavigableString
, just call the constructor:

```python
from bs4 import Comment
new_comment = Comment("Nice to see you.")
tag.append(new_comment)
tag
# <b>Hello there<!--Nice to see you.--></b>
tag.contents
# [u'Hello', u' there', u'Nice to see you.']

```

from
import
Comment
new_comment
Comment
"Nice to see you."
append
new_comment
# <b>Hello there<!--Nice to see you.--></b>
contents
# [u'Hello', u' there', u'Nice to see you.']

(This is a new feature in Beautiful Soup 4.4.0.)

(This is a new feature in Beautiful Soup 4.4.0.)

What if you need to create a whole new tag? The best solution is to
call the factory methodBeautifulSoup.new_tag():

What if you need to create a whole new tag? The best solution is to
call the factory method
BeautifulSoup.new_tag()

```python
soup = BeautifulSoup("<b></b>")
original_tag = soup.b

new_tag = soup.new_tag("a", href="http://www.example.com")
original_tag.append(new_tag)
original_tag
# <b><a href="http://www.example.com"></a></b>

new_tag.string = "Link text."
original_tag
# <b><a href="http://www.example.com">Link text.</a></b>

```

soup
BeautifulSoup
"<b></b>"
original_tag
soup
new_tag
soup
new_tag
href
"http://www.example.com"
original_tag
append
new_tag
original_tag
# <b><a href="http://www.example.com"></a></b>
new_tag
string
"Link text."
original_tag
# <b><a href="http://www.example.com">Link text.</a></b>

Only the first argument, the tag name, is required.

Only the first argument, the tag name, is required.

### insert()Â¶

insert()

Tag.insert()is just likeTag.append(), except the new element
doesnât necessarily go at the end of its parentâs.contents. Itâll be inserted at whatever numeric position you
say. It works just like.insert()on a Python list:

Tag.insert()
is just like
Tag.append()
, except the new element
doesnât necessarily go at the end of its parentâs
.contents
. Itâll be inserted at whatever numeric position you
say. It works just like
.insert()
on a Python list:

```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
tag = soup.a

tag.insert(1, "but did not endorse ")
tag
# <a href="http://example.com/">I linked to but did not endorse <i>example.com</i></a>
tag.contents
# [u'I linked to ', u'but did not endorse', <i>example.com</i>]

```

markup
'<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup
BeautifulSoup
markup
soup
insert
"but did not endorse "
# <a href="http://example.com/">I linked to but did not endorse <i>example.com</i></a>
contents
# [u'I linked to ', u'but did not endorse', <i>example.com</i>]

### insert_before()andinsert_after()Â¶

insert_before()
insert_after()

Theinsert_before()method inserts tags or strings immediately
before something else in the parse tree:

insert_before()
method inserts tags or strings immediately
before something else in the parse tree:

```python
soup = BeautifulSoup("<b>stop</b>")
tag = soup.new_tag("i")
tag.string = "Don't"
soup.b.string.insert_before(tag)
soup.b
# <b><i>Don't</i>stop</b>

```

soup
BeautifulSoup
"<b>stop</b>"
soup
new_tag
string
"Don't"
soup
string
insert_before
soup
# <b><i>Don't</i>stop</b>

Theinsert_after()method inserts tags or strings immediately
following something else in the parse tree:

insert_after()
method inserts tags or strings immediately
following something else in the parse tree:

```python
div = soup.new_tag('div')
div.string = 'ever'
soup.b.i.insert_after(" you ", div)
soup.b
# <b><i>Don't</i> you <div>ever</div> stop</b>
soup.b.contents
# [<i>Don't</i>, u' you', <div>ever</div>, u'stop']

```

soup
new_tag
'div'
string
'ever'
soup
insert_after
" you "
soup
# <b><i>Don't</i> you <div>ever</div> stop</b>
soup
contents
# [<i>Don't</i>, u' you', <div>ever</div>, u'stop']

### clear()Â¶

clear()

Tag.clear()removes the contents of a tag:

Tag.clear()
removes the contents of a tag:

```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
tag = soup.a

tag.clear()
tag
# <a href="http://example.com/"></a>

```

markup
'<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup
BeautifulSoup
markup
soup
clear
# <a href="http://example.com/"></a>

### extract()Â¶

extract()

PageElement.extract()removes a tag or string from the tree. It
returns the tag or string that was extracted:

PageElement.extract()
removes a tag or string from the tree. It
returns the tag or string that was extracted:

```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.a

i_tag = soup.i.extract()

a_tag
# <a href="http://example.com/">I linked to</a>

i_tag
# <i>example.com</i>

print(i_tag.parent)
None

```

markup
'<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup
BeautifulSoup
markup
a_tag
soup
i_tag
soup
extract
a_tag
# <a href="http://example.com/">I linked to</a>
i_tag
# <i>example.com</i>
print
i_tag
parent
None

At this point you effectively have two parse trees: one rooted at theBeautifulSoupobject you used to parse the document, and one rooted
at the tag that was extracted. You can go on to callextracton
a child of the element you extracted:

At this point you effectively have two parse trees: one rooted at the
BeautifulSoup
object you used to parse the document, and one rooted
at the tag that was extracted. You can go on to call
extract
on
a child of the element you extracted:

```python
my_string = i_tag.string.extract()
my_string
# u'example.com'

print(my_string.parent)
# None
i_tag
# <i></i>

```

my_string
i_tag
string
extract
my_string
# u'example.com'
print
my_string
parent
# None
i_tag
# <i></i>

### decompose()Â¶

decompose()

Tag.decompose()removes a tag from the tree, thencompletely
destroys it and its contents:

Tag.decompose()
removes a tag from the tree, then
completely
destroys it and its contents

```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.a

soup.i.decompose()

a_tag
# <a href="http://example.com/">I linked to</a>

```

markup
'<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup
BeautifulSoup
markup
a_tag
soup
soup
decompose
a_tag
# <a href="http://example.com/">I linked to</a>

### replace_with()Â¶

replace_with()

PageElement.replace_with()removes a tag or string from the tree,
and replaces it with the tag or string of your choice:

PageElement.replace_with()
removes a tag or string from the tree,
and replaces it with the tag or string of your choice:

```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.a

new_tag = soup.new_tag("b")
new_tag.string = "example.net"
a_tag.i.replace_with(new_tag)

a_tag
# <a href="http://example.com/">I linked to <b>example.net</b></a>

```

markup
'<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup
BeautifulSoup
markup
a_tag
soup
new_tag
soup
new_tag
new_tag
string
"example.net"
a_tag
replace_with
new_tag
a_tag
# <a href="http://example.com/">I linked to <b>example.net</b></a>

replace_with()returns the tag or string that was replaced, so
that you can examine it or add it back to another part of the tree.

replace_with()
returns the tag or string that was replaced, so
that you can examine it or add it back to another part of the tree.

### wrap()Â¶

wrap()

PageElement.wrap()wraps an element in the tag you specify. It
returns the new wrapper:

PageElement.wrap()
wraps an element in the tag you specify. It
returns the new wrapper:

```python
soup = BeautifulSoup("<p>I wish I was bold.</p>")
soup.p.string.wrap(soup.new_tag("b"))
# <b>I wish I was bold.</b>

soup.p.wrap(soup.new_tag("div")
# <div><p><b>I wish I was bold.</b></p></div>

```

soup
BeautifulSoup
"<p>I wish I was bold.</p>"
soup
string
wrap
soup
new_tag
# <b>I wish I was bold.</b>
soup
wrap
soup
new_tag
"div"
# <div><p><b>I wish I was bold.</b></p></div>

This method is new in Beautiful Soup 4.0.5.

This method is new in Beautiful Soup 4.0.5.

### unwrap()Â¶

unwrap()

Tag.unwrap()is the opposite ofwrap(). It replaces a tag with
whateverâs inside that tag. Itâs good for stripping out markup:

Tag.unwrap()
is the opposite of
wrap()
. It replaces a tag with
whateverâs inside that tag. Itâs good for stripping out markup:

```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.a

a_tag.i.unwrap()
a_tag
# <a href="http://example.com/">I linked to example.com</a>

```

markup
'<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup
BeautifulSoup
markup
a_tag
soup
a_tag
unwrap
a_tag
# <a href="http://example.com/">I linked to example.com</a>

Likereplace_with(),unwrap()returns the tag
that was replaced.

Like
replace_with()
unwrap()
returns the tag
that was replaced.

### smooth()Â¶

smooth()

After calling a bunch of methods that modify the parse tree, you may end up with two or moreNavigableStringobjects next to each other. Beautiful Soup doesnât have any problems with this, but since it canât happen in a freshly parsed document, you might not expect behavior like the following:

After calling a bunch of methods that modify the parse tree, you may end up with two or more
NavigableString

```python
soup = BeautifulSoup("<p>A one</p>")
soup.p.append(", a two")

soup.p.contents
# [u'A one', u', a two']

print(soup.p.encode())
# <p>A one, a two</p>

print(soup.p.prettify())
# <p>
# A one
# , a two
# </p>

```

soup
BeautifulSoup
"<p>A one</p>"
soup
append
", a two"
soup
contents
# [u'A one', u', a two']
print
soup
encode
# <p>A one, a two</p>
print
soup
prettify
# <p>
# A one
# , a two
# </p>

You can callTag.smooth()to clean up the parse tree by consolidating adjacent strings:

You can call
Tag.smooth()
to clean up the parse tree by consolidating adjacent strings:

```python
soup.smooth()

soup.p.contents
# [u'A one, a two']

print(soup.p.prettify())
# <p>
# A one, a two
# </p>

```

soup
smooth
soup
contents
# [u'A one, a two']
print
soup
prettify
# <p>
# A one, a two
# </p>

Thesmooth()method is new in Beautiful Soup 4.8.0.

smooth()
method is new in Beautiful Soup 4.8.0.

## OutputÂ¶

Output

### Pretty-printingÂ¶

Pretty-printing

Theprettify()method will turn a Beautiful Soup parse tree into a
nicely formatted Unicode string, with a separate line for each
tag and each string:

prettify()
method will turn a Beautiful Soup parse tree into a
nicely formatted Unicode string, with a separate line for each
tag and each string:

```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
soup.prettify()
# '<html>\n <head>\n </head>\n <body>\n <a href="http://example.com/">\n...'

print(soup.prettify())
# <html>
# <head>
# </head>
# <body>
# <a href="http://example.com/">
# I linked to
# <i>
# example.com
# </i>
# </a>
# </body>
# </html>

```

markup
'<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup
BeautifulSoup
markup
soup
prettify
# '<html>\n <head>\n </head>\n <body>\n <a href="http://example.com/">\n...'
print
soup
prettify
# <html>
# <head>
# </head>
# <body>
# <a href="http://example.com/">
# I linked to
# <i>
# example.com
# </i>
# </a>
# </body>
# </html>

You can callprettify()on the top-levelBeautifulSoupobject,
or on any of itsTagobjects:

You can call
prettify()
on the top-level
BeautifulSoup
object,
or on any of its
objects:

```python
print(soup.a.prettify())
# <a href="http://example.com/">
# I linked to
# <i>
# example.com
# </i>
# </a>

```

print
soup
prettify
# <a href="http://example.com/">
# I linked to
# <i>
# example.com
# </i>
# </a>

### Non-pretty printingÂ¶

Non-pretty printing

If you just want a string, with no fancy formatting, you can callunicode()orstr()on aBeautifulSoupobject, or aTagwithin it:

If you just want a string, with no fancy formatting, you can call
unicode()
str()
on a
BeautifulSoup
object, or a
within it:

```python
str(soup)
# '<html><head></head><body><a href="http://example.com/">I linked to <i>example.com</i></a></body></html>'

unicode(soup.a)
# u'<a href="http://example.com/">I linked to <i>example.com</i></a>'

```

soup
# '<html><head></head><body><a href="http://example.com/">I linked to <i>example.com</i></a></body></html>'
unicode
soup
# u'<a href="http://example.com/">I linked to <i>example.com</i></a>'

Thestr()function returns a string encoded in UTF-8. SeeEncodingsfor other options.

str()
function returns a string encoded in UTF-8. See
Encodings
for other options.

You can also callencode()to get a bytestring, anddecode()to get Unicode.

You can also call
encode()
to get a bytestring, and
decode()
to get Unicode.

### Output formattersÂ¶

Output formatters

If you give Beautiful Soup a document that contains HTML entities like
â&lquot;â, theyâll be converted to Unicode characters:

If you give Beautiful Soup a document that contains HTML entities like
â&lquot;â, theyâll be converted to Unicode characters:

```python
soup = BeautifulSoup("&ldquo;Dammit!&rdquo; he said.")
unicode(soup)
# u'<html><head></head><body>\u201cDammit!\u201d he said.</body></html>'

```

soup
BeautifulSoup
"&ldquo;Dammit!&rdquo; he said."
unicode
soup
# u'<html><head></head><body>\u201cDammit!\u201d he said.</body></html>'

If you then convert the document to a string, the Unicode characters
will be encoded as UTF-8. You wonât get the HTML entities back:

If you then convert the document to a string, the Unicode characters
will be encoded as UTF-8. You wonât get the HTML entities back:

```python
str(soup)
# '<html><head></head><body>\xe2\x80\x9cDammit!\xe2\x80\x9d he said.</body></html>'

```

soup
# '<html><head></head><body>\xe2\x80\x9cDammit!\xe2\x80\x9d he said.</body></html>'

By default, the only characters that are escaped upon output are bare
ampersands and angle brackets. These get turned into â&amp;â, â&lt;â,
and â&gt;â, so that Beautiful Soup doesnât inadvertently generate
invalid HTML or XML:

By default, the only characters that are escaped upon output are bare
ampersands and angle brackets. These get turned into â&amp;â, â&lt;â,
and â&gt;â, so that Beautiful Soup doesnât inadvertently generate
invalid HTML or XML:

```python
soup = BeautifulSoup("<p>The law firm of Dewey, Cheatem, & Howe</p>")
soup.p
# <p>The law firm of Dewey, Cheatem, &amp; Howe</p>

soup = BeautifulSoup('<a href="http://example.com/?foo=val1&bar=val2">A link</a>')
soup.a
# <a href="http://example.com/?foo=val1&amp;bar=val2">A link</a>

```

soup
BeautifulSoup
"<p>The law firm of Dewey, Cheatem, & Howe</p>"
soup
# <p>The law firm of Dewey, Cheatem, &amp; Howe</p>
soup
BeautifulSoup
'<a href="http://example.com/?foo=val1&bar=val2">A link</a>'
soup
# <a href="http://example.com/?foo=val1&amp;bar=val2">A link</a>

You can change this behavior by providing a value for theformatterargument toprettify(),encode(), ordecode(). Beautiful Soup recognizes five possible values forformatter.

You can change this behavior by providing a value for the
formatter
argument to
prettify()
encode()
, or
decode()
. Beautiful Soup recognizes five possible values for
formatter

The default isformatter="minimal". Strings will only be processed
enough to ensure that Beautiful Soup generates valid HTML/XML:

The default is
formatter="minimal"
. Strings will only be processed
enough to ensure that Beautiful Soup generates valid HTML/XML:

```python
french = "<p>Il a dit &lt;&lt;Sacr&eacute; bleu!&gt;&gt;</p>"
soup = BeautifulSoup(french)
print(soup.prettify(formatter="minimal"))
# <html>
# <body>
# <p>
# Il a dit &lt;&lt;SacrÃ© bleu!&gt;&gt;
# </p>
# </body>
# </html>

```

french
"<p>Il a dit &lt;&lt;Sacr&eacute; bleu!&gt;&gt;</p>"
soup
BeautifulSoup
french
print
soup
prettify
formatter
"minimal"
# <html>
# <body>
# <p>
# Il a dit &lt;&lt;SacrÃ© bleu!&gt;&gt;
# </p>
# </body>
# </html>

If you pass informatter="html", Beautiful Soup will convert
Unicode characters to HTML entities whenever possible:

If you pass in
formatter="html"
, Beautiful Soup will convert
Unicode characters to HTML entities whenever possible:

```python
print(soup.prettify(formatter="html"))
# <html>
# <body>
# <p>
# Il a dit &lt;&lt;Sacr&eacute; bleu!&gt;&gt;
# </p>
# </body>
# </html>

```

print
soup
prettify
formatter
"html"
# <html>
# <body>
# <p>
# Il a dit &lt;&lt;Sacr&eacute; bleu!&gt;&gt;
# </p>
# </body>
# </html>

If you pass informatter="html5", itâs the same asformatter="html5", but Beautiful Soup will
omit the closing slash in HTML void tags like âbrâ:

If you pass in
formatter="html5"
, itâs the same as
formatter="html5"
, but Beautiful Soup will
omit the closing slash in HTML void tags like âbrâ:

```python
soup = BeautifulSoup("<br>")

print(soup.encode(formatter="html"))
# <html><body><br/></body></html>

print(soup.encode(formatter="html5"))
# <html><body><br></body></html>

```

soup
BeautifulSoup
"<br>"
print
soup
encode
formatter
"html"
# <html><body><br/></body></html>
print
soup
encode
formatter
"html5"
# <html><body><br></body></html>

If you pass informatter=None, Beautiful Soup will not modify
strings at all on output. This is the fastest option, but it may lead
to Beautiful Soup generating invalid HTML/XML, as in these examples:

If you pass in
formatter=None
, Beautiful Soup will not modify
strings at all on output. This is the fastest option, but it may lead
to Beautiful Soup generating invalid HTML/XML, as in these examples:

```python
print(soup.prettify(formatter=None))
# <html>
# <body>
# <p>
# Il a dit <<SacrÃ© bleu!>>
# </p>
# </body>
# </html>

link_soup = BeautifulSoup('<a href="http://example.com/?foo=val1&bar=val2">A link</a>')
print(link_soup.a.encode(formatter=None))
# <a href="http://example.com/?foo=val1&bar=val2">A link</a>

```

print
soup
prettify
formatter
None
# <html>
# <body>
# <p>
# Il a dit <<SacrÃ© bleu!>>
# </p>
# </body>
# </html>
link_soup
BeautifulSoup
'<a href="http://example.com/?foo=val1&bar=val2">A link</a>'
print
link_soup
encode
formatter
None
# <a href="http://example.com/?foo=val1&bar=val2">A link</a>

If you need more sophisticated control over your output, you can
use Beautiful SoupâsFormatterclass. Hereâs a formatter that
converts strings to uppercase, whether they occur in a text node or in an
attribute value:

If you need more sophisticated control over your output, you can
use Beautiful Soupâs
Formatter
class. Hereâs a formatter that
converts strings to uppercase, whether they occur in a text node or in an
attribute value:

```python
from bs4.formatter import HTMLFormatter
def uppercase(str):
 return str.upper()
formatter = HTMLFormatter(uppercase)

print(soup.prettify(formatter=formatter))
# <html>
# <body>
# <p>
# IL A DIT <<SACRÃ BLEU!>>
# </p>
# </body>
# </html>

print(link_soup.a.prettify(formatter=formatter))
# <a href="HTTP://EXAMPLE.COM/?FOO=VAL1&BAR=VAL2">
# A LINK
# </a>

```

from
bs4.formatter
import
HTMLFormatter
uppercase
return
upper
formatter
HTMLFormatter
uppercase
print
soup
prettify
formatter
formatter
# <html>
# <body>
# <p>
# IL A DIT <<SACRÃ BLEU!>>
# </p>
# </body>
# </html>
print
link_soup
prettify
formatter
formatter
# <a href="HTTP://EXAMPLE.COM/?FOO=VAL1&BAR=VAL2">
# A LINK
# </a>

SubclassingHTMLFormatterorXMLFormatterwill give you even
more control over the output. For example, Beautiful Soup sorts the
attributes in every tag by default:

Subclassing
HTMLFormatter
XMLFormatter
will give you even
more control over the output. For example, Beautiful Soup sorts the
attributes in every tag by default:

```python
attr_soup = BeautifulSoup(b'<p z="1" m="2" a="3"></p>')
print(attr_soup.p.encode())
# <p a="3" m="2" z="1"></p>

```

attr_soup
BeautifulSoup
'<p z="1" m="2" a="3"></p>'
print
attr_soup
encode
# <p a="3" m="2" z="1"></p>

To turn this off, you can subclass theFormatter.attributes()method, which controls which attributes are output and in what
order. This implementation also filters out the attribute called âmâ
whenever it appears:

To turn this off, you can subclass the
Formatter.attributes()
method, which controls which attributes are output and in what
order. This implementation also filters out the attribute called âmâ
whenever it appears:

```python
class UnsortedAttributes(HTMLFormatter):
 def attributes(self, tag):
 for k, v in tag.attrs.items():
 if k == 'm':
 continue
 yield k, v
print(attr_soup.p.encode(formatter=UnsortedAttributes()))
# <p z="1" a="3"></p>

```

class
UnsortedAttributes
HTMLFormatter
attributes
self
attrs
items
continue
yield
print
attr_soup
encode
formatter
UnsortedAttributes
()))
# <p z="1" a="3"></p>

One last caveat: if you create aCDataobject, the text inside
that object is always presentedexactly as it appears, with no
formatting. Beautiful Soup will call your entity substitution
function, just in case youâve written a custom function that counts
all the strings in the document or something, but it will ignore the
return value:

One last caveat: if you create a
CData
object, the text inside
that object is always presented
exactly as it appears, with no
formatting
. Beautiful Soup will call your entity substitution
function, just in case youâve written a custom function that counts
all the strings in the document or something, but it will ignore the
return value:

```python
from bs4.element import CData
soup = BeautifulSoup("<a></a>")
soup.a.string = CData("one < three")
print(soup.a.prettify(formatter="xml"))
# <a>
# <![CDATA[one < three]]>
# </a>

```

from
bs4.element
import
CData
soup
BeautifulSoup
"<a></a>"
soup
string
CData
"one < three"
print
soup
prettify
formatter
"xml"
# <a>
# <![CDATA[one < three]]>
# </a>

### get_text()Â¶

get_text()

If you only want the text part of a document or tag, you can use theget_text()method. It returns all the text in a document or
beneath a tag, as a single Unicode string:

If you only want the text part of a document or tag, you can use the
get_text()
method. It returns all the text in a document or
beneath a tag, as a single Unicode string:

```python
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup)

soup.get_text()
u'\nI linked to example.com\n'
soup.i.get_text()
u'example.com'

```

markup
'<a href="http://example.com/">
I linked to <i>example.com</i>
</a>'
soup
BeautifulSoup
markup
soup
get_text
I linked to example.com
soup
get_text
'example.com'

You can specify a string to be used to join the bits of text
together:

You can specify a string to be used to join the bits of text
together:

```python
# soup.get_text("|")
u'\nI linked to |example.com|\n'

```

# soup.get_text("|")
I linked to |example.com|

You can tell Beautiful Soup to strip whitespace from the beginning and
end of each bit of text:

You can tell Beautiful Soup to strip whitespace from the beginning and
end of each bit of text:

```python
# soup.get_text("|", strip=True)
u'I linked to|example.com'

```

# soup.get_text("|", strip=True)
'I linked to|example.com'

But at that point you might want to use the.stripped_stringsgenerator instead, and process the text yourself:

But at that point you might want to use the
.stripped_strings
generator instead, and process the text yourself:

```python
[text for text in soup.stripped_strings]
# [u'I linked to', u'example.com']

```

text
text
soup
stripped_strings
# [u'I linked to', u'example.com']

## Specifying the parser to useÂ¶

Specifying the parser to use

If you just need to parse some HTML, you can dump the markup into theBeautifulSoupconstructor, and itâll probably be fine. Beautiful
Soup will pick a parser for you and parse the data. But there are a
few additional arguments you can pass in to the constructor to change
which parser is used.

If you just need to parse some HTML, you can dump the markup into the
BeautifulSoup
constructor, and itâll probably be fine. Beautiful
Soup will pick a parser for you and parse the data. But there are a
few additional arguments you can pass in to the constructor to change
which parser is used.

The first argument to theBeautifulSoupconstructor is a string or
an open filehandleâthe markup you want parsed. The second argument ishowyouâd like the markup parsed.

The first argument to the
BeautifulSoup
constructor is a string or
an open filehandleâthe markup you want parsed. The second argument is
youâd like the markup parsed.

If you donât specify anything, youâll get the best HTML parser thatâs
installed. Beautiful Soup ranks lxmlâs parser as being the best, then
html5libâs, then Pythonâs built-in parser. You can override this by
specifying one of the following:

If you donât specify anything, youâll get the best HTML parser thatâs
installed. Beautiful Soup ranks lxmlâs parser as being the best, then
html5libâs, then Pythonâs built-in parser. You can override this by
specifying one of the following:

- What type of markup you want to parse. Currently supported are
âhtmlâ, âxmlâ, and âhtml5â.
- The name of the parser library you want to use. Currently supported
options are âlxmlâ, âhtml5libâ, and âhtml.parserâ (Pythonâs
built-in HTML parser).

What type of markup you want to parse. Currently supported are
âhtmlâ, âxmlâ, and âhtml5â.
The name of the parser library you want to use. Currently supported
options are âlxmlâ, âhtml5libâ, and âhtml.parserâ (Pythonâs
built-in HTML parser).

The sectionInstalling a parsercontrasts the supported parsers.

The section
Installing a parser
contrasts the supported parsers.

If you donât have an appropriate parser installed, Beautiful Soup will
ignore your request and pick a different parser. Right now, the only
supported XML parser is lxml. If you donât have lxml installed, asking
for an XML parser wonât give you one, and asking for âlxmlâ wonât work
either.

If you donât have an appropriate parser installed, Beautiful Soup will
ignore your request and pick a different parser. Right now, the only
supported XML parser is lxml. If you donât have lxml installed, asking
for an XML parser wonât give you one, and asking for âlxmlâ wonât work
either.

### Differences between parsersÂ¶

Differences between parsers

Beautiful Soup presents the same interface to a number of different
parsers, but each parser is different. Different parsers will create
different parse trees from the same document. The biggest differences
are between the HTML parsers and the XML parsers. Hereâs a short
document, parsed as HTML:

Beautiful Soup presents the same interface to a number of different
parsers, but each parser is different. Different parsers will create
different parse trees from the same document. The biggest differences
are between the HTML parsers and the XML parsers. Hereâs a short
document, parsed as HTML:

```python
BeautifulSoup("<a><b /></a>")
# <html><head></head><body><a><b></b></a></body></html>

```

BeautifulSoup
"<a><b /></a>"
# <html><head></head><body><a><b></b></a></body></html>

Since an empty <b /> tag is not valid HTML, the parser turns it into a
<b></b> tag pair.

Since an empty <b /> tag is not valid HTML, the parser turns it into a
<b></b> tag pair.

Hereâs the same document parsed as XML (running this requires that you
have lxml installed). Note that the empty <b /> tag is left alone, and
that the document is given an XML declaration instead of being put
into an <html> tag.:

Hereâs the same document parsed as XML (running this requires that you
have lxml installed). Note that the empty <b /> tag is left alone, and
that the document is given an XML declaration instead of being put
into an <html> tag.:

```python
BeautifulSoup("<a><b /></a>", "xml")
# <?xml version="1.0" encoding="utf-8"?>
# <a><b/></a>

```

BeautifulSoup
"<a><b /></a>"
"xml"
# <?xml version="1.0" encoding="utf-8"?>
# <a><b/></a>

There are also differences between HTML parsers. If you give Beautiful
Soup a perfectly-formed HTML document, these differences wonât
matter. One parser will be faster than another, but theyâll all give
you a data structure that looks exactly like the original HTML
document.

There are also differences between HTML parsers. If you give Beautiful
Soup a perfectly-formed HTML document, these differences wonât
matter. One parser will be faster than another, but theyâll all give
you a data structure that looks exactly like the original HTML
document.

But if the document is not perfectly-formed, different parsers will
give different results. Hereâs a short, invalid document parsed using
lxmlâs HTML parser. Note that the dangling </p> tag is simply
ignored:

But if the document is not perfectly-formed, different parsers will
give different results. Hereâs a short, invalid document parsed using
lxmlâs HTML parser. Note that the dangling </p> tag is simply
ignored:

```python
BeautifulSoup("<a></p>", "lxml")
# <html><body><a></a></body></html>

```

BeautifulSoup
"<a></p>"
"lxml"
# <html><body><a></a></body></html>

Hereâs the same document parsed using html5lib:

Hereâs the same document parsed using html5lib:

```python
BeautifulSoup("<a></p>", "html5lib")
# <html><head></head><body><a><p></p></a></body></html>

```

BeautifulSoup
"<a></p>"
"html5lib"
# <html><head></head><body><a><p></p></a></body></html>

Instead of ignoring the dangling </p> tag, html5lib pairs it with an
opening <p> tag. This parser also adds an empty <head> tag to the
document.

Instead of ignoring the dangling </p> tag, html5lib pairs it with an
opening <p> tag. This parser also adds an empty <head> tag to the
document.

Hereâs the same document parsed with Pythonâs built-in HTML
parser:

Hereâs the same document parsed with Pythonâs built-in HTML
parser:

```python
BeautifulSoup("<a></p>", "html.parser")
# <a></a>

```

BeautifulSoup
"<a></p>"
"html.parser"
# <a></a>

Like html5lib, this parser ignores the closing </p> tag. Unlike
html5lib, this parser makes no attempt to create a well-formed HTML
document by adding a <body> tag. Unlike lxml, it doesnât even bother
to add an <html> tag.

Like html5lib, this parser ignores the closing </p> tag. Unlike
html5lib, this parser makes no attempt to create a well-formed HTML
document by adding a <body> tag. Unlike lxml, it doesnât even bother
to add an <html> tag.

Since the document â<a></p>â is invalid, none of these techniques is
the âcorrectâ way to handle it. The html5lib parser uses techniques
that are part of the HTML5 standard, so it has the best claim on being
the âcorrectâ way, but all three techniques are legitimate.

Since the document â<a></p>â is invalid, none of these techniques is
the âcorrectâ way to handle it. The html5lib parser uses techniques
that are part of the HTML5 standard, so it has the best claim on being
the âcorrectâ way, but all three techniques are legitimate.

Differences between parsers can affect your script. If youâre planning
on distributing your script to other people, or running it on multiple
machines, you should specify a parser in theBeautifulSoupconstructor. That will reduce the chances that your users parse a
document differently from the way you parse it.

Differences between parsers can affect your script. If youâre planning
on distributing your script to other people, or running it on multiple
machines, you should specify a parser in the
BeautifulSoup
constructor. That will reduce the chances that your users parse a
document differently from the way you parse it.

## EncodingsÂ¶

Encodings

Any HTML or XML document is written in a specific encoding like ASCII
or UTF-8. But when you load that document into Beautiful Soup, youâll
discover itâs been converted to Unicode:

Any HTML or XML document is written in a specific encoding like ASCII
or UTF-8. But when you load that document into Beautiful Soup, youâll
discover itâs been converted to Unicode:

```python
markup = "<h1>Sacr\xc3\xa9 bleu!</h1>"
soup = BeautifulSoup(markup)
soup.h1
# <h1>SacrÃ© bleu!</h1>
soup.h1.string
# u'Sacr\xe9 bleu!'

```

markup
"<h1>Sacr
\xc3\xa9
bleu!</h1>"
soup
BeautifulSoup
markup
soup
# <h1>SacrÃ© bleu!</h1>
soup
string
# u'Sacr\xe9 bleu!'

Itâs not magic. (That sure would be nice.) Beautiful Soup uses a
sub-library calledUnicode, Dammitto detect a documentâs encoding
and convert it to Unicode. The autodetected encoding is available as
the.original_encodingattribute of theBeautifulSoupobject:

Itâs not magic. (That sure would be nice.) Beautiful Soup uses a
sub-library called
Unicode, Dammit
to detect a documentâs encoding
and convert it to Unicode. The autodetected encoding is available as
the
.original_encoding
attribute of the
BeautifulSoup
object:

```python
soup.original_encoding
'utf-8'

```

soup
original_encoding
'utf-8'

Unicode, Dammit guesses correctly most of the time, but sometimes it
makes mistakes. Sometimes it guesses correctly, but only after a
byte-by-byte search of the document that takes a very long time. If
you happen to know a documentâs encoding ahead of time, you can avoid
mistakes and delays by passing it to theBeautifulSoupconstructor
asfrom_encoding.

Unicode, Dammit guesses correctly most of the time, but sometimes it
makes mistakes. Sometimes it guesses correctly, but only after a
byte-by-byte search of the document that takes a very long time. If
you happen to know a documentâs encoding ahead of time, you can avoid
mistakes and delays by passing it to the
BeautifulSoup
constructor
as
from_encoding

Hereâs a document written in ISO-8859-8. The document is so short that
Unicode, Dammit canât get a lock on it, and misidentifies it as
ISO-8859-7:

Hereâs a document written in ISO-8859-8. The document is so short that
Unicode, Dammit canât get a lock on it, and misidentifies it as
ISO-8859-7:

```python
markup = b"<h1>\xed\xe5\xec\xf9</h1>"
soup = BeautifulSoup(markup)
soup.h1
<h1>Î½ÎµÎ¼Ï</h1>
soup.original_encoding
'ISO-8859-7'

```

markup
"<h1>
\xed\xe5\xec\xf9
</h1>"
soup
BeautifulSoup
markup
soup
Î½ÎµÎ¼Ï
soup
original_encoding
'ISO-8859-7'

We can fix this by passing in the correctfrom_encoding:

We can fix this by passing in the correct
from_encoding

```python
soup = BeautifulSoup(markup, from_encoding="iso-8859-8")
soup.h1
<h1>××××©</h1>
soup.original_encoding
'iso8859-8'

```

soup
BeautifulSoup
markup
from_encoding
"iso-8859-8"
soup
××××©
soup
original_encoding
'iso8859-8'

If you donât know what the correct encoding is, but you know that
Unicode, Dammit is guessing wrong, you can pass the wrong guesses in
asexclude_encodings:

If you donât know what the correct encoding is, but you know that
Unicode, Dammit is guessing wrong, you can pass the wrong guesses in
as
exclude_encodings

```python
soup = BeautifulSoup(markup, exclude_encodings=["ISO-8859-7"])
soup.h1
<h1>××××©</h1>
soup.original_encoding
'WINDOWS-1255'

```

soup
BeautifulSoup
markup
exclude_encodings
"ISO-8859-7"
soup
××××©
soup
original_encoding
'WINDOWS-1255'

Windows-1255 isnât 100% correct, but that encoding is a compatible
superset of ISO-8859-8, so itâs close enough. (exclude_encodingsis a new feature in Beautiful Soup 4.4.0.)

Windows-1255 isnât 100% correct, but that encoding is a compatible
superset of ISO-8859-8, so itâs close enough. (
exclude_encodings
is a new feature in Beautiful Soup 4.4.0.)

In rare cases (usually when a UTF-8 document contains text written in
a completely different encoding), the only way to get Unicode may be
to replace some characters with the special Unicode character
âREPLACEMENT CHARACTERâ (U+FFFD, ï¿½). If Unicode, Dammit needs to do
this, it will set the.contains_replacement_charactersattribute
toTrueon theUnicodeDammitorBeautifulSoupobject. This
lets you know that the Unicode representation is not an exact
representation of the originalâsome data was lost. If a document
contains ï¿½, but.contains_replacement_charactersisFalse,
youâll know that the ï¿½ was there originally (as it is in this
paragraph) and doesnât stand in for missing data.

In rare cases (usually when a UTF-8 document contains text written in
a completely different encoding), the only way to get Unicode may be
to replace some characters with the special Unicode character
âREPLACEMENT CHARACTERâ (U+FFFD, ï¿½). If Unicode, Dammit needs to do
this, it will set the
.contains_replacement_characters
attribute
to
True
on the
UnicodeDammit
BeautifulSoup
object. This
lets you know that the Unicode representation is not an exact
representation of the originalâsome data was lost. If a document
contains ï¿½, but
.contains_replacement_characters
False
,
youâll know that the ï¿½ was there originally (as it is in this
paragraph) and doesnât stand in for missing data.

### Output encodingÂ¶

Output encoding

When you write out a document from Beautiful Soup, you get a UTF-8
document, even if the document wasnât in UTF-8 to begin with. Hereâs a
document written in the Latin-1 encoding:

When you write out a document from Beautiful Soup, you get a UTF-8
document, even if the document wasnât in UTF-8 to begin with. Hereâs a
document written in the Latin-1 encoding:

```python
markup = b'''
 <html>
 <head>
 <meta content="text/html; charset=ISO-Latin-1" http-equiv="Content-type" />
 </head>
 <body>
 <p>Sacr\xe9 bleu!</p>
 </body>
 </html>
'''

soup = BeautifulSoup(markup)
print(soup.prettify())
# <html>
# <head>
# <meta content="text/html; charset=utf-8" http-equiv="Content-type" />
# </head>
# <body>
# <p>
# SacrÃ© bleu!
# </p>
# </body>
# </html>

```

markup
<html>
<head>
<meta content="text/html; charset=ISO-Latin-1" http-equiv="Content-type" />
</head>
<body>
<p>Sacr
\xe9
bleu!</p>
</body>
</html>
soup
BeautifulSoup
markup
print
soup
prettify
# <html>
# <head>
# <meta content="text/html; charset=utf-8" http-equiv="Content-type" />
# </head>
# <body>
# <p>
# SacrÃ© bleu!
# </p>
# </body>
# </html>

Note that the <meta> tag has been rewritten to reflect the fact that
the document is now in UTF-8.

Note that the <meta> tag has been rewritten to reflect the fact that
the document is now in UTF-8.

If you donât want UTF-8, you can pass an encoding intoprettify():

If you donât want UTF-8, you can pass an encoding into
prettify()

```python
print(soup.prettify("latin-1"))
# <html>
# <head>
# <meta content="text/html; charset=latin-1" http-equiv="Content-type" />
# ...

```

print
soup
prettify
"latin-1"
# <html>
# <head>
# <meta content="text/html; charset=latin-1" http-equiv="Content-type" />
# ...

You can also call encode() on theBeautifulSoupobject, or any
element in the soup, just as if it were a Python string:

You can also call encode() on the
BeautifulSoup
object, or any
element in the soup, just as if it were a Python string:

```python
soup.p.encode("latin-1")
# '<p>Sacr\xe9 bleu!</p>'

soup.p.encode("utf-8")
# '<p>Sacr\xc3\xa9 bleu!</p>'

```

soup
encode
"latin-1"
# '<p>Sacr\xe9 bleu!</p>'
soup
encode
"utf-8"
# '<p>Sacr\xc3\xa9 bleu!</p>'

Any characters that canât be represented in your chosen encoding will
be converted into numeric XML entity references. Hereâs a document
that includes the Unicode character SNOWMAN:

Any characters that canât be represented in your chosen encoding will
be converted into numeric XML entity references. Hereâs a document
that includes the Unicode character SNOWMAN:

```python
markup = u"<b>\N{SNOWMAN}</b>"
snowman_soup = BeautifulSoup(markup)
tag = snowman_soup.b

```

markup
"<b>
\N{SNOWMAN}
</b>"
snowman_soup
BeautifulSoup
markup
snowman_soup

The SNOWMAN character can be part of a UTF-8 document (it looks like
â), but thereâs no representation for that character in ISO-Latin-1 or
ASCII, so itâs converted into â&#9731â for those encodings:

The SNOWMAN character can be part of a UTF-8 document (it looks like
â), but thereâs no representation for that character in ISO-Latin-1 or
ASCII, so itâs converted into â&#9731â for those encodings:

```python
print(tag.encode("utf-8"))
# <b>â</b>

print tag.encode("latin-1")
# <b>&#9731;</b>

print tag.encode("ascii")
# <b>&#9731;</b>

```

print
encode
"utf-8"
# <b>â</b>
print
encode
"latin-1"
# <b>&#9731;</b>
print
encode
"ascii"
# <b>&#9731;</b>

### Unicode, DammitÂ¶

Unicode, Dammit

You can use Unicode, Dammit without using Beautiful Soup. Itâs useful
whenever you have data in an unknown encoding and you just want it to
become Unicode:

You can use Unicode, Dammit without using Beautiful Soup. Itâs useful
whenever you have data in an unknown encoding and you just want it to
become Unicode:

```python
from bs4 import UnicodeDammit
dammit = UnicodeDammit("Sacr\xc3\xa9 bleu!")
print(dammit.unicode_markup)
# SacrÃ© bleu!
dammit.original_encoding
# 'utf-8'

```

from
import
UnicodeDammit
dammit
UnicodeDammit
"Sacr
\xc3\xa9
bleu!"
print
dammit
unicode_markup
# SacrÃ© bleu!
dammit
original_encoding
# 'utf-8'

Unicode, Dammitâs guesses will get a lot more accurate if you install
thechardetorcchardetPython libraries. The more data you
give Unicode, Dammit, the more accurately it will guess. If you have
your own suspicions as to what the encoding might be, you can pass
them in as a list:

Unicode, Dammitâs guesses will get a lot more accurate if you install
the
chardet
cchardet
Python libraries. The more data you
give Unicode, Dammit, the more accurately it will guess. If you have
your own suspicions as to what the encoding might be, you can pass
them in as a list:

```python
dammit = UnicodeDammit("Sacr\xe9 bleu!", ["latin-1", "iso-8859-1"])
print(dammit.unicode_markup)
# SacrÃ© bleu!
dammit.original_encoding
# 'latin-1'

```

dammit
UnicodeDammit
"Sacr
\xe9
bleu!"
"latin-1"
"iso-8859-1"
print
dammit
unicode_markup
# SacrÃ© bleu!
dammit
original_encoding
# 'latin-1'

Unicode, Dammit has two special features that Beautiful Soup doesnât
use.

Unicode, Dammit has two special features that Beautiful Soup doesnât
use.

#### Smart quotesÂ¶

Smart quotes

You can use Unicode, Dammit to convert Microsoft smart quotes to HTML or XML
entities:

You can use Unicode, Dammit to convert Microsoft smart quotes to HTML or XML
entities:

```python
markup = b"<p>I just \x93love\x94 Microsoft Word\x92s smart quotes</p>"

UnicodeDammit(markup, ["windows-1252"], smart_quotes_to="html").unicode_markup
# u'<p>I just &ldquo;love&rdquo; Microsoft Word&rsquo;s smart quotes</p>'

UnicodeDammit(markup, ["windows-1252"], smart_quotes_to="xml").unicode_markup
# u'<p>I just &#x201C;love&#x201D; Microsoft Word&#x2019;s smart quotes</p>'

```

markup
"<p>I just
\x93
love
\x94
Microsoft Word
\x92
s smart quotes</p>"
UnicodeDammit
markup
"windows-1252"
smart_quotes_to
"html"
unicode_markup
# u'<p>I just &ldquo;love&rdquo; Microsoft Word&rsquo;s smart quotes</p>'
UnicodeDammit
markup
"windows-1252"
smart_quotes_to
"xml"
unicode_markup
# u'<p>I just &#x201C;love&#x201D; Microsoft Word&#x2019;s smart quotes</p>'

You can also convert Microsoft smart quotes to ASCII quotes:

You can also convert Microsoft smart quotes to ASCII quotes:

```python
UnicodeDammit(markup, ["windows-1252"], smart_quotes_to="ascii").unicode_markup
# u'<p>I just "love" Microsoft Word\'s smart quotes</p>'

```

UnicodeDammit
markup
"windows-1252"
smart_quotes_to
"ascii"
unicode_markup
# u'<p>I just "love" Microsoft Word\'s smart quotes</p>'

Hopefully youâll find this feature useful, but Beautiful Soup doesnât
use it. Beautiful Soup prefers the default behavior, which is to
convert Microsoft smart quotes to Unicode characters along with
everything else:

Hopefully youâll find this feature useful, but Beautiful Soup doesnât
use it. Beautiful Soup prefers the default behavior, which is to
convert Microsoft smart quotes to Unicode characters along with
everything else:

```python
UnicodeDammit(markup, ["windows-1252"]).unicode_markup
# u'<p>I just \u201clove\u201d Microsoft Word\u2019s smart quotes</p>'

```

UnicodeDammit
markup
"windows-1252"
unicode_markup
# u'<p>I just \u201clove\u201d Microsoft Word\u2019s smart quotes</p>'

#### Inconsistent encodingsÂ¶

Inconsistent encodings

Sometimes a document is mostly in UTF-8, but contains Windows-1252
characters such as (again) Microsoft smart quotes. This can happen
when a website includes data from multiple sources. You can useUnicodeDammit.detwingle()to turn such a document into pure
UTF-8. Hereâs a simple example:

Sometimes a document is mostly in UTF-8, but contains Windows-1252
characters such as (again) Microsoft smart quotes. This can happen
when a website includes data from multiple sources. You can use
UnicodeDammit.detwingle()
to turn such a document into pure
UTF-8. Hereâs a simple example:

```python
snowmen = (u"\N{SNOWMAN}" * 3)
quote = (u"\N{LEFT DOUBLE QUOTATION MARK}I like snowmen!\N{RIGHT DOUBLE QUOTATION MARK}")
doc = snowmen.encode("utf8") + quote.encode("windows_1252")

```

snowmen
\N{SNOWMAN}
quote
\N{LEFT DOUBLE QUOTATION MARK}
I like snowmen!
\N{RIGHT DOUBLE QUOTATION MARK}
snowmen
encode
"utf8"
quote
encode
"windows_1252"

This document is a mess. The snowmen are in UTF-8 and the quotes are
in Windows-1252. You can display the snowmen or the quotes, but not
both:

This document is a mess. The snowmen are in UTF-8 and the quotes are
in Windows-1252. You can display the snowmen or the quotes, but not
both:

```python
print(doc)
# âââï¿½I like snowmen!ï¿½

print(doc.decode("windows-1252"))
# Ã¢ËÆÃ¢ËÆÃ¢ËÆâI like snowmen!â

```

print
# âââï¿½I like snowmen!ï¿½
print
decode
"windows-1252"
# Ã¢ËÆÃ¢ËÆÃ¢ËÆâI like snowmen!â

Decoding the document as UTF-8 raises aUnicodeDecodeError, and
decoding it as Windows-1252 gives you gibberish. Fortunately,UnicodeDammit.detwingle()will convert the string to pure UTF-8,
allowing you to decode it to Unicode and display the snowmen and quote
marks simultaneously:

Decoding the document as UTF-8 raises a
UnicodeDecodeError
, and
decoding it as Windows-1252 gives you gibberish. Fortunately,
UnicodeDammit.detwingle()
will convert the string to pure UTF-8,
allowing you to decode it to Unicode and display the snowmen and quote
marks simultaneously:

```python
new_doc = UnicodeDammit.detwingle(doc)
print(new_doc.decode("utf8"))
# ââââI like snowmen!â

```

new_doc
UnicodeDammit
detwingle
print
new_doc
decode
"utf8"
# ââââI like snowmen!â

UnicodeDammit.detwingle()only knows how to handle Windows-1252
embedded in UTF-8 (or vice versa, I suppose), but this is the most
common case.

UnicodeDammit.detwingle()
only knows how to handle Windows-1252
embedded in UTF-8 (or vice versa, I suppose), but this is the most
common case.

Note that you must know to callUnicodeDammit.detwingle()on your
data before passing it intoBeautifulSoupor theUnicodeDammitconstructor. Beautiful Soup assumes that a document has a single
encoding, whatever it might be. If you pass it a document that
contains both UTF-8 and Windows-1252, itâs likely to think the whole
document is Windows-1252, and the document will come out looking likeÃ¢ËÆÃ¢ËÆÃ¢ËÆâIlikesnowmen!â.

Note that you must know to call
UnicodeDammit.detwingle()
on your
data before passing it into
BeautifulSoup
or the
UnicodeDammit
constructor. Beautiful Soup assumes that a document has a single
encoding, whatever it might be. If you pass it a document that
contains both UTF-8 and Windows-1252, itâs likely to think the whole
document is Windows-1252, and the document will come out looking like
Ã¢ËÆÃ¢ËÆÃ¢ËÆâI
like
snowmen!â

UnicodeDammit.detwingle()is new in Beautiful Soup 4.1.0.

UnicodeDammit.detwingle()
is new in Beautiful Soup 4.1.0.

## Line numbersÂ¶

Line numbers

Thehtml.parser`and``html5libparsers can keep track of where in
the original document each Tag was found. You can access this
information asTag.sourceline(line number) andTag.sourcepos(position of the start tag within a line):

html.parser`
``html5lib
parsers can keep track of where in
the original document each Tag was found. You can access this
information as
Tag.sourceline
(line number) and
Tag.sourcepos
(position of the start tag within a line):

```python
markup = "<p\n>Paragraph 1</p>\n <p>Paragraph 2</p>"
soup = BeautifulSoup(markup, 'html.parser')
for tag in soup.find_all('p'):
 print(tag.sourceline, tag.sourcepos, tag.string)
# (1, 0, u'Paragraph 1')
# (2, 3, u'Paragraph 2')

```

markup
>Paragraph 1</p>
<p>Paragraph 2</p>"
soup
BeautifulSoup
markup
'html.parser'
soup
find_all
print
sourceline
sourcepos
string
# (1, 0, u'Paragraph 1')
# (2, 3, u'Paragraph 2')

Note that the two parsers mean slightly different things bysourcelineandsourcepos. For html.parser, these numbers
represent the position of the initial less-than sign. For html5lib,
these numbers represent the position of the final greater-than sign:

Note that the two parsers mean slightly different things by
sourceline
sourcepos
. For html.parser, these numbers
represent the position of the initial less-than sign. For html5lib,
these numbers represent the position of the final greater-than sign:

```python
soup = BeautifulSoup(markup, 'html5lib')
for tag in soup.find_all('p'):
 print(tag.sourceline, tag.sourcepos, tag.string)
# (2, 1, u'Paragraph 1')
# (3, 7, u'Paragraph 2')

```

soup
BeautifulSoup
markup
'html5lib'
soup
find_all
print
sourceline
sourcepos
string
# (2, 1, u'Paragraph 1')
# (3, 7, u'Paragraph 2')

You can shut off this feature by passingstore_line_numbers=False`intothe``BeautifulSoupconstructor:

You can shut off this feature by passing
store_line_numbers=False`
into
``BeautifulSoup
constructor:

```python
markup = "<p\n>Paragraph 1</p>\n <p>Paragraph 2</p>"
soup = BeautifulSoup(markup, 'html.parser', store_line_numbers=False)
soup.p.sourceline
# None

```

markup
>Paragraph 1</p>
<p>Paragraph 2</p>"
soup
BeautifulSoup
markup
'html.parser'
store_line_numbers
False
soup
sourceline
# None

This feature is new in 4.8.1, and the parsers based on lxml donât
support it.

This feature is new in 4.8.1, and the parsers based on lxml donât
support it.

## Comparing objects for equalityÂ¶

Comparing objects for equality

Beautiful Soup says that twoNavigableStringorTagobjects
are equal when they represent the same HTML or XML markup. In this
example, the two <b> tags are treated as equal, even though they live
in different parts of the object tree, because they both look like
â<b>pizza</b>â:

Beautiful Soup says that two
NavigableString
objects
are equal when they represent the same HTML or XML markup. In this
example, the two <b> tags are treated as equal, even though they live
in different parts of the object tree, because they both look like
â<b>pizza</b>â:

```python
markup = "<p>I want <b>pizza</b> and more <b>pizza</b>!</p>"
soup = BeautifulSoup(markup, 'html.parser')
first_b, second_b = soup.find_all('b')
print first_b == second_b
# True

print first_b.previous_element == second_b.previous_element
# False

```

markup
"<p>I want <b>pizza</b> and more <b>pizza</b>!</p>"
soup
BeautifulSoup
markup
'html.parser'
first_b
second_b
soup
find_all
print
first_b
second_b
# True
print
first_b
second_b
# False

If you want to see whether two variables refer to exactly the same
object, useis:

If you want to see whether two variables refer to exactly the same
object, use

```python
print first_b is second_b
# False

```

print
first_b
second_b
# False

## Copying Beautiful Soup objectsÂ¶

Copying Beautiful Soup objects

You can usecopy.copy()to create a copy of anyTagorNavigableString:

You can use
copy.copy()
to create a copy of any
NavigableString

```python
import copy
p_copy = copy.copy(soup.p)
print p_copy
# <p>I want <b>pizza</b> and more <b>pizza</b>!</p>

```

import
copy
p_copy
copy
copy
soup
print
p_copy
# <p>I want <b>pizza</b> and more <b>pizza</b>!</p>

The copy is considered equal to the original, since it represents the
same markup as the original, but itâs not the same object:

The copy is considered equal to the original, since it represents the
same markup as the original, but itâs not the same object:

```python
print soup.p == p_copy
# True

print soup.p is p_copy
# False

```

print
soup
p_copy
# True
print
soup
p_copy
# False

The only real difference is that the copy is completely detached from
the original Beautiful Soup object tree, just as ifextract()had
been called on it:

The only real difference is that the copy is completely detached from
the original Beautiful Soup object tree, just as if
extract()
had
been called on it:

```python
print p_copy.parent
# None

```

print
p_copy
parent
# None

This is because two differentTagobjects canât occupy the same
space at the same time.

This is because two different
objects canât occupy the same
space at the same time.

## Parsing only part of a documentÂ¶

Parsing only part of a document

Letâs say you want to use Beautiful Soup look at a documentâs <a>
tags. Itâs a waste of time and memory to parse the entire document and
then go over it again looking for <a> tags. It would be much faster to
ignore everything that wasnât an <a> tag in the first place. TheSoupStrainerclass allows you to choose which parts of an incoming
document are parsed. You just create aSoupStrainerand pass it in
to theBeautifulSoupconstructor as theparse_onlyargument.

Letâs say you want to use Beautiful Soup look at a documentâs <a>
tags. Itâs a waste of time and memory to parse the entire document and
then go over it again looking for <a> tags. It would be much faster to
ignore everything that wasnât an <a> tag in the first place. The
SoupStrainer
class allows you to choose which parts of an incoming
document are parsed. You just create a
SoupStrainer
and pass it in
to the
BeautifulSoup
constructor as the
parse_only
argument.

(Note thatthis feature wonât work if youâre using the html5lib parser.
If you use html5lib, the whole document will be parsed, no
matter what. This is because html5lib constantly rearranges the parse
tree as it works, and if some part of the document didnât actually
make it into the parse tree, itâll crash. To avoid confusion, in the
examples below Iâll be forcing Beautiful Soup to use Pythonâs
built-in parser.)

(Note that
this feature wonât work if youâre using the html5lib parser
.
If you use html5lib, the whole document will be parsed, no
matter what. This is because html5lib constantly rearranges the parse
tree as it works, and if some part of the document didnât actually
make it into the parse tree, itâll crash. To avoid confusion, in the
examples below Iâll be forcing Beautiful Soup to use Pythonâs
built-in parser.)

### SoupStrainerÂ¶

SoupStrainer

TheSoupStrainerclass takes the same arguments as a typical
method fromSearching the tree:name,attrs,string, and**kwargs. Here are
threeSoupStrainerobjects:

SoupStrainer
class takes the same arguments as a typical
method from
Searching the tree
name
attrs
string
, and
**kwargs
. Here are
three
SoupStrainer
objects:

```python
from bs4 import SoupStrainer

only_a_tags = SoupStrainer("a")

only_tags_with_id_link2 = SoupStrainer(id="link2")

def is_short_string(string):
 return len(string) < 10

only_short_strings = SoupStrainer(string=is_short_string)

```

from
import
SoupStrainer
only_a_tags
SoupStrainer
only_tags_with_id_link2
SoupStrainer
"link2"
is_short_string
string
return
string
only_short_strings
SoupStrainer
string
is_short_string

Iâm going to bring back the âthree sistersâ document one more time,
and weâll see what the document looks like when itâs parsed with these
threeSoupStrainerobjects:

Iâm going to bring back the âthree sistersâ document one more time,
and weâll see what the document looks like when itâs parsed with these
three
SoupStrainer
objects:

```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

print(BeautifulSoup(html_doc, "html.parser", parse_only=only_a_tags).prettify())
# <a class="sister" href="http://example.com/elsie" id="link1">
# Elsie
# </a>
# <a class="sister" href="http://example.com/lacie" id="link2">
# Lacie
# </a>
# <a class="sister" href="http://example.com/tillie" id="link3">
# Tillie
# </a>

print(BeautifulSoup(html_doc, "html.parser", parse_only=only_tags_with_id_link2).prettify())
# <a class="sister" href="http://example.com/lacie" id="link2">
# Lacie
# </a>

print(BeautifulSoup(html_doc, "html.parser", parse_only=only_short_strings).prettify())
# Elsie
# ,
# Lacie
# and
# Tillie
# ...
#

```

html_doc
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
print
BeautifulSoup
html_doc
"html.parser"
parse_only
only_a_tags
prettify
# <a class="sister" href="http://example.com/elsie" id="link1">
# Elsie
# </a>
# <a class="sister" href="http://example.com/lacie" id="link2">
# Lacie
# </a>
# <a class="sister" href="http://example.com/tillie" id="link3">
# Tillie
# </a>
print
BeautifulSoup
html_doc
"html.parser"
parse_only
only_tags_with_id_link2
prettify
# <a class="sister" href="http://example.com/lacie" id="link2">
# Lacie
# </a>
print
BeautifulSoup
html_doc
"html.parser"
parse_only
only_short_strings
prettify
# Elsie
# Lacie
# and
# Tillie
# ...

You can also pass aSoupStrainerinto any of the methods covered
inSearching the tree. This probably isnât terribly useful, but I
thought Iâd mention it:

You can also pass a
SoupStrainer
into any of the methods covered
in
Searching the tree
. This probably isnât terribly useful, but I
thought Iâd mention it:

```python
soup = BeautifulSoup(html_doc)
soup.find_all(only_short_strings)
# [u'\n\n', u'\n\n', u'Elsie', u',\n', u'Lacie', u' and\n', u'Tillie',
# u'\n\n', u'...', u'\n']

```

soup
BeautifulSoup
html_doc
soup
find_all
only_short_strings
# [u'\n\n', u'\n\n', u'Elsie', u',\n', u'Lacie', u' and\n', u'Tillie',
# u'\n\n', u'...', u'\n']

## TroubleshootingÂ¶

Troubleshooting

### diagnose()Â¶

diagnose()

If youâre having trouble understanding what Beautiful Soup does to a
document, pass the document into thediagnose()function. (New in
Beautiful Soup 4.2.0.) Beautiful Soup will print out a report showing
you how different parsers handle the document, and tell you if youâre
missing a parser that Beautiful Soup could be using:

If youâre having trouble understanding what Beautiful Soup does to a
document, pass the document into the
diagnose()
function. (New in
Beautiful Soup 4.2.0.) Beautiful Soup will print out a report showing
you how different parsers handle the document, and tell you if youâre
missing a parser that Beautiful Soup could be using:

```python
from bs4.diagnose import diagnose
with open("bad.html") as fp:
 data = fp.read()
diagnose(data)

# Diagnostic running on Beautiful Soup 4.2.0
# Python version 2.7.3 (default, Aug 1 2012, 05:16:07)
# I noticed that html5lib is not installed. Installing it may help.
# Found lxml version 2.3.2.0
#
# Trying to parse your data with html.parser
# Here's what html.parser did with the document:
# ...

```

from
bs4.diagnose
import
diagnose
with
open
"bad.html"
data
read
diagnose
data
# Diagnostic running on Beautiful Soup 4.2.0
# Python version 2.7.3 (default, Aug 1 2012, 05:16:07)
# I noticed that html5lib is not installed. Installing it may help.
# Found lxml version 2.3.2.0
# Trying to parse your data with html.parser
# Here's what html.parser did with the document:
# ...

Just looking at the output of diagnose() may show you how to solve the
problem. Even if not, you can paste the output ofdiagnose()when
asking for help.

Just looking at the output of diagnose() may show you how to solve the
problem. Even if not, you can paste the output of
diagnose()
when
asking for help.

### Errors when parsing a documentÂ¶

Errors when parsing a document

There are two different kinds of parse errors. There are crashes,
where you feed a document to Beautiful Soup and it raises an
exception, usually anHTMLParser.HTMLParseError. And there is
unexpected behavior, where a Beautiful Soup parse tree looks a lot
different than the document used to create it.

There are two different kinds of parse errors. There are crashes,
where you feed a document to Beautiful Soup and it raises an
exception, usually an
HTMLParser.HTMLParseError
. And there is
unexpected behavior, where a Beautiful Soup parse tree looks a lot
different than the document used to create it.

Almost none of these problems turn out to be problems with Beautiful
Soup. This is not because Beautiful Soup is an amazingly well-written
piece of software. Itâs because Beautiful Soup doesnât include any
parsing code. Instead, it relies on external parsers. If one parser
isnât working on a certain document, the best solution is to try a
different parser. SeeInstalling a parserfor details and a parser
comparison.

Almost none of these problems turn out to be problems with Beautiful
Soup. This is not because Beautiful Soup is an amazingly well-written
piece of software. Itâs because Beautiful Soup doesnât include any
parsing code. Instead, it relies on external parsers. If one parser
isnât working on a certain document, the best solution is to try a
different parser. See
Installing a parser
for details and a parser
comparison.

The most common parse errors areHTMLParser.HTMLParseError:malformedstarttagandHTMLParser.HTMLParseError:badendtag. These are both generated by Pythonâs built-in HTML parser
library, and the solution is toinstall lxml or
html5lib.

The most common parse errors are
HTMLParser.HTMLParseError:
malformed
start
HTMLParser.HTMLParseError:
. These are both generated by Pythonâs built-in HTML parser
library, and the solution is to
install lxml or
html5lib.

The most common type of unexpected behavior is that you canât find a
tag that you know is in the document. You saw it going in, butfind_all()returns[]orfind()returnsNone. This is
another common problem with Pythonâs built-in HTML parser, which
sometimes skips tags it doesnât understand. Again, the solution is toinstall lxml or html5lib.

The most common type of unexpected behavior is that you canât find a
tag that you know is in the document. You saw it going in, but
find_all()
returns
find()
returns
None
. This is
another common problem with Pythonâs built-in HTML parser, which
sometimes skips tags it doesnât understand. Again, the solution is to
install lxml or html5lib.

### Version mismatch problemsÂ¶

Version mismatch problems

- SyntaxError:Invalidsyntax(on the lineROOT_TAG_NAME=u'[document]'): Caused by running the Python 2 version of
Beautiful Soup under Python 3, without converting the code.
- ImportError:NomodulenamedHTMLParser- Caused by running the
Python 2 version of Beautiful Soup under Python 3.
- ImportError:Nomodulenamedhtml.parser- Caused by running the
Python 3 version of Beautiful Soup under Python 2.
- ImportError:NomodulenamedBeautifulSoup- Caused by running
Beautiful Soup 3 code on a system that doesnât have BS3
installed. Or, by writing Beautiful Soup 4 code without knowing that
the package name has changed tobs4.
- ImportError:Nomodulenamedbs4- Caused by running Beautiful
Soup 4 code on a system that doesnât have BS4 installed.

SyntaxError:
Invalid
syntax
(on the line
ROOT_TAG_NAME
u'[document]'
): Caused by running the Python 2 version of
Beautiful Soup under Python 3, without converting the code.
ImportError:
module
named
HTMLParser
- Caused by running the
Python 2 version of Beautiful Soup under Python 3.
ImportError:
module
named
html.parser
- Caused by running the
Python 3 version of Beautiful Soup under Python 2.
ImportError:
module
named
BeautifulSoup
- Caused by running
Beautiful Soup 3 code on a system that doesnât have BS3
installed. Or, by writing Beautiful Soup 4 code without knowing that
the package name has changed to
ImportError:
module
named
- Caused by running Beautiful
Soup 4 code on a system that doesnât have BS4 installed.

### Parsing XMLÂ¶

Parsing XML

By default, Beautiful Soup parses documents as HTML. To parse a
document as XML, pass in âxmlâ as the second argument to theBeautifulSoupconstructor:

By default, Beautiful Soup parses documents as HTML. To parse a
document as XML, pass in âxmlâ as the second argument to the
BeautifulSoup
constructor:

```python
soup = BeautifulSoup(markup, "xml")

```

soup
BeautifulSoup
markup
"xml"

Youâll need tohave lxml installed.

Youâll need to
have lxml installed

### Other parser problemsÂ¶

Other parser problems

- If your script works on one computer but not another, or in one
virtual environment but not another, or outside the virtual
environment but not inside, itâs probably because the two
environments have different parser libraries available. For example,
you may have developed the script on a computer that has lxml
installed, and then tried to run it on a computer that only has
html5lib installed. SeeDifferences between parsersfor why this
matters, and fix the problem by mentioning a specific parser library
in theBeautifulSoupconstructor.
- BecauseHTML tags and attributes are case-insensitive, all three HTML
parsers convert tag and attribute names to lowercase. That is, the
markup <TAG></TAG> is converted to <tag></tag>. If you want to
preserve mixed-case or uppercase tags and attributes, youâll need toparse the document as XML.

If your script works on one computer but not another, or in one
virtual environment but not another, or outside the virtual
environment but not inside, itâs probably because the two
environments have different parser libraries available. For example,
you may have developed the script on a computer that has lxml
installed, and then tried to run it on a computer that only has
html5lib installed. See
Differences between parsers
for why this
matters, and fix the problem by mentioning a specific parser library
in the
BeautifulSoup
constructor.
Because
HTML tags and attributes are case-insensitive
, all three HTML
parsers convert tag and attribute names to lowercase. That is, the
markup <TAG></TAG> is converted to <tag></tag>. If you want to
preserve mixed-case or uppercase tags and attributes, youâll need to
parse the document as XML.

### MiscellaneousÂ¶

Miscellaneous

- UnicodeEncodeError:'charmap'codeccan'tencodecharacteru'\xfoo'inpositionbar(or just about any otherUnicodeEncodeError) - This is not a problem with Beautiful Soup.
This problem shows up in two main situations. First, when you try to
print a Unicode character that your console doesnât know how to
display. (Seethis page on the Python wikifor help.) Second, when
youâre writing to a file and you pass in a Unicode character thatâs
not supported by your default encoding. In this case, the simplest
solution is to explicitly encode the Unicode string into UTF-8 withu.encode("utf8").
- KeyError:[attr]- Caused by accessingtag['attr']when the
tag in question doesnât define theattrattribute. The most
common errors areKeyError:'href'andKeyError:'class'. Usetag.get('attr')if youâre not sureattris
defined, just as you would with a Python dictionary.
- AttributeError:'ResultSet'objecthasnoattribute'foo'- This
usually happens because you expectedfind_all()to return a
single tag or string. Butfind_all()returns a _list_ of tags
and stringsâaResultSetobject. You need to iterate over the
list and look at the.fooof each one. Or, if you really only
want one result, you need to usefind()instead offind_all().
- AttributeError:'NoneType'objecthasnoattribute'foo'- This
usually happens because you calledfind()and then tried to
access the.foo`attribute of the result. But in your case,find()didnât find anything, so it returnedNone, instead of
returning a tag or a string. You need to figure out why yourfind()call isnât returning anything.

UnicodeEncodeError:
'charmap'
codec
can't
encode
character
u'\xfoo'
position
(or just about any other
UnicodeEncodeError
) - This is not a problem with Beautiful Soup.
This problem shows up in two main situations. First, when you try to
print a Unicode character that your console doesnât know how to
display. (See
this page on the Python wiki
for help.) Second, when
youâre writing to a file and you pass in a Unicode character thatâs
not supported by your default encoding. In this case, the simplest
solution is to explicitly encode the Unicode string into UTF-8 with
u.encode("utf8")
KeyError:
[attr]
- Caused by accessing
tag['attr']
when the
tag in question doesnât define the
attr
attribute. The most
common errors are
KeyError:
'href'
KeyError:
'class'
. Use
tag.get('attr')
if youâre not sure
attr
is
defined, just as you would with a Python dictionary.
AttributeError:
'ResultSet'
object
attribute
'foo'
- This
usually happens because you expected
find_all()
to return a
single tag or string. But
find_all()
returns a _list_ of tags
and stringsâa
ResultSet
object. You need to iterate over the
list and look at the
.foo
of each one. Or, if you really only
want one result, you need to use
find()
instead of
find_all()
AttributeError:
'NoneType'
object
attribute
'foo'
- This
usually happens because you called
find()
and then tried to
access the
.foo`
attribute of the result. But in your case,
find()
didnât find anything, so it returned
None
, instead of
returning a tag or a string. You need to figure out why your
find()
call isnât returning anything.

### Improving PerformanceÂ¶

Improving Performance

Beautiful Soup will never be as fast as the parsers it sits on top
of. If response time is critical, if youâre paying for computer time
by the hour, or if thereâs any other reason why computer time is more
valuable than programmer time, you should forget about Beautiful Soup
and work directly atoplxml.

Beautiful Soup will never be as fast as the parsers it sits on top
of. If response time is critical, if youâre paying for computer time
by the hour, or if thereâs any other reason why computer time is more
valuable than programmer time, you should forget about Beautiful Soup
and work directly atop
lxml

That said, there are things you can do to speed up Beautiful Soup. If
youâre not using lxml as the underlying parser, my advice is tostart. Beautiful Soup parses documents
significantly faster using lxml than using html.parser or html5lib.

That said, there are things you can do to speed up Beautiful Soup. If
youâre not using lxml as the underlying parser, my advice is to
start
. Beautiful Soup parses documents
significantly faster using lxml than using html.parser or html5lib.

You can speed up encoding detection significantly by installing thecchardetlibrary.

You can speed up encoding detection significantly by installing the
cchardet
library.

Parsing only part of a documentwonât save you much time parsing
the document, but it can save a lot of memory, and itâll makesearchingthe document much faster.

Parsing only part of a document
wonât save you much time parsing
the document, but it can save a lot of memory, and itâll make
searching
the document much faster.

## Translating this documentationÂ¶

Translating this documentation

New translations of the Beautiful Soup documentation are greatly
appreciated. Translations should be licensed under the MIT license,
just like Beautiful Soup and its English documentation are.

New translations of the Beautiful Soup documentation are greatly
appreciated. Translations should be licensed under the MIT license,
just like Beautiful Soup and its English documentation are.

There are two ways of getting your translation into the main code base
and onto the Beautiful Soup website:

There are two ways of getting your translation into the main code base
and onto the Beautiful Soup website:

- Create a branch of the Beautiful Soup repository, add your
translation, and propose a merge with the main branch, the same
as you would do with a proposed change to the source code.
- Send a message to the Beautiful Soup discussion group with a link to
your translation, or attach your translation to the message.

Create a branch of the Beautiful Soup repository, add your
translation, and propose a merge with the main branch, the same
as you would do with a proposed change to the source code.
Send a message to the Beautiful Soup discussion group with a link to
your translation, or attach your translation to the message.

Use the Chinese or Brazilian Portuguese translations as your model. In
particular, please translate the source filedoc/source/index.rst,
rather than the HTML version of the documentation. This makes it
possible to publish the documentation in a variety of formats, not
just HTML.

Use the Chinese or Brazilian Portuguese translations as your model. In
particular, please translate the source file
doc/source/index.rst
,
rather than the HTML version of the documentation. This makes it
possible to publish the documentation in a variety of formats, not
just HTML.

## Beautiful Soup 3Â¶

Beautiful Soup 3

Beautiful Soup 3 is the previous release series, and is no longer
being actively developed. Itâs currently packaged with all major Linux
distributions:

$ apt-get install python-beautifulsoup

$ apt-get install python-beautifulsoup

Itâs also published through PyPi asBeautifulSoup.:

Itâs also published through PyPi as
BeautifulSoup

$ easy_install BeautifulSoup

$ easy_install BeautifulSoup

$ pip install BeautifulSoup

$ pip install BeautifulSoup

You can alsodownload a tarball of Beautiful Soup 3.2.0.

You can also
download a tarball of Beautiful Soup 3.2.0

If you raneasy_installbeautifulsouporeasy_installBeautifulSoup, but your code doesnât work, you installed Beautiful
Soup 3 by mistake. You need to runeasy_installbeautifulsoup4.

If you ran
easy_install
beautifulsoup
easy_install
BeautifulSoup
, but your code doesnât work, you installed Beautiful
Soup 3 by mistake. You need to run
easy_install
beautifulsoup4

The documentation for Beautiful Soup 3 is archived online.

The documentation for Beautiful Soup 3 is archived online

### Porting code to BS4Â¶

Porting code to BS4

Most code written against Beautiful Soup 3 will work against Beautiful
Soup 4 with one simple change. All you should have to do is change the
package name fromBeautifulSouptobs4. So this:

Most code written against Beautiful Soup 3 will work against Beautiful
Soup 4 with one simple change. All you should have to do is change the
package name from
BeautifulSoup
. So this:

```python
from BeautifulSoup import BeautifulSoup

```

from
BeautifulSoup
import
BeautifulSoup

becomes this:

becomes this:

```python
from bs4 import BeautifulSoup

```

from
import
BeautifulSoup

- If you get theImportErrorâNo module named BeautifulSoupâ, your
problem is that youâre trying to run Beautiful Soup 3 code, but you
only have Beautiful Soup 4 installed.
- If you get theImportErrorâNo module named bs4â, your problem
is that youâre trying to run Beautiful Soup 4 code, but you only
have Beautiful Soup 3 installed.

If you get the
ImportError
âNo module named BeautifulSoupâ, your
problem is that youâre trying to run Beautiful Soup 3 code, but you
only have Beautiful Soup 4 installed.
If you get the
ImportError
âNo module named bs4â, your problem
is that youâre trying to run Beautiful Soup 4 code, but you only
have Beautiful Soup 3 installed.

Although BS4 is mostly backwards-compatible with BS3, most of its
methods have been deprecated and given new names forPEP 8 compliance. There are numerous other
renames and changes, and a few of them break backwards compatibility.

Although BS4 is mostly backwards-compatible with BS3, most of its
methods have been deprecated and given new names for
PEP 8 compliance
. There are numerous other
renames and changes, and a few of them break backwards compatibility.

Hereâs what youâll need to know to convert your BS3 code and habits to BS4:

Hereâs what youâll need to know to convert your BS3 code and habits to BS4:

#### You need a parserÂ¶

You need a parser

Beautiful Soup 3 used PythonâsSGMLParser, a module that was
deprecated and removed in Python 3.0. Beautiful Soup 4 useshtml.parserby default, but you can plug in lxml or html5lib and
use that instead. SeeInstalling a parserfor a comparison.

Beautiful Soup 3 used Pythonâs
SGMLParser
, a module that was
deprecated and removed in Python 3.0. Beautiful Soup 4 uses
html.parser
by default, but you can plug in lxml or html5lib and
use that instead. See
Installing a parser
for a comparison.

Sincehtml.parseris not the same parser asSGMLParser, you
may find that Beautiful Soup 4 gives you a different parse tree than
Beautiful Soup 3 for the same markup. If you swap outhtml.parserfor lxml or html5lib, you may find that the parse tree changes yet
again. If this happens, youâll need to update your scraping code to
deal with the new tree.

Since
html.parser
is not the same parser as
SGMLParser
, you
may find that Beautiful Soup 4 gives you a different parse tree than
Beautiful Soup 3 for the same markup. If you swap out
html.parser
for lxml or html5lib, you may find that the parse tree changes yet
again. If this happens, youâll need to update your scraping code to
deal with the new tree.

#### Method namesÂ¶

Method names

- renderContents->encode_contents
- replaceWith->replace_with
- replaceWithChildren->unwrap
- findAll->find_all
- findAllNext->find_all_next
- findAllPrevious->find_all_previous
- findNext->find_next
- findNextSibling->find_next_sibling
- findNextSiblings->find_next_siblings
- findParent->find_parent
- findParents->find_parents
- findPrevious->find_previous
- findPreviousSibling->find_previous_sibling
- findPreviousSiblings->find_previous_siblings
- getText->get_text
- nextSibling->next_sibling
- previousSibling->previous_sibling

renderContents
encode_contents
replaceWith
replace_with
replaceWithChildren
unwrap
findAll
find_all
findParent
find_parent
findParents
find_parents
getText
get_text

Some arguments to the Beautiful Soup constructor were renamed for the
same reasons:

Some arguments to the Beautiful Soup constructor were renamed for the
same reasons:

- BeautifulSoup(parseOnlyThese=...)->BeautifulSoup(parse_only=...)
- BeautifulSoup(fromEncoding=...)->BeautifulSoup(from_encoding=...)

BeautifulSoup(parseOnlyThese=...)
BeautifulSoup(parse_only=...)
BeautifulSoup(fromEncoding=...)
BeautifulSoup(from_encoding=...)

I renamed one method for compatibility with Python 3:

I renamed one method for compatibility with Python 3:

- Tag.has_key()->Tag.has_attr()

Tag.has_key()
Tag.has_attr()

I renamed one attribute to use more accurate terminology:

I renamed one attribute to use more accurate terminology:

- Tag.isSelfClosing->Tag.is_empty_element

Tag.isSelfClosing
Tag.is_empty_element

I renamed three attributes to avoid using words that have special
meaning to Python. Unlike the others, these changes arenot backwards
compatible.If you used these attributes in BS3, your code will break
on BS4 until you change them.

I renamed three attributes to avoid using words that have special
meaning to Python. Unlike the others, these changes are
not backwards
compatible.
If you used these attributes in BS3, your code will break
on BS4 until you change them.

- UnicodeDammit.unicode->UnicodeDammit.unicode_markup
- Tag.next->Tag.next_element
- Tag.previous->Tag.previous_element

UnicodeDammit.unicode
UnicodeDammit.unicode_markup

#### GeneratorsÂ¶

Generators

I gave the generators PEP 8-compliant names, and transformed them into
properties:

I gave the generators PEP 8-compliant names, and transformed them into
properties:

- childGenerator()->children
- nextGenerator()->next_elements
- nextSiblingGenerator()->next_siblings
- previousGenerator()->previous_elements
- previousSiblingGenerator()->previous_siblings
- recursiveChildGenerator()->descendants
- parentGenerator()->parents

childGenerator()
children
recursiveChildGenerator()
descendants
parentGenerator()
parents

So instead of this:

So instead of this:

```python
for parent in tag.parentGenerator():
 ...

```

parent
parentGenerator

You can write this:

You can write this:

```python
for parent in tag.parents:
 ...

```

parent
parents

(But the old code will still work.)

(But the old code will still work.)

Some of the generators used to yieldNoneafter they were done, and
then stop. That was a bug. Now the generators just stop.

Some of the generators used to yield
None
after they were done, and
then stop. That was a bug. Now the generators just stop.

There are two new generators,.strings and
.stripped_strings..stringsyields
NavigableString objects, and.stripped_stringsyields Python
strings that have had whitespace stripped.

There are two new generators,
.strings and
.stripped_strings
.strings
yields
NavigableString objects, and
.stripped_strings
yields Python
strings that have had whitespace stripped.

#### XMLÂ¶

There is no longer aBeautifulStoneSoupclass for parsing XML. To
parse XML you pass in âxmlâ as the second argument to theBeautifulSoupconstructor. For the same reason, theBeautifulSoupconstructor no longer recognizes theisHTMLargument.

There is no longer a
BeautifulStoneSoup
class for parsing XML. To
parse XML you pass in âxmlâ as the second argument to the
BeautifulSoup
constructor. For the same reason, the
BeautifulSoup
constructor no longer recognizes the
isHTML
argument.

Beautiful Soupâs handling of empty-element XML tags has been
improved. Previously when you parsed XML you had to explicitly say
which tags were considered empty-element tags. TheselfClosingTagsargument to the constructor is no longer recognized. Instead,
Beautiful Soup considers any empty tag to be an empty-element tag. If
you add a child to an empty-element tag, it stops being an
empty-element tag.

selfClosingTags
argument to the constructor is no longer recognized. Instead,
Beautiful Soup considers any empty tag to be an empty-element tag. If
you add a child to an empty-element tag, it stops being an
empty-element tag.

#### EntitiesÂ¶

Entities

An incoming HTML or XML entity is always converted into the
corresponding Unicode character. Beautiful Soup 3 had a number of
overlapping ways of dealing with entities, which have been
removed. TheBeautifulSoupconstructor no longer recognizes thesmartQuotesToorconvertEntitiesarguments. (Unicode,
Dammitstill hassmart_quotes_to, but its default is now to turn
smart quotes into Unicode.) The constantsHTML_ENTITIES,XML_ENTITIES, andXHTML_ENTITIEShave been removed, since they
configure a feature (transforming some but not all entities into
Unicode characters) that no longer exists.

An incoming HTML or XML entity is always converted into the
corresponding Unicode character. Beautiful Soup 3 had a number of
overlapping ways of dealing with entities, which have been
removed. The
BeautifulSoup
constructor no longer recognizes the
smartQuotesTo
convertEntities
arguments. (
Unicode,
Dammit
still has
smart_quotes_to
, but its default is now to turn
smart quotes into Unicode.) The constants
HTML_ENTITIES
XML_ENTITIES
, and
XHTML_ENTITIES
have been removed, since they
configure a feature (transforming some but not all entities into
Unicode characters) that no longer exists.

If you want to turn Unicode characters back into HTML entities on
output, rather than turning them into UTF-8 characters, you need to
use anoutput formatter.

If you want to turn Unicode characters back into HTML entities on
output, rather than turning them into UTF-8 characters, you need to
use an
output formatter

#### MiscellaneousÂ¶

Miscellaneous

Tag.stringnow operates recursively. If tag A
contains a single tag B and nothing else, then A.string is the same as
B.string. (Previously, it was None.)

Tag.string

Multi-valued attributeslikeclasshave lists of strings as
their values, not strings. This may affect the way you search by CSS
class.

Multi-valued attributes
like
class
have lists of strings as
their values, not strings. This may affect the way you search by CSS
class.

If you pass one of thefind*methods bothstringanda tag-specific argument likename, Beautiful Soup will
search for tags that match your tag-specific criteria and whoseTag.stringmatches your value forstring. It willnotfind the strings themselves. Previously,
Beautiful Soup ignored the tag-specific arguments and looked for
strings.

If you pass one of the
find*
methods both
string
a tag-specific argument like
name
, Beautiful Soup will
search for tags that match your tag-specific criteria and whose
Tag.string
matches your value for
string
. It will

TheBeautifulSoupconstructor no longer recognizes themarkupMassageargument. Itâs now the parserâs responsibility to
handle markup correctly.

BeautifulSoup
constructor no longer recognizes the
markupMassage
argument. Itâs now the parserâs responsibility to
handle markup correctly.

The rarely-used alternate parser classes likeICantBelieveItsBeautifulSoupandBeautifulSOAPhave been
removed. Itâs now the parserâs decision how to handle ambiguous
markup.

The rarely-used alternate parser classes like
ICantBelieveItsBeautifulSoup
BeautifulSOAP
have been
removed. Itâs now the parserâs decision how to handle ambiguous
markup.

Theprettify()method now returns a Unicode string, not a bytestring.

prettify()
method now returns a Unicode string, not a bytestring.