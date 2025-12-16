# Source: https://www.metabase.com/docs/latest/embedding/interactive-embedding

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

# Interactive embedding

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

Interactive embedding is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (both self-hosted and on Metabase Cloud).

<div>

[![interactive-embedding-workshop](/images/events/categories/embedding-workshop.png)](/events/interactive-embedding-workshop)

<div>

Embed a real dashboard in just 30 minutes.

Join our next Embedded Analytics Workshop![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+)

</div>

</div>

**Interactive embedding** lets you embed the entire Metabase app in an iframe. Interactive embedding integrates your [permissions](../permissions/introduction) and [SSO](../people-and-groups/start#authentication) to give people the right level of access to [query](../questions/query-builder/editor) and [drill-down](/learn/metabase-basics/querying-and-dashboards/questions/drill-through) into your data.

> If you are just starting out with Metabase embedding, consider using [Embedded Analytics JS](./embedded-analytics-js) instead of interactive embedding - it's an improved, more customizable option for embedding interactive Metabase elements. Interactive embedding remains fully supported.

## Interactive embedding demo

To get a feel for what you can do with interactive embedding, check out our [interactive embedding demo](/embedding-demo).

To see the query builder in action, click on **Reports** \> **+ New** \> **Question**.

## Quick start

Check out the [Interactive embedding quick start](./interactive-embedding-quick-start-guide).

## Prerequisites for interactive embedding

1.  Make sure you have a [license token](../installation-and-operation/activating-the-enterprise-edition) for a [Pro or Enterprise plan](https://store.metabase.com/checkout/login-details).
2.  Organize people into Metabase [groups](../people-and-groups/start).
3.  Set up [permissions](../permissions/introduction) for each group.
4.  Set up [SSO](../people-and-groups/start#authentication) to automatically apply permissions and show people the right data upon sign-in. In general, **we recommend using [SSO with JWT](../people-and-groups/authenticating-with-jwt)**.

If you're dealing with a [multi-tenant](/learn/metabase-basics/embedding/multi-tenant-self-service-analytics) situation, check out our recommendations for [Configuring permissions for different customer schemas](../permissions/embedding).

If you have your app running locally, and you're using the Pro Cloud version, or hosting Metabase and your app in different domains, you'll need to set your Metabase environment's session cookie SameSite option to "none".

## Enabling interactive embedding in Metabase

1.  Go to **Admin \> Embedding \> Interactive**.
2.  Click **Enable interactive embedding**.
3.  Under **Authorized origins**, add the URL of the website or web app where you want to embed Metabase (such as `https://*.example.com`).

## Setting up embedding on your website

1.  Create an iframe with a `src` attribute set to:
    -   the [URL](#pointing-an-iframe-to-a-metabase-url) of the Metabase page you want to embed, or
    -   an [authentication endpoint](#pointing-an-iframe-to-an-authentication-endpoint) that redirects to your Metabase URL.
2.  Optional: Depending on the way your web app is set up, set [environment variables](../configuring-metabase/environment-variables) to:
    -   [Add your license token](../configuring-metabase/environment-variables#mb_premium_embedding_token).
    -   [Embed Metabase in a different domain](#embedding-metabase-in-a-different-domain).
    -   [Secure your interactive embed](#securing-interactive-embeds).
3.  Optional: Enable communication to and from the embedded Metabase using supported [`postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) messages:
    -   [From Metabase](#supported-postmessage-messages-from-embedded-metabase)
    -   [To Metabase](#supported-postmessage-messages-to-embedded-metabase)
4.  Optional: Set parameters to [show or hide Metabase UI components](#showing-or-hiding-metabase-ui-components).

Once you're ready to roll out your interactive embed, make sure that people **allow** browser cookies from Metabase, otherwise they won't be able to log in.

### Pointing an iframe to a Metabase URL

Go to your Metabase and find the page that you want to embed.

For example, to embed your Metabase home page, set the `src` attribute to your [site URL](../configuring-metabase/settings#site-url), such as:

``` highlight
src="https://metabase.yourcompany.com/"
```

To embed a specific Metabase dashboard, you'll want to use the dashboard's Entity ID URL `/dashboard/entity/[Entity ID]`.

``` highlight
src="https://metabase.yourcompany.com/dashboard/entity/[Entity ID]"
```

To get a dashboard's Entity ID, visit the dashboard and click on the **info** button. In the **Overview** tab, copy the **Entity ID**. Then in your iframe's `src` attribute to:

``` highlight
src=https://metabase.yourcompany.com/dashboard/entity/Dc_7X8N7zf4iDK9Ps1M3b
```

If your dashboard has more than one tab, select the tab you want people to land on and copy the Tab's ID. Add the tab's ID to the URL:

``` highlight
src=https://metabase.yourcompany.com/dashboard/entity/Dc_7X8N7zf4iDK9Ps1M3b?tab=YLNdEYtzuSMA0lqO7u3FD
```

You *can* use a dashboard's sequential ID, but you should prefer the Entity ID, as Entity IDs are stable across different Metabase environments (e.g., if you're testing on a staging environment, the Entity IDs will remain the same when [exporting the data and importing it](../installation-and-operation/serialization) into a production environment).

If you want to point to a question, collection, or model, visit the item, click on its info, grab the item's Entity ID and follow the url structure: `/[Item type]/entity/[Entity-Id]`. Examples:

-   `/collection/entity/[Entity ID]`
-   `/model/entity/[Entity ID]`
-   `/question/entity/[Entity ID]`

### Pointing an iframe to an authentication endpoint

Use this option if you want to send people directly to your SSO login screen (i.e., skip over the Metabase login screen with an SSO button), and redirect to Metabase automatically upon authentication.

You'll need to set the `src` attribute to your auth endpoint, with a `return_to` parameter pointing to the encoded Metabase URL. For example, to send people to your SSO login page and automatically redirect them to `https://metabase.yourcompany.com/dashboard/1`:

``` highlight
https://metabase.example.com/auth/sso?return_to=http%3A%2F%2Fmetabase.yourcompany.com%2Fdashboard%2F1
```

If you're using [JWT](../people-and-groups/authenticating-with-jwt), you can use the relative path for the redirect (i.e., your Metabase URL without the [site URL](../configuring-metabase/settings#site-url)). For example, to send people to a Metabase page at `/dashboard/1`:

``` highlight
https://metabase.example.com/auth/sso?jwt=<token>&return_to=%2Fdashboard%2F1
```

You must URL encode (or double encode, depending on your web setup) all of the parameters in your redirect link, including parameters for filters (e.g., `filter=value`) and [UI settings](#showing-or-hiding-metabase-ui-components) (e.g., `top_nav=true`). For example, if you added two filter parameters to the JWT example shown above, your `src` link would become:

``` highlight
https://metabase.example.com/auth/sso?jwt=<token>&redirect=%2Fdashboard%2F1%3Ffilter1%3Dvalue%26filter2%3Dvalue
```

## Cross-browser compatibility

To make sure that your embedded Metabase works in all browsers, put Metabase and the embedding app in the same top-level domain (TLD). The TLD is indicated by the last part of a web address, like `.com` or `.org`.

Note that your interactive embed must be compatible with Safari to run on *any* browser in iOS (such as Chrome on iOS).

## Embedding Metabase in a different domain

> Skip this section if your Metabase and embedding app are already in the same top-level domain (TLD).

If you want to embed Metabase in another domain (say, if Metabase is hosted at `metabase.yourcompany.com`, but you want to embed Metabase at `yourcompany.github.io`), you can tell Metabase to set the session cookie's SameSite value to "none".

You can set session cookie's SameSite value in **Admin settings** \> **Embedding** \> **Security** \> **SameSite cookie setting**.

SameSite values include:

-   **Lax** (default): Allows Metabase session cookies to be shared on the same domain. Used for production instances on the same domain.
-   **None (requires HTTPS)**: Use "None" when your app and Metabase are hosted on different domains. Incompatible with Safari and iOS-based browsers.
-   **Strict** (not recommended): Does not allow Metabase session cookies to be shared with embedded instances. Use this if you do not want to enable session sharing with embedding.

You can also set the [`MB_SESSION_COOKIE_SAMESITE` environment variable](../configuring-metabase/environment-variables#mb_session_cookie_samesite).

If you're using Safari, you'll need to [allow cross-site tracking](https://support.apple.com/en-tj/guide/safari/sfri40732/mac). Depending on the browser, you may also run into issues when viewing emdedded items in private/incognito tabs.

Learn more about [SameSite cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite).

## Securing interactive embeds

Metabase uses HTTP cookies to authenticate people and keep them signed into your embedded Metabase, even when someone closes their browser session. If you enjoy diagrammed auth flows, check out [Interactive embedding with SSO](./securing-embeds).

To limit the amount of time that a person stays logged in, set [`MAX_SESSION_AGE`](../configuring-metabase/environment-variables#max_session_age) to a number in minutes. The default value is 20,160 (two weeks).

For example, to keep people signed in for 24 hours at most:

``` highlight
MAX_SESSION_AGE=1440
```

To automatically clear a person's login cookies when they end a browser session:

``` highlight
MB_SESSION_COOKIES=true
```

To manually log someone out of Metabase, load the following URL (for example, in a hidden iframe on the logout page of your application):

``` highlight
https://metabase.yourcompany.com/auth/logout
```

If you're using [JWT](../people-and-groups/authenticating-with-jwt) for SSO, we recommend setting the `exp` (expiration time) property to a short duration (e.g., 1 minute).

## Supported postMessage messages *from* embedded Metabase

To keep up with changes to an embedded Metabase URL (for example, when a filter is applied), set up your app to listen for "location" messages from the embedded Metabase. If you want to use this message for deep-linking, note that "location" mirrors "window.location".

``` highlight

}
```

To make an embedded Metabase page (like a question) fill up the entire iframe in your app, set up your app to listen for a "frame" message with "normal" mode from Metabase:

``` highlight

  }
}
```

To specify the size of an iframe in your app so that it matches an embedded Metabase page (such as a dashboard), set up your app to listen for a "frame" message with "fit" mode from Metabase:

``` highlight

  }
}
```

## Supported postMessage messages *to* embedded Metabase

To change an embedding URL, send a "location" message from your app to Metabase:

``` highlight

}
```

## Group strategies for row and column security

If you want multiple people from a single customer account to collaborate on questions and dashboards, you'll need to set up one [group](../people-and-groups/managing#groups) per customer account.

You can handle [row and column security](../permissions/row-and-column-security) with a single, separate group. For example, each person could be part of a customer group that sets up data permissions with row and column security via a certain attribute that applies to everyone across all your customer accounts.

Additionally, each person within a single customer account could also be a member of a group specific to that customer account. That way they can collaborate on collections with other people in their organization, without seeing stuff created by people from other customers' accounts.

## Showing or hiding Metabase UI components

See [interactive UI components](./interactive-ui-components)

## Reference apps

To build a sample interactive embed using SSO with JWT, see our reference apps:

-   [Node.js + Express](https://github.com/metabase/metabase-nodejs-express-interactive-embedding-sample) (with [quick start guide](./interactive-embedding-quick-start-guide))
-   [Node.js + React](https://github.com/metabase/sso-examples/tree/master/app-embed-example)

## Further reading

-   [Interactive embedding quick start](./interactive-embedding-quick-start-guide)
-   [Strategies for delivering customer-facing analytics](/learn/metabase-basics/embedding/overview).
-   [Permissions strategies](/learn/metabase-basics/administration/permissions/strategy).
-   [Customizing Metabase's appearance](../configuring-metabase/appearance).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/embedding/interactive-embedding.md) ]