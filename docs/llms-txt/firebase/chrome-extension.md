# Source: https://firebase.google.com/docs/auth/web/chrome-extension.md.txt

This document shows you how to useFirebase Authenticationto sign users into a Chrome extension that uses[Manifest V3](https://developer.chrome.com/docs/extensions/mv3/intro/).

Firebase Authenticationprovides multiple authentication methods to sign in users from a Chrome extension, some requiring more development effort than others.

To use the following methods in a Manifest V3 Chrome extension, you need only[import them from`firebase/auth/web-extension`](https://firebase.google.com/docs/auth/web/chrome-extension#use-web-extension):

- Sign in with email and password (`createUserWithEmailAndPassword`and`signInWithEmailAndPassword`)
- Sign in with email link (`sendSignInLinkToEmail`,`isSignInWithEmailLink`, and`signInWithEmailLink`)
- Sign in anonymously (`signInAnonymously`)
- Sign in with a custom authentication system (`signInWithCustomToken`)
- Handle provider sign-in independently then use`signInWithCredential`

The following sign in methods are also supported but require some additional work:

- Sign in with a pop-up window (`signInWithPopup`,`linkWithPopup`, and`reauthenticateWithPopup`)
- Sign in by redirecting to the sign-in page (`signInWithRedirect`,`linkWithRedirect`, and`reauthenticateWithRedirect`)
- Sign in with Phone Number with reCAPTCHA
- SMS multi-factor authentication with reCAPTCHA
- reCAPTCHA Enterprise protection

To use these methods in a Manifest V3 Chrome extension, you must use[Offscreen Documents](https://firebase.google.com/docs/auth/web/chrome-extension#use_offscreen_documents).

## Use the firebase/auth/web-extension entry point

Importing from`firebase/auth/web-extension`makes signing in users from a Chrome extension similar to a web app.

firebase/auth/web-extension is only supported on the Web SDK versions v10.8.0 and above.  

```javascript
import { getAuth, signInWithEmailAndPassword } from 'firebase/auth/web-extension';

const auth = getAuth();
signInWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    // Signed in
    const user = userCredential.user;
    // ...
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
  });
```

## Use Offscreen Documents

Some authentication methods, such as`signInWithPopup`,`linkWithPopup`, and`reauthenticateWithPopup`, aren't directly compatible with Chrome extensions, because they require code to be loaded from outside of the extension package. Starting in Manifest V3, this isn't allowed and will be blocked by the extension platform. To get around this, you can load that code within an iframe using an[offscreen document](https://developer.chrome.com/docs/extensions/reference/api/offscreen). In the offscreen document, implement the normal authentication flow and proxy the result from the offscreen document back to the extension.

This guide uses`signInWithPopup`as an example, but the same concept applies to other authentication methods.

### Before you begin

This technique requires you to set up a web page that is available on the web, that you will load in an iframe. Any host works for this, including[Firebase Hosting](https://firebase.google.com/docs/hosting/quickstart). Create a website with the following content:  

```html
<!DOCTYPE html>
<html>
  <head>
    <title>signInWithPopup</title>
    <script src="signInWithPopup.js"></script>
  </head>
  <body><h1>signInWithPopup</h1></body>
</html>
```

#### Federated sign in

If you are using federated sign in, such as sign in with Google, Apple, SAML, or OIDC, you must add your Chrome extension ID to the list of authorized domains:

1. Open your project in the[Firebaseconsole](https://console.firebase.google.com/).
2. In the**Authentication** section, open the**Settings**page.
3. Add a URI like the following to the list of Authorized Domains:  

   ```
   chrome-extension://CHROME_EXTENSION_ID
   ```

In your Chrome extension's manifest file make sure that you add the following URLs to the`content_security_policy`allowlist:

- `https://apis.google.com`
- `https://www.gstatic.com`
- `https://www.googleapis.com`
- `https://securetoken.googleapis.com`

### Implement authentication

In your HTML document, signInWithPopup.js is the JavaScript code that handles authentication. There are two different ways to implement a method that is directly supported in the extension:

- Use`firebase/auth/web-extension`in your extension code such as background scripts, service workers, or popup scripts. Use`firebase/auth`only inside your offscreen iframe, because that iframe runs in a standard web page context.
- Wrap the authentication logic in a[`postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)listener, in order to proxy the authentication request and response.

```javascript
import { signInWithPopup, GoogleAuthProvider, getAuth } from'firebase/auth';
import { initializeApp } from 'firebase/app';
import firebaseConfig from './firebaseConfig.js'

const app = initializeApp(firebaseConfig);
const auth = getAuth();

// This code runs inside of an iframe in the extension's offscreen document.
// This gives you a reference to the parent frame, i.e. the offscreen document.
// You will need this to assign the targetOrigin for postMessage.
const PARENT_FRAME = document.location.ancestorOrigins[0];

// This demo uses the Google auth provider, but any supported provider works.
// Make sure that you enable any provider you want to use in the Firebase Console.
// https://console.firebase.google.com/project/_/authentication/providers
const PROVIDER = new GoogleAuthProvider();

function sendResponse(result) {
  globalThis.parent.self.postMessage(JSON.stringify(result), PARENT_FRAME);
}

globalThis.addEventListener('message', function({data}) {
  if (data.initAuth) {
    // Opens the Google sign-in page in a popup, inside of an iframe in the
    // extension's offscreen document.
    // To centralize logic, all respones are forwarded to the parent frame,
    // which goes on to forward them to the extension's service worker.
    signInWithPopup(auth, PROVIDER)
      .then(sendResponse)
      .catch(sendResponse)
  }
});
```

### Build your Chrome Extension

After your website is live, you can use it in your Chrome Extension.

<br />

1. Add the`offscreen`permission to your manifest.json file:  

```javascript
    {
      "name": "signInWithPopup Demo",
      "manifest_version" 3,
      "background": {
        "service_worker": "background.js"
      },
      "permissions": [
        "offscreen"
      ]
    }
    
```
2. Create the offscreen document itself. This is a minimal HTML file inside of your extension package that loads the logic of your offscreen document JavaScript:  

```html
    <!DOCTYPE html>
    <script src="./offscreen.js"></script>
    
```
3. Include`offscreen.js`in your extension package. It acts as the proxy between the public website set up in step 1 and your extension.  

```javascript
    // This URL must point to the public site
    const _URL = 'https://example.com/signInWithPopupExample';
    const iframe = document.createElement('iframe');
    iframe.src = _URL;
    document.documentElement.appendChild(iframe);
    chrome.runtime.onMessage.addListener(handleChromeMessages);

    function handleChromeMessages(message, sender, sendResponse) {
      // Extensions may have an number of other reasons to send messages, so you
      // should filter out any that are not meant for the offscreen document.
      if (message.target !== 'offscreen') {
        return false;
      }

      function handleIframeMessage({data}) {
        try {
          if (data.startsWith('!_{')) {
            // Other parts of the Firebase library send messages using postMessage.
            // You don't care about them in this context, so return early.
            return;
          }
          data = JSON.parse(data);
          self.removeEventListener('message', handleIframeMessage);

          sendResponse(data);
        } catch (e) {
          console.log(`json parse failed - ${e.message}`);
        }
      }

      globalThis.addEventListener('message', handleIframeMessage, false);

      // Initialize the authentication flow in the iframed document. You must set the
      // second argument (targetOrigin) of the message in order for it to be successfully
      // delivered.
      iframe.contentWindow.postMessage({"initAuth": true}, new URL(_URL).origin);
      return true;
    }
    
```
4. Set up the offscreen document from your background.js service worker.  

```javascript
    import { getAuth } from 'firebase/auth/web-extension';

    const OFFSCREEN_DOCUMENT_PATH = '/offscreen.html';

    // A global promise to avoid concurrency issues
    let creatingOffscreenDocument;

    // Chrome only allows for a single offscreenDocument. This is a helper function
    // that returns a boolean indicating if a document is already active.
    async function hasDocument() {
      // Check all windows controlled by the service worker to see if one
      // of them is the offscreen document with the given path
      const matchedClients = await clients.matchAll();
      return matchedClients.some(
        (c) => c.url === chrome.runtime.getURL(OFFSCREEN_DOCUMENT_PATH)
      );
    }

    async function setupOffscreenDocument(path) {
      // If we do not have a document, we are already setup and can skip
      if (!(await hasDocument())) {
        // create offscreen document
        if (creating) {
          await creating;
        } else {
          creating = chrome.offscreen.createDocument({
            url: path,
            reasons: [
                chrome.offscreen.Reason.DOM_SCRAPING
            ],
            justification: 'authentication'
          });
          await creating;
          creating = null;
        }
      }
    }

    async function closeOffscreenDocument() {
      if (!(await hasDocument())) {
        return;
      }
      await chrome.offscreen.closeDocument();
    }

    function getAuth() {
      return new Promise(async (resolve, reject) => {
        const auth = await chrome.runtime.sendMessage({
          type: 'firebase-auth',
          target: 'offscreen'
        });
        auth?.name !== 'FirebaseError' ? resolve(auth) : reject(auth);
      })
    }

    async function firebaseAuth() {
      await setupOffscreenDocument(OFFSCREEN_DOCUMENT_PATH);

      const auth = await getAuth()
        .then((auth) => {
          console.log('User Authenticated', auth);
          return auth;
        })
        .catch(err => {
          if (err.code === 'auth/operation-not-allowed') {
            console.error('You must enable an OAuth provider in the Firebase' +
                          ' console in order to use signInWithPopup. This sample' +
                          ' uses Google by default.');
          } else {
            console.error(err);
            return err;
          }
        })
        .finally(closeOffscreenDocument)

      return auth;
    }
    
```
5. Now, when you call`firebaseAuth()`within your service worker, it will create the offscreen document and load the site in an iframe. That iframe will process in the background, and Firebase will go through the standard authentication flow. Once it has either been resolved or rejected, the authentication object will be proxied from your iframe to your service worker, using the offscreen document.