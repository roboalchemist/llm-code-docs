# Package org.jsoup.helper

---

@NullMarked
package org.jsoup.helper

Package containing classes supporting the core jsoup code.

- 

Related Packages

Package
Description
org.jsoup

Contains the main `Jsoup` class, which provides convenient static access to the jsoup functionality.

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
DataUtil

Internal static utilities for handling data.

HttpConnection

Implementation of `Connection`.

HttpConnection.KeyVal
 
HttpConnection.Request
 
HttpConnection.Response
 
Regex

A regular expression abstraction.

Regex.Matcher
 
RequestAuthenticator

A `RequestAuthenticator` is used in `Connection` to authenticate if required to proxies and web
 servers.

RequestAuthenticator.Context

Provides details for the request, to determine the appropriate credentials to return.

Validate

Validators to check that method arguments meet expectations.

ValidationException

Validation exceptions, as thrown by the methods in `Validate`.

W3CDom

Helper class to transform a `Document` to a `org.w3c.dom.Document`,
 for integration with toolsets that use the W3C DOM.

W3CDom.W3CBuilder

Implements the conversion by walking the input.