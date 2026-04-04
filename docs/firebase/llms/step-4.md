# Source: https://firebase.google.com/docs/tutorials/test-ad-format-adoption/step-4.md.txt

# Source: https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-4.md.txt

# Source: https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-4.md.txt

## Step 4: Start the A/B test and review the test results in theFirebaseconsole

<br />

|------------------------------------------------------------------------------------------------------------------------------------------|
| Introduction:[OptimizeAdMobad frequency using Firebase](https://firebase.google.com/docs/tutorials/optimize-ad-frequency)                |
| Step 1:[UseAdMobto create new ad unit variants for testing](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-1)     |
| Step 2:[Set up an A/B test in theFirebaseconsole](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-2)               |
| Step 3:[HandleRemote Configparameter values in your app's code](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-3) |
| **Step 4: Start the A/B test and review the test results in theFirebaseconsole**                                                         |
| Step 5:[Decide whether to roll out the new ad format](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-5)           |

<br />

Now that you have everything set up, you're ready to start and run your A/B test. While the test is running, you can review results in theFirebaseconsole.

### **Deploy your app and start the test**

1. After you add the logic to handle theRemote Configparameter value (previous step), deploy the latest builds of your app that include them.

2. In theFirebaseconsole, start the A/B test by clicking**Start Experiment**.

### **Review results**

1. Firebase A/B Testingwill run your experiment. After it's exposed users to the different variants, theFirebaseconsole will display an improvement suggestion.

2. Review how each variant performed based on the metrics that you selected during test setup.

   Firebase A/B Testingmakes its judgement based on the primary metric that you selected, butA/B Testingalso provides you with data for all the other secondary metrics that you selected. This allows you to take into account these secondary metrics when making a final judgement about the performance of a variant.

The image below shows an example of a test run with four variants, including the baseline (note that in this tutorial we kept it more simple with only three variants). In this example below,A/B Testinghas determined that the winning variant is*Variant A* due to the improvements in the primary metric of*Estimated total revenue*.
![<span class=](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/step4-5_abtest-example-test-results.svg)Firebaseconsole UI showing example A/B test results" class="screenshot"\>

<br />

*** ** * ** ***

<br />

[arrow_back_ios**Step 3** : HandleRemote Configparameter values](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-3)[**Step 5** : Decide whether to roll out the new ad formatarrow_forward_ios](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-5)

<br />

*** ** * ** ***