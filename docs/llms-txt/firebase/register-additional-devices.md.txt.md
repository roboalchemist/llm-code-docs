# Source: https://firebase.google.com/docs/app-distribution/register-additional-devices.md.txt

If you want to distribute ad hoc iOS builds using App Distribution, you must follow
this guide to register your testers' devices. An [*ad hoc
build*](https://help.apple.com/xcode/mac/current/#/dev31de635e5)
is a build not signed with an Enterprise profile. A device can only install an
ad hoc build if the device's unique device identifier (UDID) is included in the
build's provisioning profile.

When a tester accepts an invitation to test your app, App Distribution requests
permission to share the tester's device identifier with you, the developer.
Before downloading an ad hoc build, App Distribution asks the tester to register
their device. If the tester registers their device, App Distribution collects the
UDID from the device and notifies you of the UDID by email.

When you receive an email containing a UDID, update your provisioning profile
with the UDID and distribute a new build to your testers. You can manually
export UDIDs using the [Firebase console or Firebase
CLI](https://firebase.google.com/docs/app-distribution/register-additional-devices#manual-export-udids), or you can programmatically export UDIDs using
[fastlane](https://firebase.google.com/docs/app-distribution/register-additional-devices#programmatic-export-udids).

## Manually export UDIDs

1. Add the devices to your Apple developer portal.
   - *Option 1: *Import the device UDIDs as a CSV file.

     In the **Testers \& Groups** tab of the App Distribution dashboard, select
     **All testers** , then click **Export Apple UDIDs**
     to download a CSV file. Next, import the file into your
     [Apple developer account](https://developer.apple.com/account/resources/devices/add)
     using the **Register Multiple Devices** option. To learn more, see
     [Distributing your app to registered devices](https://developer.apple.com/documentation/xcode/distributing_your_app_to_registered_devices).

     Note that your Apple developer account may only allow you to import a limited number of
     devices per year.
   - *Option 2: *Collect and enter the UDIDs by email.

     On the [Add Devices](https://developer.apple.com/account/resources/devices/add)
     page of the Apple developer portal, register the new UDID specified in the
     email you received.
2. Add the registered devices to your [provisioning profile](https://developer.apple.com/account/resources/profiles/list).
3. Download the provisioning profile and use it to rebuild your app. If you are rebuilding only to update the registered devices, don't update the build number or version.
4. Re-distribute your app from the [Firebase console](https://firebase.google.com/docs/app-distribution/ios/distribute-console#distribute) or [CLI](https://firebase.google.com/docs/app-distribution/ios/distribute-cli#distribute). If you don't change your version, build number, or your app's code, App Distribution does not create a new release and won't notify testers. If you already distributed a build with the same build number and version, only users of newly-registered devices receive notification emails.

## Programmatically export UDIDs using fastlane

1. Export all of your tester device UDIDs as a CSV file from fastlane. For
   example, create and run a new `download_udids` lane:

       lane :download_udids do
           firebase_app_distribution_get_udids(
               app: "<your Firebase app ID>",
               output_file: "<path to output file>",
           )
       end

   > [!NOTE]
   > **Note:** To automate releasing a new build with new UDIDs, see [Distribute your
   > pre-release iOS builds faster with App Distribution and
   > fastlane](https://firebase.google.com/codelabs/appdistribution-udid-collection).

2. Import the UDID(s) into your [Apple developer account](https://developer.apple.com/account/resources/devices/add)
   using the **Register Multiple Devices** option. To learn more, see [Apple's
   documentation](https://developer.apple.com/documentation/xcode/distributing_your_app_to_registered_devices).
   Note that your Apple developer account may only allow you to import a
   limited number of devices per year.

3. Add the registered devices to your [provisioning profile](https://developer.apple.com/account/resources/profiles/list).

4. Download the provisioning profile and use it to rebuild your app. If you are
   rebuilding only for the purposes of updating the registered devices, don't
   update the build number or version.

5. [Re-distribute your
   app](https://firebase.google.com/docs/app-distribution/ios/distribute-fastlane#distribute). If you
   don't change your version, build number, or your app's code,
   App Distribution does not create a new release and won't notify testers. If you
   already distributed a build with the same build number and version, only
   users of newly-registered devices will receive notification emails.

## Receive alerts

### Get default alerts

By default, Firebase can send App Distribution alerts for new iOS device
registrations via email.

To receive App Distribution alerts via this default mechanism, you must have the
`firebase.projects.update` permission. The following roles include this required
permission by default: [Firebase
Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products) or project [Owner or
Editor](https://firebase.google.com/docs/projects/iam/roles-basic).

By default, every project member (who has the required permissions to receive
alerts) will get an email when a new iOS device is registered.

#### Turn on/off alerts for your own account

For your own account, you can turn on/off App Distribution alerts without
affecting other project members. Note that you still need the required
permissions to receive alerts.

To turn App Distribution alerts on or off, follow these steps:

1. In the Firebase console, in the top right-corner, go to *Firebase
   alerts*.
2. Then, go to *Settings* and set your account preference for App Distribution alerts.

### Set up advanced alerting to third-party services

You can also send App Distribution alerts to your team's preferred notification
channel using Cloud Functions for Firebase. For example, you can write a function
that captures an alert event for the registration of a new iOS device and post
the alert information to a third-party service, like Discord, Slack, or Jira.

To fully automate onboarding new iOS testers, you can write a function that adds
a new iOS device's UDID to the provisioning profile of your app, rebuilds the
app, and redistributes the app with the updated provisioning profile.

> [!NOTE]
> **Note:** To use advanced alerting capabilities, your Firebase project needs to use the [Blaze pricing plan](https://firebase.google.com/pricing).

To set up advanced alerting capabilities using Cloud Functions for Firebase, follow these steps:

1. [Set up Cloud Functions for Firebase](https://firebase.google.com/docs/functions/get-started),
   which includes the following tasks:

   1. Set up a development environment for Node.js or Python.
   2. Install and sign into the Firebase CLI.
   3. Initialize Cloud Functions for Firebase using the Firebase CLI.
2. [Write and deploy a function](https://firebase.google.com/docs/functions/alert-events) that
   captures an alert event from App Distribution and handles the event
   payload (for example, posts the alert information in a message on Discord).

To learn about all of the alert events that you can capture, go to the reference
documentation for [App Distribution
alerts](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution).

## Next steps

- [Import testers from CSV
  files](https://firebase.google.com/docs/app-distribution/import-testers-csv-files).

- To learn how to increase your internal testing base, see [Create invite
  links](https://firebase.google.com/docs/app-distribution/create-invite-links).