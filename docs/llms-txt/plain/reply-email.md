# Source: https://www.plain.com/docs/graphql/messaging/reply-email.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.plain.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Reply to emails

You can reply to an inbound email with the `replyToEmail` API.

<Tabs>
  <Tab title="Typescript SDK">
    This operation requires the following permissions:

    * `email:create`
    * `email:read`
    * `attachment:download`

    <Snippet file="typescript-sdk/reply-email.mdx" />
  </Tab>

  <Tab title="GraphQL">
    This operation requires the following permissions:

    * `email:create`
    * `email:read`

    <Snippet file="graphql/reply-email.mdx" />
  </Tab>
</Tabs>
