# Source: https://docs.hypermode.com/dgraph/dql/normalize.md

# normalize

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

With the `@normalize` directive, Dgraph returns only aliased predicates and
flattens the result to remove nesting.

Query Example: film name, country, and first two actors (by UID order) of every
Steven Spielberg movie, without `initial_release_date` because no alias is
given, and flattened by `@normalize`.

```json
{ director(func:allofterms(name@en, "steven spielberg")) @normalize {
  director: name@en
  director.film {
    film: name@en initial_release_date starring(first: 2) {
        performance.actor { actor: name@en }
        performance.character { character: name@en }
      }
      country { country: name@en }
    }
  }
}
```

You can also apply `@normalize` on nested query blocks. It works similarly but
only flatten the result of the nested query block where `@normalize` has been
applied. `@normalize` returns a list irrespective of the type of attribute on
which it's applied.

```json
{ director(func:allofterms(name@en, "steven spielberg")) {
  director: name@en
  director.film {
    film: name@en initial_release_date starring(first: 2) @normalize {
      performance.actor { actor: name@en }
      performance.character { character: name@en }
    }
    country { country: name@en }
  }
}
```
