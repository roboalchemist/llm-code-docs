# Source: https://docs.statsig.com/guides/aa-sidecar.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Running an A/A Test using Sidecar

> Learn how to run an A/A test with Statsig Sidecar to validate your experimentation setup and metrics configuration.

In this guide, we will walk you through how to leverage Statsig’s sidecar to run an A/A test on your product.

<Info>
  This guide assumes that you have successfully set up and configured Statsig Sidecar. For a step-by-step guide on how to do this, see our ["setting up Sidecar"](/guides/sidecar-experiments/setup) guide.
</Info>

## Why run an A/A (aa) test?

There are many reasons to run an A/A test, one of the most common being to validate a new experimentation engine you may be integrating with (in this case Statsig).  For new users just getting started with Statsig, we often recommend running an A/A test to provide a “low-stakes” first test environment, ensuring that you’ve got your metrics set up correctly and are seeing exposures flowing through as expected before kicking off your first real A/B test.

## How to run an A/A test

### Step 1: Create a new Experiment in Sidecar

Navigate to the page on your website that you want to run an A/A Test. Open the Statsig Side car extension and click on 'New Experiment'. Fill in the title of your A/A test.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nSBTTgzvwOEKOriT/images/sidecar_aa_setup.png?fit=max&auto=format&n=nSBTTgzvwOEKOriT&q=85&s=0c47e42056a7eabf99247be8b3449e93" alt="Sidecar A/A test experiment setup interface" width="364" height="651" data-path="images/sidecar_aa_setup.png" />
</Frame>

Then, determine of the URI filter (i.e. All Pages, contains, etc.). After you have configured the URI, it is time to set up the variants.

With the variant 'Control', pick an action. In this example we are simply changing the content of an element, specifically the title, 'Getting Started is Simple'.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nSBTTgzvwOEKOriT/images/sidecar_aa_select.png?fit=max&auto=format&n=nSBTTgzvwOEKOriT&q=85&s=0c70390ed9e1c13dac5cba4ec76b7c76" alt="Sidecar A/A test variant configuration screen" width="2772" height="1334" data-path="images/sidecar_aa_select.png" />
</Frame>

Repeating the step above, you'll do the exact same action for the variant 'Test'. Your set up should look like the following.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nSBTTgzvwOEKOriT/images/sidecar_aa_final.png?fit=max&auto=format&n=nSBTTgzvwOEKOriT&q=85&s=a2a909f025dfd2fe3caf69d46e66c7f5" alt="Sidecar A/A test final configuration showing identical variants" width="471" height="889" data-path="images/sidecar_aa_final.png" />
</Frame>

From there, all you'll need to do is click 'Publish', this will push out the experiment to Statsig as a draft.

### Step 2: Configure Experiment Scorecard in Statsig Console

Once the experiment is pushed out to end users, you will need to edit the scorecard to your experiment within the console. Navigate to the console, click on the Experiments tab, and go into the experiment you just created.

In the Setup tab, you can fill out the scorecard for the experiment Hypothesis, and any primary metrics you are interested in watching. While Statsig will show you experiment results for all your metrics, these key metrics represent your hypothesis for the experiment. Establishing a hypothesis upfront ensures that the experiment serves to improve your understanding of users rather than simply serving data points to bolster the case for shipping or not shipping your experiment.

In the Allocation and Targeting section, for an AA test, we recommend to allocate 100% of users to the experiment while targeting everyone.

Then, make sure to save and push your experiment. Your test is now set up to start measuring metrics associated with the A/A Test!

### Step 3: Review A/A test results

Within 24 hours of starting your experiment, you'll see the cumulative exposures in the **Pulse Results** tab of your experiment.

his will break down your logged exposures (as well as the distribution of the logged exposures). If something looks off, check the **Diagnostics** tab for more granular, day-by-day exposure breakdowns at both the Checks and User level.

In the **Scorecard** panel, you can see the full picture of how all your tagged metrics are performing.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HZGmTR51kQF0d2q8/images/experiments/types/aa-test/163248267-7bd7419a-59e0-4d58-b8e5-8ace95ed74d9.png?fit=max&auto=format&n=HZGmTR51kQF0d2q8&q=85&s=f3577e3032d790fae8ce2edafc245bb1" alt="pulse_results_empty" width="987" height="1208" data-path="images/experiments/types/aa-test/163248267-7bd7419a-59e0-4d58-b8e5-8ace95ed74d9.png" />
</Frame>

What should you expect to see?

* **Exposures**- make sure you’re seeing exposures flowing through as expected from your product. If you’re not seeing exposures, use the **Diagnostics** tab and the **Exposure Stream** to debug
* **Pulse results**- roughly 5% of your metrics in Pulse should be showing a statistically significant change due to the 95% confidence interval of Statsig’s stats engine

We recommend running your A/A long enough to reach most of your weekly active users, or at least a week.


Built with [Mintlify](https://mintlify.com).