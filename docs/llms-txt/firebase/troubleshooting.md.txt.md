# Source: https://firebase.google.com/docs/app-distribution/troubleshooting.md.txt

<button value="ios" default="">iOS+</button> <button value="android">Android</button>

<br />

This page provides troubleshooting help and answers to frequently asked
questions about distributing and testing apps with App Distribution.

## Distributing apps

Use the following tips to troubleshoot issues that you might encounter when
distributing apps to your testers.

<br />

### Unable to distribute an app due to a missing contact email

<br />

When uploading an app, you might encounter this error:

"We could not find a contact email for app `<app-id>`. Please visit
App Distribution within the Firebase console to set one up."

Set a Contact Email in the Firebase console, if available. If the issue
persists, contact [Firebase Support](https://firebase.google.com/support).

<br />

<br />

<br />

### There was an error provisioning your app (400, 409, or 500 errors )

<br />

If you repeatedly encounter errors 400, 409, or 500 during provisioning,
contact [Firebase Support](https://firebase.google.com/support). Provide
Support with your Firebase project number and app identifier.

<br />

<br />

<br />

### Unable to upload the IPA

<br />

The following is an example of a browser network response:

    {
    "status": "IN_PROGRESS",
      "message": "There was an error processing your
    distribution. Ensure you are uploading a valid IPA or APK and try again."
    }

To resolve this issue, follow these steps:

1. Verify the size of the IPA. The maximum file size limit for all binaries is
   2048 MiB, which is a little over 2 GB.

2. If the IPA size is within the file size limit and is reproducible, follow
   these steps:

   1. Check your `Info.plist` file and confirm whether `CFBundleDisplayName`
      contains any `<array>` delimiters.

      > [!NOTE]
      > **Note:** App Distribution doesn't accept `CFBundleDisplayName` values that are arrays.

   2. Remove the `<array>` delimiters and rebuild your app. The upload should
      succeed.

   3. If you are still experiencing issues, contact [Firebase Support](https://firebase.google.com/support).

3. If the IPA size is over the file size limit, make any necessary changes to
   decrease the file size.

4. If decreasing the IPA file size doesn't resolve the issue, contact
   [Firebase Support](https://firebase.google.com/support) and ask about using
   [Testflight](https://testflight.apple.com/).

<br />

<br />

## Installing and testing apps

Use the following tips to troubleshoot issues that your testers might
encounter when they install and test your apps.

<br />

### Tester doesn't have a Google account

<br />

When a user creates a Google account, they automatically receive a Gmail address.

If a tester doesn't have a Google Workspace or Gmail address, or if they would
rather use another email address to sign in, ask the tester to link a non-Gmail
email address to the account and use that email to sign in.

When choosing an alternate email, the tester must follow these guidelines:

- Don't use a Gmail address.
- Don't use an email address that's already linked to another Google account.
- Remember to use your Google Account password when signing in with this email address.

For more information, see [Sign in to your Google Account with another email address](https://support.google.com/accounts/answer/176347).

<br />

<br />

<br />

### Tester unable to see the right apps or builds

<br />

If the tester accepted the email invitation with a different email address than
the invite was sent to, the tester might not be able to see the right apps or
builds.

The email that the developer sends invitations to and adds to new builds
(Email A) can be different from the email that the tester uses to accept the
invitation (Email B). This creates a link behind the scenes. Whenever Email A
is added to new builds, it's actually Email B that's getting access.

If the tester accepted the email invitation with a different email address,
follow these steps to resolve the issue:

1. Delete the tester from the **View all testers** section of the **Testers \& Groups** tab in the App Distribution
   page of the Firebase console. Existing invitations are removed.

2. Re-invite the tester to test your app. The tester should receive an
   invitation email.

3. Make sure that the tester accepts the invitation with the same email address.

<br />

<br />

<br />

### Tester isn't receiving email notifications

<br />

Testers might not receive email notifications if one of the following occurs:

- Email notifications are sent to spam folders.

- Email filters are set.

- The invite was sent to one email account, but the tester accepted with a
  different email account. The tester receives new release emails for the
  email account to which the invitation was originally sent.

- The tester was previously invited but did not accept the initial invitation.
  If the tester is added to subsequent releases, App Distribution won't
  automatically send release notifications to that tester because the tester
  didn't accept the initial invitation.

**Solution 1**

1. Ask the tester to check their spam folder and any email filters they set in
   their email service.

2. If the tester unsubscribed from the emails, ask the tester to do the
   following:

   1. Find an email that the tester previously received from the app.
   2. Click **Manage email settings** at the bottom and click **Allow emails** to resubscribe.

**Solution 2**

If the tester doesn't care about getting email notifications and just wants to
be able to accept app invitations, they can view pending app invitations
directly in the Firebase App Distribution web clip:
[appdistribution.firebase.google.com](http://appdistribution.firebase.google.com).

> [!NOTE]
> **Note:** In order to see pending app invitations, the email address of the Google account the tester uses to login to the web clip must match the recipient email address of the invitation from the developer.

**Solution 3**

1. Delete the tester from the **View all testers** section of the **Testers \& Groups** tab in the App Distribution
   page in the Firebase console. This action removes existing invitations.

2. Re-invite the tester to test your app. The tester should receive an
   invitation email. Make sure that the tester accepts the invitation with the
   same email address that the invitation was sent to.

<br />

<br />

<br />

### "Untrusted Enterprise Developer" error when trying to run test app

<br />

The **Untrusted Enterprise Developer** error appears if you did not
trust the developer certificate on the test device before opening the app.
In the **Settings** app \> **Profiles \& Device Management** screen, select the
app's developer name and trust it.

<br />

<br />

<br />

### "Developer Mode Required" error when trying to run test app

<br />

The Developer Mode Required error appears when you try to launch an ad
hoc-provisioned iOS app on iOS 16 or later without first enabling Developer
Mode.

To enable Developer Mode and resolve this error, follow these steps:

1. On your iPhone, open the Settings app and then tap **Privacy \& Security**.
2. Scroll down to Security and tap **Developer Mode**.
3. Tap the **Developer Mode** slider.
4. Tap **Restart**.
5. After the device restarts, unlock the device. The Turn on Developer Mode? dialog appears.
6. Tap **Turn On**. You can now launch your app and start testing.

<br />

<br />

<br />

### "Device registered, you're all set! You'll get an email when the app is ready to test"

<br />

If you're installing an Ad Hoc distribution, this message appears when the
developer hasn't yet configured their app to run on your test device.
To make the app available to you, the developer must
complete the instructions in [Register additional devices](https://firebase.google.com/docs/app-distribution/register-additional-devices).

> [!NOTE]
> **Note:** If the developer already distributed a build with the same build number and version, only users of newly-registered devices will receive email notifications.

<br />

<br />

<br />

### Google account doesn't have access to test app

<br />

If your Google account does not have access to a test app you previously
installed (or accepted an invitation for), it's likely that you signed
in to the wrong Google account. The apps to which you have access
are associated with the Google account you used when you first accepted the
invitation to test the app. Try again by signing in with the Google account
you previously used to accept the invitation.

> [!NOTE]
> **Keep the following in mind:**
>
> - The Google account you used to accept the invitation **may not** be the same as the Google account to which the invitation was originally sent.
> - A Google account can be associated with any email address, not only addresses with Gmail or G Suite domains. Find out how to [sign in](https://support.google.com/accounts/answer/176347?co=GENIE.Platform%3DDesktop&hl=en&oco=1) with another email address.

<br />

<br />

<br />

### 403 error: "Contact your admin for access"

<br />

When you encounter a 403 error, this means that the account you're using doesn't have permission to install and test apps. Access is determined by the administrator of your account's domain in Google Workspace.

If you believe you should have permission to install and test apps, ask your Google Workspace account admin to change your account settings. Your admin should follow the instructions in [Manage access to services that aren't controlled individually](https://support.google.com/a/answer/7646040).

If you have multiple accounts, try logging in with a different account that is not restricted from installing and testing apps.

<br />

<br />

## Enabling in-app alerts with the App Distribution iOS SDK

Use the following tips to troubleshoot issues that involve
enabling in-app new build alerts using the App Distribution iOS SDK.

<br />

### Tester isn't receiving in-app alerts

<br />

If you have already set up the App Distribution iOS SDK in your app and your
testers aren't receiving in-app alerts, check to make sure your app is
fetching new releases:

1. Enable debug mode in your app. To learn how, see the
   [Google Analytics documentation](https://firebase.google.com/docs/analytics/debugview#enabling_debug_mode).

2. Run your app in a simulator and search for the string "\[Firebase/AppDistribution\]".

3. Check that the tester has access to the new release:

   - If a valid release object is returned, it's likely that there's an
     issue in the View Controller lifecycle where the alert dialog is
     loaded before the View appears.

     > [!NOTE]
     > **Note:** The App Distribution iOS SDK does not display an alert dialog by default. You must specify how and where the dialog is displayed in your app. To learn more, see [Basic alert configuration](https://firebase.google.com/docs/app-distribution/set-up-alerts#basic-config).

   - If no release is returned, your tester may not yet be associated with
     the new release. In the App Distribution dashboard of the
     Firebase console, make sure your tester is included in your build
     distribution and is in the **Accepted** state.

     If your tester still isn't receiving updates, ask them to follow the
     tips below to make sure they accepted the invitation to test your
     app and that they set up their testing device properly:
     1. On the test device, sign into the Firebase App Distribution web
        clip. Remember to select the Google account you first used when you
        accepted the invitation to test the app.

     2. Make sure that the new app release is available in the web clip.

<br />

<br />

<br />

### Tester prompted to sign in again after closing app

<br />

By default, your testers only need to sign in to their Google account once to
enable new build alerts and to install new builds. If your testers are being
prompted to sign in again after closing and re-opening your app, follow these
tips to make sure your App Distribution configuration is set up properly:

- Check to make sure you've enabled the Firebase App Testers API. For more
  information, see [Enable the App Distribution Tester API](https://firebase.google.com/docs/app-distribution/ios/set-up-alerts#enable-api).

- Under **Key restrictions**, make sure that the Firebase App Testers API is
  included in the list of allowed APIs.

- If you typically clear UserDefaults on signing out, you may be clearing
  your tester's state. App Distribution stores a flag that indicates whether
  your tester has already signed into the app. For more information, see the
  [GitHub repository](https://github.com/firebase/firebase-ios-sdk/blob/master/FirebaseAppDistribution/Sources/FIRAppDistribution.m#L58).

<br />

<br />

## Frequently asked questions

<br />

### Are there limits for adding testers to my app?

<br />

Firebase App Distribution has the following tester limits:

- Add a maximum of 500 testers to a Firebase project

- Add a maximum of 200 testers to an App Distribution group

To add more testers, request a no-cost
[limit increase](https://console.firebase.google.com/project/_/appdistribution/limits).

<br />

<br />

<br />

### Do my tester invitations expire?

<br />

Testers have 30 days to accept an invitation to test the app before it expires.
When an invitation is 5 days from expiring, an expiration notice appears in the
Firebase console next to the tester on a release. An invitation can be renewed
by resending it via the drop-down menu on the tester row.

<br />

<br />

<br />

### When is a new release created for iOS uploads?

<br />

See [Register additional devices](https://firebase.google.com/docs/app-distribution/register-additional-devices).

<br />

<br />

<br />

### How long are app releases available?

<br />

App releases are removed from App Distribution if one of the following
conditions occurs:

- The app release is older than 150 days.
- You exceed the 1,000 app release limit, and the app release is older than the 1,000 most recent app releases.

For more information, see [App Distribution supports a maximum of 1,000 releases](https://firebase.google.com/docs/app-distribution/troubleshooting#release-limits).

After the app reaches or exceeds the 150-day expiration limit or the 1,000 app
release limit, the release is removed from the App Distribution dashboard and the
App Distribution tester web app. If your tester has installed the release, the local
version of the app continues to run.

To keep the app release available longer, use one of the following recommendations:

- Before the app release expires or exceeds the release limit, download the IPA and delete the release from the App Distribution dashboard. Then, re-upload the IPA as a new build to App Distribution.
- Download the release and upload it to [Cloud Storage](https://cloud.google.com/storage) for long-term archiving.

### App releases expire after 150 days

When you upload a release of your app to Firebase, the release appears in the
[App Distribution dashboard](https://console.firebase.google.com/project/_/appdistribution)
for 150 days, starting from the upload date. After you upload the release, you
can distribute it to testers, who install the release from the App Distribution
tester web app on their testing device.

When the release is 30 days from the expiration date, an app release
expiration notification appears on your release in the App Distribution page
of the Firebase console and in the App Distribution tester web app.

### App Distribution supports a maximum of 1,000 releases

App Distribution allows a maximum of
1,000 releases per app. When your app reaches the 1,000 app release limit,
App Distribution automatically deletes the oldest
releases above the limit.

If you want to manually manage your app releases, use the App Distribution REST API
to [list](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/list)
and [delete](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/batchDelete)
app releases in bulk.

If you have questions, contact [Firebase Support](https://firebase.google.com/support).

<br />

<br />

<br />

### What is the Firebase profile?

<br />

The Firebase profile is a configuration profile that allows App Distribution to:

- Register the test device by collecting the device's unique device ID
  (UDID). If you're testing an Ad Hoc distribution, Firebase sends the app
  developer an email that includes the test device's UDID, along with
  instructions on how to include the device in the app's provisioning
  profile so that the build can be tested on your device.

- Install a Firebase App Distribution web clip to your device's home
  screen. The web clip allows you to install and access all your test apps in
  one place. New builds you're invited to test are
  automatically added to the web clip.

For help on installing configuration profiles on your iOS device, refer to
[Apple's documentation](https://support.apple.com/en-us/HT209435).

<br />

<br />

<br />

### How can I access test apps I installed on my device?

<br />

If you're a tester, you can access all of your test apps with the
**Firebase App Distribution web clip** , which is automatically added to your test
device's home screen when you install the Firebase profile. If you're testing an
Ad Hoc distribution, you must first
[install the profile](https://firebase.google.com/docs/app-distribution/ios/set-up-for-testing?auto_signin=false#install-profile)
before you can test the app.

If you're testing an
Enterprise distribution, you can manually install the profile:

1. If you haven't already, sign in to Google and accept the invitation.

2. Under **Test apps**, select the app you want to test.

3. In the top right of the app's page, tap .

4. Follow the instructions displayed to install the Firebase profile.

<br />

<br />

<br />

### How do I delete my tester account?

<br />

To delete your App Distribution tester account and its associated data,
follow these steps in order:

1. Visit <https://appdistribution.firebase.google.com>
   and sign in with your Google account.

2. In the top-right, click (**Manage account**)

   > **Delete account**.
3. Optional: In your [Google account permissions](https://myaccount.google.com/permissions),
   revoke access from Firebase App Distribution. Note that revoking access without
   first deleting your App Distribution account *does not* delete your tester
   account or data.

<br />

<br />