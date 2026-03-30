# Source: https://firebase.google.com/docs/remote-config/personalization/get-started.md.txt

# Get started with Remote Config personalization

[Video](https://www.youtube.com/watch?v=MTclqADW9rs)

With Remote Config personalization, you automatically provide users
one of several alternative user experiences, in order to optimize for an
objective of your choice.
See an [Overview](https://firebase.google.com/docs/remote-config/personalization) of this feature.

Here's how to get started.

## 1. Instrument your app with Analytics and Remote Config

Before you can start providing personalized user experiences, your app needs to
be using Analytics and Remote Config.

1. If you didn't enable [Google Analytics](https://firebase.google.com/docs/analytics) when you
   created your Firebase project, enable it on your project's
   [Integrations](https://console.firebase.google.com/project/_/settings/integrations) page.

2. Make sure you're using at least the following versions of the
   Remote Config SDK:

   - iOS: 7.5.0 and above
   - Android: 20.0.3 (Firebase BoM 26.4.0) and above
   - C++ 7.1.1 and above
   - Unity: 7.1.0 and above

   Only these versions (and newer) perform the logging necessary for the
   personalization system to learn how to optimize for your objective.
3. Add [event logging](https://firebase.google.com/docs/analytics/events) calls to your app.

   At a minimum, log an event when a user completes the objective action you're
   optimizing for. For example, if you want to optimize for Play Store rating
   submissions, log an event every time a user rates your app.

   In addition, you should explicitly log any
   [Analytics events](https://support.google.com/analytics/answer/9267735)
   relevant to your app that aren't
   [automatically logged](https://support.google.com/analytics/answer/9234069).
   By logging these contextual events, you can improve the quality of your
   personalizations.
4. Implement the different user experiences you want to be possible in your
   app. This could be as simple as personalizing how often ads are shown to
   each user, or more substantial alternatives, such as implementing different
   layouts.

5. Make the different user experiences configurable based on the value of
   a Remote Config parameter.
   See [Get started with Remote Config](https://firebase.google.com/docs/remote-config/get-started)
   and [Remote Config loading strategies](https://firebase.google.com/docs/remote-config/loading).

At this point, you can deploy your app to the App Store or Play Store. Users
will continue to get the default experience you configured, but because you can
control the experience with a remotely configurable variable, you can start
experimenting with automatic parameter personalization.

You will need to have a critical mass of users using your updated app before the
personalization system can begin to optimize individual experiences.

## 2. Configure parameter personalization in the Firebase console

Now that your instrumented app is in users' hands, you can use the
Firebase console to set up personalization.

1. On the [Remote Config](https://console.firebase.google.com/project/_/config) page of
   the Firebase console, find the parameter that controls the user
   experience you want to personalize, and click the pencil icon to edit it.

2. On the **Edit parameter** pane, click **Add new \> Personalization**.

3. Define two or more alternative values. "Alternative values" are a special
   name for the parameter values that the personalization algorithm can choose
   for your users. The format of the values you use here must match the
   [data type](https://firebase.google.com/docs/remote-config/parameters#parameter_value_data_types) that
   your Remote Config parameter uses.

   > [!NOTE]
   > **Tip:** Choose alternatives that you expect to produce a large difference in outcomes. The system will learn faster and create more value when alternatives are less similar to each other.

4. Choose an objective. You can choose one of the following:

   - Select from a list of prebuilt objectives for metrics like revenue and engagement.
   - Add a custom metric based on any other Google Analytics event that
     you'd like to optimize by typing the event name into the **Objective**
     field and clicking **Create event**.

     Because these events may be dynamic or custom, they may not appear in the
     drop-down. To ensure the metric you specify precisely matches an active
     Analytics event, verify the event in **Analytics** \> **Events**.

   > [!NOTE]
   > **Tip:** Choose an objective that fully captures the behavior you want to optimize. The algorithm only considers the objective when assigning alternatives and measuring performance.

5. Select whether to optimize for the number of events (**COUNT** ) or the sum
   of all events' values (**SUM**).

   In some cases, this option is pre-selected for built-in Analytics
   events. For example, **SUM** will always be selected for **User engagement**
   time to optimize for total time spent. If you choose **Ad clicks** ,
   personalizations are optimized for **COUNT**, or total number of ad click
   events.
6. If you selected **SUM**, enter the name of the event parameter to
   aggregate.

   In most cases, the event parameter name is `value`, but you might
   have a custom metric with a specific value you want to aggregate. For
   example, if you had an event with different currency types with parameters
   like `USD`, `JPY`, `AUD` and so on, you could optimize for Australian revenue
   by specifying `AUD` as the event parameter (and, in the next step, be sure to
   configure a targeting condition for users in Australia!).

   > [!IMPORTANT]
   > **Important:** The value passed by the event must be an `int`, `double`, or `float` to be summed/aggregated.

7. Optionally, choose up to two additional metrics to track. While these will
   not affect the personalization algorithm, these results can help you better
   understand performance and trends. For example, if your personalization
   optimizes for ad clicks, you may want to track user engagement between the
   baseline and personalized groups.

   Tracked metrics will appear in the Personalization results summary,
   organized by tab.
8. Define or select a targeting condition for the personalized parameter.
   Only users who meet this condition will get a personalized experience.
   Some commonly used conditions are to limit personalization to only users
   of a particular platform or to only users in a particular region.

   > [!NOTE]
   >
   > **Tip:** Choose large enough target segments
   > to generate plenty of result data---personalization performs best
   > with at least 10,000 users and 1,000 successful outcomes per week.
   >
   >
   > You can use the **User exists** condition to ensure that
   > all users of all apps within your project are targeted for
   > personalization.

When you're satisfied with your alternatives, objective, additional metrics, and
targeting, you're done! Save and deploy your changes to start personalizing your
users' individual experiences. Users will begin to receive personalized
parameter values in a few hours, but it will take up to 14 days for the system
to learn about your user and achieve the best performance.

You can see how a personalization is performing by selecting it from the
[Personalizations page](https://console.firebase.google.com/project/_config/personalizations)
or by clicking on the parameter's targeting condition on the
[Remote Config](https://console.firebase.google.com/project/_/config) page.

> [!TIP]
> **Tip:** You can use the [Personalizations list view](https://console.firebase.google.com/project/_config/personalizations) to search for a specific personalization by name or objective, and can sort by Name, Start time, or Total lift.

For more information about interpreting results, see
[Understand personalization results](https://firebase.google.com/docs/remote-config/personalization/about#understand-personalization-results).