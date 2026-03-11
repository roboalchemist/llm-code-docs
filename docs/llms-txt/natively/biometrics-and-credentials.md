# Source: https://docs.buildnatively.com/guides/integration/biometrics-and-credentials.md

# Biometrics & Credentials

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)
* [Recommendations](#undefined)

More details: [Apple's biometrics authentication](https://developer.apple.com/design/human-interface-guidelines/ios/user-interaction/accounts#face-id-and-touch-id) & [Google's biometrics authentication](https://9to5google.com/2019/10/31/google-android-biometric-api/)

{% embed url="<https://youtu.be/-vHWtxwk8oY>" %}

### 🧋 Bubble.io Plugin

#### \[Element] Natively - Biometrics

#### Initialization:

On initialization, the element will try to check if the user has stored credentials for this hostname(your app). This value can be found in the **User has stored credentials** state value.

#### Events:

* **User's identity verified** - Get called after biometric successfully verified user's identity.
* **User's identity verification failed** - Get called after biometric failed to verify user's identity.
* **User's credentials not received** - Get called after biometric failed to verify user's identity.
* **User's credentials received** - Get called after the user's credentials are received after verifying identity.
* **User's credentials saved** - Get called after the user's credentials are saved after verifying identity.
* **User's credentials removed**
* **Biometrics supported** - get called when **Check biometrics support** finished
* **Biometrics not supported** - get called when **Check biometrics support** finished

#### States:

* **User's login after biometric authentication.** - User's stored login (can be an email/username or phone number whatever you're using for authorization)
* **User's password after biometric authentication.**
* **User's device supports biometrics.** - Yes/No. If the user's device supports biometrics.
* **User has stored credentials.** - Yes/No. Can help to identify if credentials for this app are already stored on a device.

#### Actions:

* **Check biometrics support**
  * allow\_passcode - yes/no allow users without FaceID/TouchID to use biometric verification.
* **Verify user's identity** - The system will call a native biometric authorization to confirm the user's identity.
  * allow\_passcode - yes/no allow users without FaceID/TouchID to use biometric verification.
* **Get user's credentials** - The system will call a native biometric authorization and, after successfully confirming the user's identity, try to get the user's credentials from the device [Keychain](https://en.wikipedia.org/wiki/Keychain_\(software\)) store (for iOS) and from private Local Storage (for Android).
  * allow\_passcode - yes/no allow users without FaceID/TouchID to use biometric verification.
* **Save user's credentials** - Same as the previous but for saving.
  * login - text
  * password - text
  * allow\_passcode - yes/no allow users without FaceID/TouchID to use biometric verification.
* **Remove user's credentials** - Remove user's credentials from a device.
* **Clear user's credentials from element** - Clears user's credentials from an element. (Call this after 'Get credentials')

### 🛠 JavaScript SDK

#### NativelyBiometrics

{% code overflow="wrap" lineNumbers="true" %}

```javascript
const allowPasscode = true; // Allow users without faceid/touchid use biometrics feature through regular phone passcode.
const biometrics = new NativelyBiometrics(allowPasscode)
const biometrics_support_callback = function (resp) {
    console.log(resp.status); // true/false
};
const biometrics_has_credentials_callback = function (resp) {
    console.log(resp.status); // true/false
};
const biometrics_remove_credentials_callback = function () {
    console.log("Creds was removed");
};
const biometrics_verify_callback = function (resp) {
    console.log(resp.status); // true/false
};
const biometrics_auth_callback = function (resp) {
    console.log(resp.status); // "SUCCESS_SAVE"/"SUCCESS_BIOMETRICS"/"FAILED_OBTAIN"/"FAILED_BIOMETRICS"
};
biometrics.checkBiometricsSupport(biometrics_support_callback);
biometrics.checkCredentials(biometrics_has_credentials_callback);
biometrics.verifyUserIdentify(biometrics_verify_callback);
biometrics.getUserCredentials(biometrics_auth_callback);
biometrics.saveUserCredentials(login, password, biometrics_auth_callback);
biometrics.removeUserCredentials(biometrics_remove_credentials_callback);
```

{% endcode %}

###

### Recommendations

* User's credentials are attached to your URL hostname (e.g. '<https://google.com/search>' -> hostname is 'google.com'), which means if the domain is changed, you will need to save the user's credentials on the device one more time.
* Update user's credentials on each Login or SignUp (To make sure you stored the correct one)
* Provide to your users the option to not use a Biometric authorization (for example add a checkbox on login/signup with text like 'Use biometric for next login' or add this functionality on settings)
