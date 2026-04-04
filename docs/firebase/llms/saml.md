# Source: https://firebase.google.com/docs/auth/web/saml.md.txt

If you've upgraded toFirebase Authenticationwith Identity Platform, you can authenticate your users with Firebase using the SAML identity provider of your choice. This makes it possible to use your SAML-based SSO solution to sign users in to your Firebase app.

Firebase Authenticationsupports only the service-provider initiated SAML flow.

## Before you begin

To sign in users using a SAML identity provider, you must first collect some information from the provider:

- **The provider's Entity ID**: A URI that identifies the identity provider.
- **The provider's SAML SSO URL**: The URL of the identity provider's sign-in page.
- **The provider's public key certificate**: The certificate used to validate tokens signed by the identity provider.
- **Your app's Entity ID**: A URI that identifies your app, the "service provider".

After you have the above information, enable SAML as a sign-in provider for your Firebase project:

1. [Add Firebase to your JavaScript project](https://firebase.google.com/docs/web/setup).

2. If you haven't upgraded toFirebase Authenticationwith Identity Platform, do so. SAML authentication is only available in upgraded projects.

3. On the[**Sign-in providers**](https://console.firebase.google.com/project/_/authentication/providers)page of theFirebaseconsole, click**Add new provider** , and then click**SAML**.

4. Give a name to this provider. Note the provider ID that's generated: something like`saml.example-provider`. You'll need this ID when you add sign-in code to your app.

5. Specify your identity provider's entity ID, SSO URL, and public key certificate. Also specify the entity ID of your app (the service provider). These values must exactly match the values your provider assigned to you.

6. Save your changes.

7. If you haven't already authorized your app's domain, add it to the allow list on the[**Authentication \> Settings**](https://console.firebase.google.com/project/_/authentication/settings)page of theFirebaseconsole.

## Handle the sign-in flow with the Firebase SDK

To handle the sign-in flow with the Firebase JavaScript SDK, follow these steps:

1. Create an instance of an`SAMLAuthProvider`using the provider ID you got in the Firebase console.

   ### Web

       import { SAMLAuthProvider } from "firebase/auth";

       const provider = new SAMLAuthProvider('saml.example-provider');

   ### Web

       var provider = new firebase.auth.SAMLAuthProvider('saml.example-provider');
       ``

<!-- -->

1. Authenticate with Firebase using the SAML provider object.

   You can either redirect the user to the provider's sign-in page or open the sign-in page in a pop-up browser window.

   **Redirect flow**

   Redirect to the provider sign-in page by calling`signInWithRedirect()`:  

   ### Web

       import { getAuth, signInWithRedirect } from "firebase/auth";

       const auth = getAuth();
       signInWithRedirect(auth, provider);

   ### Web

       firebase.auth().signInWithRedirect(provider);

   After the user completes sign-in and returns to your app, you can obtain the sign-in result by calling`getRedirectResult()`.  

   ### Web

       import { getAuth, getRedirectResult, SAMLAuthProvider } from "firebase/auth";

       const auth = getAuth();
       getRedirectResult(auth)
         .then((result) => {
           // User is signed in.

           // Provider data available using getAdditionalUserInfo()
         })
         .catch((error) => {
           // Handle error.
         });

   ### Web

       firebase.auth().getRedirectResult()
         .then((result) => {
           // User is signed in.

           // Provider data available in result.additionalUserInfo.profile,
           // or from the user's ID token obtained from result.user.getIdToken()
           // as an object in the firebase.sign_in_attributes custom claim.
         })
         .catch((error) => {
           // Handle error.
         });

   **Pop-up flow**

   ### Web

       import { getAuth, signInWithPopup, OAuthProvider } from "firebase/auth";

       const auth = getAuth();
       signInWithPopup(auth, provider)
         .then((result) => {
           // User is signed in.

           // Provider data available in result.additionalUserInfo.profile,
           // or from the user's ID token obtained from result.user.getIdToken()
           // as an object in the firebase.sign_in_attributes custom claim.
         })
         .catch((error) => {
           // Handle error.
         });

   ### Web

       firebase.auth().signInWithPopup(provider)
         .then((result) => {
           // User is signed in.

           // Provider data available in result.additionalUserInfo.profile,
           // or from the user's ID token obtained from result.user.getIdToken()
           // as an object in the firebase.sign_in_attributes custom claim.
         })
         .catch((error) => {
           // Handle error.
         });

   The ID token and[UserInfo](https://firebase.google.com/docs/reference/js/auth.userinfo#userinfoemail)object contains the user's email address only if it is provided in the`NameID`attribute of the SAML assertion from the identity provider:  

       <Subject>
         <NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">test@email.com</NameID>
       </Subject>

2. While the above examples focus on sign-in flows, you can use the same pattern to link a SAML provider to an existing user using`linkWithRedirect()`and`linkWithPopup()`, and re-authenticate a user with`reauthenticateWithRedirect()`and`reauthenticateWithPopup()`, which can be used to retrieve fresh credentials for sensitive operations that require recent login.