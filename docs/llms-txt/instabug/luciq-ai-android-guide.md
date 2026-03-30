# Source: https://docs.instabug.com/android/set-up-luciq-for-android/integrate-luciq-on-android/luciq-ai-android-guide.md

# Guide for AI Coding Agents to Integrate Luciq on Android

## Guide for AI Coding Agents to Integrate Luciq on Android

### ⚠️ UNIVERSAL EXECUTION RULES ⚠️

#### Critical Rules - Apply to ALL Platforms:

* **NEVER skip WAIT instructions** - always get user confirmation before proceeding
* **NEVER auto-execute optional steps** - user must explicitly select them
* **ALWAYS fetch latest SDK version** before integration (DO NOT use placeholders like 1.0.0)
* **ALL API parameters must be included** (can be nil/null) - never omit parameters

#### Execution Guidelines:

* **Be specific and concise** - save tokens by being to the point
* **Don't create documentation files** - only code files required for integration
* **Implement mandatory steps sequentially** - complete each before moving to the next
* **Prompt user with current step** - describe what's happening, then proceed when done
* **Only ask for optional steps after mandatory ones** - show numbered list for selection
* **Use numbered lists for all options** - makes selection easier (e.g., "Select 1", "Select 2")
* **Add wrap up step** - execute validation only when user selects "Wrap up & validate"
* **Check documentation first** - confirm API availability before getting creative beyond examples

#### Official Documentation:

* Main docs: <https://docs.luciq.ai/>
* Always check official docs when unsure about API signatures or platform specifics

***

### Integration Workflow Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    MANDATORY STEPS                          │
├─────────────────────────────────────────────────────────────┤
│ Step 1: Collect Required Information                       │
│   ├─ 1A: Get App Token (MCP or Manual)                    │
│   ├─ 1B: Determine Integration Method                     │
│   └─ 1C: Apply Default Config (Inform + Opt-in Customize) │
│                                                             │
│ Step 2: Add SDK Dependency (Platform-Specific)            │
│   └─ Fetch latest version from GitHub API                 │
│                                                             │
│ Step 3: Initialize the SDK (Platform-Specific)            │
│   └─ Default: shake + floatingButton                      │
│                                                             │
│ Step 3B: Configure Network Interception [ANDROID ONLY]    │
│   └─ Enable unified network interception in Gradle        │
│                                                             │
│ Step 4: Configure Network Logging [MANDATORY]             │
│   └─ Enable network capture + mask sensitive fields       │
│                                                             │
│ Step 5: Mask Repro Step Screenshots [MANDATORY]           │
│   └─ iOS: maskNothing default | Android: all types        │
│                                                             │
│ Step 6: Upload Symbolication Files [MANDATORY]            │
│   └─ iOS: dSYM via Build Phase | Android: mapping files   │
│                                                             │
│ 🛑 MANDATORY STEPS COMPLETE                               │
├─────────────────────────────────────────────────────────────┤
│              OPTIONAL FEATURES                              │
├─────────────────────────────────────────────────────────────┤
│ Available after mandatory steps (user-selected):          │
│   • Repro Steps Mode: Configure per product               │
│   • User Identification: Link reports to users            │
├─────────────────────────────────────────────────────────────┤
│                    VERIFICATION                             │
├─────────────────────────────────────────────────────────────┤
│ Wrap up & validate: Build → Test → Verify Dashboard       │
└─────────────────────────────────────────────────────────────┘
```

***

### Step 1 — Collect Required Information **\[MANDATORY]**

#### 1A: Get App Token

**Check MCP Server First:**

```
IF Luciq MCP server is installed:
  1. Fetch all tokens with app names using MCP tools
  2. Display tokens to user in numbered list with app names
  3. Ask: "Which app token would you like to use?"
  4. WAIT for selection
  5. Store selected token
ELSE:
  1. Display to user: "To integrate Luciq SDK, you'll need your App Token."
  2. Display to user:
     "📍 Find your token: Luciq Dashboard → Settings → SDK Integration"
  3. Display on new line with indentation:
     "   Dashboard URL: https://dashboard.luciq.ai"
  4. Ask: "Please provide your Luciq App Token:"
  5. WAIT for user to provide token
  6. Validate token format (non-empty, alphanumeric)
  7. Store token for later use
END IF
```

**Validation:**

* Token should be non-empty
* Typically 32-40 character hexadecimal string
* If invalid format, warn user but proceed

***

#### 1B: Determine Integration Method

**Auto-Detection Logic:**

Platform-specific detection should look for:

* **iOS**: `Podfile`, `Cartfile`, SPM packages in `.xcodeproj`, or none → Manual
* **Android**: `build.gradle` with repositories, `pom.xml`, or none → Manual

```
DETECT package managers in project:
  - Count how many are found

IF exactly ONE package manager detected:
  1. Inform user: "Detected [PackageManager], will use this for integration"
  2. Store integration_method
  3. Proceed to Step 2
ELSE IF multiple or zero detected:
  1. Display platform-specific menu (see platform guides)
  2. WAIT for user selection
  3. Store integration_method
  4. Proceed to Step 2
END IF
```

***

#### 1C: Apply Default Configuration (Inform + Opt-in)

**Default configuration is applied automatically. Inform the user:**

```
Display: "Applying default configuration:
  • Invocation: shake + floatingButton
  • Network logging: enabled with common field masking
  • Screenshot masking:
      - iOS: maskNothing (customize per privacy settings)
      - Android: all types (text inputs, labels, media)
  • Symbolication: automatic upload enabled
  • APM (Android): enabled
  • User identification: skip (can add later)

Would you like to customize any of these settings? (yes/no)"

WAIT for response
```

**Store default configuration:**

```
  - invocation_events = [shake, floatingButton]
  - network_logging_enabled = true
  - network_masking_enabled = true
  - predefined_headers_to_mask = ["Authorization", "Cookie", "X-API-Key", "token"]
  - predefined_body_fields_to_mask = ["password", "token", "ssn"]
  - auto_masking_types:
      - iOS: maskNothing (with guidance comments)
      - Android: [textInputs, labels, media]
  - symbolication_upload = enabled
  - repro_steps_config = skip (use defaults)
  - user_identification = skip

FOR ANDROID ONLY:
  - apm_enabled = true
  - Continue to Step 1D (Compose detection)

FOR iOS:
  - Continue to Step 1D (Fastlane detection for dSYM)
```

**If user wants to customize (yes):**

```
CUSTOMIZATION LOOP:

1. Display: "Which setting would you like to customize?
     1. Invocation events
     2. Network logging
     3. Screenshot masking
     4. Symbolication upload
     5. User identification

   Enter number:"

2. WAIT for selection

3. Apply the customization (see platform-specific guides for options)

4. Redisplay updated configuration:
   "Updated configuration:
     • Invocation: <current setting>  ← CHANGED (if modified)
     • Network logging: <current setting>
     • Screenshot masking: <current setting>
     • Symbolication: <current setting>
     • User identification: <current setting>

   Would you like to customize anything else? (yes/no)"

5. WAIT for response

6. IF yes → Go to step 1
   IF no → Proceed to Step 2

LOOP until user confirms to move on
```

**If user does not want to customize (no):**

* Proceed to Step 2

***

### Step 2 — Add SDK Dependency **\[MANDATORY - Platform-Specific]**

#### Pre-Dependency Critical Step:

**⚠️ MUST FETCH LATEST VERSION FIRST:**

```
1. Fetch latest version from GitHub API:
   - iOS: https://api.github.com/repos/luciqai/luciq-ios-sdk/releases/latest
   - Android: https://api.github.com/repos/luciqai/luciq-android-sdk/releases/latest

2. Extract version number from the "tag_name" field (e.g., "19.1.0")

3. Store version for dependency configuration

4. DO NOT use placeholder versions like "1.0.0" or "latest"
```

**Then proceed to platform-specific dependency installation (see platform guides)**

***

### Step 3 — Initialize the SDK **\[MANDATORY - Platform-Specific]**

#### Invocation Events Configuration

**Default invocation events:** `[shake, floatingButton]`

These are applied automatically unless the user chose to customize in Step 1C.

**If user chose to customize invocation events:**

```
"Which invocation events (1 or more) should trigger Luciq?"

Options (select all that apply):
  1. shake: Device shake gesture
  2. screenshot: Screenshot capture
  3. floatingButton: Persistent floating button overlay
  4. none: Manual invocation only (via code)

WAIT for selection
```

**Invocation Event Mapping:**

* `none` → Empty array `[]`
* Single selection → `[selected]`
* Multiple → `[event1, event2, ...]`

**Apply configuration in platform-specific syntax (see platform guides)**

***

### Step 4 — Configure Network Logging **\[MANDATORY]**

#### Concepts (Platform-Agnostic):

**Purpose:** Automatically capture network requests/responses and optionally mask sensitive data

**Part A: Network Capture**

```
Display options:
  1. Keep automatic network capture enabled (default)
  2. Disable automatic network capture

WAIT for selection

IF option 2:
  - Apply platform-specific disable code (see platform guide)
  - END
ELSE IF option 1:
  - Continue with default (enabled)
END IF
```

**Part B: Mask Sensitive Data**

```
Display: "Specify which fields to mask:
          Options:
            1. Enter comma-separated field names
            2. Skip (no masking)

          For option 1, specify:
            - Headers (e.g., Authorization, Cookie, X-API-Key)
            - Body fields (e.g., password, token, ssn)"

WAIT for input

IF option 1 selected and input provided:
  Parse input:
    - Split by comma
    - Trim whitespace
    - Create arrays: headersToMask[], bodyFieldsToMask[]

  Apply platform-specific masking code (see platform guide):
    - Use loops for headers
    - Use recursion for nested body fields
    - Handle arrays and nested objects
ELSE IF option 2:
  - Leave network logs unmasked
END IF
```

**Implementation Requirements:**

* Masking code MUST be placed AFTER SDK initialization
* Headers: Simple loop through header names
* Body: Recursive function to handle nested JSON at any depth
* Performance: Use Set/HashSet for O(1) field lookup

***

### Step 5 — Mask Repro Step Screenshots **\[MANDATORY]**

#### Concepts (Platform-Agnostic):

**Purpose:** Automatically blur/mask sensitive UI elements in screenshot repro steps

**Default Configuration:**

* **iOS:** `maskNothing` (with guidance comments for customization)
* **Android:** All types (`textInputs`, `labels`, `media`)

```
Apply default screenshot masking configuration:

IF platform == iOS:
  Apply: Luciq.setAutoMaskScreenshots(.maskNothing)
  Add guidance comment about available options
ELSE IF platform == Android:
  Apply: Luciq.setAutoMaskScreenshotsTypes(MaskingType.TEXT_INPUTS, MaskingType.LABELS, MaskingType.MEDIA)
END IF
```

**If user chose to customize in Step 1C:**

```
Display options - Which types of elements should be masked?
  1. Text inputs only
  2. Labels only
  3. Images/media only
  4. Text inputs + labels
  5. All (text inputs + labels + media)
  6. Custom selection
  7. None (no screenshot masking - iOS only)

WAIT for selection

Map selection to mask types:
  1 → [textInputs]
  2 → [labels]
  3 → [images]
  4 → [textInputs, labels]
  5 → [textInputs, labels, images]
  6 → Ask for custom combination, then apply
  7 → maskNothing (iOS only)

Apply platform-specific masking API (see platform guide)
```

**Available Mask Types:**

* iOS:
  * `.textInputs`: Text input fields, password fields
  * `.labels`: Text labels, buttons with text
  * `.media`: Comprehensive masking (includes all types)
  * `.maskNothing`: No automatic masking (default)
* Android:
  * `MaskingType.TEXT_INPUTS`: Text input fields, password fields
  * `MaskingType.LABELS`: Text labels, buttons with text
  * `MaskingType.MEDIA`: Images, media content
  * `MaskingType.MASK_NOTHING`: Disable auto masking

***

### Step 6 — Upload Symbolication Files **\[MANDATORY]**

#### Concepts (Platform-Agnostic):

**Purpose:** Upload debug symbols (dSYM for iOS, mapping files for Android) for crash symbolication. This is required for readable crash reports.

#### iOS (dSYM Upload):

**Detection-based approach:**

```
1. Check if project uses Fastlane for archiving:
   - Look for Fastfile in project root or fastlane/ directory
   - Check if it contains archive/gym lanes

IF Fastlane detected:
   Use Fastlane Plugin approach
ELSE:
   Use Build Post-actions Script approach
```

**See ios-guide.md for implementation details.**

#### Android (Mapping File Upload):

**Default: Gradle task (automatic)**

```
Add Gradle task to upload ProGuard/R8 mapping files automatically
after release builds.
```

**See android-guide.md for implementation details.**

#### Customization Options:

```
Display: "How would you like to upload symbolication files?"

Options:
  1. Automatic (recommended) - configured during build/archive
  2. Manual - upload through dashboard
  3. Skip - disable symbolication upload

WAIT for selection
```

***

### 🛑 MANDATORY STEPS COMPLETE - STOP HERE

***

### Optional Steps Menu

**After all mandatory steps are complete, display:**

```
"✅ Luciq SDK mandatory integration complete!

Configuration Summary:
  • Invocation: <configured events>
  • Network Logging: enabled with masking
  • Network Masking:
      - Headers: Authorization, Cookie, X-API-Key, token
      - Body Fields: password, token, ssn
  • Screenshot Masking: <configured types>
  • Symbolication Upload: configured

Ready to build and test?
  1. Wrap up & validate (build and test)
  2. Configure optional features (repro steps mode, user identification)

Enter number:"

WAIT for selection
```

***

### Optional Step 1 — Configure Repro Steps Mode

#### Concepts (Platform-Agnostic):

**Purpose:** Control which products include screenshots in their repro steps

**Default Behavior:**

* Bug Reporting: Screenshots enabled
* Crash Reporting: Screenshots disabled
* Session Replay: Screenshots enabled

```
Display: "Select products to ENABLE screenshots for:"

Options (multiple selection):
  1. Bug Reporting
  2. Crash Reporting
  3. Session Replay
  4. All products
  5. None (disable screenshots for all)
  6. Keep defaults (Bug Reporting + Session Replay with screenshots, Crash without)

Enter selections (e.g., "1,3" or "4"):

WAIT for input

IF option 6:
  - Keep default configuration
  - END
ELSE IF option 5 or "none" selected:
  - Disable screenshots for all products
  - Apply platform-specific configuration (see platform guide)
  - END
ELSE:
  Parse selections:
    - Selected products → Enable with screenshots
    - Non-selected products → Enable WITHOUT screenshots

  Apply platform-specific configuration (see platform guide)
END IF
```

**Issue Type Mapping:**

* Bug Reporting → `.bug` / `IssueType.Bug`
* Crash Reporting → `.allCrashes` / `IssueType.AllCrashes`
* Session Replay → `.sessionReplay` / `IssueType.SessionReplay`
* All products → `.all` / `IssueType.All`

***

### Optional Step 2 — Add User Identification

#### Concepts (Platform-Agnostic):

**Purpose:** Link bug reports to specific user accounts for better tracking

```
Display options - How would you like to identify users?
  1. Using email
  2. Using user ID
  3. Using both email and ID
  4. Skip (no user identification)

WAIT for selection

IF option 4:
  - Skip user identification
  - END
ELSE:
  Store user_id_method
  Proceed to Step 3A and 3B
END IF
```

#### Step 3A: Identify Login Flows

**Search Strategy:**

1. Search for authentication/login methods in codebase
2. Look for successful login callbacks/handlers
3. Identify where user data becomes available

**Placement Rules:**

* Add identification AFTER authentication succeeds
* Add BEFORE any navigation/routing
* Ensure user data (email/id/name) is available at this point

**API Signature (All Platforms):**

```
identifyUser(
  id: String/null,      // User ID - required param, can be null
  email: String/null,   // Email - required param, can be null
  name: String/null     // Name - required param, can be null
)
```

**Examples by Selection:**

* Option 1 (email): `identifyUser(null, user.email, user.name)`
* Option 2 (ID): `identifyUser(user.id, null, user.name)`
* Option 3 (both): `identifyUser(user.id, user.email, user.name)`

**Platform-Specific Syntax:** See platform guides

***

#### Step 3B: Identify Logout Flows

**Search Strategy:**

1. Search for logout/signout methods in codebase
2. Look for session clearing logic
3. Identify where user data is removed

**Placement Rules:**

* Add logout call BEFORE clearing user session/data
* Ensure it's called on all logout paths

**API Signature (All Platforms):**

```
logOut() / logout()  // No parameters
```

**Platform-Specific Syntax:** See platform guides

***

### Step 7 — Verification & Testing (Wrap up & validate) **\[USER-INITIATED ONLY]**

**⚠️ CRITICAL:** This step is ONLY executed when the user explicitly selects "Wrap up & validate" from the optional steps menu. Do NOT run automatically after mandatory steps complete.

#### After Mandatory Steps Complete

**Display this summary and menu:**

```
✅ Luciq SDK integration complete!

Platform: <iOS/Android>
SDK Version: <version>
Integration Method: <SPM/Gradle/etc>

Configuration:
  • App Token: <first 8 chars>...
  • Invocation Events: <configured events>
  • Network Logging: <enabled/disabled>
  • Network Masking:
      - Headers: <list or none>
      - Body Fields: <list or none>
  • Screenshot Masking: <types or none>
  • Symbolication Upload: <automatic/manual/skip>
  • User Identification: <configured or not configured>

Next Steps - Select an option:
1. Configure optional features
2. Wrap up & validate
```

**WAIT for user selection. Do NOT proceed to build verification unless user selects option 2.**

***

#### 1. Build Verification **\[ONLY WHEN USER REQUESTS]**

**Execute platform-specific build command:**

* iOS: `xcodebuild -project ... -scheme ... build`
* Android: `./gradlew assembleDebug`

**Expected Result:** BUILD SUCCEEDED with no errors

**Common Build Errors & Solutions:**

| Error                                  | Likely Cause           | Solution                                |
| -------------------------------------- | ---------------------- | --------------------------------------- |
| "no such module" / "unresolved import" | Wrong import statement | Check platform guide for correct import |
| "version not found"                    | Invalid SDK version    | Verify version fetched from releases    |
| "package not resolved"                 | Dependency not added   | Re-run package manager sync             |

***

#### 2. Runtime Testing **\[MANUAL]**

**After successful build, instruct user to perform these steps:**

```
1. Build and run the app on simulator/emulator or device

2. Trigger Luciq using configured invocation method:
   - IF shake enabled: Shake the device/simulator
   - IF screenshot enabled: Take a screenshot
   - IF floatingButton enabled: Tap the floating button

3. Verify Luciq UI appears

4. Fill out and submit a test bug report

5. Check Luciq dashboard at https://dashboard.luciq.ai
   - Verify report appears
   - Verify user identification (if configured)
   - Verify network logs (if configured)
```

***

#### 3. Final Summary **\[DISPLAY AFTER BUILD SUCCESS]**

**Generate and display summary after successful validation:**

```
✅ Luciq SDK successfully integrated and validated!

Platform: <iOS/Android>
SDK Version: <version>
Integration Method: <SPM/Gradle/etc>

Configuration:
  • App Token: <first 8 chars>...
  • Invocation Events: <configured events>
  • Network Logging: <enabled/disabled>
  • Network Masking:
      - Headers: <list or none>
      - Body Fields: <list or none>
  • Screenshot Masking: <types or none>
  • Symbolication Upload: <automatic/manual/skip>
  • User Identification: <configured or not configured>

Build Status: ✅ SUCCEEDED

Next Steps:
  • ✅ Build completed successfully
  • Run the app and test SDK invocation
  • Submit a test report
  • Verify report in Luciq dashboard

Integration Complete - Ready for Testing!
```

***

### Error Handling & Troubleshooting

#### Common Issues Across Platforms:

**1. SDK Not Initializing:**

* Verify token is correct
* Check initialization code placement (usually in app entry point)
* Ensure import statement is correct

**2. Network Logging Not Working:**

* Verify masking code placed AFTER SDK initialization
* Check that network interceptor is properly configured
* Ensure app has network permissions

**3. User Identification Not Showing:**

* Verify identifyUser called after successful login
* Check that logout is called on all logout paths
* Ensure parameters are not all null

**4. Reports Not Appearing in Dashboard:**

* Verify device/simulator has internet connection
* Check app token is correct
* Wait a few minutes for sync
* Check dashboard filters

***

### Extension Points for Platform Guides

Platform-specific guides should include:

#### Required Sections:

1. **Platform-Specific Critical Rules** (import naming, package names, etc.)
2. **Pre-Integration Checklist** (platform-specific gotchas)
3. **Step 2 Implementation** (dependency management code)
4. **Step 3 Implementation** (SDK initialization code)
5. **Step 4 Implementation** (network logging code) \[MANDATORY]
6. **Step 5 Implementation** (screenshot masking code) \[MANDATORY]
7. **Step 6 Implementation** (symbolication upload code) \[MANDATORY]
8. **Optional Step 1 Implementation** (repro steps mode)
9. **Optional Step 2 Implementation** (user identification code)
10. **Step 7 Implementation** (build commands, platform-specific testing)

#### Reference Format:

```markdown
## Step X — [Title]

> 📋 See [common-workflow.md#step-x](common-workflow.md#step-x) for detailed workflow

### Platform-Specific Implementation

[Platform-specific code and instructions]
```

## Luciq SDK Integration - Android Guide

> **Purpose:** Android-specific implementation details for Luciq SDK integration. This guide provides Android-specific code, configuration, and platform requirements.

***

### ⚠️ ANDROID-SPECIFIC CRITICAL RULES ⚠️

#### Package and Import:

1. **Gradle Dependency**: `implementation 'ai.luciq.library:luciq:<VERSION>'`
2. **Import Statement**: `import ai.luciq.library.Luciq`
3. **Language**: Code examples in Kotlin (Java equivalents straightforward)
4. **Minimum Requirements**: compileSdkVersion 29 or above
5. **Android 15+ (API 35)**: Requires Luciq 13.4.0+ for 16KB page size support

#### Android-Specific Execution Rules:

* Initialize in Application class (not Activity)
* Network interception: **MANDATORY** - Configure in Step 3B (Gradle plugin auto-instruments OkHttp/UrlConnection)
* APM provides: App launch, network performance, UI hangs, screen loading metrics
* At least email OR id required for user identification (both null = error)
* Use exact version in gradle (not `+` or ranges)
* ALL API parameters must be included (can be `null`)

#### Official Android Documentation:

* Android Integration: <https://docs.luciq.ai/docs/android-integration>
* APM Migration: <https://docs.luciq.ai/docs/android-luciq-migration>
* User Identification: <https://docs.luciq.ai/docs/android-identify-user>
* Network Logging: <https://docs.luciq.ai/reference/network-logging-android>
* Screenshot Masking: <https://docs.luciq.ai/docs/android-repro-steps>
* Unified Network Interceptor: <https://docs.luciq.ai/docs/android-unified-network-interception>

***

***

## ANDROID-SPECIFIC IMPLEMENTATION DETAILS

***

### Pre-Integration Checklist

Before starting, verify you understand these Android-specific points:

* [ ] Must initialize in Application class (not Activity)
* [ ] **SDK initialization MUST be the FIRST line** after `super.onCreate()` in Application class
* [ ] Requires compileSdkVersion 29+
* [ ] APM (default: enabled): Enables advanced performance monitoring
* [ ] **Network interception is MANDATORY** - configure in Step 3B
* [ ] **Network logging is MANDATORY** - configure masking after SDK initialization
* [ ] **Screenshot masking is MANDATORY** - configure after SDK initialization
* [ ] **Mapping file upload is MANDATORY** - configure Gradle task for ProGuard/R8
* [ ] At least email OR id required in identifyUser
* [ ] Use exact version in gradle dependencies

***

### Step 1 — Collect Required Information **\[MANDATORY]**

> 📋 **Workflow:** See [common-workflow.md - Step 1](https://github.com/luciqai/luciq-docs/blob/main/android/set-up-luciq-for-android/integrate-luciq-on-android/common-workflow.md#step-1--collect-required-information-mandatory)

#### Android-Specific Implementation

**Package Manager Detection:**

Check for:

* `build.gradle` / `build.gradle.kts` → Gradle
* `pom.xml` → Maven

**Integration Method Menu (if multiple/none detected):**

1. Gradle (Recommended)
2. Maven

***

#### 1C: Apply Default Configuration (Inform + Opt-in)

> 📋 **Workflow:** See [common-workflow.md - Step 1C](https://github.com/luciqai/luciq-docs/blob/main/android/set-up-luciq-for-android/integrate-luciq-on-android/common-workflow.md#1c-apply-default-configuration-inform--opt-in)

**For Android:**

* Default configuration is applied automatically (shake + floatingButton, APM enabled, network masking, etc.)
* User is informed of defaults and can opt-in to customize
* If user customizes: Use the customization loop (select → apply → redisplay → confirm)
* `apm_enabled` is set to `true` by default
* After configuration: Continue to Step 1D

***

#### 1D: APM (Application Performance Monitoring)

**Check Configuration Mode:**

```
IF config_mode == default:
  apm_enabled is already set to true
  Skip APM prompt, continue to Step 2
ELSE IF config_mode == custom:
  Ask User:
    "Do you want to enable APM (Application Performance Monitoring)?

    APM provides:
      - App launch tracking
      - Network performance monitoring
      - UI hangs detection
      - Screen loading metrics
      - Custom traces & attributes

    Options: yes / no

    WAIT for response"

  Store selection as `apm_enabled` (true/false)
END IF
```

***

### Step 2 — Add the Luciq SDK Dependency **\[MANDATORY]**

> 📋 **Workflow:** See [common-workflow.md - Step 2](https://github.com/luciqai/luciq-docs/blob/main/android/set-up-luciq-for-android/integrate-luciq-on-android/common-workflow.md#step-2--add-sdk-dependency-mandatory---platform-specific) Fetch latest version from GitHub API: <https://api.github.com/repos/luciqai/luciq-android-sdk/releases/latest> Extract version from the "tag\_name" field. DO NOT hardcode versions like "18.0.0".

#### Android Implementation

**Check Configuration Mode:**

```
IF config_mode == default:
  Apply plugins automatically:
    - Always: id("luciq")
    - Always (Android default): id("luciq-apm")
ELSE IF config_mode == custom:
  Apply plugins based on user selections
END IF
```

**Part A: Gradle Plugins**

**If `integration_method == gradle`:**

```kotlin
// In project-level build.gradle.kts (Kotlin DSL)
plugins {
    id("ai.luciq.library") version "<FETCHED_VERSION>" apply false
}

// OR in project-level build.gradle (Groovy DSL)
buildscript {
    dependencies {
        classpath "ai.luciq.library:luciq-plugin:<FETCHED_VERSION>"
    }
}

// In app-level build.gradle.kts (Kotlin DSL)
plugins {
    id("luciq")
    // Add if APM enabled (default):
    IF config_mode == default OR apm_enabled: id("luciq-apm")
}

// In app-level build.gradle (Groovy)
plugins {
    id 'luciq'
    // Add if APM enabled (default):
    IF config_mode == default OR apm_enabled: id 'luciq-apm'
}
```

**⚠️ Firebase Plugin Order:** If project uses Firebase Performance Monitoring, ensure Luciq plugins are declared BEFORE Firebase:

```kotlin
plugins {
    id("luciq")
    id("luciq-apm")
    id("com.google.firebase.firebase-perf")  // Firebase AFTER Luciq
}
```

#### Part B: Add Dependencies

**Base Dependencies (Always Required):**

```kotlin
// build.gradle.kts (Kotlin DSL)
dependencies {
    implementation("ai.luciq.library:luciq:<FETCHED_VERSION>")
}

// build.gradle (Groovy)
dependencies {
    implementation 'ai.luciq.library:luciq:<FETCHED_VERSION>'
}
```

**APM Dependencies (If `config_mode == default` OR `apm_enabled == true`):**

```kotlin
// build.gradle.kts (Kotlin DSL)
dependencies {
    implementation("ai.luciq.library:luciq:<FETCHED_VERSION>")
    implementation("ai.luciq.library:luciq-apm:<FETCHED_VERSION>")
}

// build.gradle (Groovy)
dependencies {
    implementation 'ai.luciq.library:luciq:<FETCHED_VERSION>'
    implementation 'ai.luciq.library:luciq-apm:<FETCHED_VERSION>'
}
```

**Maven (If `integration_method == maven`):**

```xml
<dependency>
    <groupId>ai.luciq.library</groupId>
    <artifactId>luciq</artifactId>
    <version><FETCHED_VERSION></version>
</dependency>

<!-- IF apm_enabled -->
<dependency>
    <groupId>ai.luciq.library</groupId>
    <artifactId>luciq-apm</artifactId>
    <version><FETCHED_VERSION></version>
</dependency>
```

**Automatic Permissions:** SDK adds these to AndroidManifest.xml automatically:

```xml
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.WAKE_LOCK"/>
```

***

### Step 3 — Initialize the SDK **\[MANDATORY]**

> 📋 **Workflow:** See [common-workflow.md - Step 3](https://github.com/luciqai/luciq-docs/blob/main/android/set-up-luciq-for-android/integrate-luciq-on-android/common-workflow.md#step-3--initialize-the-sdk-mandatory---platform-specific)

#### Android Implementation

**⚠️ IMPORTANT:** The SDK initialization MUST be the FIRST code executed in `onCreate()` (immediately after `super.onCreate()`). This ensures Luciq captures all app activity from the very start.

**Part A: Detect or Create Application Class**

**Search for Existing Application Class:**

```
1. Search project for classes extending Application
2. Check AndroidManifest.xml for android:name in <application> tag

IF Application class found:
    Store application_class_path and application_class_name
    Inform user: "Found existing Application class: <name>"
ELSE:
    Inform user: "No Application class found - will create MyApplication"
    Set application_class_name = "MyApplication"
END IF
```

**Part B: Initialize Luciq SDK**

**If NO existing Application class - Create new:**

```kotlin
package com.yourpackage // Use detected package

import android.app.Application
import ai.luciq.library.Luciq
import ai.luciq.library.invocation.LuciqInvocationEvent

class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // ⚠️ MUST be FIRST - Initialize Luciq immediately after super.onCreate()
        Luciq.Builder(this, "<APP_TOKEN>")
            .setInvocationEvents(<EVENTS>)
            .build()

        // Other initialization code goes AFTER Luciq initialization
        // ...
    }
}
```

**Then register in AndroidManifest.xml:**

```xml
<application
    android:name=".MyApplication"
    android:icon="@mipmap/ic_launcher"
    android:label="@string/app_name">
    <!-- ... activities ... -->
</application>
```

**If existing Application class - Update onCreate():**

```kotlin
import ai.luciq.library.Luciq
import ai.luciq.library.invocation.LuciqInvocationEvent

class <ExistingApplicationClass> : Application() {
    override fun onCreate() {
        super.onCreate()

        // ⚠️ MUST be FIRST - Initialize Luciq immediately after super.onCreate()
        Luciq.Builder(this, "<APP_TOKEN>")
            .setInvocationEvents(<EVENTS>)
            .build()

        // Existing initialization code goes AFTER Luciq initialization
        // ...
    }
}
```

#### Part C: APM Configuration (If `config_mode == default` OR `apm_enabled == true`)

**If APM is enabled, configure APM plugin in build.gradle:**

**⚠️ IMPORTANT:** The APM plugin's `networkEnabled` captures network data for APM performance monitoring only. You MUST still add the OkHttp interceptor manually (see Optional Step 1) for network logs to appear in bug reports.

```kotlin
// In app-level build.gradle.kts
luciq {
    apm {
        // Network performance monitoring (for APM only, not bug reports)
        networkEnabled = true

        IF config_mode == default:
          captureHttpBodyEnabled = true  // Capture HTTP body for performance data

        // Fragment span tracking
        fragmentSpansEnabled = true

        // Additional APM settings (for custom mode)
        // autoUITraceEnabled = true
    }

    // Optional: Enable debug logs
    // setDebugLogsEnabled(true)
}

// In app-level build.gradle (Groovy)
luciq {
    apm {
        networkEnabled = true
        IF config_mode == default:
          captureHttpBodyEnabled = true

        fragmentSpansEnabled = true
    }
}
```

**Note:** Network logging is handled automatically by the unified network interception. Enable it in the `luciq` block with `networkInterception { enabled = true }`.

**Invocation Events Syntax:**

**Default invocation events:** `SHAKE, FLOATING_BUTTON`

```kotlin
// Default mode: shake + floatingButton (applied automatically)
.setInvocationEvents(
    LuciqInvocationEvent.SHAKE,
    LuciqInvocationEvent.FLOATING_BUTTON
)

// If user customized - other options:

// Screenshot only
.setInvocationEvents(LuciqInvocationEvent.SCREENSHOT)

// All events
.setInvocationEvents(
    LuciqInvocationEvent.SHAKE,
    LuciqInvocationEvent.SCREENSHOT,
    LuciqInvocationEvent.FLOATING_BUTTON
)

// None (manual only) - omit setInvocationEvents()
```

**Available Events:**

* `LuciqInvocationEvent.SHAKE` - Device shake
* `LuciqInvocationEvent.SCREENSHOT` - Screenshot capture
* `LuciqInvocationEvent.FLOATING_BUTTON` - Floating button overlay
* `LuciqInvocationEvent.NONE` - Manual only

***

### Step 3B — Configure Network Interception **\[MANDATORY]**

#### Android Implementation (Unified Network Interception)

**Minimum SDK Version:** 19.0.0+

**The Luciq Gradle Plugin automatically instruments OkHttp and UrlConnection networking libraries.** No manual interceptor setup required!

***

#### Configuration Settings

| Setting                                   | Default | Description                         |
| ----------------------------------------- | ------- | ----------------------------------- |
| `networkInterception.enabled`             | false   | Master switch for interception      |
| `okHttp.enabled`                          | true    | OkHttp automatic integration        |
| `urlConnection.enabled`                   | true    | UrlConnection automatic integration |
| `okHttp.legacyApmInterceptionEnabled`     | true    | APM legacy interceptor fallback     |
| `urlConnection.legacyInterceptionEnabled` | true    | Core legacy interceptor fallback    |

***

#### Part A: Enable Network Interception (Gradle Plugin)

**Kotlin DSL (build.gradle.kts):**

```kotlin
luciq {
    networkInterception {
        enabled = true
        // Disable legacy interceptors to avoid potential crashes
        okHttp { config ->
            config.enabled = true
            config.legacyApmInterceptionEnabled = false
        }
        urlConnection { config ->
            config.enabled = true
            config.legacyInterceptionEnabled = false
        }
    }
}
```

**Groovy (build.gradle):**

```groovy
luciq {
    networkInterception {
        enabled = true
        // Disable legacy interceptors to avoid potential crashes
        okHttp { config ->
            config.enabled = true
            config.legacyApmInterceptionEnabled = false
        }
        urlConnection { config ->
            config.enabled = true
            config.legacyInterceptionEnabled = false
        }
    }
}
```

**Note:** Legacy interceptors will be removed in a future major release. Disabling them now ensures smooth future upgrades.

***

#### Part B: Selective Library Instrumentation (Optional)

If you need to disable instrumentation for specific libraries:

```kotlin
luciq {
    networkInterception {
        enabled = true
        okHttp { config ->
            config.enabled = false  // Disable OkHttp instrumentation
        }
        urlConnection { config ->
            config.enabled = false  // Disable UrlConnection instrumentation
        }
    }
}
```

***

#### Part C: Mask Sensitive Data

**Use the centralized `Luciq.setNetworkLogListener` for all captured logs:**

```kotlin
import ai.luciq.library.Luciq
import org.json.JSONObject
import org.json.JSONArray

// Configure in Application class after Luciq.Builder().build()

// Predefined for default mode, or custom based on user input
val headersToMask = listOf("Authorization", "Cookie", "X-API-Key", "token")
val bodyFieldsToMask = setOf("password", "token", "ssn")

Luciq.setNetworkLogListener { snapshot ->
    // Mask sensitive headers with ***** (preserves header presence)
    headersToMask.forEach { header ->
        if (snapshot.requestHeaders.containsKey(header)) {
            snapshot.requestHeaders[header] = "*****"
        }
        snapshot.responseHeaders?.let { headers ->
            if (headers.containsKey(header)) {
                headers[header] = "*****"
            }
        }
    }

    // Mask request body fields recursively
    snapshot.requestBody?.let { body ->
        snapshot.requestBody = maskJsonFields(body, bodyFieldsToMask)
    }

    // Mask response body fields recursively
    snapshot.responseBody?.let { body ->
        snapshot.responseBody = maskJsonFields(body, bodyFieldsToMask)
    }

    snapshot  // Return modified snapshot, or null to exclude log entirely
}

// Recursive helper to mask fields at any depth
private fun maskJsonFields(jsonString: String, fieldsToMask: Set<String>): String {
    return try {
        val jsonObject = JSONObject(jsonString)
        maskJsonObject(jsonObject, fieldsToMask).toString()
    } catch (e: Exception) {
        jsonString  // Return original if not valid JSON
    }
}

private fun maskJsonObject(obj: JSONObject, fieldsToMask: Set<String>): JSONObject {
    val result = JSONObject()
    obj.keys().forEach { key ->
        result.put(key, when {
            fieldsToMask.contains(key) -> "*****"
            else -> when (val value = obj.get(key)) {
                is JSONObject -> maskJsonObject(value, fieldsToMask)
                is JSONArray -> maskJsonArray(value, fieldsToMask)
                else -> value
            }
        })
    }
    return result
}

private fun maskJsonArray(arr: JSONArray, fieldsToMask: Set<String>): JSONArray {
    val result = JSONArray()
    for (i in 0 until arr.length()) {
        result.put(when (val value = arr.get(i)) {
            is JSONObject -> maskJsonObject(value, fieldsToMask)
            is JSONArray -> maskJsonArray(value, fieldsToMask)
            else -> value
        })
    }
    return result
}
```

**Key Points:**

* Headers: Mask with "\*\*\*\*\*" (preserves header presence for debugging)
* Body fields: Recursive masking at any depth using Set for O(1) lookup
* Return `null` to exclude log entirely

***

### Step 4 — Mask Repro Step Screenshots **\[MANDATORY]**

> 📋 **Workflow:** See [common-workflow.md - Optional Step 1](https://github.com/luciqai/luciq-docs/blob/main/android/set-up-luciq-for-android/integrate-luciq-on-android/common-workflow.md#optional-step-1--mask-repro-step-screenshots)

#### Android Implementation

**Minimum SDK Version:** 11.13.0

**Check Configuration Mode:**

```
IF config_mode == default:
  Apply all masking types automatically:
    Luciq.setAutoMaskScreenshotsTypes(MaskingType.TEXT_INPUTS, MaskingType.LABELS, MaskingType.MEDIA)
ELSE IF config_mode == custom:
  Ask user for masking preferences
END IF
```

```kotlin
import ai.luciq.library.Luciq
import ai.luciq.library.MaskingType

// Default mode: All types (maximum privacy)
IF config_mode == default:
  Luciq.setAutoMaskScreenshotsTypes(
      MaskingType.TEXT_INPUTS,
      MaskingType.LABELS,
      MaskingType.MEDIA
  )

// Custom mode options:
ELSE IF config_mode == custom:
  // Text inputs only
  Luciq.setAutoMaskScreenshotsTypes(MaskingType.TEXT_INPUTS)

  // Text inputs + labels
  Luciq.setAutoMaskScreenshotsTypes(
      MaskingType.TEXT_INPUTS,
      MaskingType.LABELS
  )

  // Text inputs + labels + media
  Luciq.setAutoMaskScreenshotsTypes(
      MaskingType.TEXT_INPUTS,
      MaskingType.LABELS,
      MaskingType.MEDIA
  )

  // Labels only
  Luciq.setAutoMaskScreenshotsTypes(MaskingType.LABELS)

  // Media only
  Luciq.setAutoMaskScreenshotsTypes(MaskingType.MEDIA)

  // Disable auto masking
  Luciq.setAutoMaskScreenshotsTypes(MaskingType.MASK_NOTHING)
END IF
```

**Build-time Configuration (Alternative):**

```kotlin
// In Application class onCreate()
Luciq.Builder(this, "APP_TOKEN")
    .setAutoMaskScreenshotsTypes(MaskingType.TEXT_INPUTS, MaskingType.LABELS)
    .build()
```

**Additional Privacy Controls:**

```kotlin
// Mark specific views as private (takes precedence over auto masking)
Luciq.addPrivateViews(view1, view2, view3)

// Remove from private list
Luciq.removePrivateViews(view1, view2, view3)
```

**Available Masking Types:**

* `MaskingType.TEXT_INPUTS` - EditText, TextInputLayout, text input fields
* `MaskingType.LABELS` - TextView, Button text, labels, titles
* `MaskingType.MEDIA` - ImageView, VideoView, images and video
* `MaskingType.MASK_NOTHING` - Disable all auto masking

**Key Notes:**

* Private Views API takes precedence over Auto Masking
* Works with Bug Reporting, Crash Reporting, and Session Replay
* Screenshots are disabled by default for Crash Reporting

***

### Step 5 — Upload Mapping Files **\[MANDATORY]**

> 📋 **Workflow:** See [common-workflow.md - Step 6](https://github.com/luciqai/luciq-docs/blob/main/android/set-up-luciq-for-android/integrate-luciq-on-android/common-workflow.md#step-6--upload-symbolication-files-mandatory)

#### Android Implementation

**This step is required for readable crash reports.**

**Purpose:** Upload ProGuard/R8 mapping files for crash symbolication.

**Part A: Create Upload Script**

Create `upload_mapping.sh` in your project root:

```shell
#!/bin/bash
echo "Luciq mapping files uploader"

APP_TOKEN="$1"
VERSION_CODE="$2"
VERSION_NAME="$3"
PATH_TO_MAPPING_FILE="$4"
VERSION='{"code":"'"$VERSION_CODE"'","name":"'"$VERSION_NAME"'"}'

if [ ! -f "$PATH_TO_MAPPING_FILE" ]; then
    echo "Mapping file not found!"
    exit 0
fi

echo "Mapping file found! Uploading..."

ENDPOINT="https://api.luciq.ai/api/sdk/v3/symbols_files"
STATUS=$(curl "${ENDPOINT}" --write-out %{http_code} --silent --output /dev/null \
    -F os=android \
    -F app_version="${VERSION}" \
    -F symbols_file=@"${PATH_TO_MAPPING_FILE}" \
    -F application_token="${APP_TOKEN}")

if [ $STATUS -ne 200 ]; then
  echo "Error while uploading mapping files"
  exit 0
fi

echo "Success! Your mapping files got uploaded successfully"
```

**Part B: Add Gradle Task**

Add to your app's `build.gradle` or `build.gradle.kts`:

**Kotlin DSL (build.gradle.kts):**

```kotlin
tasks.register<Exec>("uploadMappingFiles") {
    android.applicationVariants.all {
        if (buildType.name == "release" && mappingFileProvider.isPresent) {
            val mappingFile = mappingFileProvider.get().singleFile
            if (mappingFile.exists()) {
                commandLine(
                    "sh",
                    "../upload_mapping.sh",
                    "<APP_TOKEN>",  // Use token from Step 1A
                    versionCode.toString(),
                    versionName,
                    mappingFile.absolutePath
                )
            }
        }
    }
}
```

**Groovy (build.gradle):**

```groovy
task uploadMappingFiles(type: Exec) {
    android.applicationVariants.all { variant ->
        if (variant.buildType.name == "release" && variant.mappingFile != null && variant.mappingFile.exists()) {
            commandLine 'sh', '../upload_mapping.sh',
                '<APP_TOKEN>',  // Use token from Step 1A
                variant.versionCode,
                variant.versionName,
                variant.mappingFile
        }
    }
}
```

**Part C: Run After Release Build**

```bash
./gradlew assembleRelease
./gradlew :app:uploadMappingFiles
```

**Alternative: Manual Dashboard Upload**

1. Navigate to **Upload Mapping Files** in your Luciq dashboard Settings
2. Upload your `mapping.txt` file (found in `app/build/outputs/mapping/release/`)
3. Upload for each release version

***

### 🛑 MANDATORY STEPS COMPLETE

***

### Optional Step 1 — Configure Repro Steps Mode

> 📋 **Workflow:** See [common-workflow.md - Optional Step 1](https://github.com/luciqai/luciq-docs/blob/main/android/set-up-luciq-for-android/integrate-luciq-on-android/common-workflow.md#optional-step-1--configure-repro-steps-mode)

#### Android Implementation

**Based on user selections, apply configuration:**

```kotlin
// Example: User selected Bug Reporting and Session Replay (1,3)
val configurations = ReproConfigurations.Builder()
    .setIssueMode(IssueType.Bug, ReproMode.EnableWithScreenshots)
    .setIssueMode(IssueType.SessionReplay, ReproMode.EnableWithScreenshots)
    .setIssueMode(IssueType.AllCrashes, ReproMode.EnableWithNoScreenshots)  // Not selected
    .build()

Luciq.setReproConfigurations(configurations)

// Example: User selected All products (4)
val allConfig = ReproConfigurations.Builder()
    .setIssueMode(IssueType.All, ReproMode.EnableWithScreenshots)
    .build()

Luciq.setReproConfigurations(allConfig)

// Example: User selected only Crash Reporting (2)
val crashOnlyConfig = ReproConfigurations.Builder()
    .setIssueMode(IssueType.AllCrashes, ReproMode.EnableWithScreenshots)
    .setIssueMode(IssueType.Bug, ReproMode.EnableWithNoScreenshots)  // Not selected
    .setIssueMode(IssueType.SessionReplay, ReproMode.EnableWithNoScreenshots)  // Not selected
    .build()

Luciq.setReproConfigurations(crashOnlyConfig)

// Example: User selected None (5)
val noneConfig = ReproConfigurations.Builder()
    .setIssueMode(IssueType.All, ReproMode.EnableWithNoScreenshots)
    .build()

Luciq.setReproConfigurations(noneConfig)
```

**Issue Type Options:**

* `IssueType.Bug` - Bug Reporting
* `IssueType.AllCrashes` - Crash Reporting
* `IssueType.SessionReplay` - Session Replay
* `IssueType.All` - All products

**Key Points:**

* Selected products → `ReproMode.EnableWithScreenshots`
* Non-selected products → `ReproMode.EnableWithNoScreenshots`

***

### Optional Step 2 — Add User Identification

> 📋 **Workflow:** See [common-workflow.md - Optional Step 2](https://github.com/luciqai/luciq-docs/blob/main/android/set-up-luciq-for-android/integrate-luciq-on-android/common-workflow.md#optional-step-2--add-user-identification)

#### Android Implementation - Login Flow

```kotlin
import ai.luciq.library.Luciq

class AuthManager {
    fun signIn(email: String, password: String): Boolean {
        // ... authentication logic ...

        if (authenticationSuccessful) {
            // Identify user AFTER successful auth, BEFORE navigation
            Luciq.identifyUser(
                user.name,   // name (can be null)
                user.email,  // email (can be null)
                user.id      // id (can be null)
            )

            isAuthenticated = true
            return true
        }

        return false
    }
}
```

**API Signature:**

```kotlin
Luciq.identifyUser(
    name: String?,   // Required parameter, can be null
    email: String?,  // Required parameter, can be null
    id: String?      // Required parameter, can be null
)
```

**⚠️ CRITICAL:** At least email OR id must be non-null. All null throws error.

**Examples:**

* Email only: `Luciq.identifyUser(user.name, user.email, null)`
* ID only: `Luciq.identifyUser(user.name, null, user.id)`
* Both: `Luciq.identifyUser(user.name, user.email, user.id)`

**Additional User Data (optional):**

```kotlin
// Set additional user context (max 1000 chars)
Luciq.setUserData("Premium user, subscription: pro")
```

#### Android Implementation - Logout Flow

```kotlin
class AuthManager {
    fun logout() {
        // Call Luciq logout BEFORE clearing session
        Luciq.logoutUser()

        // Then clear user data
        currentUser = null
        isAuthenticated = false
        sharedPreferences.edit().clear().apply()
    }
}
```

**Note:** `logoutUser()` only works if user was previously identified

***

### Step 6 — Verification & Testing **\[WRAP UP & VALIDATE]**

> 📋 **Workflow:** See [common-workflow.md - Step 7](https://github.com/luciqai/luciq-docs/blob/main/android/set-up-luciq-for-android/integrate-luciq-on-android/common-workflow.md#step-7--verification--testing-wrap-up--validate-user-initiated-only)

#### Android Build Verification

```bash
./gradlew assembleDebug
```

**Expected:** `BUILD SUCCESSFUL`

**Android-Specific Build Errors:**

| Error                         | Cause               | Fix                             |
| ----------------------------- | ------------------- | ------------------------------- |
| `compileSdkVersion < 29`      | SDK too old         | Set `compileSdkVersion` to 29+  |
| `Unresolved reference: Luciq` | Missing dependency  | Sync gradle, verify version     |
| `Duplicate class`             | Dependency conflict | Check: `./gradlew dependencies` |

#### Android Runtime Testing

1. Install and run:

   ```bash
   ./gradlew installDebug
   ```
2. Trigger Luciq:
   * Shake: Shake device/emulator
   * Screenshot: Power + Volume Down
   * Floating Button: Tap button overlay
3. Verify Luciq UI appears
4. Submit test report
5. Check dashboard: <https://dashboard.luciq.ai>

***

### Android-Specific Troubleshooting

#### Issue: "compileSdkVersion must be >= 29"

**Fix:** Update `build.gradle`:

```kotlin
android {
    compileSdkVersion = 34  // or higher
}
```

#### Issue: Network logs not appearing

**Fix:** Enable unified network interception in `luciq { networkInterception { enabled = true } }`

#### Issue: Application class not registered

**Fix:** Add `android:name=".MyApplication"` to `<application>` tag in manifest

#### Issue: User identification error

**Fix:** Ensure at least email OR id is non-null (not both null)

#### Issue: Screenshots not masking

**Fix:** Use `setAutoMaskScreenshotsTypes(MaskingType.TEXT_INPUTS, MaskingType.LABELS)`

***

### Quick Reference

```kotlin
// IMPORTS
import ai.luciq.library.Luciq
import ai.luciq.library.invocation.LuciqInvocationEvent
import ai.luciq.library.MaskingType

// INITIALIZATION (in Application class - default: shake + floatingButton)
Luciq.Builder(this, "APP_TOKEN")
    .setInvocationEvents(LuciqInvocationEvent.SHAKE, LuciqInvocationEvent.FLOATING_BUTTON)
    .build()

// NETWORK INTERCEPTION (in build.gradle.kts - MANDATORY)
luciq {
    networkInterception {
        enabled = true
        okHttp { config ->
            config.legacyApmInterceptionEnabled = false
        }
        urlConnection { config ->
            config.legacyInterceptionEnabled = false
        }
    }
}

// NETWORK LOG MASKING (in Application class after Luciq.Builder().build())
Luciq.setNetworkLogListener { snapshot ->
    // Mask headers with *****
    listOf("Authorization", "Cookie").forEach { header ->
        if (snapshot.requestHeaders.containsKey(header)) {
            snapshot.requestHeaders[header] = "*****"
        }
    }
    snapshot  // Return modified snapshot, or null to exclude
}

// USER IDENTIFICATION
Luciq.identifyUser(user.name, user.email, user.id)  // At least email or id non-null

// USER DATA
Luciq.setUserData("Additional context")

// LOGOUT
Luciq.logoutUser()

// SCREENSHOT AUTO MASKING
Luciq.setAutoMaskScreenshotsTypes(MaskingType.TEXT_INPUTS, MaskingType.LABELS)

// PRIVATE VIEWS
Luciq.addPrivateViews(view1, view2)
```

***

### Java Equivalents

All Kotlin examples have straightforward Java equivalents:

* `val` → `final`
* Lambda `{ }` → Anonymous inner class
* `?.let` → null check with `if`
* Extension functions → Static utility methods

Refer to official docs for Java examples if needed.
