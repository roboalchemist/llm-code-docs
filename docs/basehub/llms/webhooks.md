# Webhooks

> Learn how to use Webhooks to subscribe to changes that happen within BaseHub.

[Workflows](https://docs.basehub.com/blocks/primitives/workflow) allow you to receive event notifications from BaseHub. BaseHub will send a POST request to a URL you specify when certain events happen in a BaseHub Repository.

## Available triggers

*   A commit happens: This is a useful notification that can help you set up [on-demand revalidation for your Next.js Apps](https://docs.basehub.com/documentation/nextjs-integration/environments-and-caching#on-demand-revalidation), amongst other things.  
    \- **Requires the workflow to be committed**
    
*   Collection Events: Row created, updated or deleted.  
    \- **Requires the workflow to be committed**
    
*   New events in Event Block.  
    \- **Requires the workflow to be committed**
    
*   A [primitive block](https://docs.basehub.com/blocks/primitives) value, or a [layout block](https://docs.basehub.com/blocks/layout) title gets updated.  
    \- **Does not require the workflow to be committed**
    

## Workflow block

To configure webhooks, you’ll need to create a new Workflow block in your repo. There you can setup the URL that will be requested when the workflow is triggered.

## Handling Webhook Events on Your API Endpoint

Once you've configured a webhook in your BaseHub project, you’ll want to properly authenticate and process the incoming event on your API endpoint. The `basehub/workflows` package provides a utility called `authenticateWebhook` that simplifies this process and returns a **typed** payload, depending on the trigger used in your workflow.

Below is a full example using Vercel's Edge Functions, but the approach applies to other environments with minor adjustments.

### Authenticating and Handling a Webhook

```
import { basehub } from 'basehub'
import { authenticateWebhook } from 'basehub/workflows'

export const POST = async (request: Request) => {
  const {
    workflows: {
      onDemandRevalidation: { webhookSecret },
    },
  } = await basehub().query({
    workflows: {
      onDemandRevalidation: {
        webhookSecret: true,
      },
    },
  })

  const result = await authenticateWebhook({
    body: request.body,
    signature: request.headers,
    secret: webhookSecret,
  })

  if (!result.success) {
    return new Response('Unauthorized', { status: 401 })
  }

  // your custom webhook revalidation logic goes here

  return new Response(
    JSON.stringify({ success: true }),
    {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
      },
    }
  )
}
```

### Notes

*   `authenticateWebhook` handles signature validation and payload type-safety for you.
    
*   The structure of the `result.payload` depends on the workflow's trigger.
    
*   Use the payload data to kick off revalidation, background jobs, or sync with external services.
    

### Payload Types by Trigger

Below is a complete list of supported event types and their corresponding payload structures.

#### commit.created

Triggered when a new commit is created.

```
{
  type: 'commit.created',
  timestamp: string,
  data: Commit
}
```

#### list-block.created

#### list-block.updated

#### list-block.deleted

Triggered on commit, when a block inside a list is created, updated, or deleted.

```
{
  type: 'list-block.created' | 'list-block.updated' | 'list-block.deleted',
  timestamp: string,
  data: {
    listBlockId: string,
    blockId: string
    listBlockTitle?: string,
  }
}
```

*   `listBlockId`: The ID of the list block.
    
*   `blockId`: The child block that was created/updated/deleted.
    
*   `listBlockTitle`: Optional title of the list block.
    

#### event-block.created

Triggered when an event is received.

```
{
  type: 'event-block.created',
  timestamp: string,
  data: {
    eventBlockId: string,
    eventBlockTitle: string,
    parentBlockId?: string,
    data?: any
  }
}
```

*   `eventBlockId`: ID of the event block.
    
*   `parentBlockId`: The parent block (if applicable).
    
*   `data`: Arbitrary user-defined data.
    

#### block.updated

Triggered when a block is updated.  
This event includes only the block ID and its location in the tree.

```
{
  type: 'block.updated',
  timestamp: string,
  data: {
    blockId: string,
    blockIdPath: string
  }
}
```

*   `blockId`: ID of the block.
    
*   `blockIdPath`: A string path representation of the block's location in the tree.
    

### Common Use Cases

Once you've set up webhook handling, here are a few things you might use them for:

*   **Revalidate a page** in your frontend after committing content.
    
*   **Send feedback or logs** to a Slack or Discord channel.
    
*   **Trigger third-party services**, like uploading videos to a hosting platform.
    

Webhooks let you connect BaseHub to the rest of your stack—so you can automate what matters and keep your workflows smooth.