# Source: https://firebase.google.com/docs/cloud-messaging/send/admin-sdk.md.txt

# Source: https://firebase.google.com/docs/data-connect/admin-sdk.md.txt

<br />

TheFirebaseAdmin SDKis a set of server libraries that lets you interact with Firebase from privileged environments to perform actions like performing queries and mutations on aFirebase Data Connectservice for bulk data management and other operations with elevated privileges and impersonated credentials.

TheAdmin SDKprovides you with an API to call operations in both read/write and read-only modes. With the read-only operations, you have the peace of mind of implementing administrative functions that cannot modify data in your databases.

## Admin SDK Setup

To get started using the withFirebase Data Connecton your server, you'll first need to[install and set up theAdmin SDKfor Node.js](https://firebase.google.com/docs/admin/setup).

## Initialize the Admin SDK in your scripts

To initialize the SDK, import theData Connectextensions and declare your project service ID and location.  


    import { initializeApp } from 'firebase-admin/app';
    import { getDataConnect } from 'firebase-admin/data-connect';

    // If you'd like to use OAuth2 flows and other credentials to log in,
    // visit https://firebase.google.com/docs/admin/setup#initialize-sdk
    // for alternative ways to initialize the SDK.

    const app = initializeApp();

    const dataConnect = getDataConnect({
        serviceId: 'serviceId',
        location: 'us-west2'
    });

## Design queries and mutations to use with theAdmin SDK

TheAdmin SDKis useful for runningData Connectoperations, given the following considerations.

### Understand the SDK and`@auth(level: NO_ACCESS)`operation directive

Since theAdmin SDKoperates with privileges, it can execute any of your queries and mutations regardless of access levels set using[`@auth`directives](https://firebase.google.com/docs/data-connect/authorization-and-security), including the`NO_ACCESS`level.
| **Note:** If you do not set an access level for an operation, it is`NO_ACCESS`by default.

If alongside your client operations, you organize your administrative queries and mutations in`.gql`source files for import into administrative scripts, Firebase recommends that you mark the administrative operations without any authorization access level, or perhaps be more explicit and set them as`NO_ACCESS`. Either way, this prevents such operations from being executed from clients or in other non-privileged contexts.

### Use the SDK with theData Connectemulator

In prototype and test environments, it can be useful to perform data seeding and other operations on local data. TheAdmin SDKlets you simplify your workflows since it can ignore authentication and authorization for local flows. (You can also explicitly opt in to complying with your operations' authentication and authorization configuration with user impersonation.)

The Firebase Admin SDKs automatically connects to theData Connectemulator when the`DATA_CONNECT_EMULATOR_HOST`environment variable is set:  

    export DATA_CONNECT_EMULATOR_HOST="127.0.0.1:9399"

For more information, see:

- The[guide for data seeding in local development](https://firebase.google.com/docs/data-connect/data-seeding-bulk-operations)
- The[Data Connectemulator documentation](https://firebase.google.com/docs/data-connect/data-connect-emulator-suite).

## Run admin operations

TheAdmin SDKis provided for privileged operations on your critical data.

The Admin SDK provides three sets of APIs:

- Generated admin SDKs, which are type-safe SDKs generated from your`gql`definitions in the same way that you generate client SDKs.
- A general interface for running arbitrary GraphQL operations, in which your code implements queries and mutations and passes them to the read-write`executeGraphql`method or the read-only`executeGraphqlRead`method.
- A specialized interface for bulk data operations, which instead of generic`executeGraphql`methods, exposes dedicated methods for mutation operations:`insert`,`insertMany`,`upsert`, and`upsertMany`.

### Manage data with generated SDKs

You[generate admin SDKs](https://firebase.google.com/docs/data-connect/generate-admin-sdk#generate-admin-sdk)from your`gql`definitions in the same way that you generate client SDKs.

The generated admin SDK contains interfaces and functions that correspond with your`gql`definitions, which you can use to perform operations on your database. For example, suppose you generated an SDK for a database of songs, along with a query,`getSongs`:  

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

| **Note:** Generated JavaScript client SDKs use the same names for interfaces and operations as generated Node.js admin SDKs. Be sure to import the correct library for your platform. If you need to use both libraries in the same file, use an import alias or namespaced import for one or both of the libraries.  
|
| `import { listMovies as adminListMovies } from '@dataconnect/admin-generated';`  
| Or:  
| `import * as Admin from '@dataconnect/admin-generated';`

#### Impersonating an unauthenticated user

Admin SDKs are intended to be run from trusted environments, and therefore have unrestricted access to your databases.

When you run public operations with the admin SDK, you should avoid running the operation with full administrator privileges (following the principle of least privilege). Instead, you should run the operation either as an impersonated user (see the next section), or as an impersonated unauthenticated user. Unauthenticated users can only run operations marked as`PUBLIC`.

In the example above, the`getSongs`query is executed as an unauthenticated user.

#### Impersonating a user

You can also perform operations on behalf of specific users by passing part or all of aFirebase Authenticationtoken in the`impersonate`option; at a minimum, you must specify the user's user ID in the sub claim. (This is the same value as the[`auth.uid`server value](https://firebase.google.com/docs/data-connect/mutations-guide#use_check_checkmessage_and_redact)you can reference in Data Connect GraphQL operations.)

When you impersonate a user, the operation will succeed only if the user data you provided passes the authentication checks specified in your GraphQL definition.

If you're calling the generated SDK from a publicly accessible endpoint, it is crucial that the endpoint require authentication and that you validate the integrity of the authentication token before you use it to impersonate a user.

When using callableCloud Functions, the authentication token is automatically verified and you can use it as in the following example:  

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

Otherwise, use theAdmin SDK's`verifyIdToken`method to validate and decode the authentication token. For example, suppose your endpoint is implemented as a plain HTTP function and you have passed theFirebase Authenticationtoken to your endpoint using the`authorization`header, as is standard:  

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

Only when performing true administrative tasks, such as data migration, from a secure, non-publicly-accessible environment, should you specify a user ID that did not originate from a verifiable source:  

    // Never do this if end users can initiate execution of the code!
    const favoriteSongs = await getMyFavoriteSongs(
      undefined,
      { impersonate: { authClaims } }
    );

#### Running with unrestricted access

If you're performing an operation that requires admin level permissions, omit the impersonate parameter from the call:  

    await upsertSong(adminDc, {
      title: songTitle_one,
      instrumentsUsed: [Instrument.VOCAL],
    });

An operation called in this manner has complete access to the database. If you have queries or mutations intended only to be used for administration purposes, you should define them with the`@auth(level: NO_ACCESS)`directive. Doing so ensures that only admin-level callers can execute these operations.

### Manage data with`executeGraphql`methods

If you need to execute one-off operations for which you have not defined`gql`mutations or queries, you can use the`executeGraphql`method or the read-only`executeGraphqlRead`method.

#### Impersonating an unauthenticated user

When you run public operations with the admin SDK, you should avoid running the operation with full administrator privileges (following the principle of least privilege). Instead, you should run the operation either as an impersonated user (see the[next section](https://firebase.google.com/docs/data-connect/admin-sdk#impersonate-user)), or as an impersonated unauthenticated user. Unauthenticated users can only run operations marked as`PUBLIC`.  

    // Query to get posts, with authentication level PUBLIC
    const queryGetPostsImpersonation = `
        query getPosts @auth(level: PUBLIC) {
            posts {
              description
            }
        }`;

    // Attempt to access data as an unauthenticated user
    const optionsUnauthenticated: GraphqlOptions<undefined> = {
        impersonate: {
            unauthenticated: true
        }
    };

    // executeGraphql with impersonated unauthenticated user scope
    const gqlResponse = await dataConnect.executeGraphql<UserData, undefined>(queryGetPostsImpersonation, optionsUnauthenticated);

#### Impersonating a user

There are also use cases where you want your scripts to modify user data based on limited credentials, on behalf of a specific user. This approach honors the principle of least privilege.

To use this interface, gather information from a customized JWT auth token that follows the[Authenticationtoken format](https://firebase.google.com/docs/data-connect/cel-reference#auth-token-contents). Also see the[custom tokens guide](https://firebase.google.com/docs/auth/admin/create-custom-tokens).  

    // Get the current user's data
    const queryGetUserImpersonation = `
        query getUser @auth(level: USER) {
            user(key: {uid_expr: "auth.uid"}) {
                id,
                name
            }
        }`;

    // Impersonate a user with the specified auth claims
    const optionsAuthenticated: GraphqlOptions<undefined> = {
        impersonate: {
            authClaims: {
                sub: 'QVBJcy5ndXJ1'
            }
        }
    };

    // executeGraphql with impersonated authenticated user scope
    const gqlResponse = await dataConnect.executeGraphql<UserData, undefined>(queryGetUserImpersonation, optionsAuthenticated);

    // gqlResponse -> { "data": { "user": { "id": "QVBJcy5ndXJ1", "name": "Fred" } } }

#### Use administrative credentials

If you're performing an operation that requires admin level permissions, omit the impersonate parameter from the call:  

    // User can be publicly accessible, or restricted to admins
    const query = "query getProfile(id: AuthID) { user(id: $id) { id name } }";

    interface UserData {
      user: {
        id: string;
        name: string;
      };
    }

    export interface UserVariables {
      id: string;
    }

    const options:GraphqlOptions<UserVariables> = { variables: { id: "QVBJcy5ndXJ1" } };

    // executeGraphql
    const gqlResponse = await dataConnect.executeGraphql<UserData, UserVariables>(query, options);

    // executeGraphqlRead (similar to previous sample but only for read operations)
    const gqlResponse = await dataConnect.executeGraphqlRead<UserData, UserVariables>(query, options);

    // gqlResponse -> { "data": { "user": { "id": "QVBJcy5ndXJ1", "name": "Fred" } } }

An operation called in this manner has complete access to the database. If you have queries or mutations intended only to be used for administration purposes, you should define them with the`@auth(level: NO_ACCESS)`directive. Doing so ensures that only admin-level callers can execute these operations.

### Perform bulk data operations

Firebase recommends you use theAdmin SDKfor bulk data operations on production databases.

The SDK provides the following methods for working with bulk data. From the provided arguments, each method constructs and executes a GraphQL mutation.
**Note:** Specific workflows are described in more detail in the[Data seeding and bulk data management guide](https://firebase.google.com/docs/data-connect/data-seeding-bulk-operations#bulk-data-adminsdk).  


    // Methods of the bulk operations API
    // dc is a Data Connect admin instance from getDataConnect

    const resp = await dc.insert("movie" /*table name*/, data[0]);
    const resp = await dc.insertMany("movie" /*table name*/, data);
    const resp = await dc.upsert("movie" /*table name*/, data[0]);
    const resp = await dc.upsertMany("movie" /*table name*/, data);

#### Performance notes for bulk operations

Each request to the backend will incur one round trip to Cloud SQL, so the more you batch, the higher the throughput is.

However, the larger the batch size, the longer the generated SQL statement is. When the PostgreSQL SQL statement length limit is reached, you will encounter an error.

In practice, experiment to find the appropriate batch size for your workload.

## What's next?

- Learn about[seeding your databases with data using theAdmin SDK](https://firebase.google.com/docs/data-connect/data-seeding-bulk-operations)
- Review the[API for theAdmin SDK](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect).
- Use theFirebaseCLI andGoogle Cloudconsole for other project management operations, like[managing schemas and connectors](https://firebase.google.com/docs/data-connect/manage-schemas-and-connectors)and[managing services and databases](https://firebase.google.com/docs/data-connect/manage-services-and-databases).