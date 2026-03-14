# Source: https://developers.activecampaign.com/reference/about-the-graphql-api.md

# About the GraphQL API

**Postman**

[Postman](https://www.postman.com/) is a platform for building and using APIs. ActiveCampaign provides Postman collections for various APIs to enable quicker and easier development. The eComm GraphQL API Postman collection can be accessed using the following link:

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style={{ width: "128px", height: "32px" }} />](https://www.postman.com/acdevrel/workspace/activecampaign-developer-relations/graphql-request/6543ea58b24dfe2df636c9ef)

**Authentication**

The eComm GraphQL API follows the [same method as the existing v3 REST API](https://developers.activecampaign.com/reference/authentication) using an API Key with an `Api-Token` HTTP header.

**Root endpoint**

The eComm GraphQL API has the [same base URL as the existing v3 REST API](https://developers.activecampaign.com/reference/url) but uses `/ecom/graphql` as the path to specify the API. Base URLs will vary, but the overall URL structure will look like:

`https://<your-account>.api-us1.com/api/3/ecom/graphql`

All calls should be made over HTTPS and the URL will remain the same for any operation.

**Rate Limits**

The eComm GraphQL API follows the [same rate limit restriction as the existing v3 REST API](https://developers.activecampaign.com/reference/rate-limits) of 5 requests per second per account.

**Introspection**

GraphQL supports [introspection](https://graphql.org/learn/introspection/) which mean you can query the API schema for documentation about itself. There are various queries you can run to return specific details of the API.

* The following query will return all types defined in the schema along with details of each:

```graphql
query {  
  __schema {  
    types {  
      name  
      kind  
      description  
      fields {  
        name  
      }  
    }  
  }  
}
```

* The following query will return the details of any specific type:

```graphql
query {  
  __type(name: "Order") {  
    name  
    kind  
    description  
    fields {  
      name  
    }  
  }  
}
```

* The following query will fully introspect the API:

```graphql
query IntrospectionQuery {  
      schema {  
        queryType { name }  
        mutationType { name }  
        subscriptionType { name }  
        types {  
          ...FullType  
        }  
        directives {  
          name  
          description  
          locations  
          args {  
            ...InputValue  
          }  
        }  
      }  
    }  
    fragment FullType on Type {  
      kind  
      name  
      description  
      fields(includeDeprecated: true) {  
        name  
        description  
        args {  
          ...InputValue  
        }  
        type {  
          ...TypeRef  
        }  
        isDeprecated  
        deprecationReason  
      }  
      inputFields {  
        ...InputValue  
      }  
      interfaces {  
        ...TypeRef  
      }  
      enumValues(includeDeprecated: true) {  
        name  
        description  
        isDeprecated  
        deprecationReason  
      }  
      possibleTypes {  
        ...TypeRef  
      }  
    }  
    fragment InputValue on InputValue {  
      name  
      description  
      type { ...TypeRef }  
      defaultValue  
    }  
    fragment TypeRef on Type {  
      kind  
      name  
      ofType {  
        kind  
        name  
        ofType {  
          kind  
          name  
          ofType {  
            kind  
            name  
            ofType {  
              kind  
              name  
              ofType {  
                kind  
                name  
                ofType {  
                  kind  
                  name  
                  ofType {  
                    kind  
                    name  
                  }  
                }  
              }  
            }  
          }  
        }  
      }  
    }
```