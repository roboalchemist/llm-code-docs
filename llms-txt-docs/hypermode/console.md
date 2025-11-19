# Source: https://docs.hypermode.com/modus/sdk/go/console.md

# Source: https://docs.hypermode.com/modus/sdk/assemblyscript/console.md

# Source: https://docs.hypermode.com/dgraph/ratel/console.md

# Console

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

## Query panel

You can execute two kinds of operations: queries and mutations. The history
section holds either queries or mutations.

<img src="https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/ratel/ratel_console.png?fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=2e4443312dc8f3f52244f44cd6919ba3" alt="Ratel Console" width="777" height="480" data-path="images/dgraph/ratel/ratel_console.png" srcset="https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/ratel/ratel_console.png?w=280&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=b9f375154ccb481600c1231bdb589f26 280w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/ratel/ratel_console.png?w=560&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=dba9034b957f33c25e9424863b87413a 560w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/ratel/ratel_console.png?w=840&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=e244d82707a853d66479828cdd9e86d2 840w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/ratel/ratel_console.png?w=1100&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=ec3eb9c7600feff739e0cd722e4d52bb 1100w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/ratel/ratel_console.png?w=1650&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=5b87db61849267f38cfd2d52dd0b8a49 1650w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/ratel/ratel_console.png?w=2500&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=9b21efcfc3bdd4998b26eae1e9ea3ced 2500w" data-optimize="true" data-opv="2" />

### Query

On this panel, you can only run DQL (former GraphQL+-). You can use `#` to
comment on something. You also have the DQL Variable. See more at
[DQL](/dgraph/dql/schema).

### Mutation

On this panel, you can run RDF and JSON mutations.

## Result panel

### Graph

On this tab you can view the query results in a Graph format. This allows you to
visualize the Nodes and their relations.

### JSON

On this tab you have the JSON response from the cluster. The actual data comes
in the `data` key. You also have the `extensions` key which returns
`server_latency`, `txn`, and other metrics.

### Request

On this tab you have the actual request sent to the cluster.

### Geo

On this tab you can visualize a query that provides Geodata.

<Note>
  Your objects must contain a predicate or alias named `location` to use the geo
  display. To show a label, use a predicate or alias named `name`.
</Note>
