# Source: https://www.plain.com/docs/graphql/events/create-thread-event.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.plain.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a thread event

<Info>
  A thread event will only be created in the thread ID provided. If you want an event to appear in
  all threads for a customer please use a [customer
  event](/graphql/events/create-customer-event).
</Info>

To create a thread event you need a thread ID.

You can get this by [creating a thread](/graphql/threads/create) in Plain, from data in webhooks or other API calls you made. If you want to test this, press **⌘ + K** on any thread and then "Copy thread ID" to get an ID you can experiment with.

In this example we'll be creating the following event:

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=f168c4372479e924f08c9a04f23e8150" alt="Example event" data-og-width="1972" width="1972" data-og-height="634" height="634" data-path="public/images/events-api-key-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=71673a4fc78badf3f2eb901068dc6980 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=d70f2f75494f1aa7b24e5cb2e62d60ba 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=c929bcc2c54f5f48b3a59962eb2a0d1b 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=8e943249db6f0aa7ecd17df85bd3a995 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=8d801c54aef04486236abea487cb7ea8 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=f9245da75ef5d680153e0d3a5477ec8e 2500w" /></Frame>

<Tabs>
  <Tab title="Typescript SDK">
    For this you'll need an API key with the following permissions:

    * `threadEvent:create`
    * `threadEvent:read`
    * `thread:read`
    * `customer:read`

    <Snippet file="typescript-sdk/create-thread-event.mdx" />

    Which would console.log:

    <Snippet file="typescript-sdk/create-thread-event-response.mdx" />
  </Tab>

  <Tab title="GraphQL">
    For this you'll need an API key with the following permissions:

    * `threadEvent:create`
    * `threadEvent:read`

    <Snippet file="graphql/create-thread-event.mdx" />
  </Tab>
</Tabs>
