# Source: https://www.metabase.com/docs/latest/embedding/embedded-analytics-js

<div>

1.  [Home](/docs/latest/)
2.  [Embedding](/docs/latest/embedding/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Embedded analytics JS

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

Embedded analytics JS is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (both self-hosted and on Metabase Cloud).

Embedded analytics JS lets you embed Metabase entities like questions, dashboards, or even the query builder into your own application using customizable components.

<div>

[![interactive-embedding-workshop](/images/events/categories/embedding-workshop.png)](/events/interactive-embedding-workshop)

<div>

Embed a real dashboard in just 30 minutes.

Join our next Embedded Analytics Workshop![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+)

</div>

</div>

Embedded Analytics JS is a JavaScript library built on top of Metabase's [Embedded Analytics React SDK](./sdk/introduction). But it does not require using React or setting up full SDK embedding. Unlike with [interactive embedding](./interactive-embedding), where you embed the entire Metabase app in an iframe, Embedded Analytics JS lets you choose from a set of predefined components like a single chart, a dashboard with optional drill-through, or query builder, and customize those components.

Embedded Analytics JS uses [JWT](../people-and-groups/authenticating-with-jwt) or [SAML](../people-and-groups/authenticating-with-saml) to authenticate people and automatically apply the right permissions.

Currently you can choose to embed:

-   A dashboard
-   A question (chart). You can embed both questions built with the query builder and questions built with SQL.
-   Full graphical [query builder](../questions/query-builder/editor) to enable people to build their own charts and explorations.
-   A browser to navigate collections and open dashboards or questions.
-   [AI chat interface](./sdk/ai-chat).

## Quickstart

You can also follow the setup guide directly in Metabase in **Admin settings \> Embedding \> Setup guide**. We're recording the steps here for convenience.

### 1. Enable Embedded Analytics JS 

1.  In Metabase, go to **Admin settings \> Embedding \> Modular embedding**.
2.  Toggle on **Embedded Analytics JS**.
3.  Under **Cross-Origin Resource Sharing (CORS)**, add the URLs of the websites where you want to embed Metabase (such as `https://*.example.com`). For testing embeds, you can use `localhost` which is always included in CORS policy.
4.  If you are embedding Metabase components in a domain that's different from your Metabase's domain (including when you're testing the app locally but use Metabase Cloud), go to **Admin settings \> Embedding \> Security** and set **SameSite cookie** to **None**.

### 2. Create a new embed 

1.  In Metabase, go to **Admin \> Embedding \> Modular embedding**, and select **New embed** next to **Embedded analytics JS**.

    If you're planning to embed an existing question or dashboard, you can instead go straight to that question or dashboard, click on the **Share** button, and choose **Embedded Analytics JS**.

2.  Choose the *type* of entity to embed:

    -   Dashboard
    -   Chart
    -   Exploration (which will embed the Metabase query builder)
    -   Browser
    -   Metabot question (which will embed AI chat)

3.  Next, select the entity you want to embed. For browser, pick the collection you want people to start from.

Once you've selected what you want to embed, click Next to customize your embed.

### 3. Customize your embed 

The exact customization options you see will depend on what type of entity you're embedding. You'll see a live preview of how the embed will look with your chosen options. Check out [Customizing embeds](#customizing-embeds) for more details on customization options.

![Customizing embeds](./images/embed-flow-options.png)

You'll also be able to pick brand, text, and background color used for all your embeds. To configure other colors (e.g. secondary colors, query builder colors etc), as well as font, you can specify a [theme](#theming) in your embed code snippet.

All the customization options you select in this interactive flow will be reflected in the parameter values in the embed code, so you'll be able to adjust them later by editing the embed snippet.

Once you're done customizing your embed, click "Next".

### 4. Select authentication method 

You'll get a choice between "Existing Metabase session" and "Single sign-on (SSO)".

-   If you select **Existing Metabase session**, you'll be able to preview your embeds as the user you're currently logged into Metabase, and only in the same browser as your current session. Not all browsers are supported - we recommend using Google Chrome. To test out embedding in other contexts, you can use [API keys](#use-api-keys-to-test-embeds) instead. For production usage, use [SSO](#set-up-sso).

-   If you set up JWT in your Metabase instance, you'll be able to select **Single sign-on (SSO)**, see [Set up SSO](#set-up-sso).

### 5. Add the embedding script into your app 

Metabase will generate a code snippet that you can copy and paste into your app, see [Embed code snippets](#embed-code-snippets) for an example. You can later modify this code snippet to specify additional appearance options or change the behavior of some components.

Add the code snippet into your app, and refresh the page.

## Each end user should have their own Metabase account

Each end-user must have their own Metabase account.

The problem with having end-users share a Metabase account is that, even if you filter data on the client side via the Embedded analytics JS, all end-users will still have access to the session token, which they could use to access Metabase directly via the API to get data they're not supposed to see.

If each end-user has their own Metabase account, however, you can configure permissions in Metabase and everyone will only have access to the data they should.

In addition to this, we consider shared accounts to be unfair usage. Fair usage of Embedded Analytics JS involves giving each end-user of the embedded analytics their own Metabase account.

## Embed code snippets

The code snippets to embed Metabase entities using Embedded Analytics JS should have three parts:

1.  Loading the Embedded Analytics JS library from your Metabase instance.
2.  Global configuration settings to be used for all embeds, like the URL of your Metabase instance, appearance themes, etc. See [Configuring embeds](#configuring-embeds).
3.  Components for Metabase entities to be embedded, with their parameters. See [Components](#components).

Here's an example of a script:

``` highlight
<!-- Load embedding library -->
<!-- REPLACE WITH YOUR METABASE URL HERE -->
<script defer src="https://your-metabase-url/app/embed.js"></script>
<script>
  function defineMetabaseConfig(config) 
</script>

<!-- Embedding configuration -->
<script>
  defineMetabaseConfig(,
    },
  });
</script>

<!--Embedded entities -->
<metabase-question question-id="1"></metabase-question>

<metabase-dashboard dashboard-id="2" with-title="false"></metabase-dashboard>
```

Note the `defer` attribute and the reference to your Metabase URL in the script that loads `embed.js` library.

If you're embedding multiple entities in a single page, you only need to include the `<script>` tags once globally.

You can also generate the code snippet for Embedded Analytics JS interactively in Metabase through **Admin \> Embedding \> Setup guide \> Embed in your code**. Check out the [quickstart](#quickstart).

## Customizing embeds

The exact customization options you see will depend on what type of entity you're embedding.

When you're creating a new embed using **Admin \> Embedding \> Setup guide \> Embed in your code**, you'll see the following customization options in the interactive creation flow. These options correspond to parameters in [components](#components).

-   **Allow people to drill through on data points**: determines whether people can interact with the chart (or charts on a dashboard). Interactivity includes [drilling down](/learn/metabase-basics/querying-and-dashboards/questions/drill-through) to individual records from aggregated questions, filtering on click, zooming in, etc. Disabling drill-through for an embedded *question* also disables people's ability to add filters and summaries.

-   **Allow downloads**: determines whether people can download question results and save dashboards as PDFs.

-   **Allow people to save new questions**. If you embed the query builder but disable this option, people can still do their own explorations, they just won't be able to save them.

-   **Parameters**: for dashboard filters, SQL variables, and time grouping parameters, you can add default values. Default values set here override the default values set at the dashboard or question level. For dashboard filters and parameters, you can choose whether to hide the parameter.

-   **Show title**: what it says on the tin.

-   **Allow editing dashboards and questions**: lets people create and edit dashboards or questions in the current collection. When disabled, they can still perform actions like filter, summarize, and drill-through, but won't be able to save results.

## Configuring embeds

To define the configuration that applies to every embed on the page, use the `defineMetabaseConfig()` function. Its parameters include:

-   `instanceUrl: "https://your-metabase-url"` (required): the URL of your Metabase instance, like `https://youlooknicetoday.metabaseapp.com`

-   `theme: ` (optional): [appearance options for the embeds](#theming).

-   `useExistingUserSession: true|false` (optional, for development only) - lets you preview the embed locally using your Metabase admin account session. Only supported in Google Chrome.

-   `apiKey: mb_YourAPIKey` (optional, for development only) - another way to preview embeds locally using an API key.

-   `fetchRequestToken: () => Promise<>` (optional) - you can customize how the SDK fetches the refresh token for JWT authentication by specifying the `fetchRequestToken` function. See [customizing JWT authentication](./sdk/authentication#customizing-jwt-authentication).

### Theming

You can specify colors, fonts, spacing, and other appearance options using the `theme` parameter in your embed configuration.

For example, this code defines the font, color, and size for text, background colors, and colors for filters and summaries:

``` highlight
<script>
  defineMetabaseConfig(,
    },
  });
</script>
```

See [appearance](./sdk/appearance).

## Authentication

### Use existing user session to test embeds

> Existing sessions can only be used for testing embeds locally. To make your embeds production-ready, you'll need to implement SSO.

If you're signed into Metabase, you can use that existing session cookie to preview and test your embeds. This only works in the same browser (we recommend Chrome) you're using for your Metabase session (so it won't work in Incognito mode).

Add `useExistingUserSession: true` to `defineMetabaseConfig()` in your embed code. Check out [Configuring embeds](#configuring-embeds).

``` highlight
<script>
  defineMetabaseConfig();
</script>
```

Note that this will not work in some browsers, or in incognito mode. We recommend using Chrome if you'd like to use existing Metabase sessions to test your embeds.

### Use API keys to test embeds

> API keys can only be used for testing embeds locally. To make your embeds production-ready or deploy them to another domain, you'll need to implement SSO.

To use an API key to test your embeds:

1.  Create an [API key](../people-and-groups/api-keys)
2.  Add `apiKey: "YOUR_API_KEY"` to `defineMetabaseConfig()`:

``` highlight
<script>
  defineMetabaseConfig();
</script>
```

API keys should only be used for testing with trusted people. Anyone with access to the front-end can grab the API key and use it to make requests against the Metabase API. For this reason, we only allow using API keys on localhost.

### Set up SSO

SSO is required to embed in a domain other than localhost. You can use JWT or SAML SSO. To configure SAML, check out [Authenticating with SAML](./sdk/authentication#authenticating-with-saml-sso). To configure JWT, follow the steps below.

#### 1. In Metabase, configure [JWT SSO](../people-and-groups/authenticating-with-jwt). 

#### 2. In your app's backend, add a new endpoint to handle authentication. 

You'll need to add a library to your backend to sign your JSON Web Tokens.

For Node.js, we recommend jsonwebtoken:

``` highlight
npm install jsonwebtoken --save
```

Next, set up an endpoint on your backend (like `/sso/metabase`) that uses your Metabase JWT shared secret to generate a JWT for the authenticated person. **This endpoint must return a JSON object with a `jwt` property containing the signed JWT.** For example: ``.

This example code for Node.js sets up an endpoint using Express:

``` highlight
import express from "express";
import cors from "cors";
import session from "express-session";
import jwt from "jsonwebtoken";
import fetch from "node-fetch";

// Replace this with your Metabase URL
const METABASE_INSTANCE_URL = "YOUR_METABASE_URL_HERE";
// Replace this with the JWT signing secret you generated when enabling
// JWT SSO in your Metabase.
const METABASE_JWT_SHARED_SECRET = "YOUR_SECRET_HERE";

const app = express();

app.get("/sso/metabase", async (req, res) =>  = req.session;
  const user = ;

  if (!user) );

    return;
  }

  const token = jwt.sign(
    ,
    METABASE_JWT_SHARED_SECRET,
  );
  // The user backend should return a JSON object with the JWT.
  res.status(200).json();
});
```

See more examples in the [Embedding SDK docs](./sdk/authentication#2-add-a-new-endpoint-to-your-backend-to-handle-authentication).

#### 3. Embeds will use SSO automatically by default 

By default, Metabase uses JWT SSO, but you can specify another auth method. To turn on SSO, make sure you *don't* set your configuration to `apiKey` or `useExistingUserSession`.

## Components

There are different components available that enable different experiences for the end-user.

> While you can use component parameters to show or hide parts of the embedded component, these parameters are *not* a substitute for [permissions](../permissions/start). Even if you hide stuff, people could still grab their token from the frontend and use it to query the Metabase API.

### Dashboard

To render a dashboard:

``` highlight
<metabase-dashboard dashboard-id="1" with-title="true" with-downloads="false">
</metabase-dashboard>
```

**Required parameters:**

-   `dashboard-id` - This can be a regular ID or an entity ID. [Using Entity IDs](../installation-and-operation/serialization#entity-ids-work-with-embedding) in your embeds ensures that the IDs stay stable when exporting from one Metabase and importing to another.

**Optional parameters:**

-   `with-title` (default is true) - show the dashboard title in the embed

-   `with-downloads` (default is false) - show the button to download the dashboard as PDF and download question results

-   `drills` (default is true) - lets you drill through the dashboard

-   `initial-parameters` - default value for dashboard filters, like ``.

    Make sure to use single quotes if you are surrounding your attribute value with double quotes:

    ::: 
    ::: highlight
    ``` highlight
    <metabase-dashboard
      dashboard-id="1"
      initial-parameters=""
    ></metabase-dashboard>
    ```
    :::
    :::

-   `hidden-parameters` - list of filter names to hide from the dashboard, like `['productId']`

    Make sure to use single quotes if you are surrounding your attribute value with double quotes:

    ::: 
    ::: highlight
    ``` highlight
    <metabase-dashboard
      dashboard-id="1"
      hidden-parameters="['productId']"
    ></metabase-dashboard>
    ```
    :::
    :::

### Question

To render a question (chart):

``` highlight
<metabase-question question-id="1"></metabase-question>
```

**Required parameters:**

-   `question-id` - This can be a regular ID or an entity ID. [Using Entity IDs](../installation-and-operation/serialization#entity-ids-work-with-embedding) in your embeds ensures that the IDs stay stable when exporting from one Metabase and importing to another.

    Use `question-id="new"` to embed the query builder exploration interface.

**Optional parameters:**

-   `drills` (default is true) - lets you drill through the question
-   `with-title` (default is true) - show the title
-   `with-downloads` (default is false) - show downloads
-   `initial-sql-parameters` - default value for SQL parameters, only applicable to native SQL questions, like ``
-   `is-save-enabled` (default is false)
-   `target-collection` - this is to enforce saving into a particular collection. Values: regular ID, entity ID, `"personal”`, `"root”`

### Browser

To render a collection browser so people can navigate a collection and open dashboards or questions:

``` highlight
<metabase-browser initial-collection="14" read-only="false"></metabase-browser>
```

**Required parameters:**

-   `initial-collection` - This can be a collection ID or `root`. Use a collection ID (e.g., `14`) to start in a specific collection. Use `root` to start at the top-level, "Our Analytics" collection.

**Optional parameters:**

-   `read-only` (default is true) -- if true, people can interact with items (filter, summarize, drill-through) but cannot save. If false, they can create and edit items in the collection.

### Metabot

To render the AI chat interface:

``` highlight
<metabase-metabot></metabase-metabot>
```

**Required parameters:**

None.

**Optional parameters:**

-   `layout` (default is `auto`) -- how should the browser position the visualization with respect to the chat interface. Possible values are:
    -   `auto` (default): Metabot uses the `stacked` layout on mobile screens, and a `sidebar` layout on larger screens.
    -   `stacked`: the question visualization stacks on top of the chat interface.
    -   `sidebar`: the question visualization appears to the left of the chat interface, which is in the right sidebar.

## Embedding Metabase in a different domain

If you want to embed Metabase in another domain (say, if Metabase is hosted at `metabase.yourcompany.com`, but you want to embed Metabase at `yourcompany.github.io`), you can tell Metabase to set the session cookie's SameSite value to "none".

You can set session cookie's SameSite value in **Admin settings** \> **Embedding** \> **Security** \> **SameSite cookie setting**.

SameSite values include:

-   **Lax** (default): Allows Metabase session cookies to be shared on the same domain. Used for production instances on the same domain.
-   **None (requires HTTPS)**: Use "None" when your app and Metabase are hosted on different domains. Incompatible with Safari and iOS-based browsers.
-   **Strict** (not recommended): Does not allow Metabase session cookies to be shared with embedded instances. Use this if you do not want to enable session sharing with embedding.

You can also set the [`MB_SESSION_COOKIE_SAMESITE` environment variable](../configuring-metabase/environment-variables#mb_session_cookie_samesite).

If you're using Safari, you'll need to [allow cross-site tracking](https://support.apple.com/en-tj/guide/safari/sfri40732/mac). Depending on the browser, you may also run into issues when viewing emdedded items in private/incognito tabs.

Learn more about [SameSite cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/embedding/embedded-analytics-js.md) ]