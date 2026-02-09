# Source: https://www.plain.com/docs/graphql/tenants/remove-customers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.plain.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove customers to tenants

You can remove customers from multiple tenants in one API call.

When selecting the customer you can chose how to identify them. You can use the customer's email, externalId or id.

For this mutation you need the following permissions:

* `customer:edit`
* `customerTenantMembership:delete`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/remove-customer-from-tenants.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/remove-customer-from-tenants.mdx" />
  </Tab>
</Tabs>
