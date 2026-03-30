# jsoup Java HTML Parser 1.22.1 API

# jsoup: Java HTML parser that makes sense of real-world HTML soup.

**jsoup** is a Java library for working with real-world HTML. It provides a very convenient API for fetching URLs
  and extracting and manipulating data, using the best of HTML5 DOM methods and CSS selectors.

jsoup implements the WHATWG HTML specification, and parses HTML to the same DOM
  as modern browsers do.

  
- parse HTML from a URL, file, or string
  
- find and extract data, using DOM traversal or CSS selectors
  
- manipulate the HTML elements, attributes, and text
  
- clean user-submitted content against a safelist, to prevent XSS
  
- output tidy HTML

jsoup is designed to deal with all varieties of HTML found in the wild; from pristine and validating,
  to invalid tag-soup; jsoup will create a sensible parse tree.

See **jsoup.org** for downloads, documentation, and examples.

Packages

Package
Description
org.jsoup

Contains the main `Jsoup` class, which provides convenient static access to the jsoup functionality.

org.jsoup.helper

Package containing classes supporting the core jsoup code.

org.jsoup.nodes

HTML document structure nodes.

org.jsoup.parser

Contains the HTML parser, tag specifications, and HTML tokeniser.

org.jsoup.safety

Contains the jsoup HTML cleaner, and safelist definitions.

org.jsoup.select

Packages to support the CSS-style element selector.