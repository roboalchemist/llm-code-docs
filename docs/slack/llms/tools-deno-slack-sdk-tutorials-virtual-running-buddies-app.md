Source: https://docs.slack.dev/tools/deno-slack-sdk/tutorials/virtual-running-buddies-app

# Virtual running buddies app

Workflow apps require a paid plan

Join the [Developer Program](https://api.slack.com/developer-program) and provision a sandbox with access to all Slack features for free.

In this tutorial, you'll learn how to create a social app to log runs with your virtual running buddies.

We'll pace you along the path to design a [datastore](/tools/deno-slack-sdk/guides/using-datastores), craft a [custom type](/tools/deno-slack-sdk/guides/creating-a-custom-type), tailor [triggers](/tools/deno-slack-sdk/guides/using-triggers), wire [workflows](/tools/deno-slack-sdk/guides/creating-workflows), and form [functions](/tools/deno-slack-sdk/guides/creating-slack-functions). Now that you're familiar with the course map, let's head to the start line.

✨ **First time creating a workflow app?** Try a basic app to build your confidence, such as [Hello World](/tools/deno-slack-sdk/tutorials/hello-world-app)!

Before we begin, ensure you have the following prerequisites completed:

* Install the Slack CLI.
* Run `slack auth list` and ensure your workspace is listed.
* If your workspace is not listed, address any issues by following along with the Getting started, then come on back.

* * *

## Step 1: Create an app to complete your warmup {#warmup}

Each Slack app built using the CLI begins with the same steps. Make sure you have everything you need before you show up at the start line.

After you've [installed the command-line interface](/tools/deno-slack-sdk/guides/getting-started), you have two ways you can get started.

* Use a blank app
* Use a pre-built app

You can create a blank app with the Slack CLI using the following command:

```text
slack create virtual-running-buddies-app --template https://github.com/slack-samples/deno-blank-template
```

Or, you can use the pre-built [Virtual Running Buddies app](https://github.com/slack-samples/deno-virtual-running-buddies):

```text
slack create virtual-running-buddies-app --template https://github.com/slack-samples/deno-virtual-running-buddies
```

Once you have your new project ready to go, change into your project directory and get to the start line.

* * *

## Step 2: Map your course with your manifest {#map-course}

Determining the definitions and manifest of your app allows you to create a course map of where you want to go. Open your text editor (we recommend VSCode with the [Deno plugin](https://marketplace.visualstudio.com/items?itemName=denoland.vscode-deno)) and point to the directory you created with the `slack` command.

Import and add the following definitions to your [app's manifest](/tools/deno-slack-sdk/guides/using-the-app-manifest):

```python
import { Manifest } from "deno-slack-sdk/mod.ts";import RunningDatastore from "./datastores/run_data.ts";import LogRunWorkflow from "./workflows/log_run_workflow.ts";import DisplayLeaderboardWorkflow from "./workflows/display_leaderboard_workflow.ts";import { RunnerStatsType } from "./types/runner_stats.ts";export default Manifest({  name: "my-run-app",  description: "Log runs with virtual running buddies!",  icon: "assets/icon.png",  workflows: [LogRunWorkflow, DisplayLeaderboardWorkflow],  outgoingDomains: [],  datastores: [RunningDatastore],  types: [RunnerStatsType],  botScopes: [    "commands",    "chat:write",    "chat:write.public",    "datastore:read",    "datastore:write",    "channels:read",    "triggers:write",  ],});
```

You'll notice a lot of stuff we haven't talked about yet, but not to worry! We'll cover everything in the following steps.

* * *

## Step 3: Define a datastore {#datastore}

We need a way to store all the information that our running buddies log, including their user ID (`runner`), how long they ran (`distance`), and the date they ran (`rundate`). Enter [datastores](/tools/deno-slack-sdk/guides/using-datastores)!

Datastores have three main properties:

* `name`: to identify your datastore.
* `primary_key`: the attribute to be used as the datastore's primary key (ensure this is an actual attribute that you have defined), which we'll use for querying information later. For more information, refer to [querying the datastore](/tools/deno-slack-sdk/guides/retrieving-items-from-a-datastore).
* `attributes`: to scaffold your datastore's columns.

For what we need, the following datastore will do the trick. Let's create a `datastores` folder and add a file called `run_data.ts` with our datastore definition:

```python
import { DefineDatastore, Schema } from "deno-slack-sdk/mod.ts";export const RUN_DATASTORE = "running_datastore";const RunningDatastore = DefineDatastore({  name: RUN_DATASTORE,  primary_key: "id",  attributes: {    id: {      type: Schema.types.string,    },    runner: {      type: Schema.slack.types.user_id,    },    distance: {      type: Schema.types.number,    },    rundate: {      type: Schema.slack.types.date,    },  },});export default RunningDatastore;
```

We already did this earlier when we defined our manifest — but if you hadn't yet, you would need to import your datastore within the manifest file:

`import RunningDatastore from "./datastores/run_data.ts";`

And then, register it:

`datastores: [RunningDatastore],`

Additionally, for any datastore, you'll need to add the following bot scopes to your manifest:

* `datastore:read`
* `datastore:write`

* * *

## Step 4: Craft a custom type {#custom-type}

The next thing we'll do is define a custom type for our runners' recent runs. Since we're going to be passing this information to our datastore, workflows, and functions, having our own custom reusable type will make our lives a little easier.

✨ **For more information about custom types and how to define them**, refer to [custom types](/tools/deno-slack-sdk/guides/creating-a-custom-type).

We'll create a new `types` folder with a file called `runner_stats.ts` with our custom type definition:

```python
import { DefineType, Schema } from "deno-slack-sdk/mod.ts";export const RunnerStatsType = DefineType({  title: "Runner Stats",  description: "Information about the recent runs for a runner",  name: "runner_stats",  type: Schema.types.object,  properties: {    runner: { type: Schema.slack.types.user_id },    weekly_distance: { type: Schema.types.number },    total_distance: { type: Schema.types.number },  },  required: ["runner", "weekly_distance", "total_distance"],});
```

Just like with our datastore, we'll also verify that we imported our custom type into our manifest earlier:

`import { RunnerStatsType } from "./types/runner_stats.ts";`

And then, make sure it's registered:

`types: [RunnerStatsType],`

* * *

## Step 5: Wire your workflows {#workflows}

Next, let's define our workflows — we'll have two of them. Don't worry about functions yet; we'll get to those next. For now, you can just import and call them as shown in our workflows.

For our first workflow, we need three steps to accomplish the following:

1. Allow a runner on our team to log their run details. The Slack function [`OpenForm`](/tools/deno-slack-sdk/reference/slack-functions/open_form) is used to collect data.
2. Save those details to the datastore we defined earlier.
3. Post a message of encouragement to the runner. Every runner loves a good cheering section!

Let's create a `workflows` folder and add a file called `log_run_workflow.ts` with the following workflow definition:

```python
import { DefineWorkflow, Schema } from "deno-slack-sdk/mod.ts";import { LogRunFunction } from "../functions/log_run.ts";const LogRunWorkflow = DefineWorkflow({  callback_id: "log_run_workflow",  title: "Log a run",  description: "Collect and store info about a recent run",  input_parameters: {    properties: {      interactivity: { type: Schema.slack.types.interactivity },      channel: { type: Schema.slack.types.channel_id },      user_id: { type: Schema.slack.types.user_id },    },    required: ["interactivity", "channel", "user_id"],  },});// Step 1: Collect run information with a formconst inputForm = LogRunWorkflow.addStep(  Schema.slack.functions.OpenForm,  {    title: "Log your run",    interactivity: LogRunWorkflow.inputs.interactivity,    submit_label: "Submit run",    fields: {      elements: [{        name: "runner",        title: "Runner",        type: Schema.slack.types.user_id,        default: LogRunWorkflow.inputs.user_id,      }, {        name: "distance",        title: "Distance (in miles)",        type: Schema.types.number,        minimum: 0,      }, {        name: "rundate",        title: "Run date",        type: Schema.slack.types.date,        default: new Date().toISOString().split("T")[0], // YYYY-MM-DD      }, {        name: "channel",        title: "Channel to send entry to",        type: Schema.slack.types.channel_id,        default: LogRunWorkflow.inputs.channel,      }],      required: ["channel", "runner", "distance", "rundate"],    },  },);// Step 2: Save run info to the datastoreLogRunWorkflow.addStep(LogRunFunction, {  runner: inputForm.outputs.fields.runner,  distance: inputForm.outputs.fields.distance,  rundate: inputForm.outputs.fields.rundate,});// Step 3: Post a message about the runLogRunWorkflow.addStep(Schema.slack.functions.SendMessage, {  channel_id: inputForm.outputs.fields.channel,  message:    `:athletic_shoe: <@${inputForm.outputs.fields.runner}> submitted ${inputForm.outputs.fields.distance} mile(s) on ${inputForm.outputs.fields.rundate}. Keep up the great work!`,});export default LogRunWorkflow;
```

* * *

For our second workflow, we need to generate our leaderboard. To do this, our workflow contains the following steps:

1. Gather our team's runs.
2. Gather each individual's runs.
3. Format our leaderboard.
4. Post the leaderboard to our channel.

```python
import { DefineWorkflow, Schema } from "deno-slack-sdk/mod.ts";import { CollectTeamStatsFunction } from "../functions/collect_team_stats.ts";import { CollectRunnerStatsFunction } from "../functions/collect_runner_stats.ts";import { FormatLeaderboardFunction } from "../functions/format_leaderboard.ts";const DisplayLeaderboardWorkflow = DefineWorkflow({  callback_id: "display_leaderboard_workflow",  title: "Display the leaderboard",  description:    "Show team statistics and highlight the top runners from the past week",  input_parameters: {    properties: {      channel: { type: Schema.slack.types.channel_id },      interactivity: { type: Schema.slack.types.interactivity },    },    required: ["channel", "interactivity"],  },});// Step 1: Gather team stats from the past weekconst teamStats = DisplayLeaderboardWorkflow.addStep(  CollectTeamStatsFunction,  {},);// Step 2: Collect individual runner statsconst runnerStats = DisplayLeaderboardWorkflow.addStep(  CollectRunnerStatsFunction,  {},);// Step 3: Format the leaderboard messageconst leaderboard = DisplayLeaderboardWorkflow.addStep(  FormatLeaderboardFunction,  {    team_distance: teamStats.outputs.weekly_distance,    percent_change: teamStats.outputs.percent_change,    runner_stats: runnerStats.outputs.runner_stats,  },);// Step 4: Post the leaderboard message to channelDisplayLeaderboardWorkflow.addStep(Schema.slack.functions.SendMessage, {  channel_id: DisplayLeaderboardWorkflow.inputs.channel,  message:    `${leaderboard.outputs.teamStatsFormatted}\n\n${leaderboard.outputs.runnerStatsFormatted}`,});export default DisplayLeaderboardWorkflow;
```

Our workflows also need to be imported into our manifest, so let's just double-check the following lines are there: `import LogRunWorkflow from "./workflows/log_run_workflow.ts";` `import DisplayLeaderboardWorkflow from "./workflows/display_leaderboard_workflow.ts";`

And that they are registered:

`workflows: [LogRunWorkflow, DisplayLeaderboardWorkflow],`

* * *

## Step 6: Form your functions {#functions}

Following fast, functions: we'll fashion four.

The first function will store our collected run data in our datastore (so don't forget to import it first):

```python
import { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";import { RUN_DATASTORE } from "../datastores/run_data.ts";export const LogRunFunction = DefineFunction({  callback_id: "log_run",  title: "Log a run",  description: "Record a run in the datastore",  source_file: "functions/log_run.ts",  input_parameters: {    properties: {      runner: {        type: Schema.slack.types.user_id,        description: "Runner",      },      distance: {        type: Schema.types.number,        description: "Distance",      },      rundate: {        type: Schema.slack.types.date,        description: "Run date",      },    },    required: ["runner", "distance", "rundate"],  },  output_parameters: {    properties: {},    required: [],  },});export default SlackFunction(LogRunFunction, async ({ inputs, client }) => {  const { distance, rundate, runner } = inputs;  const uuid = crypto.randomUUID();  const putResponse = await client.apps.datastore.put({    datastore: RUN_DATASTORE,    item: {      id: uuid,      runner: runner,      distance: distance,      rundate: rundate,    },  });  if (!putResponse.ok) {    return { error: `Failed to store run: ${putResponse.error}` };  }  return { outputs: {} };});
```

✨ **For more information about how data is stored and successful vs. unsuccessful payloads**, refer to [creating or updating an item](/tools/deno-slack-sdk/guides/adding-items-to-a-datastore).

* * *

Our second function calculates weekly and all-time total distance statistics for an individual runner.

We'll query the datastore to get a runner's logged run details, calculate some statistics for that runner, and then return an array containing all of that information:

```python
import { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";import RunningDatastore, { RUN_DATASTORE } from "../datastores/run_data.ts";import { RunnerStatsType } from "../types/runner_stats.ts";export const CollectRunnerStatsFunction = DefineFunction({  callback_id: "collect_runner_stats",  title: "Collect runner stats",  description: "Gather statistics of past runs for all runners",  source_file: "functions/collect_runner_stats.ts",  input_parameters: {    properties: {},    required: [],  },  output_parameters: {    properties: {      runner_stats: {        type: Schema.types.array,        items: { type: RunnerStatsType },        description: "Weekly and all-time total distances for runners",      },    },    required: ["runner_stats"],  },});export default SlackFunction(CollectRunnerStatsFunction, async ({ client }) => {  // Query the datastore for all the data we collected  const runs = await client.apps.datastore.query<    typeof RunningDatastore.definition  >({ datastore: RUN_DATASTORE });  if (!runs.ok) {    return { error: `Failed to retrieve past runs: ${runs.error}` };  }  const runners = new Map<typeof Schema.slack.types.user_id, {    runner: typeof Schema.slack.types.user_id;    total_distance: number;    weekly_distance: number;  }>();  const startOfLastWeek = new Date();  startOfLastWeek.setDate(startOfLastWeek.getDate() - 6);  // Add run statistics to the associated runner  runs.items.forEach((run) => {    const isRecentRun = run.rundate >=      startOfLastWeek.toLocaleDateString("en-CA", { timeZone: "UTC" });    // Find existing runner record or create new one    const runner = runners.get(run.runner) ||      { runner: run.runner, total_distance: 0, weekly_distance: 0 };    // Add run distance to the runner's totals    runners.set(run.runner, {      runner: run.runner,      total_distance: runner.total_distance + run.distance,      weekly_distance: runner.weekly_distance + (isRecentRun && run.distance),    });  });  // Return an array with runner stats  return {    outputs: { runner_stats: [...runners.entries()].map((r) => r[1]) },  };});
```

✨ **For more information about how data is retrieved and successful vs. unsuccessful payloads**, refer to [retrieving a single item](/tools/deno-slack-sdk/guides/retrieving-items-from-a-datastore#get) and [querying the datastore](/tools/deno-slack-sdk/guides/retrieving-items-from-a-datastore#query).

* * *

Our third function calculates the weekly and all-time total distance for the whole team, as well as the percentage difference between this week's runs and the previous week's runs.

Similar to the query for individual runners, we'll query the datastore to get the team's logged run details, calculate statistics for the team, and then return all of that information:

```python
import { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";import { SlackAPIClient } from "deno-slack-api/types.ts";import RunningDatastore, { RUN_DATASTORE } from "../datastores/run_data.ts";export const CollectTeamStatsFunction = DefineFunction({  callback_id: "collect_team_stats",  title: "Collect team stats",  description: "Gather and compare run data from the last week",  source_file: "functions/collect_team_stats.ts",  input_parameters: {    properties: {},    required: [],  },  output_parameters: {    properties: {      weekly_distance: {        type: Schema.types.number,        description: "Total number of miles ran last week",      },      percent_change: {        type: Schema.types.number,        description: "Percent change of miles ran compared to the prior week",      },    },    required: ["weekly_distance", "percent_change"],  },});export default SlackFunction(CollectTeamStatsFunction, async ({ client }) => {  const today = new Date();  // Collect runs from the past week (days 0-6)  const lastWeekStartDate = new Date(new Date().setDate(today.getDate() - 6));  const lastWeekDistance = await distanceInWeek(client, lastWeekStartDate);  if (lastWeekDistance.error) {    return { error: lastWeekDistance.error };  }  // Collect runs from the prior week (days 7-13)  const priorWeekStartDate = new Date(new Date().setDate(today.getDate() - 13));  const priorWeekDistance = await distanceInWeek(client, priorWeekStartDate);  if (priorWeekDistance.error) {    return { error: priorWeekDistance.error };  }  // Calculate percent difference between totals of last week and the prior week  const weeklyDiff = lastWeekDistance.total - priorWeekDistance.total;  let percentageDiff = 0;  if (priorWeekDistance.total != 0) {    percentageDiff = 100 * weeklyDiff / priorWeekDistance.total;  }  return {    outputs: {      weekly_distance: Number(lastWeekDistance.total.toFixed(2)),      percent_change: Number(percentageDiff.toFixed(2)),    },  };});// Sum all logged runs in the seven days following startDateasync function distanceInWeek(  client: SlackAPIClient,  startDate: Date,): Promise<{ total: number; error?: string }> {  const endDate = new Date(startDate);  endDate.setDate(endDate.getDate() + 6);  const runs = await client.apps.datastore.query<    typeof RunningDatastore.definition  >({    datastore: RUN_DATASTORE,    expression: "#date BETWEEN :start_date AND :end_date",    expression_attributes: { "#date": "rundate" },    expression_values: {      ":start_date": startDate.toLocaleDateString("en-CA", { timeZone: "UTC" }),      ":end_date": endDate.toLocaleDateString("en-CA", { timeZone: "UTC" }),    },  });  if (!runs.ok) {    return { total: 0, error: `Failed to retrieve past runs: ${runs.error}` };  }  const total = runs.items.reduce((sum, entry) => (sum + entry.distance), 0);  return { total };}
```

* * *

Our final function generates our ordered leaderboard, as well as a formatted message with all of our queried data and calculated statistics:

```python
import { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";import { RunnerStatsType } from "../types/runner_stats.ts";export const FormatLeaderboardFunction = DefineFunction({  callback_id: "format_leaderboard",  title: "Format leaderboard message",  description: "Format team and runner stats for a sharable message",  source_file: "functions/format_leaderboard.ts",  input_parameters: {    properties: {      team_distance: {        type: Schema.types.number,        description: "Total number of miles ran last week for the team",      },      percent_change: {        type: Schema.types.number,        description:          "Percent change of miles ran compared to the prior week for the team",      },      runner_stats: {        type: Schema.types.array,        items: { type: RunnerStatsType },        description: "Weekly and all-time total distances for runners",      },    },    required: ["team_distance", "percent_change", "runner_stats"],  },  output_parameters: {    properties: {      teamStatsFormatted: {        type: Schema.types.string,        description: "A formatted message with team stats",      },      runnerStatsFormatted: {        type: Schema.types.string,        description: "An ordered leaderboard of runner stats",      },    },    required: ["teamStatsFormatted", "runnerStatsFormatted"],  },});export default SlackFunction(FormatLeaderboardFunction, ({ inputs }) => {  const teamStatsFormatted =    `Your team ran *${inputs.team_distance} miles* this past week: a ${inputs.percent_change}% difference from the prior week.`;  const runnerStatsFormatted = inputs.runner_stats.sort((a, b) =>    b.weekly_distance - a.weekly_distance  ).map((runner) =>    ` - <@${runner.runner}> ran ${runner.weekly_distance} miles last week (${runner.total_distance} total)`  ).join("\n");  return {    outputs: { teamStatsFormatted, runnerStatsFormatted },  };});
```

Whew! Don't slow down now...we're almost there!

* * *

## Step 7: Tailor your triggers {#triggers}

Triggers invoke workflows. There are four types of available triggers, but we'll only be using two: [link triggers](/tools/deno-slack-sdk/guides/creating-link-triggers) and [scheduled triggers](/tools/deno-slack-sdk/guides/creating-scheduled-triggers). For this app, we'll need three triggers, two of which will be link triggers. This means that they require a user to manually trigger them.

First, we'll create a `triggers` folder and define a link trigger for collecting our team's runs called `log_run_trigger.ts`:

```python
import { Trigger } from "deno-slack-api/types.ts";import LogRunWorkflow from "../workflows/log_run_workflow.ts";const LogRunTrigger: Trigger<typeof LogRunWorkflow.definition> = {  type: "shortcut",  name: "Log a run",  description: "Save the details of a recent run",  workflow: `#/workflows/${LogRunWorkflow.definition.callback_id}`,  inputs: {    interactivity: {      value: "{{data.interactivity}}",    },    channel: {      value: "{{data.channel_id}}",    },    user_id: {      value: "{{data.user_id}}",    },  },};export default LogRunTrigger;
```

Run the `trigger create` command in terminal:

```python
slack trigger create --trigger-def triggers/log_run_trigger.ts
```

After executing this command, select your app and workspace. Once completed, you'll be given a link called "Shortcut URL." This is your link trigger for this workflow on this workspace.

Save that URL for when you start testing, since that's how you'll invoke this particular trigger. You can also use the `slack triggers -info` command and select your workspace to grab that URL again later, or click the `/` icon within Slack to open the `Run workflow` menu and select your trigger.

* * *

Second, we'll need a trigger to display our leaderboard. Create another link trigger in that same `triggers` folder called `display_leaderboard_trigger.ts` and define it as follows:

```python
import { Trigger } from "deno-slack-api/types.ts";import DisplayLeaderboardWorkflow from "../workflows/display_leaderboard_workflow.ts";const DisplayLeaderboardTrigger: Trigger<  typeof DisplayLeaderboardWorkflow.definition> = {  type: "shortcut",  name: "Display the leaderboard",  description: "Show stats for the team and individual runners",  workflow: `#/workflows/${DisplayLeaderboardWorkflow.definition.callback_id}`,  inputs: {    interactivity: {      value: "{{data.interactivity}}",    },    channel: {      value: "{{data.channel_id}}",    },  },};export default DisplayLeaderboardTrigger;
```

Run the `trigger create` command in the terminal again and save the Shortcut URL for our second link trigger:

```python
slack trigger create --trigger-def triggers/display_leaderboard_trigger.ts
```

* * *

Finally, we'll create a scheduled trigger in our `triggers` folder to post a message to a channel with our stats on a weekly basis. We'll call this one `display_weekly_stats.ts`:

```python
import { Trigger } from "deno-slack-api/types.ts";import DisplayLeaderboardWorkflow from "../workflows/display_leaderboard_workflow.ts";const DisplayWeeklyStats: Trigger<  typeof DisplayLeaderboardWorkflow.definition> = {  type: "scheduled",  name: "Display weekly stats",  description: "Display weekly running stats on a schedule",  workflow: `#/workflows/${DisplayLeaderboardWorkflow.definition.callback_id}`,  inputs: {    interactivity: {      value: "{{data.interactivity}}",    },    channel: {      value: "{{data.channel_id}}",    },  },  schedule: {    start_time: new Date(new Date().getTime() + 60000).toISOString(),    timezone: "EDT",    frequency: {      type: "weekly",      on_days: ["Thursday"],      repeats_every: 1,    },  },};export default DisplayWeeklyStats;
```

Since this is a scheduled trigger, we won't have a Shortcut URL for this one since there's nothing to invoke manually. Use the following command to create the [scheduled trigger](/tools/deno-slack-sdk/guides/creating-event-triggers):

`slack trigger create --trigger-def triggers/display_weekly_stats.ts`

Make sure that the app has the `triggers:write` scope added to the manifest!

* * *

## Step 8: Cross the finish line {#finish}

You're almost to the finish line! Let's use development mode to run this workflow in Slack directly from the machine you're reading this from now:

```text
slack run
```

After you've chosen your app and assigned it to your workspace, you can switch over to the app in Slack and give it a spin. Use the link triggers you created previously; when you paste the Shortcut URLs into the box and post them as messages, they'll unfurl and give you buttons for invoking our workflows.

Here is an example of the message displayed after logging a run:

![Log a run](data:image/png;base64,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)

Here is an example of a message displayed after generating the leaderboard:

![Display leaderboard](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnQAAAB5CAMAAACHtkwKAAAAb1BMVEX///8uLS766bT6+vri4uLQ0NBvb2/xyf7o9foeHR708vRiYWKbm5s7OjsthuT22tp8fHzBwcFIR0hWVVaSkpLs7O21tbaIh4fS2+GkpKQfdd2sq6zjqDwZZaVblsaLueE5fbOlyOZ8qs7Tr2fYv4703bsWAAAACXBIWXMAAAsTAAALEwEAmpwYAAAZeklEQVR42u2d63arOrOmH5DEGRt8ij2z+vt67+77v6Q9xu4eMycnsRNjzJn+AXbsxJnnlTXXar0/ohiBJEShUpX0FqChoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhofHbwTj+Iai/ePLX8v98eMU7GVaqn+XfBuL4/7r98sltK9o/szGRmwFIIZrXwmZME4B3q68b/Sz/NjC/4RznP5wPaUucd62JZPg6yxaZflb/SKE7qzudf//Lerj44im/CgXvCvezzKdHcwIDCMNwAkYYGvop/pNGOuH8+1/Wah2z+pD5WvN+PbU40qwTywKKYls6+MXWCk7PlYvjBOJgIV8SgHgGcDnvzxNaDD4W8v2sub1iRWzyEK/mN68zC7W1DNVUZT40KsNcEpn2NQBjVMlzyFMdWM06Es3Wtp7L/rrLtansayLxPEpVu5oX6nFQiE0N2Jn3gGfVqgVQhm1Z17GRtymR6absXt6FUo0eIboVdk7wUDB6PGqZMh6OErisEs/00j4BEFumS1h6nTJ/1lLwewidmNqrNCU2mxVgYjOc/hfOi4n4IHesHFlljkjbnSOQOf3TS8kcGewAufMoc0pRVd3jZvFI6uxmd2UunzMH+SB38tGpwjVQUoOzgwqIM9Sjc7FpCVOZ84yyt/u6l+NNZ8SWZmdcqGOZ87fGSwLkRnl38bhPAAZWnxevQFVaCH4H9Srm//bTFfE4Xj30Cm/FJvv0afS/jjVRZcrKNQVNOsQiwqwuJ5PJHAjC42m/Z1Y4tpxMJgvuRkFbswW8ws2IgLAdkAvARxLvqDY2YDB4nPCc16xx8Kr2RfUa4X0uDNiOi7plFZnl8UyzKdqj5EJxv4TVeJ8AWI/BGmC79cDfaiH4y4XujMTxEDP/TwBGxw6U2qKpFXgJO9VgkW232wYI7sqj8zZ1CcrYbrc59U21CLGBTZ2OeAYeeXxxF1rIEgnejnRUw9SnFDaC+sXIGGa+jw22aSWAipr749lfepy0LUAc3xwlctXceAqIxjGxXWoh+EvVqxhtGytNo8JtVq9E024BjPMz/cpuBqlc0Yzg9p3hM7KgRDnZ+j0btT5yGuYWjULxnIZOuMkKvPbQ0t0gI29B3gLEyy/d3h2AajdHCdNyLV15DzxVcrvRMvDXjnQDQRaNC2G9kjkaVnlnOJ4vxSKlhdXnz5/7KVLyarGD5efPn+9wKtH6exF/ZNA54Tqnr80Kk8qjglpS3t42TYrNjmFNidVfNqLdbPL9mGt//RaVX6QvCeIBx9nspkAamZae0v3V6vXBp6hntdEfPfgi2niEDTy8U8rKJTtdElAZ7jh/c2JCe9FNooQ/dDIDcK2aQQ3cYVOBGOeAixj5SSZYU7GFCfsh6TG/hzZ/zG8BHh6+LHAeyledzKlO4w68+yRJXAPgwXK1CPy1QidsVqJGGKuHY4kD1mZDDiT37xTTMDxd/EynWVX4b877lDV3826tK91JuQSUwL4HKLNKLsOsakcZ3I3krpFuTWXilvBM9I13FAUqmu0Tw55aZer7l30CWAbA0xqgTpZaBPhLF/yFEdrP6f+sn4Ag4fAXiLcOYP+f9rw28nbO8LUnj+m5BypGSwC/qQsvBSUprby3Pi+eB7dHl3m8yPE0kWn9Awv+otaP+Dc3JOLqIUrb/Zys/xskwGraqcp3pu1e672ROc6eWndHnZSDSKUvw2V1fNmxGFW09etjp7bMe8aJxm8+p9smrMRtp1j7PwFJEJzdB3U6V3/6vmqF36neyPetFymt1u+dv6r0LpJ/5khX04b2c4ogSEgIkqOJXTfQjd9ZMrr+3mrvzo6GX3CZldqdxj9yPx3NqHkapJNGdWo1KIqigKIgCJpu9i30s9f4xWuv25KVSBXBYVYXJBAkNEcTPQ2NXzinqxkHE/sGkSQkQZAEBEnwMqm391pWQ+PXOYfzmgcfRRAksJe5IIFhb97qDtP45Qv+24SVSOnGuYQkIAmSoB/hnnR3afxyQ4JWxWJQP4emAisJsEgCiiJIbADLTupWd5nGLx7p8poHv1YcL0cEQb8E1f5WzlZPgHx/47PwfvXr6f3pt/Mxw8wvr+i7e+ZVC8wmY2dYHdPQIik6OyKxABorPXhMIicDmDnBu4sEwvypYVEMlZ8BTF0p33pqZOHXrhnszj7AEvx077f2v4FI5n3dFeR/gVk7IzR7Cz/2h93LOjGaw/3H/jDBH3ie53lOFvuek4FQg6OWyWhrRTtQ7sBohrn//b6pC9ssv+E2vfZrI4cV7b6rYj/9uZGus1+Xe1ncL0bIfofIi/G6zWeAt6zfXzEX859686O8Ut1+lfTsGpfzrgNnLk43tnwd8597+y83riylApBr2S0IzrbW4eF2Bw3DMIw6TabrZ7WWMFFndidKGTyn7pP8fsbl4q71/tzb/NN2Dh/r18Njszvj1TlabS/rnQCL4v2ig59plxSp7NeDk7MPoCon772xJ36dsv0GKttPeoKexf1dIUeAGHi3XfuX/qHe/mByf39/n3plNSpvvAvi9LWMFA9wkd2WtKr8/nnMg1otf81tFg8fakiA2cjioF8BklDaZQMQ/l9796IwR+vpdr6dPXKZi/kGgmgLk2Abx9lguAVvcp+5bUPsNLME5j4jL2WRT0q3llL0mqU7+5A5bPYZs9K3cnsL47YZVkanNxaF6VpBaHm10QiHTKF2yIFvBhli7Hp+3gKqzAKrVqWclrMEz68aLnMx3gLIaearUVuyP3SZi/G2u6KFRZjs78TOWBRikIE3rMKqwSpBzPztPO/0aN9ogLZsISwzGFZN2c0NzBdbf38QkHLX1NaOQZvvmsOm5VkpTNPeXrZFvC0DyzI9EW376vv+7H7IaTs0Rm0JsdO4dbvvXWAhLDHdRNWioZFTRnmDnHqhqo1xd8W+Y2RjDppBBvv7A+KxE2IXyIE5NNSsLSB2mphyX/35nunTfc/8sNC1yu/s1xZIPCV3om6sBuA5PDZe08UTSt3iF8K+90vCKgOnyiT21kohopaByILN0Knqen7rl0a7o1Vby3CcsCqNptPb9tYaHDIlZp+RFNsgt7ewKRp3L3SyKVSa2QZ1sDNNa6dQu/kmr/zdaDvc1btkmAETtYutVIkAsY3Stm2bSTryN1EKiDJ0nK29wxKhkYZZl+OqXWylLYQ3ovWapkDWWePDaDfdTBsxbLfzxCpBqbS067YF9ncE0LQw3Xpb4jywDVnC7GEQ7jfsHA4CMkgwnEGQ5YF30PuTpJ2K0t7mZumqXWxZpemIpK++68/+hyhdKe6tkqD0w41T9L0LMNwJhySXZjbOVRoXjdGIUu4ypxH2vVVy6BiZR6VZGg19mQDy0WnVU5SJtm7KLDdLgtK3clOW+8d5rmf2Jex75ieGvmmspvzrf3z69K//+Pfg06dPg/+c/e8//vjjjz9ieaoPRiN3TuxKUG7MOAJGEYG79yC7lzDt/kg8iF2J78PCjcHoggZ0Z+8zxxwygAt31lfkevtYJzNiNxSMXCncEZ47wncVjEaExuH9mYRAYHhgjZCu6trWmRVuDHM3xgPG1j5n0sexmLoxs7GhWITMXAlxSBQKuLAIDKKRB2q23+7X3fx+Nj0GEbrRZGRMkW54cWF03LPDQWDuKsBbBN6FfzC9PXcCwp1h+RAYXcMO1Qdu/PJDuTEsXG/qLrrm9r0L4FuAMQZGFuCPUK7qjixc8XKb+17elwkQGFNYuJ5yLwDL70oWxsXhcZ7rmUMT+575OYb/ShTCVuu8DBKnEqtV28/IT+cEm519g+VWUGbWy96nbHWyzW1pWU+EpEKCASXcs4FRf1a2gkPmBvC+OAUr2WDVJC+7rFIG4/FqR+54F6cOlBS6N5w8t+K9SG7gJitJ8eZZeJIDLD2Lba5GPHsYmWlZReWZCMuqAnD8WqRQ9jtk9o3u3wfTBLOq1vdPQUmUObe3F+kMjg4Cj14JpNeJnXrWYBD1NI+nV76oDA7Vk62OfrCBe4qq2z946N1jtgpiFwHGTkALow3cn2xK63v5pcx+u8895eGGKgqoverwOM/1zKGEvmd+XOjqbRJM7GVd7SUuScZ937xaBFO4kJcAQS+Ob3wkirZt2yoXkTd8V+d/MfOryBzH+RRS+zwrdf6UxCEbeidTinjsbOw3OeSpSN2o9JpH8rht26JKEW3bPj9D5lbVe42O6t0SJlkJtRA8qyXcyAaODsJc9FvDputsHTw+dgab4nWzHXipntc/AMX2uHdPr7b7gXj0FaviVZkd7vcVdPy5L/bMoYTTnvmRkS5vefBrQ+wlro3qL4SocaspTCu32xPw5sRHKMuyTENRPwzfK+OLmV/DyLn9/PnzHfX9ZoR/5ukBrIpg9WJMm443zcTjtnmTQ1a5o+XDypQl7qopy7IkKcuyLCvgXqzl+UZH9a4CMkcA5abTWqJbxzkchE3vDhTNuJzl0MQdkf31bCiDQ/VdLx//AMzukn3vnl6dZgVQZMtDWeef3KsyGR4Jv4kB1PkXe+alhJOe+U5izmFVfzW9flqtErtto2fr8fHq5tZxHsfbt3YHT1k6n6fZE7JU3qmjWFaerMxQoiKv3KTvh7Y7mxkvEorFFC4XJebi3RtocBeLsUU0UVUvdHY1nXPc4zPJyunV9liogXxYYzKvDzmHKyp3m1OrrYCnQHgintA2C+EtZgCJGgiC6E2jo6dBGMeKZymmXtC0PKSBJ0Ww4uLi5SCq6Qe6CffcmUKYjwCltKbSev2u7Kvvevn4B3DjhZLZ5b53X3XJ+OnSu3wan753px3zukxnJmZ5/fL4bswqnk6qI4fYmZ45KiFRA8HFxQ+PdPXWxqhIkratLesxT+s6j9vkv+37c4tg6YXz9OTIlGYkd/4JCzW4a6e0iXIrmRZl6Nnv0f3OZprrhnxdweO6ol6/69ZchazXrS/Yymf7c0+ITLbecY83dVjvXfx5I9tdXdZP4aY95LxcUTguRM4WUj9srcqkdBKrLVa9k1zQPolXjVa585hlmUO9C5PWckoqx2hVuEspy5eDWP2KQZyaUHqeZ3dKKTMT13dfjXT76rtePv4BYObKre72vfu6S8ZX7dV4xZuR7uU2X5eZra1NfjxYeUmW5OHxEPy2Z45LkIgf3N3dLcuJqVJqLqee2C/TCeFNp0e/zy/mee9kTLtCv2gx/9yypfe6kDdNmR6sV9lnet5JjvelRcWTddH9wfONPqxDdtf0Pep9ZbXV+/qa5usyxGn7X5f9XledryAwzizJet+w3HraRB1z7SyUK3UnnFk8Mn678K//ILS23od67l2c6T7Q0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0OAf/L3XH8LwI4LihzqkhRa6E5kLP6Cd1jbXoVy10LHfMRB+zKdYhf52Nf8ffWT494Ae6LTQ8dfGl9LQQvc7j3Tn4yH9WAym46tk/CNN0Z80/gXjh4H9MZ/X+mKM7anleeJM8LyFMUyrc188kabRfH/kJrWPzQQgVQZi6PRTWunG23Phqo6LrbzCiHXk5n/GzmEvKzeNccaK/h53zk5+Z4ifLXhRvueRDJyHs+GqXhXbapn7h6hXu8rKlZu/HbaTzfJbo0d5zve1J/JKpHNoVlia9blwVa+LbSq9Yf7vI3QVxAsZXeBN/EjBQsWWFR/HoOv1XCQDa8bMjySoqMv0JlYkgUvLOqIDxJEfCFCWFQjpMQ4koC6A+AKYLSCOrAXA4lAXlx1XtM3BaNb9LG+W9+RmvMVqGSi4tKxL6IvtawJS09JC97dpqQ1lPkhrIZ4HZTXl2TEtlXWk9MYVc1WNu6HmyfXjZVQPzNpj1nHUp6KdynrO5Hk63R5Ie4tKutsJSlpRMTCeyf0J0D4rMJ8l7DYEazsqLPBza1pddldddfry0YNyXe8/vlePJn0gm8ZRfoD/bHlXPl2xfU3dvFDr1x9m5Hlf+jzcn6Ved05xT11ce44F1gMYs1uA2iqfpLFvTnuLlRsPc8dOD3F31jUXj7TiM2xfvhW14SJl2DwmFCiSNUA1ULfT+1GezJ/KafLpM1MhR5vnKomfAS6vulCbwjqO9PPk1PVOhStgiRt9Js7yCtXEK0WyRnQ19Z8B3+qR7gdlrm3b6sPt7C7GE9NS5icxntTtpyLY7Mm+IQxkys2Lg2Mfeek0SFNdC1lXPO3Gl8euELNEeo5N5Vb7sEgvEY7Mxz7SnH0cLUgIv7jfHsd8OY1m1dcEHD7JoYXu+5EahvEX8ZYXo8Z4paJ873O9rKvB+xLbRV46DdIkfc9uoRzWV7ujwElPu2nhF+m0LQ5hkV4iHA2y0T4QmXHsN1oD0e5FoE+jWfU1dTmGFrofvTBN0/QvsV5nN88PRcy5zye+6/A9RF46CdI0UJutAG7W5ugo3lMp28dk6bVpdgiL9BKfaC2fe0tEHlkkLSHQyPpMNKvjmgCeN1ro/k7WayftQUv8Kua838yEF2a37127j7x0HL4JVi7eFpSCVtISyk4wvAcvxXpwK/ZhkY7iE5XRsnPD5ds+fIcQ1LUx92YP7Uu4qkM0q5ZQir6mzqEy1kL3d7JeuzFENWFrn+bdRUurNeW7k8x95KXj8E3gr0PHh9gxmmRFVWd11xuPjg+VY8I+LNJxfKLrYRf5KHoS4Fl5ankgm6d26Scv4aoO0ayqOqvNviYAtavQW5v+LlubXoLPTh/POIq9r+y36/Onx2HvxWh5nOednS/0Vwj7Va5oPn0+c15n89SHv12x+5rAUlstdHo/3Q8bNA/FD1wV+jfaT6cN+B/F3Y/ZQ1rmfsVI9yHb1ckqvYtTCx0fyMvRzBz0frrj6f2g0DKn8cEURKF+RTtKrTz1SPfBModo9Tez0c7hb4T6RQ1R+lloodPQ0EKnoYXud5qXim9nHvIdfEWx+OYWeD9CSNSGBD+7pBH1q2EXYeCpjPmbLx333z6OQiv70i6Sd9o5t936DWsQlO9nyj5HHnzLPDylBp5HdfGyVW+eFHgj2x205TmS4tGv+ZpJUWtT6GNHuk/TuTOfAXxqzPY7rYLZN4wo4Y0lQ/fMhrl3GQfBGcH9vptKWoRTSjvt/Urzkzd0cUqweUjmWpo+dO11zhJYzLM1pbr6EwR/mkTXTCsnffvV4fc+Spz4XxfDL9vTlcF46abMNt3+k/zV5xdPUF9kWpo+Ur3OzSuAJJQJvujWxVxjy2LgDjfQpz5bopFANEN/uAGikTsUGRdNOwwSKkAOzKGh1NDw64Z4vBuIST+SVVvIhcwAFvmkdGspxSDD86tGiBIWhRhkoKRwOz1nWAWxI+y6RQ7EyGNyn7ltA1OrapADs0QNMmKnmSWwT40gQQ3MEpiWKV64AqsqWkCVWWDVrZwyyhtmlSGmG69raphAUWtX4weq14grovl8enFNhFF+inppvmiR5Sf4VCGqi/5bmGtwhCznEKnKaFR0LPdGXu3KvOcYllcDqdYdcS8tQQqv+17qs7O2jDAcq0xR9JSDniPY0QlfcQy9Gp+2pwbC8smBcR6DUR44hvsUUJWVdt8wheUNQhmDGiAO8X2UWg1KpUhL/GZPh+wcjdoT8IEURA8iJ1vPDRp3ffepVHPjGuAW+NRAae417ry5AYwrFtXi2mnuYOZwNRUvGjm+5cAxJEuxDlpsspVP/VpZUxSLtXO9JyACs54j2NMJOeEYlk6xBnCjbtflUCSk5hrKqddzDOM+rWB+22/OdDp1GqV5t/B7NwluYZgU1/jhYzKuj5sKqRGttDx9GAWxarHMNfU1AFdLSRUdBsGaBb1omPPmDmAH1xjUAjDqt2vBe44hKVgHE/E+aGt54OHcs4HR4SnvOYKndMKe+aekCI5frm3qzZO88ZSz2nMM9ykUt+N+Q3DbkQXXZXlkv4hdBBh73tehqUCgF1U+kIIoG8yWhQDzGuD6piM0RLO5dTLdbtqv1n//imN4FAlkmcTRe83ZcwRP6YQ98y91bEsdWchNFlTDyg1GZrrnGO5T2Ixasdf1neRWslKvmBoeozd0SFGVWpz+ZPV6ZEfWgoaLlkVtnsiSY16xgJ2K1t3DvpvNb/YjYNuRCs9sLpndiGr/UMm6Kdsif6qhtN9rjXvTh6+5QUT1uj86aNb4wBKO3G/U0TowMNdBtH1UlEBZ9CmMqyxcHyI+Wd4aCnX8stlAke3eNNVAcws/0JDIG+6kuDEMccViehFFM3HdaTeoYS0cWFx0k6wZ4BE54hqzveCiVSBO91edcAz7kW65CqWMqndfkT1HsKcTcsIxnM4gbzpqYCcf5eoZWe6KA8dwnwLLLO8YreMAonwxnQ9l08eGms4ZP116l09j2AhvftzUUaZpXh8odOt2xtUV11fXcG0aSpmdy8ps5nMB3DTTadvpqqy9gHqqyOBWNdNGXUFbTi+OR61jjmHv/KqkqZTpvMsv2HMEezohJxxDURuGmXfUwM78ZVhzE3vLA8fwkALlaKkAqp3iLrpJnrJd3ctwsvVW46v2aryCtmgfj5u61fEi+KhNnA7Ap6bNwTY6q/XHcORbPc8x/Eq8np4jeEJF3DP/+jxxNsjdnjt4wk4E8MviVWM6J/GequilR7lS6TndxwodkVeZjUzX/BKh+00w327+bEKiFrqfELpfgN9wFclL/6yTtdBpodP4exkSv2oioydEWuj44A/ZaDaYhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhobGd+D/AbX3hOHtE8/qAAAAAElFTkSuQmCC)

## Next steps {#next-steps}

Congratulations, you made it! 🎉

Thinking about signing up for your next race? For your next challenge, perhaps consider creating an app your users can use to [request time off](/tools/deno-slack-sdk/tutorials/request-time-off-app)!
