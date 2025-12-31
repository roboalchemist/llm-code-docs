# Source: https://juno.build/docs/start-a-new-project.md

# Start a New Project

With Juno, a project typically lives in a single repository â combining your frontend, serverless functions, and configuration. Whether you're starting from scratch or extending an existing app, the result is a full-stack project that deploys as a single container.

---

## ð§­ Choose Your Starting Point

There are multiple ways to start a Juno project. Pick what fits best:

*   ([Use a Juno Template](#-scaffold-with-a-juno-template)) if you want everything preconfigured
*   ([Bring Your Own Framework](#-start-with-your-favorite-framework)) if youâve already picked a stack
*   ([Add Juno to an Existing Project](#-add-juno-to-an-existing-project)) for incremental adoption

---

## ð Scaffold with a Juno Template

One way to get started is by scaffolding a full-stack project using our prebuilt templates â it sets up your frontend framework of choice along with serverless functions and emulator support.

To create a new project, just run:

*   npm
*   yarn
*   pnpm

```
npm create juno@latest
```

```
yarn create juno
```

```
pnpm create juno
```

**Note:**

Supports Astro, Next.js, React, SvelteKit, Vue, and Angular.

---

## â¨ Start with Your Favorite Framework

Prefer to begin with `npx create-next-app`, `npm create svelte@latest`, or any other starter you know well? Totally fine. Set up your frontend however you like, then bring in Juno afterward.

**SSR not supported:**

Juno doesnât yet support Server Side Rendering (SSR). Your frontend code should run on the client side. We recommend using Static Site Generation (SSG) or prerendering instead.

Once your app is ready, head over to the [SDK Setup Guide](/docs/setup-the-sdk.md) to:

*   Install the SDK
*   Enable emulator support
*   Add serverless functions
*   Configure deployment

This gives you full flexibility while keeping everything in one repo.

---

## ð§© Add Juno to an Existing Project

Already have a project in development or production? You can integrate Juno incrementally.

Start with the [SDK Setup Guide](/docs/setup-the-sdk.md) and bring in only what you need â whether that's authentication, datastore, serverless functions, or all of the above.

---

## One Repo, One App

No matter how you start, Juno follows a simple principle: **one project = one repo = one container**.

Everything â frontend, backend, and app state â is bundled into a single WebAssembly (WASM) container and deployed together.

This architecture keeps development and deployment straightforward, reliable, and fully yours.