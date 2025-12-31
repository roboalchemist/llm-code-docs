# Source: https://firebase.google.com/docs/auth/custom-email-handler.md.txt

Some user management actions, such as updating a user's email address and resetting a user's password, result in emails being sent to the user. These emails contain links that recipients can open to complete or cancel the user management action. By default, user management emails link to the default action handler, which is a web page hosted at a URL in your project's Firebase Hosting domain.

You can instead create and host a custom email action handler to do custom processing and to integrate the email action handler with your website.

The following user management actions require the user to complete the action using an email action handler:

- Resetting passwords
- Revoking email address changes---when users change their accounts' primary email addresses, Firebase sends an email to their old addresses that allow them to undo the change
- Verifying email addresses

To customize your Firebase project's email action handler, you must create and host a web page that uses the Firebase JavaScript SDK to verify the request's validity and complete the request. Then, you must customize your Firebase project's email templates to link to your custom action handler.

## Create the email action handler page

1. Firebase adds several query parameters to your action handler URL when it generates user management emails. For example:

   ```
   https://example.com/usermgmt?mode=resetPassword&oobCode=ABC123&apiKey=AIzaSy...&lang=fr
   ```

   <br />

   These parameters specify the user management task that the user is completing. Your email action handler page must handle the following query parameters:

   |                                                                                                                                                                                                                                                                            Parameters                                                                                                                                                                                                                                                                            ||
   |-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | mode        | The user management action to be completed. Can be one of the following values: - `resetPassword` - `recoverEmail` - `verifyEmail`                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | oobCode     | A one-time code, used to identify and verify a request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | apiKey      | Your Firebase project's API key, provided for convenience                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | continueUrl | This is an optional URL that provides a way to pass state back to the app via a URL. This is relevant to password reset and email verification modes. When sending a password reset email or verification email, an`ActionCodeSettings`object needs to be specified with a continue URL for this to be available. This makes it possible for a user to continue right where they left off after an email action.                                                                                                                                    |
   | lang        | This is the optional[BCP47](https://tools.ietf.org/html/bcp47)language tag representing the user's locale (for example,`fr`). You can use this value to provide localized email action handler pages to your users. Localization can be set via the Firebase Console or dynamically by calling the corresponding client API before triggering the email action. For example, using JavaScript:`firebase.auth().languageCode = 'fr';`. For consistent user experience, make sure the email action handler localization matches the email template's. |

   The following example shows how you might handle the query parameters in a browser based handler. (You could also implement the handler as a Node.js application using similar logic.)  

   ### Web

   ```javascript
   import { initializeApp } from "firebase/app";
   import { getAuth } from "firebase/auth";

   document.addEventListener('DOMContentLoaded', () => {
     // TODO: Implement getParameterByName()

     // Get the action to complete.
     const mode = getParameterByName('mode');
     // Get the one-time code from the query parameter.
     const actionCode = getParameterByName('oobCode');
     // (Optional) Get the continue URL from the query parameter if available.
     const continueUrl = getParameterByName('continueUrl');
     // (Optional) Get the language code if available.
     const lang = getParameterByName('lang') || 'en';

     // Configure the Firebase SDK.
     // This is the minimum configuration required for the API to be used.
     const config = {
       'apiKey': "YOUR_API_KEY" // Copy this key from the web initialization
                                // snippet found in the Firebase console.
     };
     const app = initializeApp(config);
     const auth = getAuth(app);

     // Handle the user management action.
     switch (mode) {
       case 'resetPassword':
         // Display reset password handler and UI.
         handleResetPassword(auth, actionCode, continueUrl, lang);
         break;
       case 'recoverEmail':
         // Display email recovery handler and UI.
         handleRecoverEmail(auth, actionCode, lang);
         break;
       case 'verifyEmail':
         // Display email verification handler and UI.
         handleVerifyEmail(auth, actionCode, continueUrl, lang);
         break;
       default:
         // Error: invalid mode.
     }
   }, false);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/custom-email-handler/auth_handle_mgmt_query_params.js#L8-L49
   ```

   ### Web

   ```javascript
   document.addEventListener('DOMContentLoaded', () => {
     // TODO: Implement getParameterByName()

     // Get the action to complete.
     var mode = getParameterByName('mode');
     // Get the one-time code from the query parameter.
     var actionCode = getParameterByName('oobCode');
     // (Optional) Get the continue URL from the query parameter if available.
     var continueUrl = getParameterByName('continueUrl');
     // (Optional) Get the language code if available.
     var lang = getParameterByName('lang') || 'en';

     // Configure the Firebase SDK.
     // This is the minimum configuration required for the API to be used.
     var config = {
       'apiKey': "YOU_API_KEY" // Copy this key from the web initialization
                               // snippet found in the Firebase console.
     };
     var app = firebase.initializeApp(config);
     var auth = app.auth();

     // Handle the user management action.
     switch (mode) {
       case 'resetPassword':
         // Display reset password handler and UI.
         handleResetPassword(auth, actionCode, continueUrl, lang);
         break;
       case 'recoverEmail':
         // Display email recovery handler and UI.
         handleRecoverEmail(auth, actionCode, lang);
         break;
       case 'verifyEmail':
         // Display email verification handler and UI.
         handleVerifyEmail(auth, actionCode, continueUrl, lang);
         break;
       default:
         // Error: invalid mode.
     }
   }, false);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/custom-email-handler.js#L16-L54
   ```
2. Handle password reset requests by first verifying the action code with`verifyPasswordResetCode`; then get a new password from the user and pass it to`confirmPasswordReset`. For example:

   ### Web

   ```javascript
   import { verifyPasswordResetCode, confirmPasswordReset } from "firebase/auth";

   function handleResetPassword(auth, actionCode, continueUrl, lang) {
     // Localize the UI to the selected language as determined by the lang
     // parameter.

     // Verify the password reset code is valid.
     verifyPasswordResetCode(auth, actionCode).then((email) => {
       const accountEmail = email;

       // TODO: Show the reset screen with the user's email and ask the user for
       // the new password.
       const newPassword = "...";

       // Save the new password.
       confirmPasswordReset(auth, actionCode, newPassword).then((resp) => {
         // Password reset has been confirmed and new password updated.

         // TODO: Display a link back to the app, or sign-in the user directly
         // if the page belongs to the same domain as the app:
         // auth.signInWithEmailAndPassword(accountEmail, newPassword);

         // TODO: If a continue URL is available, display a button which on
         // click redirects the user back to the app via continueUrl with
         // additional state determined from that URL's parameters.
       }).catch((error) => {
         // Error occurred during confirmation. The code might have expired or the
         // password is too weak.
       });
     }).catch((error) => {
       // Invalid or expired action code. Ask user to try to reset the password
       // again.
     });
   }https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/custom-email-handler/auth_handle_reset_password.js#L8-L41
   ```

   ### Web

   ```javascript
   function handleResetPassword(auth, actionCode, continueUrl, lang) {
     // Localize the UI to the selected language as determined by the lang
     // parameter.

     // Verify the password reset code is valid.
     auth.verifyPasswordResetCode(actionCode).then((email) => {
       var accountEmail = email;

       // TODO: Show the reset screen with the user's email and ask the user for
       // the new password.
       var newPassword = "...";

       // Save the new password.
       auth.confirmPasswordReset(actionCode, newPassword).then((resp) => {
         // Password reset has been confirmed and new password updated.

         // TODO: Display a link back to the app, or sign-in the user directly
         // if the page belongs to the same domain as the app:
         // auth.signInWithEmailAndPassword(accountEmail, newPassword);

         // TODO: If a continue URL is available, display a button which on
         // click redirects the user back to the app via continueUrl with
         // additional state determined from that URL's parameters.
       }).catch((error) => {
         // Error occurred during confirmation. The code might have expired or the
         // password is too weak.
       });
     }).catch((error) => {
       // Invalid or expired action code. Ask user to try to reset the password
       // again.
     });
   }https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/custom-email-handler.js#L59-L90
   ```
3. Handle email address change revocations by first verifying the action code with`checkActionCode`; then restore the user's email address with`applyActionCode`. For example:

   ### Web

   ```javascript
   import { checkActionCode, applyActionCode, sendPasswordResetEmail } from "firebase/auth";

   function handleRecoverEmail(auth, actionCode, lang) {
     // Localize the UI to the selected language as determined by the lang
     // parameter.
     let restoredEmail = null;
     // Confirm the action code is valid.
     checkActionCode(auth, actionCode).then((info) => {
       // Get the restored email address.
       restoredEmail = info['data']['email'];

       // Revert to the old email.
       return applyActionCode(auth, actionCode);
     }).then(() => {
       // Account email reverted to restoredEmail

       // TODO: Display a confirmation message to the user.

       // You might also want to give the user the option to reset their password
       // in case the account was compromised:
       sendPasswordResetEmail(auth, restoredEmail).then(() => {
         // Password reset confirmation sent. Ask user to check their email.
       }).catch((error) => {
         // Error encountered while sending password reset code.
       });
     }).catch((error) => {
       // Invalid code.
     });
   }https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/custom-email-handler/auth_handle_recover_email.js#L8-L36
   ```

   ### Web

   ```javascript
   function handleRecoverEmail(auth, actionCode, lang) {
     // Localize the UI to the selected language as determined by the lang
     // parameter.
     var restoredEmail = null;
     // Confirm the action code is valid.
     auth.checkActionCode(actionCode).then((info) => {
       // Get the restored email address.
       restoredEmail = info['data']['email'];

       // Revert to the old email.
       return auth.applyActionCode(actionCode);
     }).then(() => {
       // Account email reverted to restoredEmail

       // TODO: Display a confirmation message to the user.

       // You might also want to give the user the option to reset their password
       // in case the account was compromised:
       auth.sendPasswordResetEmail(restoredEmail).then(() => {
         // Password reset confirmation sent. Ask user to check their email.
       }).catch((error) => {
         // Error encountered while sending password reset code.
       });
     }).catch((error) => {
       // Invalid code.
     });
   }https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/custom-email-handler.js#L94-L120
   ```
4. Handle email address verification by calling`applyActionCode`. For example:

   ### Web

   ```javascript
   function handleVerifyEmail(auth, actionCode, continueUrl, lang) {
     // Localize the UI to the selected language as determined by the lang
     // parameter.
     // Try to apply the email verification code.
     applyActionCode(auth, actionCode).then((resp) => {
       // Email address has been verified.

       // TODO: Display a confirmation message to the user.
       // You could also provide the user with a link back to the app.

       // TODO: If a continue URL is available, display a button which on
       // click redirects the user back to the app via continueUrl with
       // additional state determined from that URL's parameters.
     }).catch((error) => {
       // Code is invalid or expired. Ask the user to verify their email address
       // again.
     });
   }https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/custom-email-handler/auth_handle_verify_email.js#L8-L25
   ```

   ### Web

   ```javascript
   function handleVerifyEmail(auth, actionCode, continueUrl, lang) {
     // Localize the UI to the selected language as determined by the lang
     // parameter.
     // Try to apply the email verification code.
     auth.applyActionCode(actionCode).then((resp) => {
       // Email address has been verified.

       // TODO: Display a confirmation message to the user.
       // You could also provide the user with a link back to the app.

       // TODO: If a continue URL is available, display a button which on
       // click redirects the user back to the app via continueUrl with
       // additional state determined from that URL's parameters.
     }).catch((error) => {
       // Code is invalid or expired. Ask the user to verify their email address
       // again.
     });
   }https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/custom-email-handler.js#L124-L141
   ```
5. Host the page somewhere, for example use[Firebase Hosting](https://firebase.google.com/docs/hosting).

Next, you must configure your Firebase project to link to your custom email action handler in its user management emails.

## Link to your custom handler in your email templates

To configure your Firebase project to use your custom email action handler:

1. Open your project in the[Firebaseconsole](https://console.firebase.google.com/).
2. Go to the**Email Templates** page in the**Auth**section.
3. In any of the**Email Types**entries, click the pencil icon to edit the email template.
4. Click**customize action URL**, and specify the URL to your custom email action handler.

After you save the URL, it will be used by all of your Firebase project's email templates.
| If you're using a custom domain, even if you're not customizing your email action handler, you might want to still complete this step so that user management emails link to your domain instead of the default`firebaseapp.com`domain.