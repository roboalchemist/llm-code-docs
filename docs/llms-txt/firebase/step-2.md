# Source: https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-2.md.txt

# Source: https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-2.md.txt

# Source: https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement-event-data/step-2.md.txt

# Source: https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-2.md.txt

# Source: https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-2.md.txt

# Source: https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-2.md.txt

# Source: https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-2.md.txt

## Step 2: Set up an A/B test in theFirebaseconsole

<br />

|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Introduction:[OptimizeAdMobad frequency using Firebase](https://firebase.google.com/docs/tutorials/optimize-ad-frequency)                              |
| Step 1:[UseAdMobto create new ad unit variants for testing](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-1)                   |
| **Step 2: Set up an A/B test in theFirebaseconsole**                                                                                                   |
| Step 3:[HandleRemote Configparameter values in your app's code](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-3)               |
| Step 4:[Start the A/B test and review the test results in theFirebaseconsole](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-4) |
| Step 5:[Decide whether to roll out the new ad format](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-5)                         |

<br />

Now that you have new ad units implemented in your app, you need to set up an A/B test that will help you understand how these ad units perform. You'll define which users to target in the test as well as your testing goals. You'll also need to define your test variants (the different ad units in your app) and set up theRemote Configparameter which will control the display of the variants in your app.

Firebase A/B Testingutilizes the following products to test and analyze the effects of adding an ad unit to your app:

- Firebase A/B Testing(this step) --- define goals and configurable parameters for your test
- Firebase Remote Config(next step) --- add logic to your code to handle the configuration of the parameters
- Google Analytics(runs behind the scenes) --- measures the impact of the configurations

### **Initiate a new A/B test**

To initiate a controlled test for optimizing ad frequency, start by navigating to the*A/B Testing* section of theFirebaseconsole. Click**Create experiment** , then select**Remote Config**.
![<span class=](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/step2_set-up-abtest-select-remote-config.svg)Firebaseconsole UI showing how to start an A/B test usingRemote Config" class="screenshot"\>

### **Set up the basics**

In the*Basics*section, define the experiment name and provide the experiment description.
![<span class=](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/step2_abtest-basics.svg)Firebaseconsole UI showing how to set up the basics of A/B test" class="screenshot"\>

### **Set up targeting**

1. In the*Targeting*section, select the iOS or Android app that the experiment will target.

2. Set the percentage of users who will be exposed to the experiment. For this tutorial, the new ad units will be tested with 30% of your users. Note that this doesn't mean that 30% of all your users will see the new ad units with increased frequency caps; this means that 30% of your users will be exposed to the two new interstitial ads along with the baseline ad unit (your existing ad).

   Leave all other settings as their defaults.

![<span class=](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/step2_abtest-targeting.svg)Firebaseconsole UI showing how to set up the targeting of A/B test" class="screenshot"\>**Note:** Due to the different user behavior patterns observed from iOS and Android users, each A/B test can only target either the iOS or Android version of your app.
|
| To run the same test for both versions of your app, set up an experiment for one version of your app, then duplicate the test settings in a second experiment. In this second experiment, select the other version of your app in the*Targeting*section.

### **Set up your goals**

Firebase A/B Testingtracks a primary metric to determine the winning variant, but it also allows you to add secondary metrics to understand the impacts of different configurations on other important factors for your app.

1. For this tutorial,*EstimatedAdMobrevenue*optimization is the primary goal, so select it from the dropdown menu.

2. *(Optional)* If you wantA/B Testingto track additional metrics, like*Estimated total revenue* or different retention rates, select those by clicking**Add metric**.

![<span class=](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/step2_abtest-goals.svg)Firebaseconsole UI showing how to set up the goals of A/B test" class="screenshot"\>

### **Set up the variants**

The last step of configuring an A/B test is defining aRemote Configparameter that controls which ad unit will be shown to users.

1. In the*Variants* section, create a new parameter named`INTERSTITIAL_AD_KEY`by typing it in the*Parameter* field of the*Baseline*card.

2. Finish setting up the*Variants* section using the following settings for the`INTERSTITIAL_AD_KEY`parameter:

   - ***Baseline*** variant:*Value*set to the ad unit ID of the existing ad unit with the frequency cap setting of 4 impressions per user per 10 minutes
   - ***Variant A*** variant:*Value*set to the ad unit ID of the new ad unit with the frequency cap setting of 6 impressions per user per 10 minutes
   - ***Variant B*** variant:*Value*set to the ad unit ID of the new ad unit with the frequency cap setting of 8 impressions per user per 10 minutes

   For this tutorial, the*Baseline* variant will show the existing ad unit (4 impressions per user per 10 minutes).*Variant A* and*Variant B* will show the new ad units (6 and 8 impressions per user per 10 minutes, respectively) to a small subset of users. This is controlled by the parameter's value which is the ad unit ID taken from theAdMobUI. These parameter values are set here inFirebase A/B Testing, but it's actuallyFirebase Remote Configthat sends these values to your app's code for handling. You'll set upRemote Configin the next step.
   | **Note:** In your own future tests, if you set up various experiments and variants, we recommend giving variants meaningful names to easily track the test results later on.

![<span class=](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/step2_abtest-variants.svg)Firebaseconsole UI showing how to set up the variants of A/B test" class="screenshot"\>

Click**Review** to make sure your experiment is set up as expected. However, before you can actually start the experiment, you need to define how your app's code will react to the parameter values received from Firebase. Proceed to the next step to implement howRemote Confighandles the`INTERSTITIAL_AD_KEY`parameter.

<br />

*** ** * ** ***

<br />

[arrow_back_ios**Step 1** : UseAdMobto create new ad unit variants](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-1)[**Step 3** : HandleRemote Configparameter valuesarrow_forward_ios](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-3)

<br />

*** ** * ** ***