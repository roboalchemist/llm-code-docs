# Source: https://developers.buffer.com/examples/create-idea.md

Create an idea post for a specified Organization, using the provided content.

```graphql
mutation CreateIdea {
  createIdea(input: {
    organizationId: "some_organization_id",
    content: {
      title: "New Idea from GraphQL API"
      text: "This is the text of the new idea created via the GraphQL API."
    }
  }) {
    ... on Idea {
      id
      content {
        title
        text
      }
    }
  }
}
```
