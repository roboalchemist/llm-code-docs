# Source: https://swagger.io/docs/specification/paths-and-operations/

# Paths and Operations
Note

OAS3This page is about OpenAPI 3.0. If you use OpenAPI 2.0, see theOpenAPI 2.0 guide.

[OpenAPI 2.0 guide](/docs/specification/v2_0/paths-and-operations/) In OpenAPI terms,pathsare endpoints (resources), such as/usersor/reports/summary/, that your API exposes, andoperationsare the HTTP methods used to manipulate these paths, such as GET, POST or DELETE.

`/users` `/reports/summary/` ### Paths
API paths and operations are defined in the globalpathssection of the API specification.

`paths` ```
1paths:2  /ping: ...3  /users: ...4  /users/{id}: ...```

`1paths:2/ping:...3/users:...4/users/{id}:...` All paths are relative to theAPI server URL. The full request URL is constructed as<server-url>/path. Globalserverscan also be overridden on the path level or operation level (more on thatbelow). Paths may have an optional shortsummaryand a longerdescriptionfor documentation purposes. This information is supposed to be relevant to all operations in this path.descriptioncan bemulti-lineand supportsMarkdown(CommonMark) for rich text representation.

[API server URL](/docs/specification/api-host-and-base-path/) `<server-url>/path` `servers` [below](#overriding-servers) `summary` `description` `description` [multi-line](http://stackoverflow.com/questions/3790454/in-yaml-how-do-i-break-a-string-over-multiple-lines) [Markdown](http://commonmark.org/help/) ```
1paths:2  /users/{id}:3    summary: Represents a user4    description: >5      This resource represents an individual user in the system.6      Each user is identified by a numeric `id`.7
8    get: ...9    patch: ...10    delete: ...```

### Path Templating
You can use curly braces{}to mark parts of an URL aspath parameters:

`{}` [path parameters](/docs/specification/describing-parameters/#path-parameters) ```
1/users/{id}2/organizations/{orgId}/members/{memberId}3/report.{format}```

`1/users/{id}2/organizations/{orgId}/members/{memberId}3/report.{format}` The API client needs to provide appropriate parameter values when making an API call, such as/users/5or/users/12.

`/users/5` `/users/12` ### Operations
For each path, you define operations (HTTP methods) that can be used to access that path. OpenAPI 3.0 supportsget,post,put,patch,delete,head,options, andtrace. A single path can support multiple operations, for exampleGET /usersto get a list of users andPOST /usersto add a new user. OpenAPI defines a unique operation as a combination of a path and an HTTP method. This means that two GET or two POST methods for the same path are not allowed – even if they have different parameters (parameters have no effect on uniqueness). Below is a minimal example of an operation:

`get` `post` `put` `patch` `delete` `head` `options` `trace` `GET /users` `POST /users` ```
1paths:2  /ping:3    get:4      responses:5        "200":6          description: OK```

`1paths:2/ping:3get:4responses:5"200":6description:OK` Here is a more detailed example with parameters and response schema:

```
1paths:2  /users/{id}:3    get:4      tags:5        - Users6      summary: Gets a user by ID.7      description: >8        A detailed description of the operation.9        Use markdown for rich text representation,10        such as **bold**, *italic*, and [links](https://swagger.io).11      operationId: getUserById12      parameters:13        - name: id14          in: path15          description: User ID16          required: true17          schema:18            type: integer19            format: int6420      responses:21        "200":22          description: Successful operation23          content:24            application/json:25              schema:26                $ref: "#/components/schemas/User"27      externalDocs:28        description: Learn more about user operations provided by this API.29        url: http://api.example.com/docs/user-operations/30
31components:32  schemas:33    User:34      type: object35      properties:36        id:37          type: integer38          format: int6439        name:40          type: string41      required:42        - id43        - name```

Operations also support some optional elements for documentation purposes:

- A shortsummaryand a longerdescriptionof what an operation does.descriptioncan bemulti-lineand supportsMarkdown(CommonMark) for rich text representation.
`summary` `description` `description` [multi-line](http://stackoverflow.com/questions/3790454/in-yaml-how-do-i-break-a-string-over-multiple-lines) [Markdown](http://commonmark.org/help/) - tags– used to group operations logically by resources or any other qualifier. SeeGrouping Operations With Tags.
`tags` [Grouping Operations With Tags](/docs/specification/grouping-operations-with-tags/) - externalDocs– used to reference an external resource that contains additional documentation.
`externalDocs` ### Operation Parameters
OpenAPI 3.0 supports operation parameters passed via path, query string, headers, and cookies. You can also define the request body for operations that transmit data to the server, such as POST, PUT and PATCH. For details, seeDescribing ParametersandDescribing Request Body.

[Describing Parameters](/docs/specification/describing-parameters/) [Describing Request Body](/docs/specification/describing-request-body/describing-request-body/) ### Query String in Paths
Query string parametersmust notbe included in paths. They should be defined asquery parametersinstead.

[query parameters](/docs/specification/describing-parameters/#query-parameters) Incorrect:

```
1paths:2  /users?role={role}:```

`1paths:2/users?role={role}:` Correct:

```
1paths:2  /users:3    get:4      parameters:5        - in: query6          name: role7          schema:8            type: string9            enum: [user, poweruser, admin]10          required: true```

This also means that it is impossible to have multiple paths that differ only in query string, such as:

```
1GET /users?firstName=value&lastName=value2GET /users?role=value```

`1GET /users?firstName=value&lastName=value2GET /users?role=value` This is because OpenAPI considers a unique operation as a combination of a path and the HTTP method, and additional parameters do not make the operation unique. Instead, you should use unique paths such as:

```
1GET /users/findByName?firstName=value&lastName=value2GET /users/findByRole?role=value```

`1GET /users/findByName?firstName=value&lastName=value2GET /users/findByRole?role=value` ### operationId
operationIdis an optional unique string used to identify an operation. If provided, these IDs must be unique among all operations described in your API.

`operationId` ```
1/users:2  get:3    operationId: getUsers4    summary: Gets all users5    ...6  post:7    operationId: addUser8    summary: Adds a new user9    ...10/user/{id}:11  get:12    operationId: getUserById13    summary: Gets a user by user ID14    ...```

Some common use cases for operationId are:

- Some code generators use this value to name the corresponding methods in code.
- Linkscan refer to the linked operations byoperationId.
[Links](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.4.md#link-object) `operationId` ### Deprecated Operations
You can mark specific operations asdeprecatedto indicate that they should be transitioned out of usage:

`deprecated` ```
1/pet/findByTags:2  get:3    deprecated: true```

`1/pet/findByTags:2get:3deprecated:true` Tools may handle deprecated operations in a specific way. For example, Swagger UI displays them with a different style:

### Overriding Global Servers
The globalserversarray can be overridden on the path level or operation level. This is useful if some endpoints use a different server or base path than the rest of the API. Common examples are:

`servers` - Different base URL for file upload and download operations.
Different base URL for file upload and download operations.

- Deprecated but still functional endpoints.servers:url:https://api.example.com/v1
Deprecated but still functional endpoints.

servers:

- url:https://api.example.com/v1
[https://api.example.com/v1](https://api.example.com/v1) ```
1paths:2  /files:3    description: File upload and download operations4    servers:5      - url: https://files.example.com6        description: Override base path for all operations with the /files path7    ...8
9/ping:10    get:11      servers:12        - url: https://echo.example.com13          description: Override base path for the GET /ping operation```

Did not find what you were looking for?Ask the communityFound a mistake?Let us know

[Ask the community](https://community.smartbear.com/t5/Swagger-Open-Source-Tools/bd-p/SwaggerOSTools) [Let us know](https://github.com/swagger-api/swagger.io/issues)