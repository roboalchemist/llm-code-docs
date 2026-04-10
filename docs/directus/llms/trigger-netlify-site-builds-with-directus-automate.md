# Source: https://directus.io/docs/raw/tutorials/workflows/trigger-netlify-site-builds-with-directus-automate.md

# Trigger Netlify Site Builds with Directus Automate

> Learn how to trigger new Netlify website builds through Directus Automate.

## Explanation

When using Directus as a [Headless CMS](https://directus.io/solutions/headless-cms), it is common to pair it with a
front-end framework / static site generator like [Next.js](https://nextjs.org/), [Nuxt.js](https://nuxt.com),
[SvelteKit](https://kit.svelte.dev/), or other options.

[Netlify](https://www.netlify.com/) and other similar platforms make it easy to host and deploy your site using static
site generation (SSG) to render your site’s pages during build time, instead of waiting until a certain page is
requested.

This recipe will show you how to trigger a new deployment or build for your site when new content is published or when
existing content changes.

## How-To Guide

<callout icon="material-symbols:info-outline">

You’ll need to have already created a collection for your site content like `articles` or `posts` or `pages` with a
field `status` that controls the published state. You'll also need to have a Netlify account and a site already hosted
with them.

</callout>

### Create and Configure Your Flow

1. [Create a new flow](/guides/automate/flows)<br />

Give it a memorable name and short description like `Trigger New Site Build`.
2. [Complete the trigger setup](/guides/automate/triggers)<br />

![The trigger setup tab of the creating new flow interface is show. The event hook type is selected. The type field value is "Action(Non-Blocking)". In the scope field, "items.create" and "items.update" are selected.](/img/ee5eca7d-2bcb-4e73-b6b6-d638375282f6.webp)<br />

a. Choose **Event Hook** for the trigger.<br />

b. For **Type**, select Action (Non-Blocking).<br />

This will trigger this flow after the action (i.e. article updated) has already taken place.<br />

c. For **Scope**, choose the following:
  - `items.create`
  - `items.update`<br />

d. For **Collections**, choose any collections that should trigger this flow.<br />

In this case, we’ll use `Articles` and `Articles Translations`.

### Add an Operation to Check Status Field

> This step is optional but it is recommended to add a Condition operation to prevent unnecessary builds.

1. [Create a new Operation](/guides/automate/operations)<br />

![Within a Directus Flow, the Create Operation screen is shown. The Name of the Operation is "If Published". The Operation type is "Condition". The value of the Condition Rules field is a JSON object.](/img/4fb65e5f-8aa7-4683-96a4-6ba55ab93a7c.webp)<br />

a. Name your operation, i.e. `Check Status`, `If Published`, or similar.<br />

b. Add your Condition Rules```json
{
    "$trigger": {
        "payload": {
            "status": {
                "_eq": "published"
            }
        }
    }
}
```

### Configure Netlify Build Hook

<callout icon="material-symbols:info-outline">

You can learn more about Netlify Build Hooks on their documentation.

[https://docs.netlify.com/configure-builds/build-hooks/](https://docs.netlify.com/configure-builds/build-hooks/)

</callout>

1. Copy your Build Hook URL from Netlify<br />

a. Open your Netlify account<br />

b. Navigate to your site → Site Settings → Build & deploy → Build hooks<br />

c. **Create a new build hook and copy the unique URL.**

### Add Webhook Operation to Your Flow

1. Back inside your Directus Flow, create a new Operation.<br />

![Within a Directus Flow, the Create Operation screen is shown. The Name of the Operation is "Deploy Site". The Operation type is "Webhook / Request URL". The Method selected is "POST". The URL field value is the an HTTP address for the build hook from the hosting platform.](/img/f78a10ce-99ec-4eef-80bd-abd5154bfce6.webp)<br />

a. For the type of Operation, select **Webhook / Request URL**<br />

b. Change **Method** to POST<br />

c. Paste the Build Hook URL from Netlify into the **URL** field<br />

d. Save this Operation<br />

e. Save your Flow

### Publish Your Flow

Great job! Now whenever you update an item in the `articles` collection and the `status` is equal to `published` , your
hosting platform will automatically re-build your site.

## Final Tips

This recipe covers a basic example of triggering a static site build.

It can be used in addition to other Flows recipes to build a robust content approval and publishing workflow for your
sites and projects.

**Tips**

- Make sure to test your flow several times to ensure everything is working as expected.
- As you add other collections that are published on your static site or frontend, make sure you update this Flow to
include those collections in your Trigger.
