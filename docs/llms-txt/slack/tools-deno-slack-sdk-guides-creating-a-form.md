Source: https://docs.slack.dev/tools/deno-slack-sdk/guides/creating-a-form

# Creating a form

Workflow apps require a paid plan

Join the [Developer Program](https://api.slack.com/developer-program) and provision a sandbox with access to all Slack features for free.

Forms are a straight-forward way to collect user input and pass it onto to other parts of your workflow. Their interactivity is one way - users interact with a static form. You cannot update the form itself based on user input.

For example, say you need to collect some information from a user, send it to your system, then update a Slack channel with a link to a summary. Each task can be configured as a step in your workflow, allowing for user interactivity data to be passed to each step sequentially until the process is complete.

Forms are created with the [`OpenForm`](/tools/deno-slack-sdk/reference/slack-functions/open_form) Slack function.

✨ **If you only need to update an already-created form**, refer to the [`OpenForm`](/tools/deno-slack-sdk/reference/slack-functions/open_form) Slack function reference page.

## 1. Add interactivity to your workflow {#add-interactivity}

First let's take a look at the "Send a Greeting" workflow from the [Hello World sample app](https://github.com/slack-samples/deno-hello-world).

Making your app interactive is the key to collecting user data. To accomplish this, an [`interactivity`](/tools/deno-slack-sdk/reference/slack-types#interactivity) input parameter must be included as a property in your workflow definition. The `interactivity` parameter is required to ensure users don't experience any unexpected or unwanted forms appearing - only their interaction can open a form.

as in the following code snippet:

```python
// workflows/greeting_workflow.tsimport { DefineWorkflow, Schema } from "deno-slack-sdk/mod.ts";import { GreetingFunctionDefinition } from "../functions/greeting_function.ts";const GreetingWorkflow = DefineWorkflow({  callback_id: "greeting_workflow",  title: "Send a greeting",  description: "Send a greeting to channel",  input_parameters: {    properties: {      interactivity: {        type: Schema.slack.types.interactivity,      },      channel: {        type: Schema.slack.types.channel_id,      },    },    required: ["interactivity"],  },});
```

## 2. Add a form to your workflow {#add-form}

Now that you've added the `interactivity` property into your workflow, it's time to add the [`OpenForm`](/tools/deno-slack-sdk/reference/slack-functions/open_form) Slack function to a step in your workflow.

While some of the functions you add to your workflow will be [custom functions](/tools/deno-slack-sdk/guides/creating-custom-functions), a variety of [Slack functions](/tools/deno-slack-sdk/guides/creating-slack-functions) that cover some of the most common tasks executed on our platform are also available. The [`OpenForm`](/tools/deno-slack-sdk/reference/slack-functions/open_form) Slack function allows for the collection of user input.

### Form element schema {#element-schema}

The fields of a form are made up of different types of form elements. Form elements have several properties you can customize depending on the element type.

Links using Markdown are supported in the top-level description, but not in individual element descriptions.

Property

Type

Description

Required?

`name`

String

The internal name of the element

Required

`title`

String

Title of the form shown to the user. Maximum length is 25 characters

Required

`type`

`Schema.slack.types.*`

The [type of form element](/tools/deno-slack-sdk/guides/creating-a-form#type-parameters) to display

Required

`description`

String

Description of the form shown to the user

Optional

`default`

Same type as `type`

Default value for this field

Optional

The following parameters are available for each type when defining your form. For each parameter listed above, `type` is required.

An important distinction: some element types are prefixed with `Schema.types`, while some are prefixed with `Schema.slack.types`.

#### Form types and parameters {#type-parameters}

Type

Parameters

Notes

[`Schema.types.string`](/tools/deno-slack-sdk/reference/slack-types#string)

`title`, `description`, `default`, `minLength`, `maxLength`, `format`, `enum`, `choices`, `long`, `type`

If the `long` parameter is provided and set to `true`, it will render as a multi-line text box. Otherwise, it renders as a single-line text input field. In addition, basic input validation can be done by setting `format` to either `email` or `url`

[`Schema.types.boolean`](/tools/deno-slack-sdk/reference/slack-types#boolean)

`title`, `description`, `default`, `type`

A boolean rendered as a radio button in the form

[`Schema.types.integer`](/tools/deno-slack-sdk/reference/slack-types#integer)

`title`, `description`, `default`, `enum`, `choices`, `type`, `minimum`, `maximum`

A whole number, such as `-1`, `0`, or `31415926535`

[`Schema.types.number`](/tools/deno-slack-sdk/reference/slack-types#number)

`title`, `description`, `default`, `enum`, `choices`, `type`, `minimum`, `maximum`

A number that allows decimal points, such as `13557523.0005`

[`Schema.types.array`](/tools/deno-slack-sdk/reference/slack-types#array)

`title`, `description`, `default`, `type`, `items`, `maxItems`, `display_type`

The required `items` parameter is an object itself, which must have a `type` sub-property defined. It can accept multiple different kinds of sub-properties based on the type chosen. Can be [`Schema.types.string`](/tools/deno-slack-sdk/reference/slack-types#string), [`Schema.slack.types.channel_id`](/tools/deno-slack-sdk/reference/slack-types#channelid), [`Schema.slack.types.user_id`](/tools/deno-slack-sdk/reference/slack-types#userid). The `display_type` parameter can be used if the `items` object has the `type` parameter set to `Schema.types.string` and contains an `enum` parameter. The `display_type` parameter can be then set to `multi_static_select` (default) or `checkboxes`.

[`Schema.slack.types.date`](/tools/deno-slack-sdk/reference/slack-types#date)

`title`, `description`, `default`, `enum`, `choices`, `type`

A string containing a date, displayed in `YYYY-MM-DD` format

[`Schema.slack.types.timestamp`](/tools/deno-slack-sdk/reference/slack-types#timestamp)

`title`, `description`, `default`, `enum`, `choices`, `type`

A Unix timestamp in seconds, rendered as a [date picker](https://docs.slack.dev/reference/block-kit/block-elements/date-picker-element)

[`Schema.slack.types.user_id`](/tools/deno-slack-sdk/reference/slack-types#userid)

`title`, `description`, `default`, `enum`, `choices`, `type`

A user picker

[`Schema.slack.types.channel_id`](/tools/deno-slack-sdk/reference/slack-types#channelid)

`title`, `description`, `default`, `enum`, `choices`, `type`

A channel picker

[`Schema.slack.types.rich_text`](/tools/deno-slack-sdk/reference/slack-types#rich-text)

`title`, `description`, `default`, `type`

A way to nicely format messages in your app. Note that this type cannot be converted to other message types, such as a string

[`Schema.slack.types.file_id`](/tools/deno-slack-sdk/reference/slack-types#fileid)

`title`, `description`, `type`, `allowed_filetypes_group`, `allowed_filetypes`

Needs the [`files:read`](https://docs.slack.dev/reference/scopes/files.read) scope.

An additional example: a form element from the [Give Kudos](https://github.com/slack-samples/deno-give-kudos) sample app.

```javascript
// workflows/give_kudos.tsconst kudo = GiveKudosWorkflow.addStep(  Schema.slack.functions.OpenForm,  {    title: "Give someone kudos",    interactivity: GiveKudosWorkflow.inputs.interactivity,    submit_label: "Share",    description: "Continue the positive energy through your written word",    fields: {      elements: [{        name: "doer_of_good_deeds",        title: "Whose deeds are deemed worthy of a kudo?",        description: "Recognizing such deeds is dazzlingly desirable of you!",        type: Schema.slack.types.user_id,      }, {        name: "kudo_channel",        title: "Where should this message be shared?",        type: Schema.slack.types.channel_id,      }, {        name: "kudo_message",        title: "What would you like to say?",        type: Schema.types.string,        long: true,      }, {        name: "kudo_vibe",        title: 'What is this kudo\'s "vibe"?',        description: "What sorts of energy is given off?",        type: Schema.types.string,        enum: [          "Appreciation for someone 🫂",          "Celebrating a victory 🏆",          "Thankful for great teamwork ⚽️",          "Amazed at awesome work ☄️",          "Excited for the future 🎉",          "No vibes, just plants 🪴",        ],      }],      required: ["doer_of_good_deeds", "kudo_channel", "kudo_message"],    },  },);
```

Add the [`OpenForm`](/tools/deno-slack-sdk/reference/slack-functions/open_form) Slack function as a step in your workflow:

```javascript
// workflows/greeting_workflow.tsconst inputForm = GreetingWorkflow.addStep(  Schema.slack.functions.OpenForm,  {    title: "Send a greeting",    interactivity: GreetingWorkflow.inputs.interactivity,    submit_label: "Send greeting",    fields: {      elements: [{        name: "recipient",        title: "Recipient",        type: Schema.slack.types.user_id,      }, {        name: "channel",        title: "Channel to send message to",        type: Schema.slack.types.channel_id,        default: GreetingWorkflow.inputs.channel,      }, {        name: "message",        title: "Message to recipient",        type: Schema.types.string,        long: true,      }],      required: ["recipient", "channel", "message"],    },  },);
```

Forms have two output parameters:

* `fields`: The same field names in the inputs, which are returned as outputs with the values entered by the user
* `interactivity`: The context about the form submit action interactive event

Use these output parameters to pass the information you collected from the user to subsequent steps in a workflow. When using the [`OpenForm`](/tools/deno-slack-sdk/reference/slack-functions/open_form) Slack function, either add it as the first step in your workflow or ensure the preceding step is interactive, as an interactive step will generate a fresh pointer to use for opening the form. For example, use the interactive button in a later step in your workflow, which can be added with the [`Send a message`](/tools/deno-slack-sdk/reference/slack-functions/send_message) Slack function immediately before opening the form.

It is important to validate the inputs you receive from the user: first, that the user is authorized to pass the input, and second, that the user is passing a value you expect to receive and nothing more.

The example below passes the user's input data into the second step of the workflow, a [custom function](/tools/deno-slack-sdk/guides/creating-custom-functions), by using the output parameter `fields` and selecting the desired output element by name (i.e. `recipient` and `message`)

```javascript
// workflows/greeting_workflow.tsconst greetingFunctionStep = GreetingWorkflow.addStep(  GreetingFunctionDefinition,  {    recipient: inputForm.outputs.fields.recipient,    message: inputForm.outputs.fields.message,  },);
```

User input data can also be passed to [Slack functions](/tools/deno-slack-sdk/guides/creating-slack-functions). This example sends the user's message to a specific channel specified by the user.

```text
// workflows/greeting_workflow.tsGreetingWorkflow.addStep(Schema.slack.functions.SendMessage, {  channel_id: inputForm.outputs.fields.channel,  message: greetingFunctionStep.outputs.greeting,});export default GreetingWorkflow;
```

Take note of the `title`, `description`, and `submit_label` fields. It is important be descriptive with these fields, as these are the first things the user will see once the workflow is started and your form is displayed to them:

![form-metadata](data:image/png;base64,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 "Sample form metadata")

## 3. Add your workflow to your manifest {#manifest-workflow}

With a workflow defined and steps outlined, it's time to make this an official part of your app! Add the workflow definition to your manifest as in the following example:

```python
// manifest.tsimport { Manifest } from "deno-slack-sdk/mod.ts";import GreetingWorkflow from "./workflows/greeting_workflow.ts";export default Manifest({  name: "deno-hello-world",  description:    "A sample that demonstrates using a function, workflow and trigger to send a greeting",  icon: "assets/default_new_app_icon.png",  workflows: [GreetingWorkflow],  outgoingDomains: [],  botScopes: ["commands", "chat:write", "chat:write.public"],});
```

✨ **To learn more about workflows**, check out the [workflows](/tools/deno-slack-sdk/guides/creating-workflows) page.

## 4. Add a trigger to kick off your workflow {#add-trigger}

Let's add the needed momentum to your workflow and create a [link trigger](/tools/deno-slack-sdk/guides/creating-link-triggers#create-cli__create-a-link-trigger-with-a-trigger-file).

In the trigger definition, add `interactivity` as an input value. This value holds context about the user interactivity that invoked this trigger, and passes it along to your workflow.

In a separate file, define your trigger in the following way:

```python
// triggers/greeting_trigger.tsimport { Trigger } from "deno-slack-sdk/types.ts";import { TriggerContextData, TriggerTypes } from "deno-slack-api/mod.ts";import GreetingWorkflow from "../workflows/greeting_workflow.ts";const greetingTrigger: Trigger<typeof GreetingWorkflow.definition> = {  type: TriggerTypes.Shortcut,  name: "Send a greeting",  description: "Send greeting to channel",  workflow: `#/workflows/${GreetingWorkflow.definition.callback_id}`,  inputs: {    interactivity: {      value: TriggerContextData.Shortcut.interactivity,    },    channel: {      value: TriggerContextData.Shortcut.channel_id,    },  },};export default greetingTrigger;
```

Run the following CLI command to create the link trigger:

```python
slack trigger create --trigger-def triggers/greeting_trigger.ts...⚡ Trigger created   Trigger ID:   Ft0123ABC456   Trigger Type: shortcut   Trigger Name: Send a greeting   URL: https://slack.com/shortcuts/Ft0123ABC456/c001a02b13c42de35f47b55a89aad33c
```

You now have a shortcut `URL` to share in a channel or save as a bookmark, which allows you to kick off your workflow and open your form.

✨ **To learn more about starting workflows with triggers**, head to the [triggers overview](/tools/deno-slack-sdk/guides/using-triggers) page.
