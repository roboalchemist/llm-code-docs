# Source: https://firebase.google.com/docs/data-connect/generate-admin-sdk.md.txt

Firebase Data Connect admin SDKs let you call your queries and mutations from
trusted environments such as Cloud Functions, custom backends, or your own
workstation. In much the same way as you generate SDKs for your client apps, you
can generate a custom admin SDK in parallel as you design the schemas, queries
and mutations you deploy to your Data Connect service. Then, you integrate
methods from this SDK into your backend logic or administration scripts.

As we've mentioned elsewhere, it's important to note that Data Connect queries
and mutations are not submitted by clients at the time of the request.
Instead, when deployed, Data Connect operations are stored on the server like
Cloud Functions. This means that whenever you deploy changes to your queries and
mutations, you also need to regenerate admin SDKs and redeploy any services that
rely on them.

## Before you begin

- [Learn about designing Data Connect schemas, queries, and mutations](https://firebase.google.com/docs/data-connect/schemas-guide). In a typical workflow, you will develop them in parallel to your application code, including any services that use admin SDKs.
- [Install the Firebase CLI](https://firebase.google.com/docs/cli#setup_update_cli).
- Include [the Admin SDK for Node.js](https://firebase.google.com/docs/admin/setup) as a dependency wherever you plan to call the generated admin SDKs.

## Generate admin SDKs

After you create your Data Connect schemas, queries, and mutations, you can
generate a corresponding admin SDK:

1. Open or create a `connector.yaml` file and add an `adminNodeSdk` definition:

       connectorId: default
       generate:
         adminNodeSdk:
           outputDir: ../../dataconnect-generated/admin-generated
           package: "@dataconnect/admin-generated"
           packageJsonDir: ../..

   The `connector.yaml` file is usually found in the same directory as the
   GraphQL (.gql) files that contain your query and mutation definitions. If
   you've already generated client SDKs, this file has already been created.
2. Generate the SDK.

   If you have Data Connect VS Code extension installed, it
   will always keep generated SDKs up to date.

   Otherwise, use the Firebase CLI:

       firebase dataconnect:sdk:generate

   Or, to automatically regenerate SDKs when you update your `gql` files:

       firebase dataconnect:sdk:generate --watch

## Execute operations from an admin SDK

The generated admin SDK contains interfaces and functions that correspond with
your `gql` definitions, which you can use to perform operations on your
database. For example, suppose you generated an SDK for a database of songs,
along with a query, `getSongs`:

    import { initializeApp } from "firebase-admin/app";
    import { getSongs } from "@dataconnect/admin-generated";

    const adminApp = initializeApp();

    const songs = await getSongs(
      { limit: 4 },
      { impersonate: { unauthenticated: true } }
    );

Or, to specify a connector configuration:

    import { initializeApp } from "firebase-admin/app";
    import { getDataConnect } from "firebase-admin/data-connect";
    import {
      connectorConfig,
      getSongs,
    } from "@dataconnect/admin-generated";

    const adminApp = initializeApp();
    const adminDc = getDataConnect(connectorConfig);

    const songs = await getSongs(
      adminDc,
      { limit: 4 },
      { impersonate: { unauthenticated: true } }
    );

> [!NOTE]
> **Note:** Generated JavaScript client SDKs use the same names for interfaces and operations as generated Node.js admin SDKs. Be sure to import the correct library for your platform. If you need to use both libraries in the same file, use an import alias or namespaced import for one or both of the libraries.  
>
> `import { listMovies as adminListMovies } from '@dataconnect/admin-generated';`   
> Or:   
> `import * as Admin from '@dataconnect/admin-generated';`

#### Impersonating an unauthenticated user

Admin SDKs are intended to be run from trusted environments, and therefore have
unrestricted access to your databases.

When you run public operations with the admin SDK, you should avoid running the
operation with full administrator privileges (following the principle of least
privilege). Instead, you should run the operation either as an impersonated user
(see the next section), or as an impersonated unauthenticated user.
Unauthenticated users can only run operations marked as `PUBLIC`.

In the example above, the `getSongs` query is executed as an unauthenticated
user.

#### Impersonating a user

You can also perform operations on behalf of specific users by passing part or
all of a Firebase Authentication token in the `impersonate` option; at a minimum, you
must specify the user's user ID in the sub claim. (This is the same value as the
[`auth.uid` server value](https://firebase.google.com/docs/data-connect/mutations-guide#use_check_checkmessage_and_redact)
you can reference in Data Connect GraphQL operations.)

When you impersonate a user, the operation will succeed only if the user data
you provided passes the authentication checks specified in your GraphQL
definition.

If you're calling the generated SDK from a publicly accessible endpoint, it is
crucial that the endpoint require authentication and that you validate the
integrity of the authentication token before you use it to impersonate a user.

When using callable Cloud Functions, the authentication token is
automatically verified and you can use it as in the following example:

    import { HttpsError, onCall } from "firebase-functions/https";

    export const callableExample = onCall(async (req) => {
        const authClaims = req.auth?.token;
        if (!authClaims) {
            throw new HttpsError("unauthenticated", "Unauthorized");
        }

        const favoriteSongs = await getMyFavoriteSongs(
            undefined,
            { impersonate: { authClaims } }
        );

        // ...
    });

Otherwise, use the Admin SDK's `verifyIdToken` method to validate and decode
the authentication token. For example, suppose your endpoint is implemented as a
plain HTTP function and you have passed the Firebase Authentication token
to your endpoint using the `authorization` header, as is standard:

    import { getAuth } from "firebase-admin/auth";
    import { onRequest } from "firebase-functions/https";

    const auth = getAuth();

    export const httpExample = onRequest(async (req, res) => {
        const token = req.header("authorization")?.replace(/^bearer\s+/i, "");
        if (!token) {
            res.sendStatus(401);
            return;
        }
        let authClaims;
        try {
            authClaims = await auth.verifyIdToken(token);
        } catch {
            res.sendStatus(401);
            return;
        }

        const favoriteSongs = await getMyFavoriteSongs(
            undefined,
            { impersonate: { authClaims } }
        );

        // ...
    });

Only when performing true administrative tasks, such as data migration, from a
secure, non-publicly-accessible environment, should you specify a user ID that
did not originate from a verifiable source:

    // Never do this if end users can initiate execution of the code!
    const favoriteSongs = await getMyFavoriteSongs(
      undefined,
      { impersonate: { authClaims } }
    );

#### Running with unrestricted access

If you're performing an operation that requires admin level permissions, omit
the impersonate parameter from the call:

    await upsertSong(adminDc, {
      title: songTitle_one,
      instrumentsUsed: [Instrument.VOCAL],
    });

An operation called in this manner has complete access to the database. If you
have queries or mutations intended only to be used for administration purposes,
you should define them with the `@auth(level: NO_ACCESS)` directive. Doing so
ensures that only admin-level callers can execute these operations.