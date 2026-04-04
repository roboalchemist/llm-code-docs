# Source: https://docs.hypermode.com/dgraph/graphql/security/cors.md

# Restrict origins

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

To restrict origins of HTTP requests add lines starting with
`# Dgraph.Allow-Origin` at the end of your GraphQL schema specifying the origins
allowed.

For example, the following restricts all origins except the ones specified.

```sh
# Dgraph.Allow-Origin "https://example.com"
# Dgraph.Allow-Origin "https://www.example.com"
```

<Note>CORS restrictions only apply to browsers.</Note>

<Note>
  By default, the `/graphql` endpoint doesn't limit the request origin
  (`Access-Control-Allow-Origin: *`).
</Note>
