# Source: https://img.ly/docs/cesdk/android/get-started/new-activity-based-ui-project-d7678j/

---
title: "New Project Setup"
description: "Learn how to integrate the CreativeEditor SDK into a new Android Activity-based project"
platform: android
url: "https://img.ly/docs/cesdk/android/get-started/new-activity-based-ui-project-d7678j/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Get Started](https://img.ly/docs/cesdk/android/get-started/overview-e18f40/) > [Quickstart Activity](https://img.ly/docs/cesdk/android/get-started/new-activity-based-ui-project-d7678j/)

---

This guide shows you how to integrate the CreativeEditor SDK into a **new Android Activity-based project**. Learn how to:

- **create** a new project.
- **add** the necessary dependencies.
- **configure** the editor.
- **test** the integration.

## Who Is This Guide For?

This guide is for developers who:

- Have experience with Android development and Kotlin
- Want to create a new Android Activity-based project with integrated creative editing capabilities
- Need to implement user-friendly editing interfaces
- Want to add professional-grade image editing, design creation, and video editing to their Android apps
- Prefer using traditional Android Views with Activity-based architecture

## What You'll Achieve

By following this guide, you:

- Create a new Android Activity-based project with CreativeEditor SDK integration
- Configure platform-specific requirements for Android
- Implement a functional editor that you can launch from your app
- Test and verify the integration works correctly

[Explore Android Demos](https://img.ly/showcases/cesdk/?tags=android)

[View on GitHub](https://github.com/imgly/cesdk-android-examples)

## Prerequisites

Before you begin, ensure you have the following requirements:

### Development Environment

- **Android Studio**: Latest version (Hedgehog or later)
- **Kotlin**: 1.9.10 or later
- **Gradle**: 8.4 or later
- **Git CLI** for version control

### Platform Requirements

- **Android**: 7.0+ (API level 24+)
- **Minimum SDK**: 24
- **Target SDK**: Latest stable version

### License

- A valid **CE.SDK license key** ([Get a free trial](https://img.ly/forms/free-trial)), use `null` or an empty string to run in evaluation mode with watermark.

### Verify Your Setup

Run the following command to verify your Android development environment:

```bash
gradle --version
```

This command checks your Gradle installation and reports any issues to resolve before proceeding.

> **Note:** You can customize the CreativeEditor SDK for Android through **native code
> (Kotlin) only**, as described in the
> [configuration overview section](https://img.ly/docs/cesdk/android/user-interface/customization-72b2f8/).

## Step 1: Create a New Android Activity-Based Project

First, verify your Android Studio installation and create a new project:

1. **Open Android Studio** and select "New Project"
2. **Choose "Empty Views Activity"** template
3. **Configure your project**:
   - Name: `cesdk_android_activity_app`
   - Package name: `com.example.cesdkactivityapp`
   - Language: **Kotlin**
   - Minimum SDK: **API 24 (Android 7.0)**
   - Build configuration language: **Kotlin DSL**

### Project Structure

Your new project should have this structure:

```
cesdk_android_activity_app/
├── app/                    # Main application module
│   ├── src/main/
│   │   ├── java/          # Kotlin source files
│   │   ├── res/           # Resources
│   │   └── AndroidManifest.xml
│   ├── build.gradle.kts   # App-level build configuration
│   └── proguard-rules.pro # ProGuard rules
├── gradle/                 # Gradle wrapper
├── build.gradle.kts        # Project-level build configuration
├── settings.gradle.kts     # Project settings
└── gradle.properties       # Gradle properties
```

## Step 2: Add the CreativeEditor SDK Dependency

Add the CreativeEditor SDK to your project by updating the build configuration:

### 2.1 Add IMG.LY Repository

Update your `settings.gradle.kts` to include the IMG.LY repository:

```kotlin title="settings.gradle.kts"
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
        // Add CE.SDK dependency here
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

### 2.2 Add Editor Dependency

Update your `app/build.gradle.kts` to include the editor dependency:

```kotlin title="build.gradle.kts"
dependencies {
    implementation("ly.img:editor:1.57.0")

    // Required dependencies for CE.SDK (includes Compose internally)
    implementation("androidx.appcompat:appcompat:1.6.1")
    implementation("androidx.activity:activity-compose:1.8.2")
    implementation("androidx.compose.ui:ui:1.5.4")
    implementation("androidx.compose.material3:material3:1.1.2")

    // Other Android dependencies
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.7.0")
    implementation("com.google.android.material:material:1.11.0")
}
```

### 2.3 Configure Android Settings

Ensure your `app/build.gradle.kts` has the correct Android configuration:

```kotlin title="build.gradle.kts"
android {
    compileSdk = 34

    defaultConfig {
        minSdk = 24
        targetSdk = 34
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

### 2.4 Sync Project

After adding the dependency, sync your project to download the CreativeEditor SDK:

In Android Studio, click **Sync Project with Gradle Files**. This downloads and installs the CreativeEditor SDK and its dependencies automatically through Gradle.

## Step 3: Implement the Editor Integration

### 3.1 Create Editor Activity

Create a new Kotlin file called `EditorActivity.kt` in your app module's main source set (typically `app/src/main/java/com/yourpackage/`):

```kotlin file=@cesdk_android_examples/editor-guides-quickstart/EditorActivity.kt
import android.os.Bundle
import androidx.activity.compose.setContent
import androidx.appcompat.app.AppCompatActivity
import ly.img.editor.DesignEditor
import ly.img.editor.EngineConfiguration
import ly.img.editor.rememberForDesign

class EditorActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
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
                    finish()
                },
            )
        }
    }
}
```

### 3.2 Update MainActivity

Modify your existing `MainActivity.kt` file (located in `app/src/main/java/com/yourpackage/`) to launch the editor:

```kotlin title="MainActivity.kt"
import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.cesdkactivityapp.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.launchEditorButton.setOnClickListener {
            val intent = Intent(this, EditorActivity::class.java)
            startActivity(intent)
        }
    }
}
```

### 3.3 Update Layout File

Update your `activity_main.xml` to include a button:

```xml title="activity_main.xml"
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center">

    <Button
        android:id="@+id/launchEditorButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Launch Creative Editor SDK" />

</LinearLayout>
```

### 3.4 Add Required Permissions

Update your `AndroidManifest.xml` to include necessary permissions and register the activity:

```xml title="AndroidManifest.xml"
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.cesdkactivityapp">

    
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
        android:theme="@style/Theme.Material3.DayNight">

        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:theme="@style/Theme.Material3.DayNight">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <activity
            android:name=".EditorActivity"
            android:exported="false"
            android:theme="@style/Theme.Material3.DayNight" />
    </application>
</manifest>
```

## Step 4: Test Your Editor Integration

### 4.1 Build and Run

Build your Android project using Gradle:

### 4.2 Test on Android Device

```bash
./gradlew installDebug
```

### 4.3 Verify Features

After launching your app, verify these features work correctly:

- **App Launch**: The main activity opens without errors
- **Button Interaction**: The "Launch Creative Editor SDK" button responds to taps
- **Editor Launch**: The CreativeEditor SDK opens without errors
- **Template Selection**: You can browse and select templates
- **Editing Tools**: All editing tools are accessible and functional
- **Export**: You can export edited content successfully
- **Navigation**: The editor closes properly when finished

### 4.4 Common Test Scenarios

- **Photo Editing**: Import and edit photos
- **Text Addition**: Add and customize text elements
- **Template Usage**: Apply and customize templates
- **Export Options**: Test different export formats
- **Performance**: Verify smooth operation on target devices

## Step 5: Customize for Your Use Case

### 5.1 Editor Configuration Options

The CreativeEditor SDK offers different presets for common use cases:

| Editor Type      | Use Case                      | Kotlin Implementation     |
| ---------------- | ----------------------------- | ------------------------- |
| **PhotoEditor**  | Photo editing and enhancement | `PhotoEditor` composable  |
| **DesignEditor** | Graphic design and templates  | `DesignEditor` composable |
| **VideoEditor**  | Video editing and effects     | `VideoEditor` composable  |

### 5.2 Custom Configuration

You can customize the editor behavior:

```kotlin title="EditorActivity.kt"
class CustomEditorActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val engineConfiguration = EngineConfiguration.rememberForDesign(
            license = "<your license here>",
            userId = "<your unique user id>",
            // Add custom configuration here
        )

        setContent {
            DesignEditor(
                engineConfiguration = engineConfiguration,
                onClose = { finish() },
                onExport = { result -> /* Handle export */ }
            )
        }
    }
}
```

## Step 6: Troubleshooting

### Common Issues and Solutions

#### Gradle Sync Issues

- **Problem**: Repository not found
- **Solution**: Verify the IMG.LY repository URL in `settings.gradle.kts`

#### Compilation Errors

- **Problem**: Missing dependencies
- **Solution**: Ensure all required dependencies are included

#### Runtime Errors

- **Problem**: Invalid license
- **Solution**: Verify your license key is correct and valid (or pass `null` for evaluation mode with watermark)

#### Performance Issues

- **Problem**: Slow editor loading
- **Solution**: Check device specifications and memory usage

#### Integration Issues

- **Problem**: Editor not displaying
- **Solution**: Verify the activity is properly registered in AndroidManifest.xml

## Step 7: Next Steps

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
- [Android Activity Documentation](https://developer.android.com/guide/components/activities)
- [Android Development Guide](https://developer.android.com/guide)



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
