# Source: https://posthog.com/docs/libraries/react-router.md

# React Router - Docs

This guide walks you through setting up PostHog for React Router. React Router V7 has [**three** distinct](https://reactrouter.com/start/modes) modes, and each requires a different setup. If you're still on React Router V6, we have a guide for that, too.

## Which version/mode am I using?

#### Pick the right guide for you

Check your package.json file for the react-router version.

7.x.x (React Router V7)6.x.x (React Router V6)

Differentiating between React Router versions and modes

Here's are quick tips to help you figure out which version/mode you're using:

First, check your `package.json` file for the `react-router` version. If it's `7.x.x`, you're using React Router V7. If it's `6.x.x`, you're using React Router V6.

Then check your project to distinguish between the different modes:

-   If you see a `react-router.config.ts` file, you're using React Router V7 in framework mode.
-   If your router is configured like this: `<RouterProvider router={router} />` with router being a `createBrowserRouter` instance, you're using React Router V7 in data mode.
-   Finally, if your router has `<Routes>` and `<Route>` elements, you're using React Router V7 in declarative mode.

Follow the [React Router docs](https://reactrouter.com/start/modes) for more details.

## React Router guides

React Router V7 has [**three** distinct](https://reactrouter.com/start/modes) modes, and each requires a different setup. Some modes require only the client-side React SDK, while others require **both** the client-side React SDK and the server-side Node SDK.

Follow the [React Router docs](https://reactrouter.com/start/modes) to find out which mode you're using, then follow the guide for that mode:

| Guide | Description |
| --- | --- |
| [V7 - Framework mode (Remix V3)](/docs/libraries/react-router/react-router-v7-framework-mode.md) | This is the default mode. In framework mode, React Router functions as an SSR (server-side rendering) framework. |
| [V7 - Declarative mode](/docs/libraries/react-router/react-router-v7-declarative-mode.md) | In declarative mode, you can build SPAs (single-page applications) with basic routing. |
| [V7 - Data mode](/docs/libraries/react-router/react-router-v7-data-mode.md) | Data mode is also for building SPAs, but comes with APIs like loader, action, and useFetcher. |
| [React Router V6](/docs/libraries/react-router/react-router-v6.md) | React Router V6 is for building SPAs and has features similar to React Router V7 in declarative or data mode. |

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better