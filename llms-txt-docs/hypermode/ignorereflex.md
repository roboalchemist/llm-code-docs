# Source: https://docs.hypermode.com/dgraph/dql/ignorereflex.md

# ignorereflex

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

The `@ignorereflex` directive forces the removal of child nodes that are
reachable from themselves as a parent, through any path in the query result

Query Example: all the co-actors of Rutger Hauer. Without `@ignorereflex`, the
result would also include Rutger Hauer for every movie.

```json
{
  coactors(func: eq(name@en, "Rutger Hauer")) @ignorereflex {
    actor.film {
      performance.film {
        starring {
          performance.actor {
            name@en
          }
        }
      }
    }
  }
}
```
