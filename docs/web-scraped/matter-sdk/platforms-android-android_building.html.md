# Source: https://project-chip.github.io/connectedhomeip-doc/platforms/android/android_building.html

# Building Android

## Contents

# Building Android

There are following Apps on Android

* CHIPTool - Android CHIPTool is an application for Android for commissioning and controlling Matter accessory devices. It offers the following features:

  * Scan a Matter QR code and display payload information to the user

  * Read the NFC tag containing Matter onboarding information

  * Commission a Matter device

  * Send echo requests to the Matter echo server

  * Send on/off cluster requests to a Matter device

* CHIPTest

  * Android CHIPTest is an application for Android for running Matter’s unit tests

* * *

* Building Android

  * Source files

  * Requirements for building

    * Linux

    * MacOS

    * ABIs and TARGET_CPU

    * Gradle & JDK Version

    * Kotlin Version

  * Preparing for build

  * Building Android CHIPTool from scripts

  * Building Android CHIPTool from Android Studio

  * Building Android CHIPTest from scripts

* * *

## Source files

You can find source files of the Android applications in the `examples/android/` directory.

* * *

## Requirements for building

You need Android SDK 34 & NDK 28.2.13676358 downloaded to your machine. Set the `$ANDROID_HOME` environment variable to where the SDK is downloaded and the `$ANDROID_NDK_HOME` environment variable to point to where the NDK package is downloaded.

  1. Install [Android Studio](https://developer.android.com/studio)

  2. Install NDK:

     1. Tools -> SDK Manager -> SDK Tools Tab

     2. Click [x] Show Package Details

     3. Select NDK (Side by Side) -> 28.2.13676358

     4. Apply

  3. Install Command Line Tools:

     1. Tools -> SDK Manager -> SDK Tools Tab -> Android SDK Command Line Tools 10.0

     2. Apply

  4. Install SDK 34:

     1. Tools -> SDK Manager -> SDK Platforms Tab -> Android 14.0 (Upside Down Cake) API Level 34

     2. Apply

  5. Install Emulator:

     1. Tools -> Device Manager -> Create device -> Pixel 5 -> Android S API 34 -> Download

### Linux

    export ANDROID_HOME=~/Android/Sdk
    export ANDROID_NDK_HOME=~/Android/Sdk/ndk/28.2.13676358
    

### MacOS

    export ANDROID_HOME=~/Library/Android/sdk
    export ANDROID_NDK_HOME=~/Library/Android/sdk/ndk/28.2.13676358
    

### ABIs and TARGET_CPU

`TARGET_CPU` can have the following values, depending on your smartphone CPU architecture:

ABI | TARGET_CPU  
---|---  
armeabi-v7a | arm  
arm64-v8a | arm64  
x86 | x86  
x86_64 | x64  
  
### Gradle & JDK Version

All Android projects utilize Gradle plugin version 8.5.1, Gradle version 8.7 and JDK version 17.0.

For developer using java 17 in MacOS, the JAVA can be configured as follows via `sdkman`:

    sdk install java 17.0.14-tem
    

For developer using openjdk-17-jdk in Linux, the JAVA_HOME environment variable can be configured as follows:

    sudo apt-get install openjdk-17-jdk
    export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
    

### Kotlin Version

The build requires `kotlinc` to be in your `$PATH`.

For Linux:

    cd /usr/lib
    wget -q https://github.com/JetBrains/kotlin/releases/download/v2.1.10/kotlin-compiler-2.1.10.zip
    unzip kotlin-compiler-*.zip
    rm kotlin-compiler-*.zip
    rm -f kotlinc/bin/*.bat
    export PATH=$PATH:/usr/lib/kotlinc/bin
    

For MacOS:

    sdk install kotlin 2.1.10
    

* * *

## Preparing for build

Complete the following steps to prepare the Matter build:

  1. Check out the Matter repository.

  2. Run bootstrap (**only required first time**)

         source scripts/bootstrap.sh
         

  3. Choose how you want to build the Android CHIPTool. There are **two** ways: from script, or from source within Android Studio.

## Building Android CHIPTool from scripts

This is the simplest option. In the command line, run the following command from the top CHIP directory:

    ./scripts/build/build_examples.py --target android-arm64-chip-tool build
    

See the table above for other values of `TARGET_CPU`.

The debug Android package `app-debug.apk` will be generated at `out/android-$TARGET_CPU-chip-tool/outputs/apk/debug/`, and can be installed with

    adb install out/android-$TARGET_CPU-chip-tool/outputs/apk/debug/app-debug.apk
    

You can use Android Studio to edit the Android CHIPTool app itself and run it after build_examples.py, but you will not be able to edit Matter Android code from `src/controller/java`, or other Matter C++ code within Android Studio.

## Building Android CHIPTool from Android Studio

This option allows Android Studio to build the core Matter code from source, which allows us to directly edit core Matter code in-IDE.

  1. In the command line, run the following command from the top Matter directory:

         TARGET_CPU=arm64 ./scripts/examples/android_app_ide.sh
         

See the table above for other values of `TARGET_CPU`.

  1. Modify the `matterSdkSourceBuild` variable to true, `matterBuildSrcDir` point to the appropriate output directory (e.g. `../../../../out/android_arm64`), and `matterSourceBuildAbiFilters` to the desired ABIs in [examples/android/CHIPTool/gradle.properties](https://github.com/project-chip/connectedhomeip/blob/master/examples/android/CHIPTool/gradle.properties)

  2. Open the project in Android Studio and run **File - > Sync Project with Gradle Files**.

  3. Use one of the following options to build an Android package:

     * Click **Make Project** in Android Studio.

     * Run the following command in the command line:

           cd examples/android/CHIPTool
           ./gradlew build
           

The debug Android package `app-debug.apk` will be generated at `examples/android/CHIPTool/app/build/outputs/apk/debug/`, and can be installed with

    adb install examples/android/CHIPTool/app/build/outputs/apk/debug/app-debug.apk
    

or

    (cd examples/android/CHIPTool && ./gradlew installDebug)
    

## Building Android CHIPTest from scripts

Currently, the CHIPTest can only be built from scripts. The steps are similar to building CHIPTool from scripts.

    ./scripts/build/build_examples.py --target android-arm64-chip-test build
    

You can modify the `matterUTestLib` variable to the test lib in [examples/android/CHIPTest/gradle.properties](https://github.com/project-chip/connectedhomeip/blob/master/examples/android/CHIPTest/gradle.properties) to change target to test.
