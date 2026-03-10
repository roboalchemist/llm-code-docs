# Source: https://firebase.google.com/docs/android/integrate-play-games.md.txt

Firebase can help level up your game:

- Log Games events with Google Analytics, a free app measurement solution
  that provides insight on app usage and user engagement.

- Use any of the [Firebase products that support games](https://firebase.google.com/games), like
  Crashlytics, Remote Config, and more.

## Get started

1. If you haven't already, create a Firebase project, and then add Firebase to
   your game ([C++](https://firebase.google.com/docs/cpp/setup) \| [Unity](https://firebase.google.com/docs/unity/setup)).

   > [!NOTE]
   > Note the following:
   > - If you've previously linked your Google Play developer account to a Google Cloud project in the Play Console, use that same project for getting started with Firebase. Behind the scenes, a Firebase project is a Google Cloud project ([learn
   >   more](https://firebase.google.com/docs/projects/learn-more#firebase-cloud-relationship)).
   > - Make sure to enable Google Analytics during the Firebase project creation flow or enable it after project creation in the [*Integrations* tab](https://console.firebase.google.com/project/_/settings/integrations/) of the Firebase console.

2. [Link your Firebase app to your
   Google Play developer account](https://support.google.com/firebase/answer/6392038).
   This same link will be used by your Play Games services project.


   In the Firebase console, go to the
   [*Integrations* tab](https://console.firebase.google.com/project/_/settings/integrations).
   On the *Google Play* card, click **Link**, and then follow the on-screen
   instructions to create the link.

3. Make sure that your app in Google Play is [set up to use
   Play Games services](https://developers.google.com/games/services/console/enabling).

   > [!NOTE]
   > When you're asked to specify whether your game already uses Google APIs, choose **Yes, my game already uses Google APIs**. Select your Firebase project from the list, and then click **Use**.

## Log Games events using Google Analytics

1. [Add Google Analytics to your app.](https://firebase.google.com/docs/analytics/get-started?platform=android)

2. Once you've added the Firebase SDK for Google Analytics to your app,
   you can begin logging Play Games events. Here are some sample
   events you can log:

   - Login events

         Bundle bundle = new Bundle();
         mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.LOGIN, bundle);

   - Unlock achievements

         Bundle bundle = new Bundle();
         bundle.putString(FirebaseAnalytics.Param.ACHIEVEMENT_ID, achievementId);
         mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.UNLOCK_ACHIEVEMENT, bundle);

   - Scores on a leaderboard

         Bundle bundle = new Bundle();
         bundle.putLong(FirebaseAnalytics.Param.SCORE, score);
         bundle.putString("leaderboard_id", leaderboardId);
         mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.POST_SCORE, bundle);

3. You can view the logged events in the
   [Analytics dashboard](https://console.firebase.google.com/project/_/analytics/app/_/overview)
   of the Firebase console.

   You can also access the Firebase console from the
   [Play Console](https://play.google.com/apps/publish/)
   by clicking the Firebase icon next to your app's icon in the Game details
   page.

## Troubleshooting common errors

### Cannot view Play Games events in the Analytics dashboard

- Check that you've [enabled Google Analytics for your Firebase
  project](https://support.google.com/firebase/answer/9289399#linkga)
  and that you've
  [integrated Google Analytics](https://firebase.google.com/docs/analytics/get-started?platform=android)
  into your game.

- Verify that your code implements events for `LOGIN`, `UNLOCK_ACHIEVEMENT`, or
  `POST_SCORE`.

- Verify the SDK is logging events by enabling
  [verbose logging](https://firebase.google.com/docs/analytics/events?platform=android#view_events_in_the_android_studio_debug_log).
  Because devices batch events to preserve battery life, it can take some time
  before these events are visible in the Analytics dashboard.

### Cannot link Google Play to Firebase

You need to [link Google Play to Firebase](https://support.google.com/firebase/answer/6392038)
using the Firebase console
( \> *Project settings* \>
*Integrations* \> *Google Play*). If you're having trouble linking, check the
following:

- Make sure that your app meets all the
  [prerequisites](https://support.google.com/firebase/answer/6392038#prerequisites)
  for linking.

- Make sure that you have the
  [required access](https://support.google.com/firebase/answer/6392038#permissions-and-roles)
  for creating the link.

### Cannot access the Firebase console from the Play Console

Make sure that your Google Play developer account is linked to a Firebase app. In the
[Play Console](https://play.google.com/apps/publish/), an Owner or
Admin of the Play developer account can view the linking status under
*Setup* \> *Linked Services* \> *Firebase*.