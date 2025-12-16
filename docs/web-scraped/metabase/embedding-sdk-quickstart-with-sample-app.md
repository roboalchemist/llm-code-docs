# Source: https://www.metabase.com/docs/latest/embedding/sdk/quickstart-with-sample-app

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

# Embedded analytics SDK - quickstart with sample app

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

Embedded analytics SDK is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (both self-hosted and on Metabase Cloud).

This guide sets up the embedded analytics SDK with a [sample React app](https://github.com/metabase/metabase-nodejs-react-sdk-embedding-sample/tree/57-stable), but you can follow along with your own application.

                    width: 100%;
                    height: 0;
                    padding-bottom: 56.25%"}

## Prerequisites

-   [Node.js 20.x LTS or higher](https://nodejs.org/en) (for the sample application).
-   [Metabase version v1.52 or higher](https://github.com/metabase/metabase/releases).
-   [A Metabase Pro or Enterprise license](/pricing/) (If you don't have a license, check out [this quickstart](./quickstart) that lacks the paid JWT SSO setup.)
-   (Optional): [Docker](https://www.docker.com/)

## Clone the sample app repo

1.  Clone the [sample React app](https://github.com/metabase/metabase-nodejs-react-sdk-embedding-sample/tree/57-stable).

``` highlight
git clone git@github.com:metabase/metabase-nodejs-react-sdk-embedding-sample.git
```

1.  Check out the branch in the [metabase-nodejs-react-sdk-embedding-sample](https://github.com/metabase/metabase-nodejs-react-sdk-embedding-sample/tree/57-stable) repo that corresponds to your Metabase version.

``` highlight
git checkout v0.57-stable
```

E.g., if you're running Metabase 1.57 make sure the sample app repo is on the `57-stable` branch. You can find your Metabase version in the Metabase UI by clicking on the gears icon in the upper right and selecting **About Metabase**.

## Two ways to set up the sample app with Metabase

-   [Quick setup with Docker](#quick-setup-with-docker) (includes a sample Metabase)
-   [Walkthrough setup](#walkthrough-setup) (bring your own Metabase, or spin up a new one)

## Quick setup with Docker

This setup will run a Docker container with the sample app and a sample Metabase.

1.  Copy the environment template file:

    In the cloned directory, run:

``` highlight
cp .env.docker.example .env.docker
```

1.  In the `.env.docker` file, replace `<your_enterprise_token>` with your premium embedding token.

2.  In the top-level directory, run:

``` highlight
yarn start
```

This script will:

-   Pull a Metabase Docker image and run it in a container.
-   Set up [JWT SSO in Metabase](../../people-and-groups/authenticating-with-jwt)
-   Build and run the sample application with an embedded question.

1.  The app will start on <http://localhost:4400>.

That's it!

If you want to log in to the sample Metabase this command set up, visit <http://localhost:4300>. You can log in with email and password as Rene Descartes: E

-   email: rene@example.com
-   password: foobarbaz

## Walkthrough setup

We're going to do some setup in Metabase, and then in the sample application. You can also bring your own Metabase, in which case you can skip the installation step.

Here's a quick overview of what you'll be doing:

### Set up Metabase for embedding

1.  [Install Metabase Enterprise Edition](#install-metabase-enterprise-edition) (if you haven't already)
2.  [Activate your license](#activate-your-license)
3.  [Enable embedding](#enable-embedding-in-metabase)
4.  [Enable SSO with JWT](#enable-sso-with-jwt)

### Start up the sample application

1.  [Set up the application environment](#set-up-the-application-environment). 6.. [Run the app server](#set-up-the-application-server) to handle authentication with JWT and serve the embedded Metabase components.
2.  [Run the client application](#set-up-the-client-application) that will contain Metabase components built with the SDK.

And then fiddle around with styling.

Let's go.

## Install Metabase Enterprise Edition

You can run Metabase Pro on a Cloud plan with a [free trial](/pricing/).

Or run it locally. Here's a [docker](../../installation-and-operation/running-metabase-on-docker) one-liner:

``` highlight
docker run -d -p 3000:3000 --name metabase metabase/metabase-enterprise:latest
```

You can also [download the JAR](https://downloads.metabase.com/enterprise/latest/metabase.jar), and run it like so:

``` highlight
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

By default, Metabase will run at `http://localhost:3000`.

If you get stuck, check out our [installation docs](../../installation-and-operation/installing-metabase).

## Activate your license

To enable SSO with JWT when self-hosting, you'll need to [activate your license](../../installation-and-operation/activating-the-enterprise-edition). Metabase Pro plans on Cloud take care of this for you.

## Enable embedding in Metabase

From any Metabase page, click on the **gear** icon in the upper right and select **Admin Settings** \> **Embedding**.

Turn on:

-   Embedded analytics SDK (it's in the **Modular** section)
-   Static embedding

Otherwise, this whole thing is hopeless.

## Enable SSO with JWT

We'll also need to update our JWT Provider URI in Metabase. By default, this URI is where the SDK will redirect login requests.

From any Metabase page, click on the **gear** icon in the upper right and select **Admin Settings** \> **Settings** \> **Authentication**.

On the card that says **JWT**, click the **Setup** button.

### JWT Identity provider URI

In **JWT IDENTITY PROVIDER URI** field, paste

``` txt
http://localhost:9090/sso/metabase
```

Or substitute your Cloud URL for `http://localhost`.

### String used by the JWT signing key

Click the **Generate key** button.

Copy the key and paste it in your `.env` file into the env var `METABASE_JWT_SHARED_SECRET`.

The application server will use this key to sign tokens so Metabase knows the application's requests for content are authorized.

## Save and enable JWT

Be sure to hit the **Save and enable** button, or all is void.

## Set up the sample application

## Set up the application environment

[Clone the sample app](#clone-the-sample-app-repo) and `cd` into it.

In the sample app's main directory, copy the `.env.example` template to `.env`.

``` highlight
cp .env.example .env
```

In `.env`, make sure `VITE_METABASE_INSTANCE_URL` and `METABASE_INSTANCE_URL` point to your Metabase instance URL, e.g., `http://localhost:3000`.

Your `.env` will look something like:

``` txt
# FRONTEND
CLIENT_PORT=3100
VITE_METABASE_INSTANCE_URL="http://localhost:3000"

# BACKEND
AUTH_PROVIDER_PORT=9090
METABASE_INSTANCE_URL="http://localhost:3000"
METABASE_JWT_SHARED_SECRET="TODO"
```

## Set up the application server

Change into the `server` directory:

``` highlight
cd server
```

Install packages:

``` highlight
npm install
```

Start the server:

``` highlight
npm start
```

## Set up the client application

In a different terminal, change into the `client` directory:

``` highlight
cd client
```

Install dependencies:

``` highlight
npm install
```

This command will install the [Metabase embedded analytics SDK](https://www.npmjs.com/package/@metabase/embedding-sdk-react), in addition to the application's other dependencies.

You can also install a [different version of the SDK](./version). Just make sure that the major version of the SDK matches the major version of the Metabase you're using.

Start the client app:

``` highlight
npm start
```

Your browser should automatically open the app. By default, the app runs on <http://localhost:3100>.

## At this point, you should be up and running

In your app, you'll see an embedded `InteractiveQuestion` component.

``` highlight
<MetabaseProvider authConfig= theme=>
  <InteractiveQuestion questionId= />
</MetabaseProvider>
```

![Embedded Metabase components](../images/interactive-question-sample-app.png)

## Next steps

To style the components, try changing some of the `theme` options in the client app at `client/src/App.jsx`. For more on theming, check out [Appearance](./appearance).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/embedding/sdk/quickstart-with-sample-app.md) ]