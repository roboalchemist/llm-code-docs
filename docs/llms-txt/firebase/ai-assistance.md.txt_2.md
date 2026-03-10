# Source: https://firebase.google.com/docs/data-connect/ai-assistance.md.txt

<br />

Use Gemini in Firebase to help craft schemas, queries, and mutations for
your client-side code.

Describe your app, data model, or a desired query or mutation in natural
language, and Gemini in Firebase generates the Data Connect
equivalent.

This AI assistance is available in the following development contexts:

- In the Firebase console, you can generate, test, and deploy your schemas and operations.
- In your local environment, you can use the Firebase CLI and Data Connect VS Code extension to generate, test, and develop on your app with the emulator.
- AI-powered development tools can use Firebase MCP server to generate, test, develop your app.

Learn more about Data Connect
[schema](https://firebase.google.com/docs/data-connect/schemas-guide),
[query](https://firebase.google.com/docs/data-connect/queries-guide) and
[mutation](https://firebase.google.com/docs/data-connect/mutations-guide) syntax in guides.

## How AI assistance for Data Connect uses your data

For more information, see [How Gemini in Firebase uses your
data](https://firebase.google.com/docs/gemini-in-firebase#how-gemini-in-firebase-uses-your-data).

## Set up AI assistance for Data Connect

To use AI assistance with Data Connect, enable Gemini in Firebase
as described in [Set up
Gemini in Firebase](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/set-up-gemini).

> [!IMPORTANT]
> **Important:** Project members must have the Firebase Data Connect API Viewer role (`roles/firebasedataconnect.viewer`) to generate Data Connect operations with Gemini in Firebase. You will need Firebase Data Connect API Data Admin role (`roles/firebasedataconnect.dataAdmin`) to run generated queries in Firebase console.

## Generate schema, queries, and mutations with Gemini in Firebase

You can use AI assistance for Data Connect in many of your workflows.

> [!IMPORTANT]
> **Important:** AI assistance for Data Connect is an early-stage technology that can sometimes generate output that seems plausible but is, in fact, incorrect. It may respond with inaccurate information that doesn't represent Google's views. Validate all output from Gemini before you use it and do not use untested generated code in production. Do not enter personally-identifiable information (PII) or user data into a **Help me write GraphQL** prompt. For more information, see [How AI assistance for Data Connect uses your data](https://firebase.google.com/docs/data-connect/ai-assistance#governance) and [Gemini in Google Cloud and responsible AI](https://cloud.google.com/duet-ai/docs/discover/responsible-ai).

### In the Firebase console

When you create a Data Connect service, the Firebase console
offers a "Getting started with Gemini" experience.

You can describe an app idea, and AI assistance generates the following:

- A complete schema based on your app idea.
- Example operations and data mutations.

From the data page, you can use the **Help me write GraphQL** pen_spark button to generate and execute
operations based on natural language. Check out [some example use
cases](https://firebase.google.com/docs/data-connect/ai-assistance#use-cases).

This workflow is described in our [Get started
guide](https://firebase.google.com/docs/data-connect/quickstart). You can continue in your local
development environment with the deployed schema and operations.

### In your local environment

You can also get AI assistance from the Firebase CLI and the
Data Connect VS Code extension.

You can provide your app idea to `firebase init dataconnect`, and it generates
the following:

- A complete schema based on your app idea.
- Example operations and a seed data mutation.

The Data Connect VS Code extension provides the following features:

- **Generates/Refine Operations Code Lens** to convert GraphQL comments into Data Connect operations.
- Seamless integration with Gemini Code Assist and Firebase MCP server.

This workflow is described in our [Get started guide for local
prototyping](https://firebase.google.com/docs/data-connect/quickstart-local).

### Use the Firebase MCP server with AI-powered development tools

The Firebase MCP server works with any AI assistant tools that can act as an MCP
client, including Gemini CLI, Gemini Code Assist, Cursor, Visual Studio
Code Copilot, Claude Desktop, and Windsurf Editor.

The Firebase MCP server provides additional context and capabilities to help
AI-powered development tools work better with Data Connect. It can do
the following:

- Set up new project directories and generated SDKs.
- Build and iterate on schemas, operations based on compile errors.
- Execute operations against local emulator or backend services.
- Gather information on existing services.

To use Firebase MCP server:

1. Set up your MCP client [following this guide](https://firebase.google.com/docs/cli/mcp-server#setup).
2. Ask for help related to Data Connect. Examples prompts:
   1. "Set up a Data Connect project for a pizza delivery app."
   2. "Fix Data Connect compile errors."
   3. "In the home page, I need to show active chat rooms and friend list. Generate a Data Connect query."
   4. "What users are in my local Data Connect emulator?"
   5. "What Google Cloud regions are my Data Connect services in?"

## Example use cases for generating operations

The following sections describe sample use cases:

- [Return the top five movies in descending order by rating](https://firebase.google.com/docs/data-connect/ai-assistance#create-top-five-movie)
- [Create a mutation that adds a movie to the database based on user input](https://firebase.google.com/docs/data-connect/ai-assistance#create-a-mutation)
- [Create a query that lists reviews based on user-provided genre and ratings](https://firebase.google.com/docs/data-connect/ai-assistance#create-a-query)

### Return the top five movies in descending order by rating

To use AI assistance for Data Connect to generate GraphQL based on natural
language:

1. Open
   [Data Connect](https://console.firebase.google.com/project/_/dataconnect)
   in your project and, under **Services**, select your data source.

2. Click **Data**.

3. Click the **Help me write GraphQL** pen_spark icon. Describe in natural language
   the [query](https://firebase.google.com/docs/data-connect/queries-guide) or
   [mutation](https://firebase.google.com/docs/data-connect/mutations-guide) you want
   to generate, and click **Generate**.

   For example, if you're using the Movies data source referenced in the
   ["Build with Data Connect (web)" codelab](https://firebase.google.com/codelabs/firebase-dataconnect-web),
   you could ask, "**Return the top five movies of 2022, in descending order by
   rating**," which might return a result like the following:

       query TopMovies2022 {
         movies(where: {releaseYear: {eq: 2022}}, orderBy: [{rating: DESC}], limit: 5) {
           id
           title
           rating
           releaseYear
         }
       }

4. Review the response:

   - If the response looks correct, click **Insert** to insert the response into the code editor.
   - If the response could be refined, click **Edit** , update the prompt, and click **Regenerate**.
5. After you've accepted the response, set the following in the
   **Parameters** section, if applicable:

   - **Variables** : If your query or mutation contains variables, define them here. Use JSON to define them, for example, `{"title":"The
     Matrix", "releaseYear":"1999"}`.
   - **Authorization** : Choose the [Authorization
     context](https://firebase.google.com/docs/data-connect/authorization-and-security) (Administrator, Authenticated, or Unauthenticated) with which to run the query or mutation.

   > [!WARNING]
   > **Warning:** If you're running a [mutation](https://firebase.google.com/docs/data-connect/schemas-queries-mutations#mutations-movie), review it carefully before running it. Running a mutation in the data editor will execute the request.

6. Click **Run** in the code editor and review results.

To test multiple queries or mutations in the code editor, ensure they are
named. For example, the following query is named `GetMovie`. Move your
cursor into the first line of the query or mutation to activate the **Run**
button.

    query GetMovie($myKey: Movie_Key!) {
      movie(key: $myKey) { title }
    }

> [!NOTE]
> **Note:** If you've just created a Data Connect project and requested a new PostgreSQL instance, Data Connect will create a temporary database for you to use while your permanent PostgreSQL database is being provisioned, then migrate all data when provisioning is done. This temporary database is great for exploring your schema and CRUD operations. The temporary database is not a PostgreSQL database. It has [some limitations](https://firebase.google.com/docs/data-connect/manage-services-and-databases#ephemeral-limitations).

### Create a mutation that adds a movie to the database based on user input

This example shows how to use natural language to generate a GraphQL mutation
that populates your database. This example assumes that you're using the movie
database schema used in the [Firebase Data Connect
documentation](https://firebase.google.com/docs/data-connect) and ["Build with Data Connect
(web)" codelab](https://firebase.google.com/codelabs/firebase-dataconnect-web).

> [!WARNING]
> **Warning:** Running a mutation in the data editor will execute the mutation and may change your data.

1. From the [Firebase console](https://console.firebase.google.com/project/_/dataconnect),
   open
   **Data Connect**.

2. Select your service and data source, then open the **Data** tab.

3. Click the **Help me write GraphQL** pen_spark icon and describe your mutation:

       Create a movie based on user input.

4. Click **Generate**. The mutation is returned. For example,
   Gemini might return a mutation like:

       mutation CreateMovie($title: String!, $releaseYear: Int!, $genre: String!, $rating: Float!, $description: String!, $imageUrl: String!, $tags: [String!] = []) @auth(level: USER) {
         movie_insert(data: {
           title: $title,
           releaseYear: $releaseYear,
           genre: $genre,
           rating: $rating,
           description: $description,
           imageUrl: $imageUrl,
           tags: $tags
         })
       }

5. Review the output. If needed, click **Edit** to refine the prompt and click
   **Regenerate**.

6. Next, click **Insert** to insert the mutation into the data editor.

7. To execute the mutation, you'll need to add variables. From the
   **Parameters** section, open **Variables** and include some test variables:

       {"title":"My amazing movie", "releaseYear":2024, "genre": "Comedy",
       "rating": 8, "description": "A new movie to test mutations",
       "imageUrl": "", "tags": ["comedy","space travel"]}

8. Click **Run**.

   > [!TIP]
   > **Tip:** You can also ask Gemini to expand the output. For example, to include comments and your source prompt in the output, you might use "Create a movie based on user input. Be sure to document the mutation and include this prompt in your response".

9. Next, create a query that verifies that your movie was added. Click the
   **Help me write GraphQL** pen_spark and,
   in the box that appears, type your prompt:

       List all movies from 2024 that include all of these tags: 'space travel', 'comedy'.

   Gemini might return a response like the following:

       query ComedySpaceTravelMovies2024 @auth(level: PUBLIC) {
         movies(
           where: {
           releaseYear: { eq: 2024 },
           tags: { includesAll: ["space travel", "comedy"] }
           }
         ) {
             id
             title
             imageUrl
             releaseYear
             genre
             rating
             description
             tags
           }
       }

10. Insert and run the query. The movie you added should appear in the
    **History** field.

> [!NOTE]
> **Note:** If you've just created a Data Connect project and requested a new PostgreSQL instance, Data Connect will create a temporary database for you to use while your permanent PostgreSQL database is being provisioned, then migrate all data when provisioning is done. This temporary database is great for exploring your schema and CRUD operations. The temporary database is not a PostgreSQL database. It has [some limitations](https://firebase.google.com/docs/data-connect/manage-services-and-databases#ephemeral-limitations).

### Create a query that lists reviews based on user-provided genre and ratings

This example shows how to use natural language to generate a GraphQL query. This
example assumes that you're using the movie database used in the [Firebase Data Connect documentation](https://firebase.google.com/docs/data-connect) and ["Build with
Data Connect (web)" codelab](https://firebase.google.com/codelabs/firebase-dataconnect-web).

1. From the [Firebase console](https://console.firebase.google.com/project/_/dataconnect),
   open
   **Data Connect**.

2. Select your service and data source, then open the **Data** tab.

3. Click the **Help me write GraphQL** pen_spark icon and describe your query:

       List all movie reviews, based on user-configurable genre and ratings.

4. Click **Generate**. The query is returned. For example,
   Gemini might return a query like:

       query ListReviewsByGenreAndRating($genre: String, $minRating: Int, $maxRating: Int) @auth(level: PUBLIC) {
         reviews(where: {
           movie: {
             genre: {eq: $genre}
           },
           rating: {ge: $minRating, le: $maxRating}
         }) {
           id
           user {
             username
           }
           movie {
             title
             genre
           }
           rating
           reviewText
           reviewDate
         }
       }

5. Review the output. If needed, click **Edit** to refine the prompt and click
   **Regenerate**.

6. Next, click **Insert** to insert the mutation into the data editor.

7. To test this query, you'll need to add variables. From the **Parameters**
   section, open **Variables** and include variables to use for testing:

       {"genre":"sci-fi", "minRating":4, "maxRating":9}

8. Click **Run**.

> [!TIP]
> **Tip:** You can also ask Gemini to expand the output. For example, to include comments and your source prompt in the output, you might use "List all movie reviews, based on user-configurable genre and ratings. Be sure to document the query and include this prompt in your response."

> [!NOTE]
> **Note:** If you've just created a Data Connect project and requested a new PostgreSQL instance, Data Connect will create a temporary database for you to use while your permanent PostgreSQL database is being provisioned, then migrate all data when provisioning is done. This temporary database is great for exploring your schema and CRUD operations. The temporary database is not a PostgreSQL database. It has [some limitations](https://firebase.google.com/docs/data-connect/manage-services-and-databases#ephemeral-limitations).

## Design prompts for third-party AI assistance tools

As with all AI assistance tools, better prompts yield more useful outputs.

When you provide natural language prompts to Gemini in Firebase, behind the
scenes, the assistant translates your inputs to a more fully-developed prompt.

If you're working with third-party AI tools like Cursor or Windsurf, you can get
better Data Connect recommendations by using similar, more detailed
prompts.

We've published prompt templates for you to download, adapt, and copy into your
IDE:

- A template prompt for [schema generation](https://raw.githubusercontent.com/firebase/firebase-tools/refs/heads/master/templates/dataconnect-prompts/schema-generation-cursor-windsurf-rule.txt)
- A template prompt for [operation generation](https://raw.githubusercontent.com/firebase/firebase-tools/refs/heads/master/templates/dataconnect-prompts/operation-generation-cursor-windsurf-rule.txt)

After downloading and modifying, create a prompt in familiar tooling (for
example Cursor or Windsurf) as follows:

- In Cursor (be sure to review the latest [instructions from
  Cursor](https://docs.cursor.com/context/rules#creating-a-rule)):

  1. Click the settings icon on top right.
  2. Select the **Rules** tab.
  3. Under the **Project Rules** , click **Add a new rule** button.
  4. Copy and paste the rule.
- In Windsurf (be sure to review the latest [instructions from
  Windsurf](https://docs.windsurf.com/windsurf/cascade/memories#rules)):

  1. Open the Cascade window by clicking the **Cascade** button in the top right corner.
  2. Click the **Customizations** icon in the top right slider menu in Cascade, then navigate to the **Rules** panel.
  3. Click the **+ Global** or **+ Workspace** button to create new rules at either the global or workspace level, respectively.
  4. Copy and paste the rule.

## Troubleshoot AI assistance for Data Connect

See [Troubleshoot
Gemini in Firebase](https://firebase.google.com/docs/gemini-in-firebase/set-up-gemini#troubleshoot-gemini-in-firebase).

## Pricing

AI assistance for Data Connect is available as part of Gemini in Firebase
and is included for individual users.

See [Gemini in Firebase pricing](https://firebase.google.com/docs/gemini-in-firebase#pricing) for more
information.

## Next steps

- Learn more about [schema](https://firebase.google.com/docs/data-connect/schemas-guide), [query](https://firebase.google.com/docs/data-connect/queries-guide) and [mutation](https://firebase.google.com/docs/data-connect/mutations-guide).
- Learn more about [Gemini in Firebase](https://firebase.google.com/docs/gemini-in-firebase).