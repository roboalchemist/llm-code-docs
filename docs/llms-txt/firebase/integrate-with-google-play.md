# Source: https://firebase.google.com/docs/crashlytics/integrate-with-google-play.md.txt

<br />

By linking Firebase andGoogle Play, you get a richer view into your Android app's health. For example, in theCrashlyticsdashboard, you can filter your app's crash reports byGoogle Playtrack, which lets you better focus your dashboard on specific builds.

## Prerequisites

### Set up your app inGoogle Play

To take advantage of theCrashlyticsintegration withGoogle Play, make sure that your app meets the following requirements:

- Your app inGoogle Playand your Firebase Android App are both registered using the same package name.

- Your app inGoogle Playis[set up on the app dashboard](https://support.google.com/googleplay/android-developer/answer/9859454)and is distributed to one of theGoogle Playtracks (Internal testing, Closed testing, Open testing, or Production).

### Link toGoogle Play

| **Note:** Make sure that you have the[required level of access](https://support.google.com/firebase/answer/6392038#permissions-and-roles)to view or manage links toGoogle Play.

Link your Firebase Android App to yourGoogle Playdeveloper account:

1. In theFirebaseconsole, go tosettings\>*Project settings*, and then select the*Integrations*tab.

2. On the[*Google Play*card](https://console.firebase.google.com/project/_/settings/integrations/playlink), click**Link** .  
   *If you already have links toGoogle Play, click**Manage**instead.*

3. Follow the on-screen instructions to enable theCrashlyticsintegration and select which Firebase Android Apps to link toGoogle Play.

Learn more about[creating and managing links between Firebase andGoogle Play](https://support.google.com/firebase/answer/6392038).

## Filter events byGoogle Playtrack

You can filter your app's crash reports byGoogle Playtrack directly in theCrashlyticsdashboard. This lets you better focus your dashboard on specific builds.

Here's how to filter byPlaytrack:

1. At the top of the[Crashlyticsdashboard](https://console.firebase.google.com/project/_/crashlytics)in theFirebaseconsole, select your intended Firebase Android App.

2. In the top-levelfilter_list**Filter**menu, click**Versions** , and then select theGoogle Playtrack for which you want to viewCrashlyticsevents. You can select more than one track.

3. Click**Apply**.

All the data in theCrashlyticsdashboard (crash-free statistics, trends, and issues) will now be specific to the selectedPlaytrack(s) and version(s).

## Other topics of interest

Now that you have a link toGoogle Play, take advantage of other integrations:

- Access your[in-app purchase and subscription revenue data](https://support.google.com/analytics/answer/11548051)fromGoogle Playin both Firebase andGoogle Analytics.

- [Upload an Android app bundle toFirebase App Distribution](https://firebase.google.com/docs/app-distribution/android/distribute-console?apptype=aab)so thatGoogle Playcan generate an APK that's optimized for your tester's device configuration.