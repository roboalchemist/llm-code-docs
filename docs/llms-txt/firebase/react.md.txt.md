# Source: https://firebase.google.com/docs/data-connect/quickstart/react.md.txt

In this quickstart, you will create and deploy a small sample database and access it from a
React frontend.

## Prerequisites

To complete this quickstart, you'll need the following:

- A [Node.js](https://www.npmjs.com/) environment with NPM.
- A Google Account.

## Tutorial

| Tutorial ||
|---|---|
| ### 1. Create a new Firebase project Start by creating a new Firebase project in the [Firebase console](https://console.firebase.google.com/). Then, upgrade the project to the Blaze plan. ||
| ### 2. Initialize your project Create a new directory and initialize a Firebase project in it. When prompted, choose the following options: - Choose the project you created in the previous step. - Don't create a schema with Gemini (in this tutorial, you'll use a pre-built example schema). - Create a new Cloud SQL instance. - Create a React template. | mkdir myproj ; cd myproj npx -y firebase-tools@latest login --reauth npx -y firebase-tools@latest init dataconnect |
| ### 3. Review the example GraphQL definitions In Data Connect, you define all of your database schemas and operations using GraphQL. When you initialized your project, the Firebase CLI created some example definitions to get you started. | **dataconnect/schema/schema.gql (excerpt)** ``` type Movie @table { title: String! imageUrl: String! genre: String } type MovieMetadata @table { movie: Movie! @unique rating: Float releaseYear: Int description: String } ``` **dataconnect/example/queries.gql (excerpt)** ``` query ListMovies @auth(level: PUBLIC) { movies { id title imageUrl genre } } ``` |
| ### 4. Deploy your schemas and operations Whenever you make changes to your database schemas, queries, or mutations, you must deploy them for your changes to take effect on the database. | npx -y firebase-tools@latest deploy --only dataconnect |
| ### 5. Seed the database with sample data This seed data will give you something to look at when you test the sample app. Note that in this step you are executing arbitrary GraphQL, which is allowed for administrative tasks. | npx -y firebase-tools@latest \ dataconnect:execute dataconnect/seed_data.gql |
| ### 6. Generate a JavaScript client SDK This command uses your GraphQL definitions to generate a JavaScript library specifically for your database, complete with type definitions. You use this library in your client app to perform all database operations. You can generate libraries for multiple platforms, including Kotlin for Android, Swift for iOS, and Flutter, by adding definitions to `connector.yaml`. | npx -y firebase-tools@latest dataconnect:sdk:generate **Auto-generated React SDK (excerpt)** ```typescript export interface ListMoviesData { movies: ({ id: UUIDString; title: string; imageUrl: string; genre?: string | null; } & Movie_Key)[]; } export function useListMovies( options?: useDataConnectQueryOptions&<ListMoviesData> ): UseDataConnectQueryResult&<ListMoviesData, undefined>; ``` |
| ### 7. Set up a web app Run these commands to add a new web app to your Firebase project. | npx -y firebase-tools@latest \ apps:create web react-example npx -y firebase-tools@latest \ apps:sdkconfig web \ -o web-app/src/firebase-config.json cd web-app npm i firebase \ @tanstack/react-query \ @tanstack-query-firebase/react |
| ### 8. Write a sample React client Replace the contents of `web-app/src/App.jsx` with this simple React app. Notice that the app completes the necessary database access using a function from the generated SDK. The generated SDK for React uses TanStack Query to handle state management. | ```jsx import { initializeApp } from 'firebase/app'; import firebaseConfig from './firebase-config.json'; import { QueryClient, QueryClientProvider } from '@tanstack/react-query'; import { useListMovies } from '@dataconnect/generated/react'; import './App.css'; const app = initializeApp(firebaseConfig); const queryClient = new QueryClient(); function App() { return ( <QueryClientProvider client={queryClient}> <Movies /> </QueryClientProvider> ); } function Movies() { const { isLoading, data } = useListMovies(); if (isLoading) { return <h1>...</h1> } return ( <> {data?.movies.map( movie => <h1 key={movie.id}>{movie.title}</h1> )} </> ); } export default App; ``` |
| ### 9. Try the web app Start the development server to see the example app in action. | npm run dev |

## Next steps

### Try the Visual Studio Code extension

When developing with Data Connect, we strongly recommend using the
[Visual Studio
Code extension](https://marketplace.visualstudio.com/items?itemName=GoogleCloudTools.firebase-dataconnect-vscode). Even if you don't use Visual Studio Code as your primary development
environment, the extension provides several features that make schema and operation
development more convenient:

- A GraphQL language server, providing syntax checking and autocomplete suggestions specific to Data Connect
- CodeLens buttons in line with your code that let you read and write data from your schema definition files and execute queries and mutations from your operation definitions.
- Automatically keep your generated SDKs synchronized with your GraphQL definitions.
- Simplified local emulator setup.
- Simplified deployment to production.

### Use the Data Connect emulator for
local development

Although this tutorial showed you how to deploy Data Connect schemas and operations
directly to production, you will likely not want to make changes to your production database
while you are actively developing your app. Instead, set up the
[Data Connect emulator](https://firebase.google.com/docs/data-connect/data-connect-emulator-suite)
and do your development work against it rather than production. The emulator sets up a local
PGlite instance that behaves similarly to a live Postgres instance on CloudSQL.

### Learn how to write schemas and
operations for your app

When developing apps with Data Connect, the design of your schemas and operations
is one of the first and most important development tasks you will complete.

- [Gemini in the Firebase
  console](https://console.firebase.google.com/project/_/dataconnect/) is an AI tool that can generate Data Connect schemas from a natural language description of your app. This tool can get you started very quickly, especially if you've never worked with relational databases before.
- Alternatively, you can write database schemas, queries, and mutations directly using GraphQL. Start with the [Design Data Connect
  schemas](https://firebase.google.com/docs/data-connect/schemas-guide) page and continue to the follow-up pages to learn how to write operations.