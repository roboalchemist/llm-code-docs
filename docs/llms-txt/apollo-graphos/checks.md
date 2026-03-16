# Source: https://www.apollographql.com/docs/graphos/platform/schema-management/checks.md

# Schema Checks

Certain changes to your graph's schema, such as removing a field or type, might break one of your application's clients.
GraphOS *schema checks* help you identify breaking changes before you make them. They can also help you identify when a potentially dangerous change is, in fact, safe.

You run schema checks using the Rover CLI and can integrate checks into your CI pipeline for automated validation of each schema change.
GraphOS Studio displays check results, helping you make informed decisions about evolving your graph.

Each schema check run consists of several check types or *tasks*.
By default, [build, operations, and linter checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks.md#types-of-checks) are included in each schema check run.
[Custom, proposals, and contract checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks.md#types-of-checks) require an [Enterprise plan](https://www.apollographql.com/pricing?referrer=docs-content).

All other schema checks are free as part of all Apollo plans.

## Types of checks

GraphOS can perform the following types of schema checks:

Check Type
Description

#### Build checks

For supergraphs, verify whether proposed changes to a subgraph
schema successfully compose with other subgraph schemas. Also known as *composition checks*.

#### Operations checks

Compare proposed schema changes against historical operations to
verify whether the changes break any of your graph's active clients.

#### Linter checks

Analyze proposed schema changes for violations of formatting rules
and other GraphQL best practices.

#### Custom checks

(Enterprise only)

Run custom validations using your own validation service.

#### Proposals checks

(Enterprise only)

Check whether your proposed schema changes have matching and approved [schema proposals](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals).

#### (Downstream) contract checks

(Enterprise only)

When running schema checks on a source variant, check whether your
proposed schema changes break any downstream [contract](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/contracts/overview) variants.

This article provides further details on build and operations checks.

* For details on linter checks, see [Schema linting](https://www.apollographql.com/docs/graphos/platform/schema-management/linting).
* For details on custom checks, see [Custom checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks/custom).
* For details on proposals checks, see [Schema proposals check configuration](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals/configure#configure-schema-checks).
* For details on contract checks, see [Contract checks](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/contracts/create/#run-contract-checks).

### Build checks

When you run a schema check, GraphOS performs a *build check* before performing any other checks. A build check verifies that changes you make to a subgraph schema are valid GraphQL definitions and are compatible with your other subgraph schemas, enabling them to [compose](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/composition) into a supergraph schema for your router. For that reason, build checks are sometimes called composition checks.

If a build check fails, GraphOS performs no other checks for the provided schema.

### Operations checks

If a build check succeeds, GraphOS then validates schema changes with *operations checks*. Operations checks use your graph's historical client operation data to determine whether any clients would be negatively affected by the proposed schema changes. For example, an operations check would flag a change that removes a field that multiple clients use in their operations.

## Limitations

### Operations check cardinality

Operations checks run against a maximum of 10,000 distinct operations. GraphOS Studio displays an error when a larger cardinality has been reached.

#### Cardinality mitigation

To minimize the operation cardinality you can:

* Decrease the **time range** historical operations are drawn from
* Increase the minimum number of times an operation must have run to be included
* Remove some **included variants** from the operations check
* Add **excluded clients**
* Add **excluded operations**

Graph admins can change these settings in [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content) for a particular graph or variant in the graph's **Settings** > **Checks** > **Operations** section.

For example, decreasing the time range from the default (**Within last week**) to **Within the last three days** or increasing the minimum number of times the operation ran from the default (**1**) to **5** should decrease the operation cardinality.

### Input field usage reporting

This limitation only applies to reporting metrics from Apollo Server and older versions of the Apollo Router Core.

If you use the GraphOS Router to [report operation metrics](https://www.apollographql.com/docs/graphos/platform/insights/sending-operation-metrics), you can configure [enhanced operation signature normalization](https://www.apollographql.com/docs/graphos/reference/router/configuration/#enhanced-operation-signature-normalization) and [extended reference reporting](https://www.apollographql.com/docs/graphos/reference/router/configuration/#extended-reference-reporting) to track input field usage.

GraphOS tracks operation usage. To deduplicate operations, Apollo uses [operation signatures](https://www.apollographql.com/docs/graphos/platform/insights/operation-signatures) to denormalize the arguments and inputs. However, operation signatures don't track which fields on input types are used.

For example, by default, GraphOS doesn't track how many times the input field `GetUsersInput.firstName` is used in this schema:

```graphql
type Query {
  getUsers(filters: GetUsersInput): [User]
}

input GetUsersInput {
  firstName: String
  lastName: String
}

type User {
  id: ID!
  firstName: String!
  lastName: String!
}
```

## Next steps

To learn how to run your first schema check and integrate checks into your CI pipeline, refer to [Run Schema Checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks/run).
You can also [connect schema checks to GitHub](https://www.apollographql.com/docs/graphos/platform/schema-management/checks/github-integration) to add links to check results on the pull requests that initiate them.
For a guide on configuring checks, see [Check Configurations](https://www.apollographql.com/docs/graphos/platform/schema-management/checks/configure).
See the [Checks Reference](https://www.apollographql.com/docs/graphos/platform/schema-management/checks/reference) for the types of schema changes that checks detect.
