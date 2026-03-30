# Source: https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3.md.txt

# Tutorial: Measure iOS Ads conversions

## Step 3: Initiate on-device conversion measurement using Google Analytics

<br />

|---|
| Introduction: [Measure iOS Ads conversions](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/index-first-party) |
| Step 1: [Implement a sign-in experience](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-1) <br /> |
| [Step 2: Integrate Google Analytics](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-2) |
| **Step 3: Initiate on-device conversion measurement using Google Analytics** <br /> |
| Step 4: [Troubleshoot and handle common issues](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-4) |

<br />

Now that you can collect users' email addresses and phone numbers and your app has the
Google Analytics for Firebase SDK, you can use the two to start
measuring conversions.

### Call the API

Call the conversion measurement API with the consented email address or phone
number from Step 1, which is used for ads conversion measurement, without
allowing any personally identifiable information to leave the user device.

There are two ways to initiate measurement:

- [Using credentials](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3#use-plain-text-credentials)
- [Using hashed credentials](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3#use-hashed-credentials)

#### Use email address or phone number

### Swift

Import the `FirebaseAnalytics` module and pass in the email address or phone
number to the `initiateOnDeviceConversionMeasurement()` API.

> [!NOTE]
> **Note:** The `initiateOnDeviceConversionMeasurement(emailAddress:)` and `initiateOnDeviceConversionMeasurement(phoneNumber:)` methods may be called sequentially, but only one match can be reported per user. If a match is found with either API, then subsequent API call are effectively ignored.

```swift
import FirebaseAnalytics

// ...
// If you're using an email address....
Analytics.initiateOnDeviceConversionMeasurement(emailAddress: "example@gmail.com")
// If you're using a phone number....
Analytics.initiateOnDeviceConversionMeasurement(phoneNumber: "+15555555555")
```

### Objective-C

Import the `FirebaseAnalytics` module and pass in the email address to the
`initiateOnDeviceConversionMeasurementWithEmailAddress:` API or the phone
number to the `initiateOnDeviceConversionMeasurementWithPhoneNumber:` API.

> [!NOTE]
> **Note:** The `initiateOnDeviceConversionMeasurementWithEmailAddress:` and `initiateOnDeviceConversionMeasurementWithPhoneNumber:` methods may be called sequentially, but only one match can be reported per user. If a match is found with either API, then subsequent API call are effectively ignored.

```objective-c
@import FirebaseAnalytics;

// ...
// If you're using an email address....
[FIRAnalytics initiateOnDeviceConversionMeasurementWithEmailAddress:@"example@gmail.com"];
// If you're using a phone number....
[FIRAnalytics initiateOnDeviceConversionMeasurementWithPhoneNumber:@"+15555555555"];
```

### Unity

Import the `Firebase.Analytics` namespace and pass in the email address to the
`InitiateOnDeviceConversionMeasurementWithEmailAddress()` API or the phone
number to the `InitiateOnDeviceConversionMeasurementWithPhoneNumber()` API:

> [!NOTE]
> **Note:** The `InitiateOnDeviceConversionMeasurementWithEmailAddress()` and `InitiateOnDeviceConversionMeasurementWithPhoneNumber()` methods may be called sequentially, but only one match can be reported per user. If a match is found with either API, then subsequent API call are effectively ignored.

```c#
using Firebase.Analytics;

// ...
// If you're using an email address....
FirebaseAnalytics.InitiateOnDeviceConversionMeasurementWithEmailAddress("example@gmail.com");
// If you're using a phone number....
FirebaseAnalytics.InitiateOnDeviceConversionMeasurementWithPhoneNumber("+15555555555");
```

> [!NOTE]
> **Note:** The best practice is to call the API once per install and as close as possible to the login. Starting in Google Analytics for Firebase SDK 12.1.0, to ensure that on-device conversion measurement for re-engagement campaigns is initiated for existing users, call the API once per app instance.

> [!IMPORTANT]
> **Important:** Be aware that if an intended in-app action or event happens *immediately* after a user email or phone registration, consider implementing a small time delay between initiating on-device conversion measurement and logging the event.

#### Use a hashed email address or phone number

The API will accept email addresses and phone numbers hashed with SHA256. You
can maintain control of your user's data by performing the hashing in your code
before making calls to the SDK.

To use hashed credentials, normalize addresses and numbers, hash them with
SHA256, then call the API.

##### Normalize email addresses and phone numbers

For **email addresses** , the Google Analytics API assumes that a
particular normalization is performed before SHA256 is applied, so follow these
steps to normalize your data:

1. Convert the entire email address to lowercase.

2. If the email address ends in domain *@googlemail.com* , replace the
   *@googlemail.com* domain with *@gmail.com*.

3. For addresses ending in domain *@gmail.com* (including those modified in
   the previous step):

   1. Remove all periods from the username portion.

   2. Make the following substitutions in the username portion:

      - For letters I or i, or digit 1, substitute letter l
      - For digit 0, substitute letter o
      - For digit 2, substitute letter z
      - For digit 5, substitute letter s

For example, after normalization:

- `an.email.user0125@googlemail.com` becomes `anemalluserolzs@gmail.com`
- `CAPSUSER0125@provider.net` becomes `capsuser0125@provider.net`

For **phone numbers**, numbers must already be in E.164 format (that is,
prefix with +, 1-3 digits for country code, max 12 digits for subscriber number)
prior to hashing with SHA256.

Note that the hashed SHA256 email or phone numbers must be 32 bytes long
and not a hexadecimal string.

##### Call the API with hashed credentials

### Swift

Import the `FirebaseAnalytics` module and pass in the email address or phone
number to the `initiateOnDeviceConversionMeasurement()` API.

> [!NOTE]
> **Note:** The `initiateOnDeviceConversionMeasurement(hashedEmailAddress:)` and `initiateOnDeviceConversionMeasurement(hashedPhoneNumber:)` methods may be called sequentially, but only one match can be reported per user. If a match is found with either API, then subsequent API call are effectively ignored.

```swift
import FirebaseAnalytics

// ...
// If you're using an email address....
Analytics.initiateOnDeviceConversionMeasurement(hashedEmailAddress: hashedEmailAddress)
// If you're using a phone number....
Analytics.initiateOnDeviceConversionMeasurement(hashedPhoneNumber: hashedPhoneNumber)
```

### Objective-C

Import the `FirebaseAnalytics` module and pass in the email address to the
`initiateOnDeviceConversionMeasurementWithHashedEmailAddress:` API or the phone
number to the `initiateOnDeviceConversionMeasurementWithHashedPhoneNumber:`
API.

> [!NOTE]
> **Note:** The `initiateOnDeviceConversionMeasurementWithHashedEmailAddress:` and `initiateOnDeviceConversionMeasurementWithHashedPhoneNumber:` methods may be called sequentially, but only one match can be reported per user. If a match is found with either API, then subsequent API call are effectively ignored.

```objective-c
@import FirebaseAnalytics;

// ...
// If you're using an email address....
[FIRAnalytics initiateOnDeviceConversionMeasurementWithHashedEmailAddress:hashedEmailAddress];
// If you're using a phone number....
[FIRAnalytics initiateOnDeviceConversionMeasurementWithHashedPhoneNumber:hashedPhoneNumber];
```

### Unity

Import the `Firebase.Analytics` namespace and pass in the email address to the
`InitiateOnDeviceConversionMeasurementWithHashedEmailAddress()` API or the
phone number to the `InitiateOnDeviceConversionMeasurementWithHashedPhoneNumber()` API:

> [!NOTE]
> **Note:** The `InitiateOnDeviceConversionMeasurementWithHashedEmailAddress()` and `InitiateOnDeviceConversionMeasurementWithHashedPhoneNumber()` methods may be called sequentially, but only one match can be reported per user. If a match is found with either API, then subsequent API call are effectively ignored.

```c#
using Firebase.Analytics;

// ...
// If you're using an email address....
FirebaseAnalytics.InitiateOnDeviceConversionMeasurementWithHashedEmailAddress(hashedEmailAddress);
// If you're using a phone number....
FirebaseAnalytics.InitiateOnDeviceConversionMeasurementWithHashedPhoneNumber(hashedPhoneNumber);
```

> [!NOTE]
> **Note:** The best practice is to call the API once per install and as close as possible to the login. Starting in Google Analytics for Firebase SDK 12.1.0, to ensure that on-device conversion measurement for re-engagement campaigns is initiated for existing users, call the API once per app instance.

> [!IMPORTANT]
> **Important:** Be aware that if an intended in-app action or event happens *immediately* after a user email or phone registration, consider implementing a small time delay between initiating on-device conversion measurement and logging the event.

### Verify integration

Enable debug mode. After calling the initiate measurement API, ensure
that a message like the following log message appears in the Xcode debug
console:

    [FirebaseAnalytics][I-ACS023225] Initiated on-device conversion measurement

If you enabled debug mode and included the `-DebugOnDeviceConversionMeasurement`
launch argument, then calling the `initiateOnDeviceConversionMeasurement()` API
will simulate a match.

    [FirebaseAnalytics][I-ACS023229] On-device conversion measurement found a match

<br />

*** ** * ** ***

<br />

[**Step 2** : Integrate Google Analytics](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-2)
[**Step 4** : Troubleshoot and handle common issues](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-4)

<br />

*** ** * ** ***