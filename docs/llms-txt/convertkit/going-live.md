# Source: https://developers.kit.com/kit-app-store/going-live.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Going live

> Getting your app live onto the Kit App Store

Once you have built and tested out your app, it's ready to be published to the Kit App Store. The guide below helps map out how to get yoru app live and what to check before submitting for approval.

## App review checklist

To streamline the review process and reduce delays, apps must submit the following:

### ✅ App requirements

* App authentication
  * Developers must use OAuth for user authentication instead of API keys for a secure, seamless installation experience when Kit API access is required
  * In order to allow tracking and validation of installs, the installation process must either:
    * start and end on the Kit App Store
    * start the flow externally, utilizing the correct installation URL, with the appended attribution tracking: `https://app.kit.com/apps/:app_id/install?k_app_id=k_:app_id`. Details on setting this up [can be found here](/kit-app-store/authentication#externally-initiating-installations)
    * you can also utilize the `Redirect URL after install` functionality ([which can be found here](/kit-app-store/app-details-page#how-to-configure)) to send creators to an external site upon completion of the install flow and redirect back to Kit.
* General UX
  * Apps should offer intuitive navigation and an easy onboarding experience
  * Clear access to help center articles or other support documentation is mandatory to minimize user confusion
* Technical standards
  * Apps must follow [standard best practices](/api-reference/response-codes#429-%7C-rate-limiting) to avoid API rate limiting
  * Apps should follow the relevant plugin recommendations
* App details page
  * Ensure your app details page follow the best practices set out in [the app details guide](/kit-app-store/app-details-page#best-practices), to ensure Kit App Store quality, but also help drive installations for your app

### ✅ Functionality description

* Submit a clear, concise description of the app’s intended functionality so that we know what to test it for
* Explain the app’s key flows and use cases (both within and outside Kit as a standalone experience) so testers understand what to evaluate

### ✅ Test credentials & OAuth testing

If the app requires a paid account, developers must provide us with test credentials for use during the review process.

Apps must support all potential OAuth flows. Testers will evaluate:

* **Not logged in:** Testing OAuth from a logged-out state
* **Logged in:** Testing OAuth from an already logged-in account
* **New User Signup:** Supporting a net new account creation (you’ll need to provide us with the ability to create a trial account or use a promo code to enable this)
* **Pre-loaded Data:** For apps with sync functionality (e.g., importing contacts), the test account must include pre-loaded data to simulate a realistic creator experience

### ✅ OAuth & onboarding

* Developers must use OAuth for user authentication instead of API keys for a secure, seamless installation experience
* The installation process must start and end on Kit in order to allow tracking and validation of installs

## Publishing your app

Once you've gone through and adhered to the points outlined above, send the app for approval by clicking the "Submit for approval" button in the "Distribution" tab within your app settings:

<img width="800" alt="submit app for approval" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/kit_app_store/submit-for-approval.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=aca4317625a634bdb40202d67ce0a248" data-path="images/kit_app_store/submit-for-approval.png" />

Click the "Submit for Approval" button in the window that pops up to confirm.

<img width="400" alt="submit app for approval confirmation" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/kit_app_store/submit-for-approval-confirmation.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=4928ad2738cd1f4c3d49706e912ba20e" data-path="images/kit_app_store/submit-for-approval-confirmation.png" />

Your app will be submitted to us for approval. If we need a test account with your service to review your app, please send the test account's information to [apps@kit.com](mailto:apps@kit.com) alongside any details on the app functionality and steps for testing.

Details on what makes a great app and what to avoid can be found in our [best practices guide here](/kit-app-store/best-practices).

Once approved by our team, the developer account will receive an email that the app is ready to be published.

When ready, hit "Publish" in the "Distribution" tab of your app and your app will automatically be available in the [Kit App Store](https://app.kit.com/apps) for all eligible creators (currently all paid plans), as well as our [Kit app marketing site](https://kit.com/apps).
​
If we reject your app, we'll send you an email explaining the issues we found. You can then make changes to your app and click "Resubmit for approval" to have us review it again.

<img width="800" alt="resubmit app for approval" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/kit_app_store/resubmit-for-approval.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=8baca94efd04fe535ae3219e91eb593a" data-path="images/kit_app_store/resubmit-for-approval.png" />


Built with [Mintlify](https://mintlify.com).