# notNull - returns restaurants where description is not null
{
  restaurants(filters: { description: { notNull: true } }) {
    name
  }
}
```

```graphql title="Simple examples for logical operators (and, or, not)"