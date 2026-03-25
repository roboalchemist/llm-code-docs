# Source: https://www.apollographql.com/docs/graphos/platform/schema-management/linting.md

# Schema Linting

GraphOS provides *schema linting* to help you enforce formatting conventions and other GraphQL best practices with every proposed change to your graph's schema.

* If you set up [schema checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks) for your graph, linting runs as a separate check type alongside build and operation checks.
* You can also perform [one-off linting with the Rover CLI](https://www.apollographql.com/docs/graphos/platform/schema-management/linting.md#one-off-linting-with-the-rover-cli).

GraphOS schema linting only analyzes parts of your modified schema that differ from your published schema. It does not flag any existing violations.

## Linter configuration

The GraphOS schema linter uses a [predefined collection of rules](https://www.apollographql.com/docs/graphos/platform/schema-management/linting/rules) to identify issues with proposed schema changes.
The predefined collection includes [schema composition](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/composition) rules. The graph-wide linter defaults you define apply to all variants of a particular graph.

To navigate to your linter configuration:

1. In [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content), go to your graph's **Checks** page.
2. Click **Configuration** in the upper right to open the checks configuration page.
3. From the checks configuration page, open the **Linter** section.

This page organizes linter options into the following categories:

* **General Linter Configuration** provides high-level options, including disabling the linter entirely.
* **Approved `@tag` names** enables you to specify approved values for the `name` argument of the `@tag` directive. This directive is used most commonly with [GraphOS contracts](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/contracts/overview).
  * If you don't use the `@tag` directive, you can ignore this category.
  * Using a non-approved value for `name` raises the [`TAG_DIRECTIVE_USES_UNKNOWN_NAME`](https://www.apollographql.com/docs/graphos/platform/schema-management/linting/rules#tag_directive_uses_unknown_name) violation.
* **Rule Severity Configuration** enables you to [set the severity level](https://www.apollographql.com/docs/graphos/platform/schema-management/linting.md#setting-severity-levels) for violations of each rule.

If you view this configuration for a single variant, each category displays a **Use Graph Settings** toggle in the upper right. If this toggle is enabled, the variant uses whatever graph-wide defaults are set for that category. At this time, the **Use Graph Settings** toggle is always enabled for all variants.

### Setting severity levels

The **Rules Severity Configuration** category of your linter configuration displays all predefined rules and the current **severity** level for each. Click a rule's severity to set it to any of the following:

* **Error**: Any violation of this rule causes the associated linter check to fail.
  * This in turn causes the entire schema checks run to fail, which is useful for failing builds in CI.
* **Warn**: Violations of this rule are flagged in checks reports, but they don't cause the associated linter check to fail.
* **Ignore**: Violations of this rule are ignored entirely.

For information on specific rules, see the [reference list of rules](https://www.apollographql.com/docs/graphos/platform/schema-management/linting/rules).

## Running the linter

Schema linting runs automatically as part of your graph's [schema checks](https://www.apollographql.com/docs/graphos/platform/schema-management/linting.md#linting-via-schema-checks). You can also perform [one-off linting](https://www.apollographql.com/docs/graphos/platform/schema-management/linting.md#one-off-linting) of local schema changes via the Rover CLI.

### Linting via schema checks

If you set up [schema checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks) for your graph, schema linting automatically runs as a separate check type alongside build and operation checks. You can view the results of all check types from your graph's **Checks** page in Studio.

For the best experience running linter checks, install v0.16 or later of the Rover CLI. Earlier versions of Rover can't correctly output the results of linter checks, but they do correctly exit with a nonzero code if a linter check fails.

### One-off linting

One-off linting requires v0.16 or later of the Rover CLI. [Install the latest version.](https://www.apollographql.com/docs/rover/getting-started)

The Rover CLI provides `subgraph lint` and `graph lint` commands for running the GraphOS linter against your local schema changes.

* Use `subgraph lint` for subgraphs in a supergraph.
* Use `graph lint` for [monographs](https://www.apollographql.com/docs/graphos/get-started/concepts/graphs/#monographs).

The `rover subgraph lint` and `rover graph lint` commands validate all [linter rules](https://www.apollographql.com/docs/graphos/platform/schema-management/linting/rules) except for [composition rules](https://www.apollographql.com/docs/graphos/platform/schema-management/linting/rules#composition-rules). Use [`rover subgraph check`](https://www.apollographql.com/docs/rover/commands/subgraphs#subgraph-check) or [`rover supergraph compose`](https://www.apollographql.com/docs/rover/commands/supergraphs#supergraph-compose) to validate composition rules locally.

```bash title=Example command
rover subgraph lint --name products --schema ./products-schema.graphql my-graph@my-variant
```

The argument `my-graph@my-variant` in the example above is a graph ref that specifies the ID of the graph you're comparing your schema changes against, along with which variant you're comparing against.

Command options include:

Name
Description

###### `--schema`

**Required.** The path to a local `.graphql` or `.gql` file, in [SDL format](https://www.apollographql.com/docs/graphos/reference/glossary/#sdl).

Alternatively, you can provide `-`, in which case the command uses an SDL string piped to `stdin` instead (see [Using `stdin`](https://www.apollographql.com/docs/rover/conventions#using-stdin)).

###### `--name`

**Required** for `subgraph lint`. Omit for `graph lint`. The name of the published subgraph to compare schema changes against.

###### `--ignore-existing-lint-violations`

If provided, the linter only flags violations that are present in the diff between your local schema and your published schema.

By default, one-off linting flags all violations in your local schema.

## Linter rules

See this [reference list of rules](https://www.apollographql.com/docs/graphos/platform/schema-management/linting/rules).
