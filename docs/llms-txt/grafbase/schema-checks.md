# Source: https://grafbase.com/docs/platform/schema-checks.md

# Schema Checks

The Schema Registry runs a suite of checks on a schema.

You can check a subgraph schema before publishing to a federated graph.

Run Schema Checks with the `grafbase check` command. Read more in the [reference documentation](https://grafbase.com/docs/cli/commands/check.md).

A successful check returns a successful exit code (0).

Check errors return a non-zero exit code and print the errors, making the command suitable for scripts and CI pipelines.

## Workflow

When you run `grafbase check`, the Schema Registry:

1. Gathers all subgraph schemas for the branch
2. Validates each schema as a valid GraphQL schema
3. Composes all subgraph schemas together with the new version of the checked subgraph

The Schema Check fails if errors occur in steps 2 or 3.

## Operation Checks

APIs evolve. Most changes add functionality: new mutations, fields on types, or input objects for filtering collections. You can make these changes safely without breaking API consumers.

Other changes break clients using queries written for previous API versions. Common examples include removing fields or adding required field arguments. These changes disrupt service because GraphQL servers reject invalid queries that don't match the current schema.

Operation Checks help prevent breaking changes to your GraphQL schema. They provide rules that surface breaking changes as errors when you run `grafbase check`.

Breaking changes must meet two criteria:

- The change breaks existing functionality. See [list of breaking changes](#list-of-breaking-changes).
- Clients actively use the changed or removed schema parts.

Without the second criterion, Operation Checks would prevent schema iteration even for unused parts. Operation checks analyze request data to focus on actual API usage rather than theoretical breaking changes.

### Configuration

Configure Operation Checks in the dashboard as an opt-in feature.

![Operation Checks configuration screen](/images/docs/operation-checks-configuration-screen.png)

Enable checks for your entire graph or specific branches. Select query thresholds and timeframes for schema usage analysis.

Exclude operations by name. For example, this GraphQL document names the operation "JapaneseProducts":

```graphql
query JapaneseProducts {
  products(filter: { madeIn: "JP" }) {
    id
    name
  }
}
```

Exclude specific clients by identifying them through the `x-grafbase-client-name` header. Include this header in any GraphQL client.

### Running Operation Checks

The `grafbase check` command runs Operation Checks with other schema checks. Errors indicate breaking changes that would occur when deploying the new schema. The system analyzes real client usage data from the target branch.

### List of breaking changes

This list shows potentially breaking changes:

- Removal of a root query, mutation or subscription type.
- Removal of an object, interface or input object field.
- Removal of a field argument.
- Removal of an interface from `implements`.
- Removal of a member type in a union.
- Removal of a value of an enum.
- Addition of a nonnullable argument on a field.
- Addition of a nonnullable field on an input object.
- Change of a field's type.
  - Either change of the _inner_ type: `String` becoming `Int` for example,
  - or a change of wrapping types making the field nullable: `String!` to `String` or `[String!]` to `[String]` for example. The client would not expect null here.
- Change of a field argument's type.
  - Either change of the _inner_ type: `String` becoming `Int` for example,
  - or a change of wrapping types making the argument nonnullable: `String` to `String!` or `[String]` to `[String!]` for example. The client could be passing null.
- Removal of a field argument's default, if the argument is required.

We check actual usage before returning Operation Check errors. For example, the removal of a field will only be breaking if a field has actually been used by clients in the configured time window.

## Lint Checks

Lint checks analyze your schema to find potential issues like mistakes, oversights or disallowed behaviors that don't cause hard compilation errors.

### Lint Rules

- Naming conventions
  - Types: `PascalCase`
    - Forbidden prefixes: `"Type"`
    - Forbidden suffixes: `"Type"`
  - Fields: `camelCase`
  - Input values: `camelCase`
  - Arguments: `camelCase`
  - Directives: `camelCase`
  - Enums: `PascalCase`
    - Forbidden prefixes: `"Enum"`
    - Forbidden suffixes: `"Enum"`
  - Unions
    - Forbidden prefixes: `"Union"`
    - Forbidden suffixes: `"Union"`
  - Enum values: `SCREAMING_SNAKE_CASE`
  - Interfaces
    - Forbidden prefixes: `"Interface"`
    - Forbidden suffixes: `"Interface"`
  - Query fields
    - Forbidden prefixes: `["query", "get", "list"]`
    - Forbidden suffixes: `"Query"`
  - Mutation fields
    - Forbidden prefixes: `["mutation", "put", "post", "patch"]`
    - Forbidden suffixes: `"Mutation"`
  - Subscription fields
    - Forbidden prefixes: `"subscription"`
    - Forbidden suffixes: `"Subscription"`
- Usage of the `@deprecated` directive requires specifying the `reason` argument

### Where Lints Run

- The CLI runs lint checks through `grafbase check` or in the dashboard after passing validation and composition checks
- Run lint checks locally on SDL schemas with the `grafbase lint` command

## Proposal Checks

Proposal checks enforce that all changes in the checked schema — compared to the currently published schema — are part of an approved [schema proposal](https://grafbase.com/docs/platform/schema-proposals.md). The changes must not exactly match a given proposal, they only have to be part of any approved proposal. That means a given check or publish can implement in parts on in entirety one or more proposals. The check is based on semantic diffs between the checked schema and the relevant approved proposals.

Proposal checks are opt-in. You can enable them in the dashboard's Graph settings page.

### Example

```bash
$ grafbase check --schema products.graphql --name products grafbase/fed-demo@main
Grafbase CLI 0.82.3

⏳ Checking...

Errors were found in your schema check:

Proposal checks

❌ [Error] No approved schema proposal contains the field `name` in the new object type `Seller`
```

## Custom Checks

Custom checks extend Grafbase's built-in schema validation capabilities with your own business logic and validation rules. They run alongside standard schema checks and can enforce organization-specific standards, domain-specific rules, or integrate with other systems to validate your GraphQL schemas.

The errors and warnings from custom checks are part of the schema check results, just like the results of built-in schema checks.

### Example use cases for Custom Checks

- Enforcing naming conventions beyond built-in lint rules
- Validating domain-specific constraints (e.g., certain fields must always appear together)
- Ensuring compliance with your organization's API design guidelines
- Integrating with other systems to validate business logic
- Preventing anti-patterns specific to your implementation

### Implementation approach

Custom checks are implemented as webhooks that receive information about the subgraph schema being checked. You can build these webhooks using any language or framework and host them on your own infrastructure or serverless platforms.

To add a custom check, you must provide a webhook that will receive an event every time schema checks are run, and return an OK response with a potentially empty list of errors and warnings. These webhooks can be synchronous or asynchronnous.

### Synchronous Custom Checks

Synchronous custom checks respond immediately with validation results. These are ideal for quick validations that don't require extensive processing.

The webhook will receive an event with following JSON body shape:

```typescript
type SyncWebhookEvent = {
    graph_id: string
    branch_id: string
    git: {
      commit_url: string | null
      commit_message: string | null
      commit_sha: string | null
      branch_name: string | null
      author: string | null
    }
    subgraph: {
      name: string
      schema: string // full GraphQL schema being checked
    }
}
```

The webhook must return a JSON response with a 200 HTTP status code and a body following this schema:

```typescript
type SyncWebhookResponse = {
    diagnostics: Diagnostic[]
}

type Diagnostic = {
  message: string
  severity: "ERROR" | "WARNING"
}
```

If the webhook fails to respond in less than 12 seconds, or it responds with a
non-200 exit code, the custom check will be considered failing.

An empty `diagnostics` array corresponds to a successful check.

The errors and warnings will be part of the the check's results. Any failure to return a response with a 200 status and a valid body will also be an error in the check results, making the check fail.


#### Example sync custom check webhook implementation

```typescript
const express = require('express');
const { parse, visit } = require('graphql');
const app = express();
app.use(express.json());

app.post('/custom-check', (req, res) => {
  const { subgraph } = req.body;
  const diagnostics = [];

  try {
    const parsedSchema = parse(subgraph.schema);
    const inputTypes = new Set();
    const mutationFields = [];

    // Collect all input types
    visit(parsedSchema, {
      InputObjectTypeDefinition(node) {
        inputTypes.add(node.name.value);
      }
    });

    // Check mutation fields
    visit(parsedSchema, {
      ObjectTypeDefinition(node) {
        if (node.name.value === 'Mutation') {
          node.fields.forEach(field => {
            mutationFields.push(field.name.value);

            // Check if there's a corresponding input type
            const expectedInputName = `${field.name.value}Input`;
            if (!inputTypes.has(expectedInputName)) {
              diagnostics.push({
                message: `Mutation "${field.name.value}" should have a corresponding input type "${expectedInputName}"`,
                severity: "WARNING"
              });
            }
          });
        }
      }
    });

    res.json({ diagnostics });
  } catch (error) {
    res.status(500).json({
      diagnostics: [{
        message: `Failed to analyze schema: ${error.message}`,
        severity: "ERROR"
      }]
    });
  }
});

app.listen(3000, () => console.log('Custom check webhook running on port 3000'));
```

### Asynchronous Custom Checks

Asynchronous custom checks are designed for more complex validations that may take longer to process or require integration with other systems.

> **Coming soon:** Asynchronous custom checks are currently in development. If you have specific use cases that would benefit from async custom checks, please contact us to become a design partner and help shape this feature.

### Configuring custom checks

Once you have implemented and exposed the webhook, you can enter its url in the Settings tab of your graph in the Grafbase dashboard:

After implementing your webhook:

1. Navigate to the Settings tab of your graph in the Grafbase dashboard
2. Find the "Custom Checks" section
3. Enter your webhook URL
4. Add any headers that your webhook expects

![Custom Checks configuration in dashboard](/images/docs/schema-checks/custom-checks-configuration.png)

## Dashboard

View past schema checks in the `Checks` tab of the Grafbase dashboard.

![Schema Checks tab in the dashboardd](/images/docs/schema-checks/schema-checks-view.png)

## Using `grafbase check` in CI

_If you use GitHub Actions for CI, there is a pre-packaged and documented [grafbase-schema-check action](https://github.com/marketplace/actions/grafbase-schema-check-action) that uses the same approach as the description below._.

Use the command in scripts by providing the same arguments as interactive use.

Authentication differs from interactive use. Instead of the `grafbase login` flow, provide a Grafbase access token. Generate tokens in the dashboard:

![Access tokens view in the dashboard](/images/docs/schema-checks/access-tokens-view.png)

The `grafbase introspect --dev` command generates GraphQL schema files for the `--schema` argument of `grafbase check`. See examples in the [GitHub workflow](https://github.com/tomhoule/grafbase-schema-check-action-single-graph-example/blob/main/.github/workflows/check.yml) of the [example repository](https://github.com/tomhoule/grafbase-schema-check-action-single-graph-example/tree/main). A [federated graph example](https://github.com/tomhoule/grafbase-schema-check-action-federated-graph-example) is also available.