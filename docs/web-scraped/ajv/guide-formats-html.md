# Source: https://ajv.js.org/guide/formats.html

Title: Ajv JSON schema validator

URL Source: https://ajv.js.org/guide/formats.html

Markdown Content:
[#](https://ajv.js.org/guide/formats.html#format-validation) Format validation
------------------------------------------------------------------------------

[#](https://ajv.js.org/guide/formats.html#string-formats) String formats
------------------------------------------------------------------------

From version 7 Ajv does not include formats defined by JSON Schema specification - these and several other formats are provided by [ajv-formats(opens new window)](https://github.com/ajv-validator/ajv-formats) plugin.

To add all formats from this plugin:

See [ajv-formats(opens new window)](https://github.com/ajv-validator/ajv-formats) documentation for further details.

It is recommended NOT to use "format" keyword implementations with untrusted data, as they may use potentially unsafe regular expressions (even though known issues are fixed) - see [ReDoS attack](https://ajv.js.org/security.html#redos-attack).

Format validation of untrusted data

If you need to use "format" keyword to validate untrusted data, you MUST assess their suitability and safety for your validation scenarios.

The following formats are defined in [ajv-formats(opens new window)](https://github.com/ajv-validator/ajv-formats) for string validation with "format" keyword:

*   _date_: full-date according to [RFC3339(opens new window)](http://tools.ietf.org/html/rfc3339#section-5.6).
*   _time_: time with optional time-zone.
*   _date-time_: date-time from the same source (time-zone is mandatory).
*   _duration_: duration from [RFC3339(opens new window)](https://tools.ietf.org/html/rfc3339#appendix-A)
*   _uri_: full URI.
*   _uri-reference_: URI reference, including full and relative URIs.
*   _uri-template_: URI template according to [RFC6570(opens new window)](https://datatracker.ietf.org/doc/rfc6570/)
*   _url_ (deprecated): [URL record(opens new window)](https://url.spec.whatwg.org/#concept-url).
*   _email_: email address.
*   _hostname_: host name according to [RFC1034(opens new window)](http://tools.ietf.org/html/rfc1034#section-3.5).
*   _ipv4_: IP address v4.
*   _ipv6_: IP address v6.
*   _regex_: tests whether a string is a valid regular expression by passing it to RegExp constructor.
*   _uuid_: Universally Unique Identifier according to [RFC4122(opens new window)](https://datatracker.ietf.org/doc/rfc4122/).
*   _json-pointer_: JSON-pointer according to [RFC6901(opens new window)](https://datatracker.ietf.org/doc/rfc6901/).
*   _relative-json-pointer_: relative JSON-pointer according to [this draft(opens new window)](http://tools.ietf.org/html/draft-luff-relative-json-pointer-00).

Additional formats in ajv-formats-draft2019

JSON Schema draft-07 also defines formats `iri`, `iri-reference`, `idn-hostname` and `idn-email` for URLs, hostnames and emails with international characters. These formats are available in [ajv-formats-draft2019(opens new window)](https://github.com/luzlab/ajv-formats-draft2019) plugin.

[#](https://ajv.js.org/guide/formats.html#user-defined-formats) User-defined formats
------------------------------------------------------------------------------------

You can add and replace any formats using [addFormat](https://ajv.js.org/api.html#ajv-addformat-name-string-format-format-ajv) method:

Ajv also allows defining the formats that would be applied to numbers only:

[#](https://ajv.js.org/guide/formats.html#formats-and-standalone-validation-code) Formats and standalone validation code
------------------------------------------------------------------------------------------------------------------------

If you use formats from [ajv-formats(opens new window)](https://github.com/ajv-validator/ajv-formats) package, [standalone validation code](https://ajv.js.org/standalone) will be supported out of the box.

Standalone code and Ajv versions

You need to make sure that ajv-formats imports the same version and the same code of ajv as the one you use in your application for standalone validation code to work (because of `instanceof` check that is currently used).

`npm` and other package managers may not update the version of ajv dependency of ajv-formats when you update version of ajv in your application - the workaround is to use clean npm installation.

If you define your own formats, for standalone code generation to work you need to pass the code snippet that evaluates to an object with all defined formats to the option `code.formats`:
