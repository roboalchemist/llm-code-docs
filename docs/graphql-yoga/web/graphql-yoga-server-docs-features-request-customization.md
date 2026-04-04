# Source: https://the-guild.dev/graphql/yoga-server/docs/features/request-customization

Title: Request Customization | Yoga

URL Source: https://the-guild.dev/graphql/yoga-server/docs/features/request-customization

Markdown Content:
[Skip to Content](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#nextra-skip-nav)

On This Page

Request Customization
---------------------

For each type of request, GraphQL Yoga uses a specific parser to parse the incoming request and extract the GraphQL operation from it. Then it applies some validation logic to the extracted object, then it passes it to the GraphQL execution engine. Yoga mostly follows GraphQL-over-HTTP standards for this validation and parsing logic. [See the GraphQL-over-HTTP compliance test results of GraphQL Yoga](https://github.com/graphql/graphql-http/blob/main/implementations/graphql-yoga/README.md)

The parsers are expected to return `GraphQLParams` object that contains the following properties:

*   `query`: The GraphQL operation as a string.
*   `variables`: The variables for the operation.
*   `operationName`: The name of the operation.
*   `extensions`: The extensions for the operation.

It doesn’t matter how the request is sent, Yoga engine expects the request to parsed in the form of a `GraphQLParams` object.

Request Parser[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#request-parser)
--------------------------------------------------------------------------------------------------------------

Request parsers are responsible for extracting the GraphQL operation and the other relevant information from the incoming request. Each parser is responsible for a specific type of request based on the content type and the HTTP method.

### GraphQL-over-HTTP Spec[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#graphql-over-http-spec)

These parsers are implemented following the [GraphQL-over-HTTP spec](https://graphql.github.io/graphql-over-http/).

#### `GET` Parser[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#get-parser)

This request parser extracts the GraphQL operation from the query string by following GraphQL-over-HTTP spec.

[See the implementation](https://github.com/graphql-hive/graphql-yoga/blob/main/packages/graphql-yoga/src/plugins/request-parser/get.ts)[See the relevant part in GraphQL-over-HTTP spec](https://graphql.github.io/graphql-over-http/draft/#sec-GET)

##### Example Request[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#example-request)

`fetch('/graphql?query=query { __typename }')`

#### `POST` JSON Parser[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#post-json-parser)

This request parser extracts the GraphQL operation from the JSON body of the POST request by following GraphQL-over-HTTP spec.

[See the implementation](https://github.com/graphql-hive/graphql-yoga/blob/main/packages/graphql-yoga/src/plugins/request-parser/post-json.ts).

##### Example Request[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#example-request-1)

```
fetch('/graphql', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    query: 'query { __typename }'
  })
})
```

### GraphQL Multipart Request Spec[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#graphql-multipart-request-spec)

The parser for multipart requests is implemented following the [GraphQL Multipart Request Spec](https://github.com/jaydenseric/graphql-multipart-request-spec).

#### `POST` Multipart Parser[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#post-multipart-parser)

This request parser extracts the GraphQL operation from the multipart request by following the GraphQL Multipart Request Spec. It handles the HTTP request by parsing it as `multipart/form-data` and extracting the GraphQL operation from it.

[See the implementation](https://github.com/graphql-hive/graphql-yoga/blob/main/packages/graphql-yoga/src/plugins/request-parser/post-multipart.ts).

##### Example Request[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#example-request-2)

```
const formData = new FormData()
formData.append('operations', JSON.stringify({ query: 'query { __typename }' }))
fetch('/graphql', {
  method: 'POST',
  headers: {
    'Content-Type': 'multipart/form-data'
  },
  body: formData
})
```

### Extra Parsers[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#extra-parsers)

These parsers are not part of any spec but are de-facto standards in the GraphQL community.

### `POST` GraphQL String Parser[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#post-graphql-string-parser)

This request parser extracts the GraphQL operation from the body of the POST request as a string.

[See the implementation](https://github.com/graphql-hive/graphql-yoga/blob/main/packages/graphql-yoga/src/plugins/request-parser/post-graphql-string.ts).

##### Example Request[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#example-request-3)

```
fetch('/graphql', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/graphql'
  },
  body: 'query { __typename }'
})
```

### `POST` FormUrlEncoded Parser[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#post-formurlencoded-parser)

This request parser extracts the GraphQL operation from the form data as url encoded in the POST body. The context is similar to the `GET` parser but the data is sent in the body of the request.

[See the implementation](https://github.com/graphql-hive/graphql-yoga/blob/main/packages/graphql-yoga/src/plugins/request-parser/post-form-url-encoded.ts)

##### Example Request[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#example-request-4)

```
fetch('/graphql', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  body: 'query=query { __typename }'
})
```

### Write your own parser[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#write-your-own-parser)

If you want to handle a specific type of request body that is not part of the list above, you can write your own parser. We use `onRequestParse` to hook into the request parsing process and add your own logic.

Request parsers are functions that take the request object and return a promise that resolves to a `GraphQLParams` object.

```
import { GraphQLParams, Plugin } from 'graphql-yoga'
 
const useMyParser: Plugin = () => {
  return {
    onRequestParse({ request, url, setRequestParser }) {
      const contentType = request.headers.get('Content-Type')
      if (contentType === 'application/my-content-type') {
        setRequestParser(async function myParser() {
          const body = await request.text()
          const params: GraphQLParams = getParamsFromMyParser(body)
          return params
        })
      }
    }
  }
}
```

Request Validation[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#request-validation)
----------------------------------------------------------------------------------------------------------------------

Request validation is the process of validating the incoming request to ensure that it follows the GraphQL-over-HTTP spec. Besides the required validation rules, Yoga applies some extra rules to ensure the security and the performance of the server such as disallowing extra paramters in the request body. However, you can customize this kind of behaviors on your own risk.

### Extra Parameters in `GraphQLParams`[](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization#extra-parameters-in-graphqlparams)

Yoga doesn’t allow extra parameters in the request body other than `query`, `operationName`, `extensions`, and `variables`. And it returns a 400 HTTP error if it finds any extra parameters. But you can customize this behavior by passing an array of extra parameter names to the `extraParamNames` option.

```
import { createYoga } from 'graphql-yoga'
 
const yoga = createYoga({
  /* other options */
  extraParamNames: ['extraParam1', 'extraParam2']
})
```

Then you can send extra parameters in the request body.

```
const res = await yoga.fetch('/graphql', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    query: 'query { __typename }',
    extraParam1: 'value1',
    extraParam2: 'value2'
  })
})
 
console.assert(res.status === 200)
```
