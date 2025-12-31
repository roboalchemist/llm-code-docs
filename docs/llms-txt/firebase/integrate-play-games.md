# Source: https://firebase.google.com/docs/android/integrate-play-games.md.txt

<br />

Firebase can help level up your game:

- Log Games events withGoogle Analytics, a free app measurement solution that provides insight on app usage and user engagement.

- Use any of the[Firebase products that support games](https://firebase.google.com/games), likeCrashlytics,Remote Config, and more.

## Get started

1. If you haven't already, create a Firebase project, and then add Firebase to your game ([C++](https://firebase.google.com/docs/cpp/setup)\|[Unity](https://firebase.google.com/docs/unity/setup)).

   | Note the following:
   | - If you've previously linked yourGoogle Playdeveloper account to aGoogle Cloudproject in thePlayConsole, use that same project for getting started with Firebase. Behind the scenes, a Firebase project is aGoogle Cloudproject ([learn more](https://firebase.google.com/docs/projects/learn-more#firebase-cloud-relationship)).
   | - Make sure to enableGoogle Analyticsduring the Firebase project creation flow or enable it after project creation in the[*Integrations*tab](https://console.firebase.google.com/project/_/settings/integrations/)of theFirebaseconsole.
2. [Link your Firebase app to yourGoogle Playdeveloper account](https://support.google.com/firebase/answer/6392038). This same link will be used by yourPlay Gamesservicesproject.  
   In theFirebaseconsole, go to the[*Integrations*tab](https://console.firebase.google.com/project/_/settings/integrations). On the*Google Play* card, click**Link**, and then follow the on-screen instructions to create the link.

3. Make sure that your app inGoogle Playis[set up to usePlay Gamesservices](https://developers.google.com/games/services/console/enabling).

   | When you're asked to specify whether your game already uses Google APIs, choose**Yes, my game already uses Google APIs**. Select your Firebase project from the list, and then click**Use**.

## Log Games events usingGoogle Analytics

1. [AddGoogle Analyticsto your app.](https://firebase.google.com/docs/analytics/get-started?platform=android)

2. Once you've added the Firebase SDK forGoogle Analyticsto your app, you can begin loggingPlay Gamesevents. Here are some sample events you can log:

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

3. You can view the logged events in the[Analyticsdashboard](https://console.firebase.google.com/project/_/analytics/app/_/overview)of theFirebaseconsole.

   You can also access theFirebaseconsole from the[PlayConsole](https://play.google.com/apps/publish/)by clicking the Firebase icon next to your app's icon in the Game details page.

## Troubleshooting common errors

### Cannot viewPlay Gamesevents in theAnalyticsdashboard

- Check that you've[enabledGoogle Analyticsfor your Firebase project](https://support.google.com/firebase/answer/9289399#linkga)and that you've[integratedGoogle Analytics](https://firebase.google.com/docs/analytics/get-started?platform=android)into your game.

- Verify that your code implements events for`LOGIN`,`UNLOCK_ACHIEVEMENT`, or`POST_SCORE`.

- Verify the SDK is logging events by enabling[verbose logging](https://firebase.google.com/docs/analytics/events?platform=android#view_events_in_the_android_studio_debug_log). Because devices batch events to preserve battery life, it can take some time before these events are visible in theAnalyticsdashboard.

### Cannot linkGoogle Playto Firebase

You need to[linkGoogle Playto Firebase](https://support.google.com/firebase/answer/6392038)using theFirebaseconsole (settings\>*Project settings* \>*Integrations* \>*Google Play*). If you're having trouble linking, check the following:

- Make sure that your app meets all the[prerequisites](https://support.google.com/firebase/answer/6392038#prerequisites)for linking.

- Make sure that you have the[required access](https://support.google.com/firebase/answer/6392038#permissions-and-roles)for creating the link.

### Cannot access theFirebaseconsole from thePlayConsole

Make sure that yourGoogle Playdeveloper account is linked to a Firebase app. In the[PlayConsole](https://play.google.com/apps/publish/), an Owner or Admin of thePlaydeveloper account can view the linking status undersettings*Setup* \>*Linked Services* \>*Firebase*.