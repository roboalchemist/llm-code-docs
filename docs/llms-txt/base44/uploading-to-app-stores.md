# Source: https://docs.base44.com/documentation/building-your-app/uploading-to-app-stores.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Submitting your app to app stores

> Get your Base44 app store-ready by scanning, improving, and packaging it for the Apple App Store and Google Play.

When your Base44 app is ready for mobile, you can manage the entire store prep from inside your app editor. Scan your app against Apple and Google guidelines, use the Base44 AI chat to improve any problem areas, then generate the files you need to submit your app in your Apple and Google developer accounts.

<Frame>
    <img src="https://mintcdn.com/base44/N3afh-loi7NBLFG2/images/baseapps.png?fit=max&auto=format&n=N3afh-loi7NBLFG2&q=85&s=22009c82b08fefd012c67534ad4b81b9" alt="Baseapps" width="825" height="402" data-path="images/baseapps.png" />
</Frame>

Your mobile app runs your published Base44 app inside a secure web view. This is a lightweight native wrapper around your web app that opens only your app’s URL. It does not currently support native-only features such as push notifications or full offline mode, but it means that when you publish most content and design changes in Base44, they also appear in your app without sending a new version to the Apple App Store or Google Play.

<Warning>
  **Important:** You can run the scan to prepare your app for stores on the Free plan, but to download the files for app submission you must be on the Builder plan or higher.
</Warning>

<Card icon="sparkles" title="Before you begin">
  Store submission is a multi-step process that involves both Base44 and your Apple and Google dashboards. Keep your developer credentials nearby and set aside time to complete each part.

  **Make sure you have the following ready:**

  * A published Base44 app with a stable URL
  * An Apple Developer Program account with access to App Store Connect and API keys
  * A Google Play Console developer account
  * Permission to create and manage apps in both accounts (if you are working in a team)
  * A logo that meets Apple and Google icon requirements, or a clear prompt to generate one with AI
  * A privacy policy and terms of use page that explain how your app handles data and device permissions, and that are reachable from your main app pages

  **Information about selling products:**

  * **Physical goods and services:** Using Stripe is allowed in the app stores.
  * **Digital goods (for example, subscriptions or in-app features):** Do not use Stripe for payments inside your mobile app. Apple and Google require their own billing systems for digital content. If your app uses Stripe for digital content, your app is rejected. We are working on a built-in integration for StoreKit and Google Play Billing to handle digital purchases and keep your app compliant.
</Card>

<Check>
  **Already done all the preparation and ready to submit?** Follow our [**step-by-step visual guide**](https://submit-your-app.base44.app/) for submitting your app to Apple App Store and Google Play Store.
</Check>

***

## Step 1 | Create your developer accounts

Before you can generate store files and submit your app, you need active Apple and Google developer accounts. These accounts let you own your listings, manage releases, and handle reviews directly in each store.

<Info>
  You are responsible for setting up and paying for your Apple and Google developer accounts, as well as managing your app listings and submissions. Base44 helps you prepare your app for submission, but does not create or manage your developer accounts.
</Info>

### Apple Developer account

Use your Apple Developer account to submit your iOS app in App Store Connect and manage releases. Make sure you have an Apple ID you can use for your business.

**To create your Apple Developer account:**

1. Go to the [**Apple Developer enrollment page**](https://developer.apple.com/programs/enroll/).
2. Sign in with your Apple ID and start the enrollment process.
3. Choose the account type that fits your situation:
   * **Individual:** Select this if you are publishing as yourself.
   * **Organization:** Select this if you are publishing on behalf of a company. Apple may ask for your legal business name and D-U-N-S number.
4. Review and accept Apple program terms.
5. Complete the payment to activate your Apple Developer Program membership.
6. After your enrollment is approved, sign in to App Store Connect with the same Apple ID to manage your apps.

<Frame caption="Creating an Apple Developer account">
  <img src="https://mintcdn.com/base44/IrwJaSB1YGPPKM5X/images/appledevaccount.png?fit=max&auto=format&n=IrwJaSB1YGPPKM5X&q=85&s=40088d47bbee0ac0e99cbc1abd44a417" alt="The Apple Developer enrollment page for starting a new Apple Developer Program account" title="Creating an Apple Developer account" className="mx-auto" style={{ width:"74%" }} width="1112" height="788" data-path="images/appledevaccount.png" />
</Frame>

<Note>
  **Note:** Apple sends you an activation email after your enrollment payment is processed. This can take up to 2 business days. Once your account is active, sign in to App Store Connect and then return to Base44 to continue generating your App Store files.
</Note>

### Google Play developer account

Use your Google Play developer account to submit your Android app in Google Play Console and manage releases. Make sure you have a Google account you can use for your business.

**To create your Google Play developer account:**

1. Go to [**Google Play Console**](https://play.google.com/console/signup) in your browser.
2. Sign in with your Google account and start the registration flow.
3. Enter your developer profile details, such as your developer name, contact email, and website if you have one.
4. Review and accept Google Play terms and policies.
5. Complete the registration payment to create your Google Play developer account.
6. After setup finishes, sign in to Google Play Console and confirm that you can create a new app.

<Frame caption="Creating a Google Play developer account">
  <img src="https://mintcdn.com/base44/9kFMYgiH2a2rAihJ/images/GPC.png?fit=max&auto=format&n=9kFMYgiH2a2rAihJ&q=85&s=884c61a097085f69ae8b3d728b9900f7" alt="The Google Play Console signup flow for creating a new Google Play developer account" title="Creating a Google Play developer account" className="mx-auto" style={{ width:"78%" }} width="1056" height="812" data-path="images/GPC.png" />
</Frame>

***

## Step 2 | Scan your app for issues

From the app editor in Base44, scan your app against the latest App Store and Google Play guidelines.

**To run a scan:**

1. Go to your app editor.
2. Click **Publish** at the top-right.
3. Click the **Mobile app** tab.
4. Click **Check Your App**, then click **Run App Scan** and select what you want to scan your app against:
   * **App Store guidelines**
   * **Google Play guidelines**

<Frame caption="Running an app scan from the Mobile app tab">
  <img title="Running an app scan from the Mobile app tab" className="mx-auto hidden dark:block" src="https://mintcdn.com/base44/yQlgHqRtejzPxGje/images/scanapp-1.jpg?fit=max&auto=format&n=yQlgHqRtejzPxGje&q=85&s=b46fe3db600f4f09e18b7f49df3de4f4" alt="The Mobile app tab with Check Your App expanded and a Run App Scan drop-down button" width="1286" height="686" data-path="images/scanapp-1.jpg" />

  <img title="Running an app scan from the Mobile app tab" className="mx-auto dark:hidden" src="https://mintcdn.com/base44/yQlgHqRtejzPxGje/images/scanapp.jpg?fit=max&auto=format&n=yQlgHqRtejzPxGje&q=85&s=8d34a6673dc1f931bd63335c1c1cfe02" alt="The Mobile app tab with Check Your App expanded and a Run App Scan drop-down button" width="1286" height="686" data-path="images/scanapp.jpg" />
</Frame>

***

## Step 3 | Use AI to fix issues

After the scan finishes, use the results panel to see how ready your app is for the stores and let the AI chat suggest fixes. You can review each issue, apply recommended changes, and rerun the scan until you are happy with your score.

<Note>
  **Note:** You do not need a readiness score of 100 before you submit, but the higher the score, the smoother the submission process can be. Aim for a readiness score that is as high as possible, with no unresolved critical issues, before you generate store files.
</Note>

**To review and fix issues with the AI chat:**

1. Look at your **Readiness Score** and the number of passed, partial, and failed checks in the scan results panel.
2. Choose how you want to fix the issues:
   * **Apply with AI:** Open the AI chat with a tailored fix prompt based on your scan results.
   * **Copy Fix Prompt:** Copy the fix prompt so you can paste it into the AI chat yourself and edit it first.
3. Let the AI chat apply the suggested changes.

<Frame caption="Using AI to fix issues for app submission to stores">
  <img src="https://mintcdn.com/base44/FSrJodFJzIWjbUqE/images/aifixes.png?fit=max&auto=format&n=FSrJodFJzIWjbUqE&q=85&s=92e647a0b526b1fefe6b0195dc88d7a5" alt="Scan results in Base44 with AI-powered fix options for app store readiness issues" title="Using AI to fix issues for app submission to stores" className="mx-auto" style={{ width:"68%" }} width="592" height="760" data-path="images/aifixes.png" />
</Frame>

<Tip>
  **Check your score again:**

  1. Go back to **Preview** and test key flows such as browsing, sign up, log in, and checkout.
  2. Publish the changes.
  3. Run another app scan to see your updated readiness score and check that critical issues are resolved.
</Tip>

***

## Step 4 | Generate your app files

Generate the files for each store directly from the **Mobile app** tab so you do not have to leave the app editor. Use your scan-ready app to create the files you need to submit in the App Store and Google Play.

<Warning>
  **Important:** You must be on the Builder plan or higher to download your app files.
</Warning>

<Frame caption="Creating App Store and Google Play files from the Mobile app tab">
  <img title="Creating App Store and Google Play files from the Mobile app tab" className="mx-auto hidden dark:block" src="https://mintlify.s3.us-west-1.amazonaws.com/base44/images/appfiles-1.jpg" alt="The Mobile app tab with Build Stores Files expanded and buttons to Create App Store files and Create Google Play files" />

  <img title="Creating App Store and Google Play files from the Mobile app tab" className="mx-auto dark:hidden" src="https://mintcdn.com/base44/mz29DZQqoXbp9RIx/images/appfiles.jpg?fit=max&auto=format&n=mz29DZQqoXbp9RIx&q=85&s=4d0fd4cc7a87973e214dbd0aa5bd2e74" alt="The Mobile app tab with Build Stores Files expanded and buttons to Create App Store files and Create Google Play files" width="1286" height="614" data-path="images/appfiles.jpg" />
</Frame>

### Creating App Store files

When your app is ready for iOS, use your Apple Developer credentials in the **Mobile app** tab to generate an App Store ready IPA bundle. When generation completes, download the file from Base44, keep it in a secure location, and use it when you upload your app to App Store Connect.

**To create App Store files:**

1. Go to your app editor.
2. Click **Publish** at the top-right.
3. Click the **Mobile app** tab.
4. Click **Build Stores Files**, then **Create App Store files**.
5. Add your Issuer ID, Key ID, Team ID, and upload the `.p8` API key file from App Store Connect, then click **Continue**.

   <AccordionGroup>
     <Accordion title="Where do I find my IDs and API key file?">
       You need to generate your API key and then add the details to Base44.

       **To generate your key:**

       1. Go to App Store Connect and sign in with your Apple Developer account.
       2. Click **Users and Access**.
       3. Click <a href="https://appstoreconnect.apple.com/access/integrations/api" target="_blank" rel="noopener noreferrer">Integrations</a>

          .
       4. Click **+** to create a new API key.
       5. Enter a name for the key and choose the appropriate access role (for example, Admin or App Manager).
       6. Click **Generate** to create the key.

       **To find your Apple IDs and download the API key file (.p8):**

       1. Go to App Store Connect and sign in with your Apple Developer account.
       2. Click **Users and Access**.
       3. Click <a href="https://appstoreconnect.apple.com/access/integrations/api" target="_blank" rel="noopener noreferrer">Integrations</a>

          .
       4. Find your **Issuer ID** and **Key ID**.
       5. Click **Download** to save the `.p8` file to your computer and store it in a secure location.

       **To find your Team ID:**

       1. Go to your Apple Developer account.
       2. Look for the Team ID value listed under Membership details.
     </Accordion>
   </AccordionGroup>
6. Review your app logo. Upload a new logo from your computer or generate one with AI, then click **Generate files**.
7. When your files are ready, click **Download**.

   <Warning>
     **Important:**

     * Apple only lets you download each `.p8` key file once. If you lose it, you need to revoke the key and create a new one.
     * If you do not see the **Keys** tab in App Store Connect, your Apple Developer account is still being processed. It can take up to 48 hours after payment for Apple to activate your account and show the **Keys** tab. Wait for the activation email before you try to create API credentials.
     * Do not share your Issuer ID, Key ID, Team ID, or `.p8` file outside of trusted tools. Treat them as sensitive credentials. If you ever believe a key is exposed, revoke it in App Store Connect and create a new one.
     * Changing the logo in the **Create App Store files** window also updates the logo you currently use for your app. Make sure you are happy with the logo before you generate the files.
   </Warning>

### Creating Google Play files

When your app is ready for Android, use the **Mobile app** tab to generate a Google Play ready AAB bundle. After generation, download the file from Base44, keep it in a secure location, and upload it in your Google Play Console release.

**To create Google Play files:**

1. Go to your app editor.
2. Click **Publish** at the top-right.
3. Click the **Mobile app** tab.
4. Click **Build Stores Files**, then **Create Google Play files**.
5. Follow the on-screen steps to review your app logo, upload a new logo from your computer, or generate a new one with AI.

   <Note>
     **Note:** Changing the logo in the **Create Google Play files** window also updates the logo you currently use for your app. Make sure you are happy with the logo before you generate the files.
   </Note>
6. Click **Generate files** to create the AAB bundle.
7. When your files are ready, click **Download**.

### Adding Google Play SHA

If your app uses login with Google, you need to add the Google Play App Signing SHA-256 fingerprint to Base44 so that Google login works in the version people install from Google Play.

**To find your SHA-256 fingerprint in Google Play Console:**

1. Go to **Google Play Console** and sign in with your developer account.
2. In the side panel, go to **Setup**, then click **App integrity**.
3. Under **App signing key certificate**, copy the **SHA-256 fingerprint** value.

**To add your Google Play App Signing SHA in Base44:**

1. Go to your app editor.
2. Click **Publish** at the top-right.
3. Click the **Mobile app** tab.
4. Click **Build Stores Files**, then in the **Google Play files** section, click the **More Actions** icon <Icon icon="ellipsis" />.
5. Click **Add Google Play SHA**.
6. Paste your SHA-256 fingerprint into the **SHA-256 Fingerprint** field.
7. Click **Save**.

<Frame caption="Adding your Google Play App Signing SHA from the Mobile app tab">
  <img src="https://wixmp-ac7e9cc803be58fe35fda8c3.wixmp.com/chat/b27dbae9-b343-4114-a7b1-00c96c3d1fa7.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1cm46YXBwOjE1ZmFjM2UzMzMzNjQ0YzZiZDQ5ZDNiNzQzYTk0ZDdlIiwib2JqIjpbW3sicGF0aCI6Ii9jaGF0L2IyN2RiYWU5LWIzNDMtNDExNC1hN2IxLTAwYzk2YzNkMWZhNy5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdLCJpc3MiOiJ1cm46YXBwOjE1ZmFjM2UzMzMzNjQ0YzZiZDQ5ZDNiNzQzYTk0ZDdlIiwiaWF0IjoxNzczMTU1MTM0LCJqdGkiOiIyNzQwNDE0MzUxMmUiLCJleHAiOjE3ODg3MDcxNDR9.8vwyCkaIVVnq6AbtyHgkXlqSuvmLkPZ5UGpsRcNbCQY" alt="The Mobile app tab showing Google Play files with a Download menu that includes an Add Google Play SHA option" title="Adding your Google Play App Signing SHA from the Mobile app tab" className="mx-auto" style={{ width:"79%" }} />
</Frame>

<Note>
  **Note:** You only need to add the SHA if your app supports login with Google. If you change signing settings in Google Play later, update the SHA-256 fingerprint in Base44 so Google login continues to work in the distributed app.
</Note>

***

## Step 5 | Submit your app

After you generate your App Store and Google Play files, complete submission in your Apple and Google dashboards.

Base44 helps you get your app ready, but everything that happens after you submit in App Store Connect or Google Play Console is between you and the app stores. You are responsible for checking your submission status, responding to store emails, and applying any changes the stores request.

Follow our [**step-by-step visual guide**](https://submit-your-app.base44.app/) for submitting your app to Apple App Store and Google Play Store.

<Warning>
  **Important:**

  * Base44 cannot guarantee that an app is approved, even with a high readiness score.
  * Base44 support does not check on the status of your submission, contact Apple or Google on your behalf, or manage store review feedback for you. Take any feedback directly from the app stores and make changes yourself or work with a partner.
</Warning>

<Card icon="sparkles" title="Prepare your store listing assets">
  When you submit your app in App Store Connect and Google Play Console, you need assets for your store listings. Before you start the submission forms, prepare:

  * A short and long description for your app
  * Screenshots of your app on common phone sizes, and tablet screenshots if you plan to support tablets. You can capture screenshots by opening your published app on a device or simulator, navigating through your main flows, and taking native device screenshots that you upload in each store.
  * Your app icon and any required feature graphics that follow Apple and Google size and format guidelines
  * A support URL and privacy policy URL from your Base44 app
</Card>

***

## Troubleshooting submission issues

Use this section to resolve common issues.

<AccordionGroup>
  <Accordion title="Error 401 when generating iOS IPA files">
    If you see a message similar to **"UNAUTHENTICATED: App Store Connect rejected the authentication token"**, your App Store Connect API key details are missing, invalid, or expired.

    **To fix error 401:**

    1. Go to App Store Connect and sign in with your Apple Developer account.
    2. Click **Users and Access**, then click **Integrations**.
    3. Check that the **Issuer ID**, **Key ID**, and **Team ID** values you entered in Base44 match the values shown in App Store Connect.
    4. Confirm that the `.p8` API key file you uploaded is the correct file and that the key has not been revoked or expired.
    5. If anything looks incorrect, generate a new API key in App Store Connect, download the new `.p8` file, update all fields in Base44, and try generating the files again.
  </Accordion>

  <Accordion title="Error 403 when generating iOS IPA files">
    If you see a message similar to **"PERMISSION\_DENIED: This operation is not allowed. Your App Store Connect API key may need the Admin role"**, the API key you are using does not have enough permissions.

    **To fix error 403:**

    1. Go to App Store Connect and sign in with your Apple Developer account.
    2. Click **Users and Access**, then **Integrations**.
    3. Check the **Access** role for the API key you are using.
    4. If the key is not set to **Admin**, create a new key:
       1. Click **+** to add a new key.
       2. Enter a name and select the **Admin** role.
       3. Click **Generate** and download the `.p8` file.
    5. In Base44, update the Issuer ID, Key ID, Team ID, and upload the new `.p8` file, then try generating the App Store files again.

    <Frame>
      <img src="https://mintcdn.com/base44/dmwBtTS1sLbs79_9/images/adminrole.png?fit=max&auto=format&n=dmwBtTS1sLbs79_9&q=85&s=0b17e31b0753efd8e6a76581875ad6c8" alt="The Admin access role selected for an App Store Connect API key" title="Admin role for App Store Connect API key" className="mx-auto" style={{ width:"72%" }} width="703" height="516" data-path="images/adminrole.png" />
    </Frame>
  </Accordion>

  <Accordion title="Error 409 when generating iOS IPA files">
    If you see a message similar to **"ALREADY\_EXISTS: You've reached the limit for iOS Distribution certificates. Revoke an existing iOS Distribution certificate in App Store Connect to create a new one"**, your Apple Developer account has reached the limit for active iOS Distribution certificates.

    Every time you generate an IPA in Base44, Apple creates an iOS Distribution certificate. The standard Apple Developer Program allows up to 3 active production distribution certificates at the same time.

    **To fix error 409:**

    1. Go to your Apple Developer account and open **Certificates, Identifiers & Profiles**.
    2. Click **Certificates** and filter to **iOS Distribution** certificates.
    3. Revoke at least one iOS Distribution certificate that you no longer need.
    4. Try generating the App Store files again from the **Mobile app** tab in Base44.

    <Note>
      **Note:**

      * An iOS Distribution certificate can usually be revoked after an app has been approved, without affecting people who already installed the app.
      * Apple typically allows:
        * Up to 3 active production/distribution certificates for the standard Apple Developer Program
        * Up to 2 active enterprise distribution certificates
        * Up to 12 development certificates
    </Note>
  </Accordion>

  <Accordion title="Temporary iOS SDK alert during upload">
    When you upload your IPA to App Store Connect, you may see an alert that looks similar to:

    > This app was built with the iOS 18.1 SDK. Starting April 28, 2026, all iOS and iPadOS apps must be built with the iOS 26 SDK or later, included in Xcode 26 or later, in order to be uploaded to App Store Connect or submitted for distribution.

    This is a temporary warning about a future SDK requirement. Just click **OK** in App Store Connect and continue the upload flow.

    The Base44 team is aware of this update and is working on a solution before the deadline.
  </Accordion>

  <Accordion title="Bundle ID or signing key mismatch when uploading an update">
    If you previously uploaded a native app to the stores and now generate files from Base44 for the same brand, you might see errors about a **Bundle ID** or **signing key** mismatch.

    Base44 automatically configures a Bundle ID and signing key for your app files. These values cannot be changed inside the generated IPA or AAB files. If the values do not match a previous version that you uploaded manually or from another tool, the stores block the update.

    **To resolve Bundle ID or signing key mismatches:**

    1. Review the existing app listing in App Store Connect or Google Play Console and compare the Bundle ID and signing key with the values from your Base44 build.
    2. If they do not match and you cannot update the existing listing, create a new app entry in the store and submit the Base44 build as a new app.
    3. Update your icon, app name, or description if needed so people can clearly identify the new app.
  </Accordion>

  <Accordion title="Permissions, privacy policy, and app review feedback">
    Every mobile app package includes device-level permissions. Base44 uses AI to scan your app and set the permissions it needs. These permissions are not editable in the Base44 interface.

    Apple and Google expect your privacy policy and store listing to explain which types of data your app collects, how you use it, and which device features your app accesses.

    **If your app is rejected due to permissions or privacy issues:**

    1. Read the rejection email carefully to see which permission or behavior the store is concerned about.
    2. Update your privacy policy and terms pages on your Base44 app so they:
       * Describe the types of data your app collects (for example, location, camera, or microphone)
       * Explain why you collect the data and how people can contact you about privacy
    3. Make sure links to your privacy policy and terms appear before people register or sign in (for example, in your home page footer or login screen).
    4. Resubmit your app after updating the content.
  </Accordion>

  <Accordion title="Main URL and access to legal pages">
    Base44 automatically chooses the main entry URL for your mobile app based on your published app. You cannot currently select a different start page just for the app.

    Apple and Google require that people can access your **Privacy Policy** and **Terms of Use** before they create an account.

    **To keep your app compliant:**

    1. Make sure your privacy and terms pages are live on your Base44 app.
    2. Add visible links to these pages from the entry page of your app, such as in the footer or a menu.
    3. If your app uses a gated or members-only home page, ensure that privacy and terms links are still accessible before sign-up (for example, from the login or sign-up page).
  </Accordion>
</AccordionGroup>

***

## FAQs

Click a question below to learn more about submitting your Base44 app to the Apple App Store and Google Play.

<AccordionGroup>
  <Accordion title="Do I need to reach a readiness score of 100 before I submit?">
    You do not need a readiness score of 100. A higher score usually means your app follows more store guidelines and may have a smoother review. Focus on resolving all critical issues and as many partial issues as you can before you submit.
  </Accordion>

  <Accordion title="Can I submit to only one store, not both?">
    Yes. You can submit your app to only one store. You do not have to publish to both stores. Use the App Store scan and **Create App Store files** if you only need an iOS app, or use the Google Play scan and **Create Google Play files** if you only need an Android app.
  </Accordion>

  <Accordion title="What happens if the scan still shows failed checks after fixes?">
    You can still generate files and submit your app, but there is a higher chance that Apple or Google ask for changes during review. It is best to reread the scan descriptions for each failed check, decide whether the risk is acceptable for your app, and run another scan after any updates so you see the latest readiness score.
  </Accordion>

  <Accordion title="Can Base44 submit my app to the stores for me?">
    Base44 helps you scan your app against store guidelines, improve it with AI, and generate the IPA and AAB bundles. You still need to submit the app through your own App Store Connect and Google Play Console accounts, where you control the listing details, pricing, and release settings.
  </Accordion>

  <Accordion title="Can Base44 support check on my submission or talk to the app stores for me?">
    No. Base44 support does not track the progress of your submission, contact Apple or Google, or manage conversations with the review teams. To see the status of your app, sign in to App Store Connect and Google Play Console, read their emails, and follow any instructions they provide.
  </Accordion>

  <Accordion title="Do I need a custom domain to submit my app?">
    No. You do not need a custom domain to submit your app to the Apple App Store or Google Play. Base44 can scan your app and generate the App Store and Google Play files using your default Base44 URL. A custom domain is optional and can help with branding and SEO, but it is not required for store submission.
  </Accordion>

  <Accordion title="Do I need to resubmit my app every time I update my Base44 app?">
    No. Your Base44 mobile app loads your live app in a web view. This is a native wrapper that opens only your app URL, so when you change content or design in Base44 and publish your app, those updates usually appear in the app without submitting a new version to the Apple App Store or Google Play.

    You only need to generate new app files and submit an update when something in the app shell changes, such as the app name, icon, or bundle identifiers, or when you add features that require new device permissions. In those cases, regenerate the files in Base44 and submit an updated version to the stores.
  </Accordion>

  <Accordion title="Which native features does the Base44 mobile app support?">
    Your Base44 mobile app focuses on running your web experience inside a secure web view rather than as a fully native app.

    **Current limitations:**

    * Native-only features such as push notifications and full offline mode are not supported yet.
    * Some native capabilities may still require additional review by Apple or Google, depending on the permissions your app needs.

    Base44 continues to expand native feature coverage over time. Check product updates and release notes to see which new native features are available for your app.
  </Accordion>

  <Accordion title="How long do people stay logged in to the app?">
    Base44 uses token-based authentication with a default session duration of up to 90 days. Someone who signs in to your app stays signed in on that device until they sign out or clear the app’s cache, or until the 90-day period ends. You do not need to configure this manually.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).