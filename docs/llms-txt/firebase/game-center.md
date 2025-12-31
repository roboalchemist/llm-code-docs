# Source: https://firebase.google.com/docs/auth/ios/game-center.md.txt

You can use Game Center to sign players in to an Apple platforms game built on Firebase. To use Game Center Sign-in with Firebase, first make sure the local player is signed in with Game Center, and then use the`GameCenterAuthProvider`object to generate a Firebase credential, which you can use to authenticate with Firebase.

## Before you begin

Use Swift Package Manager to install and manage Firebase dependencies.
| Visit[our installation guide](https://firebase.google.com/docs/ios/installation-methods)to learn about the different ways you can add Firebase SDKs to your Apple project, including importing frameworks directly and using CocoaPods.

1. In Xcode, with your app project open, navigate to**File \> Add Packages**.
2. When prompted, add the Firebase Apple platforms SDK repository:  

```text
  https://github.com/firebase/firebase-ios-sdk.git
```
| **Note:**New projects should use the default (latest) SDK version, but you can choose an older version if needed.
3. Choose theFirebase Authenticationlibrary.
4. Add the`-ObjC`flag to the*Other Linker Flags*section of your target's build settings.
5. When finished, Xcode will automatically begin resolving and downloading your dependencies in the background.

| **Deprecated:** Apple has[deprecated the`playerID`field](https://developer.apple.com/documentation/gamekit/gkplayer/1521127-playerid/). The Firebase Apple platforms SDK will use`gamePlayerID`and`teamPlayerID`from version 10.5.0 and onwards. Upgrading to SDK version 10.5.0 or later updates existing integrations that use`playerID`to instead use`gamePlayerID`and`teamPlayerID`. Upgrading existing Game Center Sign-in integrations to SDK version 10.5.0 or later is irreversible. For more details, see[Method: accounts.signInWithGameCenter](https://cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/signInWithGameCenter).

Next, perform some configuration steps:

1. Make sure you register your Apple app with Firebase. This means entering your app's bundle ID in the registration section along with additional optional information such as App Store ID and Team ID, etc. This will be required for securely verifying the audience of the user's Game Center credential before completing sign-in.
2. Enable Game Center as a sign-in provider for your Firebase project:
   1. In the[Firebaseconsole](https://console.firebase.google.com/), open the**Authentication**section.
   2. On the**Sign in method** tab, enable the**Game Center**sign-in provider.

## Integrate Game Center Sign-in into your game

First, if your game doesn't already use Game Center, follow the instructions in[Incorporating Game Center into Your Game](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/GameKit_Guide/GameCenterOverview/GameCenterOverview.html#//apple_ref/doc/uid/TP40008304-CH5-SW22)and[Authenticating a Local Player on the Device](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/GameKit_Guide/Users/Users.html#//apple_ref/doc/uid/TP40008304-CH8-SW19)on the Apple developer site.

Be sure the bundle ID you provide to iTunes Connect matches the bundle ID you used when you connected your app to your Firebase project.

As part of your Game Center integration, you define an authentication handler that is called at multiple points in the Game Center authentication process. In this handler, check if the player is signed in with Game Center. If so, you can continue to sign in to Firebase.  

#### Swift

```swift
let localPlayer = GKLocalPlayer.localPlayer()
localPlayer.authenticateHandler = { (gcAuthViewController?, error) in
  if let gcAuthViewController = gcAuthViewController {
    // Pause any activities that require user interaction, then present the
    // gcAuthViewController to the player.
  } else if localPlayer.isAuthenticated {
    // Player is signed in to Game Center. Get Firebase credentials from the
    // player's Game Center credentials (see below).
  } else {
    // Error
  }
}
```

#### Objective-C

```objective-c
__weak GKLocalPlayer *localPlayer = [GKLocalPlayer localPlayer];
localPlayer.authenticateHandler = ^(UIViewController *gcAuthViewController,
                                    NSError *error) {
  if (gcAuthViewController != nil) {
    // Pause any activities that require user interaction, then present the
    // gcAuthViewController to the player.
  } else if (localPlayer.isAuthenticated) {
    // Player is signed in to Game Center. Get Firebase credentials from the
    // player's Game Center credentials (see below).
  } else {
    // Error
  }
};
```

## Authenticate with Firebase

After you determine that the local player has signed in with Game Center, sign the player in to your game by creating an`AuthCredential`object with`GameCenterAuthProvider.getCredential()`and passing that object to`signIn(with:)`:  

### Swift

```swift
// Get Firebase credentials from the player's Game Center credentials
GameCenterAuthProvider.getCredential() { (credential, error) in
  if let error = error {
    return
  }
  // The credential can be used to sign in, or re-auth, or link or unlink.
  Auth.auth().signIn(with:credential) { (user, error) in
    if let error = error {
      return
    }
    // Player is signed in!
  }
```

### Objective-C

```objective-c
// Get Firebase credentials from the player's Game Center credentials
[FIRGameCenterAuthProvider getCredentialWithCompletion:^(FIRAuthCredential *credential,
                                                         NSError *error) {
  // The credential can be used to sign in, or re-auth, or link or unlink.
  if (error == nil) {
    [[FIRAuth auth] signInWithCredential:credential
                              completion:^(FIRUser *user, NSError *error) {
      // If error is nil, player is signed in.
    }];
  }
}];
```

## Next steps

After a user signs in for the first time, a new user account is created and linked to their Game Center ID. This new account is stored as part of your Firebase project, and can be used to identify a user across every app in your project.

In your game, you can get the user's Firebase UID from the`User`object:  

### Swift

```swift
let user = Auth.auth().currentUser
if let user = user {
  let playerName = user.displayName

  // The user's ID, unique to the Firebase project.
  // Do NOT use this value to authenticate with your backend server,
  // if you have one. Use getToken(with:) instead.
  let uid = user.uid
}
```

### Objective-C

```objective-c
FIRUser *user = [FIRAuth auth].currentUser;
if (user) {
  NSString *playerName = user.displayName;

  // The user's ID, unique to the Firebase project.
  // Do NOT use this value to authenticate with your backend server,
  // if you have one. Use getTokenWithCompletion:completion: instead.
  NSString *uid = user.uid;
}
```

In your Firebase Realtime Database and Cloud Storage Security Rules, you can get the signed-in user's unique user ID from the`auth`variable, and use it to control what data a user can access.

To get a user's Game Center player information or to access Game Center services, use the APIs provided by[Game Kit](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/GameKit_Guide/Introduction/Introduction.html).

To sign a user out of Firebase, call`Auth.signOut()`:  

### Swift

```swift
let firebaseAuth = Auth.auth()
do {
  try firebaseAuth.signOut()
} catch let signOutError as NSError {
  print ("Error signing out: %@", signOutError)
}
```

### Objective-C

```objective-c
NSError *signOutError;
BOOL status = [[FIRAuth auth] signOut:&signOutError];
if (!status) {
  NSLog(@"Error signing out: %@", signOutError);
  return;
}
```