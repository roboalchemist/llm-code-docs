# Source: https://developers.notion.com/reference/webhooks.md

# Notion API

## Introduction
[Introduction](https://docs.notion.so/reference/intro)

## Integration capabilities
[Integration capabilities](https://docs.notion.so/reference/capabilities)

## Webhooks
[Webhooks](https://docs.notion.so/reference/webhooks)
- [Event types & delivery](https://docs.notion.so/reference/webhooks-events-delivery)

## Request limits
[Request limits](https://docs.notion.so/reference/request-limits)

## Status codes
[Status codes](https://docs.notion.so/reference/status-codes)

## Versioning
[Versioning](https://docs.notion.so/reference/versioning)
- [Changes by version](https://docs.notion.so/reference/changes-by-version)

## Objects

### Block
[Block](https://docs.notion.so/reference/block)
- [Rich text](https://docs.notion.so/reference/rich-text)

### Page
[Page](https://docs.notion.so/reference/page)
- [Page properties](https://docs.notion.so/reference/page-property-values)
  - [Page property items](https://docs.notion.so/reference/property-item-object)

### Database
[Database](https://docs.notion.so/reference/database)

### Data source
[Data source](https://docs.notion.so/reference/data-source)
- [Data source properties](https://docs.notion.so/reference/property-object)

### Comment
[Comment](https://docs.notion.so/reference/comment-object)
- [Comment attachment](https://docs.notion.so/reference/comment-attachment)
- [Comment display name](https://docs.notion.so/reference/comment-display-name)

### File
[File](https://docs.notion.so/reference/file-object)
- [File Upload](https://docs.notion.so/reference/file-upload)

### User
[User](https://docs.notion.so/reference/user)

### Parent
[Parent](https://docs.notion.so/reference/parent-object)

### Emoji
[Emoji](https://docs.notion.so/reference/emoji-object)

### Unfurl attribute (Link Previews)
[Unfurl attribute (Link Previews)](https://docs.notion.so/reference/unfurl-attribute-object)

## Endpoints

### Authentication
[Authentication](https://docs.notion.so/reference/authentication)
- [Create a token](https://docs.notion.so/reference/create-a-token) (post)
- [Introspect token](https://docs.notion.so/reference/introspect-token) (post)
- [Revoke token](https://docs.notion.so/reference/revoke-token) (post)
- [Refresh a token](https://docs.notion.so/reference/refresh-a-token) (post)

### Blocks
[Blocks](https://docs.notion.so/reference/patch-block-children)
- [Append block children](https://docs.notion.so/reference/patch-block-children) (patch)
- [Retrieve a block](https://docs.notion.so/reference/retrieve-a-block) (get)
- [Retrieve block children](https://docs.notion.so/reference/get-block-children) (get)
- [Update a block](https://docs.notion.so/reference/update-a-block) (patch)
- [Delete a block](https://docs.notion.so/reference/delete-a-block) (del)

### Pages
[Pages](https://docs.notion.so/reference/post-page)
- [Create a page](https://docs.notion.so/reference/post-page) (post)
- [Retrieve a page](https://docs.notion.so/reference/retrieve-a-page) (get)
- [Retrieve a page property item](https://docs.notion.so/reference/retrieve-a-page-property) (get)
- [Update page](https://docs.notion.so/reference/patch-page)
  - [Trash a page](https://docs.notion.so/reference/archive-a-page)

### Databases
[Databases](https://docs.notion.so/reference/database-create)
- [Create a database](https://docs.notion.so/reference/database-create) (post)
- [List databases](https://docs.notion.so/reference/list-databases) (get)
- [Get database properties](https://docs.notion.so/reference/get-database-properties) (get)
- [Update database properties](https://docs.notion.so/reference/update-database-properties) (patch)
```

# API Reference

## Database Operations

- [Create a database](https://docs.nestbase.com/reference/database-create)
- [Update a database](https://docs.nestbase.com/reference/database-update)
- [Retrieve a database](https://docs.nestbase.com/reference/database-retrieve)

## Data Sources

### Create a Data Source

- [Create a data source](https://docs.nestbase.com/reference/create-a-data-source)
- [Update a data source](https://docs.nestbase.com/reference/update-a-data-source)
  - [Update data source properties](https://docs.nestbase.com/reference/update-data-source-properties)
- [Retrieve a data source](https://docs.nestbase.com/reference/retrieve-a-data-source)
- [Query a data source](https://docs.nestbase.com/reference/query-a-data-source)
  - [Filter data source entries](https://docs.nestbase.com/reference/filter-data-source-entries)
  - [Sort data source entries](https://docs.nestbase.com/reference/sort-data-source-entries)
- [List data source templates](https://docs.nestbase.com/reference/list-data-source-templates)

### Databases (deprecated)

#### Create a Database

- [Create a database](https://docs.nestbase.com/reference/create-a-database)
- [Query a database](https://docs.nestbase.com/reference/post-database-query)
  - [Filter database entries](https://docs.nestbase.com/reference/post-database-query-filter)
  - [Sort database entries](https://docs.nestbase.com/reference/post-database-query-sort)
- [Retrieve a database](https://docs.nestbase.com/reference/retrieve-a-database)
- [Update a database](https://docs.nestbase.com/reference/update-a-database)
  - [Update database properties](https://docs.nestbase.com/reference/update-property-schema-object)
- [List databases (deprecated)](https://docs.nestbase.com/reference/get-databases)

### Comments

- [Create comment](https://docs.nestbase.com/reference/create-a-comment)
- [Retrieve a comment](https://docs.nestbase.com/reference/retrieve-comment)
- [List comments](https://docs.nestbase.com/reference/list-comments)

### File Uploads

- [Create a file upload](https://docs.nestbase.com/reference/create-a-file-upload)
- [Send a file upload](https://docs.nestbase.com/reference/send-a-file-upload)
- [Complete a file upload](https://docs.nestbase.com/reference/complete-a-file-upload)
- [Retrieve a file upload](https://docs.nestbase.com/reference/retrieve-a-file-upload)
- [List file uploads](https://docs.nestbase.com/reference/list-file-uploads)

### Search

- [Search](https://docs.nestbase.com/reference/post-search)
```

# Webhooks

Webhooks let your integration receive real-time updates from Notion. Whenever a page or database changes, Notion sends a secure HTTP POST request to your webhook endpoint. This allows your application to respond to workspace activity as it happens — whether that's syncing data, triggering automation, or keeping your UI in sync with user activity.

![Image 1](https://files.readme.io/cf4e4b4cbb5de9c5b1277b35386a21574b4960af36c14fe7d648d905377db478-image.png)

**Think of it like this:** Instead of repeatedly polling the Notion API to check if anything has changed, Notion will tell you the moment something important happens.

## How webhooks work: A simple example

**Let’s walk through an example from start to finish:**

1. Your integration is subscribed to `page.content_updated` events.
2. A user edits the title of a page in Notion.
3. Within a minute, Notion sends a webhook request to your configured endpoint.
4. The event payload includes metadata such as the page ID, the event type, and a timestamp.
5. Your server receives the event, verifies it, and calls the Notion API to fetch the updated title using the page ID from the event.
6. Your application updates its internal data or takes any other action you’ve defined.

This flow lets you react quickly to user activity, without polling or guessing when something has changed.

## Getting started with webhooks

### Step 1: Creating a webhook subscription

To receive webhook events, you’ll need to create a subscription through your integration settings.

**You’ll need to:**

1. Visit your [integration settings](https://www.notion.so/profile/integrations).
2. Either create a new integration or select an existing one.
3. Navigate to the **Webhooks** tab and click **+ Create a subscription**.
   ![Image 2](https://files.readme.io/522e40363df1bd7437239b25a1caacc8cc607426f45fc90febfff5f00647aeb4-webhooks-1.png)
4. Enter your public **Webhook URL** — this is the public endpoint where you want Notion to send events. It must be a secure (SSL) and publicly available endpoint. Endpoints in localhost are not reachable.
   ![Image 3](https://files.readme.io/1ef497d7b9b3622de379e6907cd722167766413693ac9f1885b59eb028b4e7dd-webhooks-2.png)
5. Choose which event types you'd like to subscribe to. You can modify these later if needed.
6. Click **Create subscription**.
   ![Image 4](https://files.readme.io/6e68cad7be75acc8165e29eb2a56a282edba31fdcba78238831466b83a115b8f-webhooks-3.png)

At this point, your webhook is created but not yet verified. To complete the setup, you’ll need to confirm that your endpoint can receive and respond to verification.

### Step 2: Verifying the subscription

When you create a subscription, Notion sends a one-time POST request to your webhook URL. The body of the request contains a `verification_token`, which proves that Notion can successfully reach your endpoint.

**Example payload with `verification_token`:**

```json
{
  "verification_token": "secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl"
}
```

**You’ll need to:**

1. Inspect the incoming request at your endpoint and extract the `verification_token` from the JSON payload.
   - (Optional): Securely store this token for payload validation setup later, [in step 3](#step-3-validating-event-payloads-recommended).
2. Go back to the **Webhooks** tab within your Notion integration UI and click **⚠️ Verify** on the bottom left of the page
   ![Image 5](https://files.readme.io/6e68cad7be75acc8165e29eb2a56a282edba31fdcba78238831466b83a115b8f-webhooks-3.png)
3. Paste the `verification_token` value into the form and click **Verify subscription.**

![Image 6](https://files.readme.io/42b82e16a49278f78ecfdfb6a8f5acafe1ae251376bdc636d43c68abf4f685e5-webhooks-4.png)

If you did not receive a `verification_token`, you can click **Resend token** from the webhook verification modal.

Once submitted, your webhook subscription is considered active, and will start receiving events.

> **Changing your webhook URL or event subscriptions**
>
> You can only change the webhook URL before verification. After verification, if you need to change the URL, you must delete and recreate the subscription. You can change the subscribed events at any time.

### Step 3: Validating event payloads (Recommended)

To help ensure the security of your integration, Notion includes a cryptographic signature with every webhook event we send. This allows you to verify that the payload was sent by Notion and hasn’t been modified in transit.

While payload validation is optional, we recommend implementing it for any production environment.

> **Using a no-code or low-code platform?**
>
> If you're using a no-code or low-code platform (like Zapier, Make, or Pipedream), you may not have access to custom code for signature verification — and that’s okay. Validation is encouraged, but not required for webhooks to work.

#### How it works

In the previous step, Notion sent a one-time `verification_token` to your webhook URL. You’ll use this token to verify the authenticity of all subsequent webhook events.

Every webhook request from Notion includes an `X-Notion-Signature` header, which contains an HMAC-SHA256 hash of the request body, signed with your `verification_token`.

**Sample `X-Notion-Signature` from Notion:**

```json
{
  "X-Notion-Signature": "sha256=461e8cbcba8a75c3edd866f0e71280f5a85cbf21eff040ebd10fe266df38a735"
}
```

To validate the request, you can use the `verification_token` along with the event's payload to recompute the signature and verify the request's authenticity. If they match, the payload is trustworthy.

**Sample code for computing the signature and validating the webhook payload:**

**JavaScript**
```javascript
import { createHmac, timingSafeEqual } from "crypto"

// Retrieve the `verification_token` from the initial request
// (subscription verification; Step 2)
const verificationToken = "secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl"

// This body should come from your request body for subsequent validations
const body = {"verification_token":"secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl"}

const calculatedSignature = `sha256=${createHmac("sha256", verificationToken).update(JSON.stringify(body)).digest("hex")}`

const isTrustedPayload = timingSafeEqual(
  Buffer.from(calculatedSignature),
  Buffer.from(headers["X-Notion-Signature"]),
)

if (!isTrustedPayload) {
  // Ignore the event
  return
}
```

**Python**
```python
import hmac
import hashlib
import json

# Retrieve the `verification_token` from initial request
# (subscription verification; Step 2)
verification_token = "secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl"

# This body should come from your request body for subsequent validations
body = {"verification_token": "secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl"}

# Calculate the signature
body_json = json.dumps(body, separators=(",", ":"))  # Minified JSON, matches JSON.stringify
hmac_obj = hmac.new(
    verification_token.encode("utf-8"),
    body_json.encode("utf-8"),
    hashlib.sha256
)
calculated_signature = "sha256=" + hmac_obj.hexdigest()

# Assume headers is a dict containing HTTP headers
# Example:
# headers = {"X-Notion-Signature": "<signature from request>"}

# Use hmac.compare_digest for timing-safe comparison
is_trusted_payload = hmac.compare_digest(
    calculated_signature,
    headers["X-Notion-Signature"]
)

if not is_trusted_payload:
    # Ignore the event
    return
```

**Ruby**
```ruby
require 'openssl'
require 'json'

# Retrieve the verification_token from initial request
verification_token = "secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl"

# This body should come from your request body for subsequent validations
body = { "verification_token" => "secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl" }

# Calculate the signature (minified JSON to match JSON.stringify)
body_json = JSON.generate(body)
digest = OpenSSL::HMAC.hexdigest("SHA256", verification_token, body_json)
calculated_signature = "sha256=#{digest}"

# Assume headers is a Hash containing HTTP headers
# Example:
# headers = { "X-Notion-Signature" => "<signature from request>" }

# Constant-time comparison
is_trusted_payload = ActiveSupport::SecurityUtils.secure_compare(
  calculated_signature,
  headers["X-Notion-Signature"]
)

unless is_trusted_payload
  # Ignore the event
  return
end
```

Implementing this validation step is a small lift that adds a strong layer of security to your webhook integration. If you ever rotate or recreate your webhook subscription, be sure to update your stored `verification_token`.

## Testing your webhook subscription

Once your webhook subscription is set up and verified, it’s a good idea to test that everything is working as expected.

Below are three common test scenarios you can try, each corresponding to a supported event type. These tests simulate typical content updates and help ensure your endpoint is receiving and processing events correctly.

### Test 1: Change a page title

This test checks your webhook’s ability to handle aggregated events, which are delivered with a short delay to avoid sending redundant updates.

**You’ll need to:**

1. In your Notion workspace, add the integration to a page.
2. Change the title of that page.

**Note:** This test assumes the content being edited is already part of a page. If you need to create a new page, see the next section for creating pages.

```yaml
# Add the integration to a page called "Test Integration"
%name{Page Name}%
%title{Page Title}%

# Edit the title of the page
%title{New Page Title}%
```

**Testing steps:**

1. Log in to your Notion workspace.
2. Open the page you just added.
3. Update the title to `New Page Title`.
4. Save the page.
5. Verify the webhook received a notification about the page update.
6. Check the log for the updated title.

By following these steps, you can ensure your webhook is correctly handling the event and updating your application accordingly.

---

You can also test your webhook subscription with different event types, such as `page.archived` or `search.results`, to ensure it handles various content modifications accurately.

For more detailed testing instructions, refer to the [testing documentation](https://help.notion.so/hc/en-us/articles/150000522371-Test-webhooks).

---

Did you find what you were looking for? Don't forget to give us feedback! We love hearing your thoughts and suggestions!
```

# How Webhooks Work: A Simple Example

Imagine you have a special club where members send messages to each other using a unique code. The code tells them how to join a game hosted at a different venue.

## Step 1: Sending a Message

One member sends a message to the club's administrator with the code "joinGame". The administrator uses this code to find the correct game room and send the member to the right place.

## Step 2: Receiving the Message

The member receives the message and follows the instructions to join the game. They enter the correct code, and the system redirects them to the game room.

## Step 3: Receiving the Game Room Information

Once in the game room, the member sees a sign that says "Page Title Changed." They realize they need to change the page title to "Summer Break!" before joining their friends.

## Summary

In this example, the member is sending a message (the "joinGame" code) to the administrator, who uses it to deliver information (the game room location) to the member. The member then uses this information to perform a task (changing the page title).

## What's Next?

Now that you understand how webhooks work, you can learn about setting up and testing your first webhook subscription.

[Creating a Webhook Subscription](https://developers.cloudflare.com/workers/guides/introduction/webhooks/#step-1-creating-a-webhook-subscription)
[Verifying Your Subscription](https://developers.cloudflare.com/workers/guides/introduction/webhooks/#step-2-verifying-the-subscription)
[Validating Event Payloads](https://developers.cloudflare.com/workers/guides/introduction/webhooks/#step-3-validating-event-payloads-recommended)

## Testing Your Webhook Subscription

### Test 1: Change a Page Title

**Instructions:**

1. In a page your integration has access to, change the title from "Welcome to Our Site" to "Hello, World!"
2. Verify that after changing the title, you receive a webhook event with the updated page title.

### Test 2: Add a Comment

**Instructions:**

1. Open any database your integration is connected to.
2. Add a new record or comment to the database.
3. Ensure you receive a webhook event with the added record or comment shortly after adding it.

### Test 3: Modify a Database Schema

**Instructions:**

1. Open any database your integration is connected to.
2. Make a structural change to the database schema, such as adding a new field.
3. Confirm that you receive a webhook event with the schema modification notification shortly after the change.

## Troubleshooting Tips

If your webhook isn’t receiving events as expected, here are a few things to double-check. These are the most common reasons developers miss events during setup or testing.

### 🔒 1. Check Access Permissions

Make sure the integration has access to the object that triggered the event. For example, if a new page is created inside a private page your integration doesn’t have access to, the event won’t be triggered.

### ✅ 2. Confirm Capabilities

Some event types require specific capabilities to be enabled for your integration.

For instance, to receive `comment.created` events, your integration must have the "comment read" capability selected. Without it, even if your integration has access to the page, the comment event won’t be delivered.

You can confirm this in the **Capabilities** tab of your integration’s settings.

### ⏳ 3. Understand Aggregated Event Timing

Not all webhook events are sent immediately. Some, like `page.content_updated`, are aggregated to reduce noise from frequent edits (e.g., typing, formatting, moving blocks). This is normal and helps group multiple rapid changes into a single webhook event.

See [Event Delivery](/reference/webhooks-events-delivery#event-delivery) for a deeper explanation.

**Tip**: If you're testing and expecting an instant response, start with non-aggregated events like `comment.created` or `page.locked`.

### ☑️ Confirm Your Subscription Status

Even if everything else is configured correctly, your webhook won’t receive events unless the subscription is active.

Head to the **Webhooks** tab under your integration settings and make sure your subscription is **active**. If the status shows as **paused**, **pending verification**, or if the subscription was deleted, events won’t be delivered to your endpoint.
```