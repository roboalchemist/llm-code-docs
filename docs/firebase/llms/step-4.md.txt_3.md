# Source: https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-4.md.txt

# Tutorial: Test adoption of new AdMob ad formats

## Step 4: Start the A/B test and review the test results in the Firebase console

<br />

|---|
| Introduction: [Test new AdMob ad format adoption using Firebase](https://firebase.google.com/docs/tutorials/test-ad-format-adoption) |
| Step 1: [Use AdMob to create a new ad unit variant for testing](https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-1) |
| Step 2: [Set up an A/B test in the Firebase console](https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-2) |
| Step 3: [Handle Remote Config parameter values in your app's code](https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-3) |
| **Step 4: Start the A/B test and review the test results in the Firebase console** <br /> |
| Step 5: [Decide whether to roll out the new ad format](https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-5) |

<br />

Now that you have everything set up, you're ready to start and run your A/B
test. While the test is running, you can review results in the
Firebase console.

### **Deploy your app and start the test**

1. After you add the logic to handle the Remote Config parameter value
   (previous step), deploy the latest builds of your app that include them.

2. In the Firebase console, start the A/B test by clicking
   **Start Experiment**.

### **Review results**

1. Firebase A/B Testing will run your experiment. After it's exposed users
   to the different variants, the Firebase console will display an
   improvement suggestion.

2. Review how each variant performed based on the metrics that you selected
   during test setup.

   Firebase A/B Testing makes its judgement based on the primary metric that
   you selected, but A/B Testing also provides you with data for all the
   other secondary metrics that you selected. This allows you to take into
   account these secondary metrics when making a final judgement about the
   performance of a variant.

The image below shows an example of a test run with four variants, including the
baseline (note that in this tutorial we kept it more simple with only two
variants). In this example below, A/B Testing has determined that the winning
variant is *Variant A* due to the improvements in the primary metric of
*Estimated total revenue*.
![<span class=](https://firebase.google.com/static/docs/tutorials/test-ad-format-adoption/images/step4-5_abtest-example-test-results.svg)Firebase console UI showing example A/B test results" class="screenshot"\>

<br />

*** ** * ** ***

<br />

[**Step 3** : Handle Remote Config parameter values](https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-3)
[**Step 5** : Decide whether to roll out the new ad format](https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-5)

<br />

*** ** * ** ***