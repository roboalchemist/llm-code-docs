# Source: https://firebase.google.com/docs/auth/ios/single-sign-on.md.txt

To share authentication states across multiple apps or extensions on Apple platforms, store the authentication state in a shared keychain using[Keychain Services](https://developer.apple.com/documentation/security/keychain_services)and configure your apps to use the shared keychain.

This allows users to:

- Sign in once and be signed in across all apps that belong to the same access group.
- Sign out once and be signed out across all apps that belong to the same access group.

| **Note:** Shared keychain does not automatically update users across apps in real time. If you make a change to a user in one app, the user must be reloaded in any other shared keychain apps before the changes will be visible.

## Share auth state between apps

To share auth state between apps:

1. Set up an access group for your apps.

   You can use either a keychain access group or an app group. See[Sharing Access to Keychain Items Among a Collection of Apps](https://developer.apple.com/documentation/security/keychain_services/keychain_items/sharing_access_to_keychain_items_among_a_collection_of_apps)for details.

   To set up a keychain access group, do the following for each app:
   1. In Xcode, go to**Project settings \> Capabilities**.
   2. Enable Keychain Sharing.
   3. Add a keychain group identifier. Use the same identifier for all of the apps you want to share state.
2. In each app, set the access group to the keychain access group or app group you created in the previous step.

   ### Swift

       do {
         try Auth.auth().useUserAccessGroup("TEAMID.com.example.group1")
       } catch let error as NSError {
         print("Error changing user access group: %@", error)
       }

   ### Objective-C

       [FIRAuth.auth useUserAccessGroup:@"TEAMID.com.example.group1"
                                          error:nil];

3. In at least one app, sign in a user with any sign in method.

   ### Swift

       Auth.auth().signInAnonymously { result, error in
         // User signed in
       }

   ### Objective-C

       [FIRAuth signInAnonymouslyWithCompletion:^(FIRAuthDataResult *_Nullable result,
                                                  NSError *_Nullable error) {
         // User signed in
       }];

   The same current user is available in all apps in the access group.  

   ### Swift

       var user = Auth.auth().currentUser

   ### Objective-C

       FIRUser *user = FIRAuth.auth.currentUser;

## Switch back to an unshared keychain

1. Set the access group to`nil`to stop sharing auth state.

   ### Swift

       do {
         try Auth.auth().useUserAccessGroup(nil)
       } catch let error as NSError {
         print("Error changing user access group: %@", error)
       }

   ### Objective-C

       [FIRAuth.auth useUserAccessGroup:nil error:nil];

2. Sign in a user with any sign in method. The user state will not be available to any other apps.

   ### Swift

       Auth.auth().signInAnonymously { result, error in
         // User signed in
       }

   ### Objective-C

       [FIRAuth signInAnonymouslyWithCompletion:^(FIRAuthDataResult *_Nullable result,
                                          NSError *_Nullable error) {
         // User signed in
       }];

## Migrate a signed-in user to a shared keychain

To migrate a user who's already signed in to a shared state:

1. Make a reference to the current user for future use.

   ### Swift

       var user = Auth.auth().currentUser

   ### Objective-C

       FIRUser *user = FIRAuth.auth.currentUser;

   | **Note:** Switching from non-sharing to a shared keychain results in clearing the signed-in user. Switching from a shared to unshared keychain will not clear the signed-in user, even when no app uses that access group.
2. (Optional) Check the auth state of the access group you want to share.

   ### Swift

       let accessGroup = "TEAMID.com.example.group1"
       var tempUser: User?
       do {
         try tempUser = Auth.auth().getStoredUser(forAccessGroup: accessGroup)
       } catch let error as NSError {
         print("Error getting stored user: %@", error)
       }
       if tempUser != nil {
         // A user exists in the access group
       } else {
         // No user exists in the access group
       }

   ### Objective-C

       NSString *accessGroup = @"TEAMID.com.example.group1";
       FIRUser *tempUser = [FIRAuth getStoredUserForAccessGroup:accessGroup
                                                          error:nil];
       if (tempUser) {
         // A user exists in the access group
         } else {
         // No user exists in the access group
       }

3. Use an access group that you previously set in the project settings.

   ### Swift

       do {
         try Auth.auth().useUserAccessGroup(accessGroup)
       } catch let error as NSError {
         print("Error changing user access group: %@", error)
       }

   ### Objective-C

       [FIRAuth.auth useUserAccessGroup:accessGroup error:nil];

4. Update the current user.

   ### Swift

       Auth.auth().updateCurrentUser(user!) { error in
         // Error handling
       }

   ### Objective-C

       [FIRAuth.auth updateCurrentUser:user completion:^(NSError * _Nullable error) {
         // Error handling
       }];

   | **Note:** You will receive 2 notifications if you are listening to auth state changes on FIRAuth: first, it is triggered with nil (when switching to a new access group), and then triggered again with user (when`updateCurrentUser`is called). You can ignore these notifications.
5. The user now can be accessed by other apps that have access to the same access group.