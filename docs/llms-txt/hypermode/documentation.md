# Source: https://docs.hypermode.com/dgraph/graphql/schema/documentation.md

# Documentation and Comments

> Dgraph accepts GraphQL documentation comments, which get passed through to the generated API and shown as documentation in GraphQL tools.

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

## Schema Documentation Processed by Generated API

Dgraph accepts GraphQL documentation comments (e.g.
`""" This is a graphql comment """`), which get passed through to the generated
API and thus shown as documentation in GraphQL tools like GraphiQL, GraphQL
Playground, Insomnia etc.

## Schema Documentation Ignored by Generated API

You can also add `# ...` comments where ever you like. These comments are not
passed via the generated API and are not visible in the API docs.

## Reserved Namespace in Dgraph

Any comment starting with `# Dgraph.` is **reserved** and **should not be used**
to document your input schema.

## An Example

An example that adds comments to a type as well as fields within the type would
be as below.

```graphql
"""
Author of questions and answers in a website
"""
type Author {
  # ... username is the author name , this is an example of a dropped comment
  username: String! @id
  """
  The questions submitted by this author
  """
  questions: [Question] @hasInverse(field: author)
  """
  The answers submitted by this author
  """
  answers: [Answer] @hasInverse(field: author)
}
```

It is also possible to add comments for queries or mutations that have been
added via the custom directive.

```graphql
type Query {
  """
  This query involves a custom directive, and gets top authors.
  """
  getTopAuthors(id: ID!): [Author]
    @custom(
      http: {
        url: "http://api.github.com/topAuthors"
        method: "POST"
        introspectionHeaders: ["Github-Api-Token"]
        secretHeaders: ["Authorization:Github-Api-Token"]
      }
    )
}
```

The screenshots below shows how the documentation appear in a GraphQL API
explorer.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/graphql/authors1.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=9afb9ac5533a14945806ba7e6d3b425c" alt="Schema Documentation On Types" width="641" height="512" data-path="images/dgraph/graphql/authors1.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/graphql/authors1.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=1a75b1ab60ffffe1e743a05518ce6810 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/graphql/authors1.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=80b1b8029f370cfeb5ac62d07843b394 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/graphql/authors1.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=34a940be402929a371de599203273d2e 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/graphql/authors1.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=553e2e7cda0873e237fcf7a916fcfb54 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/graphql/authors1.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=740e76b6eed37b7f7f625fa311ac9463 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/graphql/authors1.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=b8116197055b79b518179303bac00711 2500w" data-optimize="true" data-opv="2" />

Schema Documentation on Types

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/dgraph/graphql/CustomDirectiveDocumentation.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=249d5edc409e25a829fd8a9b46fc0398" alt="Schema Documentation On Custom Directive" width="649" height="235" data-path="images/dgraph/graphql/CustomDirectiveDocumentation.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/dgraph/graphql/CustomDirectiveDocumentation.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6991926a41537d561d0e43e72e15d719 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/dgraph/graphql/CustomDirectiveDocumentation.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=899b8bc90af553d49f2c680ecb64b3b6 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/dgraph/graphql/CustomDirectiveDocumentation.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=f897fe9f471ba7de2738a617fce250e1 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/dgraph/graphql/CustomDirectiveDocumentation.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3b7fade7f1f2be181dfb1c5c0dc612b4 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/dgraph/graphql/CustomDirectiveDocumentation.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=072890d411f3df72178f5edb09578628 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/dgraph/graphql/CustomDirectiveDocumentation.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=481c36d7e907e3151b875c1be8637e4d 2500w" data-optimize="true" data-opv="2" />
