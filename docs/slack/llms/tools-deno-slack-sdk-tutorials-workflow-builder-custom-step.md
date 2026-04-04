Source: https://docs.slack.dev/tools/deno-slack-sdk/tutorials/workflow-builder-custom-step

# Create a custom step for Workflow Builder with the Deno Slack SDK

Workflow apps require a paid plan

Join the [Developer Program](https://api.slack.com/developer-program) and provision a sandbox with access to all Slack features for free.

Custom functions in apps can be added as workflow steps in Workflow Builder.

In this tutorial, you will define and implement a [custom function](/tools/deno-slack-sdk/guides/creating-custom-functions), then wire it up as a workflow step in our no-code automation platform [Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Workflow-Builder).

When finished, you'll be ready to build custom, scalable functions for anyone using Workflow Builder in your workspace.

You'll build three things in this tutorial:

* A custom function
* A workflow app
* A workflow in Workflow Builder

The custom function will take a user-supplied string—the name of a composite color—and use a switch statement to return a new string—the meaning of the color—based on its value. The function will collect the input string from the user once the workflow is started, then return the result to the user in the form of an ephemeral message. An _ephemeral_ message in Slack is one that is only visible to the user.

To protect your organization, external users (those outside your organization connected through Slack Connect) cannot use a workflow that contains connector functions built by your organization.

This may manifest in a `home_team_only` warning. Refer to [this help center article](https://slack.com/help/articles/14844871922195-Slack-administration--Manage-workflow-usage-in-Slack-Connect-conversations#enterprise-grid-1) for more details.

Skip to the code

If you'd rather skip the tutorial and just head straight to the code, create a new app and use our [function sample](https://github.com/slack-samples/deno-function-template) as a template. The sample custom function provided in the template will be a good place to start exploring!

### The road ahead {#the-road-ahead}

1. We'll sketch out what we want the function to do and how users will integrate it in their workflows.
2. You'll write the custom function and deploy the app so you can use the step in Workflow Builder.
3. You'll find the workflow step in Workflow Builder and use it as a step in a workflow that you can run from inside Slack.

Ready? Let's get started!

## Install & authorize the Slack CLI {#install--authorize-the-slack-cli}

> Have you installed the CLI? Are you authorized in a workspace? If you answered 'yes' to both questions, skip this step!

You'll need to have the Slack CLI **installed** and **authorized** to begin this tutorial. If you need help, follow the [Quickstart](/tools/deno-slack-sdk/guides/getting-started) guide and you'll be ready to build.

You'll also need a development workspace where you have permission to install apps. Please note that the features in this tutorial require that the workspace be part of a [paid Slack plan](https://slack.com/pricing).

## Create a new app {#create-a-new-app}

When you deploy custom functions for Workflow Builder, users will be able to search for your deployed app and then include any steps you've provided for them.

Let's get our new app project started so we can define and then implement our custom function.

With your CLI authorized, go to your terminal and create a new app with the blank template:

1. Run the command `slack create meaning-of-color`. This will tell the CLI you want to create a new workflow app named `meaning-of-color`.

2. When prompted to select a template to build from, select the **Blank template**.

3. When the CLI is finished setting up your project, follow the instructions in your terminal to `cd` into your project's directory.

VS Code

If you're using VS Code, once you `cd` into your project's directory, open it up with VS code by executing `code .`.

## Create a new custom function {#create-a-new-custom-function}

Create a new folder called `functions`.

In the `functions` folder, create a new file called `interpret_color.ts` where you'll will define and implement a custom Slack function.

Start the file off by importing the necessary modules:

```python
import { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";
```

Next, define a new custom function named `InterpretColorFunction`. It should have a single string as both an input and output parameter:

```javascript
export const InterpretColorFunction = DefineFunction({  callback_id: "interpret_color_function",  source_file: "functions/interpret_color.ts",  title: "Interpret Color",  input_parameters: {    properties: {      input_string: {        type: Schema.types.string,      },    },    required: ["input_string"],  },  output_parameters: {    properties: {      result: {        type: Schema.types.string,      },    },    required: ["result"],  },});
```

The `title` property will be used to identify this function for users in Workflow Builder.

With the function defined, the next step is to implement it. This function will take the `input_string` and run it through a switch statement, then return a new string based on the matching case:

```javascript
export default SlackFunction(  InterpretColorFunction,  ({ inputs }) => {    const input_string = inputs.input_string;    switch (input_string) {      case "orange":        return {          outputs: {            input_string,            result: "Orange is the color of ambition",          },        };      case "green":        return {          outputs: {            input_string,            result: "Green is the color of collaboration",          },        };      case "purple":        return {          outputs: {            input_string,            result: "Purple is the color of harmony",          },        };      default:        return {          outputs: {            input_string,            result: "That's not a color I recognize",          },        };    }  },);
```

The function is aware of three composite colors: orange, green, and purple. If a user supplies one of those composite colors as input, the function will return a fun meaning of that color. If the user supplies a color that is not known (i.e., not orange, green, or purple), then they'll get the default case message.

In every return statement, the function includes both the required output (the `result` string) as well as the original input (the `input_string` string), which is not a required output parameter. This is a design decision that you can make depending on your use case; include the inputs in the return value if you want them available as inputs in follow-on workflow steps.

## Configure the app's manifest {#configure-the-apps-manifest}

Your app's manifest is where you configure which functions your app should care about, among other things. To do that, import your custom function and add it to your manifest's `functions` property.

Start by opening `manifest.ts` and importing `InterpretColorFunction`:

```python
import { Manifest } from "deno-slack-sdk/mod.ts";// Add this:import { InterpretColorFunction } from "./functions/interpret_color.ts";
```

Next, configure your app's manifest. For this tutorial, update the `name`, `description`, and `functions` property:

```javascript
export default Manifest({  name: "Meaning of Color App",  description: "The meaning of colors",  icon: "assets/default_new_app_icon.png",  functions: [InterpretColorFunction],  workflows: [],  outgoingDomains: [],  botScopes: ["commands", "chat:write", "chat:write.public"],});
```

This app is now finished!

In the next section, you'll start a local development server and test drive the app before deploying it for your users.

## Start the local development server {#start-the-local-development-server}

Start a local development server with `slack run`.

Since this is the first time starting the local development server for this project, you'll be prompted to choose a local environment. The local environment is the Slack workspace you will be using to interact with the app you're currently developing.

Select the option to install to a new workspace, then select the workspace you want to use for development.

Once your local development server has started, you'll see it says `Connected, awaiting events` in your terminal window.

At this point, you're ready to build a workflow in Workflow Builder to test your custom function.

## Keep your local development server running while building the workflow!

## Use the workflow step in Workflow Builder {#use-the-workflow-step-in-workflow-builder}

In the workspace you just installed your app, open up Workflow Builder and create a new workflow:

1. From your desktop, click your workspace name in the top left.
2. Select **Tools** from the menu, then click **Workflow Builder**. This will open a new window titled "Workflow Builder."
3. In the "Workflow Builder" window that just opened, click the **Create Workflow** button in the top right.

You can also find this screen by navigating to the left-side nav menu in Slack and clicking the ellipses **...More** tile, then selecting **Automations**.

There are many ways to start a workflow in Workflow Builder. For this tutorial, we will use a link trigger. Under **Start the workflow...**, select **Choose an event**, then select **From a link in Slack**:

![Creating a new workflow in Workflow Builder](/assets/images/1-78428b4e9a7814a393e0e69f7b29626f.png)

A modal will appear that show you an example **workflow link** (more on that soon) along with a scrollable container that reveals a **Custom inputs** section. Click the **Add Input** button.

Depending on which Slack plan you are on, the latest version of Workflow Builder may still be rolling out and your UI may appear differently.

If you do not see an **Add Input** button, we recommend skipping to the code and using our [function sample](https://github.com/slack-samples/deno-function-template) as a template.

![Adding custom inputs to a new workflow in Workflow Builder](/assets/images/2-83fb385b3380ad576c374af83995be25.png)

After clicking the **Add Input** button, a form will appear. Use this form to describe the required input parameter for your custom function—i.e., the `color` to interpret. When you're done, click the **Done** button:

![Configuring custom inputs to a new workflow in Workflow Builder](/assets/images/3-c5f941358ab2b40467076455bf217cb5.png)

After clicking **Done**, the form will disappear and you'll see the custom input you just defined listed above the **Add Input** button. Since your custom function only has one required input, you can now click the **Continue** button to start building the workflow:

![Finishing creating a new workflow in Workflow Builder](/assets/images/4-76f82b41bf0c524e8785fc41b9e4fee3.png)

You'll now be editing your workflow. The only thing configured right now is the trigger that will start your workflow. Recall that this workflow ought to do two things: run the custom function to get the result of the color interpretation, then send an ephemeral message to the user who ran the workflow.

To add your custom function as a step in this workflow, search for the name of the function ("Interpret Color") in the right-hand **Steps** sidebar:

![Searching for a custom function in Workflow Builder](/assets/images/5-2ee7e516ff2093d339242f5bdde9b16c.png)

In the search results that appear in the right-hand sidebar, you should see the name of your app ("Meaning of Color App") along with "(local)", which indicates that this function is provided via your local development server at this time, followed by your "Interpret Color" function. Click on the **Interpret Color** function to begin adding it to your workflow:

![Configuring inputs for custom function in Workflow Builder](/assets/images/6-22c9b8f196561ea01ac82bac85c80fe8.png)

As soon as you click on your function to add it to your workflow, you'll be presented with a modal prompting you for an **Input String**. This is your custom function's required input parameter, so pass in the custom input you configured earlier when first creating this workflow. To do that, click on the curly braces icon to the right of the text box labelled "Input String", then select **Color** from the dropdown.

When you're finished, click **Save** to go back to editing your workflow:

![Selecting custom input for function input in Workflow Builder](/assets/images/7-aad86ae39edf39cd221177d4c92cffb5.png)

Your function—along with the input configuration you set up—is now the first step in the workflow following the trigger. The last thing this workflow needs to do is send an ephemeral message to the user that started it.

In the **Steps** sidebar on the right, click **Messages**:

![Locating Messages functions in Workflow Builder](/assets/images/8-57d245ea6621d3848796cc1a043bd904.png)

This brings up built-in functions for common Slack messaging that you can use as steps in your workflow.

Select **Send an "only visible to you" message**, which sends an ephemeral message to a user that only they can see:

![Selecting the ephemeral message function in Workflow Builder](/assets/images/9-f7d88fad33470bc0c7016ab5764e22e4.png)

After you select **Send an "only visible to you" message**, a modal will appear where you can configure this step.

For **Select a channel**, choose the option **Channel where the workflow was used**.

For **Select a member of the channel**, choose the option **Person who used this workflow**.

For the **Add a message** field, select the **Insert a variable** link below the textbox:

![Configuring ephemeral message step in Workflow Builder](/assets/images/10-bfa5f8fcc7a8108c4e102676fd0a8e48.png)

In the **Insert a variable** menu that appears, select the **Result** option located in your custom function's output variable group.

![Selecting custom function output for ephemeral message step in Workflow Builder](/assets/images/11-dea11b9f04487257273e18f1675da36e.png)

When you're done, **Save** this step to return to the workflow editor:

![Saving ephemeral message step in Workflow Builder](/assets/images/12-ec44bfff24d6f4e7cb7ff3e8b8edf7aa.png)

The workflow is almost ready. The last thing to do before publishing it is configure its name. Click on **Untitled Workflow** at the top to open the **Workflow Details** modal:

![Editing details in Workflow Builder](/assets/images/13-5ae3b495064e9ef9ae9cc884d7aba4b5.png)

In the **Workflow Details** modal, edit the **Name** and **Description** of your workflow. These are what the user will see when the workflow is shared with them. When you're done, click the **Save** button:

![Editing name and description in in Workflow Builder](/assets/images/14-4911c70f6a10f80cf395f87cf4f5a86c.png)

Begin publishing your workflow by clicking the **Finish Up** button at the top:

![Publishing a workflow in Workflow Builder](/assets/images/15-961c9b5dcf990bd262365d8e775c7f35.png)

In the **Finish Up** modal, confirm your workflow's name and description, then scroll down to see **Workflow managers**. If you want to add a workflow collaborator, you can do this here. Scroll down to click **Show more permissions**. This is where you may edit your workflow's permissions:

![Confirming details in Workflow Builder](/assets/images/16-6710fac4a21088d1ed9645270eea13e4.png)

Let's leave everything as is, and finally, click **Publish**:

![Final publishing checks in Workflow Builder](/assets/images/17-2f20a38efc7070d53781c030384fca7a.png)

## Your workflow has been published!

## Run your workflow in Slack {#run-your-workflow-in-slack}

Your workflow is now ready for you to try out. Since you configured this workflow to start from a link in Slack, you'll need to copy the workflow link and then share it in any channel in your workspace.

To copy the workflow link, click the **Copy Link** button:

![Copying workflow link in Workflow Builder](/assets/images/18-94264be02fcac83660527c1d34d09756.png)

Where else can I copy the workflow link?

When you open up your workflow, hover over the first step, **Starts from a link in Slack**, and click the **Copy Link** icon that appears:

![Copying workflow link in Workflow Builder](/assets/images/21-40b2f1e9b21906a47dff440abdc88a20.png)

With the workflow link copied, leave Workflow Builder and go to Slack.

In any channel, paste the workflow link and send it in a new message. Once the message is sent, Slack will recognize it as a workflow link and it will unfurl with a button:

![An unfurled workflow link](/assets/images/19-c3c4d9542e14d6f8f86b80ce71f0d180.png)

Try out your workflow by clicking the **Start Workflow** button.

Enter `purple` for the Color input, then run the workflow by clicking the **Start Workflow** button in the modal.

You should see an ephemeral message with the appropriate return value based on how you implemented the custom function:

![Am ephemeral message from a workflow step](/assets/images/20-9b0600d06c43e1b1dcd54151e1dc3842.png)

Congratulations! You just successfully built a function, wired it up in Workflow Builder, and executed it inside Slack.

Run your workflow a few more times, trying the following inputs to see what happens:

* `purple`
* `green`
* `blue`
* `orange`

You can also update your function implementation, then re-run the workflow to see your changes propagated to Slack in realtime.

## Deploy your function {#deploy-your-function}

Your local development server is great for rapidly testing out your custom functions while building them.

When you're ready to deploy your functions in workflows that you intend to be used by people in their day-to-day jobs, you'll need to deploy your function to Slack and then swap out the local function step with the newly-deployed function step.

To do this, first go to your terminal where your local development server is running and enter `Ctrl`+`C`. This stops your server.

Next, deploy your app by running `slack deploy`. Since this is your first time _deploying_ your app, you'll go through the same steps you did when you first _installed_ your app: select **Install to a new workspace**, then select the workspace you intend to use this function as a part of a workflow in.

Once your app has finished deploying, go back into Workflow Builder and select your workflow:

![Selecting your workflow in Workflow Builder](/assets/images/22-6bb145274a2267477e9809275af6fc10.png)

To swap out the local version of your app for the deployed version of your function, you'll first create a new step that calls the deployed function, then modify the ephemeral message step to use the deployed function instead of the local one.

First, find the deployed version of your function by typing its name in the sidebar's search box. Notice how you have two options now—one for the local version, and one for the newly-deployed version. Click on the deployed version to add it into your workflow:

![Selecting a function from your deployed app in Workflow Builder](/assets/images/23-64e65603068aca4116031980c8ee051f.png)

When the modal to configure the **Input String** appears, do the same as before: click on the curly brace icon to the right of the input field, select the **Color** option from the **From a link in Slack** group, then click the **Save** button to return to the editor:

![Configuring function inputs in Workflow Builder](/assets/images/24-d42bd50e6c0c30411dafeeb1ddefa0d0.png)

You'll see two separate **Interpret Color** steps now. Delete the top one, which is the old _local_ version, by hovering over the step and clicking the **Delete** icon:

![Deleting the old function in Workflow Builder](/assets/images/25-d00428b49bf925d59bdcdfe010568d72.png)

Confirm deletion in the modal that appears:

![Confirming deletion in Workflow Builder](/assets/images/26-297175231a0dce91eb4d57874fcaca41.png)

The **Needs attention** warning is expected, since the step that provided input into the ephemeral message step was just removed.

Move the deployed **Interpret Color** function so that it is above the ephemeral message step, putting it where the deleted local function was earlier, by selecting the **Move Up** button in step controls:

![Moving the deployed function step up in Workflow Builder](/assets/images/27-7732590460b0b3bfdf51f6265bbd3a32.png)

Click on the **Edit** icon in the ephemeral message step to fix the missing data issue:

![Editing the ephemeral message step in Workflow Builder](/assets/images/28-311e35ff504b8c010ff0ae6ebb783338.png)

Delete the `Missing Data` element from the **Add a message** field:

![Removing the missing data in Workflow Builder](/assets/images/29-ad85f6c48a692da521a424db419bf9a1.png)

Then, click on the **Insert a variable** link underneath the field and select the **Result** option from the **Interpret Color** function group.

When finished, click the **Save** button:

![Saving changes in Workflow Builder](/assets/images/30-2636d42a347fa49fac487e1d080f6575.png)

## Congratulations! Your workflow is done!

All that's left to do now is **Publish changes**:

![Publishing changes in Workflow Builder](/assets/images/31-540a1f87ab63d5ae53b1e3ae1c96ce24.png)

## Onward {#onward}

In this tutorial, you built a custom function, wired it up in Workflow Builder, and fully deployed your app so that it's ready to be used in other workflows.

Here are some areas to explore now that you've come this far:

* Want to integrate with a third-party? Augment your custom function by leveraging [external authentication](/tools/deno-slack-sdk/guides/integrating-with-services-requiring-external-authentication)!

* Instead of using Workflow Builder, add your custom function as steps in [coded workflows](/tools/deno-slack-sdk/guides/creating-workflows)!

* Check out our other tutorials for more ideas about what you can do with the workflow automations!
