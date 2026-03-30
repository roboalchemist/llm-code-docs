# Source: https://blitzjs.com/docs/blitz-auth-with-next

Title: Blitz Auth with Next.js

URL Source: https://blitzjs.com/docs/blitz-auth-with-next

Markdown Content:
This guide covers how to add Blitz Auth to a Next.js app. We’ll go over setting up Blitz with Next.js, creating a basic auth logic, and using Blitz Auth features inside of Next’s pages and API handlers.

Should you get stuck while working through the guide, refer to [this repo](https://github.com/beerose/next13-blitz-auth).

[](https://blitzjs.com/docs/blitz-auth-with-next#create-new-next-app)Creating a new Next.js app
-----------------------------------------------------------------------------------------------

We’ll start by creating a brand new Next application with `create-next-app`:

You can then run `yarn dev` and open `http://localhost:3000` in your browser to check it out.

[](https://blitzjs.com/docs/blitz-auth-with-next#blitz-setup)Blitz setup
------------------------------------------------------------------------

### [](https://blitzjs.com/docs/blitz-auth-with-next#install-dependencies)Install dependencies

As the next step, we need to install Blitz.js packages:

* `blitz` — Blitz’s core package consisting of Blitz CLI, utilities and core functions used by other Blitz’s packages.
* `@blitzjs/next` — Next.js framework adapter required to initialize Blitz in a Next project.
* `@blitzjs/auth` — the Auth plugin that we’ll explore in this guide.

In order to have Blitz plugins working in your app, we need two configuration files — one for the client side and one for the server side. Let’s create an `src` directory and start with the former.

### [](https://blitzjs.com/docs/blitz-auth-with-next#add-blitz-client)Add a `blitz-client.ts` file

Create a new file — `blitz-client.ts` and add the following content:

Here, we use `setupBlitzClient` from the `@blitzjs/next` and provide a configuration for the plugins we want to use. In our case, we’re only interested in the Auth plugin. The only thing we need to configure is the cookie prefix, and for the rest — we’ll rely on Blitz’s defaults. The reason for having `authConfig` as a separate variable is so that we can export it and reuse in the server setup.

### [](https://blitzjs.com/docs/blitz-auth-with-next#add-blitz-server)Add a `blitz-server.ts` file

Now we can proceed with the server-side configuration. In the same directory, we’ll add `blitz-server.ts` file:

In this file, we have slightly more things going on:

* We use `setupBlitzServer` from `@blitzjs/next` (similar as we did in the client config file)
* In the server-side configuration of Auth plugin, we need two additional things:
  * `storage` : Blitz stores session information in the database, so we need to specify how Blitz Auth can access the storage.
  * `isAuthorized`: a function that determines what user roles are authorized to access pages and other protected code. We’ll use `simpleRoleIsAuthorized` provided by Blitz Auth. You can read more about it here: [https://blitzjs.com/docs/authorization#is-authorized-adapters](https://blitzjs.com/docs/authorization#is-authorized-adapters).

### [](https://blitzjs.com/docs/blitz-auth-with-next#add-types)Add a `types.ts` file

After creating the `blitz-server.ts` file, you might have noticed some TypeScript issues around `storage` property in the Blitz Auth configuration. That’s because Blitz uses types augmentation to set how the `Session` object should look like. Let’s create a `types.ts` file at the root of your project:

### [](https://blitzjs.com/docs/blitz-auth-with-next#setup-database)Setup Database Connection

The Blitz Auth provides a session-based auth system, so we need a database to store the session information. New Blitz apps have a Prisma setup by default, but the package is database agnostic, so we'll go over two options in this guide: with and without using Prisma.

Go to [Without Prisma section](https://blitzjs.com/docs/blitz-auth-with-next#without-prisma) if you don't want to use Prisma.

#### [](https://blitzjs.com/docs/blitz-auth-with-next#with-prisma)With Prisma

First, we’ll install `prisma` and `@prisma/client`:

And we’ll use its CLI to initialize a new Prisma client:

We also need to create a new Prisma client. For that, create an `index.ts` file in the `prisma` directory with the following content:

##### Modify Prisma schema

Next, we will update the `prisma/schema.prisma` file by adding `User`, `Session`, and `Token` database models:

To apply the changes to the database and generate Prisma’s TypeScript types, run: `yarn prisma migrate dev`.

Go to the next step: [adding auth logic](https://blitzjs.com/docs/blitz-auth-with-next/add-auth-logic).

#### [](https://blitzjs.com/docs/blitz-auth-with-next#without-prisma)Without Prisma

The `storage` property in the Blitz Auth configuration [accepts an object that implements the `SessionConfigMethods` interface](https://blitzjs.com/docs/(/docs/auth-config#customize-session-persistence-and-database-access)). The methods are:

* `getSession`
* `getSessions`
* `createSession`
* `updateSession`
* `deleteSession`

You can use any database or API, but in this guide, we’ll show a Redis example:

[](https://blitzjs.com/docs/blitz-auth-with-next#add-auth-logic)Adding auth logic
---------------------------------------------------------------------------------

Now that the setup part is done, we can proceed to implement a simple auth logic using Blitz Auth. This guide will cover sign-up, log-in, and log-out.

### [](https://blitzjs.com/docs/blitz-auth-with-next#add-signup-route)Add `pages/api/signup.ts` file

We’ll start by creating a new API Route called `signup`. Inside, we’ll use `api` function that we got from `setupBlitzServer` function in `src/blitz-server.ts`. It’s a wrapper around Next’s API handlers that provides access to the Blitz’s `ctx` object, which contains auth-related methods and properties.

Inside the handler, we’ll use `SecurePassword` from `@blitzjs/auth` to hash the password provided by user. Next, we’ll create a new user in the database and create a new authenticated session with the `$create` method. The object we provide to `session.$create` is the public data. It contains the same properties we specified in the `types.ts` file. Last but not least, we’ll send a response to the client.

Note: there’s no error handling because I’m trying to keep this guide minimal and focus only on how to setup Blitz Auth with Next.js. Before using it in your applications, you should extend and modify it accordingly.

### [](https://blitzjs.com/docs/blitz-auth-with-next#add-signup-fetch-call)Add `/signup` fetch call to signup form’s `onSubmit` method

As we have the backend logic for sign-up, we can call the new endpoint from the client, e.g. when user submits a sign-up form. The call will look like this:

One thing to notice here is the usage of `getAntiCSRFToken`. When making a request from the client to an API route, we need to include `anti-csrf` header. You can read more about it [here](https://blitzjs.com/docs/session-management#manual-api-requests).

### [](https://blitzjs.com/docs/blitz-auth-with-next#add-login-route)Add `pages/api/login.ts`

As before, we’ll add a new API route. Inside, we’ll add an `authenticateUser` function to verify the login credentials, and if correct, we’ll create a new authenticated session as we did in the signup handler.

### [](https://blitzjs.com/docs/blitz-auth-with-next#add-login-fetch-call)Add `/login` fetch call to login form’s `onSubmit` method

On the client side, you need to send a request to the `/api/login` in a similar way as in case of signup.

### [](https://blitzjs.com/docs/blitz-auth-with-next#add-logout-route)Add `pages/api/logout.ts`

One last thing we’ll do on the API side is to add a logout handler. Inside we’ll use a `$revoke` function which removes the session and logs the user out.

[](https://blitzjs.com/docs/blitz-auth-with-next#using-auth-gssp-gsp)Using authentication in API Routes, `getServerSideProps`, and `getStaticProps`
---------------------------------------------------------------------------------------------------------------------------------------------------

We already saw how to use Blitz Auth session’s methods in the Next.js API Routes. We can do so by accessing the Blitz context provided as third argument in an `api` wrapper:

A similar thing can be done in the case of `getServerSideProps` and `getStaticProps`. `createBlitzServer` returns `gSSP`, and `gSP` functions that are wrappers for `getServerSideProps` and `getStaticProps`. Example usage:

[](https://blitzjs.com/docs/blitz-auth-with-next#access-session-on-the-client)Access Session on the client
----------------------------------------------------------------------------------------------------------

Blitz Auth provides a `useSession()`` hook that returns`PublicData`with`isLoading`` property. This hook can be used anywhere in your application.

Note: `useSession()` uses suspense by default, so you need a `<Suspense>` component above it in the tree. Or you can set `useSession({suspense: false})` to disable suspense.

Here's an example usage:

[](https://blitzjs.com/docs/blitz-auth-with-next#adding-auth-to-pages)Adding authorization to pages
---------------------------------------------------------------------------------------------------

What we did so far is only a part of Blitz Auth features. We’ll also quickly explore how to protect the pages. Blitz Auth allows you to add `authenticate` or `redirectAuthenticatedTo` properties on your pages or layouts. To be able to use them, we need to wrap the `App` component with the `withBlitz` HOC. If you don’t have it, add a new `_app.tsx` file to the `pages` directory. In this file, we have to wrap the `App` component with the `withBlitz`.

Note: `withBlitz` currently doesn’t work with the new Next 13 layouts. Until we add a support for it, you’ll still have to use the old `pages/_app.tsx`.

Now, let’s go back to our pages. In the `signup.tsx` and `login.tsx`, we’ll use `redirectAuthenticatedTo`:

And in `login.tsx`:

In the `user.tsx`, we’ll use `authenticate` and redirect to the `login` page if a user attempting to visit it is not authenticated.

if you’re interested in exploring other Blitz Auth’s features, it also exports a bunch of hooks and utilities that are worth checking out: [docs](https://blitzjs.com/docs/auth-utils).

[](https://blitzjs.com/docs/blitz-auth-with-next#summary)Summary
----------------------------------------------------------------

This guide covered setting up Prisma for Blitz Auth, adding Blitz Auth to a new Next.js app, and implementing a basic auth flow. We also explored how to use Blitz Auth to protect pages.

If you want to see a full Blitz app with sign-up, login, logout, reset password you can check out an [example in Blitz’s repo](https://github.com/blitz-js/blitz/tree/main/apps/toolkit-app) or run `npx blitz new my-new-blitz-app` to generate a new production-ready Blitz app.

A repository with setup from this guide is available [here](https://github.com/beerose/next13-blitz-auth).

To learn more about Blitz.js, you can take a look at the following resources:

* [Blitz.js Documentation](https://blitzjs.com/docs/) — learn about Blitz.js.
* [Blitz Auth Documentation](https://blitzjs.com/docs/auth) — learn about Blitz Auth plugin.

And if you have any feedback reach out to us on [Discord](https://discord.blitzjs.com/) or [GitHub](https://github.com/blitz-js/blitz).
