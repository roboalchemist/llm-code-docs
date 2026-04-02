Source: https://docs.slack.dev/tools/deno-slack-sdk/tutorials/hello-world-app

# Hello world app

Workflow apps require a paid plan

Join the [Developer Program](https://api.slack.com/developer-program) and provision a sandbox with access to all Slack features for free.

In this tutorial, we're going to create an app based on the pre-built Hello World app. This is an app that will send a greeting to a channel.

We'll create an app, interact with it in our workspace, then review the components that made that interaction possible.

Before we begin, ensure you have the following prerequisites completed:

* Install the [Slack CLI](/tools/deno-slack-sdk/guides/getting-started).
* Run `slack auth list` and ensure your workspace is listed.
* If your workspace is not listed, address any issues by following along with the [Getting started](/tools/deno-slack-sdk/guides/getting-started), then come on back.

## Choose your adventure {#choose-your-adventure}

We can create our "Hello World" app in one of two ways:

### Use a blank app {#use-a-blank-app}

You can create a blank app with the Slack CLI using the following command:

```text
slack create hello-world-app --template https://github.com/slack-samples/deno-blank-template
```

### Use a pre-built app {#use-a-pre-built-app}

Or, you can use the pre-built [Hello World app](https://github.com/slack-samples/deno-hello-world):

```text
slack create hello-world-app --template https://github.com/slack-samples/deno-hello-world
```

For this tutorial, we'll use the pre-built app. Once you have your new project ready to go, change into your project directory.

## Explore the app structure {#explore-the-app-structure}

Let's take a look at what's inside our new "Hello World" project directory:

```text
LICENSEREADME.mdassets/deno.jsoncfunctions/import_map.jsonmanifest.tsslack.jsontriggers/workflows/
```

The first place to direct your attention are the `functions`, `triggers`, and `workflows` folders. These are where the definitions and implementations for the inner workings of your app live.

The next place to look is the `manifest.ts` file. This contains your app's manifest, which is where we can configure things like bot scopes and tell our app about our workflows.

Other items in the project include:

* `.slack/`: a home for internal configuration files, scripts hooks, and the app SDK. _This directory must be checked into your version control._ You'll also notice a `.slack/apps.dev.json` once you begin building: this file is in `.gitignore` and **should not** be checked in to version control.

* `import_map.json`: a helper file for Deno that specifies where modules should be imported from.

* `assets/`: a place to store assets related with the project. This is a great place to store the icon that your app will display when users interact with it.

With our project ready, it's time to take it for a spin — but before we do, we have _one more_ thing to do, which is to create the trigger that we'll use to kick off our workflow. We'll talk about triggers and the specific kind we're going to create in the next section. Onward!

## Trigger time {#trigger-time}

Inside the `triggers` folder, there's a file called `greeting_trigger.ts`.

This is a trigger configuration file. It's used by the CLI to create a type of [trigger](/tools/deno-slack-sdk/guides/using-triggers) called a "Link trigger."

Since this is a working sample app, it comes pre-baked with working code. The only thing we need to do so that the app will work correctly is to create the one trigger it uses to kick things off.

To create the trigger, use the `trigger create` command:

```python
slack trigger create --trigger-def "triggers/greeting_trigger.ts"
```

Since you haven't installed this trigger to a workspace yet, you'll be prompted to install the trigger to a new workspace. Select an authorized workspace in which to install the app.

When you select your workspace, you will be prompted to choose an app environment for the trigger. Choose the _Local_ option so you can interact with your app while developing locally. The CLI will then finish installing your trigger.

Once your app's trigger is finished being installed, you'll see the following output:

```text
📚 App Manifest   Created app manifest for "hello-world (local)" in "myworkspace" workspace🏠 Workspace Install   Installed "hello-world (local)" app to "myworkspace" workspace   Finished in 1.7s⚡ Trigger created   Trigger ID:   ABCD1234EFGH   Trigger Type: shortcut   Trigger Name: Send a greeting   Trigger Created Time: 2023-03-31 10:02:15 -04:00   Trigger Updated Time: 2023-03-31 10:02:15 -04:00   URL: https://slack.com/shortcuts/ABCD1234EFGH/01d8db3db6ea1a9e05012a90028ed678
```

See that "URL" in the output? Copy it from the terminal output — that's going to be how we start our workflow — and head to the next section to try it out!

## Starting a local development server {#starting-a-local-development-server}

With our Shortcut URL in hand (or, rather, in our clipboard), paste it into any public channel in your workspace. This will unfurl into a card with a **Run** button. You will also see your shortcut in the bookmarks bar in the `workflows` folder.

If you try to interact with your app right now, nothing will happen since our local development server isn't running yet. So let's get our local server running with the `run` command:

```text
slack run
```

Once your development server is running, click the **Run** button on the unfurled card, or select your shortcut's name from the `workflows` folder in the bookmark bar to start the workflow assigned to that trigger.

In the window that pops up, fill out the form and click the **Send greeting** button.

In the channel from which you executed the workflow, you'll see a new message for the user you selected in the form.

* * *

So far we have:

* created an app based on the "Hello World" app template
* created a **trigger** to interact with our app, which produced a **Shortcut URL**
* started a **local development server**

But we've only scratched the surface. The trigger you created is configured to call a [workflow](/tools/deno-slack-sdk/guides/creating-workflows), and each workflow is configured to call one or more [functions](/tools/deno-slack-sdk/guides/creating-slack-functions).

In the next section, let's dive in to see how everything is wired together!

## Take a look around: workflows {#take-a-look-around-workflows}

Let's open up the trigger file `triggers/greeting_trigger.ts`, and see how it relates to the rest of the app:

```python
// greeting_trigger.tsimport { Trigger } from "deno-slack-api/types.ts";import GreetingWorkflow from "../workflows/greeting_workflow.ts";const greetingTrigger: Trigger<typeof GreetingWorkflow.definition> = {  type: "shortcut",  name: "Send a greeting",  description: "Send greeting to channel",  workflow: "#/workflows/greeting_workflow",  inputs: {    interactivity: {      value: "{{data.interactivity}}",    },    channel: {      value: "{{data.channel_id}}",    },  },};export default greetingTrigger;
```

Triggers take inputs and pass them along to an assigned workflow. Our trigger above is configured to invoke the `greeting_workflow`; notice the special string formatting for calling the workflow's name.

When you create a trigger using a trigger definition like this one, your app will look for that workflow in all the workflows that you have registered in your manifest.

Let's go back to the parent folder of our project and open up the `manifest.ts` file next:

```python
// manifest.tsimport { Manifest } from "deno-slack-sdk/mod.ts";import GreetingWorkflow from "./workflows/greeting_workflow.ts";export default Manifest({  name: "deno-hello-world",  description:    "A sample that demonstrates using a function, workflow and trigger to send a greeting",  icon: "assets/default_new_app_icon.png",  workflows: [GreetingWorkflow],  outgoingDomains: [],  botScopes: ["commands", "chat:write", "chat:write.public"],});
```

Here you can see the `workflows` property in your app's manifest. This is where you will list out all of your workflows.

Notice at the top there's something that we saw in the trigger file, too: an import call to `GreetingWorkflow`.

The manifest registers the workflow, and then the trigger is configured to invoke it. With that in mind, let's open up that workflow to see what's going on:

```python
// workflows/greeting_workflow.tsimport { DefineWorkflow, Schema } from "deno-slack-sdk/mod.ts";import { GreetingFunctionDefinition } from "../functions/greeting_function.ts";// Here we define a new workflow called GreetingWorkflow, configuring its // required input parameters. Note how one of the input parameters is of type // `Schema.slack.types.interactivity`:const GreetingWorkflow = DefineWorkflow({  callback_id: "greeting_workflow",  title: "Send a greeting",  description: "Send a greeting to channel",  input_parameters: {    properties: {      interactivity: {        type: Schema.slack.types.interactivity,      },      channel: {        type: Schema.slack.types.channel_id,      },    },    required: ["interactivity"],  },});// Once the workflow is defined, we can "add steps" to the workflow with the // titular method `addStep`. In this case, we're using the Slack function // `OpenForm` to leverage that interactivity input parameter in order to // interact with the user (with a form):const inputForm = GreetingWorkflow.addStep(  Schema.slack.functions.OpenForm,  {    title: "Send a greeting",    interactivity: GreetingWorkflow.inputs.interactivity,    submit_label: "Send greeting",    fields: {      elements: [{        name: "recipient",        title: "Recipient",        type: Schema.slack.types.user_id,      }, {        name: "channel",        title: "Channel to send message to",        type: Schema.slack.types.channel_id,        default: GreetingWorkflow.inputs.channel,      }, {        name: "message",        title: "Message to recipient",        type: Schema.types.string,        long: true,      }],      required: ["recipient", "channel", "message"],    },  },);// After the first step, which is to send the form, we use the form data// in subsequent steps. Here, we are passing it along as inputs to // a custom function defined by `GreetingFunctionDefinition`. You'll note that // we also imported this into our workflow file. const greetingFunctionStep = GreetingWorkflow.addStep(  GreetingFunctionDefinition,  {    recipient: inputForm.outputs.fields.recipient,    message: inputForm.outputs.fields.message,  },);// Finally, we're using another Slack function called `SendMessage` to // send the results of our custom function to a channel specified by the // user filling out the form:GreetingWorkflow.addStep(Schema.slack.functions.SendMessage, {  channel_id: inputForm.outputs.fields.channel,  message: greetingFunctionStep.outputs.greeting,});export default GreetingWorkflow;
```

The trigger invokes the workflow, and the workflow invokes one or more [custom](/tools/deno-slack-sdk/guides/creating-custom-functions) or [built-in](/tools/deno-slack-sdk/guides/creating-slack-functions) functions. The workflow is also registered in the app's manifest.

Adding custom functions to your app is very similar to adding workflows, except you don't have to register them in the manifest; any functions that your workflows use are automatically registered with your app.

In our next section, let's take a look at the custom function that our workflow uses.

## Take a look around: functions {#take-a-look-around-functions}

Inside the `functions` folder we'll find the star of the show, our "Greeting" function, in `greeting_function.ts`.

This file contains both the function definition and its implementation.

At the top, just after the imports, is the definition:

```python
// greeting_function.tsimport { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";export const GreetingFunctionDefinition = DefineFunction({  callback_id: "greeting_function",  title: "Generate a greeting",  description: "Generate a greeting",  source_file: "functions/greeting_function.ts",  input_parameters: {    properties: {      recipient: {        type: Schema.slack.types.user_id,        description: "Greeting recipient",      },      message: {        type: Schema.types.string,        description: "Message to the recipient",      },    },    required: ["message"],  },  output_parameters: {    properties: {      greeting: {        type: Schema.types.string,        description: "Greeting for the recipient",      },    },    required: ["greeting"],  },});
```

Notice how it looks very similar to our workflow definition; we have inputs, outputs, and the option to mark parameters required.

Below that is its implementation:

```javascript
export default SlackFunction(  GreetingFunctionDefinition,  ({ inputs }) => {    const { recipient, message } = inputs;    const salutations = ["Hello", "Hi", "Howdy", "Hola", "Salut"];    const salutation =      salutations[Math.floor(Math.random() * salutations.length)];    const greeting =      `${salutation}, <@${recipient}>! :wave: Someone sent the following greeting: \n\n>${message}`;    return { outputs: { greeting } };  },);
```

If you go back to the workflow file, you'll see that when this function is added as a step to the workflow, the first context property we pass along is its definition. This gives us strong typing right out of the box for our custom functions.

With our trigger calling our workflow, our workflow calling our functions, and our functions automating things in our workspace, we've now seen a very small sampling of what workflow apps can do!

## Wrap it up {#wrap-it-up}

In this tutorial we've taken a tour of the "Hello World" sample app. This example only shows one [trigger](/tools/deno-slack-sdk/guides/using-triggers), [workflow](/tools/deno-slack-sdk/guides/creating-workflows), and [custom function](/tools/deno-slack-sdk/guides/creating-custom-functions), and is limited to essentially passing a string around.

### Next steps {#next-steps}

For your next challenge, perhaps consider creating [a bot to welcome users to your workspace](/tools/deno-slack-sdk/tutorials/welcome-bot)!
