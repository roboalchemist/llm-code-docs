# Source: https://img.ly/docs/cesdk/nuxtjs/get-started/vue/nuxt/clone-github-project-s2123y/

---
title: "Clone GitHub Nuxt Project"
description: "Using CE.SDK with a cloned Nuxt.js GitHub project"
platform: nuxtjs
url: "https://img.ly/docs/cesdk/nuxtjs/get-started/vue/nuxt/clone-github-project-s2123y/"
---

> This is one page of the CE.SDK Nuxt.js documentation. For a complete overview, see the [Nuxt.js Documentation Index](https://img.ly/docs/cesdk/nuxtjs.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/nuxtjs/llms-full.txt).

---

This guide walks you through cloning and running a **prebuilt CreativeEditor
SDK (CE.SDK)** Nuxt.js integration project from **GitHub**. It’s the fastest
way to get up and running with CE.SDK without building everything from
scratch.

## Who Is This Guide For?

This walkthrough is ideal for developers who:

- Want to **explore CE.SDK** without setting up a custom environment.
- Prefer working with a pre-configured **Nuxt.js sample project**.
- Are comfortable using **Git** and **Node.js** to manage local development environments.

## What You’ll Achieve

- Clone the CE.SDK Nuxt.js integration project from GitHub.
- Install all required dependencies and launch the project locally.
- Access a fully functional image and video editor directly in your browser.

## Prerequisites

Before starting, ensure you have:

- **Git** - Used to clone the project repository. [Download Git](https://git-scm.com/downloads).
- **The latest LTS version of Node.js and npm** - Required for installing dependencies and starting the development server. [Download Node.js](https://nodejs.org/).
- A valid **CE.SDK license key** ([Get a free trial](https://img.ly/forms/free-trial)).

## Step 1: Clone the GitHub Repository

First, clone the CE.SDK examples repository from GitHub:

```bash
git clone https://github.com/imgly/cesdk-web-examples.git
```

Then navigate to the Nuxt.js integration folder:

```bash
cd cesdk-web-examples/integrate-with-nuxt
```

## Step 2: Install the Dependencies

Install all necessary dependencies using npm:

```bash
npm install
```

## Step 3: Set Your CE.SDK License Key

Open the editor component file (located at `components/CreativeEditor.vue`) and update the configuration with your actual CE.SDK license key:

```js title="CreativeEditor.vue"
const config = {
  // license: 'YOUR_CESDK_LICENSE_KEY', // Replace with your CE.SDK license key
  // ...
};
```

## Step 4: Run the Project

Start the Nuxt.js development server by running:

```bash
npm run dev
```

Then visit `http://localhost:3000/` in your browser to access the fully functional image and video editor.

## Troubleshooting & Common Issues

❌ **Error:** `'nuxt' is not recognized as an internal or external command, operable program or batch file.`

- Ensure you’ve run `npm install` successfully before trying `npm run dev`.

❌ **Error:** `Editor engine could not be loaded: The License Key (API Key) you are using to access CE.SDK is invalid`

- Double-check that your CE.SDK license key is valid, hasn't expired, and is correctly configured in the `config` object.

❌ **Issue:** The editor doesn’t appear

- Look at your terminal output for any backend/server-side errors.
- Open your browser’s developer console to review client-side error messages that may point to the root cause.

## Next Steps

Congratulations! You’ve successfully integrated CE.SDK with Nuxt.js. When you’re ready, dive deeper into the SDK and proceed with the next steps:

- [Configure the Creative Editor](https://img.ly/docs/cesdk/nuxtjs/user-interface/overview-41101a/)
- [Serve assets from your own servers](https://img.ly/docs/cesdk/nuxtjs/serve-assets-b0827c/)
- [Create and use a license key](https://img.ly/docs/cesdk/nuxtjs/licensing-8aa063/)
- [Configure callbacks](https://img.ly/docs/cesdk/nuxtjs/actions-6ch24x/)
- [Customize interface labels and translation](https://img.ly/docs/cesdk/nuxtjs/user-interface/localization-508e20/)
- [Edit colors and appearance with themes](https://img.ly/docs/cesdk/nuxtjs/user-interface/appearance/theming-4b0938/)



---

## More Resources

- **[Nuxt.js Documentation Index](https://img.ly/docs/cesdk/nuxtjs.md)** - Browse all Nuxt.js documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/nuxtjs/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/nuxtjs/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
