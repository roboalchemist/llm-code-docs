# mutation

> The SDK method to make updates to your repository via the API.

```
import { basehub } from 'basehub'

basehub().mutation({  })
```

The `basehub.mutation()` lets you send GraphQL mutations to the BaseHub API using any JavaScript framework. This is useful for mutating data from your app into your BaseHub Repo.

You can check out its usage in the [GraphiQL Explorer](https://docs.basehub.com/api-reference/graphql-api/explorer) linked to your schema.

## Methods

The `mutation` API works a bit different to the `query` API due to how GraphQL is designed. `basehub().mutation()` has other methods to add data into BaseHub, the most important one being [transaction](https://docs.basehub.com/api-reference/javascript-sdk/basehub-client/mutation/transaction).