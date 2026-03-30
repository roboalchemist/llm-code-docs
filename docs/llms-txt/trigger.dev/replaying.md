# Source: https://trigger.dev/docs/replaying.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Replaying

> A replay is a copy of a run with the same payload but against the latest version in that environment. This is useful if something went wrong and you want to try again with the latest version of your code.

### Replaying from the UI

<Tabs>
  <Tab title="From a run">
    <Steps>
      <Step title="Click the Replay button in the top right">
                <img
                  src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-action.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=64e19da4dca5b249adee459a1eeb62e1"
                  alt="Select a task, then in the bottom right
        click &#x22;Replay&#x22;"
                  width="1600"
                  height="1119"
                  data-path="images/replay-run-action.png"
                />
      </Step>

      <Step title="Confirm replay settings">
        You can edit the payload <Icon icon="circle-1" iconType="solid" size={20} color="F43F47" /> (if available) and choose the environment <Icon icon="circle-2" iconType="solid" size={20} color="F43F47" /> to replay the run in.

                <img
                  src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-modal.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=9891cc5d05792c57d3e58a06171113f4"
                  alt="Select a task, then in the bottom right
        click &#x22;Replay&#x22;"
                  width="1600"
                  height="1291"
                  data-path="images/replay-run-modal.png"
                />
      </Step>
    </Steps>
  </Tab>

  <Tab title="Runs list">
    <Steps>
      <Step title="Click the action button on a run">
                <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=a9dc0c82c7053753ab620237be1fc63d" alt="On the runs page, press the triple dot button" width="1600" height="900" data-path="images/replay-runs-list.png" />
      </Step>

      <Step title="Click replay">      <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list-popover.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=41ea417523f3a85b6dfbe0946911ee98" alt="Click replay" width="1600" height="900" data-path="images/replay-runs-list-popover.png" /></Step>
    </Steps>
  </Tab>
</Tabs>

### Replaying using the SDK

You can replay a run using the SDK:

```ts  theme={"theme":"css-variables"}
const replayedRun = await runs.replay(run.id);
```

When you call `trigger()` or `batchTrigger()` on a task you receive back a run handle which has an `id` property. You can use that `id` to replay the run.

You can also access the run id from inside a run. You could write this to your database and then replay it later.

```ts  theme={"theme":"css-variables"}
export const simpleChildTask = task({
  id: "simple-child-task",
  run: async (payload, { ctx }) => {
    // the run ID (and other useful info) is in ctx
    const runId = ctx.run.id;
  },
});
```

### Bulk replaying

See [Bulk actions](/bulk-actions) for more information.


Built with [Mintlify](https://mintlify.com).