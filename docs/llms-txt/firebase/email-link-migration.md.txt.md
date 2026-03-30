# Source: https://firebase.google.com/docs/auth/ios/email-link-migration.md.txt

Email link authentication previously relied on Firebase Dynamic Links, which will be
[shut down on August 25, 2025](https://firebase.google.com/support/dynamic-links-faq). We've published an
alternative solution in the Firebase Authentication iOS SDK version 11.8.0+. If your
app uses Firebase Dynamic Links, you should migrate your app to the new
Firebase Hosting based system.

## Migrate your associated Firebase Dynamic Links domain to a Firebase Hosting domain

Moving forward, rather than using a Firebase Dynamic Links domain, Firebase Authentication
will use the Firebase Hosting default domain for your project to create
links for email link and other out-of-band link actions in mobile apps. This
means that your app will also need to be updated to use this default domain as
the associated domain for email authentication links to your mobile app.

You can follow the instructions in
[Authenticate with Firebase Using Email Link on Apple Platforms](https://firebase.google.com/docs/auth/ios/email-link-auth)
to update your app to use the new automatically provisioned Firebase Hosting
default domain.

Use the following instructions to handle links from the new domain and to
instruct Firebase Authentication to start using the Firebase Hosting domain to
generate mobile app links going forward.

If you'd like to continue using any of your custom Firebase Hosting domains
or even your custom Firebase Dynamic Links domain to be your new associated domain,
using the instructions in the [Customize Mobile Links](https://firebase.google.com/docs/auth/ios/email-link-migration#customize-mobile-links)
section, adapt the steps to match the intended domain you'd like to use.

1. **Link Firebase Hosting domain to your app associated domain.**

   You'll need to configure the selected domain as an Associated Domain for
   app links. To set up the entitlement in your app, open the target's
   **Signing \& Capabilities** tab in Xcode and add Firebase Hosting domains
   from the previous step to the Associated Domains capability. If using the
   default Firebase Hosting domain, this will be
   `applinks:PROJECT_ID.firebaseapp.com`.

   See [Supporting associated domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains)
   on Apple's documentation site for more information.

   An associated domain file has been deployed under all your
   Firebase Hosting domains. To access it, navigate to
   `PROJECT_ID.firebaseapp.com/.well-known/apple-app-site-association`.
   This AASA file can be overwritten; see
   [Create and host your Universal Links configuration files](https://firebase.google.com/support/guides/app-links-universal-links#create_and_host_your_universal_links_configuration_files_on_your_new_hosting_domain)
   for more information.

   > [!IMPORTANT]
   > **Important:** To ensure a seamless rollback, we recommend keeping your existing intent filter that handles Firebase Dynamic Links while trying out the Firebase Hosting link solution. The Firebase Dynamic Links solution will be available until August 25, 2025.

2. **Configure your project to use the new links.**

   When you're ready to handle the new domain links, you can use the
   [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup) to update how you want email links
   to be generated and instruct our backend to start generating links using the
   new Firebase Hosting domain.

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

3. **Send and redeem the email link.**

   Send the email sign-in link as before. When an end user clicks on the link,
   they will be redirected to the app if installed to finish the sign in.

## Customize your mobile links

You can use a custom Firebase Hosting domain or reuse your custom
Firebase Dynamic Links domain to be your new mobile links domain.

### Use a custom Firebase Hosting domain

1. Follow the [Firebase Hosting guide](https://firebase.google.com/docs/hosting/custom-domain) to set up a custom domain.
2. Link the custom domain to your app associated domain.
3. [Send an authentication link to the user's email address](https://firebase.google.com/docs/auth/ios/email-link-auth#send_an_authentication_link_to_the_users_email_address) with an updated `ActionCodeSettings` object with a custom domain as `linkDomain`.

### Re-use your custom Firebase Dynamic Links domain

1. You can re-use any of your Firebase Dynamic Links domains as your custom domain. However, any Firebase Dynamic Links functionality will no longer be supported (for example, users cannot be redirected to the app store if app isn't installed on their device).
2. [Send an authentication link to the user's email address](https://firebase.google.com/docs/auth/ios/email-link-auth#send_an_authentication_link_to_the_users_email_address) with an updated `ActionCodeSettings` object with a custom domain as `linkDomain`.