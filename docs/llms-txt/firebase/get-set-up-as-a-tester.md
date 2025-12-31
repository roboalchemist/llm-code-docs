# Source: https://firebase.google.com/docs/app-distribution/get-set-up-as-a-tester.md.txt

<br />

iOS+Android  

<br />

When you first distribute an app using the[Firebaseconsole](https://firebase.google.com/docs/app-distribution/android/distribute-console)or a CLI tool ([Firebase CLI](https://firebase.google.com/docs/app-distribution/android/distribute-cli),[fastlane](https://firebase.google.com/docs/app-distribution/android/distribute-fastlane)),App Distributionemails the tester an invitation with instructions on how to install and test the build.

This guide describes how to install and test a new app distributed throughApp Distributionfrom a tester's point of view. For answers to frequently asked questions or help with troubleshooting, read the[troubleshooting guide](https://firebase.google.com/docs/app-distribution/troubleshooting).

## **Step 1**: Sign in with Google to accept the invitation

1. On an iOS device, open the email invitation in Safari. You must open the email invitation to properly install the Firebase profile and register your device in[Step 2](https://firebase.google.com/docs/app-distribution/get-set-up-as-a-tester#install-profile).

2. When prompted, sign in with Google and accept the invitation to test the app.

| **Keep the following in mind:**
|
| - After opening an invitation to test an app, you can sign in with any Google account to accept the invitation, not just the account to which the invitation was originally sent.
| - Invitations can only be accepted once before becoming invalid.
| - A Google account can be associated with any email address, not only addresses with Gmail or G Suite domains. Find out how to[sign in](https://support.google.com/accounts/answer/176347?co=GENIE.Platform%3DDesktop&hl=en&oco=1)with another email address.
Once you accept an invitation, you're given access to install the test app. You also receive build notification emails from Firebase when the app's developer distributes a new build and includes you as a tester.**Tip:** If you don't want to go through your email to accept new app invitations, you can also access your pending app invitations directly in theFirebase App Distributionweb clip:[appdistribution.firebase.google.com](http://appdistribution.firebase.google.com).

## **Step 2**: Install the Firebase profile

### Ad Hoc distributions

1. In the test app's page, tap**Register device**.
2. When prompted, download the Firebase profile, then install the profile in the**Settings**app.

Installing the profile gives Firebase permission to:

- Register the test device by collecting the device's unique device ID (UDID). If you're testing an Ad Hoc distribution, Firebase sends all Owners and Editors of the Firebase project an email that includes the test device's UDID , along with instructions on how to include the device in the app's provisioning profile so that the build can be tested on your device.
- Install aFirebase App Distributionweb clip to the test device's home screen. The web clip allows you to install and access all of your test apps.

### Enterprise distributions

This step is optional but recommended for testing Enterprise-signed distributions. The profile installation adds theFirebase App Distributionweb clip to your device's home screen, so you can install and access all your test apps. To manually install the profile:

1. Under**Test apps**, select the app you want to test.

2. In the top right of the app's page, tap*mobile_screen_share*.

3. Follow the instructions displayed to install the Firebase profile.

## **Step 3**: Install and test the build

### Ad Hoc distributions

After you register your device, the developer must update their provisioning profile with your device's UDID and redistribute a build that's configured to run on your device. Firebase emails you a notification when the build is available for you to install.
In the**Test apps** section of theFirebase App Distributionweb clip, select the app for which you want to install a new build, then tap**Download** . The build is downloaded to your device's home screen so you can start testing right away.  

### Enterprise distributions

1. In the**Test apps** section of theFirebase App Distributionweb clip, select the app for which you want to install a new build, then tap**Download** . The build is downloaded to your device's home screen so you can start testing right away.  
2. In the**Settings** app \>**Profiles \& Device Management**screen, select the app's developer name and trust it.

If you do not have theFirebase App Distributionweb clip, you can install a new build for your test app by tapping**Download the latest build**in the new build notification email from Firebase.

Finally, return to your device's home screen and open the test app.

## **Step 4**: (Optional) Enable new build alerts

If theFirebase App DistributionSDK has been added to your test app, you can optionally enable in-app alerts that appear when new builds are available to test. For more information about the SDK, including how to add it to a test app, refer to the Get Started guide.

1. From your device's home screen, open the test app.

2. When the**Enable alerts** dialogue appears, tap**Yes**.

   | **If you don't see the dialogue,** note the following:
   | - The dialogue may appear at a different point in your app, depending on where the developer implemented the feature.
   | - If the developer customized the dialogue, it may appear with different text, buttons, or other elements.
   | - Check that you have accepted terms on your test device when you accepted the invitation to test the app.
3. Sign in with the Google account you previously used in[Step 1](https://firebase.google.com/docs/app-distribution/get-set-up-as-a-tester#sign-in)(the account you used to accept the app's invitation). In-app alerts are turned on automatically.

   If you have trouble signing in to your Google account, visit the[troubleshooting guide](https://firebase.google.com/docs/app-distribution/troubleshooting#google-signin-ios).
4. Return to the test app. Now, you receive in-app alerts when new app versions are available for testing.

To download a new app version directly from an alert, tap**Update**in the alert dialogue. The new app version is downloaded and added to your device's home screen.

### Delete your tester account

To delete yourApp Distributiontester account and its data, see the[App Distributiontroubleshooting \& FAQ](https://firebase.google.com/docs/app-distribution/troubleshooting#delete-tester-account).