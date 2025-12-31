# Source: https://firebase.google.com/docs/test-lab/ios/run-xctest.md.txt

<br />

This guide describes how to prepare an XCTest for testing inFirebase Test Lab.

## **Step 1**: Configure your project's Derived Data location

Xcode places compiled iOS artifacts, including any tests you build, in a Derived Data directory. It is possible to keep the default location for that directory, if you'd like, but it's often helpful to choose a more easily-accessible place for the files, especially if you're going to be running tests withTest Laboften:

1. Open your project in Xcode.
2. In the macOS menu bar, select**File** \>**Project Settings...**
3. Change the**Derived Data** drop-down from**Default Location** to**Custom Location**.
4. In the field below the drop-down, select a location for Xcode to output your tests to. (This is your<var class="edit" scope="FOLDER_WITH_TEST_OUTPUT" translate="no">FOLDER_WITH_TEST_OUTPUT</var>)

## **Step 2**: Build a generic test file

Test Labruns unit tests and UI tests using the[XCTest](https://developer.apple.com/documentation/xctest)framework. To run your app's XCTests onTest Labdevices, build it for testing on a Generic iOS Device:

1. From the device drop-down at the top of your Xcode workspace window, select**Generic iOS Device**.
2. In the macOS menu bar, select**Product** \>**Build For** \>**Testing**.

As an alternative, you can build your XCTest from the command line. Use the following command in a terminal:  

#### project

```
xcodebuild -project PATH/TO/YOUR_WORKSPACE/YOUR_PROJECT.xcodeproj \
   -scheme YOUR_SCHEME \
   -derivedDataPath FOLDER_WITH_TEST_OUTPUT \
   -sdk iphoneos build-for-testing
```

#### workspace

```
xcodebuild -workspace PATH/TO/YOUR_WORKSPACE.xcworkspace \
   -scheme YOUR_SCHEME \
   -derivedDataPath FOLDER_WITH_TEST_OUTPUT \
   -sdk iphoneos build-for-testing
```

## **Step 3**: Sign your test and verify

1. Make sure all artifacts in the app and test are signed. For example, you can do this through Xcode by specifying signing settings like provisioning profile and identity. For more information, see[Apple Code Signing](https://developer.apple.com/support/code-signing/).

   | **Note** :Test Labre-signs your app with its own provisioning profile and certificate.
2. Verify app signature by running`codesign --verify --deep --verbose /path/to/MyApp.app`where "MyApp" is the name of the app inside the unzipped folder. This varies for each project. Expected output is`MyApp.app: valid on disk`.

3. If you are running an XCUITest, then you need to verify the test and runner by running`codesign --verify --deep --verbose /path/to/MyTest-Runner.app`where "MyTest" is the name of the runner inside the unzipped folder. This varies for each project. Expected output is`MyTest-Runner.app: valid on disk`.

## **Step 4**: Package your app and test for uploading

1. After your test successfully builds, zip it for upload toTest Lab:

   ```
   cd FOLDER_WITH_TEST_OUTPUT/Build/Products : \
   zip -r MyTests.zip Debug-iphoneos YOUR_SCHEME_iphoneosDEPLOYMENT_TARGET-arm64.xctestrun
   ```

You can also package up your test by compressing the test files manually:

1. Open Finder and navigate to<var class="edit" scope="FOLDER_WITH_TEST_OUTPUT" translate="no">FOLDER_WITH_TEST_OUTPUT</var>.

2. Open the folder that has your project name as a prefix, then navigate to`Build/Products`folder inside.

3. Select the folders`Debug-iphoneos`and<var class="edit" scope="YOUR_SCHEME" translate="no">YOUR_SCHEME</var>`_iphoneos`<var class="edit" scope="DEPLOYMENT_TARGET" translate="no">DEPLOYMENT_TARGET</var>`-arm64.xctestrun`and then compress them.

## **Step 5**: (Optional) Run your test locally

Before running your test withTest Lab, you can run it locally with a USB-connected device to quality check its behavior:  

```
xcodebuild test-without-building \
    -xctestrun "Derived Data/Build/Products/YOUR_SCHEME.xctestrun" \
    -destination id=your-phone-id
```

## Next steps

Upload and run your test in the[Firebaseconsole](https://firebase.google.com/docs/test-lab/ios/firebase-console)or the[gcloud CLI](https://firebase.google.com/docs/test-lab/ios/command-line).