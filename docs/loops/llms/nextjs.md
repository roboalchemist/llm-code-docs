# Source: https://loops.so/docs/sdks/javascript/nextjs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up Loops in Next.js

> How to send email from your Next.js project with Loops.

This guide shows how to add Loops to your Next.js project, so you can send transactional emails, manage contacts and trigger automated emails.

## Install the SDK

The first step is to install the Loops SDK. This is written in TypeScript so you can benefit from strict types when coding.

```bash  theme={"dark"}
npm i loops
```

You'll need an API key to use the SDK. Go to your [API Settings page](https://app.loops.so/settings?page=api) in Loops to generate and copy a key.

Save this value in your environment variables as something like `LOOPS_API_KEY`.

Then you can import the Loops SDK client like this:

```javascript  theme={"dark"}
import { LoopsClient } from "loops";

const loops = new LoopsClient(process.env.LOOPS_API_KEY);
```

<Tip>
  You can also use the [Loops API](/api-reference) directly in your app, without
  the SDK. [Read more](#using-the-api-instead)
</Tip>

<CardGroup>
  <Card title="JavaScript SDK" href="/sdks/javascript" icon="js">
    Explore our official JS/TS SDK.
  </Card>

  <Card title="Loops API" icon="rectangle-terminal" href="/api-reference">
    Read the Loops API reference.
  </Card>
</CardGroup>

## Server-side only

It is important that you only use the Loops API and SDK from server-side code. If you make calls directly in the browser, you risk exposing your API key, which would give other people read and write access to your Loops account data. Additionally, the Loops API does not support cross-origin requests made from client-side JavaScript.

If you want to make calls from the browser—for example, to collect newsletter subscriptions from a form—create proxy endpoints. To add a new contact, create an internal API endpoint and use the Loops API/SDK within it.

```typescript app/api/contacts/route.ts theme={"dark"}
import { NextRequest, NextResponse } from "next/server";
import { LoopsClient } from "loops";

const loops = new LoopsClient(process.env.LOOPS_API_KEY as string);

export async function POST(request: NextRequest) {
  const res = await request.json();

  const email = res["email"];

  // Note: updateContact() will create or update a contact

  const resp: {
    success: boolean;
    id?: string;
    message?: string;
  } = await loops.updateContact(email);

  return NextResponse.json({ success: resp.success });
}
```

## Send transactional email

A big use case for using Loops in a Next.js project is to send transactional email to users. These emails are one-off emails, which help users with your product, for example password reset emails notification emails.

To create a transactional email, go to the Transactional page in Loops. Click **Create** or select a template.

Create the email in [the editor](/creating-emails/editor), which gives you rich formatting options and components.

<img src="https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=6d4f8855f2bb71dbf528ab8da2c4aacb" alt="Creating a transactional email" data-og-width="2280" width="2280" data-og-height="1355" height="1355" data-path="images/transactional-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=280&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=9e8df0d409a4bf917d37a08295dc8455 280w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=560&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=15b343e6210f4aa163570a8709f68152 560w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=840&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=5bdb62280bb095794d570da750a13c0e 840w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=1100&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=c7a97149078a5e2ac87cbd3c41d270a2 1100w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=1650&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=60cebc6a82938cb12f70af9f60ecbd21 1650w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=2500&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=fcb440735577b734aaf52a2a68f1a9f5 2500w" />

To add dynamic content (like rest password URLs or user data) you can add [data variables](/transactional#add-data-variables) into the email from the toolbar.

Give each data variable a unique name. You can populate these variables from your code when sending the email via the SDK in the next step.

Make sure to Publish your transactional email when you're done.

Now your email is created you can start sending emails.

In your code, call `sendTransactionalEmail()` and include values for each of the data variables you added to your email.

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  const dataVariables = {
    loginUrl: "https://myapp.com/login/",
  };

  const resp = await loops.sendTransactionalEmail({
  transactionalId: "transaction_email_id",
  email: "user@gmail.com",
  dataVariables
  });

  if (!resp.success) {
  // The sending failed
  } else {
  // The email was sent successfully
  }

  ```

  ```typescript TypeScript theme={"dark"}
  const dataVariables: { loginUrl: string } = {
    loginUrl: "https://myapp.com/login/",
  };

  const resp: {
    success: boolean,
    path?: string,
    message?: string
  } | {
    success: false;
    error: {
      path: string;
      message: string;
    };
    transactionalId?: string;
  } = await loops.sendTransactionalEmail({
    transactionalId: "transaction_email_id",
    email: "user@gmail.com",
    dataVariables
  });

  if (!resp.success) {
    // The sending failed
  } else {
    // The email was sent successfully
  }
  ```
</CodeGroup>

The response will contain a `success` boolean telling you if the email was sent successfully. If it was not, you'll also receive an error message.

<CardGroup className="mt-8">
  <Card title="sendTransactionalEmail()" href="/sdks/javascript#sendtransactionalemail" icon="code">
    Read more in the SDK docs.
  </Card>
</CardGroup>

## Sync users to Loops

Another main use case for teams using Loops is to keep their Loops audience updated when user data changes in their application.

To do this you can use the `updateContact()` method.

<Tip>
  `updateContact()` can be used as a shortcut "update or create" function. It
  will create new contacts if the provided email address and/or user ID are not
  found.
</Tip>

For example, you may store custom data in Loops like subscription plan level or user usage information that you include in emails. You can update contacts in Loops like this:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  const contactProperties = {
    userId: 826,
    planName: "Pro" /* Custom property */,
    usage: 172629 /* Custom property */,
  };

  const resp = await loops.updateContact("user@gmail.com", contactProperties);

  if (!resp.success) {
  // The call failed
  } else {
  // The contact was updated OK
  }

  ```

  ```typescript TypeScript theme={"dark"}
  const contactProperties: Record<string, string | number> = {
    userId: 826,
    planName: "Pro" /* Custom property */,
    usage: 172629 /* Custom property */,
  };

  const resp: {
    success: boolean,
    id?: string,
    message?: string
  } = await loops.updateContact("user@gmail.com", contactProperties);

  if (!resp.success) {
    // The call failed
  } else {
    // The contact was updated OK
  }
  ```
</CodeGroup>

The TypeScript example above shows how to properly type your `contactProperties` object and the expected response from the `updateContact` method.

<Tip>
  We recommend always populating the `userId` value for users, which should be
  their unique value in your platform. This allows you to change a contact's
  email address in the future, because they have a separate unique identifier in
  the system.
</Tip>

<CardGroup className="mt-8">
  <Card title="updateContact()" href="/sdks/javascript#updatecontact" icon="user">
    Read more in the SDK docs.
  </Card>
</CardGroup>

## Trigger loops with events

A third example of using the Loops SDK is to trigger [loops](/loop-builder). Loops are automated email workflows, which can send multiple emails to contacts.

You can trigger these emails using [events](/events), and you can send events to Loops using the SDK.

For example, you may have a loop that you send to new users after they have completed an onboarding flow in your app.

First, [create a new loop](https://app.loops.so/loops) using the "Event received" trigger. Add emails, timers and audience filters to your loop as you wish.

Then to trigger this email sequence, send an event to Loops. If your event name is `completedOnboarding`, your call would look like this...

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  const resp = await loops.sendEvent({
    email: "user@gmail.com",
    eventName: "completedOnboarding",
  });

  if (!resp.success) {
  // The event was not sent
  } else {
  // The event was sent OK
  }

  ```

  ```typescript TypeScript theme={"dark"}
  const resp: {
    success: boolean,
    message?: string,
  } = await loops.sendEvent({
    email: "user@gmail.com",
    eventName: "completedOnboarding",
  });

  if (!resp.success) {
    // The event was not sent
  } else {
    // The event was sent OK
  }
  ```
</CodeGroup>

<CardGroup className="mt-8">
  <Card title="sendEvent()" href="/sdks/javascript#sendevent" icon="bolt">
    Read more in the SDK docs.
  </Card>
</CardGroup>

## Using the API instead

If you prefer, you can use the [Loops API](/api-reference) directly instead of using the SDK.

<Warning>
  You should never call the API from your front-end code as this will expose
  your API key.
</Warning>

For example, you can send a transactional email like this:

```javascript  theme={"dark"}
const data = {
  email: "user@gmail.com",
  transactionalId: "abcdefg",
  dataVariables: {
    loginUrl: "https://myapp.com/login/?code=1234",
  },
};
return fetch("https://app.loops.so/api/v1/transactional", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${process.env.LOOPS_API_KEY}`,
  },
  body: JSON.stringify(data),
})
  .then((response) => response.json())
  .then((response) => {
    if (!response.success) {
      // The sending failed
    } else {
      // The email was sent successfully
    }
  })
  .catch((err) => console.error(err));
```

<Tip>
  On Vercel, each backend function gets its own lambda. Make sure you use
  `return` otherwise the lambda might be terminated before the promise is
  evaluated.
</Tip>

<CardGroup>
  <Card title="API Reference" icon="rectangle-terminal" href="/api-reference">
    Read through our API documentation.
  </Card>
</CardGroup>
