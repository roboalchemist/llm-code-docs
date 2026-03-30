# Source: https://developers.buffer.com/examples/get-organizations.md

Fetch all of the organizations that belong to the authenticated account.

```graphql
query GetOrganizations {
  account {
    organizations {
      id
      name
      ownerEmail
    }
  }
}
```