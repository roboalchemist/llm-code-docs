# Source: https://kreya.app/docs/operations/rest.md

# Source: https://kreya.app/docs/importers/rest.md

# REST

To call REST APIs, using importers is optional. However, using an importer has a lot of advantages. For example, request contents are generated automatically.

### Import via OpenAPI URL[​](#import-via-openapi-url "Direct link to Import via OpenAPI URL")

To import an OpenAPI definition, the simplest way is to enter the URL of the OpenAPI specification. Both YAML and JSON formats are allowed.

![Adding a OpenAPI REST importer from an URL](/assets/ideal-img/rest-openapi-url-importer.b91910b.400.png)

### Import via OpenAPI file[​](#import-via-openapi-file "Direct link to Import via OpenAPI file")

Should you have an OpenAPI file locally, simply choose the "REST OpenAPI file" importer type and select your file.

![Adding a OpenAPI REST importer from a file](/assets/ideal-img/rest-openapi-file-importer.6be76eb.400.png)

*Kreya only stores the path to the OpenAPI file. If you intend to share your Kreya project, make sure that the path stays correct. Kreya uses relative paths by default, but you may also use system environment variables like `%APPDATA%` or `${GOPATH}`. They will work on any OS, regardless of the format.*
