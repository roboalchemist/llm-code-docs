# Source: https://img.ly/docs/cesdk/android/get-started/existing-project-g0901m/

---
title: "Existing Project Setup"
description: "Learn how to integrate the CreativeEditor SDK into your existing Android Jetpack Compose project"
platform: android
url: "https://img.ly/docs/cesdk/android/get-started/existing-project-g0901m/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Get Started](https://img.ly/docs/cesdk/android/get-started/overview-e18f40/) > [Quickstart Jetpack Compose](https://img.ly/docs/cesdk/android/get-started/new-jetpack-compose-project-c6567i/)

---

This guide shows you how to integrate the CreativeEditor SDK into your existing Android Jetpack Compose project. Follow these steps to learn how to:

- **add** the necessary dependencies.
- **configure** the editor.
- **test** the integration.

## Who Is This Guide For?

This guide is for developers who:

- Have an existing Android Jetpack Compose project
- Want to add CreativeEditor SDK features to their app
- Need to understand common integration patterns
- Want to test available editing capabilities and workflows

## What You'll Achieve

By following this guide, you'll perform the following tasks:

- **Project Integration**: Add CreativeEditor SDK to your existing Android project
- **Editor Implementation**: Implement the editor with proper lifecycle management
- **Testing**: Verify the integration works correctly
- **Customization**: Learn how to customize the editor for your use case

[View Android Examples](https://github.com/imgly/cesdk-android-examples)

[Android Documentation](https://img.ly/docs/cesdk/android)

## Prerequisites

### Development Environment

- Android Studio (latest version)
- Android SDK (API level 24 or higher)
- Kotlin 1.9.10 or higher
- Gradle 8.4 or later
- Jetpack Compose BOM 2023.05.01 or higher

### Platform Requirements

- **Android**: API level 24 (Android 7.0) or higher
- **Supported ABIs**: arm64-v8a, armeabi-v7a, x86\_64, x86

### License

- A valid **CE.SDK license key** ([Get a free trial](https://img.ly/forms/free-trial)), use `null` or an empty string to run in evaluation mode with watermark.

## Verify Your Setup

Before starting, verify your Android development environment:

```bash
gradle --version
```

This command checks your Gradle installation and reports any issues to resolve before proceeding.

> **Note:** You can customize the CreativeEditor SDK for Android exclusively through
> native code (Kotlin), as described in the
> [configuration overview section](https://img.ly/docs/cesdk/android/user-interface/customization-72b2f8/).

## Step 1: Add Dependencies to Your Existing Project

### 1.1 Add IMG.LY Repository

Update your `settings.gradle.kts` file to include the IMG.LY repository:

```kotlin title="settings.gradle.kts"
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
        maven {
            name = "IMG.LY Artifactory"
            url = uri("https://artifactory.img.ly/artifactory/maven")
            mavenContent {
                includeGroup("ly.img")
            }
        }
    }
}
```

### 1.2 Add Editor Dependencies

Update your `app/build.gradle.kts` file to include the CreativeEditor SDK:

```kotlin title="build.gradle.kts"
dependencies {
    // CreativeEditor SDK
    implementation("ly.img:editor:1.57.0")

    // Jetpack Compose BOM
    implementation(platform("androidx.compose:compose-bom:2025.04.01"))
    implementation("androidx.activity:activity-compose")
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.ui:ui-tooling-preview")
    implementation("androidx.compose.material3:material3")
    implementation("androidx.compose.runtime:runtime")
    implementation("androidx.compose.foundation:foundation")
}
```

### 1.3 Configure Android Settings

Ensure your `app/build.gradle.kts` has the correct Android configuration:

```kotlin title="build.gradle.kts"
android {
    compileSdk = 34

    defaultConfig {
        minSdk = 24
        targetSdk = 34
    }

	buildFeatures {
        compose = true
	}

	composeOptions {
	    kotlinCompilerExtensionVersion = "1.5.15"
	}

    kotlinOptions {
        jvmTarget = "17"
    }

    packaging {
        resources {
            excludes += "/META-INF/{AL2.0,LGPL2.1}"
        }
    }
}
```

### 1.4 Sync Project

After adding the dependencies, sync your project:

In Android Studio, click **Sync Project with Gradle Files** to download and configure all dependencies. This downloads and installs the CreativeEditor SDK and its dependencies automatically through Gradle.

## Step 2: Implement the Editor Integration

### 2.1 Create Editor Composable

Create a new Kotlin file (for example, `EditorComposable.kt`) in your project:

```kotlin file=@cesdk_android_examples/editor-guides-quickstart/EditorComposable.kt
import androidx.compose.runtime.Composable
import ly.img.editor.DesignEditor
import ly.img.editor.EngineConfiguration
import ly.img.editor.rememberForDesign

@Composable
fun EditorComposable() {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        // Get your license from https://img.ly/forms/free-trial
        // pass null or empty for evaluation mode with watermark
        license = "<your license here>",
        userId = "<your unique user id>", // A unique string to identify your user/session
    )

    DesignEditor(
        engineConfiguration = engineConfiguration,
        onClose = {
            // Close the editor here
            // If using a navigation library, call pop() or navigateUp() here
        },
    )
}
```

### 2.2 Update Your MainActivity

Modify your existing `MainActivity.kt` to include the editor:

```kotlin title="MainActivity.kt"
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.ui.Modifier

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    EditorComposable()
                }
            }
        }
    }
}
```

### 2.3 Add Required Permissions

Update your `AndroidManifest.xml` to include necessary permissions:

```xml title="AndroidManifest.xml"
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="your.package.name">

    
    <uses-permission android:name="android.permission.INTERNET" />

    
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.RECORD_AUDIO" />

    
    <uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />
    <uses-permission android:name="android.permission.READ_MEDIA_VIDEO" />
    <uses-permission android:name="android.permission.READ_MEDIA_AUDIO" />

    
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"
                     android:maxSdkVersion="29" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"
                     android:maxSdkVersion="29" />

    
    <uses-permission android:name="android.permission.READ_MEDIA_VISUAL_USER_SELECTED" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.YourApp">

        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:theme="@style/Theme.YourApp">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

## Step 3: Test Your Editor Integration

### 3.1 Build and Run

Build your Android project using Gradle:

### 3.2 Test on Android Device

```bash
./gradlew installInternalDebug
```

### 3.3 Verify Features

After launching your app, verify these features work correctly:

- **Editor Launch**: The CreativeEditor SDK opens without errors
- **Template Selection**: You can browse and select templates
- **Editing Tools**: All editing tools are accessible and functional
- **Export**: You can export edited content successfully
- **Navigation**: The editor closes properly when finished

### 3.4 Common Test Scenarios

- **Photo Editing**: Import and edit photos
- **Text Addition**: Add and customize text elements
- **Template Usage**: Apply and customize templates
- **Export Options**: Test different export formats
- **Performance**: Verify smooth operation on target devices

## Step 4: Customize for Your Use Case

### 4.1 Editor Configuration Options

The CreativeEditor SDK offers different presets for common use cases:

#### Available Editor Types Summary

| Editor Type           | Parameters                                                  | Use Case                |
| --------------------- | ----------------------------------------------------------- | ----------------------- |
| `rememberForDesign`   | license, userId, baseUri, sceneUri, renderTarget            | General design creation |
| `rememberForPhoto`    | license, imageUri, imageSize, userId, baseUri, renderTarget | Photo editing           |
| `rememberForVideo`    | license, userId, baseUri, sceneUri, renderTarget            | Video editing           |
| `rememberForApparel`  | license, userId, baseUri, sceneUri, renderTarget            | T-shirt/apparel design  |
| `rememberForPostcard` | license, userId, baseUri, sceneUri, renderTarget            | Postcard creation       |

| Editor Type      | Use Case                      | Kotlin Implementation     |
| ---------------- | ----------------------------- | ------------------------- |
| **PhotoEditor**  | Photo editing and enhancement | `PhotoEditor` composable  |
| **DesignEditor** | Graphic design and templates  | `DesignEditor` composable |
| **VideoEditor**  | Video editing and effects     | `VideoEditor` composable  |

### 4.2 Custom Configuration

You can customize the editor behavior:

```kotlin title="EditorComposable.kt"
@Composable
fun CustomEditorComposable() {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = "<your license here>",
        userId = "<your unique user id>",
        // Add custom configuration here
    )

    DesignEditor(
        engineConfiguration = engineConfiguration,
        onClose = { /* Handle close */ },
        onExport = { result -> /* Handle export */ }
    )
}
```

## Step 5: Troubleshooting

### Common Issues and Solutions

#### Gradle Sync Issues

- **Problem**: Repository not found
- **Solution**: Verify the IMG.LY repository URL in `settings.gradle.kts`

#### Compilation Errors

- **Problem**: Missing dependencies
- **Solution**: Ensure you've installed all Jetpack Compose dependencies.

#### Runtime Errors

- **Problem**: Invalid license
- **Solution**: Verify your license key is correct and valid (or pass `null` for evaluation mode with watermark)

#### Performance Issues

- **Problem**: Slow editor loading
- **Solution**: Check device specifications and memory usage

#### Integration Issues

- **Problem**: Editor not displaying
- **Solution**: Verify the composable is properly called in your activity

## Step 6: Next Steps

### Advanced Features

- Implement custom asset sources
- Add custom filters and effects
- Integrate with your backend services
- Implement user authentication

### Other Integrations

- Explore camera integration
- Add video editing capabilities
- Implement batch processing
- Add cloud storage integration

### Production Considerations

- Optimize for performance
- Implement proper error handling
- Add analytics and monitoring
- Test on different device configurations

## Additional Resources

- [CreativeEditor SDK Documentation](https://img.ly/docs/cesdk/android)
- [Android Examples Repository](https://github.com/imgly/cesdk-android-examples)
- [Jetpack Compose Documentation](https://developer.android.com/jetpack/compose)
- [Android Development Guide](https://developer.android.com/guide)



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
