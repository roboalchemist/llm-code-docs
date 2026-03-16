# Source: https://www.apollographql.com/docs/graphos/platform/graph-management/variants.md

# Add and Manage Variants

Most graphs run in more than one environment—for example, development, staging, and production.
In GraphOS, environments correspond to *variants*. Thus, every graph in GraphOS has one or more variants.
Each variant has its own schemas, along with its own change history and metrics.

Supergraph variants each have their own router.
Different variants of the same super graph can even have completely different sets of subgraphs:

This helps you test adding new subgraphs or removing existing ones in non-production environments.

Whenever you interact with a GraphOS interface—whether Studio, the Rover CLI, or Platform API—you must specify the variant you're working with via a graph ref.

## Add a variant

All graphs in GraphOS start with one variant named `@current` by default.
You can add a new variant to your existing GraphOS supergraph in the following ways:

* [In GraphOS Studio](https://www.apollographql.com/docs/graphos/platform/graph-management/variants.md#add-a-variant-in-graphos-studio) (cloud supergraphs only)
* [Via the Rover CLI](https://www.apollographql.com/docs/graphos/platform/graph-management/variants.md#add-a-variant-via-the-rover-cli)

### Add a variant in GraphOS Studio

This method of adding a variant is available only to cloud supergraphs. For other graph types, see [Adding a variant via the Rover CLI](https://www.apollographql.com/docs/graphos/platform/graph-management/variants.md#add-a-variant-via-the-rover-cli)

1. Go to your supergraph's **Settings** page in Studio and navigate to **This Graph > Variants**.

2. Click **Add a variant**.

3. In the dialog that appears, provide a **Variant Name** and click **Continue**.

4. Provide your first subgraph's **Routing URL** (this is the URL that your new variant's router will use to communicate with the subgraph), along with a **Subgraph Name**.

   * Creating a new supergraph variant always requires also creating the first subgraph for that variant.

5. If Studio can't fetch your subgraph's schema automatically from the routing URL, click **Advanced options** to provide the schema another way (such as by pasting the schema directly or introspecting a locally running server).

6. Click **Add a new variant**. When the action completes, your new variant is listed on your organization's homepage in Studio.

### Add a variant via the Rover CLI

To add a new variant to your supergraph with Rover, you publish its first subgraph's schema. To do this, you use the exact same Rover command as [publishing a subgraph](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/publish#publish-subgraph-schemas). The only difference is that you provide the name of the new variant to the command.

## Variant management

All organizations can enable public access for individual variants of your graph. Enterprise organizations can designate particular variants of a graph as protected variants to limit contributor access.

### Public variants

Anyone with that variant's public link can view the following pages for that variant in Studio:

* Home
  * This shows the variant's README.
* Schema
* Explorer
  * You can also [embed the Explorer](https://www.apollographql.com/docs/graphos/platform/explorer/embed) on your own webpage.

This enables consumers of your graph to learn about your graph's schema and any special usage information (such as authentication details) that you've documented in the public variant's README. They can also run properly authenticated operations against your graph with the Explorer.

People outside your organization can't view any other pages for a public variant (Fields, Operations, etc.), and they can never view any pages for private variants. New variants always start as private.

#### Making a variant public

Only organization members with the [**Org Admin** or **Graph Admin** role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles) can toggle a variant's public visibility.

1. Go to your variant's **Settings** page and open the **This Variant** tab.
2. Under **Danger Zone**, find the **Public** card and click **Change**.
3. Toggle your selection and click **Save**.

You can toggle the switch back to **Off** to make the variant private again.

After you make a variant public, you can click the variant's **PUBLIC** label at the top of GraphOS Studio to get its public link:

### Protected variants (Enterprise only)

If you have a [GraphOS Enterprise plan](https://www.apollographql.com/pricing?referrer=docs-content), you can designate particular variants of a graph as *protected variants*. A protected variant limits the capabilities of users with the [**Contributor** role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles) to make certain changes to the variant:

* **Contributors** cannot push schema updates to a protected variant.
* **Contributors** cannot manage Explorer-related settings for a protected variant, such as setting the variant's endpoint URL.
* Graph API Keys with the **Contributor** role cannot report usage metrics for a protected variant.

**Graph Admins** and **Org Admins** can configure whether a variant is protected from the **This Variant** tab of the variant's Settings page.

## Next steps

To learn CI/CD best practices and examples for using variants for multiple deployment environments refer to the [Graph Environment Best Practices](https://www.apollographql.com/docs/graphos/platform/graph-management/environment-best-practices) guide.
