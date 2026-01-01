# Source: https://swagger.io/docs/specification/describing-parameters/

# Describing Parameters
Note

OAS3This page is about OpenAPI 3.0. If you use OpenAPI 2.0, see ourOpenAPI 2.0 guide.

[OpenAPI 2.0 guide](/docs/specification/v2_0/describing-parameters/) In OpenAPI 3.0, parameters are defined in theparameterssection of an operation or path. To describe a parameter, you specify itsname, location (in), data type (defined by eitherschemaorcontent) and other attributes, such asdescriptionorrequired. Here is an example:

`parameters` `name` `in` `schema` `content` `description` `required` ```
1paths:2  /users/{userId}:3    get:4      summary: Get a user by ID5      parameters:6        - in: path7          name: userId8          schema:9            type: integer10          required: true11          description: Numeric ID of the user to get```

Note thatparametersis an array, so, in YAML, each parameter definition must be listed with a dash (-) in front of it.

`parameters` `-` ### Parameter Types
OpenAPI 3.0 distinguishes between the following parameter types based on the parameter location. The location is determined by the parameter’sinkey, for example,in: queryorin: path.

`in` `in: query` `in: path` - path parameters, such as/users/{id}
[path parameters](#path-parameters) `/users/{id}` - query parameters, such as/users?role=admin
[query parameters](#query-parameters) `/users?role=admin` - header parameters, such asX-MyHeader: Value
[header parameters](#header-parameters) `X-MyHeader: Value` - cookie parameters, which are passed in theCookieheader, such asCookie: debug=0; csrftoken=BUSe35dohU3O1MZvDCU
[cookie parameters](#cookie-parameters) `Cookie` `Cookie: debug=0; csrftoken=BUSe35dohU3O1MZvDCU` ### Path Parameters
Path parameters are variable parts of a URL path. They are typically used to point to a specific resource within a collection, such as a user identified by ID. A URL can have several path parameters, each denoted with curly braces{ }.

`{ }` ```
1GET /users/{id}2GET /cars/{carId}/drivers/{driverId}3GET /report.{format}```

`1GET /users/{id}2GET /cars/{carId}/drivers/{driverId}3GET /report.{format}` Each path parameter must be substituted with an actual value when the client makes an API call. In OpenAPI, a path parameter is defined usingin: path. The parameter name must be the same as specified in the path. Also remember to addrequired: true, because path parameters are always required. For example, the/users/{id}endpoint would be described as:

`in: path` `required: true` `/users/{id}` ```
1paths:2  /users/{id}:3    get:4      parameters:5        - in: path6          name: id # Note the name is the same as in the path7          required: true8          schema:9            type: integer10            minimum: 111          description: The user ID```

Path parameters containing arrays and objects can be serialized in different ways:

- path-style expansion (matrix) – semicolon-prefixed, such as/map/point;x=50;y=20
`/map/point;x=50;y=20` - label expansion – dot-prefixed, such as/color.R=100.G=200.B=150
`/color.R=100.G=200.B=150` - simple-style – comma-delimited, such as/users/12,34,56
`/users/12,34,56` The serialization method is specified by thestyleandexplodekeywords. To learn more, seeParameter Serialization.

`style` `explode` [Parameter Serialization](/docs/specification/serialization/) ### Query Parameters
Query parameters are the most common type of parameters. They appear at the end of the request URL after a question mark (?), with differentname=valuepairs separated by ampersands (&). Query parameters can be required and optional.

`?` `name=value` `&` ```
1GET /pets/findByStatus?status=available2GET /notes?offset=100&limit=50```

`1GET /pets/findByStatus?status=available2GET /notes?offset=100&limit=50` Usein: queryto denote query parameters:

`in: query` ```
1parameters:2  - in: query3    name: offset4    schema:5      type: integer6    description: The number of items to skip before starting to collect the result set7  - in: query8    name: limit9    schema:10      type: integer11    description: The numbers of items to return```

Note:To describe API keys passed as query parameters, usesecuritySchemesandsecurityinstead. SeeAPI Keys.

`securitySchemes` `security` [API Keys](/docs/specification/authentication/api-keys/) Query parameters can be primitive values, arrays and objects. OpenAPI 3.0 provides several ways to serialize objects and arrays in the query string.

Arrays can be serialized as:

- form–/products?color=blue,green,redor/products?color=blue&color=green, depending on theexplodekeyword
`form` `/products?color=blue,green,red` `/products?color=blue&color=green` `explode` - spaceDelimited(same ascollectionFormat: ssvin OpenAPI 2.0) –/products?color=blue%20green%20red
`spaceDelimited` `collectionFormat: ssv` `/products?color=blue%20green%20red` - pipeDelimited(same ascollectionFormat: pipesin OpenAPI 2.0) –/products?color=blue|green|red
`pipeDelimited` `collectionFormat: pipes` `/products?color=blue|green|red` Objects can be serialized as:

- form–/points?color=R,100,G,200,B,150or/points?R=100&G=200&B=150, depending on theexplodekeyword
`form` `/points?color=R,100,G,200,B,150` `/points?R=100&G=200&B=150` `explode` - deepObject–/points?color[R]=100&color[G]=200&color[B]=150
`deepObject` `/points?color[R]=100&color[G]=200&color[B]=150` The serialization method is specified by thestyleandexplodekeywords. To learn more, seeParameter Serialization.

`style` `explode` [Parameter Serialization](/docs/specification/serialization/) #### Reserved Characters in Query Parameters
RFC 3986defines a set of reserved characters:/?#[]@!$&'()*+,;=that are used as URI component delimiters. When these characters need to be used literally in a query parameter value, they are usually percent-encoded. For example,/is encoded as%2F(or%2f), so that the parameter valuequotes/h2g2.txtwould be sent as

[RFC 3986](https://tools.ietf.org/html/rfc3986#section-2.2) `:/?#[]@!$&'()*+,;=` `/` `%2F` `%2f` `quotes/h2g2.txt` ```
1GET /file?path=quotes%2Fh2g2.txt```

`1GET /file?path=quotes%2Fh2g2.txt` If you want a query parameter that is not percent-encoded, addallowReserved: trueto the parameter definition:

`allowReserved: true` ```
1parameters:2  - in: query3    name: path4    required: true5    schema:6      type: string7    allowReserved: true # <-----```

`1parameters:2-in:query3name:path4required:true5schema:6type:string7allowReserved:true# <-----` In this case, the parameter value would be sent like so:

```
1GET /file?path=quotes/h2g2.txt```

`1GET /file?path=quotes/h2g2.txt` ### Header Parameters
An API call may require that custom headers be sent with an HTTP request. OpenAPI lets you define custom request headers asin: headerparameters. For example, suppose, a call toGET /pingrequires theX-Request-IDheader:

`in: header` `GET /ping` `X-Request-ID` ```
1    GET /ping HTTP/1.12    Host: example.com3    X-Request-ID: 77e1c83b-7bb0-437b-bc50-a7a58e5660ac```

`1GET /ping HTTP/1.12Host:example.com3X-Request-ID:77e1c83b-7bb0-437b-bc50-a7a58e5660ac` Using OpenAPI 3.0, you would define this operation as follows:

```
1paths:2  /ping:3    get:4      summary: Checks if the server is alive5      parameters:6        - in: header7          name: X-Request-ID8          schema:9            type: string10            format: uuid11          required: true```

In a similar way, you can definecustom response headers. Header parameter can be primitives, arrays and objects. Arrays and objects are serialized using thesimplestyle. For more information, seeParameter Serialization.

[custom response headers](/docs/specification/describing-responses/#response-headers) `simple` [Parameter Serialization](/docs/specification/serialization/) Note:Header parameters namedAccept,Content-TypeandAuthorizationare not allowed. To describe these headers, use the corresponding OpenAPI keywords:

`Accept` `Content-Type` `Authorization` `Content-Type` `requestBody.content.<media-type>` `responses.<code>.content.<media-type>` [Describing Request Body](/docs/specification/describing-request-body/describing-request-body/) [Describing Responses](/docs/specification/describing-responses/) [Media Types](/docs/specification/media-types) `Accept` `responses.<code>.content.<media-type>` [Describing Responses](/docs/specification/describing-responses/) [Media Types](/docs/specification/media-types) `Authorization` `securitySchemes` `security` [Authentication](/docs/specification/authentication/) ### Cookie Parameters
Operations can also pass parameters in theCookieheader, asCookie: name=value. Multiple cookie parameters are sent in the same header, separated by a semicolon and space.

`Cookie` `Cookie: name=value` ```
1GET /api/users2Host: example.com3Cookie: debug=0; csrftoken=BUSe35dohU3O1MZvDCUOJ```

`1GET /api/users2Host:example.com3Cookie:debug=0; csrftoken=BUSe35dohU3O1MZvDCUOJ` Usein: cookieto define cookie parameters:

`in: cookie` ```
1parameters:2  - in: cookie3    name: debug4    schema:5      type: integer6      enum: [0, 1]7      default: 08  - in: cookie9    name: csrftoken10    schema:11      type: string```

Cookie parameters can be primitive values, arrays and objects. Arrays and objects are serialized using theformstyle. For more information, seeParameter Serialization.

`form` [Parameter Serialization](/docs/specification/serialization/) Note:To define cookie authentication, useAPI keysinstead.

[API keys](/docs/specification/authentication/api-keys/) ### Required and Optional Parameters
By default, OpenAPI treats all request parameters as optional. You can addrequired: trueto mark a parameter as required. Note that path parameters must haverequired: true, because they are always required.

`required: true` `required: true` ```
1parameters:2  - in: path3    name: userId4    schema:5      type: integer6    required: true # <----------7    description: Numeric ID of the user to get.```

### schema vs content
To describe the parameter contents, you can use either theschemaorcontentkeyword. They are mutually exclusive and used in different scenarios. In most cases, you would useschema. It lets you describe primitive values, as well as simple arrays and objects serialized into a string. The serialization method for array and object parameters is defined by thestyleandexplodekeywords used in that parameter.

`schema` `content` `schema` `style` `explode` ```
1parameters:2  - in: query3    name: color4    schema:5      type: array6      items:7        type: string8
9    # Serialize as color=blue,black,brown (default)10    style: form11    explode: false```

contentis used in complex serialization scenarios that are not covered bystyleandexplode. For example, if you need to send a JSON string in the query string like so:

`content` `style` `explode` ```
1filter={"type":"t-shirt","color":"blue"}```

`1filter={"type":"t-shirt","color":"blue"}` In this case, you need to wrap the parameterschemaintocontent/<media-type>as shown below. Theschemadefines the parameter data structure, and the media type (in this example –application/json) serves as a reference to an external specification that describes the serialization format.

`schema` `content/<media-type>` `schema` `application/json` ```
1parameters:2  - in: query3    name: filter4
5    # Wrap 'schema' into 'content.<media-type>'6    content:7      application/json: # <---- media type indicates how to serialize / deserialize the parameter content8        schema:9          type: object10          properties:11            type:12              type: string13            color:14              type: string```

Note for Swagger UI and Swagger Editor users:Parameters withcontentare supported in Swagger UI 3.23.7+ and Swagger Editor 3.6.34+.

`content` ### Default Parameter Values
Use thedefaultkeyword in the parameter schema to specify the default value for an optional parameter. The default value is the one that the server uses if the client does not supply the parameter value in the request. The value type must be the same as the parameter’s data type. A typical example is paging parameters such asoffsetandlimit:

`default` `offset` `limit` ```
1GET /users2GET /users?offset=30&limit=10```

`1GET /users2GET /users?offset=30&limit=10` Assumingoffsetdefaults to 0 andlimitdefaults to 20 and ranges from 0 to 100, you would define these parameters as:

`offset` `limit` ```
1parameters:2  - in: query3    name: offset4    schema:5      type: integer6      minimum: 07      default: 08    required: false9    description: The number of items to skip before starting to collect the result set.10  - in: query11    name: limit12    schema:13      type: integer14      minimum: 115      maximum: 10016      default: 2017    required: false18    description: The number of items to return.```

#### Common Mistakes
There are two common mistakes when using thedefaultkeyword:

`default` - Usingdefaultwithrequiredparameters or properties, for example, with path parameters. This does not make sense – if a value is required, the client must always send it, and the default value is never used.
`default` `required` - Usingdefaultto specify a sample value. This is not intended use ofdefaultand can lead to unexpected behavior in some Swagger tools. Use theexampleorexampleskeyword for this purpose instead. SeeAdding Examples.
`default` `default` `example` `examples` [Adding Examples](/docs/specification/adding-examples/) ### Enum Parameters
You can restrict a parameter to a fixed set of values by adding theenumto the parameter’sschema. The enum values must be of the same type as the parameter data type.

`enum` `schema` ```
1parameters:2  - in: query3    name: status4    schema:5      type: string6      enum:7        - available8        - pending9        - sold```

`1parameters:2-in:query3name:status4schema:5type:string6enum:7-available8-pending9-sold` More info:Defining an Enum.

[Defining an Enum](/docs/specification/data-models/enums) ### Constant Parameters
You can define a constant parameter as a required parameter with only one possible value:

```
1parameters:2  - in: query3    name: rel_date4    required: true5    schema:6      type: string7      enum:8        - now```

`1parameters:2-in:query3name:rel_date4required:true5schema:6type:string7enum:8-now` Theenumproperty specifies possible values. In this example, only one value can be used, and this will be the only value available in the Swagger UI for the user to choose from.

`enum` Note:A constant parameter is not the same as thedefault parameter value. A constant parameter is always sent by the client, whereas the default value is something that the server uses if the parameter is not sent by the client.

[default parameter value](#default) ### Empty-Valued and Nullable Parameters
Query string parameters may only have a name and no value, like so:

```
1GET /foo?metadata```

`1GET /foo?metadata` UseallowEmptyValueto describe such parameters:

`allowEmptyValue` ```
1parameters:2  - in: query3    name: metadata4    schema:5      type: boolean6    allowEmptyValue: true # <-----```

`1parameters:2-in:query3name:metadata4schema:5type:boolean6allowEmptyValue:true# <-----` OpenAPI 3.0 also supportsnullablein schemas, allowing operation parameters to have thenullvalue. For example, the following schema corresponds toint?in C# andjava.lang.Integerin Java:

`nullable` `null` `int?` `java.lang.Integer` ```
1schema:2  type: integer3  format: int324  nullable: true```

`1schema:2type:integer3format:int324nullable:true` Note:nullableis not the same as an optional parameter or an empty-valued parameter.nullablemeans the parameter value can benull. Specific implementations may choose to map an absent or empty-valued parameter tonull, but strictly speaking these are not the same thing.

`nullable` `nullable` `null` `null` ### Parameter Examples
You can specify anexampleor multipleexamplesfor a parameter. The example value should match the parameter schema. Single example:

`example` `examples` ```
1parameters:2  - in: query3    name: limit4    schema:5      type: integer6      minimum: 17    example: 20```

`1parameters:2-in:query3name:limit4schema:5type:integer6minimum:17example:20` Multiple named examples:

```
1parameters:2  - in: query3    name: ids4    description: One or more IDs5    required: true6    schema:7      type: array8      items:9        type: integer10    style: form11    explode: false12    examples:13      oneId:14        summary: Example of a single ID15        value: [5] # ?ids=516      multipleIds:17        summary: Example of multiple IDs18        value: [1, 5, 7] # ?ids=1,5,7```

For details, seeAdding Examples.

[Adding Examples](/docs/specification/adding-examples/) ### Deprecated Parameters
Usedeprecated: trueto mark a parameter as deprecated.

`deprecated: true` ```
1- in: query2  name: format3  required: true4  schema:5    type: string6    enum: [json, xml, yaml]7  deprecated: true8  description: Deprecated, use the appropriate `Accept` header instead.```

### Common Parameters
#### Common Parameters for All Methods of a Path
Parameters shared by all operations of a path can be defined on the path level instead of the operation level. Path-level parameters are inherited by all operations of that path. A typical use case are the GET/PUT/PATCH/DELETE operations that manipulate a resource accessed via a path parameter.

```
1paths:2  /user/{id}:3    parameters:4      - in: path5        name: id6        schema:7          type: integer8        required: true9        description: The user ID10    get:11      summary: Gets a user by ID12      ...13    patch:14      summary: Updates an existing user with the specified ID15      ...16    delete:17      summary: Deletes the user with the specified ID18      ...```

Any extra parameters defined at the operation level are used together with path-level parameters:

```
1paths:2  /users/{id}:3    parameters:4      - in: path5        name: id6        schema:7          type: integer8        required: true9        description: The user ID.10
11    # GET/users/{id}?metadata=true12    get:13      summary: Gets a user by ID14      # Note we only define the query parameter, because the {id} is defined at the path level.15      parameters:16        - in: query17          name: metadata18          schema:19            type: boolean20          required: false21          description: If true, the endpoint returns only the user metadata.22      responses:23        "200":24          description: OK```

Specific path-level parameters can be overridden on the operation level, but cannot be removed.

```
1paths:2  /users/{id}:3    parameters:4      - in: path5        name: id6        schema:7          type: integer8        required: true9        description: The user ID.10
11    # DELETE /users/{id} - uses a single ID.12    # Reuses the {id} parameter definition from the path level.13    delete:14      summary: Deletes the user with the specified ID.15      responses:16        "204":17          description: User was deleted.18
19    # GET /users/id1,id2,id3 - uses one or more user IDs.20    # Overrides the path-level {id} parameter.21    get:22      summary: Gets one or more users by ID.23      parameters:24        - in: path25          name: id26          required: true27          description: A comma-separated list of user IDs.28          schema:29            type: array30            items:31              type: integer32            minItems: 133          explode: false34          style: simple35      responses:36        "200":37          description: OK```

#### Common Parameters for Various Paths
Different API paths may have common parameters, such as pagination parameters. You can define common parameters under parameters in the globalcomponentssection and reference them elsewhere via$ref.

`components` `$ref` ```
1components:2  parameters:3    offsetParam: # <-- Arbitrary name for the definition that will be used to refer to it.4      # Not necessarily the same as the parameter name.5      in: query6      name: offset7      required: false8      schema:9        type: integer10        minimum: 011      description: The number of items to skip before starting to collect the result set.12    limitParam:13      in: query14      name: limit15      required: false16      schema:17        type: integer18        minimum: 119        maximum: 5020        default: 2021      description: The numbers of items to return.22
23paths:24  /users:25    get:26      summary: Gets a list of users.27      parameters:28        - $ref: "#/components/parameters/offsetParam"29        - $ref: "#/components/parameters/limitParam"30      responses:31        "200":32          description: OK33  /teams:34    get:35      summary: Gets a list of teams.36      parameters:37        - $ref: "#/components/parameters/offsetParam"38        - $ref: "#/components/parameters/limitParam"39      responses:40        "200":41          description: OK```

Note that the parameters defined incomponentsare not parameters applied to all operations — they are simply global definitions that can be easily re-used.

`components` ### Parameter Dependencies
OpenAPI 3.0 does not support parameter dependencies and mutually exclusive parameters. There is an open feature request athttps://github.com/OAI/OpenAPI-Specification/issues/256. What you can do is document the restrictions in the parameter description and define the logic in the 400 Bad Request response. For example, consider the/reportendpoint that accepts either a relative date range (rdate) or an exact range (start_date+end_date):

[https://github.com/OAI/OpenAPI-Specification/issues/256](https://github.com/OAI/OpenAPI-Specification/issues/256) `/report` `rdate` `start_date` `end_date` ```
1GET /report?rdate=Today2GET /report?start_date=2016-11-15&end_date=2016-11-20```

`1GET /report?rdate=Today2GET /report?start_date=2016-11-15&end_date=2016-11-20` You can describe this endpoint as follows:

```
1paths:2  /report:3    get:4      parameters:5        - name: rdate6          in: query7          schema:8            type: string9          description: >10            A relative date range for the report, such as `Today` or `LastWeek`.11            For an exact range, use `start_date` and `end_date` instead.12        - name: start_date13          in: query14          schema:15            type: string16            format: date17          description: >18            The start date for the report. Must be used together with `end_date`.19            This parameter is incompatible with `rdate`.20        - name: end_date21          in: query22          schema:23            type: string24            format: date25          description: >26            The end date for the report. Must be used together with `start_date`.27            This parameter is incompatible with `rdate`.28      responses:29        "400":30          description: Either `rdate` or `start_date`+`end_date` are required.```

### References
Parameter Object

[Parameter Object](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.4.md#parameter-object) Did not find what you were looking for?Ask the communityFound a mistake?Let us know

[Ask the community](https://community.smartbear.com/t5/Swagger-Open-Source-Tools/bd-p/SwaggerOSTools) [Let us know](https://github.com/swagger-api/swagger.io/issues)