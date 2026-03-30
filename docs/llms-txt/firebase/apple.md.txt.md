# Source: https://firebase.google.com/docs/auth/cpp/apple.md.txt

You can let your users authenticate with Firebase using their Apple ID by
using the Firebase SDK to carry out the end-to-end OAuth 2.0 sign-in flow.
**Important**: To sign in with an Apple account, users must:

- Have an Apple ID with two-factor authentication (2FA) enabled.
- Be signed in to iCloud on an Apple device.

See [How
to use Sign in with Apple](https://support.apple.com/en-us/HT210318). You will also need to meet these requirements
to test your integration with Sign In with Apple.

## Before you begin

[Video](https://www.youtube.com/watch?v=HyiNbqLOCQ8)

To sign in users using Apple, first configure Sign In with Apple
on Apple's developer site, then enable Apple as a sign-in provider for your
Firebase project.

### Join the Apple Developer Program

Sign In with Apple can only be configured by members of the [Apple Developer
Program](https://developer.apple.com/programs/).

### Configure Sign In with Apple

Apple Sign In must be enabled and properly configured in your Firebase project. The configuration varies across Android and Apple platforms. Please follow the "Configure Sign In With Apple" section of the [Apple platforms](https://firebase.google.com/docs/auth/ios/apple#configure-sign-in-with-apple) and/or [Android](https://firebase.google.com/docs/auth/android/apple#configure-sign-in-with-apple) guides before proceeding.

### Enable Apple as a sign-in provider

1. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section. On the **Sign in method** tab, enable the **Apple** provider.
2. Configure the Apple Sign-in provider settings:
   1. If you're deploying your app only on Apple platforms, you can leave the Service ID, Apple Team ID, private key and key ID fields empty.
   2. For support on Android devices:
      1. [Add Firebase to your Android project](https://firebase.google.com/docs/android/setup). Be sure to register your app's SHA-1 signature when you set up your app in the Firebase console.
      2. In the [Firebase
         console](https://console.firebase.google.com/), open the **Auth** section. On the **Sign in method** tab, enable the **Apple** provider. Specify the Service ID you created in the previous section. Also, in the OAuth code flow configuration section, specify your Apple Team ID and the private key and key ID you created in the previous section.

<br />

## Comply with Apple anonymized data requirements

Sign In with Apple gives users the option of anonymizing their data,
including their email address, when signing in. Users who choose this option
have email addresses with the domain `privaterelay.appleid.com`. When
you use Sign In with Apple in your app, you must comply with any applicable
developer policies or terms from Apple regarding these anonymized Apple
IDs.

This includes obtaining any required user consent before you
associate any directly identifying personal information with an anonymized Apple
ID. When using Firebase Authentication, this may include the following
actions:

- Link an email address to an anonymized Apple ID or vice versa.
- Link a phone number to an anonymized Apple ID or vice versa
- Link a non-anonymous social credential (Facebook, Google, etc) to an anonymized Apple ID or vice versa.

The above list is not exhaustive. Refer to the Apple Developer Program
License Agreement in the Membership section of your developer account to make
sure your app meets Apple's requirements.

## Access the `firebase::auth::Auth` class

The `Auth` class is the gateway for all API calls.

1. Add the Auth and App header files:

   ```c++
   #include "firebase/app.h"
   #include "firebase/auth.h"
   ```
2. In your initialization code, create a [`firebase::App`](https://firebase.google.com/docs/reference/cpp/class/firebase/app) class.

   ```c++
   #if defined(__ANDROID__)
     firebase::App* app =
         firebase::App::Create(firebase::AppOptions(), my_jni_env, my_activity);
   #else
     firebase::App* app = firebase::App::Create(firebase::AppOptions());
   #endif  // defined(__ANDROID__)
   ```
3. Acquire the `firebase::auth::Auth` class for your `firebase::App`. There is a one-to-one mapping between `App` and `Auth`.

   ```c++
   firebase::auth::Auth* auth = firebase::auth::Auth::GetAuth(app);
   ```

## Handle the sign-in flow with the Firebase SDK

The process to Sign-in With Apple varies across Apple and Android platforms.

### On Apple platforms

Authenticate your users with Firebase via the Apple Sign In
Objective-C SDK invoked from your C++ code.

1. For every sign-in request, generate a random string---a
   "nonce"---which you will use to make sure the ID token you get was
   granted specifically in response to your app's authentication request. This
   step is important to prevent replay attacks.

         - (NSString *)randomNonce:(NSInteger)length {
           NSAssert(length > 0, @"Expected nonce to have positive length");
           NSString *characterSet = @"0123456789ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz-._";
           NSMutableString *result = [NSMutableString string];
           NSInteger remainingLength = length;

           while (remainingLength > 0) {
             NSMutableArray *randoms = [NSMutableArray arrayWithCapacity:16];
             for (NSInteger i = 0; i < 16; i++) {
               uint8_t random = 0;
               int errorCode = SecRandomCopyBytes(kSecRandomDefault, 1, &random);
               NSAssert(errorCode == errSecSuccess, @"Unable to generate nonce: OSStatus %i", errorCode);

               [randoms addObject:@(random)];
             }

             for (NSNumber *random in randoms) {
               if (remainingLength == 0) {
                 break;
               }

               if (random.unsignedIntValue < characterSet.length) {
                 unichar character = [characterSet characterAtIndex:random.unsignedIntValue];
                 [result appendFormat:@"%C", character];
                 remainingLength--;
               }
             }
           }
         }

   You will send the SHA256 hash of the nonce with your sign-in request, which
   Apple will pass unchanged in the response. Firebase validates the response
   by hashing the original nonce and comparing it to the value passed by Apple.
2. Start Apple's sign-in flow, including in your request the SHA256 hash of
   the nonce and the delegate class that will handle Apple's response (see
   the next step):

         - (void)startSignInWithAppleFlow {
           NSString *nonce = [self randomNonce:32];
           self.currentNonce = nonce;
           ASAuthorizationAppleIDProvider *appleIDProvider = [[ASAuthorizationAppleIDProvider alloc] init];
           ASAuthorizationAppleIDRequest *request = [appleIDProvider createRequest];
           request.requestedScopes = @[ASAuthorizationScopeFullName, ASAuthorizationScopeEmail];
           request.nonce = [self stringBySha256HashingString:nonce];

           ASAuthorizationController *authorizationController =
               [[ASAuthorizationController alloc] initWithAuthorizationRequests:@[request]];
           authorizationController.delegate = self;
           authorizationController.presentationContextProvider = self;
           [authorizationController performRequests];
         }

         - (NSString *)stringBySha256HashingString:(NSString *)input {
           const char *string = [input UTF8String];
           unsigned char result[CC_SHA256_DIGEST_LENGTH];
           CC_SHA256(string, (CC_LONG)strlen(string), result);

           NSMutableString *hashed = [NSMutableString stringWithCapacity:CC_SHA256_DIGEST_LENGTH * 2];
           for (NSInteger i = 0; i < CC_SHA256_DIGEST_LENGTH; i++) {
             [hashed appendFormat:@"%02x", result[i]];
           }
           return hashed;
         }

3. Handle Apple's response in your implementation of
   ASAuthorizationControllerDelegate\`. If sign-in was successful, use the ID
   token from Apple's response with the unhashed nonce to authenticate with
   Firebase:

         - (void)authorizationController:(ASAuthorizationController *)controller
            didCompleteWithAuthorization:(ASAuthorization *)authorization API_AVAILABLE(ios(13.0)) {
           if ([authorization.credential isKindOfClass:[ASAuthorizationAppleIDCredential class]]) {
             ASAuthorizationAppleIDCredential *appleIDCredential = authorization.credential;
             NSString *rawNonce = self.currentNonce;
             NSAssert(rawNonce != nil, @"Invalid state: A login callback was received, but no login request was sent.");

             if (appleIDCredential.identityToken == nil) {
               NSLog(@"Unable to fetch identity token.");
               return;
             }

             NSString *idToken = [[NSString alloc] initWithData:appleIDCredential.identityToken
                                                       encoding:NSUTF8StringEncoding];
             if (idToken == nil) {
               NSLog(@"Unable to serialize id token from data: %@", appleIDCredential.identityToken);
             }
           }

4. Use the resulting token string and original nonce to construct a Firebase
   Credential and sign into Firebase.

       firebase::auth::OAuthProvider::GetCredential(
               /*provider_id=*/"apple.com", token, nonce,
               /*access_token=*/nullptr);

       firebase::Future<firebase::auth::AuthResult> result =
           auth->SignInAndRetrieveDataWithCredential(credential);

5. The same pattern can be used with `Reauthenticate` which can be
   used to retrieve fresh credentials for sensitive operations that require
   recent login.

       firebase::Future<firebase::auth::AuthResult> result =
           user->Reauthenticate(credential);

6. The same pattern can be used to link an account with Apple Sign In.
   However, you may encounter an error when an existing Firebase account has
   already been linked to the Apple account you're attempting to link against.
   When this occurs the future will return a status of
   `kAuthErrorCredentialAlreadyInUse` and the `AuthResult` may contain a valid
   `credential`. This credential can be used to sign in the Apple-linked
   account via `SignInAndRetrieveDataWithCredential` without the need to
   generate another Apple Sign In token and nonce.

   ```c++
   firebase::Future<firebase::auth::AuthResult> link_result =
       auth->current_user().LinkWithCredential(credential);

   // To keep example simple, wait on the current thread until call completes.
   while (link_result.status() == firebase::kFutureStatusPending) {
     Wait(100);
   }

   // Determine the result of the link attempt
   if (link_result.error() == firebase::auth::kAuthErrorNone) {
     // user linked correctly.
   } else if (link_result.error() ==
                  firebase::auth::kAuthErrorCredentialAlreadyInUse &&
              link_result.result()
                  ->additional_user_info.updated_credential.is_valid()) {
     // Sign In with the new credential
     firebase::Future<firebase::auth::AuthResult> result =
         auth->SignInAndRetrieveDataWithCredential(
             link_result.result()->additional_user_info.updated_credential);
   } else {
     // Another link error occurred.
   }
   ```

### On Android

On Android, authenticate your users with Firebase by integrating web-based
generic OAuth Login into your app using the Firebase SDK to carry out the end to
end sign-in flow.

To handle the sign-in flow with the Firebase SDK, follow these steps:

1. Construct an instance of a `FederatedOAuthProviderData` configured with
   the provider ID appropriate for Apple.

       firebase::auth::FederatedOAuthProviderData provider_data("apple.com");

2. **Optional:** Specify additional OAuth 2.0 scopes beyond the default that you
   want to request from the authentication provider.

       provider_data.scopes.push_back("email");
       provider_data.scopes.push_back("name");

3. **Optional:** If you want to display Apple's sign-in screen in a language
   other than English, set the `locale` parameter. See the
   [Sign In with Apple docs](https://developer.apple.com/documentation/signinwithapplejs/incorporating_sign_in_with_apple_into_other_platforms#3332112)
   for the supported locales.

       // Localize to French.
       provider_data.custom_parameters["language"] = "fr";
       ```

4. Once your provider data has been configured, use it to create a
   FederatedOAuthProvider.

       // Construct a FederatedOAuthProvider for use in Auth methods.
       firebase::auth::FederatedOAuthProvider provider(provider_data);

5. Authenticate with Firebase using the Auth provider object. Note that unlike
   other FirebaseAuth operations, this will take control of your UI by popping
   up a web view in which the user can enter their credentials.

   To start the sign in flow, call `signInWithProvider`:

       firebase::Future<firebase::auth::AuthResult> result =
         auth->SignInWithProvider(provider_data);

   Your application may then wait or [register a callback on the Future](https://firebase.google.com/docs/auth/cpp/apple#register_callback_on_future).
6. The same pattern can be used with `ReauthenticateWithProvider` which can be
   used to retrieve fresh credentials for sensitive operations that require
   recent login.

       firebase::Future<firebase::auth::AuthResult> result =
         user.ReauthenticateWithProvider(provider_data);

   Your application may then wait or [register a callback on
   the Future](https://firebase.google.com/docs/auth/cpp/apple#register_callback_on_future).
7. And, you can use `LinkWithCredential()` to link different identity providers
   to existing accounts.

   Note that Apple requires you to get explicit consent from users before you
   link their Apple accounts to other data.

   For example, to link a Facebook account to the current Firebase account, use
   the access token you got from signing the user in to Facebook:

       // Initialize a Facebook credential with a Facebook access token.
       AuthCredential credential =
           firebase::auth::FacebookAuthProvider.getCredential(token);

       // Assuming the current user is an Apple user linking a Facebook provider.
       firebase::Future<firebase::auth::AuthResult> result =
           auth.current_user().LinkWithCredential(credential);

### Sign in with Apple Notes

Unlike other providers supported by Firebase Auth, Apple does not provide a
photo URL.

Also, when the user chooses not to share their email with the app, Apple
provisions a unique email address for that user (of the form
`xyz@privaterelay.appleid.com`), which it shares with your app. If you
configured the private email relay service, Apple forwards emails sent to
the anonymized address to the user's real email address.

Apple only shares user information such as the display name with apps the
first time a user signs in. Usually, Firebase stores the display name the
first time a user signs in with Apple, which you can get with
`current_user().display_name()`. However, if you previously used Apple to sign a
user in to the app without using Firebase, Apple will not provide Firebase with
the user's display name.

## Next steps

After a user signs in for the first time, a new user account is created and linked to the credentials---that is, the user name and password, phone number, or auth provider information---the user signed in with. This new account is stored as part of your Firebase project, and can be used to identify a user across every app in your project, regardless of how the user signs in.

<br />

In your apps, you can get the user's basic profile information from the
`firebase::auth::User` object. See
[Manage Users](https://firebase.google.com/docs/auth/cpp/manage-users).

In your Firebase Realtime Database and Cloud Storage Security Rules, you can get
the signed-in user's unique user ID from the auth variable, and use it to
control what data a user can access.