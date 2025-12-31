# Source: https://firebase.google.com/docs/studio/firebase-projects.md.txt

While you don't need a Firebase project to start working inFirebase Studio, connecting one is essential for using Firebase products. At certain points in your development process,Firebase Studiomight automatically create a project for you, or you can choose to connect one manually. This guide explains the purpose a Firebase project serves and how to connect one to your workspace inFirebase Studio.

## Understand Firebase projects

Think of a Firebase project as a container for all of your app's backend services, including user authentication, data storage, hosting, analytics, and more. By connecting yourFirebase Studioworkspace to a Firebase project, you can integrate a[suite of Firebase products](https://firebase.google.com/products)into your app.

A Firebase project can have one or more Firebase Apps registered to it (for example, both the free and paid versions of an app), but keep in mind the following:

- All Firebase Apps registered to the same Firebase project share and have access to all the same resources and services provisioned for that project.
- IfFirebase Studio[automatically creates a Firebase project for you](https://firebase.google.com/docs/studio/firebase-projects#connect-auto), it creates a new project and links it to yourFirebase Studioworkspace.
- If you[duplicate aFirebase Studioworkspace](https://firebase.google.com/docs/studio/get-started-workspace#duplicate-workspace)that's linked to a Firebase project, the duplicated workspace is linked to the same project.

Consider connecting differentFirebase Studioworkspaces to separate Firebase projects. This prevents multiple workspaces from sharing (and potentially overwriting) the same backend data and resources.

After connecting your workspace to a Firebase project, visit the[Firebase console](https://console.firebase.google.com/)for administrative and configuration tasks. This includes viewing security rules, managing user accounts, viewing detailed crash reports, editing stored data directly, and reviewing A/B test results.

## Connect aFirebase Studioapp to a Firebase project

In order to use Firebase services in your app, you'll need to connect your app to a Firebase project. For example, if you want to useFirebase Authentication, you'll need to connect to a Firebase project so that you can create and manage user accounts. At certain points during the development process,Firebase Studiocreates a Firebase project for you, or you can choose to do so manually.

### Automatically connect to a Firebase project

When using theApp Prototyping agent,Firebase Studioprovisions a Firebase project on your behalf when you:

- Auto-generate a Gemini API key
- Ask to connect your app to a Firebase project
- Ask for help connecting your app to Firebase services, such asCloud FirestoreorFirebase Authentication
- Click the**Publish** button and set upFirebase App Hosting

When using interactive chatorGemini CLI,Geminican use terminal commands or the[Firebase MCP server](https://firebase.google.com/docs/cli/mcp-server)to connect to a Firebase project when you:

- Ask to connect your app to a Firebase project
- Ask for help connecting your app to Firebase services, such asCloud FirestoreorFirebase Authentication

### Manually connect to a Firebase project

To manually connect yourFirebase Studioapp to a Firebase project:

1. In the[Firebase console](https://console.firebase.google.com/)create a new project or open an existing project:

   - **Create a new project** : Click**Create a new Firebase project**and follow the instructions to create a new project.
   - **Open an existing project**: Click the project you want to use.
2. **Note your project ID.** In the Firebase console, clicksettings\>[**Project settings**](https://console.firebase.google.com/project/_/settings/general/). The project ID is displayed in the top pane.

3. **Open your app inFirebase Studio.** If you're using theApp Prototyping agentinPrototyperview, click![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg)**Switch to Code** to openCodeview.

4. **Connect your Firebase project.** In the terminal (`Shift+Ctrl+C`), run the following commands:

   1. `touch firebase.json`This ensures a Firebase configuration file exists in your directory.
   2. `firebase login --reauth`Follow the prompts to authorize your account.
   3. `firebase use <your project ID>`Replace`<your-project-ID>`with the project ID you noted earlier.

| **Note:** To change the Firebase project connected to your workspace, prompt theApp Prototyping agentwith the project ID you want to use instead. For example, "Switch to Firebase project with ID`<your-project-id>`."

### Change the Firebase project connected to your app

To change the Firebase project associated with yourFirebase Studioworkspace, follow the instructions in[Manually connect to a Firebase project](https://firebase.google.com/docs/studio/firebase-projects#connect-manual)using the new project ID.
| **Important:** Any Firebase services you set up for the original project won't transfer over. You must set them up again in the new project.

## Identify the Firebase project connected to your app

To confirm if a Firebase project is already connected, check the top of yourFirebase Studioworkspace. The connected project ID, if one exists, is shown next to the name of your workspace. You can click the project ID to open that project directly in the Firebase console.

## Next steps

- [Understand Firebase projects](https://firebase.google.com/docs/projects/learn-more)
- [Integrate with Google and Firebase services](https://firebase.google.com/docs/studio/google-integrations)
- [Monitor and protect web apps](https://firebase.google.com/docs/studio/monitor)