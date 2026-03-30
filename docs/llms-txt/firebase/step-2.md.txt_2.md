# Source: https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-2.md.txt

# Tutorial: Test adoption of new AdMob ad formats

## Step 2: Set up an A/B test in the Firebase console

<br />

|---|
| Introduction: [Test new AdMob ad format adoption using Firebase](https://firebase.google.com/docs/tutorials/test-ad-format-adoption) |
| Step 1: [Use AdMob to create a new ad unit variant for testing](https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-1) |
| **Step 2: Set up an A/B test in the Firebase console** <br /> |
| Step 3: [Handle Remote Config parameter values in your app's code](https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-3) |
| Step 4: [Start the A/B test and review the test results in the Firebase console](https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-4) |
| Step 5: [Decide whether to roll out the new ad format](https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-5) |

<br />

Now that you have a new ad unit implemented in your app, you need to set up an
A/B test that will help you understand how this ad unit performs. You'll define
which users to target in the test as well as your testing goals. You'll also
need to define your test variants (the different ad units in your app) and set
up the Remote Config parameter which will control the display of the
variants in your app.

Firebase A/B Testing utilizes the following products to test and analyze the
effects of adding an ad unit to your app:

- Firebase A/B Testing (this step) --- define goals and configurable parameters for your test
- Firebase Remote Config (next step) --- add logic to your code to handle the configuration of the parameters
- Google Analytics (runs behind the scenes) --- measures the impact of the configurations

### **Initiate a new A/B test**

To initiate a controlled test over adopting a new ad format, start by navigating
to the *A/B Testing* section of the Firebase console. Click **Create
experiment** , then select **Remote Config**.
![Set up A/B test](https://firebase.google.com/static/docs/tutorials/test-ad-format-adoption/images/step2_set-up-abtest-select-remote-config.svg)

### **Set up the basics**

In the *Basics* section, define the experiment name and provide the
experiment description.
![<span class=](https://firebase.google.com/static/docs/tutorials/test-ad-format-adoption/images/step2_abtest-basics.svg)Firebase console UI showing how to set up the basics of A/B test" class="screenshot"\>

### **Set up targeting**

1. In the *Targeting* section, select the iOS or Android app that the
   experiment will target.

2. Set the percentage of users who will be exposed to the experiment. For this
   tutorial, the new ad unit will be tested with 10% of your users. Note that
   this doesn't mean that 10% of all your users will see the new ad format;
   this means that 10% of your users will be part of the experiment to see or
   not see the new ad format.

   Leave all other settings as their defaults.

![<span class=](https://firebase.google.com/static/docs/tutorials/test-ad-format-adoption/images/step2_abtest-targeting.svg)Firebase console UI showing how to set up the targeting of A/B test" class="screenshot"\>

> [!NOTE]
> **Note:** Due to the different user behavior patterns observed from iOS and Android users, each A/B test can only target either the iOS or Android version of your app.
>
> To run the same test for both versions of your app, set up an experiment
> for one version of your app, then duplicate the test settings in a second
> experiment. In this second experiment, select the other version of your app
> in the *Targeting* section.

### **Set up your goals**

Firebase A/B Testing tracks a primary metric to determine the winning
variant, but it also allows you to add secondary metrics to understand the
impacts of different configurations on other important factors for your app.

1. For this tutorial, *Estimated AdMob revenue* optimization is the primary
   goal, so select it from the dropdown menu.

2. *(Optional)* If you want A/B Testing to track additional metrics, like
   *Estimated total revenue* or different retention rates, select those by
   clicking **Add metric**.

![<span class=](https://firebase.google.com/static/docs/tutorials/test-ad-format-adoption/images/step2_abtest-goals.svg)Firebase console UI showing how to set up the goals of A/B test" class="screenshot"\>

### **Set up the variants**

The last step of configuring an A/B test is defining a Remote Config
parameter that controls whether the new ad unit will be shown to users.

1. In the *Variants* section, create a new parameter named
   `SHOW_NEW_AD_KEY` by typing it in the *Parameter* field of the
   *Baseline* card.

2. Finish setting up the *Variants* section using the following settings
   for the `SHOW_NEW_AD_KEY` parameter:

   - ***Baseline*** variant: *Value* set to `false` (which means: do ***not*** show new ad format)
   - ***Variant A*** variant: *Value* set to `true` (which means: show new ad format)

   For this tutorial, the *Baseline* variant ***will not show*** the new ad
   format to users at all, but the *Variant A* variant ***will show*** the
   new ad format to a small subset of users. This is controlled by the
   parameter's boolean value. These values are set here in
   Firebase A/B Testing, but it's actually Firebase Remote Config
   that sends these values to your app's code for handling. You'll set up
   Remote Config in the next step.

   > [!NOTE]
   > **Note:** In your own future tests, if you set up various experiments and variants, we recommend giving variants meaningful names to easily track the test results later on.

![<span class=](https://firebase.google.com/static/docs/tutorials/test-ad-format-adoption/images/step2_abtest-variants.svg)Firebase console UI showing how to set up the variants of A/B test" class="screenshot"\>

Click **Review** to make sure your experiment is set up as expected. However,
before you can actually start the experiment, you need to define how your app's
code will react to the `true` or `false` parameter value received from Firebase.
Proceed to the next step to implement how Remote Config handles the
`SHOW_NEW_AD_KEY` parameter.

<br />

*** ** * ** ***

<br />

[**Step 1** : Use AdMob to create a new ad unit variant](https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-1)
[**Step 3** : Handle Remote Config parameter values](https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-3)

<br />

*** ** * ** ***