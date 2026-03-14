# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/StringHelper.md

# [StringHelper](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper)

Helper for string manipulation.

## Functions

Functions are methods available for calling on the class

[capitalize](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-capitalize-static)
Capitalizes the first letter of a string, "myString" -> "MyString".

[uncapitalize](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-uncapitalize-static)
Makes the first letter of a string lowercase, "MyString" -> "myString".

[hyphenate](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-hyphenate-static)
Converts the passed camelCased string to a hyphen-separated string. eg "minWidth" -> "min-width"

[hyphenateAttributeName](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-hyphenateAttributeName-static)
Converts the passed camelCased string to a hyphen-separated attribute name when it has a recognized prefix. Use for e.g. `dataUserId` -> `data-user-id` or `ariaDescribedBy` -> `aria-described-by`.

[separate](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-separate-static)
Converts the passed camelCased string to a capitalized, space-separated string. eg "startDate" -> "Start date".

[createId](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-createId-static)
Creates an alphanumeric identifier from any passed string. Encodes spaces and non-alpha characters.

[escapeRegExp](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-escapeRegExp-static)
Escapes special RegExp characters.

[decodeHtml](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-decodeHtml-static)
This method decodes HTML entities and returns the original HTML.

See also [encodeHtml](https://bryntum.com/docs/gantt/api/#Core/helper/StringHelper#function-encodeHtml-static).

[encodeHtml](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-encodeHtml-static)
This method encodes HTML entities and returns a string that can be placed in the document and produce the original text rather than be interpreted as HTML. Using this method with user-entered values prevents those values from executing as HTML (i.e., a cross-site scripting or "XSS" security issue).

See also [decodeHtml](https://bryntum.com/docs/gantt/api/#Core/helper/StringHelper#function-decodeHtml-static).

[encodeHtmlBR](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-encodeHtmlBR-static)
This method is similar to [encodeHtml](https://bryntum.com/docs/gantt/api/#Core/helper/StringHelper#function-encodeHtml-static) except that `\n` and `\r` characters in the given `str` are replaced by `<br>` tags _after_ first being encoded by [encodeHtml](https://bryntum.com/docs/gantt/api/#Core/helper/StringHelper#function-encodeHtml-static).

[isHtml](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-isHtml-static)
Returns `true` if the provided `text` contains special HTML characters.

[initHtmlEntities](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-initHtmlEntities-static)
Initializes HTML entities used by [encodeHtml](https://bryntum.com/docs/gantt/api/#Core/helper/StringHelper#function-encodeHtml-static) and [decodeHtml](https://bryntum.com/docs/gantt/api/#Core/helper/StringHelper#function-decodeHtml-static).

[parseMarkdown](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-parseMarkdown-static)
Parses Markdown text into a structured format

[stripDiacritics](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-stripDiacritics-static)
Converts letters with diacritics to their base letter equivalents. For example, "Ångström" becomes "Angstrom".

[stripHtmlTags](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-stripHtmlTags-static)
Removes all HTML tags from the passed string and decodes HTML entities.

[safeJsonParse](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-safeJsonParse-static)
Parses JSON inside a try-catch block. Returns null if the string could not be parsed.

[safeJsonStringify](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-safeJsonStringify-static)
Stringifies an object inside a try-catch block. Returns null if an exception is encountered.

See [JSON.stringify on MDN](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) for more information on the arguments.

[joinPaths](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-joinPaths-static)
Joins all given paths together using the separator as a delimiter and normalizes the resulting path.

[split](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-split-static)
Returns the provided string split on whitespace. If the string is empty or consists of only whitespace, the returned array will be empty. If `str` is not a string, it is simply returned. This allows `null` or already split strings (arrays) to be passed through.

For example:

```
 console.log(StringHelper.split(' abc def xyz   '));
 > ['abc', 'def', 'xyz']
 console.log(StringHelper.split(''));
 > []
```

Compare to the standard `split()` method:

```
 console.log(' abc def xyz   '.split(/\s+/));
 > ['', 'abc', 'def', 'xyz', '']
 console.log(''.split(/\s+/));
 > ['']
```

[xss](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-xss-static)
This is a tagged template function that performs HTML encoding on replacement values to avoid XSS (Cross-Site Scripting) attacks.

For example:

```
 eventRenderer(eventRecord) {
     return StringHelper.xss`<span class="${eventRecord.attrib}">${eventRecord.name}</span>`;
 }
```

[xssBR](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-xssBR-static)
This is a tagged template function that performs HTML encoding on replacement values to avoid XSS (Cross-Site Scripting) attacks. Unlike [xss](https://bryntum.com/docs/gantt/api/#Core/helper/StringHelper#function-xss-static), this method converts `\n` and `\r` characters into `<br>` tags.

For example:

```
 eventRenderer(eventRecord) {
     return StringHelper.xssBR`<span class="${eventRecord.attrib}">${eventRecord.name}</span>`;
 }
```

See [encodeHtmlBR](https://bryntum.com/docs/gantt/api/#Core/helper/StringHelper#function-encodeHtmlBR-static).

[toJavaScriptValue](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-toJavaScriptValue-static)
Converts a value to a JavaScript string (not JSON).

For example a date to `"new Date(y, m, d)"`, an array to `"[...]"` etc.

[toJavaScriptString](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-toJavaScriptString-static)
Converts an object into a JavaScript string (not JSON).

For example `{ a: 1, b: [2, 3] }` -> `"'{ a: 1, b: [2, 3] }'"`

[encodeAttributeSelector](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-encodeAttributeSelector-static)
Escapes " and \\ in CSS attribute selectors, e.g. \[data-id="somevalue"\]

Usage:

```
document.querySelector(StringHelper.cssAttributeQuery('data-id', 'id with & \\ chars'))
```

[generateUUID](https://bryntum.com/docs/gantt/api/Core/helper/StringHelper#function-generateUUID-static)
Generates a UUID. Uses `Crypto.randomUUID()` if available, otherwise generates a random UUID using `Crypto.getRandomValues()`.
