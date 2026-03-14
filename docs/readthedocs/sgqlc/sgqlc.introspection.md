# sgqlc.introspection module

## Introspection

Provides the standard GraphQL Introspection Query, same as
https://github.com/graphql/graphql-js/blob/master/src/utilities/introspectionQuery.js
however allows to choose whether to include descriptions and
deprecated fields.

### Downloading schema.json

Usually services provide a `schema.json` file with the introspection results
or offer a development server where the introspection query can be executed
and saved as JSON:

```
python3 \
    -m sgqlc.introspection \
    --exclude-deprecated \
    -H "Authorization: bearer ${TOKEN}" \
    https://server.com/graphql \
    schema.json

```