# Clone GitHub Vue Project

This guide will walk you through downloading and running a pre-built CreativeEditor SDK (CE.SDK) Vue.js integration project from GitHub. It’s the fastest way to get started with CE.SDK without the need to build anything from scratch.

## Who Is This Guide For?[#](#who-is-this-guide-for)

This guide is designed for developers who:

*   Want to explore CE.SDK without the hassle of configuring a custom environment.
*   Prefer getting started with a ready-made Vue.js sample project.
*   Are familiar with Git and Node.js for setting up local development environments.

## What You’ll Achieve[#](#what-youll-achieve)

By following this guide, you will:

*   Clone the CE.SDK Vue.js integration project from GitHub.
*   Install the required dependencies and run the project on your local machine.
*   Launch a fully functional image and video editor directly in your browser.

## Prerequisites[#](#prerequisites)

Before you begin, make sure you have the following:

*   **Git**: Needed to clone the project from GitHub. [Download Git](https://git-scm.com/downloads).
*   **The latest LTS version of Node.js and npm**: Required for installing dependencies and running the local server. [Download Node.js](https://nodejs.org/).
*   A valid **CE.SDK license key** ([Get a free trial](https://img.ly/forms/free-trial)).

## Step 1: Clone the GitHub Repository[#](#step-1-clone-the-github-repository)

Clone the CE.SDK examples repository from GitHub:

Terminal window

```
git clone https://github.com/imgly/cesdk-web-examples.git
```

Then navigate to the Vue integration folder:

Terminal window

```
cd cesdk-web-examples/integrate-with-vue
```

## Step 2: Install the Dependencies[#](#step-2-install-the-dependencies)

Once inside, install the necessary dependencies via npm by running:

Terminal window

```
npm install
```

This will download and install all the packages listed in the project’s `package.json` file.

## Step 3: Set Your CE.SDK License Key[#](#step-3-set-your-cesdk-license-key)

Open the `App.vue` component and replace the placeholder license key with your valid CE.SDK key:

**Note:** The cloned repository includes an example-specific license key for demonstration purposes only. You must replace this with your own valid license key for production use. [Get a free trial license](https://img.ly/forms/free-trial).

```
export default {  name: 'App',  components: { CreativeEditor },  data() {    return {      editorConfig: {        license: '<YOUR_CE_SDK_LICENSE>', // replace this with your CE.SDK license key        // ...      },    };  },};
```

This configuration will be passed down as a prop to the CE.SDK editor component (imported from `components/CreativeEditor.vue`).

## Step 4: Run the Project[#](#step-4-run-the-project)

Launch the local [Vite](https://vite.dev/) development server by executing:

Terminal window

```
npm run dev
```

By default, the Vue.js application will be available on your localhost at `http://localhost:5173/`. Open this URL in your browser to see the creative editor component in action.

## Troubleshooting & Common Issues[#](#troubleshooting--common-issues)

❌ **Issue**: `Module not found` or missing packages

*   Make sure you’ve run `npm install` and that it completed successfully without any errors.

❌ **Error**: `'vite' is not recognized as an internal or external command, operable program or batch file.`

*   Confirm that you ran `npm install` before running `npm run dev`. This step also installs Vite, which is necessary to run the project locally.

❌ **Error**: `Editor engine could not be loaded: The License Key (API Key) you are using to access CE.SDK is invalid`

*   Ensure your CE.SDK license key is valid, hasn’t expired, and has been properly passed to the `CreativeEditor` component’s props.

❌ **Issue**: The editor doesn’t load

*   Check the browser’s console for any specific error messages.

## Next Steps[#](#next-steps)

Congratulations! You’ve successfully integrated CE.SDK with Vue.js. When you’re ready, explore the SDK and move on to the next steps:

*   [Perform Basic Configuration](vue/user-interface/overview-41101a/)
*   [Configure the Callbacks](vue/actions-6ch24x/)
*   [Serve assets from your own servers](vue/serve-assets-b0827c/)
*   [Add Localization](vue/user-interface/localization-508e20/)
*   [Adapt the User Interface](vue/user-interface/appearance/theming-4b0938/)

---



[Source](https:/img.ly/docs/cesdk/vue/filters-and-effects/support-a666dd)