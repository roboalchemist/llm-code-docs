# GraphQL API

The GraphQL API allows performing queries and mutations to interact with the [content-types](/cms/backend-customization/models#content-types) through Strapi's [GraphQL plugin](/cms/plugins/graphql). Results can be [filtered](#filters), [sorted](#sorting) and [paginated](#pagination).

:::prerequisites
To use the GraphQL API, install the [GraphQL](/cms/plugins/graphql) plugin:

</Tabs>
:::

Once installed, the GraphQL playground is accessible at the `/graphql` URL and can be used to interactively build your queries and mutations and read documentation tailored to your content-types:

</Tabs>

#### Fetch relations

You can ask to include relation data in your flat queries or in your 

</Columns>
</details>

:::

</TabItem>

</Tabs>

### Fetch media fields

Media fields content is fetched just like other attributes.

The following example fetches the `url` attribute value for each `cover` media field attached to each document from the "Restaurants" content-type:

```graphql
{
  restaurants {
    images {
      documentId
      url
    }
  }
}
```

For multiple media fields, you can use flat queries or 

</Tabs>

### Fetch components

Components content is fetched just like other attributes.

The following example fetches the `label`, `start_date`, and `end_date` attributes values for each `closingPeriod` component added to each document from the "Restaurants" content-type:

```graphql
{
  restaurants {
    closingPeriod {
      label
      start_date
      end_date
    }
  }
}
```

### Fetch dynamic zone data

Dynamic zones are union types in GraphQL so you need to use 

```graphql title="Simple examples for membership operators (in, notIn)"