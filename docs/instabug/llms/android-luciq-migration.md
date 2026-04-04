# Source: https://docs.instabug.com/android/android-luciq-migration.md

# Android Luciq Migration

### Overview

This guide helps you migrate your Android project from the Instabug SDK to the Luciq SDK. This change is part of a company-wide rebranding initiative. You can perform the migration manually by following the step-by-step instructions or use our automated migration script for a faster transition.

### Prerequisites

Before starting the migration process, ensure your project meets the following requirements and take the necessary precautions.

#### Supported Instabug Versions

This migration guide supports projects currently using:

* **Instabug SDK (Manual & Automated):** 16.x.x and above
* **Target Luciq SDK:** 18.0.0
* **All Instabug modules:** Core, APM, Crash, Bug, Survey, Features Request, NDK Crash, Compose, Compose APM, OkHttp Interceptors, gRPC Interceptors, Compiler Extension, Test Report

{% hint style="warning" %}
If you're using Instabug version prior to 16.0.0, it's recommended to upgrade Instabug SDK (consult change logs) before proceeding with this migration process.
{% endhint %}

#### Pre-Migration Checklist

* Commit all changes to your version control system (e.g., Git).
* Create a dedicated backup branch to allow for a clean rollback if needed.
* Build and run your project to confirm it's in a stable, working state before you begin.
* Assess your project's complexity using the Migration Complexity Assessment to choose the best approach for you.

Project Assessment

* Identify all Instabug dependencies in your project
* List custom Instabug configurations in build files
* Note any custom ProGuard rules related to Instabug
* Check for hardcoded Instabug references in code comments or strings

Environment Preparation

* Sync project and resolve any existing build issues
* Clean build cache: ./gradlew clean
* Ensure stable internet connection (for dependency downloads)

### Migration Complexity Assistant

| Project Type                     | Complexity     | Recommended Approach                        | Estimated Time |
| -------------------------------- | -------------- | ------------------------------------------- | -------------- |
| Single-target, standard setup    | 🟢 **Simple**  | Automated script                            | 15-30 minutes  |
| Multi-target, standard config    | 🟡 **Medium**  | Automated script + manual review            | 1-2 hours      |
| Complex setup, on-premise config | 🔴 **Complex** | Manual migration or script + careful review | 2-4 hours      |

### When to Use Manual vs. Automated Migration

Use Automated Migration when:

* You have a standard Instabug setup with minimal customization.
* You are using a supported Instabug version.
* Your project doesn't have complex custom build scripts that reference Instabug.
* You are comfortable using command-line tools and have created a backup.

Use Manual Migration when:

* You have a heavily customized Instabug implementation.
* You are using an older, unsupported version of the Instabug SDK.
* Your project has complex build logic or dependencies that the script might not handle.
* You prefer granular control over every step of the migration process.

### Step-by-Step Manual Migration

{% stepper %}
{% step %}

#### Migrate Your Dependency

Quick option: this step can be automated using the migration script.

General rules:

* Replace `com.instabug.library` group with `ai.luciq.library`
* Replace `instabug` prefix in artifact names with `luciq`
* Upgrade artifact version to `18.0.0`

Artifact name mappings:

| Instabug Artifact                | Luciq Artifact                |
| -------------------------------- | ----------------------------- |
| instabug                         | luciq                         |
| instabug-apm                     | luciq-apm                     |
| instabug-crash                   | luciq-crash                   |
| instabug-bug                     | luciq-bug                     |
| instabug-survey                  | luciq-survey                  |
| instabug-features-request        | luciq-features-request        |
| instabug-ndk-crash               | luciq-ndk-crash               |
| instabug-compose                 | luciq-compose                 |
| instabug-compose-apm             | luciq-compose-apm             |
| instabug-apm-okhttp-interceptor  | luciq-apm-okhttp-interceptor  |
| instabug-apm-grpc-interceptor    | luciq-apm-grpc-interceptor    |
| instabug-core                    | luciq-core                    |
| instabug-with-okhttp-interceptor | luciq-with-okhttp-interceptor |
| instabug-plugin                  | luciq-plugin                  |
| instabug-test-report             | luciq-test-report             |
| instabug-compose-core            | luciq-compose-core            |

Examples:

Before (Version Catalog `libs.versions.toml`):

{% code title="TOML" overflow="wrap" %}

```toml
[versions]
instabug = "16.0.1"

[libraries]
instabug = {group = "com.instabug.library", name = "instabug", version.ref = "instabug"}
instabug-compose = {group = "com.instabug.library", name = "instabug-compose", version.ref = "instabug"}
```

{% endcode %}

After:

{% code title="TOML" overflow="wrap" %}

```toml
[versions]
luciq = "18.0.0"

[libraries]
instabug = {group = "ai.luciq.library", name = "luciq", version.ref = "luciq"}
instabug-compose = {group = "ai.luciq.library", name = "luciq-compose", version.ref = "luciq"}
```

{% endcode %}

Before (`build.gradle` dependencies):

{% code title="Kotlin" %}

```kotlin
dependencies {
    implementation 'com.instabug.library:instabug:16.0.1'
    implementation 'com.instabug.library:instabug-compose:16.0.1'
}
```

{% endcode %}

After:

{% code title="Kotlin" %}

```kotlin
dependencies {
    implementation 'ai.luciq.library:luciq:18.0.0'
    implementation 'ai.luciq.library:luciq-compose:18.0.0'
}
```

{% endcode %}
{% endstep %}

{% step %}

#### Migrate your plugin integration

Actions:

* Replace `com.instabug.library:instabug-plugin:16.0.1` classpath with `ai.luciq.library:luciq-plugin:18.0.0` (if used as classpath).
* Replace root plugin id `com.instabug.library` with `ai.luciq.library` and version `18.0.0` (if using `id`).
* Replace module-level plugin ids according to mapping.

Plugin mappings:

| Instabug Plugin             | Luciq Plugin             |
| --------------------------- | ------------------------ |
| instabug                    | luciq                    |
| instabug-crash              | luciq-crash              |
| instabug-apm                | luciq-apm                |
| instabug-compiler-extension | luciq-compiler-extension |

Examples:

Classpath before:

<pre class="language-kotlin" data-title="Kotlin"><code class="lang-kotlin"><strong>buildScript {
</strong>    dependencies {
        classpath 'com.instabug.library:instabug-plugin:16.0.1'
    }
}
</code></pre>

After:

{% code title="Kotlin" %}

```kotlin
buildScript {
    dependencies {
        classpath 'ai.luciq.library:luciq-plugin:18.0.0'
    }
}
```

{% endcode %}

Root plugin before:

{% code title="Kotlin" %}

```kotlin
plugins {
    id("com.instabug.library") version "16.0.1" apply false
}
```

{% endcode %}

After:

{% code title="Kotlin" %}

```kotlin
plugins {
    id("ai.luciq.library") version "18.0.0" apply false
}
```

{% endcode %}

Version Catalog plugin before:

{% code title="TOML" %}

```toml
[versions]
instabug = "16.0.1"

[plugins]
instabug = { id = "com.instabug.library", version.ref = "instabug" }
```

{% endcode %}

After:

{% code title="TOML" %}

```toml
[versions]
luciq = "18.0.0"

[plugins]
instabug = { id = "ai.luciq.library", version.ref = "luciq" }
```

{% endcode %}

Module-level plugin before:

{% code title="Kotlin" %}

```kotlin
plugins {
    id("instabug")
    id("instabug-apm")
    id("instabug-crash")
}
```

{% endcode %}

After:

{% code title="Kotlin" %}

```kotlin
plugins {
    id("luciq")
    id("luciq-apm")
    id("luciq-crash")
}
```

{% endcode %}
{% endstep %}

{% step %}

#### Migrate your plugin configurations

Skip this step if you're not using the Instabug plugin.

Changes summary:

* Replace `Instabug` / `instabug` configuration closures with a unified `luciq` closure.
* APM's `debugEnabled` is removed; use `setDebugLogsEnabled()` under `luciq` top-level instead.
* Change `APM` block to `apm` (lowercase) inside `luciq`.

Naming mapping:

| Instabug Naming       | Luciq Naming      |
| --------------------- | ----------------- |
| Instabug{}/instabug{} | luciq{}           |
| Instabug { APM { } }  | luciq { apm { } } |

Migration steps:

1. Change `instabug` / `Instabug` blocks to `luciq`.
2. If both legacy and new blocks exist, merge into a single `luciq` block.
3. Change `APM` to `apm`.
4. If `apm` had `debugEnabled = {boolean}`, remove it and add `setDebugLogsEnabled({boolean})` at the top-level `luciq` block.

Examples:

Legacy `Instabug` before:

{% code title="Kotlin" %}

```kotlin
Instabug {
   APM {
      debugEnabled = true
      networkEnabled = false
      fragmentSpansEnabled = true
   }
}
```

{% endcode %}

After:

{% code title="Kotlin" %}

```kotlin
luciq {
   // Added for backward compatibility with apm.debugEnabled = true
   setDebugLogsEnabled(true)
   apm {
      // debugEnabled = true is removed
      networkEnabled = false
      fragmentSpansEnabled = true
   }
}
```

{% endcode %}

Using both blocks, `Instabug` (legacy) and `instabug`

{% code title="Kotlin" %}

```kotlin
Instabug {
   APM {
      debugEnabled = true
      networkEnabled = false
      fragmentSpansEnabled = true
   }
}

instabug {
   setDebugLogsEnabled(false)
   setCaptureComposeNavigationDestinations(true)
   compilerExtension{
      // Compiler extension configurations
   }
}
```

{% endcode %}

After:

{% code title="Kotlin" %}

```kotlin
luciq {
   // Value changed to true for backward compatibility with apm.debugEnabled = true
   setDebugLogsEnabled(true)
   setCaptureComposeNavigationDestinations(true)
   apm {
      // debugEnabled = true is removed
      networkEnabled = false
      fragmentSpansEnabled = true
   }
   compilerExtension{
      // Compiler extension configurations
   }
}
```

{% endcode %}
{% endstep %}

{% step %}

#### Migrate your source code (Kotlin/Java)

Key changes:

* SDK packages now use prefix `ai.luciq` instead of `com.instabug`.
* Public classes/methods containing `Instabug`, `IBG`, `instabug`, or `ibg` are renamed to `Luciq`/`luciq` as per casing.

Class/method mappings (select):

| Type         | Instabug Naming                        | Luciq Naming                     |
| ------------ | -------------------------------------- | -------------------------------- |
| Class        | Instabug                               | Luciq                            |
| Class        | IBGNonFatalException                   | LuciqNonFatalException           |
| Class        | InstabugInvocationEvent                | LuciqInvocationEvent             |
| Class        | InstabugFloatingButtonEdge             | LuciqFloatingButtonEdge          |
| Class        | IBGBugReportingType                    | LuciqBugReportingType            |
| Class        | InstabugApmOkHttpEventListener         | LuciqApmOkHttpEventListener      |
| Class        | InstabugOkhttpInterceptor              | LuciqOkhttpInterceptor           |
| Class        | InstabugColorTheme                     | LuciqColorTheme                  |
| Method       | Replies.isInstabugNotification()       | Replies.isLuciqNotification()    |
| Method       | Instabug$Builder.setInstabugLogState() | Luciq$Builder.setLuciqLogState() |
| Composable   | IBGScreen()                            | LuciqScreen()                    |
| Extension fn | ibgTrackingInfo()                      | luciqTrackingInfo()              |

Migration actions (apply to all Java/Kotlin files):

1. Replace import prefix `com.instabug` with `ai.luciq`.
2. Replace fully-qualified Instabug class references to `ai.luciq`.
3. Replace symbols (classes/methods/enums) according to the mapping table.
4. Update ProGuard rules: replace `com.instabug` with `ai.luciq` where applicable.
   {% endstep %}

{% step %}

#### Migrate your Manifest file

Only required if:

* You specify Instabug application token as metadata `com.instabug.APP_TOKEN` for early initialization.
* You override Instabug framework components (Activities, ContentProviders).

Component mappings:

| Type            | Instabug Naming         | Luciq Naming         |
| --------------- | ----------------------- | -------------------- |
| ContentProvider | InstabugContentProvider | LuciqContentProvider |
| Activity        | InstabugDialogActivity  | LuciqDialogActivity  |
| Activity        | InstabugThanksActivity  | LuciqThanksActivity  |

Migration actions:

1. Change metadata key `com.instabug.APP_TOKEN` → `ai.luciq.APP_TOKEN`
2. Replace `com.instabug` package prefix with `ai.luciq` for overridden components.
3. Map component class names as per the table above.
   {% endstep %}

{% step %}

#### Migrate your resources

Only required if you're using `instabug_config.json`.

Actions:

1. Rename `instabug_config.json` → `luciq_config.json`
2. In the file content, replace key `instabug-domain` → `luciq-domain`
   {% endstep %}
   {% endstepper %}

### Automated Migration Script

#### Introduction

The Luciq Migrator is a Python-based tool that automates the migration steps in this guide. It covers:

* Gradle files: Version catalogs (`libs.versions.toml`), dependencies, and plugin configurations
* Plugin configurations: Legacy and new configuration block migrations
* Java/Kotlin source code: Package imports, class names, method names, fully qualified references
* Android Manifests: App tokens and ContentProvider declarations
* Resource files: `instabug_config.json` → `luciq_config.json`
* ProGuard rules: Package name references

The script provides backups, dry-run previews, and follows the exact mapping tables defined in this guide.

#### Where to find it?

You can find the migration script in Luciq's Github public repository:\
<https://github.com/luciqai/luciq-android-sdk/blob/master/luciq-migrator.zip>

#### Step-by-Step Usage Guide

{% stepper %}
{% step %}
**Step: Extract the Migration Scripts**

1. Extract `luciq-migrator.zip` in your Android project root directory:

```
cd /path/to/your/android/project
unzip luciq-migrator.zip
```

2. Verify the directory structure:

```
your-android-project/
├── luciq-migrator/          # ← Migration scripts directory
├── src/                     # ← Your project source code
├── build.gradle             # ← Your project files
└── ...
```

{% endstep %}

{% step %}
**Step: Make the Script Executable**

```
chmod +x luciq-migrator/migrate-to-luciq.sh
```

{% endstep %}

{% step %}
**Step: Preview Changes (Recommended)**

Always preview changes first:

```
./luciq-migrator/migrate-to-luciq.sh --dry-run --output-file migration-preview.txt
```

This shows:

* Files that will be modified
* Exact changes
* Migration statistics\
  No changes are applied in dry-run.
  {% endstep %}

{% step %}
**Step: Run the Migration**

Run full migration once satisfied with preview:

```
./luciq-migrator/migrate-to-luciq.sh
```

The script will:

* Create a backup in migration-backup/
* Migrate files per mapping tables
* Provide detailed statistics
  {% endstep %}

{% step %}
**Step: Verify the Migration**

After migration, check for remaining references and build:

{% code title="Shell" %}

```bash
# Check for remaining Instabug references
grep -r "com\.instabug" . --exclude-dir=migration-backup

# Build your project
./gradlew clean build
```

{% endcode %}
{% endstep %}
{% endstepper %}

#### Options Catalog

Basic Options

| Option             | Description                                        | Example                                                                  |
| ------------------ | -------------------------------------------------- | ------------------------------------------------------------------------ |
| --help             | Show help message and usage examples               | ./luciq-migrator/migrate-to-luciq.sh --help                              |
| --dry-run          | Preview changes without making modifications       | ./luciq-migrator/migrate-to-luciq.sh --dry-run                           |
| --output-file FILE | Write dry-run output to FILE (only with --dry-run) | ./luciq-migrator/migrate-to-luciq.sh --dry-run --output-file changes.txt |

Advanced Options

| Option        | Description                                                        | When to Use                                                                                    | Example                                            |
| ------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| --source-only | Migrate only Java/Kotlin files, Manifest & resources (skip Gradle) | When you've already migrated Gradle files manually or want to test source code migration first | ./luciq-migrator/migrate-to-luciq.sh --source-only |
| --no-backup   | Skip creating backup (not recommended)                             | Only when you have your own backup strategy or project is version controlled                   | ./luciq-migrator/migrate-to-luciq.sh --no-backup   |

Combining Options examples:

```
# Preview source-only changes
./luciq-migrator/migrate-to-luciq.sh --source-only --dry-run

# Run source-only migration without backup
./luciq-migrator/migrate-to-luciq.sh --source-only --no-backup

# Run migration on a different project path
./luciq-migrator/migrate-to-luciq.sh /path/to/different/project
```

Migration Modes

* Comprehensive Mode (Default): Migrates Gradle, Java/Kotlin, Manifest, Resources. Recommended for most users.
* Source-Only Mode (`--source-only`): Migrates Java/Kotlin, Manifest, Resources only.

#### Safety Features

* Automatic Backup: Creates complete project backup before migration
* Dry Run Mode: Preview all changes without applying them
* Detailed Statistics: Shows what was modified
* Easy Rollback: Restore from backup if issues occur
* Zero Dependencies: Uses built-in Python functionality

#### System Requirements

* Python 3.6+
* No external dependencies (uses built-in Python modules)
* Keep all migration scripts in the same directory

{% hint style="info" %}

#### **Pro Tip**

Always run `--dry-run` first to understand the scope of changes, especially on large projects. The migration script is designed to be safe and reversible, but previewing changes helps ensure confidence in the process.
{% endhint %}

### Q\&As

<details>

<summary>What should I do before starting the migration process?</summary>

Before proceeding:

* Commit all current changes on your working branch for easy revert.
* Clean build cache: ./gradlew clean
* Sync the project so dependencies resolve correctly
* Build the project to ensure it compiles successfully
* Ensure stable internet connection for new dependency downloads

</details>

<details>

<summary>Is there a recommended Instabug version to be in use before migration?</summary>

It's recommended to use Instabug version 16.0.0 or higher for a graceful migration.

</details>

<details>

<summary>Will Instabug artifacts still be available by the time I do the migration?</summary>

Yes. Instabug artifacts will remain available; the last version referenced is 16.0.1.

</details>

<details>

<summary>Is it possible to proceed with the migration without upgrading to Instabug version 16.0.0?</summary>

It's generally not recommended. Older major releases may have removed APIs, causing unresolved references after migration. If you must migrate from a version older than 16.0.0, review Instabug's major release change logs and adjust your usage accordingly.

</details>

<details>

<summary>What's the expected outcome if I migrate from a version older than 16.0.0 without checking change logs?</summary>

If your project uses APIs removed in Instabug releases prior to 16.0.0, you will likely encounter unresolved references and compilation issues after migration.

</details>

<details>

<summary>Are there specific system requirements to run the automated script?</summary>

The automated script requires Python 3.6+. You can check your Python version with:

```
python3 --version
```

</details>

<details>

<summary>What exactly does the script do?</summary>

The script performs a comprehensive migration covering the 6 steps in this guide: Gradle/plugin changes, plugin configurations, source code updates, manifest updates, resource file updates, and ProGuard rules adjustments.

</details>

<details>

<summary>What types of build configurations does the script support?</summary>

The script supports:

* Version catalog (`.toml`)
* `buildSrc` modules
* `build.gradle` files (Groovy/KTS)

</details>

<details>

<summary>When should I fully rely on the script for migration?</summary>

In most cases, the script will handle migration well. If your build configuration files are highly custom or non-standard, consider manual migration for Gradle/plugin parts and use the script with `--source-only` for source code changes.

</details>

<details>

<summary>If build configurations are custom, do I have to do all migration steps manually?</summary>

Not necessarily. You can manually migrate Gradle/plugin configurations (steps 1–3) and then run the script with `--source-only` to migrate source code, manifests, and resources.

</details>

<details>

<summary>My project is version controlled. Is it mandatory for the script to create a backup folder?</summary>

No. If you use version control, you can run the script with `--no-backup` to skip creating a backup folder.

</details>

<details>

<summary>Can I use the automated script if I'm on Instabug version lower than 16.0.0?</summary>

It's generally not recommended for the same reasons noted above regarding removed APIs and potential compilation issues.

</details>

Last updated about 1 month ago.
