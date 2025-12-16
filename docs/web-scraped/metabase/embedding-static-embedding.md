# Source: https://www.metabase.com/docs/latest/embedding/static-embedding

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

# Static embedding

Also known as: standalone embedding, or signed embedding.

<div>

[![interactive-embedding-workshop](/images/events/categories/embedding-workshop.png)](/events/interactive-embedding-workshop)

<div>

Embed a real dashboard in just 30 minutes.

Join our next Embedded Analytics Workshop![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+)

</div>

</div>

In general, embedding works by displaying a Metabase URL inside an iframe in your website. A **static embed** (or signed embed) is an iframe that's loading a Metabase URL secured with a signed JSON Web Token (JWT). Metabase will only load the URL if the request supplies a JWT signed with the secret shared between your app and your Metabase. The JWT also includes a reference to the resource to load, e.g., the dashboard ID, and any values for locked parameters.

You can't use static embeds with [row and column security](../permissions/row-and-column-security), [drill-through](/learn/metabase-basics/querying-and-dashboards/questions/drill-through), and user-specific data isn't captured in [usage analytics](../usage-and-performance-tools/usage-analytics) because signed JWTs don't create user sessions (server-side sessions). For those features, check out [Embedded analytics JS](./embedded-analytics-js).

You can, however, restrict data in static embeds for specific people or groups by [locking parameters](./static-embedding-parameters#restricting-data-in-a-static-embed-with-locked-parameters).

## How static embedding works

If you want to set up interactive Metabase filters in your iframe, your web server will need to make requests to Metabase for updated data each time a website visitor updates the filter widget.

To ask for updated data from Metabase, your web server will generate a new Metabase [embedding URL](#adding-the-embedding-url-to-your-website). For example, if a website visitor enters the value "true" in an [embedded filter widget](./static-embedding-parameters#adding-a-filter-widget-to-a-static-embed), your web server will generate a new embedding URL with an extra parameter:

``` highlight
your_metabase_embedding_url?filter=true
```

To prevent people from editing the embedding URL to get access to other parts of your Metabase (e.g., by changing the parameter to `filter=company_secrets`), your web server will add a signed JWT to the new embedding URL:

``` highlight
your_metabase_embedding_url/your_signed_jwt?filter=true
```

The signed JWT is generated using your [Metabase secret key](#regenerating-the-static-embedding-secret-key). The secret key tells Metabase that the request for filtered data can be trusted, so it's safe to display the results at the new embedding URL. Note that this secret key is shared for all static embeds, so whoever has access to that key will have access to all embedded artifacts.

If you want to embed charts with additional interactive features, like [drill-down](/learn/metabase-basics/querying-and-dashboards/questions/drill-through) and [self-service querying](../questions/query-builder/editor), see [Embedded analytics JS](./embedded-analytics-js).

## Turning on the embedding feature in Metabase

1.  Go to **Settings** \> **Admin settings** \> **Embedding \> Static**.
2.  Toggle **Enable static embedding**.

## Making a question or dashboard embeddable

![Sharing button to embed dashboard](./images/sharing-embed.png)

To create a static embed:

1.  Go to the question or dashboard that you want to embed in your website.
2.  Click on the **sharing icon**.
3.  Select **Embed**.
4.  Select **Static embedding**.
5.  Optional: [customize the appearance of the embed](./static-embedding-parameters#customizing-the-appearance-of-a-static-embed)
6.  Optional: [Add parameters to the embed](./static-embedding-parameters).
7.  Click **Publish**.

![Preview](./images/04-preview.png)

## Adding the embedding URL to your website

The embedding URL for a question or dashboard is the Metabase URL that'll be displayed in your website's iframe. It's generated by your web server using your [Metabase site URL](../configuring-metabase/settings#site-url), [signed JWT](#how-static-embedding-works), and [parameters](./static-embedding-parameters):

``` highlight
metabase_site_url/embed/question/your_jwt_token?parameter_name=value
```

Once you've made a question or dashboard [embeddable](#making-a-question-or-dashboard-embeddable), you'll need to put the embedding URL for that question or dashboard on your website:

1.  Go to the question or dashboard \> **sharing icon** \> **Embed**.
2.  Make any changes and copy the code.
3.  [Preview the code](#previewing-the-code-for-an-embed)
4.  Add the code to the server code that builds your website.
5.  Add the frontend code to the code that generates the page where you want the embedded item to appear.

For more examples, see our [reference apps repo](https://github.com/metabase/embedding-reference-apps).

## Previewing the code for an embed

1.  Go to the question or dashboard \> **sharing icon** \> **Embed this item in an application**.
2.  Click **Code**.
3.  In the top code block, you'll find the sample code for your web server. You'll also find the iframe snippet to plug into your HTML template or single page app.

When you make changes to the look and feel or parameter preview settings, Metabase will update the code and highlight the changes. Make sure to copy these changes to your actual server code.

![Code samples for embedding](./images/05-code.png)

Metabase generates server code for:

-   Clojure
-   Node.js
-   Python
-   Ruby

For iframe snippets:

-   ERB
-   JSX
-   Mustache
-   Pug/Jade

## If you serialize your Metabase, use Entity IDs in your static embeds

Using [Entity IDs](../installation-and-operation/serialization#metabase-uses-entity-ids-to-identify-and-reference-metabase-items) in your static embeds will make sure that the IDs are stable when exporting from one Metabase and importing to another Metabase.

To use an Entity ID in a static embed, all you need to do is edit the `resource` map in the `payload` used to sign your token. Replace the item's (autopopulated) ID with its Entity ID and you're done.

So, in the code below you'd change the `` to:

``` highlight
const payload = ,
  params: ,
  exp: Math.round(Date.now() / 1000) + (10 * 60) // 10 minute expiration
};
```

If you don't serialize your Metabase, don't worry about which ID you use; both will work just fine.

## Editing an embedded question or dashboard

If you change the [parameters](./static-embedding-parameters) of your embedded item:

1.  After making your changes, copy the code Metabase generates.
2.  Click **Publish** again.
3.  [Update the code](#adding-the-embedding-url-to-your-website) on your server so that it matches the code generated by Metabase.

## Disabling embedding for a question or dashboard

You can find a list of all static embeds of questions and dashboards from **Admin settings** \> **Embedding** \> **Static**.

1.  Visit the embeddable question or dashboard.
2.  Click on the **sharing icon** (square with an arrow pointing to the top right).
3.  Select **Embed**.
4.  Select **Static embedding**
5.  Click **Unpublish**.

## Customizing the appearance of static embeds

See [Customizing appearance of static embeds](./static-embedding-parameters#customizing-the-appearance-of-a-static-embed)

## Auto-refreshing the results of an embedded dashboard

> Auto-refreshing is only available for dashboards, not questions.

To refresh the results of a dashboard at a specific cadence, you can parameterize the embedded URL with `refresh`. For example, to set an embedded dashboard to refresh every 60 seconds, you would append `refresh=60` to the URL.

For example, the following code for generating an iframe URL for a dashboard would display the dashboard's title and refresh its results every 60 seconds.

``` highlight
var iframeUrl =
  METABASE_SITE_URL + "/embed/dashboard/" + token + "#titled=true&refresh=60";
```

For the full list options you can parameterize, see [customizing the appearance of a static embed](./static-embedding-parameters#customizing-the-appearance-of-a-static-embed).

## Removing the "Powered by Metabase" banner

![Powered by Metabase](./images/powered-by-metabase.png)

The banner appears on static embeds created with Metabase's open-source version. To remove the banner, you'll need to upgrade to a [Pro](/product/pro) or [Enterprise](/product/enterprise) plan.

## Regenerating the static embedding secret key

Your embedding secret key is used to sign JWTs for all of your [embedding URLs](#adding-the-embedding-url-to-your-website).

1.  Go to **Admin** \> **Embedding** \> **Static embedding**.
2.  Under **Regenerate secret key**, click **Regenerate key**.

This key is shared across all static embeds. Whoever has access to this key could get access to all embedded artifacts, so keep this key secure. If you regenerate this key, you'll need to update your server code with the new key.

## Resizing dashboards to fit their content

Dashboards are a fixed aspect ratio, so if you'd like to ensure they're automatically sized vertically to fit their contents you can use the [iFrame Resizer](https://github.com/davidjbradshaw/iframe-resizer) script. Metabase serves a copy for convenience:

``` highlight
<script src="/app/iframeResizer.js"></script>

<iframe
  src="https://metabase.example.com/embed/dashboard/TOKEN"
  onload="iFrameResize(, this)"
></iframe>
```

Due to iframe-resizer's licensing changes, we recommend that you use iframe-resizer version 4.3.2 or lower.

## Custom destinations on dashboards in static embeds

You can only use the **URL** option for [custom destinations](../dashboards/interactive#custom-destinations) on dashboards with static embedding. External URLs will open in a new tab or window.

You can propagate filter values into the external URL, unless the filter is locked.

## Translating static embeds

See [Translating embedded questions and dashboards](./translations).

## Further reading

-   [Parameters for static embeds](./static-embedding-parameters).
-   [Reference apps repo](https://github.com/metabase/embedding-reference-apps).
-   [Strategies for delivering customer-facing analytics](/learn/metabase-basics/embedding/overview).
-   [Publishing data visualizations to the web](/learn/metabase-basics/embedding/charts-and-dashboards).
-   [Customizing Metabase's appearance](../configuring-metabase/appearance).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/embedding/static-embedding.md) ]