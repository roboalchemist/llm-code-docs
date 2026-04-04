# Source: https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-1.md.txt

# Tutorial: Optimize AdMob ad frequency

## Step 1: Use AdMob to create new ad unit variants for testing

<br />

|---|
| Introduction: [Optimize AdMob ad frequency using Firebase](https://firebase.google.com/docs/tutorials/optimize-ad-frequency) |
| **Step 1: Use AdMob to create new ad unit variants for testing** <br /> |
| Step 2: [Set up an A/B test in the Firebase console](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-2) |
| Step 3: [Handle Remote Config parameter values in your app's code](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-3) |
| Step 4: [Start the A/B test and review the test results in the Firebase console](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-4) |
| Step 5: [Decide whether to roll out the new ad format](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-5) |

<br />

To get started, you first need to create new ad units and then implement the ads
in your app's code.

This tutorial uses the
[interstitial](https://support.google.com/admob/answer/9884467) ad
format as the example test case. When reading this tutorial, though, keep in
mind that you could follow similar steps to implement and test frequency capping
for other ad formats.

<br />

**Make sure you have the prerequisites for this tutorial**

<br />

- Your own app (iOS, Android, or Unity project)

- Your app registered as a Firebase App that's linked to an AdMob App
  ([learn more](https://support.google.com/admob/answer/6383165))

- Access to your app's associated AdMob account, with permissions to create
  new ad units

- Access to your app's associated Firebase project, with permissions to create
  and manage Remote Config and A/B Testing as well as to view
  Google Analytics

- Your preferred IDE

<br />

<br />

### **Create an ad unit**

![<span class=](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/step1_create-interstitial.svg)AdMob UI showing how to create a new interstitial ad unit"\>

![](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/step1_create-interstitial.svg)

1. In your AdMob account, create a new *Interstitial* ad unit.

2. Set the frequency cap:

   1. Expand the **Advanced settings** in the AdMob UI, then enable
      **Frequency capping**.

   2. Specify an ad frequency that you want to test. Choose a frequency that's
      higher than the frequency used in your existing ad unit.

   For example, suppose your existing interstitial ad unit shows 4 impressions
   per user per 10 minutes, but you want to test out if you can increase the
   cap to *6 impressions* per user per 10 minutes.

   We recommend keeping the time duration (that is, "per 10 minutes")
   consistent across the ad units being compared. The other ad unit settings,
   though, aren't important for this particular tutorial, so select settings
   that are appropriate for your app.
   ![<span class=](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/step1_set-frequency-capping.svg)AdMob UI showing how to set the frequency capping for the new ad unit" class="screenshot"\>
3. Repeat the steps above if you'd like to add another interstitial unit to
   test out an even higher frequency cap. For this tutorial, we created another
   ad unit with *8 impressions* per user per 10 minutes.

### **Implement the ad unit**

![<span class=](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/step1_display-ad-unit-id-and-sdk-instructions.svg)AdMob UI displaying new ad unit ID and instructions for integrating the SDK"\>

![](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/step1_display-ad-unit-id-and-sdk-instructions.svg)

After you create each ad unit, AdMob provides you with the ad unit's unique
**ad unit ID** . Remember where to find this ad unit ID in your AdMob account
as you'll need it to implement the ad into your app.

Follow the on-screen instructions to integrate the
Google Mobile Ads (AdMob) SDK and to implement the new ad unit into your app.

After creating two new interstitial ad units, you should now have three ad units
listed in your AdMob account for this specific app. In the next steps of
this tutorial, you'll configure Firebase to use each of these ad units in an A/B
test using the *same ad placement*.
![<span class=](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/step1_different-ad-frequency-ad-units.svg)AdMob UI displaying all ad units for the app" class="screenshot"\>

<br />

*** ** * ** ***

<br />

[**Introduction**](https://firebase.google.com/docs/tutorials/optimize-ad-frequency)
[**Step 2** : Set up an A/B test in the Firebase console](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-2)

<br />

*** ** * ** ***