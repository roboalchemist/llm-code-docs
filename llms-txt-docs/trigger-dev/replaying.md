# Source: https://trigger.dev/docs/replaying.md

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
                  data-og-width="1600"
                  width="1600"
                  data-og-height="1119"
                  height="1119"
                  data-path="images/replay-run-action.png"
                  data-optimize="true"
                  data-opv="3"
                  srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-action.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=79d76f07ffc53d8ca2e0f9d476916a6c 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-action.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=f7c001e785f946cfa10509bd5bdf10fe 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-action.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=93b7290ab8123c1791c07213bd372962 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-action.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=84ee5b71497a635461e2c19aea572c50 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-action.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=38d6e4c8e61a571835e9d2f87bacf235 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-action.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=baf3c7d6f105cc3208d5e9f34957ee33 2500w"
                />
      </Step>

      <Step title="Confirm replay settings">
        You can edit the payload <Icon icon="circle-1" iconType="solid" size={20} color="F43F47" /> (if available) and choose the environment <Icon icon="circle-2" iconType="solid" size={20} color="F43F47" /> to replay the run in.

                <img
                  src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-modal.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=9891cc5d05792c57d3e58a06171113f4"
                  alt="Select a task, then in the bottom right
        click &#x22;Replay&#x22;"
                  data-og-width="1600"
                  width="1600"
                  data-og-height="1291"
                  height="1291"
                  data-path="images/replay-run-modal.png"
                  data-optimize="true"
                  data-opv="3"
                  srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-modal.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=ed05fc9706ae81cf14f68927d22b8f73 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-modal.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=21442bda61813c50bb4314681440cfa7 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-modal.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=7c569aa440d06fb02a3f9159693e52d3 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-modal.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=6b25d98591108c1fd2912dee60156ffa 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-modal.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=f60049686106e4efc377ae6eaf306cb6 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-modal.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=39aa7ae272cbfb43d480db2e186ed885 2500w"
                />
      </Step>
    </Steps>
  </Tab>

  <Tab title="Runs list">
    <Steps>
      <Step title="Click the action button on a run">
                <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=a9dc0c82c7053753ab620237be1fc63d" alt="On the runs page, press the triple dot button" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/replay-runs-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=3a536d96cc682dc2c30d5199eb5cab7f 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=debd27af5b2f2740fbcf9f8b2dd55c81 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=5367f46371c0cc1b002f0922ffb318ce 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=e5950600d946e5ae7a86a804fe31a823 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=f04257d4a23c3d09cc824cefb8e58024 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=49aaa6bfaa1c1a3e2f7a37d0c8c0ccac 2500w" />
      </Step>

      <Step title="Click replay">      <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list-popover.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=41ea417523f3a85b6dfbe0946911ee98" alt="Click replay" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/replay-runs-list-popover.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list-popover.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=a209714c65dd764887340b4e74982e31 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list-popover.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=4878f0b2ef8a6f0454c5de06fa93afae 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list-popover.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=8ae5e94682543b0635843fa4a53cb78f 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list-popover.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=01dccbbc607bfce636f9741b0fcd2a60 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list-popover.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=82675f2f8ab5c55decf4820ceae8bb2e 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list-popover.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=f3a61382a15ee4515bd4cfaf35a397d2 2500w" /></Step>
    </Steps>
  </Tab>
</Tabs>

### Replaying using the SDK

You can replay a run using the SDK:

```ts  theme={null}
const replayedRun = await runs.replay(run.id);
```

When you call `trigger()` or `batchTrigger()` on a task you receive back a run handle which has an `id` property. You can use that `id` to replay the run.

You can also access the run id from inside a run. You could write this to your database and then replay it later.

```ts  theme={null}
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
