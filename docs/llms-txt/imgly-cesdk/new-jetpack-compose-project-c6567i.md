# Source: https://img.ly/docs/cesdk/android/get-started/new-jetpack-compose-project-c6567i/

---
title: "Android Jetpack Compose New Project Setup"
description: "Complete guide to integrate CreativeEditor SDK into a new Android Jetpack Compose project."
platform: android
url: "https://img.ly/docs/cesdk/android/get-started/new-jetpack-compose-project-c6567i/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Get Started](https://img.ly/docs/cesdk/android/get-started/overview-e18f40/) > [Quickstart Jetpack Compose](https://img.ly/docs/cesdk/android/get-started/new-jetpack-compose-project-c6567i/)

---

This comprehensive guide walks you through integrating the CreativeEditor SDK
(CE.SDK) into a new Android Jetpack Compose project from scratch. By the end,
you'll have a fully functional creative editor running in your Android app,
ready for: - photo editing - design creation - video processing

## Who Is This Guide For?

This guide is for developers who:

- Have experience with Android development and Kotlin
- Want to create a new Android Jetpack Compose project with integrated creative editing capabilities
- Need to implement user-friendly editing interfaces
- Want to add professional-grade:
  - image editing
  - design creation
  - video editing to their Android apps
- Prefer using Jetpack Compose for modern Android UI development

## What You'll Achieve

By following this guide, you:

- Create a new Android Jetpack Compose project with CreativeEditor SDK integration
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
- **Jetpack Compose**: Latest BOM version
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

> **Note:** You can customize the CreativeEditor SDK for Android exclusively through
> Kotlin code, as described in the
> [configuration overview section](https://img.ly/docs/cesdk/android/user-interface/customization-72b2f8/).

## Step 1: Create a New Android Jetpack Compose Project

First, verify your Android Studio installation and create a new project:

1. **Open Android Studio** and select "New Project"
2. **Choose "Empty Activity"** template
3. **Configure your project**:
   - Name: `cesdk_android_app`
   - Package name: `com.example.cesdkapp`
   - Language: **Kotlin**
   - Minimum SDK: **API 24 (Android 7.0)**
   - Build configuration language: **Kotlin DSL**

### Project Structure

Your new project should have this structure:

```
cesdk_android_app/
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

<ImageContainer image="android-project-structure.png" />

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

    // Jetpack Compose dependencies
    implementation(platform("androidx.compose:compose-bom:2025.04.01"))
    implementation("androidx.activity:activity-compose")
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.ui:ui-graphics")
    implementation("androidx.compose.ui:ui-tooling-preview")
    implementation("androidx.compose.material3:material3")

    // Other Android dependencies
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.7.0")
    implementation("androidx.activity:activity-compose:1.8.2")
}
```

This adds the latest version of the CreativeEditor SDK editor to your `build.gradle.kts` file.

### 2.3 Configure Android Settings

Update your `app/build.gradle.kts` to ensure proper configuration:

```kotlin title="build.gradle.kts"
android {
    namespace = "com.example.cesdkapp"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.example.cesdkapp"
        minSdk = 24  // Required for CE.SDK
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
        vectorDrawables {
            useSupportLibrary = true
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = "17"
    }

    buildFeatures {
        compose = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.8"
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

In Android Studio, click **Sync Project with Gradle Files** to download and configure all dependencies.

This downloads and installs the CreativeEditor SDK and its dependencies automatically through Gradle.

## Step 3: Implement the Editor Integration

Now let's implement the CreativeEditor SDK editor in your Android Jetpack Compose application:

### 3.1 Create Editor Composable

Create a new file `EditorComposable.kt` in your project:

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

### 3.2 Update MainActivity

Update your `MainActivity.kt` to use the editor composable:

```kotlin title="MainActivity.kt"
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.ui.Modifier

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
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

### 3.3 Add Required Permissions

Add the necessary permissions to your `AndroidManifest.xml`:

```xml title="AndroidManifest.xml"
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    package="com.example.cesdkapp">

    
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
        android:theme="@style/Theme.Material3.DayNight"
        tools:targetApi="31">

        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:theme="@style/Theme.Material3.DayNight">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

## Step 4: Test Your Editor Integration

Now let's test your CreativeEditor SDK editor integration:

### 4.1 Build and Run

Build your Android project using Gradle:

### 4.2 Test on Android Device

Connect your Android device and run:

```bash
# Build and install the app
./gradlew installDebug

# Or run from Android Studio
# Click the "Run" button (green play icon)
```

### 4.3 Verify Features

When the app launches successfully, you should see:

1. **Main Screen**: A clean Android Jetpack Compose interface
2. **Editor Launch**: The CreativeEditor SDK editor should open immediately
3. **Editor Features**: You should be able to access:
   - photo editing tools
   - design creation tools
   - video editing capabilities
4. **User Interface**: The editor should have a complete UI with:
   - toolbar with editing tools
   - canvas for design work
   - panels for assets and properties

### 4.4 Common Test Scenarios

Test these scenarios to ensure everything works:

- **Editor Launch**: Verify the editor opens properly
- **Tool Access**: Test that all editing tools are accessible
- **Media Import**: Import photos from your device gallery
- **Basic Editing**: Try basic editing features like:
  - filters and effects
  - text addition and styling
  - shape and graphic tools
- **Save/Export**: Test saving and exporting edited content
- **Navigation**: Ensure proper navigation within the editor

> **Note**: The first build may take several minutes as it compiles all native dependencies. Subsequent builds are faster.

## Step 5: Customize for Your Use Case

The CreativeEditor SDK editor offers different presets for common use cases:

### 5.1 Editor Configuration Options

#### Available Editor Types Summary

The CreativeEditor SDK provides several editor types for different use cases:

| Editor Type      | Description                 | Use Case                            |
| ---------------- | --------------------------- | ----------------------------------- |
| `DesignEditor`   | Full-featured design editor | General design creation and editing |
| `PhotoEditor`    | Photo editing focused       | Image enhancement and photo editing |
| `VideoEditor`    | Video editing focused       | Video processing and editing        |
| `ApparelEditor`  | Apparel design focused      | T-shirt and merchandise design      |
| `PostcardEditor` | Postcard design focused     | Greeting cards and postcards        |

**Available Editor Types with Parameters:**

| Editor Type           | Parameters                                                  | Use Case                |
| --------------------- | ----------------------------------------------------------- | ----------------------- |
| `rememberForDesign`   | license, userId, baseUri, sceneUri, renderTarget            | General design creation |
| `rememberForPhoto`    | license, imageUri, imageSize, userId, baseUri, renderTarget | Photo editing           |
| `rememberForVideo`    | license, userId, baseUri, sceneUri, renderTarget            | Video editing           |
| `rememberForApparel`  | license, userId, baseUri, sceneUri, renderTarget            | T-shirt/apparel design  |
| `rememberForPostcard` | license, userId, baseUri, sceneUri, renderTarget            | Postcard creation       |

Choose the appropriate editor type based on your use case:

```kotlin title="EditorComposable.kt"
// For photo editing
@Composable
fun PhotoEditorComposable() {
    val engineConfiguration = EngineConfiguration.rememberForPhoto(
        license = "<your license here>",
        userId = "<your unique user id>",
    )

    PhotoEditor(
        engineConfiguration = engineConfiguration,
        onClose = { /* handle close */ }
    )
}

// For video editing
@Composable
fun VideoEditorComposable() {
    val engineConfiguration = EngineConfiguration.rememberForVideo(
        license = "<your license here>",
        userId = "<your unique user id>",
    )

    VideoEditor(
        engineConfiguration = engineConfiguration,
        onClose = { /* handle close */ }
    )
}
```

### 5.2 Custom Configuration

**Note**: Custom configuration features are currently limited in version 1.57.0 for new Jetpack Compose projects. Basic editor types work as expected.

You can customize the editor configuration for your specific needs:

```kotlin title="EditorComposable.kt"
@Composable
fun CustomEditorComposable() {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = "<your license here>",
        userId = "<your unique user id>",
        // Custom configuration options
        configuration = {
            // Configure editor appearance
            appearance {
                theme = Theme.DARK
                primaryColor = Color.Blue
            }

            // Configure available tools
            tools {
                // Enable/disable specific tools
                text = true
                shapes = true
                filters = true
                effects = false
            }

            // Configure asset sources
            assets {
                // Add custom asset sources
                addImageSource("my-images", "https://my-api.com/images")
            }
        }
    )

    DesignEditor(
        engineConfiguration = engineConfiguration,
        onClose = { /* handle close */ }
    )
}
```

## Step 6: Troubleshooting

If you encounter issues, here are common solutions:

### 6.1 Build Issues

#### 1. Gradle Sync Errors

**Problem**: Gradle sync fails with dependency resolution errors.

**Solution**:

1. Check your internet connection
2. Verify the IMG.LY repository URL is correct
3. Clean and rebuild the project:

```bash
./gradlew clean
./gradlew build
```

#### 2. Compilation Errors

**Problem**: Kotlin compilation errors related to Compose.

**Solution**: Ensure your Compose compiler version matches your Kotlin version. Check the [official compatibility matrix](https://developer.android.com/jetpack/androidx/releases/compose-kotlin).

#### 3. Runtime Errors

**Problem**: App crashes on startup with editor-related errors.

**Solution**:

1. Verify your license key is valid (or pass `null` for evaluation mode with watermark)
2. Check that minSdk is set to 24 or higher
3. Ensure all required permissions are declared in AndroidManifest.xml

### 6.2 Performance Issues

#### 1. Slow Editor Loading

**Problem**: Editor takes too long to load or is sluggish.

**Solution**:

1. Ensure you're running on a device with sufficient GPU capabilities
2. Check that the device has adequate memory
3. Verify the engine configuration is optimized

#### 2. Memory Issues

**Problem**: App crashes due to memory issues during editing.

**Solution**:

1. Implement proper memory management
2. Monitor memory usage during editing operations
3. Use appropriate image sizes and formats

### 6.3 Integration Issues

#### 1. Editor Not Displaying

**Problem**: Editor doesn't appear or display correctly.

**Solution**:

1. Check that the Composable is properly integrated
2. Verify the engine configuration is correct
3. Ensure proper lifecycle management

#### 2. Tool Access Issues

**Problem**: Editing tools are not accessible or don't work.

**Solution**:

1. Check the editor configuration and tool permissions
2. Verify that the license includes the required features
3. Ensure proper asset loading and access

## Step 7: Next Steps

Now that you have a basic CreativeEditor SDK editor integration, you can:

### 7.1 Explore Advanced Features

- **[Editor Configuration](https://img.ly/docs/cesdk/android/configuration-2c1c3d/)**: Learn advanced editor customization
- **[Custom Tools](https://img.ly/docs/cesdk/android/configuration-2c1c3d/)**: Implement custom editing tools
- **[Asset Management](https://img.ly/docs/cesdk/android/import-media/concepts-5e6197/)**: Manage and organize media assets
- **[Performance Optimization](https://img.ly/docs/cesdk/android/configuration-2c1c3d/)**: Optimize editor performance

### 7.2 Integrate with Other Components

- **[Engine Integration](https://img.ly/docs/cesdk/android/engine-interface-6fb7cf/)**: Add custom engine features
- **[Camera Integration](https://img.ly/docs/cesdk/android/import-media-4e3703/)**: Capture media directly in your app
- **[Navigation Integration](https://img.ly/docs/cesdk/android/user-interface/customization/navigation-bar-4e5d39/)**: Integrate with app navigation

### 7.3 Production Considerations

- **License Management**: Implement proper license validation
- **Error Handling**: Add comprehensive error handling
- **Performance Monitoring**: Monitor editor performance in production
- **Testing**: Implement comprehensive testing for editor features

## Additional Resources

- **[CreativeEditor SDK Documentation](https://img.ly/docs/cesdk/)**
- **[Android Examples Repository](https://github.com/imgly/cesdk-android-examples)**
- **[Community Support](https://img.ly/support)**

Congratulations! You've successfully integrated the CreativeEditor SDK editor into your Android Jetpack Compose application. Your app now has powerful creative editing capabilities that work seamlessly on Android devices.



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
