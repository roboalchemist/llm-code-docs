# Source: https://www.plain.com/docs/graphql/tiers/remove-members.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.plain.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove companies and tenants to tiers

You can remove companies and tenants from the tiers they are part of manually in the UI or via the API.

For this mutation you need the following permissions:

* `tierMembership:read`
* `tierMembership:delete`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/remove-members-from-tier.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/remove-members-from-tier.mdx" />
  </Tab>
</Tabs>
