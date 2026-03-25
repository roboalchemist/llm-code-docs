# Source: https://relay.dev/docs/guides/graphql-server-specification/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [GraphQL Server and Network]
-   [GraphQL Server Specification]

[Version: v20.1.0]

On this page

<div>

# GraphQL Server Specification

</div>

The goal of this document is to specify the assumptions that Relay makes about a GraphQL server and demonstrate them through an example GraphQL schema.

Table of Contents:

-   [Preface](#preface)
-   [Schema](#schema)
-   [Object Identification](#object-identification)
-   [Connections](#connections)
-   [Further Reading](#further-reading)

## Preface[​](#preface "Direct link to Preface") 

The two core assumptions that Relay makes about a GraphQL server are that it provides:

1.  A mechanism for refetching an object.
2.  A description of how to page through connections.

This example demonstrates all two of these assumptions. This example is not comprehensive, but it is designed to quickly introduce these core assumptions, to provide some context before diving into the more detailed specification of the library.

The premise of the example is that we want to use GraphQL to query for information about ships and factions in the original Star Wars trilogy.

It is assumed that the reader is already familiar with [GraphQL](http://graphql.org/); if not, the README for [GraphQL.js](https://github.com/graphql/graphql-js) is a good place to start.

It is also assumed that the reader is already familiar with [Star Wars](https://en.wikipedia.org/wiki/Star_Wars); if not, the 1977 version of Star Wars is a good place to start, though the 1997 Special Edition will serve for the purposes of this document.

## Schema[​](#schema "Direct link to Schema") 

The schema described below will be used to demonstrate the functionality that a GraphQL server used by Relay should implement. The two core types are a faction and a ship in the Star Wars universe, where a faction has many ships associated with it.

``` 
interface Node 

type Faction implements Node 

type Ship implements Node 

type ShipConnection 

type ShipEdge 

type PageInfo 

type Query 
```

## Object Identification[​](#object-identification "Direct link to Object Identification") 

Both `Faction` and `Ship` have identifiers that we can use to refetch them. We expose this capability to Relay through the `Node` interface and the `node` field on the root query type.

The `Node` interface contains a single field, `id`, which is an `ID!`. The `node` root field takes a single argument, an `ID!`, and returns a `Node`. These two work in concert to allow refetching; if we pass the `id` returned in that field to the `node` field, we get the object back.

Let\'s see this in action, and query for the ID of the rebels:

``` 
query RebelsQuery 
}
```

returns

``` 

}
```

So now we know the ID of the Rebels in our system. We can now refetch them:

``` 
query RebelsRefetchQuery 
  }
}
```

returns

``` 

}
```

If we do the same thing with the Empire, we\'ll find that it returns a different ID, and we can refetch it as well:

``` 
query EmpireQuery 
}
```

yields

``` 

}
```

and

``` 
query EmpireRefetchQuery 
  }
}
```

yields

``` 

}
```

The `Node` interface and `node` field assume globally unique IDs for this refetching. A system without globally unique IDs can usually synthesize them by combining the type with the type-specific ID, which is what was done in this example.

The IDs we got back were base64 strings. IDs are designed to be opaque (the only thing that should be passed to the `id` argument on `node` is the unaltered result of querying `id` on some object in the system), and base64ing a string is a useful convention in GraphQL to remind viewers that the string is an opaque identifier.

Complete details on how the server should behave are available in the [GraphQL Object Identification](https://graphql.org/learn/global-object-identification/) best practices guide in the GraphQL site.

## Connections[​](#connections "Direct link to Connections") 

A faction has many ships in the Star Wars universe. Relay contains functionality to make manipulating one-to-many relationships easy, using a standardized way of expressing these one-to-many relationships. This standard connection model offers ways of slicing and paginating through the connection.

Let\'s take the rebels, and ask for their first ship:

``` 
query RebelsShipsQuery 
      }
    }
  }
}
```

yields

``` 

        }
      ]
    }
  }
}
```

That used the `first` argument to `ships` to slice the result set down to the first one. But what if we wanted to paginate through it? On each edge, a cursor will be exposed that we can use to paginate. Let\'s ask for the first two this time, and get the cursor as well:

``` 
query MoreRebelShipsQuery 
      }
    }
  }
}
```

and we get back

``` 

        },
        
        }
      ]
    }
  }
}
```

Notice that the cursor is a base64 string. That\'s the pattern from earlier: the server is reminding us that this is an opaque string. We can pass this string back to the server as the `after` argument to the `ships` field, which will let us ask for the next three ships after the last one in the previous result:

``` 
query EndOfRebelShipsQuery 
      }
    }
  }
}
```

gives us

``` 

        },
        
        },
        
        }
      ]
    }
  }
}
```

Sweet! Let\'s keep going and get the next four!

``` 
query RebelsQuery 
      }
    }
  }
}
```

yields

``` 

  }
}
```

Hm. There were no more ships; guess there were only five in the system for the rebels. It would have been nice to know that we\'d reached the end of the connection, without having to do another round trip in order to verify that. The connection model exposes this capability with a type called `PageInfo`. So let\'s issue the two queries that got us ships again, but this time ask for `hasNextPage`:

``` 
query EndOfRebelShipsQuery 
      }
      pageInfo 
    }
    moreShips: ships(first: 3 after: "YXJyYXljb25uZWN0aW9uOjE=") 
      }
      pageInfo 
    }
  }
}
```

and we get back

``` 

        },
        
        }
      ],
      "pageInfo": 
    },
    "moreShips": 
        },
        
        },
        
        }
      ],
      "pageInfo": 
    }
  }
}
```

So on the first query for ships, GraphQL told us there was a next page, but on the next one, it told us we\'d reached the end of the connection.

Relay uses all of this functionality to build out abstractions around connections, to make these easy to work with efficiently without having to manually manage cursors on the client.

Complete details on how the server should behave are available in the [GraphQL Cursor Connections](https://relay.dev/graphql/connections.htm) spec.

## GraphQL Conf Talk[​](#graphql-conf-talk "Direct link to GraphQL Conf Talk") 

Sabrina Wasserman, an engineer at Meta, gave a talk at GraphQL Conf 2024 deriving the GraphQL connection spec, and explaining how having the behavior of list pagination specified can enable powerful tooling for clients broadly, not just Relay.

# An error occurred. 

Unable to execute JavaScript.

## Further Reading[​](#further-reading "Direct link to Further Reading") 

This concludes the overview of the GraphQL Server Specifications. For the detailed requirements of a Relay-compliant GraphQL server, a more formal description of the [Relay cursor connection](https://relay.dev/graphql/connections.htm) model, the [GraphQL global object identification](https://graphql.org/learn/global-object-identification/) model are all available.

To see code implementing the specification, the [GraphQL.js Relay library](https://github.com/graphql/graphql-relay-js) provides helper functions for creating nodes and connections; that repository\'s [`__tests__`](https://github.com/graphql/graphql-relay-js/tree/main/src/__tests__) folder contains an implementation of the above example as integration tests for the repository.

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/graphql-server-specification.md)