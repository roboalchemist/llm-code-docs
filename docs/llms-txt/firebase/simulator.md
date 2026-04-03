# Source: https://firebase.google.com/docs/rules/simulator.md.txt

<br />

To quickly test your updatedFirebase Security Rulesin theFirebaseconsole, use the Rules Playground.
| **Note:** To fully validate your app's behavior and verify yourFirebase Security Rules  
| configurations, use the[Firebase Emulator](https://firebase.google.com/docs/rules/emulator-setup)to run and automate unit tests in a local environment.

The Rules Playground is a convenient tool to use as you're exploring new behaviors or quickly validating rules as you write them. It displays a message confirming that access was either allowed or denied according to the parameters you set for the simulation.

## Use the Rules Playground

![](https://firebase.google.com/static/docs/firestore/images/playground-firestore.png)

1. Open the[Firebaseconsole](https://console.firebase.google.com/)and select your project.
2. Then, from the product navigation, do one of the following:
   - Select**Realtime Database** ,**Cloud Firestore** , or**Storage** , as appropriate, then click**Rules** to navigate to theRuleseditor.
3. Once you've made your edits, click**Rules Playground**from the editor.
4. In the*Rules Playground* settings, select options for your test, including:
   - Testing reads or writes.
   - A specific**Location**in your database or storage bucket, as a path.
   - Authentication type --- unauthenticated, authenticated anonymous user, or a specific user ID.
   - Document-specific data that your rules specifically reference (for example, if your rules require the presence of a specific field before allowing a write).
5. Click**Run**and look for the results in the banner above the editor.

## Sample Rules Playground scenario

Test the Rules Playground behavior with the following sample scenario and basic rules.  

### Cloud Firestore

    service cloud.firestore {
      match /databases/{database}/documents {
        // Allow only authenticated content owners access
        match /some_collection/{document} {
          allow read, write: if request.auth != null && request.auth.uid == request.resource.data.author_uid
          }
        }
      }

### Realtime Database

<br />

```scilab
 // These rules grant access to a node matching the authenticated
 // user's ID from the Firebase auth token
 {
   "rules": {
     "users": {
       "$uid": {
         ".read": "$uid === auth.uid",
         ".write": "$uid === auth.uid"
       }
     }
   }
 }
 
```

<br />

### Cloud Storage

    // Grants a user access to a node matching their user ID
    service firebase.storage {
      match /b/{bucket}/o {
        // Files look like: "user/&lt;UID&gt;/file.txt"
        match /user/{userId}/{fileName} {
          allow read, write: if request.auth != null && request.auth.uid == userId;
        }
      }
    }

- In theRuleseditor, add the rule given.

- ![](https://firebase.google.com/static/docs/rules/images/playground-test.png)Select**get** from the**Simulation type** drop-down menu and enter a valid path in the**Location**field.

- Toggle on**Authentication** and select an authentication type from the**Provider**drop-down.

- Enter the user ID details and click**Run**.

The results of the simulation appear at the top of the editor. Depending on the user ID details you entered, you should see a banner confirming the read was either successfully allowed or denied.