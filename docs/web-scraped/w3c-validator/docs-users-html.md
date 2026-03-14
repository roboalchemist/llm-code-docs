# Source: https://validator.w3.org/docs/users.html

Title: User Documentation for The W3C Markup Validator

URL Source: https://validator.w3.org/docs/users.html

Markdown Content:
The W3C Markup Validator provides Perl/CGI/SGML/XML/DTD-based validation of a variety of document types. SGML and DTDs are older technologies that never found wide use on the Web, so for checking of HTML documents using modern technologies, you probably want to instead use the [W3C HTML Checker](https://validator.w3.org/nu/). To do that,

![Image 1: HTML5](https://validator.w3.org/images/HTML5_Badge_32.png)

*   Download the [latest release version](https://github.com/validator/validator/releases/latest).
*   Read the [usage guide](http://validator.github.io/validator/).

If for some reason rather than using the W3C HTML Checker, you want to use the W3C Markup Validator, this page provides the following information:

*   [Running your own instance of the W3C Markup Validator](https://validator.w3.org/docs/users.html#Installing)
*   [Using the W3C Markup Validator API](https://validator.w3.org/docs/users.html#Calling)
*   [Controlling the behavior of the W3C Markup Validator](https://validator.w3.org/docs/users.html#Options)
*   [Using HTTP headers to check validation results](https://validator.w3.org/docs/api.html#http_headers)

### Controlling the behavior of the W3C Markup Validator

This section describes the behavior of each of the options exposed in the W3C Markup Validator user interface, and names of the corresponding query parameters (shown in parentheses) you can use with the W3C Markup Validator API.

[](https://validator.w3.org/docs/users.html)Encoding (`charset`)
This allows you to **override** the character encoding information about your document. You may use this option for test purposes, but you will eventually have to serve your document with the correct character encoding, or the validator will [complain](https://validator.w3.org/docs/help#faq-charset) about it and you document will not be valid.

[](https://validator.w3.org/docs/users.html)Use Fallback instead of Override (`fbc`)
Uses the [character encoding override](https://validator.w3.org/docs/users.html#option-charset) mechanism described above, but only does it as a fall back mechanism if the actual document is not served with character encoding information. Think of this as a gentler override mechanism.

[](https://validator.w3.org/docs/users.html)Document Type (`doctype`)
This allows you to **override** the DOCTYPE declaration for your document. You may use this option for test purposes, but you will eventually have to serve your document with the correct DOCTYPE declaration, or the validator will [complain](https://validator.w3.org/docs/help#faq-doctype) about it and you document will not be valid.

[](https://validator.w3.org/docs/users.html)Use Fallback instead of Override (`fbd`)
Uses the [Doctype override](https://validator.w3.org/docs/users.html#option-doctype) mechanism described above, but only does it as a fall back mechanism if the actual document does not have a Doctype declaration. Think of this as a gentler override mechanism.

[](https://validator.w3.org/docs/users.html)Show Source (`ss`)
Displays the HTML source of the document you validated and links error messages directly to lines in this output. Makes it easy to see what's wrong.

[](https://validator.w3.org/docs/users.html)Show Outline (`outline`)
Will generate an outline of your document from the H1 - H6 elements. For a properly formed document, this will be a nicely nested tree structure. The visualization of your document's structure makes it easier to see where you've skipped a heading.

If you want to examine the semantic structure of your documents, beyond the outline, try the [Semantic data extractor](http://www.w3.org/2003/12/semantic-extractor.html).

[](https://validator.w3.org/docs/users.html)Validate error pages (`No200`)
The W3C Markup Validator will usually tell you if the page you tried to validate could not be retrieved (for example, if the server gave a "404 not found" message. In some circumstances you may want to be able to validate the error page sent by the server. This is the option to use then.

[](https://validator.w3.org/docs/users.html)Verbose Output (`verbose`)
This option triggers verbose output. Verbose output adds more explanations and suggestions to the validation results, and gives more information on the resource validated. This makes it a useful option if you prefer to be given as much help as possible; if you prefer more concise reports, leave this option unset.

For Content-Negotiated resources, set a specific `Accept` Header (`accept`)
This option (_experimental, as of 0.8.2_) is useful if your Web server is set up to use format negotiation, serving different content based on the preferred/accepted media types of the user agent. The validator can then emulate different HTTP `Accept` behaviors.

For example, append "`accept=application%2Fxhtml%2Bxml%2C*`" and the validator will send the HTTP Header "`Accept: application/xhtml+xml,*`".

For Content-Negotiated resources, set a specific `Accept-Language` Header (`accept-language`)
This option (_experimental, as of 0.8.2_) is useful if your Web server is set up to use language negotiation, serving content in different languages based on the preferred/accepted language setup of the user agent. The validator can then emulate different HTTP `Accept-Language` behaviors.

For example, append "`accept-language=ja%2Cfr`" and the validator will send the HTTP Header "`Accept-Language: ja,fr`".

Set a specific `Accept-Charset` Header (`accept-charset`)
This option (_experimental, as of 0.8.3_) makes the validator send an `Accept-Charset` HTTP header, specifying the character encodings which it will accept from server. This option is mainly used to interface the W3C Markup Validator for [Mobile Web Best Practices](http://www.w3.org/TR/mobileOK-basic10-tests/#http_request) checking.

Set a specific `User-Agent` Header (`user-agent`)
This option (_experimental, as of 0.8.3_) makes the validator send a custom `User-Agent` HTTP header instead of the usual `W3C_Validator/xx.xxxx`. If the value of this parameter is `mobileok`, the validator will output a `User-Agent` string as defined by the [Mobile Web Best Practices](http://www.w3.org/TR/mobileOK-basic10-tests/#http_request) spec.
