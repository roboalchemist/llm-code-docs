# Source: https://resend.com/docs/dashboard/receiving/forward-emails.md

# Forward Receiving Emails

> Forward Receiving emails to another email address.

Receiving emails can also be forwarded to another email address.

<Info>
  Webhooks do not include the actual HTML or Plain Text body of the email. You
  must call the [received emails
  API](/api-reference/emails/retrieve-received-email) to retrieve them. This
  design choice supports large payloads in serverless environments that have
  limited request body sizes.
</Info>

To forward an email, use the [Send Email API](/api-reference/emails/send-email).

After receiving the webhook event, call the [Receiving API](/api-reference/emails/retrieve-received-email) (and the [Attachments API](/api-reference/emails/list-received-email-attachments) if you want to include attachments). Then forward the email using the [Send Email API](/api-reference/emails/send-email).

Here's an example of forwarding an email in a Next.js application:

```js app/api/events/route.ts theme={null}
import type { NextRequest } from 'next/server';
import { NextResponse } from 'next/server';
import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

export const POST = async (request: NextRequest) => {
  const event = await request.json();

  if (event.type === 'email.received') {
    const { data: email } = await resend
      .emails
      .receiving
      .get(event.data.email_id);

    const { data: attachments } = await resend
      .attachments
      .receiving
      .list({ emailId: event.data.email_id });

    // download the attachments and encode them in base64
    for (const attachment of attachments.data) {
      const response = await fetch(attachment.download_url);
      const buffer = Buffer.from(await response.arrayBuffer());
      attachment.content = buffer.toString('base64');
    }

    const { data, error } = await resend.emails.send({
      from: 'Acme <onboarding@resend.dev>',
      to: ['delivered@resend.dev'],
      subject: event.data.subject,
      html: email.html,
      text: email.text,
      attachments
    });

    return NextResponse.json(data);
  }

  return NextResponse.json({});
};
```
