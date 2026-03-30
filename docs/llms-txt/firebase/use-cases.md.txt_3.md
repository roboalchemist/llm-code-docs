# Source: https://firebase.google.com/docs/remote-config/personalization/use-cases.md.txt

# What can you do with Remote Config personalization?

Remote Config personalization optimizes for Google Analytics events,
so if you can trigger an event with meaningful parameters, you can create a
personalization for it.

For the most useful results, you should choose an event that triggers often
with alternative values that you expect to produce significant differences in
outcomes. Personalization performs best when you have at least 10,000 users and
over 1000 triggering events per week (or conversions).

A few of the different ways you can personalize your app are described below.

## Optimize for ad impression revenue

One way you can use personalization is to optimize for ad impression revenue.
For this use case, let's say you have a game with optional mini-games gated
behind a full-page ad and you want to optimize the mini-game experience for each
user, providing the most ad revenue without impacting user engagement.

Let's walk through one way you might accomplish this:

1. In your game, implement custom event logging for the `ad_impression` event
   specific to the ad providers you use, making sure that `currency` and
   `value` parameters are included and that revenue is being added in the
   reported value parameter.

   [Measure ad revenue](https://firebase.google.com/docs/analytics/measure-ad-revenue)
   describes how to
   [automatically log ad_impression events with Admob](https://firebase.google.com/docs/analytics/measure-ad-revenue#implementation-admob)
   and also provides a few other implementation examples for other ad serving
   platforms, like
   [AppLovin](https://firebase.google.com/docs/analytics/measure-ad-revenue#implementation-appLovin)
   and
   [ironSource](https://firebase.google.com/docs/analytics/measure-ad-revenue#implementation-ironsource).

   > [!IMPORTANT]
   > **Important:** Report revenue values using the same base currency to ensure consistency.

2. Determine the Remote Config parameter you'll use and the alternative
   values to choose from and ensure that the logic in your game can handle the
   different values.

   This example describes implementing a Remote Config parameter as a
   feature flag to enable several different mini-games. To do this, open the
   [Remote Config page](https://console.firebase.google.com/project/_/config)
   and click **Add parameter** . You can name the Remote Config parameter
   `minigame` with a default value of `no_game`.

   ![Add a Remote Config parameter](https://firebase.google.com/static/docs/remote-config/personalization/images/usecase-personalization-editparam.png "Add a Remote Config parameter")
3. Now, add a personalization by clicking **Add new** and selecting
   **Personalization**.

4. Add up to five alternative values, and then click **Next**.

   For this minigame example, you can use `tictactoe`, `word_scramble`, and
   `race`.

   ![Add alternative values](https://firebase.google.com/static/docs/remote-config/personalization/images/usecase-personalization-addparams.png "Add alternative values")
5. Next, choose an objective. Because you are now logging ad impression events
   that contain revenue values, select **Ad Impression** as the objective,
   choose **SUM** and **value** as the parameter to aggregate, and add an
   additional tracking metric for **User engagement time**. This allows you to
   see how it compares in personalization results.

   You can select one other event as a custom metric here, too, if you find it
   relevant.

   ![Select an objective](https://firebase.google.com/static/docs/remote-config/personalization/images/usecase-personalization-objective-adimpression.png "Select an objective")
6. Click **Next** to choose a target condition. Because you are optimizing on
   the aggregated value of ad impression revenue, if you aren't converting your
   event revenue value into the same currency, you may want to create a
   condition based on users in a specific region to improve consistency.

   ![Choose a target condition](https://firebase.google.com/static/docs/remote-config/personalization/images/usecase-personalization-targeting-us.png "Choose a target condition")
7. Click **Next** and name your personalization, then click **Save**.

   ![Name your personalization](https://firebase.google.com/static/docs/remote-config/personalization/images/usecase-personalization-editname.png "Name your personalization")
8. Click **Publish changes** to launch the personalization. Users will begin to
   receive personalized parameter values in a few hours (depending on the
   Remote Config
   [fetch interval](https://firebase.google.com/docs/remote-config/web/get-started#minimum-fetch).
   Because the amount of time a value is applied to a user (the *stickiness
   window*) is 24 hours, we recommend that you let your personalizations run
   for 14 days (or perpetually) so that they continually learn and improve,
   providing an optimal experience for each user.

   You can see how your personalizations are performing by clicking on the
   parameter's targeting condition on the
   [Remote Config](https://console.firebase.google.com/project/_/config) page.

Now that you've learned how to create a personalization, read on to explore
other use cases and discuss the options you can use to implement them.

## Select the best ad placement for each user

Different users may respond in different ways when presented with certain ad
form factors or location. In this use case, you can use a Remote Config
parameter like `ad_placement` with different locational values, and optimize
for ad clicks.

When optimizing for `ad_clicks`, you may want to configure at least one
additional metric for `user_engagement` to track user engagement levels to
ensure they stay high.

| **Personalization Component** | **Potential and recommended values** |
|---|---|
| Remote Config parameter | `ad_placement` |
| Alternative values | `top-left, bottom, middle-panel, full-screen` |
| Objective | `ad_clicks` |
| Additional metrics | `user_engagement` |

## Optimize for ad frequency

In this use case, you can optimize ad frequency, optimizing for user engagement
to determine which ad frequency results in the most user engagement. Use
`ad_click` as an additional metric to track.

| **Personalization Component** | **Potential or recommended values** |
|---|---|
| Remote Config parameter | `ad_display_freq_in_min` |
| Alternative values | `2, 10, 50` |
| Objective | `user_engagement` |
| Additional metrics | `ad_click` |

## Determine the best difficulty selection to maximize for user engagement

In this use case, you can customize your app for each user, choosing the right
level of difficulty to fully engage each individual user with varying levels of
player skill. You can use `level_difficulty` as a Remote Config parameter
and user engagement as an objective. Add any additional metric you find
relevant here---this example uses `level_complete` to gain insight
into user progression through the game.

You could also use an objective like ad impression revenue (as configured in
[Optimize for ad impression revenue](https://firebase.google.com/docs/remote-config/personalization/use-cases#optimize-for-ad-impression-revenue)) or
use `in_app_purchase` to optimize for IAPs.

| **Personalization Component** | **Potential or recommended values** |
|---|---|
| Remote Config parameter | `level_difficulty` |
| Alternative values | `easy, medium, difficult, impossible` |
| Objective | `user_engagement` |
| Additional metrics | `level_complete` |