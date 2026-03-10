# Source: https://firebase.google.com/docs/app-distribution/ios/distribute-console.md.txt

You can manage your team's testers and distribute builds to them using the
Firebase console.

To distribute your app to testers, upload the IPA file using the
Firebase console:

1. Open the [App Distribution page](https://console.firebase.google.com/project/_/appdistribution) of the
   Firebase console. Select your Firebase project when prompted.

2. On the **Releases** page, select the app you want to distribute from
   the drop-down menu.

3. Drag your app's IPA file to the console to upload it.

4. When the upload completes, specify the tester groups and individual testers
   you want to receive the build. Then, add release notes for the build.

   See [Manage testers](https://firebase.google.com/docs/app-distribution/manage-testers) for more on
   creating tester groups.
5. Click **Distribute** to make the build available to testers.

6. To share links to specific releases with testers who have access
   to those releases, click the **Link** icon to copy the release link to the
   clipboard.

Once you distribute your build, it becomes available in the
App Distribution dashboard of the Firebase console for 150 days (five months).
When the build is 30 days from expiring, an expiration notice appears in both
the Firebase console and your tester's list of builds on their test device.

Testers who haven't been invited to test the app receive email invitations to
get started, and existing testers receive email notifications that a new build
is ready to test. To learn how to install the test
app, see [Get set up as a tester](https://firebase.google.com/docs/app-distribution/get-set-up-as-a-tester?platform=ios).
You can monitor the status of each tester-whether they accepted the
invitation and whether they downloaded the app-in the Firebase console.

Testers have 30 days to accept an invitation to test the app before it expires.
When an invitation is 5 days from expiring, an expiration notice appears in the
Firebase console next to the tester on a release. An invitation can be
renewed by resending it using the drop-down menu on the tester row.

## Next steps

- To register more devices manually or programmatically, see
  [Register additional iOS devices](https://firebase.google.com/docs/app-distribution/register-additional-devices).

- Learn best practices for [distributing Apple apps to QA testers using CI/CD and fastlane](https://firebase.google.com/docs/app-distribution/best-practices-distributing-apple-apps-to-qa-testers-with-ci-cd-fastlane).