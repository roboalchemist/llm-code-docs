# Source: https://relay.dev/docs/guides/persisted-queries/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [GraphQL Server and Network]
-   [Persisted Queries]

[Version: v20.1.0]

On this page

<div>

# Persisted Queries

</div>

The Relay compiler supports persisted queries. This is useful because:

-   The client operation text becomes just an md5 hash which is usually shorter than the real query string. This saves upload bytes from the client to the server.

-   The server can now allowlist queries which improves security by restricting the operations that can be executed by a client.

## Usage on the client[​](#usage-on-the-client "Direct link to Usage on the client") 

### The `persistConfig` option[​](#the-persistconfig-option "Direct link to the-persistconfig-option") 

In the `relay` configuration section of your `package.json` you\'ll need specify \"persistConfig\".

``` 
"scripts": ,
"relay": 
  }
}
```

Specifying `persistConfig` in the config will do the following:

1.  It converts all query and mutation operation texts to md5 hashes.

    For example without `persistConfig`, a generated `ConcreteRequest` might look like below:

    ::: 
    ::: codeBlockContent_QJqH
    ``` 
    const node/*: ConcreteRequest*/ = (function()\n}\n\nfragment TodoItem_item_2FOrhs on Todo \n",
      //... excluded for brevity
    };
    })();
    ```
    :::
    :::

    With `persistConfig` this becomes:

    ::: 
    ::: codeBlockContent_QJqH
    ``` 
    const node/*: ConcreteRequest*/ = (function();
    })();
    ```
    :::
    :::

2.  It will send an HTTP POST request with a `text` parameter to the specified `url`. You can also add additional request body parameters via the `params` option.

``` 
"scripts": ,
"relay": 
  }
}
```

### Local Persisted Queries[​](#local-persisted-queries "Direct link to Local Persisted Queries") 

With the following config, you can generate a local JSON file which contains a map of `operation_id => full operation text`.

``` 
"scripts": ,
"relay": 
}
```

Ideally, you\'ll take this file and ship it to your server at deploy time so your server knows about all the queries it could possibly receive. If you don\'t want to do that, you\'ll have to implement the [Automatic Persisted Queries handshake](https://www.apollographql.com/docs/apollo-server/performance/apq/).

#### Tradeoffs[​](#tradeoffs "Direct link to Tradeoffs") 

-   ✅ If your server\'s persisted query datastore gets wiped, you can recover automatically through your client\'s requests.
-   ❌ When there\'s a cache miss, it\'ll cost you an extra round trip to the server.
-   ❌ You\'ll have to ship your `persisted_queries.json` file to the browser which will increase your bundle size.

### Example implementation of `relayLocalPersisting.js`[​](#example-implementation-of-relaylocalpersistingjs "Direct link to example-implementation-of-relaylocalpersistingjs") 

Here\'s an example of a simple persist server that will save query text to the `queryMap.json` file.

``` 
const http = require('http');
const crypto = require('crypto');
const fs = require('fs');

function md5(input) 

class QueryMap 

  _flush() 

  saveQuery(text) 
}

const queryMap = new QueryMap('./queryMap.json');

async function requestListener(req, res) 
    const data = Buffer.concat(buffers).toString();
    res.writeHead(200, );
    try 
      const text = new URLSearchParams(data).get('text');
      if (text == null) 
      const id = queryMap.saveQuery(text);
      res.end(JSON.stringify());
    } catch (e) .`);
    }
  } else 
}

const PORT = 2999;
const server = http.createServer(requestListener);
server.listen(PORT);

console.log(`Relay persisting server listening on $ port.`);
```

The example above writes the complete query map file to `./queryMap.json`. To use this, you\'ll need to update `package.json`:

``` 
"scripts": 
```

### Network layer changes[​](#network-layer-changes "Direct link to Network layer changes") 

You\'ll need to modify your network layer fetch implementation to pass an ID parameter in the POST body (e.g., `doc_id`) instead of a query parameter:

``` 
function fetchQuery(operation, variables) ,
    body: JSON.stringify(),
  }).then(response => );
}
```

## Executing Persisted Queries on the Server[​](#executing-persisted-queries-on-the-server "Direct link to Executing Persisted Queries on the Server") 

To execute client requests that send persisted queries instead of query text, your server will need to be able to lookup the query text corresponding to each ID. Typically this will involve saving the output of the `queryMap.json` JSON file to a database or some other storage mechanism, and retrieving the corresponding text for the ID specified by a client.

Additionally, your implementation of `relayLocalPersisting.js` could directly save queries to the database or other storage.

For universal applications where the client and server code are in one project, this is not an issue since you can place the query map file in a common location accessible to both the client and the server.

### Compile time push[​](#compile-time-push "Direct link to Compile time push") 

For applications where the client and server projects are separate, one option is to have an additional npm run script to push the query map at compile time to a location accessible by your server:

``` 
"scripts": 
```

Some possibilities of what you can do in `./pushQueries.js`:

-   `git push` to your server repo.

-   Save the query maps to a database.

### Run time push[​](#run-time-push "Direct link to Run time push") 

A second more complex option is to push your query maps to the server at runtime, without the server knowing the query IDs at the start. The client optimistically sends a query ID to the server, which does not have the query map. The server then in turn requests for the full query text from the client so it can cache the query map for subsequent requests. This is a more complex approach requiring the client and server to interact to exchange the query maps.

### Simple server example[​](#simple-server-example "Direct link to Simple server example") 

Once your server has access to the query map, you can perform the mapping. The solution varies depending on the server and database technologies you use, so we\'ll just cover the most common and basic example here.

If you use `express-graphql` and have access to the query map file, you can import it directly and perform the matching using the `persistedQueries` middleware from [express-graphql-persisted-queries](https://github.com/kyarik/express-graphql-persisted-queries).

``` 
import express from 'express';
import  from 'express-graphql';
import  from 'express-graphql-persisted-queries';
import queryMap from './path/to/queryMap.json';

const app = express();

app.use(
  '/graphql',
  persistedQueries(),
  graphqlHTTP(),
);
```

## Using `persistConfig` and `--watch`[​](#using-persistconfig-and---watch "Direct link to using-persistconfig-and---watch") 

It is possible to continuously generate the query map files by using the `persistConfig` and `--watch` options simultaneously. This only makes sense for universal applications i.e. if your client and server code are in a single project and you run them both together on localhost during development. Furthermore, in order for the server to pick up changes to the `queryMap.json`, you\'ll need to have server side hot-reloading set up. The details on how to set this up are out of the scope of this document.

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/persisted-queries.md)