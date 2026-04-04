# Source: https://firebase.google.com/docs/crashlytics/integrate-with-google-play.md.txt

By linking Firebase and Google Play, you get a richer view into your Android
app's health. For example, in the Crashlytics dashboard, you can filter your
app's crash reports by Google Play track, which lets you better focus
your dashboard on specific builds.

## Prerequisites

### Set up your app in Google Play

To take advantage of the Crashlytics integration with Google Play, make
sure that your app meets the following requirements:

- Your app in Google Play and your Firebase Android App are both
  registered using the same package name.

- Your app in Google Play is
  [set up on the app dashboard](https://support.google.com/googleplay/android-developer/answer/9859454)
  and is distributed to one of the Google Play tracks (Internal testing,
  Closed testing, Open testing, or Production).

### Link to Google Play

> [!NOTE]
> **Note:** Make sure that you have the [required level of access](https://support.google.com/firebase/answer/6392038#permissions-and-roles) to view or manage links to Google Play.

Link your Firebase Android App to your Google Play developer account:

1. In the Firebase console, go to
   \> *Project settings*,
   and then select the *Integrations* tab.

2. On the
   [*Google Play* card](https://console.firebase.google.com/project/_/settings/integrations/playlink),
   click **Link** .  

   *If you already have links to Google Play, click **Manage** instead.*

3. Follow the on-screen instructions to enable the Crashlytics integration
   and select which Firebase Android Apps to link to Google Play.

Learn more about
[creating and managing links between Firebase and Google Play](https://support.google.com/firebase/answer/6392038).

## Filter events by Google Play track

You can filter your app's crash reports by Google Play track directly in the
Crashlytics dashboard. This lets you better focus your dashboard on
specific builds.

Here's how to filter by Play track:

1. At the top of the [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics) in the
   Firebase console, select your intended Firebase Android App.

2. In the top-level
   **Filter**
   menu, click **Versions** , and then select the Google Play track for which
   you want to view Crashlytics events. You can select more than one track.

3. Click **Apply**.

All the data in the Crashlytics dashboard (crash-free statistics, trends,
and issues) will now be specific to the selected Play track(s)
and version(s).

## Other topics of interest

Now that you have a link to Google Play, take advantage of other integrations:

- Access your
  [in-app purchase and subscription revenue data](https://support.google.com/analytics/answer/11548051)
  from Google Play in both Firebase and Google Analytics.

- [Upload an Android app bundle to Firebase App Distribution](https://firebase.google.com/docs/app-distribution/android/distribute-console?apptype=aab)
  so that Google Play can generate an APK that's optimized for your
  tester's device configuration.