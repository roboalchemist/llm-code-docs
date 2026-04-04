# Source: https://resend.com/docs/dashboard/emails/add-unsubscribe-to-transactional-emails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add an unsubscribe link to transactional emails

> Learn how to give email recipients the ability to unsubscribe without searching for the unsubscribe link.

<Info>
  For contact and unsubscribe management workflows, see the [Audiences
  overview](/dashboard/audiences/introduction), where Broadcasts are built for
  keeping track of topics, segments, and unsubscribe preferences.
</Info>

Resend doesn't manage contact lists for transactional emails.

If you manage your own list, you can add the `List-Unsubscribe: https://example.com/unsubscribe` header when sending emails using the Resend API.

As of February 2024, your bulk messages must include a URL version in your list-unsubscribe header, `List-Unsubscribe-Post: List-Unsubscribe=One-Click`, and to allow for a `POST` request from the same URL.

When receiving a `POST`, it should return a blank page with `200 (OK)` or `202 (Accepted)`, and should show the regular unsubscribe page with the `GET` method. Ensure that users stop receiving email within 48 hours of this request.

This header allows email clients to offer an easy “Unsubscribe” option in their UI, enhancing user experience and decreasing spam complaints.

You can read more about this requirement in our [Bulk Sending Requirements blog post.](https://resend.com/blog/gmail-and-yahoo-bulk-sending-requirements-for-2024#one-click-unsubscribe)

```ts Node.js {11} theme={"theme":{"light":"github-light","dark":"vesper"}}
import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

await resend.emails.send({
  from: 'Acme <onboarding@resend.dev>',
  to: ['delivered@resend.dev'],
  subject: 'hello world',
  text: 'it works!',
  headers: {
    'List-Unsubscribe': '<https://example.com/unsubscribe>',
  },
});
```

## Example

<Card title="Unsubscribe url header" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/tree/main/with-unsubscribe-url-header">
  See the full source code.
</Card>
