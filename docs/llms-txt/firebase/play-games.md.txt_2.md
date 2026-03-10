# Source: https://firebase.google.com/docs/auth/unity/play-games.md.txt

You can use Google Play Games services to sign in players to an Android game
built on Firebase and Unity. To use Google Play Games services sign-in with
Firebase, first sign in the player with Google Play Games, and request an
OAuth 2.0 auth code when you do so. Then, pass the auth code to
`PlayGamesAuthProvider` to generate a Firebase credential, which you can use to
authenticate with Firebase.

> [!IMPORTANT]
> **Important:** You can use Google Play Games services sign-in only on Android.

## Before you begin

### Set up your Unity project

1. Add the Firebase config file and the Firebase Unity SDK to your Unity project
   as described in
   [Add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup#set_up_environment).
   Follow the instructions for Android.

   Be sure to import `FirebaseAuth.unitypackage`.
2. In the Unity Editor, under **Build Settings \> Player Settings \> Other
   Settings** set the Android package name of your game.

3. Then, under **Build Settings \> Player Settings \> Publishing Settings**,
   select or create a keystore and key, which will be used to sign your Android
   package. Your APK must be signed for Play Games sign-in to work---this
   requirement applies not just for publishing, but also during development of
   your game.

### Set up your Firebase project

1. In the [Firebase console](https://console.firebase.google.com/), go to the Firebase project
   in which you registered your Unity project.

2. Set your game's SHA-1 fingerprint from the
   [Settings](https://console.firebase.google.com/project/_/settings/general/) page
   of the Firebase console, using the key you set in Unity.

   You can get the SHA-1 fingerprint of your key with the `keytool` command:

   ```
   keytool -exportcert -list -v \
       -alias YOUR-KEY-NAME -keystore PATH-TO-KEYSTORE
   ```

   <br />

   Alternatively, you can get the SHA hash of your signing certificate with the
   gradle `signingReport` command:

   ```
   gradlew signingReport
   ```

   <br />

   Your APK must be signed with this key, including during development.
3. Enable Google Play Games as a sign-in provider:

   1. In the Firebase console, open the
      [**Authentication** section](https://console.firebase.google.com/project/_/authentication/providers).

   2. Generate and obtain your project's web server client ID and client
      secret:

      1. Within the **Sign in method** tab, enable the **Google** sign-in
         provider.

      2. Copy the web server client ID and secret from the **Google** sign-in
         provider.

   3. Within the **Sign in method** tab, enable the **Play Games**
      sign-in provider, and specify your project's web server client ID and
      client secret, which you got in the last step.

### Configure Play Games services with your Firebase app information

1. In the
   [Google Play Console](https://play.google.com/console/developers),
   open your Google Play app or create one.

2. In the *Grow* section, click
   **Play Games services \> Setup \& Management \> Configuration**.

3. Click **Yes, my game already uses Google APIs** , select your Firebase
   project from the list, and then click **Use**.

4. On the Play Games services configuration page, click
   **Add Credential**.

   1. Select the **Game server** type.
   2. In the **OAuth client** field, select your project's web client ID. Be sure this is the same client ID you specified when you enabled Play Games sign-in.
   3. Save your changes.
5. Still on the Play Games services configuration page, click
   **Add Credential** again.

   1. Select the **Android** type.
   2. In the **OAuth client** field, select your project's Android client ID. (If you don't see your Android client ID, be sure you set your game's SHA-1 fingerprint in the Firebase console.)
   3. Save your changes.
6. On the **Events** , **Achievements** , and **Leaderboards** pages, create any
   Play Games resources you want to use with your game (if you don't
   want to use any immediately, you can create a placeholder entry). Then, on
   any of the **Events** , **Achievements** , or **Leaderboards** pages, click
   **Get resources** and copy the Android resources snippet somewhere
   convenient. You will need the snippet to set up the Google Play Games services
   plugin.

   The resources snippet looks like the following example:

       <?xml version="1.0" encoding="utf-8"?>
       <!--
       Google Play game services IDs.
       Save this file as res/values/games-ids.xml in your project.
       -->
       <resources>
         <!-- app_id -->
         <string name="app_id" translatable="false">123456789000</string>
         <!-- package_name -->
         <string name="package_name" translatable="false">com.example.game</string>
         <!-- event Wiped Raid -->
         <string name="event_wiped_raid" translatable="false">CgkIpKjv1a4PEAIYBA</string>
       </resources>

7. On the **Testers** page, add the email addresses of any users who need
   to be able to sign in to your game before you release it on the
   Play Store.

## Integrate Play Games sign-in into your game

1. Download the latest release of the
   [Play Games plugin for Unity](https://github.com/playgameservices/play-games-plugin-for-unity/releases)
   and extract it.

2. Import the plugin's Unity package into your Unity project. You can find the
   Unity package in the `current-build` directory of the release archive.

3. Set up the Play Games plugin:

   1. Click **Window \> Google Play Games \> Setup \> Android Setup** to open the **Android Configuration** screen.
   2. Paste the Android resources snippet you got from the Play console into the **Resources Definition** field.
   3. Paste your web server client ID, which you provided when you enabled Play Games sign-in in the Firebase console, into the **Client ID** field.
   4. Click **Setup**.
4. In your game, configure a Play Games client with the `RequestServerAuthCode`
   setting enabled:

       using GooglePlayGames;
       using GooglePlayGames.BasicApi;
       using UnityEngine.SocialPlatforms;
       using System.Threading.Tasks;

       PlayGamesClientConfiguration config = new PlayGamesClientConfiguration.Builder()
           .RequestServerAuthCode(false /* Don't force refresh */)
           .Build();

       PlayGamesPlatform.InitializeInstance(config);
       PlayGamesPlatform.Activate();

5. Then, when a player chooses to sign in with Play Games, call
   `Social.localUser.Authenticate()`:

       Social.localUser.Authenticate((bool success) => {
         // handle success or failure
       });

## Authenticate with Firebase

After you add Play Games sign-in to your game, you can use the auth code from
Play Games services to authenticate with Firebase.

1. After the player has successfully signed in using Play Games, in the sign-in
   continuation handler, get an auth code for the player's account:

       Social.localUser.Authenticate((bool success) => {
         if (success) {
           authCode = PlayGamesPlatform.Instance.GetServerAuthCode();
         }
       });

2. Then, exchange the auth code from Play Games services for a Firebase
   credential, and use the Firebase credential to authenticate the player:

       Firebase.Auth.FirebaseAuth auth = Firebase.Auth.FirebaseAuth.DefaultInstance;
       Firebase.Auth.Credential credential =
           Firebase.Auth.PlayGamesAuthProvider.GetCredential(authCode);
       auth.SignInAndRetrieveDataWithCredentialAsync(credential).ContinueWith(task => {
         if (task.IsCanceled) {
           Debug.LogError("SignInAndRetrieveDataWithCredentialAsync was canceled.");
           return;
         }
         if (task.IsFaulted) {
           Debug.LogError("SignInAndRetrieveDataWithCredentialAsync encountered an error: " + task.Exception);
           return;
         }

         Firebase.Auth.AuthResult result = task.Result;
         Debug.LogFormat("User signed in successfully: {0} ({1})",
             result.User.DisplayName, result.User.UserId);
       });

## Next steps

After a user signs in for the first time, a new user account is created and
linked to their Play Games ID. This new account is stored as part of your
Firebase project, and can be used to identify a user across every app in your
project.

In your game, you can get the user's Firebase UID from the
`Firebase.Auth.FirebaseUser` object:

    Firebase.Auth.FirebaseUser user = auth.CurrentUser;
    if (user != null && user.IsValid()) {
      string playerName = user.DisplayName;

      // The user's Id, unique to the Firebase project.
      // Do NOT use this value to authenticate with your backend server, if you
      // have one; use User.TokenAsync() instead.
      string uid = user.UserId;
    }

In your Firebase Realtime Database and Cloud Storage Security Rules, you can get
the signed-in user's unique user ID from the `auth` variable, and use it to
control what data a user can access.

To get a user's Play Games player information or to access Play Games services,
use the APIs provided by the Play Games plugin.

To sign out a user, call `SignOut()`:

    auth.SignOut();