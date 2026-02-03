# Source: https://www.plain.com/docs/graphql/labels/remove.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.plain.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove labels

You can remove labels from a thread with a call to `removeLabels`. Label IDs for this call can be retrieved by fetching a thread with the API.

This operation requires the following permissions:

* `label:delete`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/remove-labels.mdx" />

    Which if successful will console log `null`.
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/remove-labels.mdx" />
  </Tab>
</Tabs>
