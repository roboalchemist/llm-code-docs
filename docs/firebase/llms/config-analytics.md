# Source: https://firebase.google.com/docs/remote-config/config-analytics.md.txt

<br />

When you build an app that includes both FirebaseRemote ConfigandGoogle Analytics, you gain the ability to understand your app users better and to respond to their needs more quickly. You can useAnalytics[audiences](https://support.google.com/firebase/answer/6317509)and[user properties](https://support.google.com/firebase/answer/6317519)to customize your app for segments of your user base with flexibility and precision.

Integrating theGoogle AnalyticsSDK provides insights that help you tailor your offerings with[A/B Testing](https://firebase.google.com/docs/ab-testing),[Remote Configpersonalization](https://firebase.google.com/docs/remote-config/personalization), and[Remote Configrollouts](https://firebase.google.com/docs/remote-config/rollouts). You can analyze the results to understand how different choices impact key metrics like revenue and engagement.
| **Warning:** To use audiences and user properties withRemote Config, you must enable[Google Analyticsdata sharing](https://support.google.com/firebase/answer/6383877)for your project. In your app, you'll need to ensure Firebase Analytics is present and data collection is available as well.

To learn more about analyzing app usage withGoogle Analytics, see the[Analyticsintroduction](https://firebase.google.com/docs/analytics).

To customize your app using segments you may have identified outside Firebase, see the[imported segments documentation](https://firebase.google.com/docs/projects/import-segments).

## Remote Configand user properties

Remote Confignow lets you use combinations ofAnalyticsuser properties to create conditions, allowing you to customize your app for segments of your user base that you have defined.

For example, you could define the following user properties inGoogle Analyticsfor use in an exercise app with a range of exercise activities at different durations and difficulty levels:

- Exercise_Interest
- Preferred_Exercise_Duration
- Preferred_Difficulty_Level

Then, you could create conditions that use these properties (individually, or in combination) to tailor the appearance and behavior of your app for specific users. For example, you could design your app so that users who are interested in running see an image of a jogger when your app is loading. Or, you could define segments of your user base by exercise duration and difficulty level so that casual users are first presented with a suggestion for a shorter, easier workout, whereas serious athletes are invited to start a 40-minute run when our app starts up.
| **Caution:**You can't use a small set of user property names reserved by Google:
|
| - **Age**
| - **Gender**
| - **Interest**
|
| If you create an audience containing any of these disallowed properties, it won't be available for creating conditions.

If the behaviors of your users change in ways that alter their user properties, those updates are collected byGoogle Analytics, which can change the behavior and appearance of their app instance after the next fetch request. A full range of operators are available so that you can create rules that include or exclude users with specific user properties or combinations of user properties.

You can also combine otherRemote Configrules with rules based on user properties, to deliver customized app behaviors to audience segments like the following:

- Users who like yoga (**Exercise_Interest** exactly matches**yoga** ), who use your app on an Android device (**OS type** ==**Android** ), located in Canada (**Device in region/country** ==**Canada**).
- Users who are interested in either weight lifting or weight loss (**Exercise_Interest** contains**weight** ) who use your app on an Apple device (**OS type** ==**iOS** ) with an English-language UI (**Device language** ==**English**).

| **Note:** On Web, it can take several hours for a property to be available for targeting. See the documentation for[user properties on Web/JavaScript](https://firebase.google.com/docs/analytics/user-properties?platform=web)for more information.

## Target by first open time

After you linkGoogle AnalyticsandRemote Config, you can target users based on the first time they open your app (using theAnalyticsevent`first_open`) forRemote Configparameter fetches and personalizations, andA/B Testingexperiments.

You can use**First Open Time**to:

- Target new users.
- Target user groups who joined during a specific time period in the past.
- Create and test onboarding flows and welcome experiences for new users.
- Create custom experiences for users who join during specific time periods.

For example, say you have an online shopping app with users in multiple countries, and want to advertise special holiday deals to new app users. For something like a Black Friday sale, which applies to US users, you can set up a condition for yourRemote ConfigorA/B Testingexperiment that targets a specific iOS or Android app, then select all US users (**Device in region/country** ==**United States** ) who first open your app in the month leading up to the sale (**First open After 11/01/2022 12:00 AM Los Angeles Time** and**First open Before 11/26/2022 12:00 AM Los Angeles Time**).

User targeting by first open time is available after you select an Android or iOS app. It is currently supported by the followingRemote ConfigSDK versions: Apple platforms SDK v9.0.0+ and Android SDK v21.1.1+ (Firebase BoMv30.3.0+).

You can target users that first launch your app at any time, as long as a supported SDK is installed andAnalyticsis enabled.

## Next Steps

To learn more about user properties, see the following guides:

- [Set user properties on Apple platforms](https://firebase.google.com/docs/analytics/user-properties?platform=ios)
- [Set user properties on Android](https://firebase.google.com/docs/analytics/user-properties?platform=android)
- [Set user properties on Web/JavaScript](https://firebase.google.com/docs/analytics/user-properties?platform=web)

| **Note:** [Automatically collected user properties](https://support.google.com/firebase/answer/6317486)are not currently available when creatingRemote Configconditions.

To learn more about how conditions are created by combining rules, see[Remote Config Parameters and Conditions](https://firebase.google.com/docs/remote-config/parameters).

To add aRemote Configcondition to your project, see[Add or edit a condition](https://support.google.com/firebase/answer/6386651#add_a_condition). You can create parameters, rules and conditions in the[Firebaseconsole](https://console.firebase.google.com/project/_/config).