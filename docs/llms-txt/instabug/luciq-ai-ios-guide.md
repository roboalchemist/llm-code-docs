# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/integrate-luciq-on-ios/luciq-ai-ios-guide.md

# Guide for AI Coding Agents to Integrate Luciq on iOS

## Guide for AI Coding Agents to Integrate Luciq on iOS

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

## Luciq SDK Integration - iOS Guide

> **Purpose:** iOS-specific implementation details for Luciq SDK integration. This guide provides iOS-specific code, configuration, and platform requirements.

***

### ⚠️ iOS-SPECIFIC CRITICAL RULES ⚠️

#### Package vs Import Naming (MUST FOLLOW):

1. **SPM Package Product Name**: Use "Luciq" (in project.pbxproj, Podfile, etc.)
2. **Swift Import Statement**: ALWAYS use `import LuciqSDK` (NOT `import Luciq`)
3. **Why Different?**: The binary XCFramework is named "LuciqSDK.framework" internally
4. **If Build Fails** with "no such module 'Luciq'": You forgot to use `import LuciqSDK`

#### iOS-Specific Execution Rules:

* Network logging code goes AFTER `Luciq.start()`
* ALL API parameters must be included (can be `nil`) - never omit parameters
* Use `exact` for SPM version requirement (not `upToNextMajorVersion`)
* Place SDK initialization in AppDelegate or main App struct's `init()`

#### Official iOS Documentation:

* iOS Integration: <https://docs.luciq.ai/docs/ios-integration>
* iOS User Identification: <https://docs.luciq.ai/docs/ios-identify-user>
* iOS Screenshot Masking: <https://docs.luciq.ai/docs/product-guides-reprosteps-and-automasking>

***

***

## IOS-SPECIFIC IMPLEMENTATION DETAILS

***

### Pre-Integration Checklist

Before starting, verify you understand these iOS-specific points:

* [ ] Package product is "Luciq" but import is `import LuciqSDK`
* [ ] **SPM requires updating BOTH `Package.swift` AND `project.pbxproj`** - updating only one is insufficient
* [ ] **SDK initialization MUST be the FIRST line** in init()/didFinishLaunchingWithOptions
* [ ] **Network logging is MANDATORY** - configure masking AFTER `Luciq.start()`
* [ ] **Screenshot masking is MANDATORY** - configure after SDK initialization
* [ ] **dSYM upload is MANDATORY** - add Run Script Build Phase to `project.pbxproj` (if no Fastlane)
* [ ] Use `exact` for SPM (not range)
* [ ] Build errors about "no such module" mean wrong import
* [ ] ALL parameters in API calls are required (can be `nil`)

***

### Step 1 — Collect Required Information **\[MANDATORY]**

> 📋 **Workflow:** See [common-workflow.md - Step 1](https://github.com/luciqai/luciq-docs/blob/main/ios/setup-luciq-for-ios/integrate-luciq-on-ios/common-workflow.md#step-1--collect-required-information-mandatory)

#### iOS-Specific Implementation

**Package Manager Detection:**

Check for:

* `Podfile` → CocoaPods
* `Cartfile` → Carthage
* `.xcodeproj` with SPM packages → SPM
* None → Manual

**Integration Method Menu (if multiple/none detected):**

1. Swift Package Manager (SPM) \[Recommended]
2. CocoaPods
3. Carthage
4. Manual (XCFramework)

***

#### 1C: Apply Default Configuration (Inform + Opt-in)

> 📋 **Workflow:** See [common-workflow.md - Step 1C](https://github.com/luciqai/luciq-docs/blob/main/ios/setup-luciq-for-ios/integrate-luciq-on-ios/common-workflow.md#1c-apply-default-configuration-inform--opt-in)

**For iOS:**

* Default configuration is applied automatically (shake + floatingButton, network masking, etc.)
* User is informed of defaults and can opt-in to customize
* If user customizes: Use the customization loop (select → apply → redisplay → confirm)
* After configuration: Continue to Step 1D (Fastlane detection for dSYM)

***

#### 1D: Detect Fastlane for dSYM Upload

**Auto-Detection:**

```
Search for Fastlane configuration:
  - Look for Fastfile in project root or fastlane/ directory
  - Check if it contains archive/gym lanes

IF Fastlane detected:
  Store fastlane_detected = true
  Inform user: "Fastlane detected - will configure dSYM upload via Fastlane plugin"
ELSE:
  Store fastlane_detected = false
  Inform user: "Will configure dSYM upload via Xcode Archive Post-actions"
END IF

Proceed to Step 2
```

***

### Step 2 — Add the Luciq SDK Dependency **\[MANDATORY]**

> 📋 **Workflow:** See [common-workflow.md - Step 2](https://github.com/luciqai/luciq-docs/blob/main/ios/setup-luciq-for-ios/integrate-luciq-on-ios/common-workflow.md#step-2--add-sdk-dependency-mandatory---platform-specific) Fetch latest version from GitHub API: <https://api.github.com/repos/luciqai/luciq-ios-sdk/releases/latest>

#### iOS Implementation

**⚠️ CRITICAL FOR SPM INTEGRATION:** When adding the SDK via SPM, you MUST update BOTH files:

1. `Package.swift` - Add the package dependency and product
2. `project.pbxproj` - Add all SPM-related entries (package reference, product dependency, framework link)

Updating only Package.swift is NOT sufficient - the Xcode project file must also be modified for the SDK to be recognized.

**If `integration_method == spm`:**

**Option A: Via Xcode UI (Manual - for reference only)**

1. File → Add Package Dependencies...
2. Enter URL: `https://github.com/luciqai/luciq-ios-sdk`
3. Select "Exact Version" and enter `<FETCHED_VERSION>`
4. Add "Luciq" product to your target

**Option B: Programmatic - REQUIRED for agent integration**

The agent MUST modify `project.pbxproj` directly. Add the following entries:

**1. Add to PBXBuildFile section:**

```
/* Begin PBXBuildFile section */
    <UNIQUE_ID_1> /* Luciq in Frameworks */ = {isa = PBXBuildFile; productRef = <UNIQUE_ID_2> /* Luciq */; };
    // ... existing build files ...
/* End PBXBuildFile section */
```

**2. Add to PBXFrameworksBuildPhase > files array:**

```
/* Begin PBXFrameworksBuildPhase section */
    <EXISTING_ID> /* Frameworks */ = {
        isa = PBXFrameworksBuildPhase;
        buildActionMask = 2147483647;
        files = (
            <UNIQUE_ID_1> /* Luciq in Frameworks */,
        );
        runOnlyForDeploymentPostprocessing = 0;
    };
/* End PBXFrameworksBuildPhase section */
```

**3. Add to PBXNativeTarget > packageProductDependencies array:**

```
/* Begin PBXNativeTarget section */
    <TARGET_ID> /* YourApp */ = {
        // ... other properties ...
        packageProductDependencies = (
            <UNIQUE_ID_2> /* Luciq */,
        );
        // ... other properties ...
    };
/* End PBXNativeTarget section */
```

**4. Add to PBXProject > packageReferences array:**

```
/* Begin PBXProject section */
    <PROJECT_ID> /* Project object */ = {
        // ... other properties ...
        packageReferences = (
            <UNIQUE_ID_3> /* XCRemoteSwiftPackageReference "luciq-ios-sdk" */,
        );
        // ... other properties ...
    };
/* End PBXProject section */
```

**5. Add XCRemoteSwiftPackageReference section (before closing brace):**

```
/* Begin XCRemoteSwiftPackageReference section */
    <UNIQUE_ID_3> /* XCRemoteSwiftPackageReference "luciq-ios-sdk" */ = {
        isa = XCRemoteSwiftPackageReference;
        repositoryURL = "https://github.com/luciqai/luciq-ios-sdk";
        requirement = {
            kind = exactVersion;
            version = <FETCHED_VERSION>;
        };
    };
/* End XCRemoteSwiftPackageReference section */
```

**6. Add XCSwiftPackageProductDependency section (before closing brace):**

```
/* Begin XCSwiftPackageProductDependency section */
    <UNIQUE_ID_2> /* Luciq */ = {
        isa = XCSwiftPackageProductDependency;
        package = <UNIQUE_ID_3> /* XCRemoteSwiftPackageReference "luciq-ios-sdk" */;
        productName = Luciq;
    };
/* End XCSwiftPackageProductDependency section */
```

**ID Generation Notes:**

* Use unique 24-character hexadecimal IDs (e.g., `A10017001A000000000000001`)
* IDs must be unique within the project file
* Follow the existing ID format pattern in the project

**Also update Package.swift (if present):**

```swift
// In Package.swift dependencies array:
dependencies: [
    .package(url: "https://github.com/luciqai/luciq-ios-sdk", exact: "<FETCHED_VERSION>")
],

// In target dependencies:
.target(
    name: "YourTarget",
    dependencies: [
        .product(name: "Luciq", package: "luciq-ios-sdk")
    ]
)
```

**If `integration_method == cocoapods`:**

```ruby
# In Podfile:
pod 'Luciq', '~> <MAJOR_VERSION>'  # e.g., '~> 19.0'

# Then run:
pod install
```

**If `integration_method == carthage`:**

```
# In Cartfile:
binary "https://raw.githubusercontent.com/luciqai/luciq-ios-sdk/main/Luciq.json"

# Then run:
carthage update --platform iOS
```

**If `integration_method == manual`:**

```
1. Download: https://github.com/luciqai/luciq-ios-sdk/releases/latest/download/Luciq-XCFramework.zip
2. Unzip to reveal Luciq.xcframework
3. Drag into Xcode project → Frameworks, Libraries, and Embedded Content
4. Select "Embed & Sign"
```

***

### Step 3 — Initialize the SDK **\[MANDATORY]**

> 📋 **Workflow:** See [common-workflow.md - Step 3](https://github.com/luciqai/luciq-docs/blob/main/ios/setup-luciq-for-ios/integrate-luciq-on-ios/common-workflow.md#step-3--initialize-the-sdk-mandatory---platform-specific)

#### iOS Implementation

**⚠️ CRITICAL:** ALWAYS use `import LuciqSDK` (not `import Luciq`)

**Where to place:**

* **SwiftUI**: App struct's `init()` - **AS THE FIRST LINE**
* **UIKit**: AppDelegate's `application(_:didFinishLaunchingWithOptions:)` - **AS THE FIRST LINE**

**⚠️ IMPORTANT:** The SDK initialization MUST be the FIRST code executed in the init method, before any other initialization code. This ensures Luciq captures all app activity from the very start.

**Option 1: SwiftUI App**

```swift
import SwiftUI
import LuciqSDK  // ← CRITICAL: Import is LuciqSDK, not Luciq

@main
struct YourApp: App {
    init() {
        // ⚠️ MUST be FIRST - Initialize Luciq before any other code
        Luciq.start(withToken: "<APP_TOKEN>", invocationEvents: <EVENTS>)

        // Other initialization code goes AFTER Luciq.start()
        // ...
    }

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

**Option 2: UIKit App (AppDelegate)**

```swift
import UIKit
import LuciqSDK  // ← CRITICAL: Import is LuciqSDK, not Luciq

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // ⚠️ MUST be FIRST - Initialize Luciq before any other code
        Luciq.start(withToken: "<APP_TOKEN>", invocationEvents: <EVENTS>)

        // Other initialization code goes AFTER Luciq.start()
        // ...

        return true
    }

    // ... rest of AppDelegate methods ...
}
```

**Invocation Events Syntax:**

**Default invocation events:** `[.shake, .floatingButton]`

```swift
// Default mode: shake + floatingButton (applied automatically)
Luciq.start(withToken: "<APP_TOKEN>", invocationEvents: [.shake, .floatingButton])

// If user customized - other options:

// Screenshot only
Luciq.start(withToken: "<APP_TOKEN>", invocationEvents: [.screenshot])

// All events
Luciq.start(withToken: "<APP_TOKEN>", invocationEvents: [.shake, .screenshot, .floatingButton])

// None (manual only)
Luciq.start(withToken: "<APP_TOKEN>", invocationEvents: [])
```

**Note:** The class name is `Luciq` but the import is `LuciqSDK`

***

#### Step 3B: Add Info.plist Permissions

**Required permissions for Luciq features (voice notes, image attachments):**

**First, fetch the app name:**

```
1. Read Info.plist for CFBundleDisplayName or CFBundleName
2. If not found, check project.pbxproj for PRODUCT_NAME
3. Store as <APP_NAME>
```

**Add to Info.plist if not present:**

```xml
<key>NSMicrophoneUsageDescription</key>
<string><APP_NAME> needs access to your microphone so you can attach voice notes.</string>
<key>NSPhotoLibraryUsageDescription</key>
<string><APP_NAME> needs access to your photo library so you can attach images.</string>
```

**Example (if app name is "MyApp"):**

```xml
<key>NSMicrophoneUsageDescription</key>
<string>MyApp needs access to your microphone so you can attach voice notes.</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>MyApp needs access to your photo library so you can attach images.</string>
```

**Implementation:**

```
1. Locate Info.plist file in project
2. Check if NSMicrophoneUsageDescription exists
   - If not, add it with the app name prefix
3. Check if NSPhotoLibraryUsageDescription exists
   - If not, add it with the app name prefix
4. Inform user of added permissions
```

***

### Step 4 — Configure Network Logging **\[MANDATORY]**

> 📋 **Workflow:** See [common-workflow.md - Step 4](https://github.com/luciqai/luciq-docs/blob/main/ios/setup-luciq-for-ios/integrate-luciq-on-ios/common-workflow.md#step-4--configure-network-logging-mandatory)

#### iOS Implementation

**Check Configuration Mode:**

```
IF config_mode == default:
  Network logging is enabled by default
  Apply predefined masking with:
    - Headers: ["Authorization", "Cookie", "X-API-Key", "token"]
    - Body fields: ["password", "token", "ssn"]
ELSE IF config_mode == custom:
  Ask user for network logging preferences
END IF
```

**Disable Automatic Capture (call BEFORE Luciq.start()) - Custom Mode Only:**

```swift
NetworkLogger.disableAutomaticCapturingOfNetworkLogs()
```

**Mask Sensitive Data (call AFTER Luciq.start()):**

**Option 1: SwiftUI App**

```swift
import SwiftUI
import LuciqSDK

@main
struct YourApp: App {
    init() {
        // Step 1: Initialize SDK first
        Luciq.start(withToken: "<APP_TOKEN>", invocationEvents: [.floatingButton])

        // Step 2: Configure network masking AFTER start
        configureNetworkMasking()
    }

    private func configureNetworkMasking() {
        // Define fields based on config_mode
        let headersToMask: [String] = IF config_mode == default:
            ["Authorization", "Cookie", "X-API-Key", "token"]  // Predefined for default mode
        ELSE:
            ["Authorization", "Cookie", "X-API-Key"]  // Custom user input

        let bodyFieldsToMask: Set<String> = IF config_mode == default:
            ["password", "token", "ssn"]  // Predefined for default mode
        ELSE:
            ["password", "token", "ssn", "uuid"]  // Custom user input

        NetworkLogger.setRequestObfuscationHandler { request in
            var mutableRequest = (request as NSURLRequest).mutableCopy() as! NSMutableURLRequest

            // Mask headers using loop
            for header in headersToMask {
                if mutableRequest.value(forHTTPHeaderField: header) != nil {
                    mutableRequest.setValue("*****", forHTTPHeaderField: header)
                }
            }

            // Mask body fields using recursive function
            if let body = mutableRequest.httpBody,
               let jsonObject = try? JSONSerialization.jsonObject(with: body) {
                let maskedObject = Self.maskFields(in: jsonObject, fieldsToMask: bodyFieldsToMask)
                if let newBody = try? JSONSerialization.data(withJSONObject: maskedObject) {
                    mutableRequest.httpBody = newBody
                }
            }

            return mutableRequest.copy() as! URLRequest
        }
    }

    // Recursive helper to mask fields at any depth
    private static func maskFields(in object: Any, fieldsToMask: Set<String>) -> Any {
        if var dictionary = object as? [String: Any] {
            for (key, value) in dictionary {
                if fieldsToMask.contains(key) {
                    dictionary[key] = "*****"
                } else if value is [String: Any] || value is [Any] {
                    dictionary[key] = maskFields(in: value, fieldsToMask: fieldsToMask)
                }
            }
            return dictionary
        } else if let array = object as? [Any] {
            return array.map { maskFields(in: $0, fieldsToMask: fieldsToMask) }
        }
        return object
    }

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

**Option 2: UIKit App (AppDelegate)**

```swift
import UIKit
import LuciqSDK

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Step 1: Initialize SDK first
        Luciq.start(withToken: "<APP_TOKEN>", invocationEvents: [.floatingButton])

        // Step 2: Configure network masking AFTER start
        configureNetworkMasking()

        return true
    }

    private func configureNetworkMasking() {
        // Define fields based on config_mode
        let headersToMask: [String] = IF config_mode == default:
            ["Authorization", "Cookie", "X-API-Key", "token"]  // Predefined for default mode
        ELSE:
            ["Authorization", "Cookie", "X-API-Key"]  // Custom user input

        let bodyFieldsToMask: Set<String> = IF config_mode == default:
            ["password", "token", "ssn"]  // Predefined for default mode
        ELSE:
            ["password", "token", "ssn", "uuid"]  // Custom user input

        NetworkLogger.setRequestObfuscationHandler { request in
            var mutableRequest = (request as NSURLRequest).mutableCopy() as! NSMutableURLRequest

            // Mask headers using loop
            for header in headersToMask {
                if mutableRequest.value(forHTTPHeaderField: header) != nil {
                    mutableRequest.setValue("*****", forHTTPHeaderField: header)
                }
            }

            // Mask body fields using recursive function
            if let body = mutableRequest.httpBody,
               let jsonObject = try? JSONSerialization.jsonObject(with: body) {
                let maskedObject = self.maskFields(in: jsonObject, fieldsToMask: bodyFieldsToMask)
                if let newBody = try? JSONSerialization.data(withJSONObject: maskedObject) {
                    mutableRequest.httpBody = newBody
                }
            }

            return mutableRequest.copy() as! URLRequest
        }
    }

    // Recursive helper to mask fields at any depth
    private func maskFields(in object: Any, fieldsToMask: Set<String>) -> Any {
        if var dictionary = object as? [String: Any] {
            for (key, value) in dictionary {
                if fieldsToMask.contains(key) {
                    dictionary[key] = "*****"
                } else if value is [String: Any] || value is [Any] {
                    dictionary[key] = maskFields(in: value, fieldsToMask: fieldsToMask)
                }
            }
            return dictionary
        } else if let array = object as? [Any] {
            return array.map { maskFields(in: $0, fieldsToMask: fieldsToMask) }
        }
        return object
    }

    // ... rest of AppDelegate methods ...
}
```

**Key Points:**

* Masking MUST be called AFTER `Luciq.start()`
* Use `Set<String>` for O(1) lookup performance
* Recursive function handles nested JSON at any depth
* For SwiftUI: Use `Self.maskFields` (static) inside init closure
* For UIKit: Use `self.maskFields` (instance) in AppDelegate

***

### Step 5 — Mask Repro Step Screenshots **\[MANDATORY]**

> 📋 **Workflow:** See [common-workflow.md - Optional Step 1](https://github.com/luciqai/luciq-docs/blob/main/ios/setup-luciq-for-ios/integrate-luciq-on-ios/common-workflow.md#optional-step-1--mask-repro-step-screenshots)

#### iOS Implementation

**Default Configuration (maskNothing with guidance):**

```swift
// Configure screenshot masking based on your app's privacy requirements
// Options: .textInputs, .labels, .media, or combine multiple types
// Example: Luciq.setAutoMaskScreenshots([.textInputs, .labels])
Luciq.setAutoMaskScreenshots(.maskNothing)  // Default: no automatic masking

// SwiftUI views are automatically masked when you change the masked types from .maskNothing
// Uncomment the line below to disable automatic SwiftUI view masking
// Luciq.autoMaskSwiftUIViews = false
```

**If user customizes masking:**

```swift
// For text inputs only:
Luciq.setAutoMaskScreenshots([.textInputs])

// For labels only:
Luciq.setAutoMaskScreenshots([.labels])

// For text inputs + labels:
Luciq.setAutoMaskScreenshots([.textInputs, .labels])

// For all types (comprehensive):
Luciq.setAutoMaskScreenshots([.textInputs, .labels, .media])

// Or use .media for comprehensive masking:
Luciq.setAutoMaskScreenshots([.media])
```

**Available iOS Mask Types:**

* `.maskNothing` - No automatic masking (default)
* `.textInputs` - UITextField, UITextView, secure text fields
* `.labels` - UILabel, UIButton text
* `.media` - Comprehensive masking (includes all types)

**SwiftUI Auto Masking:**

* When masking types are changed from `.maskNothing`, SwiftUI views are automatically masked
* To disable this behavior: `Luciq.autoMaskSwiftUIViews = false`

***

### Step 6 — Upload dSYM Files **\[MANDATORY]**

> 📋 **Workflow:** See [common-workflow.md - Step 6](https://github.com/luciqai/luciq-docs/blob/main/ios/setup-luciq-for-ios/integrate-luciq-on-ios/common-workflow.md#step-6--upload-symbolication-files-mandatory)

#### iOS Implementation

**This step is configured automatically based on Step 1D detection.**

**Option A: Fastlane Plugin (if `fastlane_detected == true`)**

First, install the Fastlane plugin:

```bash
fastlane add_plugin luciq_official
```

Then add to your Fastfile:

```ruby
# In Fastfile, add to your archive lane:
lane :archive do
  gym(
    scheme: "<SCHEME_NAME>",
    archive_path: "./build/<APP_NAME>.xcarchive"
  )
  # IMPORTANT: For local archives, you MUST specify dsym_array_paths
  # The plugin will NOT automatically find dSYMs from local archives
  luciq_official(
    api_token: "<APP_TOKEN>",
    dsym_array_paths: ["./build/<APP_NAME>.xcarchive/dSYMs/<APP_NAME>.app.dSYM"]
  )
end

# For bitcode-enabled apps or App Store Connect downloads:
# (dsym_array_paths not needed - plugin uses downloaded dSYMs automatically)
lane :refresh_dsyms do
  download_dsyms(version: "latest")
  luciq_official(api_token: "<APP_TOKEN>")
end
```

**Plugin Parameters:**

| Parameter          | Required                 | Description                          |
| ------------------ | ------------------------ | ------------------------------------ |
| `api_token`        | Yes                      | Your Luciq app token from Step 1A    |
| `dsym_array_paths` | Yes (for local archives) | Array of paths to dSYM files/folders |
| `eu`               | No                       | Set to `true` for EU data center     |
| `end_point`        | No                       | Custom API endpoint (if applicable)  |

**Common Mistake:** Omitting `dsym_array_paths` for local archives. Without this parameter, the plugin only looks for dSYMs downloaded via `download_dsyms` action and will show: "Fastlane dSYMs file is not found!"

**Option B: Run Script Build Phase (if `fastlane_detected == false`)**

**Via Xcode UI (Manual - for reference only):**

1. In Xcode: Select target → **Build Phases** → **+** → **New Run Script Phase**
2. Name it "Upload dSYM to Luciq"
3. Add the following script:

```shell
#- -- SCRIPT BEGIN - --

# SKIP_SIMULATOR_BUILDS=1

# Check PROJECT_DIR first (CocoaPods, Carthage, Manual)
SCRIPT_SRC=$(find "$PROJECT_DIR" -name 'Luciq_dsym_upload.sh' | head -1)

# If not found, check SPM location
if [ -z "$SCRIPT_SRC" ]; then
  SCRIPT_SRC=$(find "$BUILT_PRODUCTS_DIR" -name 'Luciq_dsym_upload.sh' | head -1)
fi

if [ -z "$SCRIPT_SRC" ]; then
  echo "Luciq: err: script not found. Make sure the Luciq SDK is properly installed."
  exit 1
fi

APP_TOKEN="YOUR-APP-TOKEN-HERE"
source "${SCRIPT_SRC}"
#- -- SCRIPT END - --
```

**Programmatic - REQUIRED for agent integration:**

The agent MUST modify `project.pbxproj` to add a Run Script Build Phase.

**1. Add PBXShellScriptBuildPhase section (after PBXSourcesBuildPhase, before XCBuildConfiguration):**

```
/* Begin PBXShellScriptBuildPhase section */
		<UNIQUE_ID> /* Upload dSYM to Luciq */ = {
			isa = PBXShellScriptBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			inputFileListPaths = (
			);
			inputPaths = (
			);
			name = "Upload dSYM to Luciq";
			outputFileListPaths = (
			);
			outputPaths = (
			);
			runOnlyForDeploymentPostprocessing = 0;
			shellPath = /bin/sh;
			shellScript = "#- -- SCRIPT BEGIN - --\n\n# SKIP_SIMULATOR_BUILDS=1\n\n# Check PROJECT_DIR first (CocoaPods, Carthage, Manual)\nSCRIPT_SRC=$(find \"$PROJECT_DIR\" -name 'Luciq_dsym_upload.sh' | head -1)\n\n# If not found, check SPM location\nif [ -z \"$SCRIPT_SRC\" ]; then\n  SCRIPT_SRC=$(find \"$BUILT_PRODUCTS_DIR\" -name 'Luciq_dsym_upload.sh' | head -1)\nfi\n\nif [ -z \"$SCRIPT_SRC\" ]; then\n  echo \"Luciq: err: script not found. Make sure the Luciq SDK is properly installed.\"\n  exit 1\nfi\n\nAPP_TOKEN=\"YOUR-APP-TOKEN-HERE\"\nsource \"${SCRIPT_SRC}\"\n#- -- SCRIPT END - --\n";
		};
/* End PBXShellScriptBuildPhase section */
```

**2. Add to PBXNativeTarget > buildPhases array (as the LAST item):**

```
buildPhases = (
	<EXISTING_ID> /* Sources */,
	<EXISTING_ID> /* Frameworks */,
	<EXISTING_ID> /* Resources */,
	<UNIQUE_ID> /* Upload dSYM to Luciq */,
);
```

**Shell Script Escaping Notes:**

* Use `\n` for newlines in the shellScript string
* Use `\"` for double quotes inside the string
* Use `'` for single quotes (no escaping needed)

**Important Notes:**

* The script runs automatically after each build as part of the build phases
* The `<APP_TOKEN>` should be replaced with the token from Step 1A
* Download `Luciq_dsym_upload.sh` from the Luciq dashboard if not present
* Use `exit 0` (not `exit 1`) when script is not found to avoid build failures

***

### 🛑 MANDATORY STEPS COMPLETE

***

### Optional Step 1 — Configure Repro Steps Mode

> 📋 **Workflow:** See [common-workflow.md - Optional Step 1](https://github.com/luciqai/luciq-docs/blob/main/ios/setup-luciq-for-ios/integrate-luciq-on-ios/common-workflow.md#optional-step-1--configure-repro-steps-mode)

#### iOS Implementation

**Based on user selections, apply configuration:**

```swift
// Example: User selected Bug Reporting and Session Replay (1,3)
Luciq.setReproStepsFor(.bug, with: .enable)
Luciq.setReproStepsFor(.sessionReplay, with: .enable)
Luciq.setReproStepsFor(.allCrashes, with: .enabledWithNoScreenshots)  // Not selected

// Example: User selected All products (4)
Luciq.setReproStepsFor(.all, with: .enable)

// Example: User selected only Crash Reporting (2)
Luciq.setReproStepsFor(.allCrashes, with: .enable)
Luciq.setReproStepsFor(.bug, with: .enabledWithNoScreenshots)  // Not selected
Luciq.setReproStepsFor(.sessionReplay, with: .enabledWithNoScreenshots)  // Not selected

// Example: User selected None (5)
Luciq.setReproStepsFor(.all, with: .enabledWithNoScreenshots)
```

**Issue Type Options:**

* `.bug` - Bug Reporting
* `.allCrashes` - Crash Reporting
* `.sessionReplay` - Session Replay
* `.all` - All products

**Key Points:**

* Selected products → `.enable` (with screenshots)
* Non-selected products → `.enabledWithNoScreenshots` (without screenshots)

***

### Optional Step 2 — Add User Identification

> 📋 **Workflow:** See [common-workflow.md - Optional Step 2](https://github.com/luciqai/luciq-docs/blob/main/ios/setup-luciq-for-ios/integrate-luciq-on-ios/common-workflow.md#optional-step-2--add-user-identification)

#### iOS Implementation - Login Flow

```swift
import LuciqSDK

class AuthenticationManager: ObservableObject {
    func signIn(email: String, password: String) -> Bool {
        // ... authentication logic ...

        if authenticationSuccessful {
            // Identify user AFTER successful auth, BEFORE navigation
            Luciq.identifyUser(
                withID: nil,              // or user.id
                email: user.email,        // or nil
                name: user.name           // or nil
            )

            currentUser = user
            isAuthenticated = true
            return true
        }

        return false
    }

    func signUp(email: String, password: String, name: String) -> Bool {
        // ... signup logic ...

        if signupSuccessful {
            // Identify user after signup
            Luciq.identifyUser(
                withID: nil,
                email: email,
                name: name
            )

            return true
        }

        return false
    }
}
```

**API Signature:**

```swift
Luciq.identifyUser(
    withID: String?,     // Required parameter, can be nil
    email: String?,      // Required parameter, can be nil
    name: String?        // Required parameter, can be nil
)
```

**Examples:**

* Email only: `Luciq.identifyUser(withID: nil, email: user.email, name: user.name)`
* ID only: `Luciq.identifyUser(withID: user.id, email: nil, name: user.name)`
* Both: `Luciq.identifyUser(withID: user.id, email: user.email, name: user.name)`

#### iOS Implementation - Logout Flow

```swift
class AuthenticationManager: ObservableObject {
    func logout() {
        // Call Luciq logout BEFORE clearing session
        Luciq.logOut()

        // Then clear user data
        currentUser = nil
        isAuthenticated = false
        UserDefaults.standard.removeObject(forKey: "loggedInUserEmail")
    }
}
```

***

### Step 7 — Verification & Testing **\[WRAP UP & VALIDATE]**

> 📋 **Workflow:** See [common-workflow.md - Step 7](https://github.com/luciqai/luciq-docs/blob/main/ios/setup-luciq-for-ios/integrate-luciq-on-ios/common-workflow.md#step-7--verification--testing-wrap-up--validate-user-initiated-only)

#### iOS Build Verification

```bash
xcodebuild -project YourProject.xcodeproj \
           -scheme YourScheme \
           -configuration Debug \
           -destination 'platform=iOS Simulator,name=iPhone 15 Pro' \
           build
```

**Expected:** `** BUILD SUCCEEDED **`

**iOS-Specific Build Errors:**

| Error                             | Cause                                            | Fix                                |
| --------------------------------- | ------------------------------------------------ | ---------------------------------- |
| `no such module 'Luciq'`          | Used `import Luciq` instead of `import LuciqSDK` | Change to `import LuciqSDK`        |
| `version not found`               | Invalid SPM version                              | Check version from releases/latest |
| `Missing package product 'Luciq'` | Package not added to target                      | Add "Luciq" product in Xcode       |

#### iOS Runtime Testing

1. Run app in Xcode (Cmd+R)
2. Trigger Luciq:
   * Shake: Hardware → Shake (Cmd+Ctrl+Z in simulator)
   * Screenshot: Cmd+S in simulator
   * Floating Button: Tap the button overlay
3. Verify Luciq UI appears
4. Submit test report
5. Check dashboard

***

### iOS-Specific Troubleshooting

#### Issue: "Command SwiftCompile failed"

**Cause:** Import or syntax error **Fix:** Verify all imports are `import LuciqSDK`, check Swift syntax

#### Issue: NetworkLogger not found

**Cause:** Import missing **Fix:** Ensure `import LuciqSDK` at top of file

#### Issue: Shake not working in simulator

**Cause:** Simulator gesture needed **Fix:** Use Hardware → Shake or Cmd+Ctrl+Z

#### Issue: Reports missing user info

**Cause:** identifyUser called with all nil parameters **Fix:** Pass at least email or ID (not all nil)

#### Issue: "Fastlane dSYMs file is not found!"

**Cause:** Missing `dsym_array_paths` parameter in Fastlane plugin call **Fix:** For local archives (using `gym`/`build_app`), you MUST specify the dSYM path:

```ruby
luciq_official(
  api_token: "<APP_TOKEN>",
  dsym_array_paths: ["./build/<APP_NAME>.xcarchive/dSYMs/<APP_NAME>.app.dSYM"]
)
```

**Note:** This parameter is only optional when using `download_dsyms` to fetch dSYMs from App Store Connect.

***

### Quick Reference

```swift
// ALWAYS use this import
import LuciqSDK

// Default initialization (shake + floatingButton)
Luciq.start(withToken: "token", invocationEvents: [.shake, .floatingButton])

// User identification
Luciq.identifyUser(withID: nil, email: "user@example.com", name: "John")

// Logout
Luciq.logOut()

// Screenshot masking (default: maskNothing)
// Configure screenshot masking based on your app's privacy requirements
// Options: .textInputs, .labels, .media, or combine multiple types
Luciq.setAutoMaskScreenshots(.maskNothing)  // Default: no automatic masking

// SwiftUI views are automatically masked when you change masked types from .maskNothing
// Luciq.autoMaskSwiftUIViews = false  // Uncomment to disable

// Network masking (after start)
NetworkLogger.setRequestObfuscationHandler { request in
    // ... masking logic ...
}
```
