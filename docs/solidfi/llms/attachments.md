# Source: https://docs.solidfi.com/v2/api-reference/getting-started/attachments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Attachments

> Solid Platform supports attachments

The Solid Platform support includes attachments on all the resources.

While adding an attachment, pass the resource id to which the attachment belongs. In response, you will receive a public URL, which is available for 5 minutes that you need to push the attachment to (supports standard mime types).

```json  theme={null}
{
  "id": "att_a8d2b191fa0e960d8e49a4bfd320e07b",
  "reference_id": "ctp_8e5541c8a9e50c3af3b0daacf9175130",
  "label": "formation",
  "url": "http://bucket.s3-website-us-east-1.amazonaws.com",
  "created_at": "2024-04-04T11:06:00Z"
}
```

API reference to add, retrieve, list and delete attachments are [here](/v2/api-reference/attachments/create-an-attachment).

<Tip>You can add multiple attachments to a resource.</Tip>
