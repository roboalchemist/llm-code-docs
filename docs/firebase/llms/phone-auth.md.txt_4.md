# Source: https://firebase.google.com/docs/auth/cpp/phone-auth.md.txt

You can use Firebase Authentication to sign in a user by sending an SMS message
to the user's phone. The user signs in using a one-time code contained in the
SMS message.

This document describes how to implement a phone number sign-in flow using
the Firebase SDK.
Phone numbers that end users provide for authentication will be sent and stored by Google to improve our spam and abuse prevention across Google services, including but not limited to Firebase. Developers should ensure they have appropriate end-user consent prior to using the Firebase Authentication phone number sign-in service.

## Before you begin

1. [Add Firebase to your C++
   project](https://firebase.google.com/docs/cpp/setup#note_select_platform).
2. If you haven't yet connected your app to your Firebase project, do so from the [Firebase console](https://console.firebase.google.com/).
3. Understand the platform requirements for Phone Number sign-in:
   - Phone Number sign-in is for mobile platforms only.
   - On iOS, Phone Number sign-in requires a physical device and won't work on a simulator.

### Security concerns

Authentication using only a phone number, while convenient, is less secure
than the other available methods, because possession of a phone number
can be easily transferred between users. Also, on devices with multiple user
profiles, any user that can receive SMS messages can sign in to an account using
the device's phone number.

If you use phone number based sign-in in your app, you should offer it
alongside more secure sign-in methods, and inform users of the security
tradeoffs of using phone number sign-in.

## Enable Phone Number sign-in for your Firebase project

To sign in users by SMS, you must first enable the Phone Number sign-in
method for your Firebase project:

1. In the [Firebase console](https://console.firebase.google.com/), open the **Authentication** section.
2. On the **Sign-in Method** page, enable the **Phone Number** sign-in method.
3. On the **Settings** page, set a policy on the regions to which you want to allow or deny SMS messages to be sent. For new projects, the default policy allows no regions.

## Start receiving APNs notifications (Apple platforms)

To use phone number authentication on Apple platforms, your app must be able to receive
APNs notifications from Firebase. When you sign in a user with their phone
number for the first time on a device, Firebase Authentication sends a silent push
notification to the device to verify that the phone number sign-in request
comes from your app. (For this reason, phone number sign-in cannot be used
on a simulator.)

To enable APNs notifications for use with Firebase Authentication:

1. In Xcode, [enable push notifications](http://help.apple.com/xcode/mac/current/#/dev11b059073?sub=dev73a37248c) for your project.
2.
   Upload your APNs certificate to Firebase.
   If you don't already have an APNs certificate, make sure to create one in the
   [Apple Developer Member Center](https://developer.apple.com/membercenter/index.action).

   1.
      Inside your project in the Firebase console, select the
      gear icon, select
      **Project Settings** , and then select the
      **Cloud Messaging** tab.

   2.
      Select the **Upload Certificate**
      button for your development certificate, your
      production certificate, or both. At least one is
      required.

   3.
      For each certificate, select the .p12 file, and provide
      the password, if any. Make sure the bundle ID for this certificate
      matches the bundle ID of your app. Select
      **Save**.

## Send a verification code to the user's phone

To initiate phone number sign-in, present the user an interface that prompts
them to provide their phone number, and then call
`PhoneAuthProvider::VerifyPhoneNumber` to request that Firebase send an
authentication code to the user's phone by SMS:

1. Get the user's phone number.

   Legal requirements vary, but as a best practice
   and to set expectations for your users, you should inform them that if they use
   phone sign-in, they might receive an SMS message for verification and standard
   rates apply.
2. Call `PhoneAuthProvider::VerifyPhoneNumber`, passing to it the user's phone number.

   ```c++
   class PhoneListener : public PhoneAuthProvider::Listener {
    public:
     ~PhoneListener() override {}

     void OnVerificationCompleted(PhoneAuthCredential credential) override {
       // Auto-sms-retrieval or instant validation has succeeded (Android only).
       // No need for the user to input the verification code manually.
       // `credential` can be used instead of calling GetCredential().
     }

     void OnVerificationFailed(const std::string& error) override {
       // Verification code not sent.
     }

     void OnCodeSent(const std::string& verification_id,
                     const PhoneAuthProvider::ForceResendingToken&
                         force_resending_token) override {
       // Verification code successfully sent via SMS.
       // Show the Screen to enter the Code.
       // Developer may want to save that verification_id along with other app states in case
       // the app is terminated before the user gets the SMS verification code.
     }
   };

   PhoneListener phone_listener;
   PhoneAuhtOptions options;
   options.timeout_milliseconds = kAutoVerifyTimeOut;
   options.phone_number = phone_number;
   PhoneAuthProvider& phone_provider = PhoneAuthProvider::GetInstance(auth);
   phone_provider->VerifyPhoneNumber(options, &phone_listener);
   ```
   When you call `PhoneAuthProvider::VerifyPhoneNumber`, Firebase,
   - (on iOS) sends a silent push notification to your app,
   - sends an SMS message containing an authentication code to the specified phone number and passes a verification ID to your completion function. You will need both the verification code and the verification ID to sign in the user.

     > [!NOTE]
     > **Note:** See [Firebase Authentication
     > Limits](https://firebase.google.com/docs/auth/limits#phone-auth) for applicable usage limits and quotas.

3. Save the verification ID and restore it when your app loads. By doing so,
   you can ensure that you still have a valid verification ID if your app is
   terminated before the user completes the sign-in flow (for example, while
   switching to the SMS app).

   You can persist the verification ID any way you want. If you're writing
   with a cross-platform C++ framework, it should provide notifications for app
   termination and restoration. On these events, you can save and restore,
   respectively, the verification ID.

If the call to `VerifyPhoneNumber` results in `OnCodeSent`
being called on your Listener, you can prompt the user to type the verification
code when they receive it in the SMS message.

On the other hand, if the call to `VerifyPhoneNumber` results in
`OnVerificationCompleted`, then automatic verification has succeeded
and you will now have a `PhoneAuthCredential` with which you can use as described
below.


> [!NOTE]
> To prevent abuse, Firebase enforces a limit on the number of SMS messages that can be sent to a single phone number within a period of time. If you exceed this limit, phone number verification requests might be throttled. If you encounter this issue during development, use a different phone number for testing, or try the request again later.

## Sign in the user with the verification code

After the user provides your app with the verification code from the SMS
message, sign the user in by creating a `PhoneAuthCredential`
object from the verification code and verification ID and passing that object
to `Auth::SignInWithCredential`.

1. Get the verification code from the user.
2. Create a `Credential` object from the verification code and verification ID.

   ```c++
   PhoneAuthCredential credential = phone_auth_provider->GetCredential(
       verification_id_.c_str(), verification_code.c_str());
       
   ```
3. Sign in the user with the `Credential` object:

   ```c++
   Future<User> future = auth_->SignInWithCredential(credential);
   future.OnCompletion(
       [](const Future<User*>& result, void*) {
         if (result.error() == kAuthErrorNone) {
           // Successful.
           // User is signed in.
           User user = *result.result();

           // This should display the phone number.
           printf("Phone number: %s", user.phone_number().c_str());

           // The phone number provider UID is the phone number itself.
           printf("Phone provider uid: %s", user.uid().c_str());

           // The phone number providerID is 'phone'
           printf("Phone provider ID: %s", user.provider_id().c_str());
         } else {
           // Error.
           printf("Sign in error: %s", result.error_message().c_str());
         }
       },
       nullptr);
   ```

## Next steps

After a user signs in for the first time, a new user account is created and
linked to the credentials---that is, the user name and password, phone
number, or auth provider information---the user signed in with. This new
account is stored as part of your Firebase project, and can be used to identify
a user across every app in your project, regardless of how the user signs in.

- In your apps, you can get the user's basic profile information from the
  [`firebase::auth::User`](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user) object:

  ```c++
  firebase::auth::User user = auth->current_user();
  if (user.is_valid()) {
    std::string name = user.display_name();
    std::string email = user.email();
    std::string photo_url = user.photo_url();
    // The user's ID, unique to the Firebase project.
    // Do NOT use this value to authenticate with your backend server,
    // if you have one. Use firebase::auth::User::Token() instead.
    std::string uid = user.uid();
  }
  ```
- In your Firebase Realtime Database and Cloud Storage
  [Security Rules](https://firebase.google.com/docs/database/security/user-security), you can
  get the signed-in user's unique user ID from the `auth` variable,
  and use it to control what data a user can access.

You can allow users to sign in to your app using multiple authentication
providers by [linking auth provider credentials to an
existing user account.](https://firebase.google.com/docs/auth/cpp/account-linking)

To sign out a user, call [`SignOut()`](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#signout):

```c++
auth->SignOut();
```