# Selectors

When you’re scraping web pages, the most common task you need to perform is
to extract data from the HTML source. There are several libraries available to
achieve this, such as:

- 

BeautifulSoup [https://www.crummy.com/software/BeautifulSoup/] is a very popular web scraping library among Python
programmers which constructs a Python object based on the structure of the
HTML code and also deals with bad markup reasonably well, but it has one
drawback: it’s slow.

- 

lxml [https://lxml.de/] is an XML parsing library (which also parses HTML) with a pythonic
API based on `ElementTree` [https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree]. (lxml is not part of the Python
standard library.)

Scrapy comes with its own mechanism for extracting data. They’re called
selectors because they “select” certain parts of the HTML document specified
either by XPath [https://www.w3.org/TR/xpath/all/] or CSS [https://www.w3.org/TR/selectors] expressions.

XPath [https://www.w3.org/TR/xpath/all/] is a language for selecting nodes in XML documents, which can also be
used with HTML. CSS [https://www.w3.org/TR/selectors] is a language for applying styles to HTML documents. It
defines selectors to associate those styles with specific HTML elements.

Note

Scrapy Selectors is a thin wrapper around parsel [https://parsel.readthedocs.io/en/latest/] library; the purpose of
this wrapper is to provide better integration with Scrapy Response objects.

parsel [https://parsel.readthedocs.io/en/latest/] is a stand-alone web scraping library which can be used without
Scrapy. It uses lxml [https://lxml.de/] library under the hood, and implements an
easy API on top of lxml API. It means Scrapy selectors are very similar
in speed and parsing accuracy to lxml.