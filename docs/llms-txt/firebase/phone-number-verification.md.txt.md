# Source: https://firebase.google.com/docs/phone-number-verification.md.txt

# Firebase Phone Number Verification

# Firebase Phone Number Verification

Firebase Phone Number Verification (Firebase PNV) is a fast and secure method for verifying user phone
numbers. Unlike SMS-based verification, which requires users to receive and
input a code from a text message, Firebase PNV works by getting the phone number for
the SIM in the device directly from the connected carrier with a single tap. This
reduces friction for the user, improves reliability by not depending on SMS
message delivery, and eliminates abuse vectors commonly exploited when using SMS.

## Key capabilities

|---|---|
| Carriers are the source of truth | With Firebase PNV, Google obtains the verified phone number for the SIM directly from the carrier, telling you what number is on the device running your app right now. SMS OTPs can only tell you if the user has access to the phone number. |
| Use standalone or with an identity provider | You can use Firebase PNV on its own as an easy-to-integrate and reliable method of phone number verification, or you can use it as a sign-in method with Firebase Authentication or your own authentication system. |
| Automatically use available carriers | You can use the Firebase PNV SDK to detect compatibility and fall back to another method such as SMS when Firebase PNV is not yet supported on the device. Firebase PNV will gradually become available for carriers worldwide. As new carriers become available, you can automatically use them with no additional changes to your app. See [Carrier support](https://firebase.google.com/docs/phone-number-verification/pricing#supported-carriers) for a list of the participating carriers. |
| Eliminate SMS phishing attacks | Since Firebase PNV doesn't send any SMS messages to verify a phone number, users are not expecting messages from your app with one time passcodes, which can be used in account takeover attacks. |

## How does it work?

When you make a phone number verification request, Firebase PNV:

1. Checks that the user's device and mobile carrier are supported.

2. Gets consent from the user to share their phone number with your app.

3. Works with the mobile carrier assigned to the SIM to obtain the verified
   phone number.

4. Returns to your app a signed token containing the verified phone
   number, typically in 1-3 seconds from user consent.

After verifying the signature of this token, your app now has the user's
verified phone number. You can also use this token as part of a phone number
based sign-in flow, for example using Firebase Authentication or your own
authentication backend.

> [!WARNING]
> **Beta:** Firebase Authentication support is under development, and does not accept the Firebase PNV token as a sign-in token. To implement sign-in using Firebase PNV and Firebase Authentication, you can use custom authentication to exchange the Firebase PNV token for a Firebase Authentication token. For an example, see the [Authenticate with Firebase using Firebase Phone Number Verification](https://firebase.google.com/docs/phone-number-verification/android/sign-in) page.

## Implementation path

|---|---|---|
|   | Set up your Firebase project | In the [Firebase console](https://console.firebase.google.com/project/_/phoneverification/sites/?useAutoProject=true), complete onboarding steps to enable billing and the Firebase Phone Number Verification API for your Firebase project. |
|   | Install the SDK and initialize | Install the Firebase PNV SDK for your app's platform. The SDK requires that OAuth brand verification has been successfully completed. |
|   | Design an explainer screen | (Recommended) Before triggering the formal user consent UI, explain that they need to select a SIM to fetch the number for, and how this is faster and more secure than SMS OTPs. This will reduce confusion, and train users on the new phone number verification flow. |
|   | Check for device and carrier compatibility | (Recommended) When your app launches, use the Firebase PNV SDK to check that the device and its mobile carrier are compatible with Firebase PNV. If it is compatible, display the explainer screen, and prompt for consent. If it isn't, use your legacy method of phone number verification, such as SMS. |
|   | Request the verified phone number | Use the Firebase PNV SDK to request the device's verified phone number from the mobile carrier. This triggers user consent, which your explainer screen helps prepare the user to complete. |
|   | Verify the response token | In the response from the Firebase PNV service, you get a signed token, which you can send to your app's backend. On the backend, verify the signature of the token. If the signature is valid, then the token contains the device's verified phone number. |

## Next steps

- Firebase PNV is a billed service that incurs a cost per verification. See the [Pricing](https://firebase.google.com/docs/phone-number-verification/pricing) page for details.
- See the [Get started on Android](https://firebase.google.com/docs/phone-number-verification/android/get-started) guide to learn how to use Firebase PNV in an Android app.