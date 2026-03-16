# Source: https://www.apollographql.com/docs/graphos/platform/graph-management/manage-subgraphs.md

# Manage Subgraphs

Learn how to effectively manage subgraphs in GraphOS Studio.
This guide covers viewing subgraphs, modifying routing URLs, safely deleting subgraphs, and managing contact information and schema tagging for a well-organized supergraph.

## Viewing subgraphs

After you create a supergraph or new variant, you can view a list of its associated subgraphs from the variant's **Subgraphs** page, under the **Schema** section:

The list includes each subgraph's name and routing URL, along with type and field counts for each subgraph's schema.

### Viewing subgraph SDL

The **Schema > SDL** page in Studio displays the raw SDL for each schema type associated with your supergraph—an API schema, a supergraph schema, and subgraph schemas.

From this page, you can:

* View metadata about the composed supergraph, along with metadata about each subgraph (such its endpoint URL and most recent schema registration date)
* Identify which subgraphs define any type or field in your API and share a link with team members
* Search for types and fields
* Download a copy of your subgraph's SDL for local development
* Filter out comments and deprecated fields for improved scanning

Organization members with the [**Consumer** role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles) can only view the API schema. **Observers**, **Documenters**, **Contributors**, **Graph Admins**, and **Org Admins** can view all schema types.

### Viewing a field's originating subgraph

The **Schema > Reference** page in Studio displays a table of your supergraph's types and fields. This table includes a **Subgraph** column, which lists the subgraphs that define each type and field:

Clicking the subgraph link for a type or field takes you to the line where it's defined in the corresponding subgraph schema:

If you're using [the `@contact` directive](https://www.apollographql.com/docs/graphos/platform/graph-management/manage-subgraphs.md#contact-info-for-subgraphs) to specify owner contact information for your subgraphs, hovering over a subgraph name displays its contact information, enabling you to follow up with the appropriate team:

## Modifying a subgraph

From your variant's Subgraphs page, you can modify an existing subgraph's routing URL:

1. Open the **•••** menu for the subgraph you want to modify:

2. Click **Edit routing URL**.

3. In the dialog that appears, provide a new URL and click **Update**.
   * Your router automatically begins using the new URL to communicate with your subgraph.

If you need to make any other modifications to an existing subgraph, use the Rover CLI. [Learn about `rover subgraph` commands.](https://www.apollographql.com/docs/rover/commands/subgraphs)

## Deleting a subgraph

**Deleting a subgraph is dangerous!** Read this section fully before deleting a subgraph.

You can delete an existing subgraph from a variant of your cloud supergraph. If you do:

1. The variant automatically attempts to compose an updated supergraph schema using the schemas from all remaining subgraphs.

   * Studio displays the result of this attempt, and you can cancel the deletion if there are errors.

2. **If composition succeeds,** the variant's router automatically begins using the updated supergraph schema. This means clients can no longer query the router for fields that are defined only in the deleted subgraph.

   **If composition fails,** the router continues using its existing supergraph schema. This means clients can continue querying the router for fields from the deleted subgraph, until the remaining subgraph schemas are updated to compose successfully.

### Important considerations

* **Deleting a subgraph can break existing clients!** This action is equivalent to removing all the subgraph's types and fields from your supergraph (unless they're also defined in another subgraph). If a client sends an operation that includes any of those types and fields, the router will reject that operation.

  * To help you remove schema definitions safely, learn about [schema checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks).

* Deleting a subgraph in Studio has no effect on your actual running subgraph instance. It only removes your router's knowledge of that instance and its corresponding schema fields.

### Steps to delete within Studio

1. Go to the Subgraphs page for the subgraph's corresponding variant.

2. Click the **•••** button on the right of the subgraph you want to delete:

3. Click **Delete subgraph**. Studio attempts to compose a new supergraph schema that doesn't include the subgraph you want to delete.

4. A confirmation dialog appears that displays any composition errors that occurred. If you're sure you want to delete the subgraph, enter its name and click **Delete subgraph**.

## Contact info for subgraphs

You can use the `@contact` directive to add your team's contact info to a subgraph schema. This info is displayed in Studio, which helps other teams know who to contact for assistance with the subgraph:

The contact info includes a name (of a team or individual), along with an optional description and custom URL.

### Adding the `@contact` directive

To use the `@contact` directive in your subgraph schema, you first need to define the directive in your schema. Add the following definition to each of your subgraph schemas:

```graphql title=schema.graphql
"Annotate a schema with contact information for the subgraph owner"
directive @contact(
  "Contact title of the subgraph owner"
  name: String!
  "URL where the subgraph's owner can be reached"
  url: String
  "Other relevant notes can be included here; supports markdown links"
  description: String
) on SCHEMA
```

You can now apply the `@contact` directive to each subgraph schema's special `schema` object. If your schema doesn't already define this object, you can add it like so:

```graphql title=schema.graphql
extend schema
  @contact(
    name: "Acephei Server Team"
    url: "https://myteam.slack.com/archives/teams-chat-room-url"
    description: "send urgent issues to [#oncall](https://yourteam.slack.com/archives/oncall)."
  )
```

#### Supported `@contact` fields

Name /Type
Description

#### `name`

`String!`

**Required.** The name of the person, people, or team responsible for the subgraph.

#### `url`

`String`

The URL where the subgraph's owner can be reached. This might be the URL of a chat room or forum, or it could be an email address.

#### `description`

`String`

Provides any additional helpful details about working with this subgraph or contacting its owner.

This field supports Markdown-formatted links.

### Viewing contact info

After you publish a subgraph schema that includes the `@contact` directive, the contact information is included in the metadata shown in Studio's **Schema > SDL** tab:

In the **Schema > Reference** tab, you'll also see a contact card when you hover over the subgraph link of a type or field:

### Known `@contact` limitations

* To provide the `@contact` directive to Apollo, you must publish your subgraph schemas by providing a local `.graphql` file as the `--schema` option of [`rover subgraph publish`](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/publish/).
  * If you provide an introspection result to the command instead, the `@contact` directive is **not** included in that result.

## Schema tagging

In your subgraph schemas, you can use the `@tag` directive to tag a type or field with an arbitrary string value:

```graphql title=products.graphql
type Product {
  id: ID!
  name: String!
  codename: String! @tag(name: "internal")
}
```

By default, these tags are removed from the [API schema](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/schema-types/#api-schema) that's generated as part of composition. This means that tag information isn't visible to clients querying your supergraph.

If tag information should be visible to clients (for example, to help document your API), you can enable this for a variant in Studio with the following steps:

1. Go to the **Settings** page for your variant in GraphOS Studio.
2. On the **General** tab, click **Update Version** (if you're not on the latest minor version) or **Configure** at the top-right corner. The **Configure build pipeline** modal dialog appears.
3. Enable the toggle labeled **Show all uses of @tag directives to consumers in Schema Reference and Explorer**.
4. Click **Save**.

1) Go to the **Settings** page for your variant in GraphOS Studio.
2) On the **General** tab, click **Update Version** (if you're not on the latest minor version) or **Configure** at the top-right corner. The **Configure build pipeline** modal dialog appears.
3) Under **Directives**, enable the toggle for the `@tag` directive.
4) Click **Save**.

After you make your `@tag` directives visible, you can view them inline with both the Schema and Explorer tabs in Studio.

In the **Schema > Reference** tab, tags are shown inline with each type and field:
