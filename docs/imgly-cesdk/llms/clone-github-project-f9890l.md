# Source: https://img.ly/docs/cesdk/android/get-started/clone-github-project-f9890l/

---
title: "Clone GitHub Project"
description: "Using CE.SDK with a cloned Android GitHub project"
platform: android
url: "https://img.ly/docs/cesdk/android/get-started/clone-github-project-f9890l/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Get Started](https://img.ly/docs/cesdk/android/get-started/overview-e18f40/) > [Quickstart Jetpack Compose](https://img.ly/docs/cesdk/android/get-started/new-jetpack-compose-project-c6567i/)

---

This guide will walk you through cloning an existing sample project with the CE.SDK editor already set up

## Pre-requisites

- Android Studio installed on your machine
- A valid **CE.SDK license key** ([Get a free trial](https://img.ly/forms/free-trial)), use `null` or an empty string to run in evaluation mode with watermark.

## Clone the GitHub Repository

Launch Android Studio and select `File -> New -> Project from version control`
Next, add the following URL:

```
https://github.com/imgly/cesdk-android-examples.git
```

![Android Studio Clone dialog](assets/CloneDialog.png)
Click "Clone" and wait for the project to be downloaded and set up.

## Run the Project

In the `local.properties` file, add your CE.SDK license key (or leave it empty to run in evaluation mode with watermark)

```
license=MY_LICENSE_GOES_HERE
```

You may have to create this file, if Android Studio did not generate it for you.

Finally, run the app on your device or android emulator.

## Common Errors

Here are some common errors you may encounter through this guide, and how to solve them.

#### Invalid License

| ![Invalid license dialog](assets/InvalidLicense.png) | ![Missing license dialog](assets/MissingLicense.png) |
| ---------------------------------------------------- | ---------------------------------------------------- |
|                                                      |                                                      |

**Solution** -> Check whether you have supplied a valid license

#### No Internet

![No internet dialog](assets/NoInternet.png)

**Solution** -> Check your internet connection



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
