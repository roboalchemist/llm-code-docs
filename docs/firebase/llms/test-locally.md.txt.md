# Source: https://firebase.google.com/docs/test-lab/ios/test-locally.md.txt

# Run a test locally

This guide describes how to run an iOS test locally so you can quality check
the test's behavior before running it in Firebase Test Lab.

## Run an XCTest locally

You can verify that Test Lab will be able to install your app and tests by
running locally with a USB-connected device as follows:

```
xcodebuild test-without-building \
    -xctestrun "Derived Data/Build/Products/YourApp.xctestrun" \
    -destination id=your-phone-id
```

## Run a Game Loop test locally