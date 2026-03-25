# Source: https://docs.mailtrap.io/guides/integrations/supabase/contacts-management.md

# Sync Contacts with Supabase

You can seamlessly sync your Supabase user base with Mailtrap, which allows you to:

* Seamlessly update your email list
* Create segments based on user data
* Launch personalized email campaigns
* Measure campaign effectiveness

In this guide, you'll learn how to:

* Generate a Mailtrap API token
* Create contacts in Supabase and Mailtrap
* Update contacts in Supabase and Mailtrap
* Demo and test the integration

{% hint style="info" %}
You can read more about Contacts in our [dedicated article](https://docs.mailtrap.io/guides/integrations/supabase/broken-reference).
{% endhint %}

## Generate a Mailtrap API token

Whether you want to only create contacts or update them via Mailtrap x Supabase, you'll first need a Mailtrap API token.

{% stepper %}
{% step %}
**Access API Tokens**

Go to **Settings** on the left side-bar menu, navigate to **API Tokens**, and click on **Add Token**.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-2cb1288df6f60ca8f3548963140bf9521b5482dd%2Fsupabase-contacts-integration-1.png?alt=media" alt="Mailtrap Settings page showing API Tokens section with Add Token button highlighted"></div>
{% endstep %}

{% step %}
**Configure Token Permissions**

Enter the desired name, click on **Add Token**, tick the desired permission checkboxes, and hit **Save**.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-7b92faf74ea0602d99a93ef3a57901d26fcbdbae%2Fsupabase-contacts-integration-2.png?alt=media" alt="Mailtrap API Token creation dialog with name field and permission checkboxes"></div>
{% endstep %}

{% step %}
**Copy and Store Token**

Copy the token and save it in a secure place.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-5120d84055568a89c845c2f5840f8c3b684a8526%2Fsupabase-contacts-integration-3.png?alt=media" alt="Mailtrap API Token display showing generated token ready to copy" width="375"></div>
{% endstep %}
{% endstepper %}

## Creating contacts

Before we start, let me briefly explain the workflow:

* A user registers in your app
* Their email appears not only in Supabase but also in the Contacts page
* Then, you can easily group the new contact into different lists, segments, etc.

### Step 1. Create an Edge Function in Supabase

First, let's create an Edge Function containing our Mailtrap API token.

{% stepper %}
{% step %}
**Open Edge Functions**

Open your Supabase [project dashboard](https://supabase.com/dashboard/projects) and go to **Edge Functions**.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-ae4a0062b553d7b686dfec45c700c60b876d4951%2Fsupabase-contacts-integration-4.png?alt=media" alt="Supabase project dashboard with Edge Functions navigation highlighted in sidebar"></div>
{% endstep %}

{% step %}
**Deploy New Function**

Click on **Deploy a new Function** in the upper-right corner and select **Via Editor**.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-b59fabb72189346837b04620f2a6c16eee18036e%2Fsupabase-contacts-integration-5.png?alt=media" alt="Supabase Edge Functions page showing Deploy a new Function button with dropdown menu"></div>
{% endstep %}

{% step %}
**Add Function Code**

Inside the function editor, you should see the default serverless function template.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-d5a1d5d21561f41faebc99babf8f4d43d7c132c0%2Fsupabase-contacts-integration-6.png?alt=media" alt="Supabase Edge Function editor showing default function template code"></div>

Replace it with the following code snippet that will send user data to Contacts:

{% code title="create-contact Edge Function" %}

```javascript
const MAILTRAP_API_TOKEN = Deno.env.get("MAILTRAP_TOKEN") || "";
const MAILTRAP_ACCOUNT_ID = Deno.env.get("MAILTRAP_ACCOUNT_ID") || "";

const handler = async (req) => {
  const requestData = await req.json();
  const { email } = requestData.record;
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Authorization": `Bearer ${MAILTRAP_API_TOKEN}`
    },
    body: JSON.stringify({
      contact: {
        email: email,
        list_ids: [
          4292 // List for New Users
        ]
      }
    })
  };
  return await fetch(`https://mailtrap.io/api/accounts/${MAILTRAP_ACCOUNT_ID}/contacts`, options);
};

Deno.serve(handler);
```

{% endcode %}

Replace the variable `list_ids:` value (4292 in this example) with the ID of the list where you want to add the contact.

Then, click on **Deploy Function**.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-b8aa9416c325e6b0596af0a3fad1c0c5c37e824a%2Fsupabase-contacts-integration-7.png?alt=media" alt="Supabase Edge Function editor with Deploy Function button highlighted"></div>
{% endstep %}

{% step %}
**Verify Deployment**

Supabase will build and deploy the Edge Function.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-590ae70c93ce5a212df6dc526dd2ced7c7570a20%2Fsupabase-contacts-integration-8.png?alt=media" alt="Supabase Edge Function deployment progress showing build and deploy status"></div>
{% endstep %}
{% endstepper %}

### Step 2. Set up webhooks for contact creation

Next, we will create a [Supabase Webhook](https://supabase.com/docs/guides/database/webhooks) to trigger the Edge Function we just created.

{% stepper %}
{% step %}
**Navigate to Database Webhooks**

Open your Supabase Dashboard, go to **Database Webhooks**, and click on **Create a new hook**.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-38e986f930b4e3774f23311dc30e80ca2d7eb00f%2Fsupabase-contacts-integration-9.png?alt=media" alt="Supabase Database page with Webhooks section and Create a new hook button"></div>
{% endstep %}

{% step %}
**Configure Basic Settings**

Configure the following:

* **Name**: create\_contact
* **Table**: users
* **Events**: ✅ Insert

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-e3992482ac9c3c320f2f1cf246f6d07914225bd8%2Fsupabase-contacts-integration-10.png?alt=media" alt="Supabase webhook configuration form showing name, table, and Insert event checkbox"></div>
{% endstep %}

{% step %}
**Configure Webhook Type**

Configure the following:

* Choose **Supabase Edge Functions** under 'Webhook configuration'
* Go for **POST** under 'Method'
* Select the previously created function **create-contact**
* Set the desired timeout (e.g., 5000)

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-c288914d9af7498809b009801359cd6a91fbb665%2Fsupabase-contacts-integration-11.png?alt=media" alt="Supabase webhook configuration showing Edge Functions type, POST method, and function selection"></div>
{% endstep %}

{% step %}
**Set HTTP Headers**

Set HTTP headers for Auth:

* **Content-type**: application/json
* **Authorization**: Bearer \[your-token]

Click **Create webhook** to activate it.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-73a4ae576885a883e39fd825341926ad39b4371a%2Fsupabase-contacts-integration-12.png?alt=media" alt="Supabase webhook HTTP headers configuration with Content-type and Authorization fields"></div>
{% endstep %}
{% endstepper %}

## Updating contacts

Here, the flow is quite similar to creating contacts, with the major difference being the code we'll use.

How it works:

* A registered user updates their name/account info
* The newly updated info appears not only in Supabase but also in the Mailtrap Contacts page
* Then, you can send more personalized emails (e.g., name or state fields)

### Step 1. Create an edge function

Again, we start by creating an Edge Function and adding Mailtrap API token to it.

{% stepper %}
{% step %}
**Open Edge Functions**

Open your Supabase [project dashboard](https://supabase.com/dashboard/projects) and go to **Edge Functions**.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-ae4a0062b553d7b686dfec45c700c60b876d4951%2Fsupabase-contacts-integration-4.png?alt=media" alt="Supabase project dashboard with Edge Functions navigation highlighted in sidebar"></div>
{% endstep %}

{% step %}
**Deploy New Function**

Click on **Deploy a new function** in the upper-right corner and select **Via Editor**.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-b59fabb72189346837b04620f2a6c16eee18036e%2Fsupabase-contacts-integration-5.png?alt=media" alt="Supabase Edge Functions page showing Deploy a new function button with dropdown menu"></div>
{% endstep %}

{% step %}
**Add Function Code**

Inside the function editor, you should see the default serverless function template.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-d5a1d5d21561f41faebc99babf8f4d43d7c132c0%2Fsupabase-contacts-integration-6.png?alt=media" alt="Supabase Edge Function editor showing default function template code"></div>

Replace it with the following code snippet, which will:

* Receive user data from the webhook
* Call the Mailtrap API to update existing contact details

{% code title="update-contact Edge Function" %}

```javascript
// Setup type definitions for built-in Supabase Runtime APIs
import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from 'jsr:@supabase/supabase-js@2';

// Define environment variables (you'll need to set these in Supabase)
const MAILTRAP_API_TOKEN = Deno.env.get("MAILTRAP_TOKEN") || "";
const MAILTRAP_ACCOUNT_ID = Deno.env.get("MAILTRAP_ACCOUNT_ID") || "";

const handler = async (req) => {
  const requestData = await req.json();
  let userEmail;
  try {
    const supabase = createClient(Deno.env.get('SUPABASE_URL'), Deno.env.get('SUPABASE_SERVICE_ROLE_KEY'), {
      auth: {
        autoRefreshToken: false,
        persistSession: false
      }
    });
    // Access auth admin api
    const { data, error } = await supabase.auth.admin.getUserById(requestData.record.id);
    if (error) {
      throw error;
    }
    userEmail = data.user.email;
  } catch (err) {
    // error handling
  }
  const options = {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Authorization": `Bearer ${MAILTRAP_API_TOKEN}`
    },
    body: JSON.stringify({
      contact: {
        email: userEmail,
        fields: {
          name: requestData.record.full_name
        },
        unsubscribed: false
      }
    })
  };
  return await fetch(`https://mailtrap.io/api/accounts/${MAILTRAP_ACCOUNT_ID}/contacts/${userEmail}`, options);
};

Deno.serve(handler);
```

{% endcode %}

And, of course, click on **Deploy updates/Deploy function**.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-78123c59002983342c38853d0a1fbf8a33d5b93f%2Fsupabase-contacts-integration-16.png?alt=media" alt="Supabase Edge Function editor with Deploy function button highlighted"></div>
{% endstep %}
{% endstepper %}

### Step 2. Set up a webhook for updating contacts

{% stepper %}
{% step %}
**Create Webhook**

If you don't already have a webhook for updating contacts, open your Supabase Dashboard, go to **Database Webhooks**, and click on **Create a new hook**.

Navigate to **Integrations** → **Webhooks** and configure the following:

* **Name**: update\_contact
* **Table**: profiles
* **Events**: ✅ Update

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-bc0570236856bf9800f7237d85bb9e61d2171a6d%2Fsupabase-contacts-integration-17.png?alt=media" alt="Supabase webhook configuration form showing name set to update_contact, table set to profiles, and Update event checkbox"></div>
{% endstep %}

{% step %}
**Configure Webhook Settings**

Configure the following:

* **Type of webhook**: HTTP Request
* **Method**: POST
* **Edge Function**: Select the previously created **update-contact** function
* **Add HTTP Headers**:
  * **Content-Type**: application/json
  * **Authorization**: Bearer \[your-token]

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-6e72c06ce59fc1c33276ce3b884167ede310ba71%2Fsupabase-contacts-integration-18.png?alt=media" alt="Supabase webhook configuration showing HTTP Request type, POST method, Edge Function selection, and HTTP headers"></div>
{% endstep %}
{% endstepper %}

## Integration demo and testing

Finally, let's test our webhook configuration. For this example, I'll use a demo app created in FlutterFlow.

{% stepper %}
{% step %}
**Create Test Account**

First, create an account as if you were a new user.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-f086de699b2156c4e1763b8342de9e8ba805e3e7%2Fsupabase-contacts-integration-19.png?alt=media" alt="" width="145"></div>
{% endstep %}

{% step %}
**Verify in Supabase**

A new user should appear in the **Users** page within your Supabase Project.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-0619e5ea89b324d9d33bfb84f26cf1d152dd623a%2Fsupabase-contacts-integration-20.png?alt=media" alt="Supabase Authentication Users page showing newly created user in table"></div>
{% endstep %}

{% step %}
**Verify in Mailtrap**

At the same time, a new user also appears in your Mailtrap Contacts page.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-0cdacb41a06c88477f61bf3efa0d40ec2ac9038a%2Fsupabase-contacts-integration-21.png?alt=media" alt="Mailtrap Contacts page showing newly synced contact with email address"></div>
{% endstep %}

{% step %}
**Check Initial Data**

Since the demo app only requires email and password upon registration, that's all the info the webhook sends to the Mailtrap Contacts page initially.

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-76e9f8e3be1cedb677f1fa28bec7ebe1fee7feaf%2Fsupabase-contacts-integration-22.png?alt=media" alt="Mailtrap contact detail showing only email field populated"></div>
{% endstep %}

{% step %}
**Update Profile**

If you go to your demo app and update the profile name...

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-4e4143a5ee39c20d1374d03cc382009a3b0b5cd3%2Fsupabase-contacts-integration-23.png?alt=media" alt="" width="146"></div>
{% endstep %}

{% step %}
**Verify Update in Supabase**

It should get updated in your Supabase Project...

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-87284f3308165afcb670e526c2f387703388355b%2Fsupabase-contacts-integration-24.png?alt=media" alt="Supabase profiles table showing updated full_name field"></div>
{% endstep %}

{% step %}
**Verify Update in Mailtrap**

And the Mailtrap Contacts Page, so everything works as intended!

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-bbc1851165fdf7fc88fa5d2b36602d0da3ad8099%2Fsupabase-contacts-integration-25.png?alt=media" alt="Mailtrap Contacts page showing updated contact with name field now populated"></div>

Now, every time a new user logs in and updates their name, their information will be logged in your Mailtrap Contacts page. There, you can group them into lists, segment them accordingly, and use Fields to personalize your email campaigns further.
{% endstep %}
{% endstepper %}
