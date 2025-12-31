# Source: https://resend.com/docs/dashboard/receiving/get-email-content.md

# Get Email Content

> Get the body and headers of a received email.

Receiving emails contain the HTML and Plain Text body of the email, as well as the headers.

<Info>
  Webhooks do not include the actual HTML or Plain Text body of the email. You
  must call the [received emails
  API](/api-reference/emails/retrieve-received-email) to retrieve them. This
  design choice supports large payloads in serverless environments that have
  limited request body sizes.
</Info>

After receiving the webhook event, call the [Receiving API](/api-reference/emails/retrieve-received-email).

Here's an example in a Next.js application:

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

    console.log(email.html);
    console.log(email.text);
    console.log(email.headers);

    return NextResponse.json(email);
  }

  return NextResponse.json({});
};
```
