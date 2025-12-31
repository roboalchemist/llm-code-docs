# Source: https://firebase.google.com/docs/tutorials/test-ad-format-adoption/solution-overview.md.txt

# Source: https://firebase.google.com/docs/tutorials/optimize-ad-frequency/solution-overview.md.txt

### **Solution overview**

## What is ad frequency optimization?

Whether your app is hybrid-revenue or ads-revenue driven, optimizing ads revenue and keeping a high-quality user experience can be tricky. Ads are a great source of revenue, but a high frequency of ads can provide a negative user experience and might lead to user churn.

There is no "one ad frequency suits all" approach for any app; ads performance varies greatly from app to app and from audience to audience. You might be concerned that increasing ad frequency could have a negative impact on user experience or retention, but you might also be curious to see if it could lead to an increase in revenue and engagement when instrumented properly, keeping engagement metrics in check.
![Graph showing changes in ARPDAU, net daily revenue, and retention with increasing ad frequency](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/optimal-ad-frequency-business-chart.svg)***Figure 1**: Optimal ad frequency maximizes revenue with minimal impact to churn*

To resolve these unknowns, Firebase offers tools that help you test and then make data-driven decisions about the optimal ad frequency:

- Using Firebase, you can A/B test the performance of various ad frequencies with a*small subset*of users.

- You can observe the test results and review recommendations from Firebase about which ad frequency is performing better and with minimal impact on retention.

- Once you're confident that the changes will likely have a positive impact, you can roll out the changes to more of your users with a click of a button.

## Business case and the value

Developers and publishers usingGoogle AdMoband Firebase tools for optimizing their ad frequencies enjoy major revenue uplifts without adversely impacting user experience.

|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![Qtonz logo](https://firebase.google.com/static/images/usecases/qtonz.png) | [**Qtonz**](https://firebase.google.com/use-cases/qtonz-mbit-music)uses Firebase to boost ad revenue by 4x and grow engagement by customizing the experience for different stages of the user journey. - **Fewer ads for new users** : They*reduced the number of ads*that a user sees on their first day using the app. They also changed the placement so that ads only appear after users complete a key in-app action. These changes made ads less intrusive. - **More frequent ads for engaged users** : For users with longer session lengths, Qtonz*increased the number of ads*shown from 2 to 3-4 per day. |

## Implementing the solution

To implement this solution, you can follow our step-by-step tutorial (find an overview of this tutorial later on this page).  

In this multistep tutorial, you'll learn**how to use Firebase to test various frequency caps forGoogle AdMobads in your app** . It uses[interstitial ads](https://support.google.com/admob/answer/7311435)as the example test case, but you can extrapolate and use these same steps to test frequency capping for[other ad formats](https://support.google.com/admob/answer/6128738).

This tutorial assumes that you already useAdMobin your app and that you'd like to test whether changing the*frequency* of an interstitial ad unit will have an impact on your app's revenue or other metrics. However, if you don't already useAdMobin your app, that's ok! The steps in this tutorial can also help you understand what ad frequency you should use in your app.
| **Tip:** If there's a term that you're not familiar with, check out the[glossary](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/solution-overview#glossary)at the bottom of this page.

### Products and features used for this solution

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Google AdMob > [Google AdMob](https://firebase.google.com/docs/admob)enables you to create ad units with various ad frequencies or refresh rates that will be served within your app. When you linkAdMobwith Firebase,AdMobsends ad revenue information to Firebase to improve ad strategy optimization. Google Analytics > [Google Analytics](https://firebase.google.com/docs/analytics)gives you insight into user engagement, retention, and monetization metrics like total revenue,AdMobrevenue, purchase revenue, and much more. It also allows you to create user audiences and segments. | Firebase Remote Config > [Firebase Remote Config](https://firebase.google.com/docs/remote-config)enables you to dynamically change and customize the behavior and appearance of your app for desired user segments ---*all without publishing a new version of your app* . In this tutorial, you'll useRemote Configparameters to control which ad unit is shown to your users. Firebase A/B Testing > [Firebase A/B Testing](https://firebase.google.com/docs/ab-testing)provides the interface and infrastructure to run product and marketing experiments in your app. It takes care of distributing experiment variants to users, and then performs statistical analysis to determine if an experiment variant is outperforming the control group based on your selected key metric, such as revenue or user retention. |

<br />

![Flowchart of solution and products used](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/optimize-ad-frequency-flowchart.svg)

![](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/optimize-ad-frequency-flowchart.svg)

<br />

### Solution tutorial overview

[Go directly to the step-by-step tutorial](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-1)

1. [**UseAdMobto create new ad unit variants for testing**](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-1)

   1. Create two new interstitial ad units inAdMob.

   2. Set the*Frequency capping*of each ad unit to an impressions per user value that you want to test.

   3. Implement the ad unit placements within your app's code.

2. [**Set up an A/B test in theFirebaseconsole**](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-2)

   1. Define testing basics, targeting, and the goals that the test will run against.

   2. Define test variants and set up theRemote Configparameter that will control which ad unit is shown to users in the test.

3. [**HandleRemote Configparameter values in your app's code**](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-3)

   1. Use theRemote Configparameter in your app.

   2. Implement the logic for displaying the ad unit based on the parameter's value.

4. [**Start the A/B test and review the test results in theFirebaseconsole**](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-4)

   1. After starting the test and allowing it to run for a few days or weeks, check theFirebaseconsole for whether the A/B test has a winning variant based on the primary goal of the A/B test.

   2. Review the impact on secondary metrics for each variant to ensure the variants didn't cause unintended negative impacts to those metrics.

5. [**Decide whether to roll out the new ad unit with the updated ad frequency**](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-5)

   1. IfA/B Testingdetermines that the variant showing the new ad format is the winner, you can start showing the ad format to all users targeted in the experiment, all users of your app, or to a subset of your users.

   2. If a clear winner isn't yet determined, you can either continue running the experiment to gather more data, or end the experiment if it's already been running for a long period with inconclusive results.

### Glossary

<br />

View a list of common terms for this solution

<br />

- **AdMobrevenue** :AdMobnetwork and open bidding revenue

- **IAP revenue**: In app purchases revenue

- **Total revenue**: Total revenue

- **Retention**: Retention as a key metric in A/B tests is tracked as 1 day, 2-3 days, 4-7 days, 8-14 days, or 15+ days user retention

- **Remote Configparameter**: The configurable parameter used to control which ad unit is show to users. In this guide, it will be an ad unit ID.

- **Baseline configuration** : The as-is configuration in any particular A/B test --- also known as the control. The control usually uses the default value for theRemote Configparameter, but it can be configured to use a new control value if needed.

- **Variant configurations** : The variant configurations are the alternative configurations with differentRemote Configparameter values that we would like to test against the baseline configuration.

<br />

<br />