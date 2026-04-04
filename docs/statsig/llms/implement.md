# Source: https://docs.statsig.com/segments/implement.md

# Source: https://docs.statsig.com/experiments/implementation/implement.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Implement an Experiment

> Learn how to deploy an experiment by pulling configurations, logging events, testing, and launching.

To deploy an experiment, you'll need to:

1. Pull the experiment configurations in your application
2. Log the events you'll want in your experiment results
3. Test your experiment in development or a lower environment
4. Click "Start"!

Every experiment needs to expose users into more than one bucket (#1) and log metrics on their behavior after exposure (#2, called "log events"). Statsig automates many of the annoying parts of setting up an experiment, like writing the code you can use to assign buckets, and conducting analysis on the exposures and log events. The experimenter's job is to devise the experiments - and use our SDKs to accomplish #1 and #2.

## Pulling experiment configurations from Statsig

In the code snippets below, we illustrate experimenting on a product demo flow, where you might experiment to improve conversion through the funnel to demo completion. For full implementation details, check out the [SDK documentation](/sdks/getting-started) for the language you'll be using, or walkthrough our example guide for [your first a/b test](/guides/abn-tests).

```js  theme={null}
const user = { userID: loggedInUserID };
const demoConfiguration = statsig.getExperiment(user, "demo_experience");

// use parameters to control the experience
if (demoConfiguration.get("show_banner", false) {
  showBanner();
}

const title = demoConfiguration.get("title", "Start Demo");
banner.setTitle(title);
```

You can also look at a code snippet for your particular experiment by clicking into the code snippet button on the experiment page and selecting the right SDK

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/F_V_VJJ-2qC3MQMI/images/experiments/code-snippet-button.png?fit=max&auto=format&n=F_V_VJJ-2qC3MQMI&q=85&s=891d6de2d08518179e6b10441eb66394" alt="experiment code snippet button" width="3276" height="584" data-path="images/experiments/code-snippet-button.png" />
</Frame>

## Logging events for your scorecard

In order to get experiment results for the events and metrics you care about, you should instrument the experience with the proper event logging (or set up an event integration/data warehouse import to send events to Statsig experimentation stats engine). If you'd like to use our SDKs, your code might look like this:

```

statsig.logEvent(user, "demo_started");
...
statsig.logEvent(user, "demo_completed");
```

Just a few simple events can help you measure how people are moving through a certain funnel in your product, and enable you to experiment on those flows to increase conversion.

## Testing in a lower environment

Once experiments are launched, you can't edit the groups without restarting the experiment, as users are already being allocated to each group. We therefore recommend testing each experiment in lower environments before starting. You can do this by clicking the "Test" button in the experiment setup page, then selecting "Enable for Environments". These environments should match your [SDK environment setup](/guides/using-environments/#configuring-environments). Testing in a lower environment and [overrides](/experiments-plus/overrides) can help you manually set your experiment "group" to properly test each variant.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/kpNw96pSJgcYfCY9/images/experiments/experiment_test_button.png?fit=max&auto=format&n=kpNw96pSJgcYfCY9&q=85&s=5a5556f55671d41d6a75adfd15c7aff5" alt="Experiment test button interface" width="822" height="554" data-path="images/experiments/experiment_test_button.png" />
</Frame>

Once the experiment is enabled for a lower environment, the experiment status will shift from “Not Started” to “Testing”.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WZhckwn2L5WeRO_3/images/experiments/lower_environment_results.png?fit=max&auto=format&n=WZhckwn2L5WeRO_3&q=85&s=401a0f8645ffcf2d3e14ceffd3ba878d" alt="Lower environment resalt" width="937" height="684" data-path="images/experiments/lower_environment_results.png" />
</Frame>

In the results section, you can track cumulative exposures and metric results collected from lower environments. Results data will be displayed in aggregate across all lower environments and won't be distinguishable between individual environments. Metric data and exposure data will be retained even when the experiment is repeatedly disabled and re-enabled for the lower environment.

You can resalt experiment in lower environments. This is helpful in the situation where a given user is looking to re-test the experiment E2E.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WZhckwn2L5WeRO_3/images/experiments/lower_environment_resalt.png?fit=max&auto=format&n=WZhckwn2L5WeRO_3&q=85&s=be58abbf2869063e2b8ee9d3035abc2d" alt="Lower environment resalt" width="589" height="536" data-path="images/experiments/lower_environment_resalt.png" />
</Frame>

## Starting your experiments

Once your experiment has metrics, parameters, and a hypothesis - and you've tested it in a lower environment, you're ready to launch! Click the "Start" button and your experiment will be immediately live in Production.


Built with [Mintlify](https://mintlify.com).