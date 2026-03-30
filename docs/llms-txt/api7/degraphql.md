# Source: https://docs.api7.ai/hub/degraphql.md

# degraphql

The `degraphql` plugin supports communicating with upstream GraphQL services over regular HTTP requests by mapping GraphQL queries to HTTP endpoints.

## Examples[â](#examples "Direct link to Examples")

The examples below use [Pokemon GraphQL API](https://graphql-pokemon.js.org/) as the upstream GraphQL server and demonstrate how you can configure `degraphql` to transform different types of GraphQL queries.

### Transform a Basic Query[â](#transform-a-basic-query "Direct link to Transform a Basic Query")

The following example demonstrates how you can transform a simple query below:

```
query {
  getAllPokemon {
    key
    color
  }
}
```

Create a route with the `degraphql` plugin as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "degraphql-route",
    "methods": ["POST"],
    "uri": "/v7",
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "graphqlpokemon.favware.tech": 1
      },
      "scheme": "https",
      "pass_host": "node"
    },
    "plugins": {
      "degraphql": {
        "query": "{\n  getAllPokemon {\n    key\n    color\n  }\n}"
      }
    }
  }'
```

Send a request to the route to verify:

```
curl "http://127.0.0.1:9080/v7" -X POST
```

You should see a response similar to the following:

```
{
  "data": {
    "getAllPokemon": [
      { "key": "pokestarsmeargle", "color": "White" },
      { "key": "pokestarufo", "color": "White" },
      { "key": "pokestarufo2", "color": "White" },
      ...
      { "key": "walkingwake", "color": "Blue" },
      { "key": "ironleaves", "color": "Green" }
    ]
  }
}
```

### Transform a Query with Variables[â](#transform-a-query-with-variables "Direct link to Transform a Query with Variables")

The following example demonstrates how you can transform the query below, with a variable:

```
query ($pokemon: PokemonEnum!) {
  getPokemon(
    pokemon: $pokemon
  ) {
    color
    species
  }
}

variable:
{
  "pokemon": "pikachu"
}
```

Create a route with the `degraphql` plugin as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "degraphql-route",
    "uri": "/v7",
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "graphqlpokemon.favware.tech": 1
      },
      "scheme": "https",
      "pass_host": "node"
    },
    "plugins": {
      "degraphql": {
        "query": "query ($pokemon: PokemonEnum!) {\n  getPokemon(\n    pokemon: $pokemon\n  ) {\n    color\n    species\n  }\n}\n",
        "variables": ["pokemon"]
      }
    }
  }'
```

Send a request to the route to verify:

```
curl "http://127.0.0.1:9080/v7" -X POST \
  -d '{
    "pokemon": "pikachu"
  }'
```

You should see a response similar to the following:

```
{
  "data": {
    "getPokemon": {
      "color": "Yellow",
      "species": "pikachu"
    }
  }
}
```

Alternatively, you can also pass the variable in the URL query string of a GET request:

```
curl "http://127.0.0.1:9080/v7?pokemon=pikachu" -H "x-apollo-operation-name: GET"
```

You should see the same response as the previous.
