# Source: https://firebase.google.com/docs/auth/web/auth-state-persistence.md.txt

You can specify how the Authentication state persists when using the Firebase JS SDK. This includes the ability to specify whether a signed in user should be indefinitely persisted until explicit sign out, cleared when the window is closed or cleared on page reload.

For a web application, the default behavior is to persist a user's session even after the user closes the browser. This is convenient as the user is not required to continuously sign-in every time the web page is visited on the same device. This could require the user having to re-enter their password, send an SMS verification, etc, which could add a lot of friction to the user experience.

However, there are cases where this behavior may not be ideal:

- Applications with sensitive data may want to clear the state when the window or tab is closed. This is important in case the user forgets to sign out.
- Applications that are used on a device shared by multiple users. A common example here is an app running in a library computer.
- An application on a shared device that might be accessed by multiple users. The developer is unable to tell how that application is accessed and may want to provide a user with the ability to choose whether to persist their session or not. This could be done by adding a "Remember me" option during sign-in.
- In some situations, a developer may want to not persist an anonymous user until that user is upgraded to a non-anonymous account (federated, password, phone, etc.).
- A developer may want to allow different users to sign in to an application on different tabs. The default behavior is to persist the state across tabs for the same origin.

As stated above, there are multiple situations where the default permanent persistence may need to be overridden.
| **Note:** Do not confuse Auth state persistence with Firestore[offline data persistence](https://firebase.google.com/docs/firestore/manage-data/enable-offline). Auth state persistence specifies how a user session is persisted on a device. Whereas Firestore`enablePersistence`enables Cloud Firestore data caching when the device is offline.

## Supported types of Auth state persistence

You can choose one of three types of Auth state persistence on a specified Firebase Auth instance based on your application or user's requirements.

|                   Enum                   |   Value   |                                                                                                                                           Description                                                                                                                                           |
|------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `firebase.auth.Auth.Persistence.LOCAL`   | 'local'   | Indicates that the state will be persisted even when the browser window is closed or the activity is destroyed in React Native. An explicit sign out is needed to clear that state. Note that Firebase Auth web sessions are single host origin and will be persisted for a single domain only. |
| `firebase.auth.Auth.Persistence.SESSION` | 'session' | Indicates that the state will only persist in the current session or tab, and will be cleared when the tab or window in which the user authenticated is closed. Applies only to web apps.                                                                                                       |
| `firebase.auth.Auth.Persistence.NONE`    | 'none'    | Indicates that the state will only be stored in memory and will be cleared when the window or activity is refreshed.                                                                                                                                                                            |

## Modifying the Auth state persistence

You can specify or modify the existing type of persistence by calling the`firebase.auth().setPersistence`method:  

### Web

```javascript
import { getAuth, setPersistence, signInWithEmailAndPassword, browserSessionPersistence } from "firebase/auth";

const auth = getAuth();
setPersistence(auth, browserSessionPersistence)
  .then(() => {
    // Existing and future Auth states are now persisted in the current
    // session only. Closing the window would clear any existing state even
    // if a user forgets to sign out.
    // ...
    // New sign-in will be persisted with session persistence.
    return signInWithEmailAndPassword(auth, email, password);
  })
  .catch((error) => {
    // Handle Errors here.
    const errorCode = error.code;
    const errorMessage = error.message;
  });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/auth-state-persistence/auth_set_persistence_session.js#L8-L24
```

### Web

```javascript
firebase.auth().setPersistence(firebase.auth.Auth.Persistence.SESSION)
  .then(() => {
    // Existing and future Auth states are now persisted in the current
    // session only. Closing the window would clear any existing state even
    // if a user forgets to sign out.
    // ...
    // New sign-in will be persisted with session persistence.
    return firebase.auth().signInWithEmailAndPassword(email, password);
  })
  .catch((error) => {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;
  });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/auth-state-persistence.js#L12-L25
```

This will change the type of persistence on the specified Auth instance for the currently saved Auth session and apply this type of persistence for future sign-in requests, including sign-in with redirect requests. This will return a promise that will resolve once the state finishes copying from one type of storage to the other. Calling a sign-in method after changing persistence will wait for that persistence change to complete before applying it on the new Auth state.

The default for web browser and React Native apps is`local`(provided the browser supports this storage mechanism, eg. 3rd party cookies/data are enabled) whereas it is`none`for Node.js backend apps.

## Overview of persistence behavior

The following criteria will be applied when determining the current state of persistence.

- Initially, the SDK will check if an authenticated user exists. Unless`setPersistence`is called, that user's current persistence type will be applied for future sign-in attempts. So if that user was persisted in`session`on a previous web page and a new page was visited, signing in again with a different user will result in that user's state being also saved with`session`persistence.
- If no user is signed in and no persistence is specified, the default setting will be applied (`local`in a browser app).
- If no user is signed in and a new type of persistence is set, any future sign-in attempt will use that type of persistence.
- If the user is signed in and persistence type is modified, that existing signed in user will change persistence to the new one. All future sign-in attempts will use that new persistence.
- When signInWithRedirect is called, the current persistence type is retained and applied at the end of the OAuth flow to the newly signed in user, even if the persistence was`none`. If the persistence is explicitly specified on that page, it will override the retained auth state persistence from the previous page that started the redirect flow.

  ### Web

  ```javascript
  import { getAuth, setPersistence, signInWithRedirect, inMemoryPersistence, GoogleAuthProvider } from "firebase/auth";

  const auth = getAuth();
  setPersistence(auth, inMemoryPersistence)
    .then(() => {
      const provider = new GoogleAuthProvider();
      // In memory persistence will be applied to the signed in Google user
      // even though the persistence was set to 'none' and a page redirect
      // occurred.
      return signInWithRedirect(auth, provider);
    })
    .catch((error) => {
      // Handle Errors here.
      const errorCode = error.code;
      const errorMessage = error.message;
    });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/auth-state-persistence/auth_set_persistence_none.js#L8-L23
  ```

  ### Web

  ```javascript
  firebase.auth().setPersistence(firebase.auth.Auth.Persistence.NONE)
    .then(() => {
      var provider = new firebase.auth.GoogleAuthProvider();
      // In memory persistence will be applied to the signed in Google user
      // even though the persistence was set to 'none' and a page redirect
      // occurred.
      return firebase.auth().signInWithRedirect(provider);
    })
    .catch((error) => {
      // Handle Errors here.
      var errorCode = error.code;
      var errorMessage = error.message;
    });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/auth-state-persistence.js#L31-L43
  ```

## Expected behavior across browser tabs

The following expected behavior will apply when different persistence types are used in different tabs. The requirement is that at any point, there should never be multiple types of saved states at the same time (eg. auth state saved in`session`and`local`types of storage):

- Users can sign in using`session`or`none`persistence with different users on multiple tabs. Each tab cannot see the state of the other tab.
- Any attempt to sign in using`local`persistence will be detected and synchronized on all tabs. If the user was previously signed in on a specific tab using`session`or`none`persistence, that state will be cleared.
- If the user was previously signed in using`local`persistence with multiple tabs opened and then switches to`none`or`session`persistence in one tab, the state of that tab will be modified with the user persisted in`session`or`none`and on all other tabs, the user will be signed out.