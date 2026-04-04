# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-crash-reporting/symbolication-deobfuscation.md

# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/setup-crash-reporting/symbolication-deobfuscation.md

# Symbolication/Deobfuscation

### iOS Crash Reporting

**JavaScript Crashes**

**Uploading iOS Source Map Files**

You can follow these steps to generate iOS sourcemap files and upload them.

{% stepper %}
{% step %}
**Prepare**

Go to your project root directory.
{% endstep %}

{% step %}
**Generate sourcemap and bundle**

Run the following script for the **iOS** platform:

{% code title="Shell" %}

```sh
react-native bundle --platform ios \
  --entry-file index.js \
  --dev false \
  --bundle-output ./ios/main.jsbundle \
  --sourcemap-output ./ios-sourcemap.json &&
  zip ./ios-sourcemap.zip ./ios-sourcemap.json
```

{% endcode %}
{% endstep %}

{% step %}
**Upload**

Upload the generated file "ios-sourcemap.json" at your project’s root directory.
{% endstep %}
{% endstepper %}

#### Android Crash Reporting

**JavaScript Crashes**

**Uploading Android Source Map Files**

You can follow these steps to generate Android sourcemap files and upload them.

{% stepper %}
{% step %}
**Prepare**

Go to your project root directory.
{% endstep %}

{% step %}
**Generate sourcemap and bundle**

Run the following script for the **Android** platform:

{% code title="Shell" %}

```sh
react-native bundle --platform android \
  --entry-file index.js \
  --dev false \
  --bundle-output ./android/main.jsbundle \
  --sourcemap-output ./android-sourcemap.json &&
  zip ./android-sourcemap.zip ./android-sourcemap.json
```

{% endcode %}
{% endstep %}

{% step %}
**Upload**

Upload the generated file "android-sourcemap.json" at your project's root directory.
{% endstep %}
{% endstepper %}

**Uploading source maps via CLI**

You can upload JavaScript source map files from the command line using the Luciq CLI. Useful for CI or when you generate source maps outside the automatic build flow.

{% code title="Shell" %}

```sh
npx luciq upload-sourcemaps \
  --platform <ios|android> \
  --file <path-to-sourcemap.json> \
  --token YOUR_APP_TOKEN \
  --name VERSION_NAME \
  --code VERSION_CODE
```

{% endcode %}

Optional: `--label <value>` for CodePush (or other OTA) release labels. Options can be set via environment variables: `LUCIQ_APP_TOKEN`, `LUCIQ_APP_VERSION_NAME`, `LUCIQ_APP_VERSION_CODE`, `LUCIQ_APP_VERSION_LABEL`.

**Uploading Source Maps Automatically**

For your app crashes to show up with a fully symbolicated/deobfuscated stack trace, we will automatically generate the source map files and upload them to your dashboard on release build. To do so, we rely on your app token being explicitly added to `Luciq.init('YOUR_APP_TOKEN')` (iOS) or `Luciq.start('YOUR_APP_TOKEN')` (Android) in JavaScript.

**Environment variables**

You can control automatic source map upload and override defaults with these environment variables. Where supported, `INSTABUG_*` equivalents are accepted as a fallback (e.g. `INSTABUG_APP_TOKEN`, `INSTABUG_SOURCEMAPS_UPLOAD_DISABLE`).

| Variable                          | Platform     | Description                                                                                                               |
| --------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------- |
| `LUCIQ_APP_TOKEN`                 | iOS, Android | Your app token. Overrides the token inferred from JavaScript (e.g. when the token is a constant or differs per platform). |
| `LUCIQ_APP_VERSION_NAME`          | iOS          | Version name (e.g. `1.2.0`) used for upload. Defaults to `CFBundleShortVersionString` from Info.plist.                    |
| `LUCIQ_APP_VERSION_CODE`          | iOS          | Version code (e.g. `42`) used for upload. Defaults to `CFBundleVersion` from Info.plist.                                  |
| `LUCIQ_VERSION_NAME`              | Android      | Version name used for upload. Defaults to `versionName` from your app's `build.gradle`.                                   |
| `LUCIQ_VERSION_CODE`              | Android      | Version code used for upload. Defaults to `versionCode` from your app's `build.gradle`.                                   |
| `LUCIQ_SOURCEMAPS_UPLOAD_DISABLE` | iOS, Android | Set to `true` to disable automatic source map upload on release builds.                                                   |

**iOS:** Set variables in your Xcode Run Script phase, in `ios/.xcode.env`, or in `ios/.xcode.env.local` (recommended for secrets).\
**Android:** Set variables in your shell or CI before running the build (e.g. `export LUCIQ_APP_TOKEN=...`).

**Expo and EAS Update**

If you use **Expo** or **EAS Update**, you must install the Luciq Expo config plugin from the **`@luciq/react-native`** package. Add the plugin to your `app.json`

```json
"plugins": [
"@luciq/react-native"
]
```

\
The plugin can **upload source maps automatically** on release builds (iOS and Android). and it will add the upload build phase and patch the bundle phase so source maps are generated and uploaded.

* **EAS Update builds** — After you run an EAS Update build, the JavaScript bundle and source maps are written to your update output folder (e.g. `dist`). To upload those source maps to Luciq, use the EAS Updates upload command from your project root:

{% code title="Shell" %}

```sh
npx luciq upload-eas-updates-sourcemaps \
  -f <path-to-eas-update-output> \
  -t YOUR_APP_TOKEN \
  -n VERSION_NAME \
  -c VERSION_CODE
```

{% endcode %}

Pass `--iosUpdateId` and `--androidUpdateId` (from EAS Update) so crash reports match the correct update. You can run this in a CI step after `eas update` or manually.

* **Expo prebuild / development builds** — With the Luciq Expo config plugin, the iOS source map upload build phase and bundle phase are configured so source maps are generated and uploaded automatically on release builds.

**Uploading Files via API**

You can also upload dSYMs, mapping files, and source map files directly via API. Files must be uploaded one by one:

* dSYMs: .zip
* Mapping files: .txt
* Source map files: .json

Request format:

{% code title="API For Ios" %}

```bash
curl -X POST "https://api.instabug.com/api/sdk/v3/symbols_files" \
  -F "symbols_file=@/path/to/your/symbols_file" \
  -F "platform=react_native" \
  -F "os=ios" \
  -F "application_token=YOUR_APPLICATION_TOKEN" \
  -F 'app_version={"code":"APP_VERSION_CODE","name":"APP_VERSION_NAME"}'
```

{% endcode %}

{% code title="API for Android" %}

```sh
url -X POST "https://api.instabug.com/api/sdk/v3/symbols_files" \
  -F "symbols_file=@/path/to/your/symbols_file" \
  -F "platform=react_native" \
  -F "os=Android" \
  -F "application_token=YOUR_APPLICATION_TOKEN" \
  -F 'app_version={"code":"APP_VERSION_CODE","name":"APP_VERSION_NAME"}'
```

{% endcode %}

{% code overflow="wrap" %}

```python
curl -X POST "https://api.instabug.com/api/sdk/v3/symbols_files" \
  -F "symbols_file=@/path/to/your/file.zip" \
  -F "platform=react_native" \
  -F "os=ios" \
  -F "application_token=YOUR_APP_TOKEN" \
  -F 'app_version={"code":"APP_VERSION_CODE","name":"APP_VERSION_NAME"}'
```

{% endcode %}

***

#### Native SDKs (iOS and Android)

For **native** crashes (iOS and Android), symbolication and deobfuscation use platform-specific artifacts. What you can do:

* **iOS native crashes** — For symbolicating native iOS crashes (uploading dSYMs, Xcode build phase, Fastlane, or API), follow the [Symbolication](https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-crash-reporting/symbolication) guide for the native iOS SDK.
* **Android native crashes** — For deobfuscating Java/Kotlin and NDK crashes (mapping files, .so files, Gradle plugin, scripts, or API), follow the [Deobfuscation for Android](https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-crash-reporting/deobfuscation-for-android) guide for the native Android SDK.

  For **NDK (native C/C++) crash** symbolication, upload **.so** files (one .zip per architecture) using the CLI:

{% code title="Shell" %}

```sh
npx @luciq/react-native upload-so-files \
  --arch <x86|x86_64|arm64-v8a|armeabi-v7a> \
  --file <path-to-so-files.zip> \
  --api_key YOUR_APP_KEY \
  --token YOUR_APP_TOKEN \
  --name VERSION_NAME
```

{% endcode %}

The file must be a **.zip** containing the .so files for the given `--arch`. You can set `LUCIQ_APP_TOKEN` and `LUCIQ_APP_VERSION_NAME` via environment variables instead of `--token` and `--name`.

Updated 1 days ago

<details>

<summary>What’s Next</summary>

After a crash has been symbolicated/deobfuscated and the fix is done, reach out to your affected users and let them know to update.

* [Reply to Affected Users](https://docs.luciq.ai/react-native/setup-luciq-for-react-native/setup-crash-reporting/broken-reference)

</details>
