# Source: https://firebase.google.com/docs/auth/unity/phone-auth.md.txt

You can use Firebase Authentication to sign in a user by sending an SMS message
to the user's phone. The user signs in using a one-time code contained in the
SMS message.

This document describes how to implement a phone number sign-in flow using
the Firebase SDK.
Phone numbers that end users provide for authentication will be sent and stored by Google to improve our spam and abuse prevention across Google services, including but not limited to Firebase. Developers should ensure they have appropriate end-user consent prior to using the Firebase Authentication phone number sign-in service.

## Before you begin

1. Before you can use
   [Firebase Authentication](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth),
   you need to add the [Firebase Unity SDK](https://firebase.google.com/download/unity) (specifically,
   `FirebaseAuth.unitypackage`) to your Unity project.

   **Find detailed instructions for these initial setup steps in
   [Add Firebase to your Unity
   project](https://firebase.google.com/docs/unity/setup#set_up_environment).**
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

## Start receiving APNs notifications (iOS only)

To use phone number authentication on iOS, your app must be able to receive
APNs notifications from Firebase. When you sign in a user with their phone
number for the first time on a device, Firebase Authentication sends a silent push
notification to the device to verify that the phone number sign-in request comes
from your app. (For this reason, phone number sign-in cannot be used on a
simulator.)

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
`PhoneAuthProvider.VerifyPhoneNumber` to request that Firebase
send an authentication code to the user's phone by SMS:

1. Get the user's phone number.

   Legal requirements vary, but as a best practice
   and to set expectations for your users, you should inform them that if they use
   phone sign-in, they might receive an SMS message for verification and standard
   rates apply.
2. Call `PhoneAuthProvider.VerifyPhoneNumber`, passing to it a PhoneAuthOptions containing the user's phone number.

   ```c#
   PhoneAuthProvider provider = PhoneAuthProvider.GetInstance(firebaseAuth);
   provider.VerifyPhoneNumber(
     new Firebase.Auth.PhoneAuthOptions {
       PhoneNumber = phoneNumber,
       TimeoutInMilliseconds = phoneAuthTimeoutMs,
       ForceResendingToken = null
     },
     verificationCompleted: (credential) =&gt {
       // Auto-sms-retrieval or instant validation has succeeded (Android only).
       // There is no need to input the verification code.
       // `credential` can be used instead of calling GetCredential().
     },
     verificationFailed: (error) =&gt {
       // The verification code was not sent.
       // `error` contains a human readable explanation of the problem.
     },
     codeSent: (id, token) =&gt {
       // Verification code was successfully sent via SMS.
       // `id` contains the verification id that will need to passed in with
       // the code from the user when calling GetCredential().
       // `token` can be used if the user requests the code be sent again, to
       // tie the two requests together.
     },
     codeAutoRetrievalTimeout: (id) =&gt {
       // Called when the auto-sms-retrieval has timed out, based on the given
       // timeout parameter.
       // `id` contains the verification id of the request that timed out.
     });
   ```

   > [!NOTE]
   > **Note:** See [Firebase Authentication
   > Limits](https://firebase.google.com/docs/auth/limits#phone-auth) for applicable usage limits and quotas.

   When you call `PhoneAuthProvider.VerifyPhoneNumber`, Firebase,
   - (on iOS), sends a silent push notification to your app.
   - Firebase sends an SMS message containing an authentication code to the specified phone number and passes a verification ID to your completion function. You will need both the verification code and the verification ID to sign in the user.
3. Save the verification ID and restore it when your app loads. By doing so,
   you can ensure that you still have a valid verification ID if your app is
   terminated before the user completes the sign-in flow (for example, while
   switching to the SMS app).

   You can persist the verification ID any way you want. A simple way is to
   save the verification ID with `UnityEngine.PlayerPrefs`.

If the callback passed in to `codeSent` is called, you can
prompt the user to type the verification code when they receive it in the SMS
message.

On the other hand, if the callback for `verificationCompleted` is
called, then automatic verification has succeeded and you will now have a
`PhoneAuthCredential` with which you can use as described below.


> [!NOTE]
> To prevent abuse, Firebase enforces a limit on the number of SMS messages that can be sent to a single phone number within a period of time. If you exceed this limit, phone number verification requests might be throttled. If you encounter this issue during development, use a different phone number for testing, or try the request again later.

## Sign in the user with the verification code

After the user provides your app with the verification code from the SMS
message, sign the user in by creating a `PhoneAuthCredential`
object from the verification code and verification ID and passing that object
to `FirebaseAuth.SignInAndRetrieveDataWithCredentialAsync`.

1. Get the verification code from the user.
2. Create a `Credential` object from the verification code and verification ID.

   ```c#
   PhoneAuthCredential credential =
       phoneAuthProvider.GetCredential(verificationId, verificationCode);
       
   ```
3. Sign in the user with the `PhoneAuthCredential` object:

   ```c#
   auth.SignInAndRetrieveDataWithCredentialAsync(credential).ContinueWith(task =&gt {
     if (task.IsFaulted) {
       Debug.LogError("SignInAndRetrieveDataWithCredentialAsync encountered an error: " +
                      task.Exception);
       return;
     }

     FirebaseUser newUser = task.Result.User;
     Debug.Log("User signed in successfully");
     // This should display the phone number.
     Debug.Log("Phone number: " + newUser.PhoneNumber);
     // The phone number providerID is 'phone'.
     Debug.Log("Phone provider ID: " + newUser.ProviderId);
   });
   ```

## Next steps

After a user signs in for the first time, a new user account is created and
linked to the credentials---that is, the user name and password, phone
number, or auth provider information---the user signed in with. This new
account is stored as part of your Firebase project, and can be used to identify
a user across every app in your project, regardless of how the user signs in.

- In your apps, you can get the user's basic profile information from the
  [`Firebase.Auth.FirebaseUser`](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user) object:

  ```c#
  Firebase.Auth.FirebaseUser user = auth.CurrentUser;
  if (user != null) {
    string name = user.DisplayName;
    string email = user.Email;
    System.Uri photo_url = user.PhotoUrl;
    // The user's Id, unique to the Firebase project.
    // Do NOT use this value to authenticate with your backend server, if you
    // have one; use User.TokenAsync() instead.
    string uid = user.UserId;
  }
  ```
- In your Firebase Realtime Database and Cloud Storage
  [Security Rules](https://firebase.google.com/docs/database/security/user-security), you can
  get the signed-in user's unique user ID from the `auth` variable,
  and use it to control what data a user can access.

You can allow users to sign in to your app using multiple authentication
providers by [linking auth provider credentials to an
existing user account.](https://firebase.google.com/docs/auth/unity/account-linking)

To sign out a user, call [`SignOut()`](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#signout):

```c#
auth.SignOut();
```