# Source: https://docs.instabug.com/ios/ios-luciq-migration.md

# iOS Luciq Migration

### Overview

This guide helps you migrate your iOS project from the Instabug SDK to the Luciq SDK. This change is part of a company-wide rebranding initiative. You can perform the migration manually by following the step-by-step instructions or use our automated migration script for a faster transition.

### Prerequisites

Before starting the migration process, ensure your project meets the following requirements and take the necessary precautions.

#### Supported Instabug Versions

This migration guide supports projects currently using:

* **Instabug SDK (Manual & Automated):** 16.x.x and above
* **Target Luciq SDK:** 18.0.0

#### Pre-Migration Checklist

**🔒 Backup Your Project**

\[ ] Commit all changes to your version control system (e.g., Git).\
\[ ] Create a dedicated backup branch to allow for a clean rollback if needed.\
\[ ] Build and run your project to confirm it's in a stable, working state before you begin.

{% hint style="info" %}
**Tip:** Assess your project's complexity using our Migration Complexity Assessment to choose the best approach for you
{% endhint %}

**🔍 Project Assessment**

\[ ] Identify how the Instabug SDK is integrated (CocoaPods, Swift Package Manager, or Manual).\
\[ ] Check for an Instabug.plist file if you use an on-premise or dedicated cloud setup.\
\[ ] Note any custom build scripts that might reference Instabug paths or symbols.

**⚙️ Environment Preparation**

\[ ] Ensure your project builds successfully without any existing errors.\
\[ ] Clean the build folder in Xcode (Product > Clean Build Folder or Cmd + Shift + K).\
\[ ] Run pod install or swift package resolve to ensure all dependencies are correctly synced.shel

***

### Migration Complexity Assistant

| Project Type                     | Complexity     | Recommended Approach                        | Estimated Time |
| -------------------------------- | -------------- | ------------------------------------------- | -------------- |
| Single-target, standard setup    | 🟢 **Simple**  | Automated script                            | 15-30 minutes  |
| Multi-target, standard config    | 🟡 **Medium**  | Automated script + manual review            | 1-2 hours      |
| Complex setup, on-premise config | 🔴 **Complex** | Manual migration or script + careful review | 2-4 hours      |

***

### When to Use Manual vs. Automated Migration

**✅ Use Automated Migration When:**

* You have a standard Instabug setup with minimal customization.
* You are using a supported Instabug version.
* Your project doesn't have complex custom build scripts that reference Instabug.
* You are comfortable using command-line tools and have created a backup.

⚠️ **Use Manual Migration When:**

* You have a heavily customized Instabug implementation.
* You are using an older, unsupported version of the Instabug SDK.
* Your project has complex build logic or dependencies that the script might not handle.
* You prefer granular control over every step of the migration process.

***

### Step-by-Step Manual Migration

#### Step 1: Migrate Your Dependency

{% hint style="info" %}

### **Quick Option**&#x20;

This step can be automated using our migration script. Continue reading for manual instructions.
{% endhint %}

Update the SDK dependency in your project's configuration based on your dependency manager.

#### For CocoaPods Users

In your `Podfile`, change `pod 'Instabug'` to `pod 'Luciq'`.

**Before:**

{% code title="Shell" %}

```shellscript
pod 'Instabug'
```

{% endcode %}

**After:**

{% code title="Shell" %}

```shellscript
pod 'Luciq'
```

{% endcode %}

Then, run `pod install` in your terminal.

**For Swift Package Manager (SPM) Users**

1. In Xcode, navigate to your project's **Package Dependencies** tab.
2. Select the "InstabugSDK" package and click the minus (`-`) button to remove it.
3. Click the plus (`+`) button, and in the search bar, enter the new repository URL: `https://github.com/luciqai/luciq-ios-sdk`.
4. Follow the prompts to add the new `LuciqSDK` package.

#### For Carthage Users

In your Cartfile, change the Instabug dependency to point to the new Luciq repository.

**Before:**

{% code title="Shell" overflow="wrap" %}

```shellscript
binary "https://raw.githubusercontent.com/Instabug/Instabug-iOS/master/Instabug.json"
```

{% endcode %}

**After:**

{% code title="Shell" overflow="wrap" %}

```shellscript
binary "https://raw.githubusercontent.com/luciqai/luciq-ios-sdk/main/Luciq.json"
```

{% endcode %}

Then, run the following command in your terminal:

{% code title="Shell" overflow="wrap" %}

```shellscript
carthage update
```

{% endcode %}

Finally, remove `InstabugSDK.xcframework` from your project in Xcode and drag the newly built `LuciqSDK.xcframework` from the `Carthage/Build` folder into your target's "Frameworks, Libraries, and Embedded Content" section.

**For Manual Installations**

1. Locate and remove `InstabugSDK.xcframework` from your project navigator and target's "Frameworks, Libraries, and Embedded Content" section.
2. Download and add the new `LuciqSDK.xcframework` to your project.

#### Step 2: Migrate On-Premise Configuration File (Enterprise Only)

⚠️ **Important**: This step is only for enterprise customers using a custom Instabug.plist file for on-premise setups. If you do not use this file, you can safely skip this step.

The SDK now looks for a `LuciqConfig.plist` file. You must rename your existing file and update the keys within it.

1. Rename the File\
   In your Xcode project, find Instabug.plist and rename it to LuciqConfig.plist.
2. Update the Keys\
   Open LuciqConfig.plist and update the keys according to the table below. The URL values should remain unchanged.

| Old Key                 | New Key                |
| ----------------------- | ---------------------- |
| `InstabugURL`           | `SDKBaseURL`           |
| `InstabugAPMURL`        | `APMBaseURL`           |
| `InstabugMonitoringURL` | `SDKMonitoringBaseURL` |

**Example** `Before` (`Instabug.plist`):

{% code title="XML" overflow="wrap" %}

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>InstabugURL</key>
	<string>https://your-on-prem-sdk.com/api/sdk/v3</string>
</dict>
</plist>
```

{% endcode %}

**Example** `After` (`LuciqConfig.plist`):

{% code title="XML" overflow="wrap" %}

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>SDKBaseURL</key>
	<string>https://your-on-prem-sdk.com/api/sdk/v3</string>
</dict>
</plist>
```

{% endcode %}

#### Step 3: Migrate Your Source Code (Swift & Objective-C)

{% hint style="info" %}

### Quick Option

This step can be automated using our migration script. Continue reading for manual instructions.
{% endhint %}

Perform the following find-and-replace operations across your entire Xcode workspace.

1. **Update Import Statements**

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
// Before
import InstabugSDK

// After
import LuciqSDK
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
// Before
#import <InstabugSDK/InstabugSDK.h> 

// After
#import <LuciqSDK/LuciqSDK.h>
```

{% endcode %}
{% endtab %}
{% endtabs %}

2. Update code symbols\
   Perform these case-sensitive "Find and Replace in Workspace" operations:

* Main Class Name: Find `Instabug` and replace with `Luciq`.
* Symbol Prefix: Find `IBG` and replace with `LCQ`.
* Note: In Swift, most type names that were prefixed with `IBG` now have the prefix removed (e.g., `IBGReport` becomes `Report`). The script handles this, but for manual migration, refer to the full mapping table.

**Code Snippet Example (Swift):**

**Before:**

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
import InstabugSDK

// ...
Instabug.start(withToken: "YOUR_APP_TOKEN", invocationEvents: .shake)
BugReporting.setCommentMinimumCharacterCount(10, forBugReportType: .bug)
```

{% endcode %}
{% endtab %}
{% endtabs %}

**After:**

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
import InstabugSDK

// ...
Instabug.start(withToken: "YOUR_APP_TOKEN", invocationEvents: .shake)
BugReporting.setCommentMinimumCharacterCount(10, forBugReportType: .bug)
```

{% endcode %}
{% endtab %}
{% endtabs %}

***

### Automated Migration Script

#### Introduction

To simplify the migration, our `migrate-luciq.sh` script automates the entire process. The script performs a comprehensive find-and-replace operation, handling:

* **Source Code:** Replaces `Instabug` and `IBG` symbols in all `.swift`, `.m`, and `.h` files.
* **Configuration File:** Renames `Instabug.plist` to `LuciqConfig.plist` and updates all keys within it.
* **Xcode Project File:** Updates the `.pbxproj` file to reflect the renamed `.plist`, ensuring Xcode finds the new file reference.

#### Where to find it?

You can find the migration script in Luciq's [public GitHub repository here.](https://github.com/luciqai/luciq-ios-sdk/releases/download/18.0.0/migrate-luciq.sh)

#### Step-by-Step Usage Guide

1. Make the Script Executable\
   Open Terminal, navigate to where you saved the script, and run:\
   `chmod +x migrate-luciq.sh`
2. Run the Migration\
   ⚠️ Warning: This script modifies your files directly and the changes are irreversible. Please ensure you have committed all your work to version control and created a backup branch before proceeding, as recommended in the Pre-Migration Checklist.\
   Once you are ready, execute the script on your project's root directory:\
   `./migrate-luciq.sh /path/to/your/project`\
   You will be prompted for a final confirmation before the script begins modifying your files. Type y to proceed.
3. Verify the Migration\
   After the script finishes, it is crucial to verify the results:
   * Open your project in Xcode.
   * Clean the build folder (**Product > Clean Build Folder**).
   * Build the project (**Product > Build** or `Cmd + B`) to check for any compilation errors.
   * Use your version control tool (e.g., `git diff`) to meticulously review all changes before committing them to your repository.

#### Safety Features

🛡️ Version Control Prerequisite: The script should only be run on a project with a clean version control status. This is your primary safety net for reviewing and reverting changes.

🤔 User Confirmation: The script requires explicit user confirmation before modifying any files, giving you a final chance to cancel the operation.

#### System Requirements

* **macOS Environment:** The script relies on the `plutil` command-line tool, which is standard on macOS.
* **Bash Shell:** A standard Bash-compatible shell is required to execute the script.

### SwiftUI Integrator Migration

If your project uses our command-line tool to automatically instrument SwiftUI views, you'll need to update your build process. The `InstabugSwiftUIIntegrator` has been renamed to `LuciqSwiftUIIntegrator` as part of the rebranding.

#### What is the SwiftUI Integrator?

The `LuciqSwiftUIIntegrator` is a powerful command-line tool that automatically adds instrumentation to your SwiftUI code during the build process. It observes UI element states and user interactions (like taps and navigation) to enhance user experience monitoring and debugging. Importantly, all changes are reverted after the build, so your source code remains untouched.

#### How to Migrate?

Before you begin, it is essential that your project's codebase has been fully migrated from Instabug to Luciq. This can be accomplished either by using the automated migration script or by following the manual migration steps outlined previously. The `LuciqSwiftUIIntegrator` is designed to work on an already-migrated project and depends on the updated symbols and imports to function correctly.

1. **Clean Up Old Instrumentation Files (Recommended)**\
   Before running the new integrator, delete the old instrumentation cache folder named `InstabugInstrumentation` from your project's root directory. The new `LuciqSwiftUIIntegrator` will automatically create a new folder named `LuciqInstrumentation` on its first run. This step prevents retaining outdated files.
2. **Download the New Integrator**\
   You can download the new `LuciqSwiftUIIntegrator` from our [public GitHub repository: Here](https://github.com/luciqai/luciq-ios-sdk/releases/download/18.0.0/LuciqSwiftUIIntegrator.zip)
3. Update Your Build Phase Script\
   In Xcode, go to your target's **Build Phases** and locate the pre-build script that runs the integrator. You only need to change the name of the executable.

**Before:**

{% code title="Shell" %}

```shellscript
# Pre-build phase in Xcode
/path/to/InstabugSwiftUIIntegrator instrument --directory "${SRCROOT}"`
```

{% endcode %}

**After:**

{% code title="Shell" %}

```shellscript
# Pre-build phase in Xcode
/path/to/LuciqSwiftUIIntegrator instrument --directory "${SRCROOT}"
```

{% endcode %}

After updating the script, your SwiftUI instrumentation will work seamlessly with the new `LuciqSDK`.

### Fastlane Plugin Migration

If your project uses the `fastlane-plugin-instabug_official` plugin to upload dSYM files, you'll need to update your configuration to use the new `fastlane-plugin-luciq_dsym_upload` plugin. This plugin is responsible for uploading symbolication files to Luciq.

#### How to Migrate?

Follow these steps to update your Fastlane configuration.

**Step 1: Update Your Plugin**

First, remove the old plugin and add the new one.

1. **Remove the old plugin** by running this command in your terminal:\
   `fastlane remove_plugin instabug_official`
2. **Add the new plugin** by running this command:\
   `fastlane add_plugin luciq_dsym_upload`\
   \&#xNAN;*Alternatively*, if you manage plugins using a `Pluginfile`, update it:\
   Before:\
   `gem 'fastlane-plugin-instabug_official'`\
   After:\
   `gem 'fastlane-plugin-luciq_dsym_upload'`\
   Then run bundle install.

**Step 2: Update Your Fastfile**

In your `Fastfile`, rename the action from `instabug_official` to `luciq_dsym_upload`. The available parameters (`api_token`, `dsym_array_paths`, `eu`, `end_point`) remain the same.

* **Environment Variable:** If you were providing your API token via the environment variable `FL_INSTABUG_API_TOKEN`, you must rename it to `FL_LUCIQ_API_TOKEN`.

{% hint style="warning" %}
**Important:** If you were using the end\_point parameter to point to a custom Instabug URL, you **must** update it to point to your new Luciq endpoint.
{% endhint %}

**Example** `Fastfile` **Lane (Before):**

```
lane :upload_symbols do
  instabug_official(
    api_token: "<Your Token>",
    dsym_array_paths: ["./App1.dSYM.zip", "./App2.dSYM.zip"]
  )
end
```

**Example `Fastfile` Lane (After):**

```
lane :upload_symbols do
  luciq_dsym_upload(
    api_token: "<Your Token>",
    dsym_array_paths: ["./App1.dSYM.zip", "./App2.dSYM.zip"]
  )
end
```

### FAQ

#### Automated Script & File System

1. **What specific files does the`migrate-luciq.sh` script modify? ⚙️**\
   The script is designed to perform a comprehensive search and replace operation. It will modify:
   * **Source Code Files:** Any file with a `.swift`, `.m`, or `.h` extension within the provided project path.
   * **Configuration File:** It will rename `Instabug.plist` to `LuciqConfig.plist`.
   * **Plist Contents:** It will use the plutil command to replace the old keys (e.g., `InstabugURL`) with the new keys (e.g., `SDKBaseURL`) inside the newly renamed `LuciqConfig.plist`.
   * **Xcode Project File:** It will modify the `.pbxproj` file to update the file reference from `Instabug.plist` to `LuciqConfig.plist`, ensuring Xcode can find the file after it's renamed.
2. **I ran the script, but it failed or my project has errors. What are the technical debugging steps? 🔧**\
   If you encounter issues after running the script:
   * **Do Not Commit:** First, do not commit the changes.
   * **Review the Diff:** Use `git diff` to see every single change the script made. This is the most effective way to spot incorrect replacements or unintended modifications, especially in your `.pbxproj` file.
   * **Check Script Permissions:** Ensure the script was made executable with `chmod +x migrate-luciq.sh`.
   * **Revert and Go Manual:** If the diff is too noisy or the errors are complex, the safest option is to revert all changes (`git checkout .` or `git stash`) and perform the migration manually. The script is a powerful tool, but manual migration gives you granular control.

#### Code & Symbol Migration

3. **What is the most common pitfall when migrating Swift code symbols? 🐛**\
   The most common mistake is overlooking the **prefix** removal rule for Swift types. While the main class becomes `Luciq` and the symbol prefix changes from `IBG` to `LCQ` in Objective-C, in **Swift**, most class/struct/enum names that were prefixed with `IBG` now have the prefix **removed entirely**.
   * Incorrect: let `myReport` = `LCQReport()`
   * Correct: let `myReport` = `Report()`\
     Similarly, `IBGSurvey` becomes `Survey`, and `IBGInvocationEvent` becomes `InvocationEvent`. Always refer to the "**New Name (Swift)**" column in the Complete Symbol Mapping table.
4. **Are there any symbols that don't follow the standard renaming rules? ⚠️**\
   Yes. A few symbols are exceptions to the general find-and-replace rules. These are highlighted in the mapping table. For example:
   * **Enum**: `IBGReportType` is renamed to `LCQReportCategory` in Objective-C and `ReportCategory` in Swift. This is a semantic change, not just a prefix swap.
   * **Enum**: `IBGActionType` becomes `LCQConsentAction` / `ConsentAction`.
   * **Properties**: Some properties like `instabugLogs` were renamed to `luciqLogs` without following the `IBGprefix` convention.\
     Carefully review the highlighted items in the Complete Symbol Mapping table for these specific cases.
5. **I'm getting "'file not found'" errors in Objective-C after updating my imports. What should I check?📄**\
   This typically happens if you were importing specific sub-headers instead of the main SDK header. The script may not catch all permutations. You must ensure every #import statement is updated according to the **Complete Mapping of Public Header Imports** table.
   * Example: `import <InstabugSDK/IBGReport.h>` must be changed to `import <LuciqSDK/LCQReport.h`>.
   * Best Practice: After running `pod install` for the new `Luciq` pod, perform a global search in your workspace for `#import <InstabugSDK>` to find any headers that were missed.

#### Build Process & Configuration

6. **I renamed Instabug.plist, but my on-premise configuration isn't being loaded. What did I miss? 🔌**\
   Renaming the file is only the first of two required steps. You must also **update the keys within the file itself.** The SDK no longer looks for `InstabugURL` or `InstabugAPMURL`. You need to open `LuciqConfig.plist` and change the keys to `SDKBaseURL`, `APMBaseURL`, etc., as specified in the guide. The URL values should remain the same.
7. **In what order should I migrate my main app code versus the SwiftUI Integrator? ➡️**\
   You **must** migrate your application's source code first.
   1. Run the automated script or perform the manual migration on your codebase.
   2. Ensure the project builds successfully with the `LuciqSDK`.
   3. Only then should you go to your target's **Build Phases** and update the pre-build script to call `LuciqSwiftUIIntegrator`. The integrator depends on the updated `LuciqSDK` symbols to function correctly.

#### Post-Migration Troubleshooting

8. **After manual migration, Xcode throws "Use of unresolved identifier" errors everywhere. What's the fastest way to fix this? ⚡**\
   This classic error has a few common causes after this migration:

   1. **Check Imports**: The most likely cause is a missed `import` statement. Ensure every relevant file has `import LuciqSDK` (for Swift) or `#import <LuciqSDK/LuciqSDK.h>` (for Objective-C).
   2. **Clean Build Folder**: Xcode's index might be stale. Use **Product > Clean Build Folder** (Cmd + Shift + K) to force Xcode to re-index the project with the new SDK.
   3. **Verify Dependency**: Ensure you've correctly removed the old SDK and added the new one in CocoaPods or SPM, and have run `pod install` or resolved Swift packages.
   4. **Check Swift Prefix Removal**: As mentioned in question #3, double-check that you've removed the `IBGprefix` from Swift types (e.g., use `Report` instead of `IBGReport`).\\<br>

   #### Reference: Complete Symbol Mapping

   The following tables provide a one-to-one mapping of every public symbol. The general rules are:

   * The `Instabug` class becomes `Luciq`.
   * Any symbol prefixed with `IBG` is now prefixed with `LCQ` in Objective-C.
   * In Swift, most types prefixed with `IBG` now have the prefix removed (e.g. `IBGReport` → `Report`).

| Symbol Type                         | Old Name                            | New Name (ObjC)                     | New Name (Swift)                             |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | -------------------------------------------- |
| Class                               | Instabug                            | Luciq                               | Luciq                                        |
| Class                               | IBGReport                           | LCQReport                           | Report                                       |
| Property (in IBGReport)             | instabugLogs                        | luciqLogs                           | luciqLogs                                    |
| Class                               | IBGTheme                            | LCQTheme                            | Theme (No Change)                            |
| Class                               | IBGUserStep                         | LCQUserStep                         | UserStep (No Change)                         |
| Class                               | IBGFeatureFlag                      | LCQFeatureFlag                      | FeatureFlag (No Change)                      |
| Class                               | IBGAPM                              | LCQAPM                              | APM (No Change)                              |
| Class                               | IBGExecutionTrace                   | LCQExecutionTrace                   | ExecutionTrace (No Change)                   |
| Class                               | IBGNetworkTrace                     | LCQNetworkTrace                     | NetworkTrace (No Change)                     |
| Class                               | IBGBugReporting                     | LCQBugReporting                     | BugReporting (No Change)                     |
| Class                               | IBGProactiveReportingConfigurations | LCQProactiveReportingConfigurations | ProactiveReportingConfigurations (No Change) |
| Class                               | IBGCrashReporting                   | LCQCrashReporting                   | CrashReporting (No Change)                   |
| Class                               | IBGCrashMetaData                    | LCQCrashMetaData                    | CrashMetaData (No Change)                    |
| Class                               | IBGCrashReporterState               | LCQCrashReporterState               | CrashReporterState (No Change)               |
| Property (in IBGCrashReporterState) | instabugHandlers                    | luciqHandlers                       | luciqHandlers                                |
| Property (in IBGCrashReporterState) | isInstabugCrashReporterActive       | isLuciqCrashReporterActive          | isLuciqCrashReporterActive                   |
| Class                               | IBGCrashHandlersInfo                | LCQCrashHandlersInfo                | CrashHandlersInfo (No Change)                |
| Class                               | IBGFunctionInfo                     | LCQFunctionInfo                     | FunctionInfo (No Change)                     |
| Class                               | IBGNonFatalError                    | LCQNonFatalError                    | NonFatalError (No Change)                    |
| Class                               | IBGNonFatalException                | LCQNonFatalException                | NonFatalException (No Change)                |
| Protocol                            | IBGNonFatalBuilder                  | LCQNonFatalBuilder                  | NonFatalBuilder (No Change)                  |
| Class                               | IBGFeatureRequests                  | LCQFeatureRequests                  | FeatureRequests (No Change)                  |
| Class                               | IBGLog                              | LCQLog                              | LCQLog                                       |
| Class                               | IBGNetworkLogger                    | LCQNetworkLogger                    | NetworkLogger (No Change)                    |
| Class                               | IBGReplies                          | LCQReplies                          | Replies (No Change)                          |
| Class                               | IBGSessionReplay                    | LCQSessionReplay                    | SessionReplay (No Change)                    |
| Property (in IBGSessionReplay)      | IBGLogsEnabled                      | LCQLogsEnabled                      | lcqLogsEnabled                               |
| Class                               | IBGSessionMetadata                  | LCQSessionMetadata                  | SessionMetadata (No Change)                  |
| Class                               | IBGSessionMetadataNetworkLogs       | LCQSessionMetadataNetworkLogs       | SessionMetadataNetworkLogs (No Change)       |
| Class                               | IBGSurveys                          | LCQSurveys                          | Surveys (No Change)                          |
| Class                               | IBGSurvey                           | LCQSurvey                           | Survey                                       |
| Category Property                   | UIView\.instabug\_privateView       | UIView\.luciq\_privateView          | UIView\.luciq\_privateView                   |
| C Struct                            | ibgcrash\_async\_file\_t            | lcqcrash\_async\_file\_t            | lcqcrash\_async\_file\_t                     |
| C Struct                            | IBGCrashReportWriterContext         | LCQCrashReportWriterContext         | CrashReportWriterContext                     |
| C Struct                            | IBGCrashReportWriter                | LCQCrashReportWriter                | CrashReportWriter                            |
| Global Function                     | InstabugLog(...)                    | LuciqLog(...)                       | LuciqLog(...)                                |
| Global Function                     | IBGLogVerbose(...)                  | LCQLogVerbose(...)                  | LCQLogVerbose(...)                           |
| Global Function                     | IBGLogDebug(...)                    | LCQLogDebug(...)                    | LCQLogDebug(...)                             |
| Global Function                     | IBGLogInfo(...)                     | LCQLogInfo(...)                     | LCQLogInfo(...)                              |
| Global Function                     | IBGLogWarn(...)                     | LCQLogWarn(...)                     | LCQLogWarn(...)                              |
| Global Function                     | IBGLogError(...)                    | LCQLogError(...)                    | LCQLogError(...)                             |
| Global Function                     | IBGNSLog(...)                       | LCQNSLog(...)                       | LCQNSLog(...)                                |
| Global Function                     | IBGNSLogWithLevel(...)              | LCQNSLogWithLevel(...)              | LCQNSLogWithLevel(...)                       |
| Enum                                | IBGInvocationEvent                  | LCQInvocationEvent                  | InvocationEvent                              |
| Enum                                | IBGAutoMaskScreenshotOption         | LCQAutoMaskScreenshotOption         | AutoMaskScreenshotOption                     |
| Enum                                | IBGColorTheme                       | LCQColorTheme                       | ColorTheme                                   |
| Enum                                | IBGInvocationMode                   | LCQInvocationMode                   | InvocationMode                               |
| Enum                                | IBGBugReportingReportType           | LCQBugReportingReportType           | BugReportingReportType                       |
| Enum                                | IBGBugReportingType                 | LCQBugReportingType                 | BugReportingType (No Change)                 |
| Enum                                | IBGBugReportingOption               | LCQBugReportingOption               | BugReportingOption                           |
| Enum                                | IBGReportType                       | LCQReportCategory                   | ReportCategory                               |
| Enum                                | IBGActionType                       | LCQConsentAction                    | ConsentAction                                |
| Enum                                | IBGDismissType                      | LCQDismissType                      | SDKDismissType                               |
| Enum                                | IBGLocale                           | LCQLocale                           | SDKLocale                                    |
| Enum                                | IBGPromptOption                     | LCQPromptOption                     | PromptOption                                 |
| Enum                                | IBGPosition                         | LCQPosition                         | SDKPosition                                  |
| Enum                                | IBGLogLevel                         | LCQLogLevel                         | SDKLogLevel                                  |
| Enum                                | IBGSDKDebugLogsLevel                | LCQSDKDebugLogsLevel                | SDKDebugLogsLevel                            |
| Enum                                | IBGUserStepsMode                    | LCQUserStepsMode                    | UserStepsMode                                |
| Enum                                | IBGAttachmentType                   | LCQAttachmentType                   | AttachmentType                               |
| Enum                                | IBGExtendedBugReportMode            | LCQExtendedBugReportMode            | ExtendedBugReportMode                        |
| Enum                                | IBGAction                           | LCQAction                           | SDKAction                                    |
| Enum                                | IBGWelcomeMessageMode               | LCQWelcomeMessageMode               | WelcomeMessageMode                           |
| Enum                                | IBGPlatform                         | LCQPlatform                         | SDKPlatform                                  |
| Enum                                | IBGUIEventType                      | LCQUIEventType                      | UserInteractionEventType                     |
| Enum                                | IBGInteractionViewType              | LCQInteractionViewType              | InteractionViewType                          |
| Enum                                | IBGIssueType                        | LCQIssueType                        | ReportableIssueType                          |
| Enum                                | IBGCrashType                        | LCQCrashType                        | CrashType                                    |
| Enum                                | IBGCrashReportConsent               | LCQCrashReportConsent               | CrashReportConsent                           |
| Enum                                | IBGOverAirType                      | LCQOverAirType                      | OverAirType                                  |
| Enum                                | IBGSurveyFinishedState              | LCQSurveyFinishedState              | SurveyFinishedState                          |
| Enum                                | IBGNonFatalLevel                    | LCQNonFatalLevel                    | NonFatalLevel (No Change)                    |
| Enum                                | IBGNonFatalStackTraceMode           | LCQNonFatalStackTraceMode           | NonFatalStackTraceMode (No Change)           |
| Type Alias                          | IBGCrashReportConsentReplyHandler   | LCQCrashReportConsentReplyHandler   | LCQCrashReportConsentReplyHandler            |

#### Complete Mapping of Public Header Imports

When migrating your Objective-C files, users may need to update any `#import` statements that reference specific headers from the old SDK.

| Old Header Import                                             | New Header Import                                          |
| ------------------------------------------------------------- | ---------------------------------------------------------- |
| `#import <InstabugSDK/InstabugSDK.h>`                         | `#import <LuciqSDK/LuciqSDK.h>`                            |
| `#import <InstabugSDK/Instabug.h>`                            | `#import <LuciqSDK/Luciq.h>`                               |
| `#import <InstabugSDK/IBGAPM.h>`                              | `#import <LuciqSDK/LCQAPM.h>`                              |
| `#import <InstabugSDK/IBGBugReporting.h>`                     | `#import <LuciqSDK/LCQBugReporting.h>`                     |
| `#import <InstabugSDK/IBGCrashAsyncFile.h>`                   | `#import <LuciqSDK/LCQCrashAsyncFile.h>`                   |
| `#import <InstabugSDK/IBGCrashHandlersInfo.h>`                | `#import <LuciqSDK/LCQCrashHandlersInfo.h>`                |
| `#import <InstabugSDK/IBGCrashMetaData.h>`                    | `#import <LuciqSDK/LCQCrashMetaData.h>`                    |
| `#import <InstabugSDK/IBGCrashReporterState.h>`               | `#import <LuciqSDK/LCQCrashReporterState.h>`               |
| `#import <InstabugSDK/IBGCrashReporting.h>`                   | `#import <LuciqSDK/LCQCrashReporting.h>`                   |
| `#import <InstabugSDK/IBGCrashReportWriter.h>`                | `#import <LuciqSDK/LCQCrashReportWriter.h>`                |
| `#import <InstabugSDK/IBGFeatureFlag.h>`                      | `#import <LuciqSDK/LCQFeatureFlag.h>`                      |
| `#import <InstabugSDK/IBGFeatureRequests.h>`                  | `#import <LuciqSDK/LCQFeatureRequests.h>`                  |
| `#import <InstabugSDK/IBGFunctionInfo.h>`                     | `#import <LuciqSDK/LCQFunctionInfo.h>`                     |
| `#import <InstabugSDK/IBGLog.h>`                              | `#import <LuciqSDK/LCQLog.h>`                              |
| `#import <InstabugSDK/IBGNetworkLogger.h>`                    | `#import <LuciqSDK/LCQNetworkLogger.h>`                    |
| `#import <InstabugSDK/IBGNetworkTrace.h>`                     | `#import <LuciqSDK/LCQNetworkTrace.h>`                     |
| `#import <InstabugSDK/IBGNonFatal.h>`                         | `#import <LuciqSDK/LCQNonFatal.h>`                         |
| `#import <InstabugSDK/IBGProactiveReportingConfigurations.h>` | `#import <LuciqSDK/LCQProactiveReportingConfigurations.h>` |
| `#import <InstabugSDK/IBGReplies.h>`                          | `#import <LuciqSDK/LCQReplies.h>`                          |
| `#import <InstabugSDK/IBGReport.h>`                           | `#import <LuciqSDK/LCQReport.h>`                           |
| `#import <InstabugSDK/IBGSessionMetadata.h>`                  | `#import <LuciqSDK/LCQSessionMetadata.h>`                  |
| `#import <InstabugSDK/IBGSessionReplay.h>`                    | `#import <LuciqSDK/LCQSessionReplay.h>`                    |
| `#import <InstabugSDK/IBGSurvey.h>`                           | `#import <LuciqSDK/LCQSurvey.h>`                           |
| `#import <InstabugSDK/IBGSurveyFinishedState.h>`              | `#import <LuciqSDK/LCQSurveyFinishedState.h>`              |
| `#import <InstabugSDK/IBGSurveys.h>`                          | `#import <LuciqSDK/LCQSurveys.h>`                          |
| `#import <InstabugSDK/IBGTheme.h>`                            | `#import <LuciqSDK/LCQTheme.h>`                            |
| `#import <InstabugSDK/IBGTypes.h>`                            | `#import <LuciqSDK/LCQTypes.h>`                            |
| `#import <InstabugSDK/IBGUserStep.h>`                         | `#import <LuciqSDK/LCQUserStep.h>`                         |
| `#import <InstabugSDK/UIView+Instabug.h>`                     | `#import <LuciqSDK/UIView+Luciq.h>`                        |

#### SwiftUI Interface Migration

The following table outlines the renaming for our public SwiftUI views and view modifiers. The `instabug` prefix has been replaced with `luciq`.

| Symbol Type   | Old Swift Name              | New Swift Name           |
| ------------- | --------------------------- | ------------------------ |
| View Modifier | `instabug_privateView()`    | `luciq_privateView()`    |
| View          | `InstabugPrivateView`       | `LuciqPrivateView`       |
| View Modifier | `instabugTracedView(name:)` | `luciqTracedView(name:)` |
| View          | `InstabugTracedView`        | `LuciqTracedView`        |

#### Complete Mapping of Localization String Constants (LCQTypes.h)

Predefined keys to be used to override any of the user-facing strings in the SDK. See + \[Luciq setValue:forStringWithKey]

| Old Constant Name (Instabug SDK)                                | New Constant Name (Luciq SDK)                                   |
| --------------------------------------------------------------- | --------------------------------------------------------------- |
| `kIBGStartAlertTextStringName`                                  | `kLCQStartAlertTextStringName`                                  |
| `kIBGShakeStartAlertTextStringName`                             | `kLCQShakeStartAlertTextStringName`                             |
| `kIBGTwoFingerSwipeStartAlertTextStringName`                    | `kLCQTwoFingerSwipeStartAlertTextStringName`                    |
| `kIBGEdgeSwipeStartAlertTextStringName`                         | `kLCQEdgeSwipeStartAlertTextStringName`                         |
| `kIBGScreenshotStartAlertTextStringName`                        | `kLCQScreenshotStartAlertTextStringName`                        |
| `kIBGFloatingButtonStartAlertTextStringName`                    | `kLCQFloatingButtonStartAlertTextStringName`                    |
| `kIBGBetaWelcomeMessageWelcomeStepTitle`                        | `kLCQBetaWelcomeMessageWelcomeStepTitle`                        |
| `kIBGBetaWelcomeMessageWelcomeStepContent`                      | `kLCQBetaWelcomeMessageWelcomeStepContent`                      |
| `kIBGBetaWelcomeMessageHowToReportStepTitle`                    | `kLCQBetaWelcomeMessageHowToReportStepTitle`                    |
| `kIBGBetaWelcomeMessageHowToReportStepContent`                  | `kLCQBetaWelcomeMessageHowToReportStepContent`                  |
| `kIBGBetaWelcomeMessageFinishStepTitle`                         | `kLCQBetaWelcomeMessageFinishStepTitle`                         |
| `kIBGBetaWelcomeMessageFinishStepContent`                       | `kLCQBetaWelcomeMessageFinishStepContent`                       |
| `kIBGBetaWelcomeDoneButtonTitle`                                | `kLCQBetaWelcomeDoneButtonTitle`                                |
| `kIBGLiveWelcomeMessageTitle`                                   | `kLCQLiveWelcomeMessageTitle`                                   |
| `kIBGLiveWelcomeMessageContent`                                 | `kLCQLiveWelcomeMessageContent`                                 |
| `kIBGInvalidEmailMessageStringName`                             | `kLCQInvalidEmailMessageStringName`                             |
| `kIBGInvalidEmailTitleStringName`                               | `kLCQInvalidEmailTitleStringName`                               |
| `kIBGInvalidNumberTitleStringName`                              | `kLCQInvalidNumberTitleStringName`                              |
| `kIBGReportCategoriesAccessibilityScrollStringName`             | `kLCQReportCategoriesAccessibilityScrollStringName`             |
| `kIBGAnnotationCloseButtonStringName`                           | `kLCQAnnotationCloseButtonStringName`                           |
| `kIBGAnnotationSaveButtonStringName`                            | `kLCQAnnotationSaveButtonStringName`                            |
| `kIBGAnnotationDrawnShapeStringName`                            | `kLCQAnnotationDrawnShapeStringName`                            |
| `kIBGAttachmentActionSheetStopScreenRecording`                  | `kLCQAttachmentActionSheetStopScreenRecording`                  |
| `kIBGAttachmentActionSheetUnmuteMic`                            | `kLCQAttachmentActionSheetUnmuteMic`                            |
| `kIBGAttachmentActionSheetMuteMic`                              | `kLCQAttachmentActionSheetMuteMic`                              |
| `kIBGScreenRecordingDuration`                                   | `kLCQScreenRecordingDuration`                                   |
| `kIBGInvalidNumberMessageStringName`                            | `kLCQInvalidNumberMessageStringName`                            |
| `kIBGCloseConversationsStringLabel`                             | `kLCQCloseConversationsStringLabel`                             |
| `kIBGBackToConversationsStringLabel`                            | `kLCQBackToConversationsStringLabel`                            |
| `kIBGSendMessageStringLabel`                                    | `kLCQSendMessageStringLabel`                                    |
| `kIBGDismissMessageStringLabel`                                 | `kLCQDismissMessageStringLabel`                                 |
| `kIBGReplyToMessageStringLabel`                                 | `kLCQReplyToMessageStringLabel`                                 |
| `kIBGInvocationTitleStringName`                                 | `kLCQInvocationTitleStringName`                                 |
| `kIBGInvocationTitleHintStringName`                             | `kLCQInvocationTitleHintStringName`                             |
| `kIBGChatsListHintStringName`                                   | `kLCQChatsListHintStringName`                                   |
| `kIBGOneChatsListHintStringName`                                | `kLCQOneChatsListHintStringName`                                |
| `kIBGCancelPromptHintStringName`                                | `kLCQCancelPromptHintStringName`                                |
| `kIBGReportCategoriesBackButtonStringName`                      | `kLCQReportCategoriesBackButtonStringName`                      |
| `kIBGReportCategoriesBackButtonHintStringName`                  | `kLCQReportCategoriesBackButtonHintStringName`                  |
| `kIBGAskAQuestionStringName`                                    | `kLCQAskAQuestionStringName`                                    |
| `kIBGFrustratingExperienceStringName`                           | `kLCQFrustratingExperienceStringName`                           |
| `kIBGReportBugStringName`                                       | `kLCQReportBugStringName`                                       |
| `kIBGReportFeedbackStringName`                                  | `kLCQReportFeedbackStringName`                                  |
| `kIBGReportBugDescriptionStringName`                            | `kLCQReportBugDescriptionStringName`                            |
| `kIBGReportFeedbackDescriptionStringName`                       | `kLCQReportFeedbackDescriptionStringName`                       |
| `kIBGReportQuestionDescriptionStringName`                       | `kLCQReportQuestionDescriptionStringName`                       |
| `kIBGRequestFeatureDescriptionStringName`                       | `kLCQRequestFeatureDescriptionStringName`                       |
| `kIBGProactiveReportingForceRestartAlertTitle`                  | `kLCQProactiveReportingForceRestartAlertTitle`                  |
| `kIBGProactiveReportingForceRestartAlertMessage`                | `kLCQProactiveReportingForceRestartAlertMessage`                |
| `kIBGProactiveReportingReportActionTitleName`                   | `kLCQProactiveReportingReportActionTitleName`                   |
| `kIBGProactiveReportingCancelActionTitleName`                   | `kLCQProactiveReportingCancelActionTitleName`                   |
| `kIBGAccessibilityReportFeedbackDescriptionStringName`          | `kLCQAccessibilityReportFeedbackDescriptionStringName`          |
| `kIBGAccessibilityReportBugDescriptionStringName`               | `kLCQAccessibilityReportBugDescriptionStringName`               |
| `kIBGAccessibilityRequestFeatureDescriptionStringName`          | `kLCQAccessibilityRequestFeatureDescriptionStringName`          |
| `kIBGPhotoPickerTitle`                                          | `kLCQPhotoPickerTitle`                                          |
| `kIBGProgressViewTitle`                                         | `kLCQProgressViewTitle`                                         |
| `kIBGGalleryPermissionDeniedAlertTitle`                         | `kLCQGalleryPermissionDeniedAlertTitle`                         |
| `kIBGGalleryPermissionDeniedAlertMessage`                       | `kLCQGalleryPermissionDeniedAlertMessage`                       |
| `kIBGMaximumSizeExceededAlertTitle`                             | `kLCQMaximumSizeExceededAlertTitle`                             |
| `kIBGMaximumSizeExceededAlertMessage`                           | `kLCQMaximumSizeExceededAlertMessage`                           |
| `kIBGiCloudImportErrorAlertTitle`                               | `kLCQiCloudImportErrorAlertTitle`                               |
| `kIBGiCloudImportErrorAlertMessage`                             | `kLCQiCloudImportErrorAlertMessage`                             |
| `kIBGEmailFieldPlaceholderStringName`                           | `kLCQEmailFieldPlaceholderStringName`                           |
| `kIBGEmailFieldAccessibilityStringLabel`                        | `kLCQEmailFieldAccessibilityStringLabel`                        |
| `kIBGEmailFieldAccessibilityStringHint`                         | `kLCQEmailFieldAccessibilityStringHint`                         |
| `kIBGNumberFieldPlaceholderStringName`                          | `kLCQNumberFieldPlaceholderStringName`                          |
| `kIBGNumberInfoAlertMessageStringName`                          | `kLCQNumberInfoAlertMessageStringName`                          |
| `kIBGCommentFieldPlaceholderForBugReportStringName`             | `kLCQCommentFieldPlaceholderForBugReportStringName`             |
| `kIBGCommentFieldPlaceholderForFeedbackStringName`              | `kLCQCommentFieldPlaceholderForFeedbackStringName`              |
| `kIBGCommentFieldPlaceholderForQuestionStringName`              | `kLCQCommentFieldPlaceholderForQuestionStringName`              |
| `kIBGCommentFieldPlaceholderForFrustratingExperienceStringName` | `kLCQCommentFieldPlaceholderForFrustratingExperienceStringName` |
| `kIBGCommentFieldAccessibilityStringLabel`                      | `kLCQCommentFieldAccessibilityStringLabel`                      |
| `kIBGCommentFieldBugAccessibilityStringHint`                    | `kLCQCommentFieldBugAccessibilityStringHint`                    |
| `kIBGCommentFieldImprovementAccessibilityStringHint`            | `kLCQCommentFieldImprovementAccessibilityStringHint`            |
| `kIBGCommentFieldAskQuestionAccessibilityStringHint`            | `kLCQCommentFieldAskQuestionAccessibilityStringHint`            |
| `kIBGCommentFieldFrustratingExperienceAccessibilityStringHint`  | `kLCQCommentFieldFrustratingExperienceAccessibilityStringHint`  |
| `kIBGChatReplyFieldPlaceholderStringName`                       | `kLCQChatReplyFieldPlaceholderStringName`                       |
| `kIBGAddScreenRecordingMessageStringName`                       | `kLCQAddScreenRecordingMessageStringName`                       |
| `kIBGAddVoiceMessageStringName`                                 | `kLCQAddVoiceMessageStringName`                                 |
| `kIBGAddImageFromGalleryStringName`                             | `kLCQAddImageFromGalleryStringName`                             |
| `kIBGExtraFieldsStringLabel`                                    | `kLCQExtraFieldsStringLabel`                                    |
| `kIBGAccessibilityExtraFieldsStepsLabel`                        | `kLCQAccessibilityExtraFieldsStepsLabel`                        |
| `kIBGAccessibilityExtraFieldsStepsRequiredLabel`                | `kLCQAccessibilityExtraFieldsStepsRequiredLabel`                |
| `kIBGRequiredExtraFieldsStringLabel`                            | `kLCQRequiredExtraFieldsStringLabel`                            |
| `kIBGAddExtraScreenshotStringName`                              | `kLCQAddExtraScreenshotStringName`                              |
| `kIBGAccessibilityReproStepsDisclaimerStringLabel`              | `kLCQAccessibilityReproStepsDisclaimerStringLabel`              |
| `kIBGAccessibilityImageAttachmentStringHint`                    | `kLCQAccessibilityImageAttachmentStringHint`                    |
| `kIBGAccessibilityVideoAttachmentStringHint`                    | `kLCQAccessibilityVideoAttachmentStringHint`                    |
| `kIBGTakeScreenshotAccessibilityStringLabel`                    | `kLCQTakeScreenshotAccessibilityStringLabel`                    |
| `kIBGTakeScreenRecordingAccessibilityStringLabel`               | `kLCQTakeScreenRecordingAccessibilityStringLabel`               |
| `kIBGSelectImageFromGalleryLabel`                               | `kLCQSelectImageFromGalleryLabel`                               |
| `kIBGAddAttachmentAccessibilityStringLabel`                     | `kLCQAddAttachmentAccessibilityStringLabel`                     |
| `kIBGAddAttachmentAccessibilityStringHint`                      | `kLCQAddAttachmentAccessibilityStringHint`                      |
| `kIBGExpandAttachmentAccessibilityStringLabel`                  | `kLCQExpandAttachmentAccessibilityStringLabel`                  |
| `kIBGCollapseAttachmentAccessibilityStringLabel`                | `kLCQCollapseAttachmentAccessibilityStringLabel`                |
| `kIBGAudioRecordingPermissionDeniedTitleStringName`             | `kLCQAudioRecordingPermissionDeniedTitleStringName`             |
| `kIBGAudioRecordingPermissionDeniedMessageStringName`           | `kLCQAudioRecordingPermissionDeniedMessageStringName`           |
| `kIBGScreenRecordingPermissionDeniedMessageStringName`          | `kLCQScreenRecordingPermissionDeniedMessageStringName`          |
| `kIBGMicrophonePermissionAlertSettingsButtonTitleStringName`    | `kLCQMicrophonePermissionAlertSettingsButtonTitleStringName`    |
| `kIBGMicrophonePermissionAlertLaterButtonTitleStringName`       | `kLCQMicrophonePermissionAlertLaterButtonTitleStringName`       |
| `kIBGChatsTitleStringName`                                      | `kLCQChatsTitleStringName`                                      |
| `kIBGTeamStringName`                                            | `kLCQTeamStringName`                                            |
| `kIBGRecordingMessageToHoldTextStringName`                      | `kLCQRecordingMessageToHoldTextStringName`                      |
| `kIBGRecordingMessageToReleaseTextStringName`                   | `kLCQRecordingMessageToReleaseTextStringName`                   |
| `kIBGMessagesNotificationTitleSingleMessageStringName`          | `kLCQMessagesNotificationTitleSingleMessageStringName`          |
| `kIBGMessagesNotificationTitleMultipleMessagesStringName`       | `kLCQMessagesNotificationTitleMultipleMessagesStringName`       |
| `kIBGScreenshotTitleStringName`                                 | `kLCQScreenshotTitleStringName`                                 |
| `kIBGOkButtonTitleStringName`                                   | `kLCQOkButtonTitleStringName`                                   |
| `kIBGSendButtonTitleStringName`                                 | `kLCQSendButtonTitleStringName`                                 |
| `kIBGCancelButtonTitleStringName`                               | `kLCQCancelButtonTitleStringName`                               |
| `kIBGThankYouAlertTitleStringName`                              | `kLCQThankYouAlertTitleStringName`                              |
| `kIBGThankYouAccessibilityConfirmationTitleStringName`          | `kLCQThankYouAccessibilityConfirmationTitleStringName`          |
| `kIBGThankYouAlertMessageStringName`                            | `kLCQThankYouAlertMessageStringName`                            |
| `kIBGAudioStringName`                                           | `kLCQAudioStringName`                                           |
| `kIBGScreenRecordingStringName`                                 | `kLCQScreenRecordingStringName`                                 |
| `kIBGImageStringName`                                           | `kLCQImageStringName`                                           |
| `kIBGReachedMaximimNumberOfAttachmentsTitleStringName`          | `kLCQReachedMaximimNumberOfAttachmentsTitleStringName`          |
| `kIBGReachedMaximimNumberOfAttachmentsMessageStringName`        | `kLCQReachedMaximimNumberOfAttachmentsMessageStringName`        |
| `kIBGVideoRecordingFailureMessageStringName`                    | `kLCQVideoRecordingFailureMessageStringName`                    |
| `kIBGSurveyEnterYourAnswerTextPlaceholder`                      | `kLCQSurveyEnterYourAnswerTextPlaceholder`                      |
| `kIBGSurveyNoAnswerTitle`                                       | `kLCQSurveyNoAnswerTitle`                                       |
| `kIBGSurveyNoAnswerMessage`                                     | `kLCQSurveyNoAnswerMessage`                                     |
| `kIBGVideoPressRecordTitle`                                     | `kLCQVideoPressRecordTitle`                                     |
| `kIBGCollectingDataText`                                        | `kLCQCollectingDataText`                                        |
| `kIBGLowDiskStorageTitle`                                       | `kLCQLowDiskStorageTitle`                                       |
| `kIBGLowDiskStorageMessage`                                     | `kLCQLowDiskStorageMessage`                                     |
| `kIBGInboundByLineMessage`                                      | `kLCQInboundByLineMessage`                                      |
| `kIBGExtraFieldIsRequiredText`                                  | `kLCQExtraFieldIsRequiredText`                                  |
| `kIBGExtraFieldMissingDataText`                                 | `kLCQExtraFieldMissingDataText`                                 |
| `kIBGFeatureRequestsTitle`                                      | `kLCQFeatureRequestsTitle`                                      |
| `kIBGFeatureDetailsTitle`                                       | `kLCQFeatureDetailsTitle`                                       |
| `kIBGStringFeatureRequestsRefreshText`                          | `kLCQStringFeatureRequestsRefreshText`                          |
| `kIBGFeatureRequestErrorStateTitleLabel`                        | `kLCQFeatureRequestErrorStateTitleLabel`                        |
| `kIBGFeatureRequestErrorStateDescriptionLabel`                  | `kLCQFeatureRequestErrorStateDescriptionLabel`                  |
| `kIBGFeatureRequestSortingByRecentlyUpdatedText`                | `kLCQFeatureRequestSortingByRecentlyUpdatedText`                |
| `kIBGFeatureRequestSortingByTopVotesText`                       | `kLCQFeatureRequestSortingByTopVotesText`                       |
| `kIBGStringFeatureRequestAllFeaturesText`                       | `kLCQStringFeatureRequestAllFeaturesText`                       |
| `kIBGAddNewFeatureRequestText`                                  | `kLCQAddNewFeatureRequestText`                                  |
| `kIBGAddNewFeatureRequestToastText`                             | `kLCQAddNewFeatureRequestToastText`                             |
| `kIBGAddNewFeatureRequestErrorToastText`                        | `kLCQAddNewFeatureRequestErrorToastText`                        |
| `kIBGAddNewFeatureRequestLoadingHUDTitle`                       | `kLCQAddNewFeatureRequestLoadingHUDTitle`                       |
| `kIBGAddNewFeatureRequestSuccessHUDTitle`                       | `kLCQAddNewFeatureRequestSuccessHUDTitle`                       |
| `kIBGAddNewFeatureRequestSuccessHUDMessage`                     | `kLCQAddNewFeatureRequestSuccessHUDMessage`                     |
| `kIBGAddNewFeatureRequestTryAgainText`                          | `kLCQAddNewFeatureRequestTryAgainText`                          |
| `kIBGAddNewFeatureRequestCancelPromptTitle`                     | `kLCQAddNewFeatureRequestCancelPromptTitle`                     |
| `kIBGAddNewFeatureRequestCancelPromptYesAction`                 | `kLCQAddNewFeatureRequestCancelPromptYesAction`                 |
| `kIBGFeatureRequestInvalidEmailText`                            | `kLCQFeatureRequestInvalidEmailText`                            |
| `kIBGFeatureRequestTimelineEmptyText`                           | `kLCQFeatureRequestTimelineEmptyText`                           |
| `kIBGFeatureRequestTimelineErrorDescriptionLabel`               | `kLCQFeatureRequestTimelineErrorDescriptionLabel`               |
| `kIBGFeatureRequestStatusChangeText`                            | `kLCQFeatureRequestStatusChangeText`                            |
| `kIBGFeatureRequestAddButtonText`                               | `kLCQFeatureRequestAddButtonText`                               |
| `kIBGFeatureRequestVoteWithCountText`                           | `kLCQFeatureRequestVoteWithCountText`                           |
| `kIBGFeatureRequestVoteText`                                    | `kLCQFeatureRequestVoteText`                                    |
| `kIBGFeatureRequestPostButtonText`                              | `kLCQFeatureRequestPostButtonText`                              |
| `kIBGFeatureRequestCommentsText`                                | `kLCQFeatureRequestCommentsText`                                |
| `kIBGFeatureRequestAuthorText`                                  | `kLCQFeatureRequestAuthorText`                                  |
| `kIBGFeatureRequestEmptyViewTitle`                              | `kLCQFeatureRequestEmptyViewTitle`                              |
| `kIBGFeatureRequestAddYourIdeaText`                             | `kLCQFeatureRequestAddYourIdeaText`                             |
| `kIBGFeatureRequestAnonymousText`                               | `kLCQFeatureRequestAnonymousText`                               |
| `kIBGFeatureRequestStatusPosted`                                | `kLCQFeatureRequestStatusPosted`                                |
| `kIBGFeatureRequestStatusPlanned`                               | `kLCQFeatureRequestStatusPlanned`                               |
| `kIBGFeatureRequestStatusStarted`                               | `kLCQFeatureRequestStatusStarted`                               |
| `kIBGFeatureRequestStatusCompleted`                             | `kLCQFeatureRequestStatusCompleted`                             |
| `kIBGFeatureRequestStatusMaybeLater`                            | `kLCQFeatureRequestStatusMaybeLater`                            |
| `kIBGFeatureRequestStatusMoreText`                              | `kLCQFeatureRequestStatusMoreText`                              |
| `kIBGFeatureRequestStatusLessText`                              | `kLCQFeatureRequestStatusLessText`                              |
| `kIBGFeatureRequestAddYourThoughtsText`                         | `kLCQFeatureRequestAddYourThoughtsText`                         |
| `kIBGEmailRequiredText`                                         | `kLCQEmailRequiredText`                                         |
| `kIBGNameText`                                                  | `kLCQNameText`                                                  |
| `kIBGEmailText`                                                 | `kLCQEmailText`                                                 |
| `kIBGTitleText`                                                 | `kLCQTitleText`                                                 |
| `kIBGDescriptionText`                                           | `kLCQDescriptionText`                                           |
| `kIBGUserConsentRequired`                                       | `kLCQUserConsentRequired`                                       |
| `kIBGUserConsentDefaultDescription`                             | `kLCQUserConsentDefaultDescription`                             |
| `kIBGStringFeatureRequestMyFeaturesText`                        | `kLCQStringFeatureRequestMyFeaturesText`                        |
| `kIBGSurveyIntroTitleText`                                      | `kLCQSurveyIntroTitleText`                                      |
| `kIBGSurveyIntroDescriptionText`                                | `kLCQSurveyIntroDescriptionText`                                |
| `kIBGSurveyIntroTakeSurveyButtonText`                           | `kLCQSurveyIntroTakeSurveyButtonText`                           |
| `kIBGDismissButtonTitleStringName`                              | `kLCQDismissButtonTitleStringName`                              |
| `kIBGStoreRatingThankYouTitleText`                              | `kLCQStoreRatingThankYouTitleText`                              |
| `kIBGStoreRatingThankYouDescriptionText`                        | `kLCQStoreRatingThankYouDescriptionText`                        |
| `kIBGSurveysNPSLeastLikelyStringName`                           | `kLCQSurveysNPSLeastLikelyStringName`                           |
| `kIBGSurveysNPSMostLikelyStringName`                            | `kLCQSurveysNPSMostLikelyStringName`                            |
| `kIBGSurveyNextButtonTitle`                                     | `kLCQSurveyNextButtonTitle`                                     |
| `kIBGSurveySubmitButtonTitle`                                   | `kLCQSurveySubmitButtonTitle`                                   |
| `kIBGSurveyAppStoreThankYouTitle`                               | `kLCQSurveyAppStoreThankYouTitle`                               |
| `kIBGSurveyAppStoreButtonTitle`                                 | `kLCQSurveyAppStoreButtonTitle`                                 |
| `kIBGExpectedResultsStringName`                                 | `kLCQExpectedResultsStringName`                                 |
| `kIBGActualResultsStringName`                                   | `kLCQActualResultsStringName`                                   |
| `kIBGStepsToReproduceStringName`                                | `kLCQStepsToReproduceStringName`                                |
| `kIBGReplyButtonTitleStringName`                                | `kLCQReplyButtonTitleStringName`                                |
| `kIBGAddAttachmentButtonTitleStringName`                        | `kLCQAddAttachmentButtonTitleStringName`                        |
| `kIBGDiscardAlertTitle`                                         | `kLCQDiscardAlertTitle`                                         |
| `kIBGDiscardAlertMessage`                                       | `kLCQDiscardAlertMessage`                                       |
| `kIBGDiscardAlertAction`                                        | `kLCQDiscardAlertAction`                                        |
| `kIBGDiscardAlertCancel`                                        | `kLCQDiscardAlertCancel`                                        |
| `kIBGVideoGalleryErrorMessageStringName`                        | `kLCQVideoGalleryErrorMessageStringName`                        |
| `kIBGVideoDurationErrorTitle`                                   | `kLCQVideoDurationErrorTitle`                                   |
| `kIBGVideoDurationErrorMessage`                                 | `kLCQVideoDurationErrorMessage`                                 |
| `kIBGAutoScreenRecordingAlertAllowText`                         | `kLCQAutoScreenRecordingAlertAllowText`                         |
| `kIBGAutoScreenRecordingAlertAlwaysAllowText`                   | `kLCQAutoScreenRecordingAlertAlwaysAllowText`                   |
| `kIBGAutoScreenRecordingAlertDenyText`                          | `kLCQAutoScreenRecordingAlertDenyText`                          |
| `kIBGAutoScreenRecordingAlertTitleText`                         | `kLCQAutoScreenRecordingAlertTitleText`                         |
| `kIBGAutoScreenRecordingAlertBodyText`                          | `kLCQAutoScreenRecordingAlertBodyText`                          |
| `kIBGReproStepsDisclaimerBody`                                  | `kLCQReproStepsDisclaimerBody`                                  |
| `kIBGReproStepsDisclaimerLink`                                  | `kLCQReproStepsDisclaimerLink`                                  |
| `kIBGReproStepsListHeader`                                      | `kLCQReproStepsListHeader`                                      |
| `kIBGReproStepsListEmptyStateLabel`                             | `kLCQReproStepsListEmptyStateLabel`                             |
| `kIBGReproStepsListTitle`                                       | `kLCQReproStepsListTitle`                                       |
| `kIBGReproStepsListItemName`                                    | `kLCQReproStepsListItemName`                                    |
| `kIBGInsufficientContentTitleStringName`                        | `kLCQInsufficientContentTitleStringName`                        |
| `kIBGInsufficientContentMessageStringName`                      | `kLCQInsufficientContentMessageStringName`                      |
