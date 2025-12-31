# Source: https://firebase.google.com/docs/test-lab/game-loop.md.txt

# Source: https://firebase.google.com/docs/test-lab/android/game-loop.md.txt

<br />

It can be hard to automate game testing when gaming apps are built on different UI frameworks. Game Loop tests allow you to integrate your native tests withTest Laband easily run them on devices you select. A Game Loop test runs your test through your gaming app while simulating the actions of a real player. This guide shows you how to run a Game Loop test, then view and manage your test results in theFirebaseconsole.

Depending on your game engine, you can implement tests with single or multiple loops. A loop is a full or partial run-through of your test on your gaming app. Game loops can be used to:

- Run a level of your game the same way an end user would play it. You can either script the input of the user, let the user be idle, or replace the user with an AI if it makes sense in your game (e.g., say you have a race car gaming app and already have an AI implemented. You can easily put an AI driver in charge of the user's input).
- Run your game at the highest quality setting to see if devices support it.
- Run a technical test (compile multiple shaders, execute them, check that the output is as expected, etc).

You can run a Game Loop test on a single test device, a set of test devices, or onTest Lab. However, we don't recommend running Game Loop tests on virtual devices because they have lower graphics frame rates than physical devices.
| **Note:** Test Laboffers additional features to help you customize your Game Loop tests, such as the ability to run multiple loops at once, or to organize your loops with labels. For more information on these features, see[Optional features](https://firebase.google.com/docs/test-lab/android/game-loop#optional-features).

## Before you begin

To implement a test, you must first configure your app for Game Loop tests.

1. In your app manifest, add a new intent filter to your[activity](https://developer.android.com/reference/android/app/Activity):

   ```scdoc
   <activity android:name=".MyActivity">
      <intent-filter>
          <action android:name="com.google.intent.action.TEST_LOOP"/>
          <category android:name="android.intent.category.DEFAULT"/>
          <data android:mimeType="application/javascript"/>
      </intent-filter>
      <intent-filter>
         ... (other intent filters here)
      </intent-filter>
   </activity>
   ```

   This allowsTest Labto launch your game by triggering it with a specific intent.
   | **Note:** Game loops require a separate, dedicated intent filter that is not used for other purposes. Your activity can include other intent filters. To learn more about intent filters, see the[\<intent-filter\> reference page.](https://developer.android.com/guide/topics/manifest/intent-filter-element.html)
2. In your code (we recommend inside the`onCreate`method declaration), add the following:

   ### Kotlin

   ```kotlin
   val launchIntent = intent
   if (launchIntent.action == "com.google.intent.action.TEST_LOOP") {
       val scenario = launchIntent.getIntExtra("scenario", 0)
       // Code to handle your game loop here
   }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/test-lab/app/src/main/java/com/google/firebase/example/testlab/kotlin/MainActivity.kt#L27-L31
   ```

   ### Java

   ```java
   Intent launchIntent = getIntent();
   if(launchIntent.getAction().equals("com.google.intent.action.TEST_LOOP")) {
       int scenario = launchIntent.getIntExtra("scenario", 0);
       // Code to handle your game loop here
   }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/test-lab/app/src/main/java/com/google/firebase/example/testlab/MainActivity.java#L36-L40
   ```

   This allows your activity to check the intent that launches it. You can also add this code later if you prefer (e.g., after initially loading your game engine).
3. Recommended: At the end of the test, add:

   ### Kotlin

   ```kotlin
   yourActivity.finish()https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/test-lab/app/src/main/java/com/google/firebase/example/testlab/kotlin/MainActivity.kt#L38-L38
   ```

   ### Java

   ```java
   yourActivity.finish();https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/test-lab/app/src/main/java/com/google/firebase/example/testlab/MainActivity.java#L47-L47
   ```

   This closes your app when the Game Loop test is complete. The test relies on your app's UI framework to start the next loop, and closing your app tells it that the test is finished.

## Create and run a Game Loop test

After you configure your app for Game Loop tests, you can immediately create a test and run it in your gaming app. You can choose to run a test inTest Labusing either the[Firebaseconsole](https://firebase.google.com/docs/test-lab/android/game-loop#run-console)or the[gcloud command line interface (CLI)](https://firebase.google.com/docs/test-lab/android/game-loop#run-gcloud), or on a[local device using the Test Loop Manager](https://firebase.google.com/docs/test-lab/android/game-loop#run-local).

### Run on a local device

Test Lab's**Test Loop Manager**is an open source app that helps you integrate Game Loop tests and run them on your local devices. It also allows your Quality Assurance team to run the same game loops on their devices.

To run a test on a local device using the Test Loop Manager:

1. Download the[Test Loop Manager](https://dl.google.com/firebase/testlab/testloopmanager.apk)on a phone or tablet and install it by running:  

   ```
   adb install testloopmanager.apk
   ```
2. On your device, open the**Test Loop Apps** app on your phone or tablet. The app displays a list of apps on your device that can be run with game loops. If you don't see your gaming app here, make sure your intent filter matches the one described in the first step of the[Before you begin section](https://firebase.google.com/docs/test-lab/android/game-loop#begin-anchor).
3. Select your gaming app, then select the number of loops you want to run. Note: At this step, you can choose to run a subset of loops instead of just one loop. For more information on running multiple loops at once, see[Optional features](https://firebase.google.com/docs/test-lab/android/game-loop#optional-features).
4. Click**Run test**. Your test starts running immediately.

| **Note:** Game Loop tests have a default timeout of three minutes. When the timeout ends, the test terminates and cancels all pending loops. To set a different timeout duration in the**Test Loop Manager** app, click**menu** \>**Set timeout**, then change the timeout in the dialogue that appears.

## Run inTest Lab

You can run a Game Loop test inTest Labusing either the[Firebaseconsole](https://firebase.google.com/docs/test-lab/android/game-loop#run-console)or the[gcloud CLI.](https://firebase.google.com/docs/test-lab/android/game-loop#run-gcloud)Before you begin, if you haven't already, open the[Firebaseconsole](https://console.firebase.google.com/)and create a project.
| **Note:** You can useTest Labat no charge with the Spark pricing plan, which comes with a limited daily quota. For more information about other pricing plans and usage limits, see[Firebase Pricing Plans](https://firebase.google.com/pricing).

### Use theFirebaseconsole

1. In theFirebaseconsole, click**Test Lab**from the left panel.
2. Click**Run Your First Test** (or**Run a Test**if your project has previously run a test).
3. Select**Game Loop** as the test type, and then click**Continue**.
4. Click**Browse** , and then browse to your app's`.apk`file. Note: At this step, you can choose to run a subset of loops instead of just one loop. For more information on running multiple loops at once, see[Optional features](https://firebase.google.com/docs/test-lab/android/game-loop#optional-features).
5. Click**Continue**.
6. Select the physical devices to use to test your app.
7. Click**Start Tests**.

For more information on getting started with theFirebaseconsole, see[Start testing with theFirebaseconsole.](https://firebase.google.com/docs/test-lab/android/firebase-console)

### Use the gcloud command-line (CLI)

1. If you haven't already, download and install the[Google Cloud SDK](https://cloud.google.com/sdk/docs/install-sdk#installing_the_latest_version)

2. Sign in to the gcloud CLI using your Google Account:

   `gcloud auth login`
3. Set your Firebase project in gcloud, where`PROJECT_ID`is the ID of your Firebase project:

   ```
   gcloud config set project PROJECT_ID
   ```
4. Run your first test:

   ```
   gcloud firebase test android run \
    --type=game-loop --app=<var>path-to-apk</var> \
    --device model=herolte,version=23
   ```
   | **Note:** At this step, you can choose to run a subset of loops instead of just one loop. For more information on running multiple loops at once, see[Optional features](https://firebase.google.com/docs/test-lab/android/game-loop#optional-features).

For more information on getting started with the gcloud CLI, see[Start testing from the gcloud command line.](https://firebase.google.com/docs/test-lab/android/command-line)

## Optional features

Test Laboffers several optional features that let you further customize your tests, including the ability to write output data, support for multiple game loops, and labels for related loops.

### Write output data

Your Game Loop test can write output to a file specified in the`launchIntent.getData()`method. After you run a test, you can access this output data in the**Test Lab** section of theFirebaseconsole (see[Game Loop test output file example](https://firebase.google.com/docs/test-lab/android/game-loop#output-example)).

Test Labfollows best practices for sharing a file between apps described in[Sharing a File](https://developer.android.com/training/secure-file-sharing/share-file.html). In your activity's`onCreate()`method, where your intent is located, you can check your data output file by running following code:  

### Kotlin

```kotlin
val launchIntent = intent
val logFile = launchIntent.data
logFile?.let {
    Log.i(TAG, "Log file ${it.encodedPath}")
    // ...
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/test-lab/app/src/main/java/com/google/firebase/example/testlab/kotlin/MainActivity.kt#L44-L49
```

### Java

```java
Intent launchIntent = getIntent();
Uri logFile = launchIntent.getData();
if (logFile != null) {
    Log.i(TAG, "Log file " + logFile.getEncodedPath());
    // ...
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/test-lab/app/src/main/java/com/google/firebase/example/testlab/MainActivity.java#L53-L58
```

If you want to write to the file from the C++ side of your game app, you can pass in the file descriptor instead of the file path:  

### Kotlin

```kotlin
val launchIntent = intent
val logFile = launchIntent.data
var fd = -1
logFile?.let {
    Log.i(TAG, "Log file ${it.encodedPath}")
    fd = try {
        contentResolver
            .openAssetFileDescriptor(logFile, "w")!!
            .parcelFileDescriptor
            .fd
    } catch (e: FileNotFoundException) {
        e.printStackTrace()
        -1
    } catch (e: NullPointerException) {
        e.printStackTrace()
        -1
    }
}

// C++ code invoked here.
// native_function(fd);  
https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/test-lab/app/src/main/java/com/google/firebase/example/testlab/kotlin/MainActivity.kt#L56-L76
```

### Java

```java
Intent launchIntent = getIntent();
Uri logFile = launchIntent.getData();
int fd = -1;
if (logFile != null) {
    Log.i(TAG, "Log file " + logFile.getEncodedPath());
    try {
        fd = getContentResolver()
                .openAssetFileDescriptor(logFile, "w")
                .getParcelFileDescriptor()
                .getFd();
    } catch (FileNotFoundException e) {
        e.printStackTrace();
        fd = -1;
    } catch (NullPointerException e) {
        e.printStackTrace();
        fd = -1;
    }
}

// C++ code invoked here.
// native_function(fd);  
https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/test-lab/app/src/main/java/com/google/firebase/example/testlab/MainActivity.java#L64-L84
```

### C++

```c++
#include <unistd.h>
JNIEXPORT void JNICALL
Java_my_package_name_MyActivity_native_function(JNIEnv *env, jclass type, jint log_file_descriptor) {
// The file descriptor needs to be duplicated.
int my_file_descriptor = dup(log_file_descriptor);
}
```

### Output file example

You can use output data files (formatted like the example below) to display game loop test results in the**Test Lab** section of theFirebaseconsole. Areas shown as`/.../`can contain any custom fields that you need, as long as they don't conflict with the names of other fields used in this file:  

```
{
  "name": "test name",
  "start_timestamp": 0, // Timestamp of the test start (in us).
                           Can be absolute or relative
  "driver_info": "...",
  "frame_stats": [
    {
      "timestamp": 1200000, // Timestamp at which this section was written
                               It contains value regarding the period
                               start_timestamp(0) -> this timestamp (1200000 us)
      "avg_frame_time": 15320, // Average time to render a frame in ns
      "nb_swap": 52, // Number of frame rendered
      "threads": [
        {
          "name": "physics",
          "Avg_time": 8030 // Average time spent in this thread per frame in us
        },
        {
          "name": "AI",
          "Avg_time": 2030 // Average time spent in this thread per frame in us
        }
      ],
      /.../ // Any custom field you want (vertices display on the screen, nb units â¦)
    },
    {
      // Next frame data here, same format as above
    }
  ],
  "loading_stats": [
    {
      "name": "assets_level_1",
      "total_time": 7850, // in us
      /.../
    },
    {
      "name": "victory_screen",
      "total_time": 554, // in us
      /.../
    }

  ],
  /.../, // You can add custom fields here
}

```

### Multiple game loops

You might find it useful to run multiple game loops in your app. A loop is a complete run-through of your game app from beginning to end. For example, if you have multiple levels in your game, you might want to have one game loop to launch each level instead of having one loop that iterates through all of them. That way, if your app crashes on level 32, you can directly launch that game loop to reproduce the crash and test bug fixes.

To enable your app to run multiple loops at once:

- If you're running a test with the Test Loop Manager:

  1. Add the following line to your app's manifest, inside the`<application>`element:

     ```text
     <meta-data
       android:name="com.google.test.loops"
       android:value="5" />
     ```

     <br />

     This launch intent contains the target loop as an integer parameter. In the`android:value`field, you can specify an integer from 1 to 1024 (the maximum number of loops allowed for a single test). Note that loops are indexed starting from 1, not 0.
  2. In the Test Loop Manager app, a selection screen appears that allows you to select which loop(s) you want to run. If you select multiple loops, each loop is launched in sequence after the preceding loop completes.

- If you're running a test with theFirebaseconsole, enter a list or a range of loop numbers in the**Scenarios**field.

- If you're running a test with the gcloud CLI, specify a list of loop numbers by using the`--scenario-numbers`flag. For example,`--scenario-numbers=1,3,5`runs loops 1, 3, and 5.

- If you're writing C++ and want to change the behavior of your loop, pass the following extra to your native C++ code:

  ### Kotlin

  ```kotlin
  val launchIntent = intent
  val scenario = launchIntent.getIntExtra("scenario", 0)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/test-lab/app/src/main/java/com/google/firebase/example/testlab/kotlin/MainActivity.kt#L82-L83
  ```

  ### Java

  ```java
  Intent launchIntent = getIntent();
  int scenario = launchIntent.getIntExtra("scenario", 0);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/test-lab/app/src/main/java/com/google/firebase/example/testlab/MainActivity.java#L90-L91
  ```

  You can now change the behavior of your loop based on the resulting`int`value.

### Label game loops

When you label your game loops with one or more scenario labels, you and your QA team can easily launch a set of related game loops (e.g., "all compatibility game loops") and test them in a single matrix. You can create your own labels or use the predefined labels offered byTest Lab:

- `com.google.test.loops.player_experience`: For loops used to reproduce a real user's experience when playing the game. The goal of testing with these loops is to find issues that a real user would face while playing the game.
- `com.google.test.loops.gpu_compatibility`: For loops used to test GPU-related issues. The goal of testing with these loops is to execute GPU code that might not run properly run in production, to expose issues with hardware and drivers.
- `com.google.test.loops.compatibility`: For loops used to test a broad range of compatibility issues, including I/O issues and OpenSSL issues.
- `com.google.test.loops.performance`: For loops used to test the performance of the device. For example, a game might run at the most complex graphics settings to see how a new device behaves.

To enable your app to run loops with the same label:

- If you're running a test with the Test Loop Manager:

  1. In your app's manifest, add the following meta-data line and replace<var translate="no">LABEL_NAME</var>with a label of your choice:

     ```scdoc
     <meta-data
      android:name="com.google.test.loops.LABEL_NAME"
      android:value="1,3-5" />
     ```

     In the`android:value`field, you can specify a range or a set of integers from 1 to 1024 (the maximum number of loops allowed for a single test) that represent the loops you want to label. Note that loops are indexed starting from 1, not 0. For example,`android:value="1,3-5"`applies<var translate="no">LABEL_NAME</var>to loops 1, 3, 4, and 5.
  2. In the Test Loop Manager app, enter one or more labels in the**Labels**field.

- If you're running a test with theFirebaseconsole, enter one or more labels in the**Labels**field.

- If you're running a test with the gcloud CLI, specify one or more scenario labels by using the`--scenario-labels`flag (e.g.,`--scenario-labels=performance,gpu`).

## App licensing support

Test Labsupports apps that use the[App Licensing](https://developer.android.com/google/play/licensing/index.html)service offered by Google Play. To successfully check licensing when testing your app withTest Lab, you must publish your app to the production channel in the Play store. To test your app in the alpha or beta channel usingTest Lab, remove the licensing check before uploading your app toTest Lab.

## Known issues

Game Loop tests inTest Labhave the following known issues:

- Some crashes do not support backtraces. For example, some release builds may suppress the output of the`debuggerd`process using`prctl(PR_SET_DUMPABLE, 0)`. To learn more, see[`debuggerd`](https://source.android.com/devices/tech/debug/#debuggerd).
- API Level 19 is not currently supported due to file permission errors.