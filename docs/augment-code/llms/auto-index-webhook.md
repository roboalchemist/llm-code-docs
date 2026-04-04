# Source: https://docs.augmentcode.com/context-services/context-connectors/quickstart/auto-index-webhook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Auto-Index with Webhooks

> Set up a custom webhook server to re-index on push (advanced) in 10 minutes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

## Prerequisites

* A Vercel account (or Express server)
* Augment API credentials
* AWS credentials + S3 bucket
* A GitHub repo you control

## Steps

### 1. Create a Vercel project

```bash  theme={null}
npx create-next-app@latest my-webhook --typescript --app
cd my-webhook
npm install @augmentcode/context-connectors @aws-sdk/client-s3
```

### 2. Create the webhook handler

Create `app/api/webhook/route.ts`:

```typescript  theme={null}
import { createVercelHandler } from "@augmentcode/context-connectors/integrations/vercel";
import { S3Store } from "@augmentcode/context-connectors/stores";

const store = new S3Store({ bucket: process.env.INDEX_BUCKET! });

export const POST = createVercelHandler({
  store,
  secret: process.env.GITHUB_WEBHOOK_SECRET!,
  shouldIndex: (event) => event.ref === "refs/heads/main",
});
```

### 3. Set environment variables in Vercel

```
AUGMENT_API_TOKEN=your-token
AUGMENT_API_URL=https://your-tenant.api.augmentcode.com/
GITHUB_WEBHOOK_SECRET=your-secret
INDEX_BUCKET=my-indexes
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
```

### 4. Deploy

```bash  theme={null}
npx vercel --prod
```

Note the URL (e.g., `https://my-webhook.vercel.app`).

### 5. Configure GitHub webhook

1. Go to your repo → Settings → Webhooks → Add webhook
2. Payload URL: `https://my-webhook.vercel.app/api/webhook`
3. Content type: `application/json`
4. Secret: same as `GITHUB_WEBHOOK_SECRET`
5. Events: Just the push event
6. Click "Add webhook"

### 6. Test it

Push a commit to main. Check Vercel logs for:

```
Indexed myorg/myrepo: 142 files indexed
```

## Done!

Your index updates automatically on every push to main.

## Also Works With

| Instead of...    | Try...                                                                     |
| ---------------- | -------------------------------------------------------------------------- |
| Vercel           | Express: `createExpressHandler()` from `integrations/express`              |
| Vercel           | Any framework: `createGitHubWebhookHandler()` + `verifyWebhookSignature()` |
| Main branch only | Customize `shouldIndex` to match any branch pattern                        |
| S3 storage       | `FilesystemStore` for local/self-hosted setups                             |
