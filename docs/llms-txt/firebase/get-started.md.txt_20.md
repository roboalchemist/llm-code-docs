# Source: https://firebase.google.com/docs/app-hosting/get-started.md.txt

With an existing Next.js or Angular app (Next.js versions 13.5.x+
or Angular 18.2.x+)
in a GitHub repository, getting started with App Hosting can be as
straightforward as creating an App Hosting backend and then starting a
rollout with a push to your live branch. If you don't have an app, use one of
our sample apps to walk through the steps described in this guide.

This guide describes how to set up App Hosting in the Firebase console to
automatically deploy every time a new commit is made to a GitHub repository. At
the end of this flow you'll have a live Next.js or Angular example app that is
redeployed every time you commit a new change to your GitHub repository's
`main` branch.

Though this guide focuses on the recommended Firebase console flow, there are
[other ways to
deploy](https://firebase.google.com/docs/app-hosting/alt-deploy),
including using the Firebase CLI to deploy local code without a GitHub
connection.

## Step 1: Fork the demo repository

Visit <https://github.com/firebase/apphosting-adapters> and
select **Fork**.

## Step 2: Create an App Hosting backend

In the Firebase console, open
[App Hosting](https://console.firebase.google.com/project/_/apphosting)
and select **Get started.** You'll need to upgrade to the Blaze plan to use App
Hosting.

> [!NOTE]
> **Note:** If you already have created at least one backend, select **Create backend**.

<br />

![A screenshot of App Hosting backend setup.](https://firebase.google.com/static/docs/app-hosting/images/backend-console.png)

<br />

Follow the prompts to complete these steps:

- Choose a primary region (usually the region closest to your users).
- Connect to GitHub. Choose the repository you just created by forking the firebase-framework-tools repository.
- Set your app's root directory to one of the following:
  - [**/starters/nextjs/basic**](https://github.com/firebase/apphosting-adapters/tree/main/starters/nextjs/basic)
  - [**/starters/angular/basic**](https://github.com/firebase/apphosting-adapters/tree/main/starters/angular/basic)
- Set the live branch as **main.**
- Enable automatic rollouts (automatic rollouts are enabled by default).
- Assign a name to your backend.
- Create a new Firebase web app.

Select **Finish and deploy**.

## Step 3: View the deployed app

When you create a backend, Firebase gives you a no-cost subdomain where end
users can visit your web app. Its format is
`backend-id--project-id.us-central1.hosted.app`.

In the **Backend information** row in the dashboard for your backend, select
the link to your live backend to view your new website:

<br />

![A screenshot of the backend information row with the live app link
emphasized.](https://firebase.google.com/static/docs/app-hosting/images/live-link.png)

<br />

> [!NOTE]
> **Note:** After creating your backend, it may take around five minutes for your app's URL to work.

## Step 4: Trigger a rollout by pushing a change

Once your backend is created and you have a live URL, you can
trigger the rollout of a new version of your web app whenever you push
changes into the live branch of your GitHub repository. To perform a
test of your App Hosting setup:

1. In your fork of the demo GitHub repository, navigate to the source of the
   demo app home page, make any recognizable edit you like, and then push your
   change to the main branch. To find your home page:

   - **Next.js:** `/starters/nextjs/basic/src/app/page.tsx`
   - **Angular:** `/starters/angular/basic/src/app/pages/home/home.component.html`
2. In the Firebase console, monitor
   [App Hosting](https://console.firebase.google.com/project/_/apphosting) as
   your new change is rolled out to production. When the rollout is complete,
   you can view your change in the app's home page.

## Next steps

- Go deeper: walk through a Firebase codelab that integrates a hosted app with Firebase Authentication and Google AI features: [Next.js](https://firebase.google.com/codelabs/firebase-nextjs) \| [Angular](https://firebase.google.com/codelabs/firebase-web)
- [Connect a custom domain](https://firebase.google.com/docs/app-hosting/custom-domain).
- [Configure your backend](https://firebase.google.com/docs/app-hosting/configure)---set environment variables, store secret parameters, and more.
- [Monitor rollouts, site usage, and logs](https://firebase.google.com/docs/app-hosting/rollouts).