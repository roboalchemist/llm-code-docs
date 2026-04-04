# Source: https://swagger.io/docs/specification/basic-structure/

# Basic Structure
Note

OAS3This page is about OpenAPI 3.0. If you use OpenAPI 2.0, visitOpenAPI 2.0 pages.

[OpenAPI 2.0 pages](/docs/specification/v2_0/basic-structure/) You can write OpenAPI definitions inYAMLorJSON. In this guide, we use only YAML examples but JSON works equally well. A sample OpenAPI 3.0 definition written in YAML looks like:

[YAML](https://en.wikipedia.org/wiki/YAML) [JSON](https://en.wikipedia.org/wiki/JSON) ```
1openapi: 3.0.42info:3  title: Sample API4  description: Optional multiline or single-line description in [CommonMark](http://commonmark.org/help/) or HTML.5  version: 0.1.96
7servers:8  - url: http://api.example.com/v19    description: Optional server description, e.g. Main (production) server10  - url: http://staging-api.example.com11    description: Optional server description, e.g. Internal staging server for testing12
13paths:14  /users:15    get:16      summary: Returns a list of users.17      description: Optional extended description in CommonMark or HTML.18      responses:19        "200": # status code20          description: A JSON array of user names21          content:22            application/json:23              schema:24                type: array25                items:26                  type: string```

All keyword names arecase-sensitive.

### Metadata
Every API definition must include the version of the OpenAPI Specification that this definition is based on:

```
1openapi: 3.0.4```

`1openapi:3.0.4` The OpenAPI version defines the overall structure of an API definition – what you can document and how you document it. OpenAPI 3.0 usessemantic versioningwith a three-part version number. Theavailable versionsare3.0.0,3.0.1,3.0.2,3.0.3, and3.0.4; they are functionally the same.

[semantic versioning](http://semver.org/) [available versions](https://github.com/OAI/OpenAPI-Specification/releases) `3.0.0` `3.0.1` `3.0.2` `3.0.3` `3.0.4` Theinfosection contains API information:title,description(optional),version:

`info` `title` `description` `version` ```
1info:2  title: Sample API3  description: Optional multiline or single-line description in [CommonMark](http://commonmark.org/help/) or HTML.4  version: 0.1.9```

titleis your API name.descriptionis extended information about your API. It can bemultilineand supports theCommonMarkdialect of Markdown for rich text representation. HTML is supported to the extent provided by CommonMark (seeHTML BlocksinCommonMark 0.27 Specification).versionis an arbitrary string that specifies the version of your API (do not confuse it with file revision or theopenapiversion). You can usesemantic versioninglikemajor.minor.patch, or an arbitrary string like1.0-betaor2017-07-25.infoalso supports other keywords for contact information, license, terms of service, and other details.

`title` `description` [multiline](http://stackoverflow.com/a/21699210) [CommonMark](http://commonmark.org/help/) [HTML Blocks](http://spec.commonmark.org/0.27/) [CommonMark 0.27 Specification](http://spec.commonmark.org/0.27/) `version` `openapi` [semantic versioning](http://semver.org/) `info` Reference:Info Object.

[Info Object](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.4.md#info-object) ### Servers
Theserverssection specifies the API server and base URL. You can define one or several servers, such as production and sandbox.

`servers` ```
1servers:2  - url: http://api.example.com/v13    description: Optional server description, e.g. Main (production) server4  - url: http://staging-api.example.com5    description: Optional server description, e.g. Internal staging server for testing```

All API paths are relative to the server URL. In the example above,/usersmeanshttp://api.example.com/v1/usersorhttp://staging-api.example.com/users, depending on the server used. For more information, seeAPI Server and Base Path.

`/users` `http://api.example.com/v1/users` `http://staging-api.example.com/users` [API Server and Base Path](/docs/specification/api-host-and-base-path/) ### Paths
Thepathssection defines individual endpoints (paths) in your API, and the HTTP methods (operations) supported by these endpoints. For example,GET /userscan be described as:

`paths` `GET /users` ```
1paths:2  /users:3    get:4      summary: Returns a list of users.5      description: Optional extended description in CommonMark or HTML6      responses:7        "200":8          description: A JSON array of user names9          content:10            application/json:11              schema:12                type: array13                items:14                  type: string```