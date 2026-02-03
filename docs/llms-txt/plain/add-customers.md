# Source: https://www.plain.com/docs/graphql/tenants/add-customers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.plain.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add customers to tenants

You can add a customer to multiple tenants.

When selecting the customer you can chose how to identify them. You can use the customer's email, externalId or id.

For this mutation you need the following permissions:

* `customer:edit`
* `customerTenantMembership:create`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/add-customer-to-tenants.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/add-customer-to-tenants.mdx" />
  </Tab>
</Tabs>
