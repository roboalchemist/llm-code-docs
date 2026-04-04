# Source: https://docs.instabug.com/android/set-up-luciq-for-android/set-up-crash-reporting/deobfuscation-for-android.md

# Deobfuscation for Android

Deobfuscation requires uploading the ProGuard/R8 mapping files (mapping.txt) and .so corresponding to your release builds.

### Deobfuscating Java/Kotlin Crashes

You can upload mapping files using one of these ways:

1. **Manually via the Luciq Dashboard**
2. **Automated via Gradle Plugin (Straightforward & Recommended)**
3. **Automated via Script**
4. **Automated via API**

#### Recovering Mapping Files from Google Play Console

{% hint style="info" %}
When uploading your .aab to the Google Play Console (or any other store), it's a good practice to **keep a backup of the mapping file** in case automated upload methods fail.
{% endhint %}

If you need to upload the mapping file **after the AAB has already been published**, you can still retrieve it from the Google Play Console by following these steps:

1. Go to **Google Play Console → Test and release → Production**
2. Open **App bundles** and select **Details**

   ![](https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2Fgit-blob-ef40c4f4037e2b72aebd8932c8ad634812bf5bef%2Fgoogle-play-app-bundles.png?alt=media)
3. Download the published app bundle

   ![](https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2Fgit-blob-ec217d5420c7d923e5c0cba6ef36f9643d744b75%2Fgoogle-play-download-bundle.png?alt=media)
4. Rename the file from app-release.aab to app-release.zip then extract the ZIP file
5. Navigate to: `BUNDLE-METADATA/com.android.tools.build.obfuscation/`
6. Locate the proguard.map file then rename it to proguard.txt
7. Upload the file **manually via the Luciq Dashboard**

This allows you to recover and upload the correct mapping file even after your app has already been released.

#### 1. Uploading Manually via the Dashboard

1. Open your **Luciq Dashboard**.
2. Go to **Settings → Upload Mapping Files**.
3. Upload your mapping.txt file.

Multiple mapping files can be uploaded for different app versions.

![](https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2Fgit-blob-3f9b16cb27b0d77ec21abb459d0ff354684b4aa8%2Fupload-mapping-files-dashboard.png?alt=media)

#### 2. Uploading via Gradle Plugin

Using the Luciq plugin ensures that mapping files are uploaded **automatically**.

{% hint style="info" %}
If you're using **Gradle Version Catalog TOML**, please check out this [page](https://docs.luciq.ai/android/set-up-luciq-for-android/integrate-luciq-on-android/updating-the-sdk#gradle-version-catalog-toml) for adding 'luciq-plugin'.
{% endhint %}

**Step 1: Add the Plugin to your buildscript**

{% tabs %}
{% tab title="Gradle" %}
{% code overflow="wrap" %}

```gradle
buildscript {
    dependencies {
        classpath "ai.luciq.library:luciq-plugin:x.y.z"
    }
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

**Step 2: Apply the plugin in your app module**

Add `apply plugin: 'luciq-crash'` to your app's Gradle file.

**Step 3: Configure the plugin**

Ready to go example:

{% tabs %}
{% tab title="Gradle" %}
{% code overflow="wrap" %}

```gradle
luciq {
    crashReporting {
        autoUploadEnabled = true
        appToken = "YOUR_APP_TOKEN"
    }
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

Full example:

{% tabs %}
{% tab title="Gradle" %}
{% code overflow="wrap" %}

```gradle
luciq {
    crashReporting {
        /**
         * Application token
         * Required: Yes (when autoUploadEnabled = true, otherwise build fails)
         */
        appToken = "YOUR_APP_TOKEN"

        /**
         * Controls whether mapping files should be automatically uploaded.
         * Required: No
         * Default: false
         * Purpose: When enabled, attaches upload tasks to whitelisted variant build flows.
         *          When disabled, upload tasks are skipped entirely.
         */
        autoUploadEnabled = true

        /**
         * Enables experimental support for GuardSquare's obfuscation tools (ProGuard/DexGuard).
         * Required: No
         * Default: false
         * Purpose: Allows detection and processing of minification from GuardSquare tools
         *          in addition to AGP's built-in minification.
         */
        experimentalGuardSquareSupportEnabled = false

        /**
         * Custom upload URL for mapping files.
         * Required: No
         * Purpose: Allows overriding the default upload endpoint for on-premise
         *          or custom backend deployments.
         */
        uploadUrl = "https://your-custom-url.com"

        /**
         * Lambda function to configure per-variant settings.
         * Required: No
         * Default: Debug variants are not whitelisted by default
         * Purpose: Provides fine-grained control over which variants get upload tasks
         *          and allows custom mapping file paths per variant.
         */
        variantConfigurations { configurations ->
            // The name of the variant being configured.
            def variantName = configurations.name

            /**
             * Controls whether this variant should have upload tasks created.
             * Required: No
             * Default: true (except debug variants which are false by default)
             * Purpose: Whitelists a variant for the plugin to create and attach
             *          upload task to its build flow.
             */
            configurations.setWhitelisted(true)

            /**
             * Path to a custom mapping file for this variant.
             * Required: No
             * Default: null (automatic mapping file detection is used)
             * Purpose: Allows specifying an alternative mapping file location
             *          instead of the auto-detected one from the build.
             */
            configurations.setCustomMappingFilePath("FILE_PATH")
        }
    }
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

This ensures mapping files are uploaded automatically during your **build process**.

#### 3. Uploading via Script

Automating uploads ensures that mapping files are uploaded **every time a release build is generated**.

**Step 1: Create the Upload Script**

Create a file called `upload_mapping.sh` at the **root of your project**:

{% tabs %}
{% tab title="Shell" %}
{% code overflow="wrap" %}

```sh
#!/bin/bash
echo "Luciq mapping files uploader"

APP_TOKEN="$1"
VERSION_CODE="$2"
VERSION_NAME="$3"
PATH_TO_MAPPING_FILE="$4"
VERSION='{"code":"'"$VERSION_CODE"'","name":"'"$VERSION_NAME"'"}'

if [ ! -f "$PATH_TO_MAPPING_FILE" ]; then
    echo "File not found: $PATH_TO_MAPPING_FILE"
    exit 1
fi

echo "Mapping file found! Uploading..."

ENDPOINT="https://api.instabug.com/api/sdk/v3/symbols_files"
STATUS=$(curl "${ENDPOINT}" \
  --write-out %{http_code} \
  --silent \
  --output /dev/null \
  -F os=android \
  -F app_version="${VERSION}" \
  -F symbols_file=@"${PATH_TO_MAPPING_FILE}" \
  -F application_token="${APP_TOKEN}")

if [ "$STATUS" -ne 200 ]; then
  echo "Error while uploading mapping files (HTTP $STATUS)"
  exit 1
fi

echo "Success! Your mapping files got uploaded successfully"
```

{% endcode %}
{% endtab %}
{% endtabs %}

**Step 2: Add the Gradle Task**

Add the following to your **app module's** `build.gradle` **(Groovy DSL)**:

{% tabs %}
{% tab title="Gradle" %}
{% code overflow="wrap" %}

```gradle
tasks.register('uploadMappingFiles') {
    doLast {
        android.applicationVariants.all { variant ->
            if (variant.buildType.name == "release") {
                def mappingFile = variant.mappingFile
                if (mappingFile == null || !mappingFile.exists()) {
                    logger.lifecycle("No mapping file for ${variant.name}")
                    return
                }
                exec {
                    commandLine(
                        "/bin/sh",
                        "${rootDir}/upload_mapping.sh",
                        "YOUR_APP_TOKEN",
                        variant.versionCode.toString(),
                        variant.versionName,
                        mappingFile.absolutePath
                    )
                }
            }
        }
    }
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Notes:**

* Use **absolute paths** (`${rootDir}`) for the script.
* Mapping files are generated **only after assembling a release variant**.
  {% endhint %}

**Step 3: Run the Task**

First, build your release variant:\
`./gradlew :app:assembleRelease`

Then upload the mapping file:\
`./gradlew :app:uploadMappingFiles`

{% hint style="success" %}
**Tip:** For CI/CD, you can attach the upload task directly to the release build to ensure mapping files always exist.
{% endhint %}

#### 4. Uploading via API

You can also upload mapping files directly via API. Mapping files must be uploaded as a .txt file.

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```
curl --location --request POST 'https://api.instabug.com/api/sdk/v3/symbols_files' \
--form 'os="android"' \
--form 'application_token="YOUR_APP_TOKEN"' \
--form 'app_version="{\"code\":\"7\",\"name\":\"7.7\"}"' \
--form 'symbols_file=@"./mapping.txt"'
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Deobfuscating NDK/C++ Crashes

By default, native crashes are obfuscated. In order to deobfuscate them, you'll need to upload the relevant .so files and we'll take care of the rest.

#### Locating .so Files

The .so files are usually found in specific directories related to the different app architectures. You can find below the different files, as well as their related architecture.

![](https://files.readme.io/a6a54f5-a28ebc85-915d-4dfe-a8e2-9588bee1f2dd.png)

#### Uploading Manually via the Dashboard

Once you have the .so files, you can upload them directly to the dashboard through **Upload NDK DSYMs** page found in the **Settings** menu of your [Luciq dashboard](https://dashboard.luciq.ai/dashboard). You'll only need to upload the file, while selecting the correct app version and app architecture.

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2FvnYVZLmmgWJkYOXnqO69%2Fimage.png?alt=media&#x26;token=3bfaae69-ce38-43b9-bd41-b440e03a393b" alt=""><figcaption></figcaption></figure>

#### Uploading via API

We have an API endpoint that you can use to upload your symbol files directly from the console or from the CI.

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```
curl --location --request POST 'https://api.instabug.com/api/web/public/so_files' \
--form 'application_token="YOUR_APP_TOKEN"' \
--form 'api_key="API_KEY"' \
--form 'app_version="1.1"' \
--form 'arch="x86"' \
--form 'so_file=@"so-files.zip"'
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="success" %}
Please contact support to obtain your API Key
{% endhint %}
