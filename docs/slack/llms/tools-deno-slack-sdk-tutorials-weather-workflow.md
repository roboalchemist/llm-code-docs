Source: https://docs.slack.dev/tools/deno-slack-sdk/tutorials/weather-workflow

# Check the weather using a custom step in Workflow Builder

In this tutorial, we'll create a workflow that tells us what the weather is like in our locale using a custom function to call a third-party API and Workflow Builder in Slack. Workflow Builder creates workflows that automate routine tasks and processes in Slack through the use of steps. These steps include Slack-native functions (creating a channel, sending a message, opening a form, etc.) and custom functions, which you define.

Your workflow in Slack will contain:

* **Built-in function**: Collect info in a form
* **Custom function**: Weather function that calls a third-party API
* **Built-in function**: Send an ephemeral message with the output of the custom function

## Get started {#get-started}

### Set up tools {#set-up-tools}

We are using the [Slack CLI](/tools/slack-cli) and [Deno Slack SDK](/tools/deno-slack-sdk) to create an app where the custom function exists and can be pulled into Workflow Builder to be used as a step. You should be familiar with the Slack CLI and how it works before going further. If this is new for you, we recommend starting with the [Hello world app](/tools/deno-slack-sdk/tutorials/hello-world-app) first.

### Create the project {#create-the-project}

Next, navigate to a directory where you have permission to create new files. Using the Slack CLI, run the following command to create a new project from a template:

```text
slack create weather-app --template slack-samples/deno-function-template
```

This creates your project from a blank template. After that, navigate to your project folder.

```text
cd weather-app
```

Open the project in VSCode.

```text
code .
```

### Create an account with OpenWeather {#create-an-account-with-openweather}

Create an account with [openweathermap.org](https://openweathermap.org/), which is where we’ll be pulling weather information from. Follow the prompts on [this page](https://home.openweathermap.org/users/sign_up) and once you’ve created an account, navigate to the API keys tab to retrieve your API key. Set this key as an environment variable by creating a file in your project named `.env` and putting the key in there, so that it looks like this:

```html
WEATHER_API_KEY=<YOUR-TOKEN-HERE>
```

Save the file.

## Code the custom step {#code-the-custom-step}

In order to get the weather via the OpenWeather API, we'll need to code a custom step.

We’ll be calling the OpenWeather API to get weather information from around the world. The specific API method that should be called is the [current weather data by city name](https://openweathermap.org/current#name). As for outputs, you’ll want the `weather.description`, which gives us a description of the weather in plain language.

Within your project, the foundation has already been laid for you to create your function. This function will show up in Workflow Builder as a step that you can add to any workflow.

Copy and paste the code below into the `sample_function.ts` file in your project. Rename the file to `weather_function.ts`, then save your changes.

```python
import { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";export const WeatherFunctionDefinition = DefineFunction({  callback_id: "weather_function",  title: "Weather function",  description:    "Weather function that checks a location for the weather ",  source_file: "functions/weather_function.ts",  // These input parameters correspond to fields within your form, which are passed along to this step.  input_parameters: {    properties: {      location: {        type: Schema.types.string,        description: "Location of where we're getting the weather",      },    },    required: ["location"],  },  // Your function will produce a single string output that can be used in your workflow.  output_parameters: {    properties: {      weather_result: {        type: Schema.types.string,        description: "The weather of the inputted location",      },    },    required: ["weather_result"],  },});export default SlackFunction(  WeatherFunctionDefinition,  async ({    env,    inputs,  }) => {    // Call this OpenWeather API method to retrieve the `weather.description` parameter from the JSON result.    const location = inputs.location;    const api_key = process.env.WEATHER_API_KEY;    const resp = await fetch(      `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${api_key}`,    );    const weather_json = await resp.json();    // Use this to view the JSON object if needed!    // console.log(weather_json)    const weather_result = weather_json.weather[0].description;    return {      outputs: {        weather_result,      },    };  },);
```

### Update the manifest {#update-the-manifest}

The `manifest.ts` file declares everything about your app, from which functions it hosts to which domains that your app will call. There are a few things that we need to change here in order for you to be able to find your step within Workflow Builder.

* Change the name of your app to something like `<your-name>-weather-function`. e.g. `my-weather-function`.
* Within the `outgoingDomains` array, add the `api.openweathermap.org` domain.
* Add an icon of your choice and update the filepath for it.

```python
//manifest.tsimport { Manifest } from "deno-slack-sdk/mod.ts";import { WeatherFunctionDefinition } from "./functions/weather_function.ts";export default Manifest({    name: "my-weather-function",    description: "A custom function for finding the weather based on location.",    icon: "icon.png",    workflows: [],    functions: [ WeatherFunctionDefinition ],    outgoingDomains: ["api.openweathermap.org"],    datastores: [],    botScopes: [        "commands",        "chat:write",        "chat:write.public",    ]});
```

### Run your app {#run-your-app}

Now that you’ve finished coding your app, let's test it in the wild. Run your app locally by using the following command:

```text
slack run
```

After following the prompts, a successful `slack run` execution will show the message `Connected, awaiting events` in the terminal window. This means that your app is up and ready to go. Your step is now available in Workflow Builder.

## Create a workflow with Workflow Builder {#create-a-workflow-with-workflow-builder}

Now that we have everything in place, let’s start building our workflow. To create a new workflow, you will need to open Workflow Builder in Slack. You can open Workflow Builder using one of the following methods.

* **Use the message box:** In any channel, type `/workflow` and select **Create a workflow**.
* **Use the sidebar:** Navigate to the left sidebar in Slack and click **More**, then **Tools**, then **Workflows**. Click **+New** then **Build Workflow** to create a new workflow.

Under **Start the workflow...**, click **Choose an event**, then select **From a link in Slack**. It might make more sense that this workflow runs on a schedule, but for ease of testing, we’ll use a link.

The next page you’ll see is your workflow’s main page. Take a moment here to update your workflow name.

### Add a form workflow step {#add-a-form-workflow-step}

The first step that you’ll add to your workflow is a form. Click **\+ Add step**, then select **Collect info in a form**. Name your form, then add a question. Ask your users for the location for which they want the weather and select **Short answer** for the answer type. After you add this question to your form, you’ll be able to access it as a variable in subsequent steps. Save your changes.

### Add the custom step {#add-the-custom-step}

Next we'll add the custom step we coded to your workflow. Click the button to add another step, then search for the function name in the left sidebar. Select the **Weather function** as a step. For the location, click the variable field `{}` to the right and select **Answer to: Which location would you like the weather for?**. Save your changes.

### Send a message with your weather result {#send-a-message-with-your-weather-result}

The last step is to send your user a message to notify them of the weather result. Add another step to the workflow and search for **Messages** > **Send a “only visible to you” message**. For the **Select a channel** field, choose **Channel where the workflow was used**. For the **Select a member of the channel** field, choose **Person who used this workflow**. Add a message in the text box including the input and output variables. It might look something like this: The weather for **Answer to Which location would you like the weather for?** today is **Weather Result**.

Save your changes. Publish your workflow by clicking the green **Finish Up** button, then the **Publish** button. Once your workflow is published, it will give you a link to trigger the workflow. Copy and paste this link into a test channel, then click the button to run the workflow.

## Deploy the app {#deploy-the-app}

We’ve used `slack run` to run our app on our local machine, but as soon as you shut that environment down or turn off your computer, the function will stop running. Deploying your function to infrastructure managed by Slack ensures that the function is always available.

To deploy your function to production, run the following command:

```text
slack deploy
```

Choose the appropriate workspace for deployment. The local version (`slack run`) and the production version (`slack deploy`) are separate apps. Update the workflow in Workflow Builder to use the production function and reconnect input variables.
