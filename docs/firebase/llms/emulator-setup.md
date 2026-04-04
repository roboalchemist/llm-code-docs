# Source: https://firebase.google.com/docs/rules/emulator-setup.md.txt

<br />

The Firebase Emulators make it easier to fully validate your app's behavior and verify yourFirebase Security Rulesconfigurations. Use the Firebase Emulators to run and automate unit tests in a local environment.
| **Beta**
|
| Some of the Firebase Emulators are currently in Beta. These products might be changed in backward-incompatible ways and are not subject to any SLA or deprecation policy. As always, feedback is greatly appreciated. Let us know what you think!

## Install the Firebase Emulators

Before you begin make sure you have installed the[Firebase CLI](https://firebase.google.com/docs/cli)and configured the[Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite/install_and_configure)

Start the emulator using the following command. The emulator runs during all your tests.  

### Cloud Firestore

```text
 firebase emulators:start --only firestore
 
```

### Realtime Database

```text
 firebase emulators:start --only database
 
```

### Cloud Storage

```text
 firebase emulators:start --only storage
 
```

## Set up tests and run the emulator

Now that you've installed the emulator,[set up tests](https://firebase.google.com/docs/rules/unit-tests)and[generate reports](https://firebase.google.com/docs/rules/emulator-reports)to validate your rules' behavior before you deploy them to production.

## Quickstart

For a few basic test cases with simple rules, try out the[testing quickstart](https://github.com/firebase/quickstart-testing).