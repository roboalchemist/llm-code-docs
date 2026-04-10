# Source: https://dub.co/docs/conversions/leads/appwrite.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Appwrite

> Learn how to track lead conversion events with Appwrite and Dub

<Note>
  Conversion tracking requires a [Business plan](https://dub.co/pricing)
  subscription or higher.
</Note>

When it comes to [conversion tracking](/conversions/quickstart), a `lead` event happens when a user performs an action that indicates interest in your product or service. This could be anything from:

* Signing up for an account
* Booking a demo meeting
* Joining a mailing list

<Frame>
  <img className="rounded-lg border border-gray-100" src="https://assets.dub.co/help/conversion-lead-event.png" alt="A diagram showing how lead events are tracked in the conversion funnel" />
</Frame>

In this guide, we will be focusing on tracking new user sign-ups for a SaaS application that uses Appwrite for user authentication.

## Prerequisites

First, you'll need to enable conversion tracking for your Dub links to be able to start tracking conversions:

<Tip>
  If you're using [Dub Partners](/partners/quickstart), you can skip this step
  since partner links will have conversion tracking enabled by default.
</Tip>

<AccordionGroup>
  <Accordion title="Option 1: On a workspace-level">
    To enable conversion tracking for all future links in a workspace, you can do the following:
    To enable conversion tracking for all future links in a workspace, you can do the following:

    1. Navigate to your [workspace's Analytics settings page](https://app.dub.co/settings/analytics).
    2. Toggle the **Workspace-level Conversion Tracking** switch to enable conversion tracking for the workspace.

    <Frame>
      <img src="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=f810945d33a42f45de3e06647b2cfd15" alt="Enabling conversion tracking for a workspace" data-og-width="3082" width="3082" data-og-height="1529" height="1529" data-path="images/conversions/enable-conversion-tracking-workspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=280&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=514f7549b9a65a40fc4224ea68859e06 280w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=560&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=9c002882f7093efb76ae4be72e5f0312 560w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=840&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=d4da71527556174d30b71c0f9acdad6f 840w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=1100&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=c887363f92b258c3493267e2f4a3dd8e 1100w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=1650&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=e1b23eb5cf148df63105fdc572e6936b 1650w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=2500&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=1623f4206427342d87df828a17d66438 2500w" />
    </Frame>

    This option will enable conversion tracking in the [Dub Link Builder](https://dub.co/help/article/dub-link-builder) for all future links.
  </Accordion>

  <Accordion title="Option 2: On a link-level">
    If you don't want to enable conversion tracking for all your links in a workspace, you can also opt to enable it on a link-level.

    To enable conversion tracking for a specific link, open the [Dub Link Builder](https://dub.co/help/article/dub-link-builder) for a link and toggle the **Conversion Tracking** switch.

    <Frame>
      <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=4153d4a981e2a13324464ca3d30625cd" alt="Enabling conversion tracking for a link" data-og-width="2345" width="2345" data-og-height="908" height="908" data-path="images/conversions/enable-conversion-tracking.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=0984b50a4b6987e7bc4f8f3975559d0e 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=673093d978579d5cd19e22b2c786f6a4 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=94cb269be979162dd8bb74b2a5b614e9 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=4572ec2e03c96b50d1da93f8b3f04636 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=f0a017e718cc81ae682e89809e4dab25 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=078ec13ca0166c3b751d24271c1d2171 2500w" />
    </Frame>

    <Tip>
      You can also use the `C` keyboard shortcut when inside the link builder to
      quickly enable conversion tracking for a given link.
    </Tip>
  </Accordion>

  <Accordion title="Option 3: Via the API">
    Alternatively, you can also enable conversion tracking programmatically via the [Dub API](/api-reference/introduction). All you need to do is pass `trackConversion: true` when creating or updating a link:

    <CodeGroup>
      ```javascript Node.js theme={null}
      const link = await dub.links.create({
        url: "https://dub.co",
        trackConversion: true,
      });
      ```

      ```python Python theme={null}
      link = d.links.create(url="https://dub.co", track_conversion=True)
      ```

      ```go Go theme={null}
      link, err := d.Links.Create(ctx, &dub.CreateLinkRequest{
          URL: "https://dub.co",
          TrackConversion: true,
      })
      ```

      ```ruby Ruby theme={null}
      s.links.create_many(
        ::OpenApiSDK::Operations::CreateLinkRequest.new(
          url: "https://dub.co",
          track_conversion: true,
        )
      )
      ```
    </CodeGroup>
  </Accordion>
</AccordionGroup>

Then, you'd want to install the `@dub/analytics` script to your website to track conversion events.

You can install the `@dub/analytics` script in several different ways:

<CardGroup>
  <Card title="React" icon="react" href="/sdks/client-side/installation-guides/react" horizontal />

  <Card title="Manual installation" icon="browser" href="/sdks/client-side/installation-guides/manual" horizontal />

  <Card
    title="Framer"
    icon={
    <svg
      width="74"
      height="111"
      viewBox="0 0 74 111"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className="w-7 h-7"
    >
      <path d="M0 0H73.8374V36.9892H36.9187L0 0Z" fill="#eb5611" />
      <path d="M0 36.989H36.9187L73.8374 73.9796H0V36.989Z" fill="#eb5611" />
      <path d="M0 73.9797H36.9187V110.97L0 73.9797Z" fill="#eb5611" />
    </svg>
  }
    href="/sdks/client-side/installation-guides/framer"
    horizontal
  />

  <Card title="Shopify" icon="shopify" href="/sdks/client-side/installation-guides/shopify" horizontal />

  <Card title="WordPress" icon="wordpress" href="/sdks/client-side/installation-guides/wordpress" horizontal />

  <Card title="Webflow" icon="webflow" href="/sdks/client-side/installation-guides/webflow" horizontal />

  <Card title="Google Tag Manager" icon="google" href="/sdks/client-side/installation-guides/google-tag-manager" horizontal />
</CardGroup>

<Check>
  You can **verify the installation** with the following tests:

  1. Open the browser console and type in `_dubAnalytics` – if the script is installed correctly, you should see the `_dubAnalytics` object in the console.
  2. Add the `?dub_id=test` query parameter to your website URL and make sure that the `dub_id` cookie is being set in your browser.

  If both of these checks pass, the script is installed correctly. Otherwise, please make sure:

  * The analytics script was added to the `<head>` section of the page
  * If you're using a content delivery network (CDN), make sure to purge any cached content
</Check>

## Configure Appwrite

Next, configure Appwrite to track lead conversion events during the sign up process.

<Steps>
  <Step title="Create an Appwrite Cloud project">
    Head to [Appwrite Cloud](https://apwr.dev/appwrite-dub) and create a new project.

    <Frame>
      <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/appwrite/appwrite-new-project.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=1e110fd5a9d9ad54ba839c24261962c2" alt="New project on Appwrite Cloud" width="1440" height="1024" data-og-width="2880" data-og-height="2048" data-path="images/conversions/appwrite/appwrite-new-project.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/appwrite/appwrite-new-project.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=3a1a964f50dc62a182ac3add5aa471b2 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/appwrite/appwrite-new-project.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=98af772dee7536aafc84554cb6c5d9fb 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/appwrite/appwrite-new-project.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=393d9341b1d65c43efb12fa22f21000d 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/appwrite/appwrite-new-project.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=97c305eeaf3052ea8b14849d13d926a1 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/appwrite/appwrite-new-project.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=82e3bf852e376a686a797716fe167988 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/appwrite/appwrite-new-project.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=c1b734e06d94d1a7bf78510fc0ed9b19 2500w" />
    </Frame>

    Create a new API key with the `sessions.write` scope enabled and save the API key for later use. You can also copy your project ID and endpoint from the project's Settings page.

    <Frame>
      <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/appwrite/appwrite-api-key.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=17ca65fff8249659fd7ac45e7ecf2739" alt="API key in your project on Appwrite Cloud" width="1440" height="1024" data-og-width="2880" data-og-height="2048" data-path="images/conversions/appwrite/appwrite-api-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/appwrite/appwrite-api-key.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=c9c7691347137711e4012b3e05597b86 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/appwrite/appwrite-api-key.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=3de18fff94be16a7c53b61b39cd4faf5 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/appwrite/appwrite-api-key.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=ad73daf37ade8b17d8efc8e68876a93b 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/appwrite/appwrite-api-key.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=e878d605bad457ba334f12171269adeb 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/appwrite/appwrite-api-key.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=60dac77d056765af6d260aeafe0bbb06 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/appwrite/appwrite-api-key.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=9d17998d19d2d03a3683d32b9021dd07 2500w" />
    </Frame>

    Then, in your Next.js app, install the Appwrite Node.js SDK.

    ```bash  theme={null}
    npm i node-appwrite
    ```
  </Step>

  <Step title="Add environment variables">
    Add the following environment variables to your app.

    ```bash  theme={null}
    NEXT_PUBLIC_APPWRITE_ENDPOINT=https://cloud.appwrite.io/v1
    NEXT_PUBLIC_APPWRITE_PROJECT=<APPWRITE_PROJECT_ID>
    NEXT_APPWRITE_KEY=<APPWRITE_API_KEY>
    NEXT_DUB_API_KEY=<DUB_API_KEY>
    ```
  </Step>

  <Step title="Integrate Dub Analytics">
    Add the `DubAnalytics` component from the `@dub/analytics` package to your app’s root layout.

    ```tsx src/app/layout.tsx theme={null}
    import type { Metadata } from 'next';
    import { Analytics as DubAnalytics } from '@dub/analytics/react';

    export const metadata: Metadata = {
      title: 'Appwrite Dub Leads Example',
      description: 'Appwrite Dub Leads Tracking example app with Next.js'
    };

    export default function RootLayout({
      children
    }: Readonly<{
      children: React.ReactNode;
    }>) {
      return (
        <html lang="en">
          <body>{children}</body>
          <DubAnalytics />
        </html>
      );
    }
    ```
  </Step>

  <Step title="Prepare the Appwrite client and auth library">
    Create the Appwrite Session and Admin client (necessary for SSR apps, as explained in the [Appwrite docs](https://appwrite.io/docs/products/auth/server-side-rendering)). Additionally, create a function to verify user login.

    ```ts src/lib/server/appwrite.ts theme={null}
    'use server';
    import { Client, Account } from 'node-appwrite';
    import { cookies } from 'next/headers';

    export async function createSessionClient() {
      const client = new Client()
        .setEndpoint(process.env.NEXT_PUBLIC_APPWRITE_ENDPOINT as string)
        .setProject(process.env.NEXT_PUBLIC_APPWRITE_PROJECT as string);

      const session = (await cookies()).get('my-custom-session');
      if (!session || !session.value) {
        throw new Error('No session');
      }

      client.setSession(session.value);

      return {
        get account() {
          return new Account(client);
        }
      };
    }

    export async function createAdminClient() {
      const client = new Client()
        .setEndpoint(process.env.NEXT_PUBLIC_APPWRITE_ENDPOINT as string)
        .setProject(process.env.NEXT_PUBLIC_APPWRITE_PROJECT as string)
        .setKey(process.env.NEXT_APPWRITE_KEY as string);

      return {
        get account() {
          return new Account(client);
        }
      };
    }
    ```
  </Step>

  <Step title="Set up Dub SDK">
    Create the Dub client and send leads to Dub using the `dub.track.lead()` function.

    ```ts src/lib/server/dub.ts theme={null}
    import type { Models } from 'node-appwrite';
    import { Dub } from 'dub';

    const dub = new Dub({
      token: process.env.NEXT_DUB_API_KEY
    });

    export function addDubLead(user: Models.User<Models.Preferences>, dub_id: string) {
      dub.track.lead({
        clickId: dub_id,
        eventName: 'Sign Up',
        customerExternalId: user.$id,
        customerName: user.name,
        customerEmail: user.email
      });
    }
    ```
  </Step>

  <Step title="Send leads to Dub on user signup">
    In the `/auth` page, use the Appwrite Admin client to allow users to sign up. Post sign up, check if the `dub_id` cookie is present, send a lead event to Dub if found, and delete the `dub_id` cookie.

    ```tsx src/app/auth/page.tsx theme={null}
    import { ID } from 'node-appwrite';
    import { createAdminClient, getLoggedInUser } from '@/lib/server/appwrite';
    import { cookies } from 'next/headers';
    import { redirect } from 'next/navigation';
    import { addDubLead } from '@/lib/server/dub';

    async function signUpWithEmail(formData: any) {
      'use server';

      // Get sign up info from form
      const email = formData.get('email');
      const password = formData.get('password');
      const name = formData.get('name');

      // Create account and session using Appwrite
      const { account } = await createAdminClient();

      const user = await account.create(ID.unique(), email, password, name);
      const session = await account.createEmailPasswordSession(email, password);

      (await cookies()).set('my-custom-session', session.secret, {
        path: '/',
        httpOnly: true,
        sameSite: 'strict',
        secure: true
      });

      // Check if Dub ID is present in cookies and track lead if found
      const dub_id = (await cookies()).get('dub_id')?.value;
      if (dub_id) {
        addDubLead(user, dub_id);
        (await cookies()).delete('dub_id');
      }

      // Redirect to success page
      redirect('/auth/success');
    }

    export default async function SignUpPage() {

      // Verify active user session and redirect to success page if found
      const user = await getLoggedInUser();
      if (user) redirect('/auth/success');

      return (
        <>
          <form action={signUpWithEmail}>
            <input id="email" name="email" placeholder="Email" type="email" required />
            <input id="password" name="password" placeholder="Password" minLength={8} type="password" required />
            <input id="name" name="name" placeholder="Name" type="text" required />
            <button type="submit">Sign up</button>
          </form>
        </>
      );
    }
    ```
  </Step>
</Steps>

Here's the full list of attributes you can pass when sending a lead event:

| Property             | Required | Description                                                                                                                                                                                                                                                                                                                                                                       |
| :------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `clickId`            | **Yes**  | The unique ID of the click that the lead conversion event is attributed to. You can read this value from `dub_id` cookie. If an empty string is provided (i.e. if you're using [tracking a deferred lead event](/conversions/leads/deferred)), Dub will try to find an existing customer with the provided `customerExternalId` and use the `clickId` from the customer if found. |
| `eventName`          | **Yes**  | The name of the lead event to track. Can also be used as a unique identifier to associate a given lead event for a customer for a subsequent sale event (via the `leadEventName` prop in `/track/sale`).                                                                                                                                                                          |
| `customerExternalId` | **Yes**  | The unique ID of the customer in your system. Will be used to identify and attribute all future events to this customer.                                                                                                                                                                                                                                                          |
| `customerName`       | No       | The name of the customer. If not passed, a random name will be generated (e.g. "Big Red Caribou").                                                                                                                                                                                                                                                                                |
| `customerEmail`      | No       | The email address of the customer.                                                                                                                                                                                                                                                                                                                                                |
| `customerAvatar`     | No       | The avatar URL of the customer.                                                                                                                                                                                                                                                                                                                                                   |
| `mode`               | No       | The mode to use for tracking the lead event. `async` will not block the request; `wait` will block the request until the lead event is fully recorded in Dub; `deferred` will defer the lead event creation to a subsequent request.                                                                                                                                              |
| `metadata`           | No       | Additional metadata to be stored with the lead event. Max 10,000 characters.                                                                                                                                                                                                                                                                                                      |

## Example App

To learn more about how to track leads with Appwrite, check out the following example app:

<Card title="Appwrite + Dub Next.js  Example" icon="github" href="https://github.com/appwrite-community/appwrite-dub-next">
  See how to track new user sign-ups with Appwrite and the Dub SDK.
</Card>

## View your conversions

Once you've completed the setup, all your tracked conversions will show up in [Dub Analytics](https://dub.co/analytics). We provide 3 different views to help you understand your conversions:

* **Time-series**: A [time-series view](https://app.dub.co/dub/analytics?view=timeseries) of the number clicks, leads and sales.

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=7380bc6120ade538b2b65eefdc76d3ed" alt="Time-series line chart" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/timeseries-chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=430758e529cd22c5d28f976ee7da5379 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=9cf861c9aa7cf680f46ce32585303d2b 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=999b05a7805bd208b4649fc67a3b45e0 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=42baa1d9d42c26ed191875fef033128a 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=127ee673f66f2079f236985ec754416e 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=1c0696bb18043dd86388f03d09aed450 2500w" />
</Frame>

* **Funnel chart**: A [funnel chart view](http://app.dub.co/analytics?view=funnel) visualizing the conversion & dropoff rates across the different steps in the conversion funnel (clicks → leads → sales).

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=6275caafcfc3be6d8b498149222f225e" alt="Funnel chart view showing the conversion & dropoff rates from clicks → leads → sales" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/funnel-chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=df57b14d04dd585c5236f6fcf16a4963 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=fc1689a06ce8ceecf1487faca8730d06 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=b69533d460a2bc95964d7f6d2e5f23f4 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=43b86431662a4c214a36fbf5405abb4a 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=687f900f0b8732301c43c8ee18ca7dd4 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=aed9e63c7fd1fb67c463920c73911cba 2500w" />
</Frame>

* **Real-time events stream**: A [real-time events stream](https://app.dub.co/events) of every single conversion event that occurs across all your links in your workspace.

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=c2467f9fa2e755f06b3e7b147fa0bd81" alt="The Events Stream dashboard on Dub" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/events-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=8e747ccc2f01015e014a9b4fbc98d588 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=4a0c65b37cf99181b712beb063e46dc2 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=345d5b0b36c6f2093ea7b6a97d73ff49 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=5deb48ab5e08bf2e31447fd32615c05e 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=33d6f27b5c067eb8586cfea15fe0a040 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=132a7592c8ecf518b31c043dad2093f4 2500w" />
</Frame>
