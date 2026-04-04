# Source: https://www.plain.com/docs/graphql/tiers/add-members.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.plain.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add companies and tenants to tiers

You can add multiple tenants and companies to a tier in a single mutation.

Companies and tenants can only be in a single tier.

For this mutation you need the following permissions:

* `tierMembership:read`
* `tierMembership:create`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/add-members-to-tier.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/add-members-to-tier.mdx" />
  </Tab>
</Tabs>
