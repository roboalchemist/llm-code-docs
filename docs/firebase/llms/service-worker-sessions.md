# Source: https://firebase.google.com/docs/auth/web/service-worker-sessions.md.txt

Firebase Auth provides the ability to use service workers to detect and pass Firebase ID tokens for session management. This provides the following benefits:

- Ability to pass an ID token on every HTTP request from the server without any additional work.
- Ability to refresh the ID token without any additional round trip or latencies.
- Backend and frontend synchronized sessions. Applications that need to access Firebase services such as Realtime Database, Firestore, etc and some external server side resource (SQL database, etc) can use this solution. In addition, the same session can also be accessed from the service worker, web worker or shared worker.
- Eliminates the need to include Firebase Auth source code on each page (reduces latency). The service worker, loaded and initialized once, would handle session management for all clients in the background.

## Overview

Firebase Auth is optimized to run on the client side. Tokens are saved in web storage. This makes it easy to also integrate with other Firebase services such as Realtime Database, Cloud Firestore, Cloud Storage, etc. To manage sessions from a server side perspective, ID tokens have to be retrieved and passed to the server.  

### Web

```javascript
import { getAuth, getIdToken } from "firebase/auth";

const auth = getAuth();
getIdToken(auth.currentUser)
  .then((idToken) => {
    // idToken can be passed back to server.
  })
  .catch((error) => {
    // Error occurred.
  });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/service-worker-sessions/auth_svc_get_idtoken.js#L8-L17
```

### Web

```javascript
firebase.auth().currentUser.getIdToken()
  .then((idToken) => {
    // idToken can be passed back to server.
  })
  .catch((error) => {
    // Error occurred.
  });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/service-worker-sessions.js#L11-L17
```

However, this means that some script has to run from the client to get the latest ID token and then pass it to the server via the request header, POST body, etc.

This may not scale and instead server side session cookies may be needed. ID tokens can be set as session cookies but these are short lived and will need to be refreshed from the client and then set as new cookies on expiration which may require an additional round trip if the user had not visited the site in a while.

While Firebase Auth provides a more traditional[cookie based session management solution](https://firebase.google.com/docs/auth/admin/manage-sessions), this solution works best for server side`httpOnly`cookie based applications and is harder to manage as the client tokens and server side tokens could get out of sync, especially if you also need to use other client based Firebase services.

Instead, service workers can be used to manage user sessions for server side consumption. This works because of the following:

- Service workers have access to the current Firebase Auth state. The current user ID token can be retrieved from the service worker. If the token is expired, the client SDK will refresh it and return a new one.
- Service workers can intercept fetch requests and modify them.

## Service worker changes

The service worker will need to include the Auth library and the ability to get the current ID token if a user is signed in.  

### Web

```javascript
import { initializeApp } from "firebase/app";
import { getAuth, onAuthStateChanged, getIdToken } from "firebase/auth";

// Initialize the Firebase app in the service worker script.
initializeApp(config);

/**
 * Returns a promise that resolves with an ID token if available.
 * @return {!Promise<?string>} The promise that resolves with an ID token if
 *     available. Otherwise, the promise resolves with null.
 */
const auth = getAuth();
const getIdTokenPromise = () => {
  return new Promise((resolve, reject) => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      unsubscribe();
      if (user) {
        getIdToken(user).then((idToken) => {
          resolve(idToken);
        }, (error) => {
          resolve(null);
        });
      } else {
        resolve(null);
      }
    });
  });
};https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/service-worker-sessions/auth_svc_subscribe.js#L8-L35
```

### Web

```javascript
// Initialize the Firebase app in the service worker script.
firebase.initializeApp(config);

/**
 * Returns a promise that resolves with an ID token if available.
 * @return {!Promise<?string>} The promise that resolves with an ID token if
 *     available. Otherwise, the promise resolves with null.
 */
const getIdToken = () => {
  return new Promise((resolve, reject) => {
    const unsubscribe = firebase.auth().onAuthStateChanged((user) => {
      unsubscribe();
      if (user) {
        user.getIdToken().then((idToken) => {
          resolve(idToken);
        }, (error) => {
          resolve(null);
        });
      } else {
        resolve(null);
      }
    });
  });
};https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/service-worker-sessions.js#L23-L46
```

All fetch requests to the app's origin will be intercepted and if an ID token is available, appended to the request via the header. Server side, request headers will be checked for the ID token, verified and processed. In the service worker script, the fetch request would be intercepted and modified.  

### Web

```javascript
const getOriginFromUrl = (url) => {
  // https://stackoverflow.com/questions/1420881/how-to-extract-base-url-from-a-string-in-javascript
  const pathArray = url.split('/');
  const protocol = pathArray[0];
  const host = pathArray[2];
  return protocol + '//' + host;
};

// Get underlying body if available. Works for text and json bodies.
const getBodyContent = (req) => {
  return Promise.resolve().then(() => {
    if (req.method !== 'GET') {
      if (req.headers.get('Content-Type').indexOf('json') !== -1) {
        return req.json()
          .then((json) => {
            return JSON.stringify(json);
          });
      } else {
        return req.text();
      }
    }
  }).catch((error) => {
    // Ignore error.
  });
};

self.addEventListener('fetch', (event) => {
  /** @type {FetchEvent} */
  const evt = event;

  const requestProcessor = (idToken) => {
    let req = evt.request;
    let processRequestPromise = Promise.resolve();
    // For same origin https requests, append idToken to header.
    if (self.location.origin == getOriginFromUrl(evt.request.url) &&
        (self.location.protocol == 'https:' ||
         self.location.hostname == 'localhost') &&
        idToken) {
      // Clone headers as request headers are immutable.
      const headers = new Headers();
      req.headers.forEach((val, key) => {
        headers.append(key, val);
      });
      // Add ID token to header.
      headers.append('Authorization', 'Bearer ' + idToken);
      processRequestPromise = getBodyContent(req).then((body) => {
        try {
          req = new Request(req.url, {
            method: req.method,
            headers: headers,
            mode: 'same-origin',
            credentials: req.credentials,
            cache: req.cache,
            redirect: req.redirect,
            referrer: req.referrer,
            body,
            // bodyUsed: req.bodyUsed,
            // context: req.context
          });
        } catch (e) {
          // This will fail for CORS requests. We just continue with the
          // fetch caching logic below and do not pass the ID token.
        }
      });
    }
    return processRequestPromise.then(() => {
      return fetch(req);
    });
  };
  // Fetch the resource after checking for the ID token.
  // This can also be integrated with existing logic to serve cached files
  // in offline mode.
  evt.respondWith(getIdTokenPromise().then(requestProcessor, requestProcessor));
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/service-worker-sessions/auth_svc_intercept.js#L8-L81
```

### Web

```javascript
const getOriginFromUrl = (url) => {
  // https://stackoverflow.com/questions/1420881/how-to-extract-base-url-from-a-string-in-javascript
  const pathArray = url.split('/');
  const protocol = pathArray[0];
  const host = pathArray[2];
  return protocol + '//' + host;
};

// Get underlying body if available. Works for text and json bodies.
const getBodyContent = (req) => {
  return Promise.resolve().then(() => {
    if (req.method !== 'GET') {
      if (req.headers.get('Content-Type').indexOf('json') !== -1) {
        return req.json()
          .then((json) => {
            return JSON.stringify(json);
          });
      } else {
        return req.text();
      }
    }
  }).catch((error) => {
    // Ignore error.
  });
};

self.addEventListener('fetch', (event) => {
  /** @type {FetchEvent} */
  const evt = event;

  const requestProcessor = (idToken) => {
    let req = evt.request;
    let processRequestPromise = Promise.resolve();
    // For same origin https requests, append idToken to header.
    if (self.location.origin == getOriginFromUrl(evt.request.url) &&
        (self.location.protocol == 'https:' ||
         self.location.hostname == 'localhost') &&
        idToken) {
      // Clone headers as request headers are immutable.
      const headers = new Headers();
      req.headers.forEach((val, key) => {
        headers.append(key, val);
      });
      // Add ID token to header.
      headers.append('Authorization', 'Bearer ' + idToken);
      processRequestPromise = getBodyContent(req).then((body) => {
        try {
          req = new Request(req.url, {
            method: req.method,
            headers: headers,
            mode: 'same-origin',
            credentials: req.credentials,
            cache: req.cache,
            redirect: req.redirect,
            referrer: req.referrer,
            body,
            // bodyUsed: req.bodyUsed,
            // context: req.context
          });
        } catch (e) {
          // This will fail for CORS requests. We just continue with the
          // fetch caching logic below and do not pass the ID token.
        }
      });
    }
    return processRequestPromise.then(() => {
      return fetch(req);
    });
  };
  // Fetch the resource after checking for the ID token.
  // This can also be integrated with existing logic to serve cached files
  // in offline mode.
  evt.respondWith(getIdToken().then(requestProcessor, requestProcessor));
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/service-worker-sessions.js#L57-L130
```

As a result, all authenticated requests will always have an ID token passed in the header without additional processing.

In order for the service worker to detect Auth state changes, it has to be installed on the sign-in/sign-up page. Make sure that the service worker is bundled so that it will still work after the browser has been closed.

After installation, the service worker has to call`clients.claim()`on activation so it can be setup as controller for the current page.  

### Web

```javascript
self.addEventListener('activate', (event) => {
  event.waitUntil(clients.claim());
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/service-worker-sessions/auth_svc_listen_activate.js#L8-L10
```

### Web

```javascript
self.addEventListener('activate', (event) => {
  event.waitUntil(clients.claim());
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/service-worker-sessions.js#L136-L138
```

## Client side changes

The service worker, if supported, needs to be installed on the client side sign-in/sign-up page.  

### Web

```javascript
// Install servicerWorker if supported on sign-in/sign-up page.
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/service-worker.js', {scope: '/'});
}https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/service-worker-sessions/auth_svc_register.js#L8-L11
```

### Web

```javascript
// Install servicerWorker if supported on sign-in/sign-up page.
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/service-worker.js', {scope: '/'});
}https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/service-worker-sessions.js#L144-L147
```

When the user is signed in and redirected to another page, the service worker will be able to inject the ID token in the header before the redirect completes.  

### Web

```javascript
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";

// Sign in screen.
const auth = getAuth();
signInWithEmailAndPassword(auth, email, password)
  .then((result) => {
    // Redirect to profile page after sign-in. The service worker will detect
    // this and append the ID token to the header.
    window.location.assign('/profile');
  })
  .catch((error) => {
    // Error occurred.
  });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/service-worker-sessions/auth_svc_sign_in_email.js#L8-L20
```

### Web

```javascript
// Sign in screen.
firebase.auth().signInWithEmailAndPassword(email, password)
  .then((result) => {
    // Redirect to profile page after sign-in. The service worker will detect
    // this and append the ID token to the header.
    window.location.assign('/profile');
  })
  .catch((error) => {
    // Error occurred.
  });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/service-worker-sessions.js#L153-L162
```

## Server side changes

The server side code will be able to detect the ID token on every request. This behavior is supported by the Admin SDK for Node.js or with the Web SDK using`FirebaseServerApp`.  

### Node.js

      // Server side code.
      const admin = require('firebase-admin');

      // The Firebase Admin SDK is used here to verify the ID token.
      admin.initializeApp();

      function getIdToken(req) {
        // Parse the injected ID token from the request header.
        const authorizationHeader = req.headers.authorization || '';
        const components = authorizationHeader.split(' ');
        return components.length > 1 ? components[1] : '';
      }

      function checkIfSignedIn(url) {
        return (req, res, next) => {
          if (req.url == url) {
            const idToken = getIdToken(req);
            // Verify the ID token using the Firebase Admin SDK.
            // User already logged in. Redirect to profile page.
            admin.auth().verifyIdToken(idToken).then((decodedClaims) => {
              // User is authenticated, user claims can be retrieved from
              // decodedClaims.
              // In this sample code, authenticated users are always redirected to
              // the profile page.
              res.redirect('/profile');
            }).catch((error) => {
              next();
            });
          } else {
            next();
          }
        };
      }

      // If a user is signed in, redirect to profile page.
      app.use(checkIfSignedIn('/'));  
    https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/service-worker-sessions.js#L170-L205

### Web modular API

    import { initializeServerApp } from 'firebase/app';
    import { getAuth } from 'firebase/auth';
    import { headers } from 'next/headers';
    import { redirect } from 'next/navigation';

    export default function MyServerComponent() {

        // Get relevant request headers (in Next.JS)
        const authIdToken = headers().get('Authorization')?.split('Bearer ')[1];

        // Initialize the FirebaseServerApp instance.
        const serverApp = initializeServerApp(firebaseConfig, { authIdToken });

        // Initialize Firebase Authentication using the FirebaseServerApp instance.
        const auth = getAuth(serverApp);

        if (auth.currentUser) {
            redirect('/profile');
        }

        // ...
    }  
    https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firebaseserverapp-next/firebaseserverapp.js#L3-L24

## Conclusion

In addition, since ID tokens will be set via the service workers, and service workers are restricted to run from the same origin, there is no risk of CSRF since a website of different origin attempting to call your endpoints will fail to invoke the service worker, causing the request to appear unauthenticated from the server's perspective.

While service workers are now supported in all modern major browsers, some older browsers do not support them. As a result, some fallback may be needed to pass the ID token to your server when service workers are not available or an app can be restricted to only run on browsers that support service workers.

Note that services workers are single origin only and will only be installed on websites served via https connection or localhost.

Learn more about about browser support for service worker at[caniuse.com](https://caniuse.com/#feat=serviceworkers).

## Useful links

- For more information on using service workers for session management, check out the[sample app source code on GitHub](https://github.com/FirebaseExtended/firebase-auth-service-worker-sessions).
- A deployed sample app of the above is available at<https://auth-service-worker.appspot.com>