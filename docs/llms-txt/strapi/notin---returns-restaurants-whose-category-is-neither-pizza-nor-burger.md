# notIn - returns restaurants whose category is neither "pizza" nor "burger"
{
  restaurants(filters: { category: { notIn: ["pizza", "burger"] } }) {
    name
  }
}
```

```graphql title="Simple examples for null checks operators (null, notNull)"