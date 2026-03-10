# Clone GitHub SvelteKit Project

Learn how to download and run a **pre-configured SvelteKit project** for CE.SDK from GitHub. This approach provides a ready-made environment, eliminating the need for initial setup.

## What’s CreativeEditor SDK?[#](#whats-creativeeditor-sdk)

CreativeEditor SDK (CE.SDK) lets you integrate a customizable image and video editor into your web app. It includes filters, text overlays, and other media editing tools, and adapts easily to your use case.

CreativeEditor SDK is a commercial product. To use it, you need a valid license key. If you don’t have one yet, you can get a free trial or purchase a license.

[Free Trial](https://img.ly/forms/free-trial)[

Purchase License

](https://img.ly/pricing)

## Who Is This Guide For?[#](#who-is-this-guide-for)

This guide is for developers who:

*   Want to skip setting up a custom environment to test CE.SDK.
*   Prefer to use a **pre-built** SvelteKit template or sample project.
*   Are comfortable using **Git** and **SvelteKit** to set up local development environments.

## What You’ll Achieve[#](#what-youll-achieve)

Follow this guide to:

*   **Clone** the project from GitHub.
*   **Install** dependencies.
*   **Run** the project locally.
*   **Access** a fully functional editor in your browser.

## Prerequisites[#](#prerequisites)

Before you start, ensure you have the following:

*   A **cloning tool** (Git, GitHub CLI, or `npx`).
*   **The latest LTS version of Node.js and npm**: Needed to install dependencies and run the local server. [Download Node.js](https://nodejs.org/).
*   A valid **CE.SDK license key**.

## Step 1: Clone the GitHub Repository[#](#step-1-clone-the-github-repository)

Begin by cloning the CE.SDK examples repository from GitHub:

Since this is a large repository, the cloning process can be **slow** depending on your network. The following steps include **alternative** methods to clone faster.

[

Git

](#tab-panel-92)[

GitHub CLI

](#tab-panel-93)[

npx

](#tab-panel-94)

Terminal window

```
git clone https://github.com/imgly/cesdk-web-examples.git
```

Clone taking too long?

Try a shallow clone instead:

Terminal window

```
git clone --depth=1 --branch main --single-branch https://github.com/imgly/cesdk-web-examples.git
```

Then, navigate to the SvelteKit folder:

Terminal window

```
cd cesdk-web-examples/integrate-with-angular
```

Terminal window

```
gh repo clone imgly/cesdk-web-examples
```

Clone taking too long?

Try a shallow clone instead:

Terminal window

```
gh repo clone imgly/cesdk-web-examples -- --depth=1 --branch main --single-branch
```

Then navigate to the SvelteKit folder:

Terminal window

```
cd cesdk-web-examples/integrate-with-angular
```

Use `npx degit` to clone only the Angular integration example:

Terminal window

```
npx degit https://github.com/imgly/cesdk-web-examples/integrate-with-sveltekit
```

## Step 2: Install the Dependencies[#](#step-2-install-the-dependencies)

At the root of the project directory, install the required dependencies using **npm**:

Terminal window

```
npm install
```

This downloads and installs all the packages specified in the project’s `package.json` file.

## Step 3: Add Your License Key[#](#step-3-add-your-license-key)

Next, add your license key to the project:

1.  Open `/src/lib/CreativeEditorSDK.svelte`.
2.  Replace the placeholder license key with your valid key:

CreativeEditorSDK.svelte

```
const defaultConfig = {  // license: "<YOUR_CE_SDK_LICENSE>", // Replace with your CE.SDK license key  // ...};
```

## Step 4: Run the Project[#](#step-4-run-the-project)

Launch the development server by running:

Terminal window

```
npm run dev
```

By default, the SvelteKit app runs on port `5173`.

1.  Navigate to `http://localhost:5173/` in your browser.
2.  Access a fully functional video and image editor in your browser.

## Troubleshooting & Common Issues[#](#troubleshooting--common-issues)

❌ **Issue**: `Module not found` or missing packages

*   Ensure you’ve run `npm install` and that it **completed** without any issues.

❌ **Error**: `'vite' is not recognized as an internal or external command, operable program or batch file.`

*   The install step also installs Vite, which the project requires to run locally. Double-check that you’ve run the following commands in the correct order:
    
    1.  `npm install`.
    2.  `npm run dev`.

❌ **Error**: `Editor engine could not be loaded: The License Key (API Key) you are using to access CE.SDK is invalid`

*   Verify that your CE.SDK license key:
    
    *   Is valid.
    *   Hasn’t expired.
    *   Is correctly added to the `defaultConfig` object.

❌ **Issue**: The editor doesn’t appear.

*   Look for any server-side errors in the terminal.
*   Check the browser console for detailed error messages.

## Next Steps[#](#next-steps)

Congratulations! You’ve successfully integrated CE.SDK into SvelteKit. When you’re ready, explore the SDK, and proceed to the next steps:

*   [Configure the Creative Editor](sveltekit/user-interface/overview-41101a/)
*   [Configure the Callbacks](sveltekit/actions-6ch24x/)
*   [Serve assets from your own servers](sveltekit/serve-assets-b0827c/)
*   [
    
    Customize interface labels and translations
    
    ](sveltekit/user-interface/localization-508e20/)
*   [Edit colors and appearance with themes](sveltekit/user-interface/appearance/theming-4b0938/)

---



[Source](https:/img.ly/docs/cesdk/sveltekit/create-composition/overview-5b19c5)