# Source: https://firebase.google.com/docs/cloud-messaging/send/firebase-console.md.txt

# Source: https://firebase.google.com/docs/test-lab/android/firebase-console.md.txt

# Source: https://firebase.google.com/docs/test-lab/ios/firebase-console.md.txt

<br />

This guide describes how to run iOS tests using theFirebaseconsole.

## Step 1. Create a Firebase project

If you haven't yet, go to the[Firebaseconsole](https://console.firebase.google.com/)and create a new Firebase project.
| **Note:** If you're working on a shared Firebase project, you'll need to have ownership or edit permissions for the project.

## Step 2. Upload and run your test

### XCTest

1. OpenTest Labin the[Firebaseconsole](https://console.firebase.google.com/project/_/testlab).

2. If it's your first test, click**Get Started** under iOS. If you previously ran a test, click**Run a Test** , and then select**Run an XCTest**.

3. Click**Browse** , and find the`.zip`file you created.

4. Check the box for each device, version, orientation, and locale you'd like to test against.

5. (Optional) To help you identify and locate your test matrices in theFirebaseconsole, you can add a label to your test matrix by entering a label name in the**Test matrix label (optional)**field.

6. Click**Start Tests**.

### Game Loop test

1. On theTest Labpage of the[Firebaseconsole](https://console.firebase.google.com/project/_/testlab), click**Run Your First Test \> Run an iOS Game Loop**.

2. In the**Upload App** section, click**Browse** , then select your app's IPA file (if you haven't already,[generate an IPA file](https://firebase.google.com/docs/test-lab/ios/run-game-loop-test#package-app)for your app).

3. (Optional) To help you identify and locate your test matrices in theFirebaseconsole, you can add a label to your test matrix by entering a label name in the**Test matrix label (optional)**field.

4. (Optional) If you want to run multiple loops (aka scenarios) at a time or select specific loops to run, enter the loop numbers in the**Scenarios**field.

   For example, when you enter "1-3, 5",Test Labruns loops 1, 2, 3, and 5. By default (if you don't enter anything in the**Scenarios** field),Test Labonly runs loop 1.
5. In the**Devices** section, select one or more physical devices you want to test your app on, then click**Start Tests**.

## Step 3. Investigate your test results

When the test starts, you're automatically redirected to the test results page. Tests can take a few minutes to run, depending on the number of different configurations you have selected and the test timeout duration set for your tests. After your tests have run, you can review test results. See[AnalyzingFirebase Test LabResults](https://firebase.google.com/docs/test-lab/ios/analyzing-results)to learn more about how to interpret the test results.