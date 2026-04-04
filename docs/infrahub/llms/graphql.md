# Source: https://docs.infrahub.app/topics/graphql.md

# GraphQL

The GraphQL interface is the main interface to interact with Infrahub. The GraphQL schema is automatically generated based on the core models and the user-defined schema models.

The endpoint to interact with the main branch is accessible at `https://<host>/graphql`. To interact with a branch the URL must include the name of the branch, such as `https://<host>/graphql/<branch_name>`. If you need to extract the current GraphQL schema in your environment you can issue an HTTP get request to:

* `https://<host>//schema.graphql`
* `https://<host>//schema.graphql?branch=some-other-branch`

## Introduction to GraphQL videos[​](#introduction-to-graphql-videos "Direct link to Introduction to GraphQL videos")

This short demo shows how to use the GraphQL query interface to explore and read data from Infrahub. It walks through how to open the built-in GraphQL interface and run your first queries.

This video demonstrates how to use filters and relationships in GraphQL to find specific information, such as IP addresses for a particular device, using the Infrahub query interface.

## Query & mutations[​](#query--mutations "Direct link to Query & mutations")

In GraphQL, a query is used to fetch data and mutations are use to create/update or delete data. In Infrahub, a GraphQL query and 4 mutations will be generated for each model you define in the schema. The name of the query or mutation is based on the namespace and name of the model.

For example, for the model `CoreRepository` the following query and mutations have been generated:

* `Query` : **CoreRepository** to fetch `CoreRepository` nodes from Infrahub
* `Mutation` : **CoreRepositoryCreate** to create a `CoreRepository` node
* `Mutation` : **CoreRepositoryUpdate** to update an existing `CoreRepository` node
* `Mutation` : **CoreRepositoryUpsert** to create or update a `CoreRepository` node
* `Mutation` : **CoreRepositoryDelete** to delete a `CoreRepository` node

### Query format[​](#query-format "Direct link to Query format")

The top level query for each model will always return a list of objects and the query will have the following format `CoreRepository` > `edges` > `node` > `display_label`

```
query {
  CoreRepository {            # PaginatedCoreRepository object
    count
    edges {                 # EdgedCoreRepository object
      node {                # CoreRepository object
        id
        hfid
        display_label
        __typename
      }
    }
  }
}
```

info

All list of objects will be nested under `edges` & `node` to make it possible to control the pagination and access the attribute `count`.

#### `ID`, `hfid` and `display_label`[​](#id-hfid-and-display_label "Direct link to id-hfid-and-display_label")

For all nodes, the attribute `id`, `hfid` and `display_label` are automatically available.

The value used to generate the `display_label` can be defined for each model in the schema. If no value has been provided a generic display label with the kind and the ID of the Node will be generated.

The value used to generate the `hfid` can be defined for each model in the schema. If no value has been provided and the `model` has a single uniqueness constraint defined, then the `hfid` will be automatically generated from the uniqueness constraint.

At the object level, there are mainly 3 types of resources that can be accessed, each with a different format:

* `Attribute`
* `Relationship` of `Cardinality One`
* `Relationship` of `Cardinality Many`

#### Attribute[​](#attribute "Direct link to Attribute")

Each attribute is its own object in GraphQL to expose the value and all the metadata.

In the query below, to access the attribute **name** of the object the query must be `CoreRepository` > `edges` > `node` > `name` > `value`. At the same level all the metadata of the attribute are also available, for example: `is_protected`, `source` & `owner`

Example query to access the value and the properties of the attribute 'name'

```
query {
  CoreRepository {
    count
    edges {
      node {
        name {              # TextAttribute object
          value
          is_protected
          source {
            id
            display_label
          }
        }
      }
    }
  }
}
```

#### Relationship of `Cardinality One`[​](#relationship-of-cardinality-one "Direct link to relationship-of-cardinality-one")

A relationship to another model with a cardinality of `One` will be represented with a `NestedEdged` object composed of a `node` and a `properties` objects. The `node` gives access to the remote `node` (the peer of the relationship) while `properties` gives access to the properties of the relationship itself.

Example query to access the peer and the properties of the relationship 'account', with a cardinality of one.

```
query {
  CoreRepository {
    count
    edges {
      node {
        account {
          properties {
            is_protected
            source {
              id
              display_label
            }
          }
          node {
            display_label
            hfid
            id
          }
        }
      }
    }
  }
}
```

#### Relationship of `Cardinality Many`[​](#relationship-of-cardinality-many "Direct link to relationship-of-cardinality-many")

A relationship with a cardinality of `Many` will be represented with a `NestedPaginated` object composed. It was the same format as the top level `PaginatedObject` with `count` and `edges` but the child element will expose both `node` and `properties`. The `node` gives access to the remote `node` (the peer of the relationship) while `properties` gives access to the properties of the relationship itself.

Example query to access the relationship 'tags', with a cardinality of Many.

```
query {
  CoreRepository {
    count
    edges {
      node {
        tags {                      # NestedPaginatedBuiltinTag object
          count
          edges {                   # NestedEdgedBuiltinTag object
            properties {
              is_protected
              source {
                id
              }
            }
            node {
              display_label
              hfid
              id
            }
          }
        }
      }
    }
  }
}
```

### Mutations format[​](#mutations-format "Direct link to Mutations format")

The format of the mutation to `Create`, `Update` and `Upsert` an object has some similarities with the query format. The format will be slightly different for:

* An `Attribute`
* A relationship of `Cardinality One`
* A relationship of `Cardinality Many`

#### Create, update and upsert[​](#create-update-and-upsert "Direct link to Create, update and upsert")

To `Create`, `Update` or `Upsert` an object, the mutations will have the following properties.

* The input for the mutation must be provided inside `data`.
* All mutations will return `ok` and `object` to access some information after the mutation has been executed.
* `Update` mutations require you to provide an `id` or `hfid` to identify the object you want to update.
* `Upsert` mutations do not require you to provide the `id` or the `hfid`, but enough information needs to be provided for the back-end to uniquely identify the node. Typically this means that all the attribute or relationship values need to be provided that make up the `hfid` or `uniqueness_constraints` of the node.

```
mutation {
  CoreRepositoryCreate(
    data: {
      name: { value: "myrepop" },           # Attribute
      location: { value: "myrepop" },       # Attribute
      account: { hfid: ["my_account"] },         # Relationship One
      tags: [ { hfid: ["my_tag"] } ]}            # Relationship Many
  ) {
    ok
    object {
      id
      hfid
    }
  }
}
```

#### Delete[​](#delete "Direct link to Delete")

For a `Delete` mutation, we have to provide the `id` or the `hfid` of the node as part of the `data` argument.

```
mutation {
  CoreRepositoryDelete(data: {hfid: ["myrepo"]}) {
    ok
  }
}
```

## Branch management[​](#branch-management "Direct link to Branch management")

In addition to the queries and the mutations automatically generated based on the schema, there are some queries and mutations to interact with the branches.

* **Query**: `Branch`, Query a list of all branches
* **Mutation**: `BranchCreate`, Create a new branch
* **Mutation**: `BranchUpdate`, Update the description of a branch
* **Mutation**: `BranchDelete`, Delete an existing branch
* **Mutation**: `BranchRebase`, Rebase an existing branch with the main branch
* **Mutation**: `BranchMerge`, Merge a branch into main
* **Mutation**: `BranchValidate`, Validate if a branch has some conflicts

## Stored GraphQL queries in the database[​](#stored-graphql-queries-in-the-database "Direct link to Stored GraphQL queries in the database")

The `GraphQLQuery` model has been designed to store a GraphQL query in order to simplify its execution and to associate it with other internal objects like `Transformation`.

A `GraphQLQuery` object can be created via the web interface, the API or it can be imported from a Git repository.

Every time a `GraphQLQuery` is created or updated, the content of the query will be analyzed to:

* Ensure the query is valid and compatible with the schema.
* Extract some information about the query itself (see below).

### Information extracted from the query[​](#information-extracted-from-the-query "Direct link to Information extracted from the query")

* Type of operations present in the Query \[Query, Mutation, Subscription]
* Variables accepted by the query
* Depth, number of nested levels in the query
* Height, total number of fields requested in the query
* List of Infrahub models referenced in the query

### Import from a Git repository[​](#import-from-a-git-repository "Direct link to Import from a Git repository")

GraphQL queries could be defined in file(s) with a `.gql` extension in a remote repository. Then queries must also be explicitly identified in the `.infrahub.yml` file under `queries`.

More details on the `.infrahub.yml` file format can be found in [.infrahub.yml topic](/topics/infrahub-yml.md).

### Executing stored GraphQL queries[​](#executing-stored-graphql-queries "Direct link to Executing stored GraphQL queries")

Stored GraphQL queries can be executed by using the `/api/query/{query_id}` REST API endpoint. The `{query_id}` can be the name or the id of the `GraphQLQuery` node in the database. More information can be found in the [Swagger documentation](http://localhost:8000/api/docs).

## Working with groups in GraphQL[​](#working-with-groups-in-graphql "Direct link to Working with groups in GraphQL")

[Groups](/topics/groups.md) are first-class objects in Infrahub that can be queried and manipulated through GraphQL. Groups provide powerful ways to organize and operate on collections of infrastructure objects.

### Querying groups and their members[​](#querying-groups-and-their-members "Direct link to Querying groups and their members")

Query a specific group and its members:

```
query {
  CoreStandardGroup(name__value: "ProductionRouters") {
    edges {
      node {
        name {
          value
        }
        members {
          edges {
            node {
              display_label
              __typename
            }
          }
        }
      }
    }
  }
}
```

### Finding groups for an object[​](#finding-groups-for-an-object "Direct link to Finding groups for an object")

Every object automatically gains relationships to find its group memberships:

```
query {
  InfraDevice(name__value: "router01") {
    edges {
      node {
        name {
          value
        }
        member_of_groups {
          edges {
            node {
              name {
                value
              }
            }
          }
        }
      }
    }
  }
}
```

### Query groups for bulk operations[​](#query-groups-for-bulk-operations "Direct link to Query groups for bulk operations")

Groups enable efficient bulk queries across related objects:

```
query {
  CoreStandardGroup(name__value: "EdgeDevices") {
    edges {
      node {
        members {
          edges {
            node {
              ... on InfraDevice {
                interfaces {
                  edges {
                    node {
                      name {
                        value
                      }
                      ip_addresses {
                        edges {
                          node {
                            address {
                              value
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

This pattern enables powerful operations where you can process all objects in a group with a single query, making groups essential for scalable infrastructure management.

See [organizing objects with groups](/guides/groups.md) for creating and managing groups, and [understanding groups](/topics/groups.md) for architectural concepts.
