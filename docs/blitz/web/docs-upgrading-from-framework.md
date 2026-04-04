# Source: https://blitzjs.com/docs/upgrading-from-framework

Title: Upgrading Your Blitz App to Blitz 2.0

URL Source: https://blitzjs.com/docs/upgrading-from-framework

Markdown Content:
If you have an existing Blitz.js app, and would like to upgrade it to the Blitz 2.0, you can use our `@blitzjs/codemod` package:

After running the above command, your Blitz app will be upgraded to the Blitz 2.0. If you face any issues with the codemod — let us know! You can also check out the manual upgrade guide below.

[](https://blitzjs.com/docs/upgrading-from-framework#manual-upgrade-steps)Manual Upgrade Steps
----------------------------------------------------------------------------------------------

Below, we're going to list down the steps performed by the codemod in case you want to do some of them or all of them manually. Also, in case something goes wrong with the codemod tool, you can follow these steps to upgrade your app:

### [](https://blitzjs.com/docs/upgrading-from-framework#rename-blitz-config-ts-file)Rename the `blitz.config.ts` file to `next.config.js`

Inside of the config file, you'll also need to wrap the config with `withBlitz` function imported from `@blitzjs/next`:

### [](https://blitzjs.com/docs/upgrading-from-framework#update-dependencies)Update dependencies in `package.json`

1. Update `react`, `react-dom` to the latest versions.
2. Install `@blitzjs/next`, `@blitzjs/rpc`, `@blitzjs/auth`.
3. Set `blitz` version to `latest`.
4. Upgrade `next` to the latest version.

### [](https://blitzjs.com/docs/upgrading-from-framework#update-imports)Update project's named imports

Now, for most of the things previously imported from `blitz` package, you'd need to update the import to the new packages. Use the following list as a reference:

| Import | Source Package |
| --- | --- |
| `NextApiHandler` | `next` |
| `NextApiRequest` | `next` |
| `NextApiResponse` | `next` |
| `GetServerSideProps` | `next` |
| `InferGetServerSidePropsType` | `next` |
| `GetServerSidePropsContext` | `next` |
| `useRouterQuery`: | `next/router` |
| `useRouter` | `next/router` |
| `Router` | `next/router` |
| `Link` | `next/link` |
| `Image` | `next/image` |
| `Script` | `next/script` |
| `Document` | `next/document` |
| `DocumentHead` | `next/document` |
| `Html` | `next/document` |
| `Main` | `next/document` |
| `Head` | `next/head` |
| `App` | `next/app` |
| `dynamic` | `next/dynamic` |
| `noSSR` | `next/dynamic` |
| `getConfig` | `next/config` |
| `setConfig` | `next/config` |
| `ErrorBoundary` | `@blitzjs/next` |
| `ErrorFallbackProps` | `@blitzjs/next` |
| `useParam` | `@blitzjs/next` |
| `Routes` | `@blitzjs/next` |
| `ErrorComponent` | `@blitzjs/next` |
| `AppProps` | `@blitzjs/next` |
| `BlitzPage` | `@blitzjs/next` |
| `BlitzLayout` | `@blitzjs/next` |
| `invokeWithMiddleware` | `@blitzjs/rpc` |
| `resolver` | `@blitzjs/rpc` |
| `useQuery` | `@blitzjs/rpc` |
| `usePaginatedQuery` | `@blitzjs/rpc` |
| `useInfiniteQuery` | `@blitzjs/rpc` |
| `useMutation` | `@blitzjs/rpc` |
| `queryClient` | `@blitzjs/rpc` |
| `getQueryKey` | `@blitzjs/rpc` |
| `getInfiniteQueryKey` | `@blitzjs/rpc` |
| `invalidateQuery` | `@blitzjs/rpc` |
| `setQueryData` | `@blitzjs/rpc` |
| `useQueryErrorResetBoundary` | `@blitzjs/rpc` |
| `QueryClient` | `@blitzjs/rpc` |
| `dehydrate` | `@blitzjs/rpc` |
| `invoke` | `@blitzjs/rpc` |
| `getAntiCSRFToken` | `@blitzjs/auth` |
| `passportAuth` | `@blitzjs/auth` |
| `sessionMiddleware` | `@blitzjs/auth` |
| `simpleRolesIsAuthorized` | `@blitzjs/auth` |
| `getSession` | `@blitzjs/auth` |
| `setPublicDataForUser` | `@blitzjs/auth` |
| `SecurePassword` | `@blitzjs/auth` |
| `hash256` | `@blitzjs/auth` |
| `generateToken` | `@blitzjs/auth` |
| `useAuthenticatedSession` | `@blitzjs/auth` |
| `useRedirectAuthenticated` | `@blitzjs/auth` |
| `useSession` | `@blitzjs/auth` |
| `useAuthorize` | `@blitzjs/auth` |
| `AuthenticatedSessionContext` | `@blitzjs/auth` |

### [](https://blitzjs.com/docs/upgrading-from-framework#update-default-imports)Update project's default imports

There are also some default imports that you'll need to update. Use the following list as a reference:

| Default Import | Source Package |
| --- | --- |
| `Link` | `next/link` |
| `Image` | `next/image` |
| `Head` | `next/head` |
| `dynamic` | `next/dynamic` |

### [](https://blitzjs.com/docs/upgrading-from-framework#change-query-client-import)Change `queryClient` import to `getQueryClient`

If you imported `queryClient` from `blitz`, you'd need to change it to the following code:

### [](https://blitzjs.com/docs/upgrading-from-framework#update-api-imports)Update `BlitzApiRequest`, `BlitzApiResponse`, `BlitzApiHandler`

`blitz` no longer exports `BlitzApiRequest`, `BlitzApiResponse`, `BlitzApiHandler`. You'll need to update your imports to the following:

### [](https://blitzjs.com/docs/upgrading-from-framework#create-blitz-files)Create `blitz-server.ts` and `blitz-client.ts`

To configure the plugins, you'd need to add the following files to your project:

1. `blitz-server.ts`:

1. `blitz-client.ts`:

### [](https://blitzjs.com/docs/upgrading-from-framework#create-api-route)Create API Route for the Zero-API Layer

To setup the Zero-API layer, you'd need to create a `src/pages/api/rpc/[[...blitz]].ts` file with the following content:

### [](https://blitzjs.com/docs/upgrading-from-framework#remove-babel-config)Remove `babel.config.js`

It's not needed anymore.

### [](https://blitzjs.com/docs/upgrading-from-framework#move-pages-to-pages)Move all pages to `src/pages` directory

Having pages in separate directories in not supported with Next.js. They now have to be consolidated in the top level `pages` directory, or we recommend placing it in the `src` directory.

### [](https://blitzjs.com/docs/upgrading-from-framework#move-api-routes-to-pages-api)Move API Routes to `src/pages/api` directory

All your API Routes have to be inside of the `src/pages/api` directory.

### [](https://blitzjs.com/docs/upgrading-from-framework#wrap-app-with-blitz)Wrap your App component with `withBlitz`

To use Blitz on the client, you also have to use the `withBlitz` function in your App component.

### [](https://blitzjs.com/docs/upgrading-from-framework#convert-use-router-query-to-use-router)Convert `useRouterQuery` to `useRouter`

Blitz no longer exports `useRouterQuery`. You'll need to use the `useRouter` function instead.

### [](https://blitzjs.com/docs/upgrading-from-framework#wrap-get-ssp-static-props-api-routes)Wrapping `getServerSideProps`, `getStaticProps`, and API Routes

If you want to access the Blitz context inside of the `getServerSideProps`, `getStaticProps`, and API Routes, you'll need to wrap them with corresponding functions: `gSSP`, `gSP`, and `api` imported from `@blitzjs/next`.

To learn more about it, follow the [`@blitzjs/next` docs](https://blitzjs.com/docs/blitzjs-next).

### [](https://blitzjs.com/docs/upgrading-from-framework#replace-query-client-with-get-query-client)Replacing `queryClient` with `getQueryClient` function

If you're using `queryClient` in your code, you can replace it with the following code:

### [](https://blitzjs.com/docs/upgrading-from-framework#types-changes)`types.ts` changes

In your `types.ts` file, you'll need to change the module that is being augmented:
