# Source: https://firebase.google.com/docs/auth/android/email-link-migration.md.txt

Email link authentication previously relied on Firebase Dynamic Links, which will be
[shut down on August 25, 2025](https://firebase.google.com/support/dynamic-links-faq). We've published an
alternative solution in the Firebase Authentication Android SDK version 23.2.0+ and
Firebase BoM version 33.9.0+. If your app uses the old style links and you
want to use an alternative method for migrating your app, see
[Authenticate with Firebase using Email Link in Android](https://firebase.google.com/docs/auth/android/email-link-auth)
to use the new Firebase Hosting based system.

Also, if you're using the **Firebase Authentication Android SDK below v20.0.0 (or the
Firebase BoM below v26.0.0) to manage OAuth flows** with Firebase Authentication,
you'll need to update to the latest Authentication SDK or BoM version
(Authentication v20.0.0+ or BoM v26.0.0+) in order to continue managing OAuth
flows in Firebase Authentication.

## Migrate your associated Firebase Dynamic Links domain to a Firebase Hosting domain

Moving forward, rather than using a Firebase Dynamic Links domain, Firebase Authentication
will use the Firebase Hosting default domain for your project to create
links for email link and other out-of-band link actions in mobile apps. This
means that your app will also need to be updated to use this default domain as
the associated domain for email authentication links to your mobile app.

You can follow the instructions in
[Authenticate with Firebase Using Email Link in Android](https://firebase.google.com/docs/auth/android/email-link-auth) to update your mobile app links
to use the new automatically provisioned Firebase Hosting default domain.

Use the following instructions to handle links from the new domain and to
instruct Firebase Authentication to start using the new domain to generate mobile app
links going forward.

If you'd like to continue using any of your custom Firebase Hosting domains
or even your custom Firebase Dynamic Links domain to be your new associated
domain, follow the steps that match the intended domain you'd like to use. Note
that after completing the instructions in the following section, the deep
linking feature on your Firebase Dynamic Links custom domain will be removed;
only the domain itself will remain for creating email links.

1. **Configure your Android application to handle your Firebase Hosting link**

   1. In order to handle these links from your Android application, your app's package name needs to be specified in the Firebase console project settings. In addition, the SHA-1 and SHA-256 of the application certificate need to be provided.
   2. If you want these Firebase Hosting links to redirect to a specific
      activity, you will need to configure an intent filter in your
      `AndroidManifest.xml` file. The intent filter should catch
      Firebase Hosting links of your domain. In `AndroidManifest.xml`:

          <intent-filter android:autoVerify="true">
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.BROWSABLE" />
            <category android:name="android.intent.category.DEFAULT" />
            <data
              android:scheme="https"
              android:host="PROJECT_ID.firebaseapp.com or a custom hosting domain"
              android:pathPrefix="/__/auth/links" />
          </intent-filter>

   When users open a hosting link with the "/__/auth/links" path and the
   scheme and host you specify, your app will start the activity with this
   intent filter to handle the link.

   > [!IMPORTANT]
   > **Important:** To ensure a seamless rollback, we recommend keeping your existing intent filter that handles Firebase Dynamic Links while trying out the Firebase Hosting link solution. The Firebase Dynamic Links solution will be available until August 25, 2025.

2. **Configure your project to use the new links**

   When you're ready to handle the new domain links, you can use the
   [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup) to update how you want email links
   to be generated and instruct our backend to start generating links using
   the new Firebase Hosting domain.

       import { getAuth } from 'firebase-admin/auth';

       const updateEmailAuthDomain = async () => {
         const updateRequest = {
           mobileLinksConfig: {
             domain: 'HOSTING_DOMAIN',
           },
         };

         const projectConfigManager = getAuth().projectConfigManager();

         try {
           const response = await projectConfigManager.updateProjectConfig(updateRequest);
           // Updated project config
           console.log('Project configuration updated successfully:', response);
         } catch (error) {
           console.error('Error updating the project:', error);
         }
       };

   > [!IMPORTANT]
   > **Important:** To rollback to the Firebase Dynamic Links while implementing and testing the backup solution, you should set the domain back to `FIREBASE_DYNAMIC_LINK`. The Firebase Dynamic Links solution will be available until August 25, 2025.

3. **Send and redeem the email link**

   Send the email sign-in link as before. When the end user clicks the link,
   they will be redirected to the app if installed to complete the sign-in.

## Customize your mobile links

You can use a custom Firebase Hosting domain or reuse your custom
Firebase Dynamic Links domain to be your new mobile links domain.

### Use a custom Firebase Hosting domain

1. Follow the [Firebase Hosting guide](https://firebase.google.com/docs/hosting/custom-domain) to set up a custom domain.
2. Configure your Android application to handle your Firebase Hosting link. (instructions in previous section above).
3. [Send an authentication link to the user's email
   address](https://firebase.google.com/docs/auth/android/email-link-auth#send_an_authentication_link_to_the_users_email_address) with an updated `ActionCodeSettings` object with a custom domain as `linkDomain`.

### Re-use your custom Firebase Dynamic Links domain

1. You can re-use any of your Firebase Dynamic Links domains as your custom domain. However, any Firebase Dynamic Links functionality will no longer be supported (for example, users cannot be redirected to an app store if the app isn't installed on their device).
2. Configure your Android application to handle your Firebase Hosting link (instructions in previous section above).
3. [Send an authentication link to the user's email
   address](https://firebase.google.com/docs/auth/android/email-link-auth#send_an_authentication_link_to_the_users_email_address) with an updated `ActionCodeSettings` object with a custom domain as `linkDomain`.