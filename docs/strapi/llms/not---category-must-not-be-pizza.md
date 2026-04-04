# not - category must NOT be "pizza"
{
  restaurants(filters: {
    not: { category: { eq: "pizza" } }
  }) {
    name
  }
}
```

```graphql title="Example with nested logical operators: use and, or, and not to find pizzerias under 20 euros"
{
  restaurants(
    filters: {
      and: [
        { not: { averagePrice: { gte: 20 } } }
        {
          or: [
            { name: { eq: "Pizzeria" } }
            { name: { startsWith: "Pizzeria" } }
          ]
        }
      ]
    }
  ) {
    documentId
    name
    averagePrice
  }
}
```

</ApiCall>

### Fetch a document in a specific locale {#locale-fetch}

To fetch a documents 

</ApiCall>

### Create a new localized document {#locale-create}

The `locale` field can be passed to create a localized document