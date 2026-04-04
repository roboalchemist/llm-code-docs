# Source: https://kreya.app/docs/operations/graphql.md

# Source: https://kreya.app/docs/importers/graphql.md

# GraphQL

To call GraphQL APIs, using importers is optional. However, using a schema importer has a lot of advantages. For example, it provides autocompletion for your requests and scripting types and validates your queries.

### GraphQL schema introspection[​](#graphql-schema-introspection "Direct link to GraphQL schema introspection")

Should you have a running GraphQL server which supports introspection, simply choose the "GraphQL schema introspection" importer type and enter the endpoint URL. You can use templating for the endpoint if needed (see [Templating](/docs/templating.md)). You may also configure authentication, headers and query parameters if needed.

### GraphQL Schema file importer[​](#graphql-schema-file-importer "Direct link to GraphQL Schema file importer")

Should you have a GraphQL Schema file locally (e.g. `.graphql` or `.gql`), simply choose the "GraphQL Schema file" importer type and select your file.

*Kreya only stores the path to the Schema file. If you intend to share your Kreya project, make sure that the path stays correct. Kreya uses relative paths by default, but you may also use system environment variables like `%APPDATA%` or `${GOPATH}`. They will work on any OS, regardless of the format.*

### GraphQL Schema URL importer[​](#graphql-schema-url-importer "Direct link to GraphQL Schema URL importer")

Should you have a GraphQL Schema file hosted online, simply choose the "GraphQL Schema URL" importer type and enter the URL to your file You can use templating for the endpoint if needed (see [Templating](/docs/templating.md)). You may also configure authentication, headers and query parameters if needed.

*Kreya does not store the schema file locally. Make sure that the URL is always accessible when using this importer.*
