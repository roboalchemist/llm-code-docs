# Source: https://docs.luciq.ai/flutter/flutter-luciq-migration.md

# Flutter Luciq Migration

### Overview

This comprehensive migration guide helps you migrate from Instabug to Luciq Flutter SDK, covering all recent changes, API updates, and configuration requirements.

**Summary of Core Changes:** Dependency: `"instabug_flutter":xxx` → `"luciq_flutter": "xxx"` Main Class: `Instabug` -> `Luciq`

### Prerequisites

* Ensure you have a clean git working directory (no uncommitted changes)
* Make sure you’re using Instabug version **16.0.0** or later.
* Make sure you're in the root directory of your Flutter project

### Migration Script Usage

{% stepper %}
{% step %}

#### Pre-Migration Setup

{% code title="Shell" %}

```bash
## Ensure clean git working directory
git status
git add .
git commit -m "Pre-migration commit"
## Install Luciq CLI and need to be called everytime you need to migrate to fetch last version
dart pub global activate luciq_cli
```

{% endcode %}
{% endstep %}

{% step %}

#### Run Migration Script

{% code title="Shell" %}

```bash
## Dry run first to preview changes
luciq-cli migrate --dry-run
## Run actual migration
luciq-cli migrate
```

{% endcode %}
{% endstep %}

{% step %}

#### Update Dependencies

{% code title="YAML" %}

```yaml
# pubspec.yaml
dependencies:
  luciq_flutter: ^18.0.0
  luciq_dio_interceptor: ^3.0.0 # Optional
  luciq_http_client: ^3.0.0 # Optional
  luciq_flutter_modular: ^2.0.0 # Optional
```

{% endcode %}
{% endstep %}

{% step %}

#### SDK Initialization

{% code title="Dart" %}

```dart
// New initialization pattern
await Luciq.init(
  token: 'YOUR_TOKEN',
  invocationEvents: [InvocationEvent.shake],
  debugLogsLevel: LogLevel.error,
  appVariant: 'production', // New optional parameter
);
```

{% endcode %}
{% endstep %}

{% step %}

#### Private Views API

{% code title="Dart" %}

```dart
// New private views configuration
LuciqWidget(
  child: MyApp(),
  enablePrivateViews: true,
  enableUserSteps: true,
  automasking: [
    AutoMasking.allTextFields(),
    AutoMasking.allButtons(),
  ],
)
```

{% endcode %}
{% endstep %}
{% endstepper %}

### API Reference

#### Main Module

| Old API                   | New API                | Notes                        |
| ------------------------- | ---------------------- | ---------------------------- |
| `Instabug.init()`         | `Luciq.init()`         | Main initialization method   |
| `Instabug.setEnabled()`   | `Luciq.setEnabled()`   | Enable/disable functionality |
| `Instabug.show()`         | `Luciq.show()`         | Show bug reporting UI        |
| `Instabug.setUserData()`  | `Luciq.setUserData()`  | Set user data                |
| `Instabug.identifyUser()` | `Luciq.identifyUser()` | Identify user                |
| `Instabug.logOut()`       | `Luciq.logOut()`       | Log out user                 |

#### Configuration

| Old API                    | New API                 | Notes                             |
| -------------------------- | ----------------------- | --------------------------------- |
| `InstabugConfig`           | `LuciqConfig`           | Configuration interface           |
| `Instabug.invocationEvent` | `Luciq.invocationEvent` | Invocation events enum            |
| `Instabug.LogLevel`        | `Luciq.LogLevel`        | Log level enum                    |
| `Instabug.ColorTheme`      | `Luciq.ColorTheme`      | Color theme enum                  |
| `Instabug.IBGLocale`       | `Luciq.LuciqLocale`     | Locale enum                       |
| `IBG_*`                    | `LCQ_*`                 | All prefixed constants in iOS     |
| `IBG_*`                    | `LUCIQ_*`               | All prefixed constants in Android |

#### Environment Variables

| Variable                   | Description                            |
| -------------------------- | -------------------------------------- |
| `LUCIQ_APP_TOKEN`          | Your Luciq application token           |
| `LUCIQ_API_KEY`            | Your Luciq API key                     |
| `LUCIQ_AUTO_UPLOAD_ENABLE` | Enable/disable automatic symbol upload |

#### Test Migration

{% code title="Shell" %}

```bash
## Run tests
flutter test
## Build and test on devices
flutter build apk --release
flutter build ios --release
```

{% endcode %}

#### Getting Help

<details>

<summary>Resources</summary>

**Documentation:** [Luciq Flutter Documentation](https://docs.luciq.ai/docs/flutter-overview)\
**GitHub Issues:** [Luciq Flutter GitHub](https://github.com/Luciq/Luciq-Flutter/issues)

</details>
