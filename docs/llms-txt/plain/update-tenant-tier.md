# Source: https://www.plain.com/docs/graphql/tiers/update-tenant-tier.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.plain.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update tenant tier

If you want to explicitly set the tier for a tenant you can do so using this mutation. If instead you want to add many companies to a tier at once, you can use the [add members mutation](./add-members).

For this mutation you need the following permissions:

* `tierMembership:read`
* `tierMembership:create`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/update-tenant-tier.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/update-tenant-tier.mdx" />
  </Tab>
</Tabs>
