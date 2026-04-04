# Source: https://firebase.google.com/docs/data-connect/web-sdk.md.txt

<br />

Firebase Data Connectclient SDKs let you call your server-side queries and mutations directly from a Firebase app. You generate a custom client SDK in parallel as you design the schemas, queries and mutations you deploy to yourData Connectservice. Then, you integrate methods from this SDK into your client logic.

As we've mentioned elsewhere, it's important to note thatData Connectqueries and mutations are not submitted by client code and executed on the server. Instead, when deployed,Data Connectoperations are stored on the server like Cloud Functions. This means you need to deploy corresponding client-side changes to avoid breaking existing users (for example, on older app versions).

That's whyData Connectprovides you with a developer environment and tooling that lets you prototype your server-deployed schemas, queries and mutations. It also generates client-side SDKs automatically, while you prototype.

When you've iterated updates to your service and client apps, both server- and client-side updates are ready to deploy.

## What is the client development workflow?

If you followed the[Get started](https://firebase.google.com/docs/data-connect/quickstart), you were introduced to the overall development flow forData Connect. In this guide, you'll find more detailed information about generating Web SDKs from your schema and working with client queries and mutations.
| You can learn client development with a quickstart app repository and build a fully-featuredData Connectapp by following our[codelab for web](https://firebase.google.com/codelabs/firebase-dataconnect-web).

To summarize, to use generated Web SDKs in your client apps, you'll follow these prerequisite steps:

1. Add Firebase to your[web](https://firebase.google.com/docs/web/setup)app.

Then:

1. Develop your app schema.
2. Initialize your client code with the[JavaScript SDK](https://firebase.google.com/docs/data-connect/web-sdk#use-core), or[React](https://firebase.google.com/docs/data-connect/web-sdk#use-core-with-react-angular)or[Angular](https://firebase.google.com/docs/data-connect/web-sdk#use-core-with-react-angular)libraries.
3. For React and Angular,[install Tanstack Query packages](https://firebase.google.com/docs/data-connect/web-sdk#tanstack-install)
4. Set up SDK generation:

   - With the**Add SDK to app**button in our Data Connect VS Code extension
   - By updating your`connector.yaml`for the[JavaScript SDK](https://firebase.google.com/docs/data-connect/web-sdk#generate-web), or[React](https://firebase.google.com/docs/data-connect/web-sdk#generate-react-angular)or[Angular](https://firebase.google.com/docs/data-connect/web-sdk#generate-react-angular).
5. Import libraries and generated code with[JavaScript SDK](https://firebase.google.com/docs/data-connect/web-sdk#import-web), or[React](https://firebase.google.com/docs/data-connect/web-sdk#import-react-angular)or[Angular](https://firebase.google.com/docs/data-connect/web-sdk#import-react-angular).

6. Implement calls to queries and mutations with the[JavaScript SDK](https://firebase.google.com/docs/data-connect/web-sdk#using-queries), or[React](https://firebase.google.com/docs/data-connect/web-sdk#operations-react-angular)or[Angular](https://firebase.google.com/docs/data-connect/web-sdk#operations-react-angular).

7. Test, by setting up theData Connectemulator with the[JavaScript SDK](https://firebase.google.com/docs/data-connect/web-sdk#emulator), or[React](https://firebase.google.com/docs/data-connect/web-sdk#emulator-react-angular)or[Angular](https://firebase.google.com/docs/data-connect/web-sdk#emulator-react-angular).

## Implement client code with theFirebaseJavaScriptSDK

This section covers how you can implement clients using theFirebaseJavaScriptSDK.

If you're using React or Angular, see alternate setup instructions and links to additional documentation about[generatingData ConnectSDKs for frameworks](https://firebase.google.com/docs/data-connect/web-sdk#react-angular).

### Initialize your app

First, initialize your app using the[standard Firebase sequence](https://firebase.google.com/docs/web/setup).  

    initializeApp({...});

### Install the generated JavaScript SDK

Use theFirebaseCLI to set upData Connectgenerated SDKs in your apps. The`init`command should detect all apps in the current folder and install generated SDKs automatically.  

    firebase init dataconnect:sdk

Connect your app to theData Connectservice.  

    import { connectDataConnectEmulator } from 'firebase/data-connect';
    import { connectorConfig } from '@dataconnect/generated';

    const dataConnect = getDataConnect(connectorConfig);
    // [Optionally] Configure the SDK to use Data Connect local emulator.
    connectDataConnectEmulator(dataConnect, 'localhost', 9399);

### Update SDKs while prototyping

If you have Data Connect VS Code extension installed, it will always keep generated SDKs up to date.

If you don't use Data Connect VS Code extension, you can use Firebase CLI to keep generated SDKs up to date.  

    firebase dataconnect:sdk:generate --watch

### Generate SDKs in build pipelines

You can use the Firebase CLI to generate Data Connect SDKs in CI/CD build processes.  

    firebase dataconnect:sdk:generate

#### Import libraries

There are two sets of imports needed to initialize your client code: generalData Connectimports and specific, generated SDK imports.

Note the`ConnectorConfig`object included in the general imports.  

    // general imports
    import { ConnectorConfig, DataConnect, getDataConnect, QueryRef, MutationRef, QueryPromise, MutationPromise } from 'firebase/data-connect';

    // generated queries and mutations from SDK
    import { listMovies, ListMoviesResponse, createMovie, connectorConfig } from '@dataconnect/generated';

| **Note:** Generated JavaScript client SDKs use the same names for interfaces and operations as generated Node.js admin SDKs. Be sure to import the correct library for your platform. If you need to use both libraries in the same file, use an import alias or namespaced import for one or both of the libraries.  
|
| `import { listMovies as adminListMovies } from '@dataconnect/admin-generated';`  
| Or:  
| `import * as Admin from '@dataconnect/admin-generated';`

### Use queries from the JavaScript SDK

The generated code will already come with predefined Query Refs. All you need to do is import and call execute on them.  

    import { executeQuery } from 'firebase/data-connect';
    import { listMoviesRef } from '@dataconnect/generated';

    const ref = listMoviesRef();
    const { data } = await executeQuery(ref);
    console.log(data.movies);

#### Call SDK query methods

Here's an example using these action shortcut functions:  

    import { listMovies } from '@dataconnect/generated';
    function onBtnClick() {
    // This will call the generated JS from the CLI and then make an HTTP request out
    // to the server.
      listMovies().then(data => showInUI(data)); // == executeQuery(listMoviesRef);
    }

#### Subscribe to changes

You can subscribe to changes (which will update any time you execute a query).  

    const listRef = listAllMoviesRef();

    // subscribe will immediately invoke the query if no execute was called on it previously.
    subscribe(listRef, ({ data }) => {
     updateUIWithMovies(data.movies);
    });

    await createMovie({ title: 'Empire Strikes Back', releaseYear: 1980, genre: "Sci-Fi", rating: 5 });\
    await listMovies(); // will update the subscription above`

#### Handle changes to enumeration fields

An app's schema can[contain enumerations](https://firebase.google.com/docs/data-connect/schemas-guide#enumeration-fields), which can be accessed by your[GraphQL queries](https://firebase.google.com/docs/data-connect/queries-guide#query-enumerations).

As an app's design changes, you may add new enum supported values. For example, imagine that later in your application's lifecycle you decide to add a FULLSCREEN value to the`AspectRatio`enum.

In theData Connectworkflow, you can use local development tooling to update your queries and SDKs.

However, before you release an updated version of your clients, older deployed clients may break.

##### Example resilient implementation

Always add a`default`branch to a`switch`statement over the enum values, or an`else`branch to an`if/else if`block comparing against the enum values. This is not enforced by the JavaScript/TypeScript language, but is the way to make client code robust in the case that new enum values are added.  

    const queryResult = await getOldestMovie();

    if (queryResult.data) {
      // we can use a switch statement's "default" case to check for unexpected values
      const oldestMovieAspectRatio = queryResult.data.originalAspectRatio;
      switch (oldestMovieAspectRatio) {
          case AspectRatio.ACADEMY:
          case AspectRatio.WIDESCREEN:
          case AspectRatio.ANAMORPHIC:
            console.log('This movie was filmed in Academy, widescreen or anamorphic aspect ratio!');
            break;
          default:
            // the default case will catch FULLSCREEN, UNAVAILABLE or _UNKNOWN
            // it will also catch unexpected values the SDK isn't aware of, such as CINEMASCOPE
            console.log('This movie was was NOT filmed in Academy, widescreen or anamorphic.');
            break;
      }

      // alternatively, we can check to see if the returned enum value is a known value
      if (!Object.values(AspectRatio).includes(oldestMovieAspectRatio)) {
        console.log(`Unrecognized aspect ratio: ${oldestAspectRatio}`);
      }
    } else {
      console.log("no movies found!");
    }

### Use mutations from the JavaScript SDK

Mutations are accessible the same way as queries.  

    import { executeMutation } from 'firebase/data-connect';
    import { createMovieRef } from '@dataconnect/generated';

    const { data } = await executeMutation(createMovieRef({ movie: 'Empire Strikes Back' }));

### Connect to theData Connectemulator

Optionally, you can connect to the emulator by calling`connectDataConnectEmulator`and then passing in theData Connectinstance, like so:  

    import { connectDataConnectEmulator } from 'firebase/data-connect';
    import { connectorConfig } from '@dataconnect/generated';

    const dataConnect = getDataConnect(connectorConfig);
    connectDataConnectEmulator(dataConnect, 'localhost', 9399);`

    // Make calls from your app

To switch to production resources, comment out lines for connecting to the emulator.
| **Note:** Calling`getDataConnect`is only required if you'd like to connect to theData Connectemulator. Otherwise the generated SDK will automatically create an instance of the`DataConnect`object for you.

## Implement client code for React and Angular

Firebase Data Connectprovides a generated SDK with hooks for React and Angular using libraries available from our partners at Invertase,[TanStack Query Firebase](https://react-query-firebase.invertase.dev/).

This library provides a set of hooks that greatly ease handling of asynchronous tasks with Firebase in your applications.

### Initialize your app

First, as with any Firebase web app, initialize your app using the[standard Firebase sequence](https://firebase.google.com/docs/web/setup).  

    initializeApp({...});

### Install TanStack Query Firebase packages

install packages for TanStack Query in your project.  

### React

    npm i --save @tanstack/react-query @tanstack-query-firebase/react
    npm i --save firebase@latest # Note: React has a peer dependency on ^11.3.0

### Angular

    ng add @angular/fire

### Generate your React or Angular SDK

As with the standard web SDK, as described[earlier](https://firebase.google.com/docs/data-connect/web-sdk#generate-web), Firebase tooling handles automatic generation of SDKs based on your schema and operations.

If you just added React or Angular to your project, re-run`firebase init dataconnect:sdk`to re-configure the generated SDKs to include the extra framework bindings.

### Import libraries

There are four sets of imports needed to initialize your React or Angular client code: generalData Connectimports, general TanStack imports, and specific imports for your JS and React generated SDKs.

Note the`ConnectorConfig`type included in the general imports.  

### React

    // general imports
    import { ConnectorConfig, DataConnect, getDataConnect, QueryRef, MutationRef, QueryPromise, MutationPromise } from 'firebase/data-connect';

    // TanStack Query-related functions
    import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

    // generated queries and mutations from SDK
    import { ListMoviesResponse, connectorConfig } from '@dataconnect/generated';

    // generated React hooks from SDK
    import { useListAllMovies, useCreateMovie } from "@dataconnect/generated/react";

### Angular

    // general imports
    import { ConnectorConfig, DataConnect, getDataConnect, QueryRef, MutationRef, QueryPromise, MutationPromise } from 'firebase/data-connect';

    // TanStack Query-related functions
    import { provideTanStackQuery, QueryClient } from "@tanstack/angular-query-experimental";

    // generated queries and mutations from SDK
    import { ListMoviesResponse, connectorConfig } from '@dataconnect/generated';

    // generated React hooks from SDK
    import { injectListAllMovies, injectCreateMovie } from "@dataconnect/generated/angular";

### Use queries and mutations in your React or Angular client

With setup complete, you can incorporate methods from the generated SDK.

In the following snippet, notice the`use`-prefixed method`useListAllMovies`for React and the`inject`-prefixed method`injectListAllMovies`for Angular, both from the generated SDK.  

### React

All such operations in the generated SDK, both queries and mutations, call TanStackQuery bindings:

- Queries call and return the[TanStack`useDataConnectQuery`hook](https://react-query-firebase.invertase.dev/react/data-connect/querying)
- Mutations call and return the[TanStack`useDataConnectMutation`hook](https://react-query-firebase.invertase.dev/react/data-connect/mutations)

    import { useListAllMovies } from '@dataconnect/generated/react';

    function MyComponent() {
      const { isLoading, data, error } = useListAllMovies();
      if(isLoading) {
        return <div>Loading...</div>
      }
      if(error) {
        return <div> An Error Occurred: {error} </div>
      }
    }

    // App.tsx
    import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
    import MyComponent from './my-component';

    function App() {
      const queryClient = new QueryClient();
      return <QueryClientProvider client={queryClient}>
        <MyComponent />
      </QueryClientProvider>
    }

### Angular

**Note:** `ng add @angular/fire`will automatically do this for you, but if you choose to manually set it up, you can do so with the following code:  

    import { injectAllMovies, connectorConfig } from '@dataconnect/generated/angular';
    import { provideDataConnect, getDataConnect } from '@angular/fire/data-connect';
    import { provideTanStackQuery, QueryClient } from "@tanstack/angular-query-experimental";
    const queryClient = new QueryClient();
    ...
    providers: [
      ...
      provideTanStackQuery(queryClient),
      provideDataConnect(() => {
        const dc = getDataConnect(connectorConfig);
        return dc;
      })
    ]

### Use auto reload queries with React and Angular

You can configure queries to automatically reload when data changes.  

### React

    export class MovieListComponent {
      movies = useListAllMovies();
    }

    export class AddPostComponent {
      const mutation = useCreateMovie({ invalidate: [listAllMoviesRef()] });
      addMovie() {
        // The following will automatically cause Tanstack to reload its listAllMovies query
        mutation.mutate({ title: 'The Matrix });
      }
    }

### Angular

    // class
    export class MovieListComponent {
      movies = injectListAllMovies();
    }

    // template
    @if (movies.isPending()) {
        Loading...
    }
    @if (movies.error()) {
        An error has occurred: {{  movies.error() }}
    }
    @if (movies.data(); as data) {
        @for (movie of data.movies; track movie.id) {
        <mat-card appearance="outlined">
            <mat-card-content>{{movie.description}}</mat-card-content>
        </mat-card>
        } @empty {
            <h2>No items!</h2>
        }
    }

### Connect to theData Connectemulator

Optionally, you can connect to the emulator by calling`connectDataConnectEmulator`and then passing in theData Connectinstance to your generated hook, like so:  

### React

    import { getDataConnect, connectDataConnectEmulator } from 'firebase/data-connect';
    import { connectorConfig } from '@dataconnect/generated';
    import { useListAllMovies } from '@dataconnect/generated/react';

    const dc = getDataConnect(connectorConfig);
    connectDataConnectEmulator(dc, 'localhost', 9399);

    class AppComponent() {
      ...
      const { isLoading, data, error } = useListAllMovies(dc);
      ...
    }

### Angular

    // app.config.ts
    import { provideDataConnect } from '@angular/fire/data-connect';
    import { getDataConnect, connectDataConnectEmulator } from 'firebase/data-connect';
    provideDataConnect(() => {
      const dc = getDataConnect(connectorConfig);
      connectDataConnectEmulator(dc, 'localhost', 9399);
      return dc;
    }),

To switch to production resources, comment out lines for connecting to the emulator.
| **Note:** Calling`getDataConnect`is only required if you'd like to connect to theData Connectemulator. Otherwise the generated SDK will automatically create an instance of the`DataConnect`object for you.

## Data types in the SDK

TheData Connectserver represents common GraphQL data types. These are represented in the SDK as follows.

| Data Connect Type | TypeScript |
|-------------------|------------|
| Timestamp         | string     |
| Date              | string     |
| UUID              | string     |
| Int64             | string     |
| Double            | Number     |
| Float             | Number     |

### Update SDKs while prototyping

If you have Data Connect VS Code extension installed, it will always keep generated SDKs up to date.

If you don't use Data Connect VS Code extension, you can use Firebase CLI to keep generated SDKs up to date.  

    firebase dataconnect:sdk:generate --watch

### Generate SDKs in build pipelines

You can use the Firebase CLI to generate Data Connect SDKs in CI/CD build processes.  

    firebase dataconnect:sdk:generate