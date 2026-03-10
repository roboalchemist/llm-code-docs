# Source: https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-5.md.txt

# Tutorial: Optimize AdMob ad frequency

## Step 5: Decide whether to roll out the new ad format

<br />

|---|
| Introduction: [Optimize AdMob ad frequency using Firebase](https://firebase.google.com/docs/tutorials/optimize-ad-frequency) |
| Step 1: [Use AdMob to create new ad unit variants for testing](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-1) |
| Step 2: [Set up an A/B test in the Firebase console](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-2) |
| Step 3: [Handle Remote Config parameter values in your app's code](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-3) |
| Step 4: [Start the A/B test and review the test results in the Firebase console](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-4) |
| **Step 5: Decide whether to roll out the new ad format** <br /> |

<br />

After letting the test run for several days or weeks, your app has probably
supplied enough data for Firebase to construct recommendations.

If Firebase A/B Testing determines that one of the variants with a higher
frequency cap is the winner, you can start showing that ad unit to all users
exposed to the experiment -- just click the **Roll out variant** button in the
A/B Testing page.
![<span class=](https://firebase.google.com/static/docs/tutorials/optimize-ad-frequency/images/step4-5_abtest-example-test-results.svg)Firebase console UI showing button to roll out a variant to selected users" class="screenshot"\>

Alternatively, if Firebase determines a winner, you can end the experiment, then
set the Remote Config parameter value to the winning variant's value. You
can make this be the setting for all your users or even just a subset of your
users.

However, if Firebase hasn't yet determined a clear winner, you can either
continue running the experiment to gather more data, or end the experiment if
it's already been running for a long period with inconclusive results.

<br />

And that's it! You've completed the tutorial for optimizing ad frequency using
Firebase.

## Related resources

- Check out another solution guide: [Test ad format adoption using
  Firebase](https://firebase.google.com/docs/tutorials/test-ad-format-adoption)

- Watch a video series: [Optimize your app revenue with Firebase and
  AdMob](https://www.youtube.com/watch?v=9lYjl5dz6F0&list=PLl-K7zZEsYLlNxt9KQJ0YGPPJjkoDBEy9)

<br />

*** ** * ** ***

<br />

[**Step 4**: Start the A/B test \& review test results](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-4)

<br />

<br />

*** ** * ** ***