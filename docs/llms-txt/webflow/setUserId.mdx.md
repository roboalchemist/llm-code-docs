# Source: https://developers.webflow.com/browser/custom-goals/off-site-conversions/setUserId.mdx

***

title: setUserId()
slug: custom-goals/off-site-conversions/setUserId
description: Identify visitors with a known user ID for off-site conversion tracking
hidden: false
'og:title': setUserId()
'og:description': Identify visitors with a known user ID for off-site conversion tracking
-----------------------------------------------------------------------------------------

## `wf.setUserId(userDomain, userId)`

Identify a visitor with a known user ID. This client-side API tells Webflow who the visitor is so that off-site conversions can be attributed to their session.

<Note title="Call before sending server-side events">
  You must pass the user ID to Webflow via `wf.setUserId()` before you can report any related off-site conversion events via the [server-side API](/browser/custom-goals/off-site-conversions/server-api).
</Note>

### Syntax

```typescript
wf.setUserId(userDomain: string, userId: string): void
```

### Parameters

* **userDomain** (required): `string` — A label identifying the system where your user data lives (e.g., `salesforce`, `marketo`, `applicationId`). This helps distinguish between different ID sources.

* **userId** (required): `string` — The unique identifier for the user in your system. This must match the `userId` you send in the server-side API request.

### Example

```javascript
wf.ready(function() {
    wf.setUserId('salesforce', '72349876');
});
```

### When to call setUserId

Call `wf.setUserId()` as soon as you know the visitor's identity. Common scenarios include:

* After a user logs in
* When a user submits a form with identifying information
* When you can match the visitor to a record in your CRM or database

The user ID must be set before the visitor leaves your site. Once set, Webflow can attribute any subsequent off-site conversions to this visitor's session. The user ID persists for the duration of the session, which ends after 30 minutes of inactivity or a 24-hour maximum timeout.

### Choosing a user ID

The value you use for the ID depends on the system where your user data lives. Common sources include:

* In-house databases
* Salesforce contact IDs
* Marketo lead IDs
* Application or account IDs

Choose an ID that's available on both the client side (your website) and server side (your backend systems) so you can match conversions correctly.

<Warning title="Protect personally identifiable information">
  The `userId` sent to Webflow should not contain personally identifiable information (PII). If your identifiers include any of the following, use a one-way hash (such as SHA-256) before sending:

  **Do not include information like:**

  * Names
  * Email addresses
  * Phone numbers
  * Any combination of data that could identify an individual

  Your organization is responsible for implementing appropriate hashing before calling this API.
</Warning>

### Example: Credit card application

In this example, a visitor fills out a form to apply for a credit card. The actual conversion (approval) happens later, after a review process.

```javascript
wf.ready(function() {
    // Use the application ID as the user identifier
    wf.setUserId('applicationId', '123456789');
});
```

Later, when the application is approved, your backend sends the conversion event using the same `userDomain` and `userId` via the [server-side API](/browser/custom-goals/off-site-conversions/server-api).

### Returns

This method doesn't return a value. The user ID is stored and associated with the visitor's session.

### FAQs

{/* <!-- vale off --> */}

<Accordion title="Can I call setUserId multiple times?">
  {/* <!-- vale on --> */}

  Yes, you can call `wf.setUserId()` multiple times with different `userDomain` values if you have multiple ID systems. Each call associates the visitor with that specific domain and ID combination.

  {/* <!-- vale off --> */}
</Accordion>

<Accordion title="What if the visitor clears their cookies?">
  {/* <!-- vale on --> */}

  If the visitor clears their cookies or uses a different device, they'll be treated as a new visitor. You'll need to call `wf.setUserId()` again to identify them.

  {/* <!-- vale off --> */}
</Accordion>

{/* <!-- vale on --> */}
