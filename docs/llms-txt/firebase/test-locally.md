# Source: https://firebase.google.com/docs/test-lab/ios/test-locally.md.txt

<br />

This guide describes how to run an iOS test locally so you can quality check the test's behavior before running it inFirebase Test Lab.

## Run an XCTest locally

You can verify thatTest Labwill be able to install your app and tests by running locally with a USB-connected device as follows:  

```
xcodebuild test-without-building \
    -xctestrun "Derived Data/Build/Products/YourApp.xctestrun" \
    -destination id=your-phone-id
```

## Run a Game Loop test locally