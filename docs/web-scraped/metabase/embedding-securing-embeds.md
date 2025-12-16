# Source: https://www.metabase.com/docs/latest/embedding/securing-embeds

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

# Securing embedded Metabase

## Securing embeds with authentication and authorization

There are two basic ways to secure stuff on the internet:

1.  **Authentication** looks at *who* someone is (using standards such as [JWT](../people-and-groups/authenticating-with-jwt) or [SAML](../people-and-groups/authenticating-with-saml)).
2.  **Authorization** looks at *what* someone has access to (using standards such as OAuth 2.0).

In this guide, we'll talk primarily about authentication.

## Public embedding

[Public embedding](public-links#public-embeds) doesn't involve any authentication or authorization. A public embed displays a public link with a unique string at the end, like this:

``` highlight
https://my-metabase.com/public/dashboard/184f819c-2c80-4b2d-80f8-26bffaae5d8b
```

The string (in this example: `184f819c-2c80-4b2d-80f8-26bffaae5d8b`) uniquely identifies your Metabase question or dashboard. Since public embeds don't do any authentication or authorization, anyone with the URL can view the data.

### Example: filters in public links don't secure data

So, how could someone exploit a public embed? Say we have a dashboard that displays Accounts data:

  Account ID   Plan      Status
  ------------ --------- ----------
  1            Basic     Active
  2            Basic     Active
  3            Basic     Inactive
  4            Premium   Inactive
  5            Premium   Active

We want to add a "Status = Active" filter and display the dashboard's public link in an embed:

  Account ID   Plan      Status
  ------------ --------- --------
  1            Basic     Active
  2            Basic     Active
  5            Premium   Active

To apply and hide the "Status = Active" filter, we'll add [query parameters](public-links#public-embed-parameters) to the end of the public link in our embed:

``` highlight
https://my-metabase.com/public/dashboard/184f819c-2c80-4b2d-80f8-26bffaae5d8b?status=active#hide_parameters=status
```

Even though we've hidden the filter from the embed, someone could take the public link used in the embed, and remove the query parameter `?status=active`:

``` highlight
https://my-metabase.com/public/dashboard/184f819c-2c80-4b2d-80f8-26bffaae5d8b
```

Loading the public link without the query parameter would remove the "Status = Active" filter from the data. The person would get access to the original Accounts data, including the rows with inactive accounts.

## Static embeds are authorized with JWT

Static embedding uses a [JWT authorization flow](#static-embedding-with-jwt-authorization) to do two things:

-   Sign resources (e.g., the URLs of charts or dashboards) to ensure that only your embedding application can ask for data from your Metabase.
-   Sign parameters (e.g., dashboard filters) to prevent people from [changing the filters](#example-filters-in-public-links-dont-secure-data) and getting access to other data.

### Static embeds don't have user sessions

Static embeds don't authenticate people's identities on the Metabase side, so people can view a static embed without creating a Metabase account. However, without a Metabase account, Metabase won't have a way to remember a user or their session, which means:

-   Metabase [permissions](../permissions/introduction) and [row and column security](../permissions/row-and-column-security) won't work --- if you need to lock down sensitive data, you must set up [locked parameters](#example-securing-data-with-locked-parameters-on-a-static-embed) for *each* of your static embeds.
-   Any filter selections in a static embed will reset once the signed JWT expires.
-   All Static embed usage will show up in [usage analytics](../usage-and-performance-tools/usage-analytics) under "External user".

## Security in static embedding vs. modular and interactive embedding 

Static embedding only guarantees authorized access to your Metabase data (you decide *what* is accessible).

If you want to secure your static embeds based on someone's identity (you decide *who* gets access to *what*), you'll need to set up your own authentication flow and manually wire that up to [locked parameters](#example-sending-user-attributes-to-a-locked-parameter) on each of your static embeds. Note that locked parameters are essentially filters, so you can only set up **row-level** restrictions in a static embed.

If you want an easier way to embed different views of data for different customers (without allowing the customers to see each other's data), learn how [Modular and interactive embedding authenticates and authorizes people in one flow](#modular-and-interactive-embedding-auth-with-jwt-or-saml).

### Static embedding with JWT authorization

![Static embedding with JWT authorization.](./images/signed-embedding-jwt.png)

This diagram illustrates how an embed gets secured by a signed JWT:

1.  **Visitor arrives**: your frontend gets a request to display a Metabase [embedding URL](./static-embedding#adding-the-embedding-url-to-your-website).
2.  **Signed request**: your backend generates a Metabase embedding URL with a [signed JWT](./static-embedding#how-static-embedding-works). The signed JWT should encode any query [parameters](./static-embedding-parameters) you're using to filter your data.
3.  **Response**: your Metabase backend returns data based on the query parameters encoded in the signed JWT.
4.  **Success**: your frontend displays the embedded Metabase page with the correct data.

### Example: securing data with locked parameters on a static embed

In the [public embedding example](#example-filters-in-public-links-dont-secure-data), we showed you (perhaps unwisely) how someone could exploit a unique public link by editing its query parameters.

Let's go back to our Accounts example:

  Account ID   Plan      Status
  ------------ --------- ----------
  1            Basic     Active
  2            Basic     Active
  3            Basic     Inactive
  4            Premium   Inactive
  5            Premium   Active

Remember, we can filter the data in a public embed by including a query parameter at the end of the embedding URL:

``` highlight
https://my-metabase.com/public/dashboard/184f819c-2c80-4b2d-80f8-26bffaae5d8b?status=active
```

  Account ID   Plan      Status
  ------------ --------- --------
  1            Basic     Active
  2            Basic     Active
  5            Premium   Active

With static embeds, we can "lock" the filter by encoding the query parameter in a signed JWT. For example, say we set up the "Status = Active" filter as a [locked parameter](./static-embedding-parameters). The `?status=active` query parameter will be encoded in the signed JWT, so it won't be visible or editable from the static embedding URL:

``` highlight
https://my-metabase.com/dashboard/your_signed_jwt
```

If someone tries to add an (unsigned) query parameter to the end of the static embedding URL like this:

``` highlight
https://my-metabase.com/dashboard/your_signed_jwt?status=inactive
```

Metabase will reject this unauthorized request for data, so the inactive account rows will remain hidden from the embed.

### Example: sending user attributes to a locked parameter

Let's say that we want to expose the Accounts table to our customers, so that customers can look up a row based on an Account ID.

  Account ID   Plan      Status
  ------------ --------- ----------
  1            Basic     Active
  2            Basic     Active
  3            Basic     Inactive
  4            Premium   Inactive
  5            Premium   Active

If we want to avoid creating a Metabase login for each of our customers, we'll need:

-   An [embeddable dashboard](./static-embedding#making-a-question-or-dashboard-embeddable) with the Accounts data.
-   A [locked parameter](./static-embedding-parameters) for the Account ID filter.
-   A login flow in our embedding application (the web app where we want to embed Metabase).

The flow might look something like this:

1.  A customer logs into our web app.
2.  Our app backend looks up the customer's `account_id` based on the account email used during login.
3.  Our app backend uses Metabase's [secret key](./static-embedding#regenerating-the-static-embedding-secret-key) to [generate the embedding URL](./static-embedding#how-static-embedding-works) with a signed JWT. The signed JWT encodes the query parameters to filter the Accounts dashboard on `Account ID = account_id`.
4.  Metabase returns the filtered dashboard at the static embedding URL.
5.  Our app frontend displays the filtered dashboard in an iframe.

For code samples, see the [static embedding reference app](https://github.com/metabase/embedding-reference-apps).

## Modular and interactive embedding auth with JWT or SAML

Modular embedding (using Embedded Analytics [SDK](./sdk/introduction) or [JS](./embedded-analytics-js) components), and [interactive full-app embedding](./interactive-embedding) integrate with SSO (either [JWT](../people-and-groups/authenticating-with-jwt) or [SAML](../people-and-groups/authenticating-with-saml)) to authenticate and authorize people in one flow. The auth integration makes it easy to map user attributes (such as a person's role or department) to granular levels of data access, including:

-   [Tables](../permissions/data)
-   [Rows](../permissions/row-and-column-security#row-level-security-filter-by-a-column-in-the-table)
-   [Columns](../permissions/row-and-column-security#custom-row-and-column-security-use-a-sql-question-to-create-a-custom-view-of-a-table)
-   [Other data permissions](../permissions/data), such as data download permissions or SQL access.

![Interactive embedding with SSO.](./images/full-app-embedding-sso.png)

This diagram shows you how an interactive embed gets secured with [SSO](../people-and-groups/start#sso-for-metabase-pro-and-enterprise-plans):

1.  **Visitor arrives**: your frontend gets a request to display all content, including a Metabase component (such as a React component).
2.  **Load embed**: your frontend component loads the Metabase frontend using your [embedding URL](./interactive-embedding#pointing-an-iframe-to-a-metabase-url).
3.  **Check session**: to display data at the embedding URL, your Metabase backend checks for a valid session (a logged-in visitor).
4.  **If there's no valid session**:
    -   **Redirect to SSO**: your Metabase frontend redirects the visitor to your SSO login page.
    -   **SSO auth**: your SSO flow authenticates the visitor and generates a session based on their identity. The session info should encode user attributes such as group membership and [row and column security](../permissions/row-and-column-security) permissions.
    -   **Redirect to Metabase**: your SSO flow redirects the visitor to your Metabase frontend with the session info.
5.  **Request**: your Metabase frontend sends the request for data to the Metabase backend, along with the session info.
6.  **Response**: your Metabase backend returns data based on the user attributes encoded in the session info.
7.  **Success**: your frontend component displays the embedded Metabase page with the correct data for the logged-in visitor.

The mechanics of step 4 will vary a bit depending on whether you use [JWT](../people-and-groups/authenticating-with-jwt) or [SAML](../people-and-groups/authenticating-with-saml) for SSO.

### Example: securing data with SSO and row and column security

In our static embedding example, we used [locked parameters](#example-securing-data-with-locked-parameters-on-a-static-embed) to display secure filtered views of the Accounts table.

The nice thing about modular/interactive embedding and [SSO](../people-and-groups/start#sso-for-metabase-pro-and-enterprise-plans) integration is that we don't have to manually manage locked parameters for each embed. Instead, we can map user attributes from our identity provider (IdP) to [permissions](../permissions/introduction) and [row and column security](../permissions/row-and-column-security) in Metabase. People can get authenticated and authorized to self-serve specific subsets of data from their very first login.

Let's expand on our Accounts example to include a Tenant ID. The Tenant ID represents the parent org for a group of customers:

  Tenant ID   Account ID   Plan      Status
  ----------- ------------ --------- ----------
  999         1            Basic     Active
  999         2            Basic     Active
  999         3            Basic     Inactive
  777         4            Premium   Inactive
  777         5            Premium   Active

We still want to expose the Accounts table to our customers, but with a few extra requirements:

-   Individual customers can only view the data for their own Account ID.
-   Tenants can view all of their child accounts (but not the data of other tenants).

To set up these multi-tenant permissions, we'll need to:

1.  Create an `primary_id` attribute in our IdP to uniquely identify all tenants and customers.
2.  Create a user attribute in our IdP called `role` and set that to `tenant` or `customer` for each person who will be using Metabase.
3.  Create two groups in Metabase: Tenants and Customers.
4.  Synchronize group membership between Metabase and our IdP so that:
    -   People with `role=tenant` are assigned to the Tenant group.
    -   People with `role=customer` are assigned to the Customers group.
5.  Set up row-level security on the Accounts table for each group:
    -   For the Customers group, the Accounts table will be restricted with `Account ID = primary_id`.
    -   For the Tenants group,, the Accounts table will be restricted with `Tenant ID = primary_id`.

When Tenant A logs in with SSO for the first time:

-   Metabase will create an account for them.
-   Our IdP will send the `role=tenant` and `primary_id=999` attributes to Metabase.
-   Metabase will automatically assign Tenant A to the Tenant group.
-   Tenant A will get the Tenant group's permissions (including row and column security).
-   Tenant A will see a restricted view of the Accounts table everywhere in Metabase:

  Tenant ID   Account ID   Plan    Status
  ----------- ------------ ------- ----------
  999         1            Basic   Active
  999         2            Basic   Active
  999         3            Basic   Inactive

When Customer 1 logs in, they'll see a different filtered version of the Accounts table based on their `role` and `primary_id` attributes:

  Tenant ID   Account ID   Plan    Status
  ----------- ------------ ------- --------
  A           1            Basic   Active

## Sample apps

-   [Modular embedding demo](https://embedded-analytics-sdk-demo.metabase.com)
-   [Modular embedding with SDK reference app](https://github.com/metabase/metabase-nodejs-react-sdk-embedding-sample)
-   [Interactive embedding demo](https://embedding-demo.metabase.com/)
-   [Interactive embedding reference app](https://github.com/metabase/sso-examples/tree/master/app-embed-example)
-   [Static embedding reference app](https://github.com/metabase/embedding-reference-apps)

## Further reading

-   [Configuring permissions for different customer schemas](../permissions/embedding)

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/embedding/securing-embeds.md) ]