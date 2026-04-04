# Source: https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/try-gemini.md.txt

<br />

After you
[set up Gemini in Firebase](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/set-up-gemini),
you can start using it to enhance your Firebase developer experience.

To open the Gemini pane:

- Click ✦**Gemini in Firebase** , located in the upper right menu of the [Firebase console](https://console.firebase.google.com/).

The Gemini pane opens and persists across all pages in the Firebase console.
You can now [chat with Gemini](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/try-gemini#chat) and explore all of
the features available in the [Gemini pane](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/try-gemini#explore).

If ✦**Gemini in Firebase** doesn't
appear in the Firebase console, follow the steps in
[Set up Gemini in Firebase for a project](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/set-up-gemini)
to enable it.

## Chat with Gemini

After you've opened the Gemini pane, you can immediately start a
conversation with Gemini and begin asking questions using
natural language.
Gemini in Firebase can generate output that seems plausible but is factually incorrect. It may respond with inaccurate information that doesn't represent Google's views. Validate all output from Gemini before you use it and do not use untested generated code in production. Do not enter personally-identifiable information (PII) or user data into the chat. For more information, see [Gemini in Google Cloud and responsible AI](https://cloud.google.com/duet-ai/docs/discover/responsible-ai).

> [!NOTE]
> **Note:** While Gemini in Firebase can answer questions about Firebase Security Rules, it is unable to generate Security Rules because it doesn't have access to your specific codebase. To generate Security Rules for Cloud Firestore and Cloud Storage, use an AI assistant that can access your codebase, such as Gemini CLI. For more information, refer to [AI Prompt: Write Firebase Security Rules](https://firebase.google.com/docs/ai-assistance/prompt-catalog/write-security-rules).

The following steps demonstrate a conversation you might have with
Gemini about [Remote Config](https://firebase.google.com/docs/remote-config):

1. In the **Ask me anything about Firebase** field, enter a question
   and then click send **Send**. For
   example, you might ask something like the following:

       When should I use a Remote Config rollout vs. an A/B Test?

   Gemini displays its response.
2. Next, you can ask Gemini clarifying questions
   to expand on the conversation or paste code in and ask for advice.

You can continue the conversation, and continue sharing information and
questions about the app and projects you're working on as you troubleshoot and
Gemini will suggest improvements and optimizations and
additional guidance. Gemini also includes [source
citations](https://cloud.google.com/gemini/docs/discover/works#how-when-gemini-cites-sources)
that list which documentation and code samples Gemini used
to generate its responses.

> [!TIP]
> **Tip:** See [Write better
> prompts](https://cloud.google.com/gemini/docs/discover/write-prompts) for information about optimizing prompts to enhance your productivity with conversational AI assistants.

## Explore the Gemini pane in the Firebase console

The Gemini pane in the Firebase console has a number of features that
simplify working collaboratively with Gemini.

| Option | Action |
|---|---|
| notifications | View Firebase alerts. |
| spark | Chat with Gemini in Firebase. |
|   | Start a new chat thread with Gemini in Firebase. |
| history | Access your chat history in Gemini in Firebase. |
| contact_support | Get help: Search the developer documentation, contact support, and check Firebase service status. |
| dark_mode | Choose a theme: Select a light or dark theme, or choose the device default. |
| text_select_start | Dock the Gemini pane to a specific location on the console. You can choose to dock the pane to the left, top, right, or bottom. |
| text_select_move_back_word | Undock the Gemini pane to return it to its original state. |
| fullscreen | Maximize the Gemini pane to take up the entire console. |
| fullscreen_exit | Restore the Gemini pane to its original size. |
|   | Report an issue to the Firebase team about your experience with Gemini in Firebase. We encourage you to report bugs, suggest improvements, or provide general feedback. |
| close | Close the Gemini pane. |

## Use personalization in Gemini in Firebase

To get the most out of Gemini in Firebase, try asking questions
related to your Firebase project. Here are some ideas:

- **Realtime Database:** "How do I structure my Realtime Database for efficient data
  retrieval in my chat app?"

- **Authentication:** "What kinds of login methods does my app support, and which
  ones can I add?""

- **Crashlytics:** "Based on my recent Crashlytics reports, what are
  the top three issues I should address to improve my app's stability?"

  If you tailor your questions to your specific Firebase setup,
  Gemini in Firebase can provide more relevant and actionable insights.

## Use AI assistance in Crashlytics

To use AI assistance in Crashlytics to generate insights about your crashes:

1. In the Firebase console, open the
   [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics)
   and select your app.

2. Locate and select a crash you want to investigate. The Crashlytics event
   page appears, including insights with one or more of the following:

   - an analysis of the crash with a possible cause
   - debugging instructions
   - actionable next steps
   - best practices

   If you don't see the AI assistance in Crashlytics feature at the top of the
   event page, verify that Gemini in Firebase has been enabled (for setup
   instructions, see
   [Set up Gemini in Firebase](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/set-up-gemini)).
   Also, make sure that you're viewing a crash or ANR event. Non-fatal events
   are not yet supported.
3. If you'd like to use AI assistance to fix the issue directly in your app's
   codebase, consider using
   [AI assistance for Crashlytics via MCP](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp).

> [!IMPORTANT]
> **Important:** AI assistance in Crashlytics is an early-stage technology that can generate output that seems plausible but is factually incorrect. It may respond with inaccurate information that doesn't represent Google's views. Validate all output from Gemini before you use it and do not use untested generated code in production. Do not log personally-identifiable information (PII) through Crashlytics APIs. For more information, see [How AI assistance in Crashlytics uses your data](https://firebase.google.com/docs/crashlytics/ai-assistance-in-dashboard#governance) and [Gemini in Google Cloud and responsible AI](https://cloud.google.com/duet-ai/docs/discover/responsible-ai).

Learn more at
[Get AI assistance in Crashlytics](https://firebase.google.com/docs/crashlytics/ai-assistance-in-dashboard).

## Get AI insights for messaging campaigns with Gemini in Firebase

Gemini in Firebase
provides messaging campaign summarization, insights,
and guidance to improve your Firebase Cloud Messaging and In-App Messaging
campaign performance. By analyzing campaign data,
Gemini in Firebase can help you understand your campaigns' reach and impact
and suggests strategies to improve user engagement and growth.

### Access AI insights for messaging campaigns

To use messaging campaign AI insights, make sure that your project has the
following:

- Gemini in Firebase is enabled for your project. Learn more at
  [Set up Gemini in Firebase](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/set-up-gemini).

- Firebase Cloud Messaging or In-App Messaging is enabled in your Firebase
  project.

- At least one campaign exists and appears in the Firebase console.

After ensuring these requirements are met:

1. Open [**Messaging**](https://console.firebase.google.com/project/_/messaging) in the
   Firebase console to access campaign data.

2. After your campaign data loads, click **Generate AI insights**.

   A summary and analysis of your messaging campaigns appears.

## Generate GraphQL queries and mutations for Data Connect with Gemini in Firebase

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

For more advanced use cases, see [AI assistance for Data Connect use
cases](https://firebase.google.com/docs/data-connect/ai-assistance#use-cases).

## Use AI assistance in Firebase App Distribution

The Firebase App Testing agent uses the power of AI to create and run tests
based on natural language prompts that you provide. The agent creates
step-by-step tests that you can run on various virtual and physical devices to
make sure your app is of the highest quality. For more information, see
[App Testing agent](https://firebase.google.com/docs/app-distribution/android/app-testing-agent).

## Use AI assistance in Firebase Studio

Gemini in Firebase provides an AI-assisted development experience within
Firebase Studio. You can use Gemini in Firebase within
Firebase Studio through two main interfaces:

- The App Prototyping agent (Prototyper view): This agent assists with prototyping and Next.js web app generation and publishing to Firebase App Hosting with Genkit-powered agentic AI flows. Learn more at [Get started with
  the App Prototyping agent](https://firebase.google.com/docs/studio/get-started-ai) and [Develop, publish, and monitor a full-stack web app with
  the App Prototyping agent](https://firebase.google.com/docs/studio/solution-build-with-ai).
- Firebase Studio workspace (Code view): Firebase Studio provides a full IDE that offers AI-assisted features to streamline your coding workflow---inline within your code editor and using chat, which can provide code suggestions, generate code, explain code concepts, update project files, run terminal commands, and interpret command output. Learn more at [About Firebase Studio
  workspaces](https://firebase.google.com/docs/studio/get-started-workspace).

Learn more at [AI assistance in Firebase Studio](https://firebase.google.com/docs/studio/ai-assistance).