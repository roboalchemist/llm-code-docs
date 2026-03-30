# Source: https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-1.md.txt

# Tutorial: Measure iOS Ads conversions

## Step 1: Implement a sign-in experience

<br />

|---|
| Introduction: [Measure iOS Ads conversions](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/index-first-party) |
| **Step 1: Implement a sign-in experience** <br /> |
| Step 2: [Integrate Google Analytics](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-2) |
| Step 3: [Initiate on-device conversion measurement using Google Analytics](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3) |
| Step 4: [Troubleshoot and handle common issues](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-4) |

<br />

The first step is to implement a sign-in experience to allow users to provide
their email addresses or phone number.

**The authentication system that you use must provide an email address or
phone number associated with the user.** The following steps outline the process
for securely collecting sign-in information using Firebase Authentication, but you
can skip this step if you already have an authentication system that collects
user emails or phone numbers and continue to [Step 2: Integrate Google Analytics](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-2).

<br />

**Make sure you have the prerequisites for this tutorial**

<br />

- Your own app that can run on iOS 12 or higher

- Your app registered as a Firebase App that's linked to Google Analytics
  and Ads

- Your preferred IDE

  <br />

<br />

### Set up an authentication system

#### Use a Firebase Authentication sign-in method

You can use Firebase Authentication to allow users to sign in to your app using one or
more sign-in methods, including email address, phone number, password sign-in,
and federated identity providers (like Google, Facebook or Twitter).
Please review [Get started with Firebase Authentication](https://firebase.google.com/docs/auth/ios/start).

#### Integrate Firebase Authentication with a custom authentication system

Alternatively, you can integrate Firebase Authentication with a custom
authentication system by modifying your authentication server to produce custom
signed tokens when a user successfully signs in. Your app receives this token
and uses it to authenticate with Firebase. Please review [Get started with a custom
authentication system](https://firebase.google.com/docs/auth/ios/custom-auth).

### Get the authenticated user's email address or phone number

After you've set up an authentication system with Firebase Authentication, you can
get the currently signed-in user.

The recommended way to get the current user is by setting a listener on the
`Auth` object:

### Swift

```swift
handle = Auth.auth().addStateDidChangeListener { auth, user in
  // Get the user's email address
  let email = user.email
  // or get their phone number
  let phoneNumber = user.phoneNumber
  // ...
}
```

### Objective-C

```objective-c
self.handle = [[FIRAuth auth]
  addAuthStateDidChangeListener:^(FIRAuth *_Nonnull auth, FIRUser *_Nullable user) {
    // Get the user's email address
    NSString *email = user.email;
    // or get their phone number
    NSString *phoneNumber = user.phoneNumber;
    // ...
  }];
```

### Unity

```c#
Firebase.Auth.FirebaseAuth auth;
Firebase.Auth.FirebaseUser user;

// Handle initialization of the necessary firebase modules:
void InitializeFirebase() {
  auth = Firebase.Auth.FirebaseAuth.DefaultInstance;
  auth.StateChanged += AuthStateChanged;
  AuthStateChanged(this, null);
}

// Track state changes of the auth object.
void AuthStateChanged(object sender, System.EventArgs eventArgs) {
  if (auth.CurrentUser != user) {
    bool signedIn = user != auth.CurrentUser && auth.CurrentUser != null;
    user = auth.CurrentUser;
    if (signedIn) {
      // Get the user's email address
      string email = user.Email;
      // or get their phone number
      string phoneNumber = user.PhoneNumber;
      // ...
    }
  }
}

// Handle removing subscription and reference to the Auth instance.
// Automatically called by a Monobehaviour after Destroy is called on it.
void OnDestroy() {
  auth.StateChanged -= AuthStateChanged;
  auth = null;
}
```

> [!NOTE]
> **Note:** Find more code examples demonstrating Firebase Authentication in the [Firebase quickstarts](https://github.com/firebase/quickstart-ios).

<br />

*** ** * ** ***

<br />

[**Introduction**](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/index-first-party)
[**Step 2** : Integrate Google Analytics](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-2)

<br />

*** ** * ** ***