# Source: https://swagger.io/docs/specification/serialization/

# Parameter Serialization
Note

OAS3This guide is for OpenAPI 3.0.

Serialization means translating data structures or object state into a format that can be transmitted and reconstructed later. OpenAPI 3.0 supports arrays and objects inoperation parameters(path, query, header, and cookie) and lets you specify how these parameters should be serialized. The serialization method is defined by thestyleandexplodekeywords:

[operation parameters](/docs/specification/describing-parameters/) `style` `explode` - styledefines how multiple values are delimited. Possible styles depend on the parameter location –path,query,headerorcookie.
`style` [path](#path-parameters) [query](#query-parameters) [header](#header-parameters) [cookie](#cookie-parameters) - explode(true/false) specifies whether arrays and objects should generate separate parameters for each array item or object property.
`explode` OpenAPI serialization rules are based on a subset of URI template patterns defined byRFC 6570. Tool implementers can use existing URI template libraries to handle the serialization, as explainedbelow.

[RFC 6570](https://tools.ietf.org/html/rfc6570) [below](#serialization-and-rfc-6570) ### Path Parameters
Path parameters support the followingstylevalues:

`style` - simple– (default) comma-separated values. Corresponds to the{param_name}URI template.
`{param_name}` - label– dot-prefixed values, also known as label expansion. Corresponds to the{.param_name}URI template.
`{.param_name}` - matrix– semicolon-prefixed values, also known as path-style expansion. Corresponds to the{;param_name}URI template.
`{;param_name}` The default serialization method isstyle: simpleandexplode: false. Given the path/users/{id}, the path parameteridis serialized as follows:

`style: simple` `explode: false` `/users/{id}` `id` - Default serialization method
Thelabelandmatrixstyles are sometimes used with partial path parameters, such as/users{id}, because the parameter values get prefixed.

`label` `matrix` `/users{id}` ### Query Parameters
Query parameters support the followingstylevalues:

`style` - form– (default) ampersand-separated values, also known as form-style query expansion. Corresponds to the{?param_name}URI template.
`{?param_name}` - spaceDelimited– space-separated array values. Same ascollectionFormat: ssvin OpenAPI 2.0. Has effect only for non-exploded arrays (explode: false), that is, the space separates the array values if the array is asingle parameter, as inarr=a b c.
`collectionFormat: ssv` `explode: false` `arr=a b c` - pipeDelimited– pipeline-separated array values. Same ascollectionFormat: pipesin OpenAPI 2.0. Has effect only for non-exploded arrays (explode: false), that is, the pipe separates the array values if the array is asingle parameter, as inarr=a|b|c.
`collectionFormat: pipes` `explode: false` `arr=a|b|c` - deepObject– simple non-nested objects are serialized asparamName[prop1]=value1&paramName[prop2]=value2&.... The behavior for nested objects and arrays is undefined.
`paramName[prop1]=value1&paramName[prop2]=value2&...` The default serialization method isstyle: formandexplode: true. This corresponds tocollectionFormat: multifrom OpenAPI 2.0. Given the path/userswith a query parameterid, the query string is serialized as follows:

`style: form` `explode: true` `collectionFormat: multi` `/users` `id` * Default serialization method

Additionally, theallowReservedkeyword specifies whether the reserved characters:/?#[]@!$&'()*+,;=in parameter values are allowed to be sent as they are, or should be percent-encoded. By default,allowReservedisfalse, and reserved characters are percent-encoded. For example,/is encoded as%2F(or%2f), so that the parameter valuequotes/h2g2.txtwill be sent asquotes%2Fh2g2.txt.

`allowReserved` `:/?#[]@!$&'()*+,;=` `allowReserved` `false` `/` `%2F` `%2f` `quotes/h2g2.txt` `quotes%2Fh2g2.txt` ### Header Parameters
Header parameters always use thesimplestyle, that is, comma-separated values. This corresponds to the{param_name}URI template. An optionalexplodekeyword controls the object serialization. Given the request header namedX-MyHeader, the header value is serialized as follows:

`simple` `{param_name}` `explode` `X-MyHeader` - Default serialization method
### Cookie Parameters
Cookie parameters always use theformstyle. An optionalexplodekeyword controls the array and object serialization. Given the cookie namedid, the cookie value is serialized as follows:

`form` `explode` `id` - Default serialization method
### Serialization and RFC 6570
OpenAPI serialization rules are based on a subset of URI templates defined byRFC 6570. Tool implementers can use existing URI template libraries to handle the serialization. You will need to construct the URI template based on the path and parameter definitions. The following table shows how OpenAPI keywords are mapped to the URI Template modifiers.

[RFC 6570](https://tools.ietf.org/html/rfc6570) `style: simple` `style: label` `.` `style: matrix` `;` `style: form` `?` `&` `style: pipeDelimited` `?` `&` `|` `,` `style: spaceDelimited` `?` `&` `,` `explode: false` `explode: true` `*` `allowReserved: false` `allowReserved: true` `+` For example, consider the path/users{id}with a query parametermetadata, defined like so:

`/users{id}` `metadata` ```
1paths:2  # /users;id=3;id=4?metadata=true3  /users{id}:4    get:5      parameters:6        - in: path7          name: id8          required: true9          schema:10            type: array11            items:12              type: integer13            minItems: 114          style: matrix15          explode: true16        - in: query17          name: metadata18          schema:19            type: boolean20          # Using the default serialization for query parameters:21          # style=form, explode=false, allowReserved=false22      responses:23        '200':24          description: A list of users```

The path parameteriduses thematrixstyle with theexplodemodifier, which corresponds to the{;id*}template. The query parametermetadatauses the defaultformstyle, which corresponds to the{?metadata}template. The complete URI template would look like:

`id` `matrix` `explode` `{;id*}` `metadata` `form` `{?metadata}` ```
1/users{;id*}{?metadata}```

`1/users{;id*}{?metadata}` A client application can then use an URI template library to generate the request URL based on this template and specific parameter values.

### Other Serialization Methods
styleandexplodecover the most common serialization methods, but not all. For more complex scenarios (for example, a JSON-formatted object in the query string), you can use thecontentkeyword and specify the media type that defines the serialization format. For more information, seeschema vs content.

`style` `explode` `content` [schema vs content](/docs/specification/describing-parameters/#schema-vs-content) Did not find what you were looking for?Ask the communityFound a mistake?Let us know

[Ask the community](https://community.smartbear.com/t5/Swagger-Open-Source-Tools/bd-p/SwaggerOSTools) [Let us know](https://github.com/swagger-api/swagger.io/issues)