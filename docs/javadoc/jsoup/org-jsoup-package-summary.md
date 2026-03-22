# Package org.jsoup

---

@NullMarked
package org.jsoup

Contains the main `Jsoup` class, which provides convenient static access to the jsoup functionality.

- 

Related Packages

Package
Description
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

- 

Class
Description
Connection

The Connection interface is a convenient HTTP client and session object to fetch content from the web, and parse them
 into Documents.

Connection.Base<T extends Connection.Base<T>>

Common methods for Requests and Responses

Connection.KeyVal

A Key:Value tuple(+), used for form data.

Connection.Method

GET and POST http methods.

Connection.Request

Represents a HTTP request.

Connection.Response

Represents a HTTP response.

HttpStatusException

Signals that a HTTP request resulted in a not OK HTTP response.

Jsoup

The core public access point to the jsoup functionality.

Progress<ProgressContext>
 
SerializationException

A SerializationException is raised whenever serialization of a DOM element fails.

UnsupportedMimeTypeException

Signals that a HTTP response returned a mime type that is not supported.