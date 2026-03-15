# Source: https://posthog.com/docs/libraries/unity.md

# Unity - Docs

> **Note:** This SDK is currently in **beta**. Please report any issues on [GitHub](https://github.com/PostHog/posthog-unity/issues).

This is the official PostHog SDK for Unity. It uses an internal queue to make calls fast and non-blocking. It also batches requests and flushes asynchronously, making it perfect to use in any part of your Unity game or application.

PostHog Unity SDK supports Windows, Mac, Linux, iOS, Android, and WebGL platforms.

## Installation

PostHog is available for Unity via the [Unity Package Manager](https://docs.unity3d.com/Manual/upm-ui.html).

### Requirements

-   Unity 2021.3 LTS or later
-   .NET Standard 2.1 API Compatibility Level

### Via Unity Package Manager (Git URL)

1.  Open **Window > Package Manager**
2.  Click the **+** button and select **Add package from git URL**
3.  Enter: `https://github.com/PostHog/posthog-unity.git?path=com.posthog.unity`

### Via local package

1.  Clone or download the [posthog-unity repository](https://github.com/PostHog/posthog-unity)
2.  Open **Window > Package Manager**
3.  Click the **+** button and select **Add package from disk**
4.  Navigate to `com.posthog.unity/package.json`

### Configuration

There are two ways to configure PostHog in Unity:

#### Option 1: Unity Inspector (recommended)

The easiest way to configure PostHog is through the Unity Inspector:

1.  Go to **Edit > Project Settings > PostHog** (this creates a settings asset if one doesn't exist)
2.  Enter your **API Key** and select your **Host** (US or EU Cloud)
3.  Configure other options as needed

The settings asset is created at `Assets/Resources/PostHogSettings.asset`. PostHog automatically initializes when your game starts using these settings.

You can also create the settings asset manually via **Assets > Create > PostHog > Settings in Resources**.

> **Tip:** Click **Test Connection** in the Inspector to verify your API key is valid.

#### Option 2: Code-based initialization

For more control, initialize PostHog in your game's startup script:

C#

PostHog AI

```csharp
using PostHogUnity;
using UnityEngine;
public class GameManager : Monobehavior
{
    void Start()
    {
        PostHog.Setup(new PostHogConfig
        {
            ApiKey = "<ph_project_token>",
            Host = "https://us.i.posthog.com" // usually 'https://us.i.posthog.com' or 'https://eu.i.posthog.com'
        });
    }
}
```

> **Note:** If you use code-based initialization, remove any `PostHogSettings.asset` from your Resources folder to avoid double initialization.

### Configuration options

All options below can be set via the Unity Inspector or in code:

C#

PostHog AI

```csharp
PostHog.Setup(new PostHogConfig
{
    // Required
    ApiKey = "<ph_project_token>",
    // Optional
    Host = "https://us.i.posthog.com",         // PostHog instance URL (default: https://us.i.posthog.com)
    FlushAt = 20,                           // Events before auto-flush (default: 20)
    FlushIntervalSeconds = 30,              // Seconds between flushes (default: 30)
    MaxQueueSize = 1000,                    // Max queued events (default: 1000)
    MaxBatchSize = 50,                      // Max events per request (default: 50)
    CaptureApplicationLifecycleEvents = true, // Auto-capture app lifecycle events (default: true)
    CaptureExceptions = true,               // Auto-capture unhandled exceptions (default: true)
    PersonProfiles = PersonProfiles.IdentifiedOnly, // When to create person profiles
    PreloadFeatureFlags = true,             // Fetch flags on init (default: true)
    SendFeatureFlagEvent = true,            // Track flag usage (default: true)
    LogLevel = PostHogLogLevel.Warning      // Log verbosity (default: Warning)
});
```

## Capturing events

You can send custom events using `capture`:

C#

PostHog AI

```csharp
PostHog.Capture("user_signed_up");
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

C#

PostHog AI

```csharp
PostHog.Capture("user_signed_up", new Dictionary<string, object>
{
    { "login_type", "email" },
    { "is_free_trial", true }
});
```

### Capturing screen views

Track screen views to understand user navigation through your game:

C#

PostHog AI

```csharp
PostHog.Screen("Main Menu");
// With additional properties
PostHog.Screen("Level Select", new Dictionary<string, object>
{
    { "unlocked_levels", 5 }
});
```

## Identifying users

> We highly recommend reading our section on [Identifying users](/docs/integrate/identifying-users.md) to better understand how to correctly use this method.

When a user logs in, you can associate their events with their identity by calling `IdentifyAsync`:

C#

PostHog AI

```csharp
using PostHogUnity;
using System.Collections.Generic;
await PostHog.IdentifyAsync("user_123", new Dictionary<string, object>
{
    { "email", "user@example.com" },
    { "name", "Max Hedgehog" },
    { "plan", "premium" }
});
```

### Reset on logout

When a user logs out, call `ResetAsync` to clear the current user's identity and generate a new anonymous distinct ID:

C#

PostHog AI

```csharp
await PostHog.ResetAsync();
```

## Anonymous vs identified events

PostHog captures two types of events: [**anonymous** and **identified**](/docs/data/anonymous-vs-identified-events.md)

**Identified events** enable you to attribute events to specific users, and attach [person properties](/docs/product-analytics/person-properties.md). They're best suited for logged-in users.

Scenarios where you want to capture identified events are:

-   Tracking logged-in users in B2B and B2C SaaS apps
-   Doing user segmented product analysis
-   Growth and marketing teams wanting to analyze the *complete* conversion lifecycle

**Anonymous events** are events without individually identifiable data. They're best suited for [web analytics](/docs/web-analytics.md) or apps where users aren't logged in.

Scenarios where you want to capture anonymous events are:

-   Tracking a marketing website
-   Content-focused sites
-   B2C apps where users don't sign up or log in

Under the hood, the key difference between identified and anonymous events is that for identified events we create a [person profile](/docs/data/persons.md) for the user, whereas for anonymous events we do not.

> **Important:** Due to the reduced cost of processing them, anonymous events can be up to 4x cheaper than identified ones, so we recommended you only capture identified events when needed.

### Controlling person profiles

By default, the SDK captures identified events. To control whether events create person profiles, configure `PersonProfiles` during initialization:

C#

PostHog AI

```csharp
PostHog.Setup(new PostHogConfig
{
    ApiKey = "<ph_project_token>",
    Host = "https://us.i.posthog.com",
    PersonProfiles = PersonProfiles.IdentifiedOnly // Only create profiles on identify
});
```

Available options:

-   `PersonProfiles.IdentifiedOnly` (default) - Only creates person profiles when `Identify` is called
-   `PersonProfiles.Always` - Creates person profiles for all events
-   `PersonProfiles.Never` - Never creates person profiles (anonymous events only)

## Super properties

Super properties are properties associated with events that are set once and then sent with every `Capture` call.

They are set using `Register`, which takes a key and value, and they persist across sessions.

C#

PostHog AI

```csharp
// Register a super property
PostHog.Register("app_version", "1.2.3");
PostHog.Register("platform", "iOS");
```

This ensures that every event sent by the user will include these properties.

### Removing super properties

Super properties are persisted across sessions so you have to explicitly remove them if they are no longer relevant:

C#

PostHog AI

```csharp
PostHog.Unregister("app_version");
```

If you are doing this as part of a user logging out you can instead simply use `PostHog.ResetAsync()` which takes care of clearing all stored super properties and more.

## Group analytics

Group analytics allows you to associate the events for that person's session with a group (e.g. teams, organizations, etc.). Read the [Group Analytics](/docs/user-guides/group-analytics.md) guide for more information.

> **Note:** This is a paid feature and is not available on the open-source or free cloud plan. Learn more on the [pricing page](/pricing.md).

-   Associate events with a group:

C#

PostHog AI

```csharp
PostHog.Group("company", "company_id_in_your_db");
```

-   Associate events with a group AND update group properties:

C#

PostHog AI

```csharp
PostHog.Group("company", "company_id_in_your_db", new Dictionary<string, object>
{
    { "name", "Acme Inc" },
    { "plan", "enterprise" },
    { "employees", 100 }
});
```

The `name` is a special property which is used in the PostHog UI for the name of the group. If you don't specify a `name` property, the group ID will be used instead.

## Feature flags

PostHog's [feature flags](/docs/feature-flags.md) enable you to safely deploy and roll back new features as well as target specific users and groups with them.

### Boolean feature flags

C#

PostHog AI

```csharp
if (PostHog.IsFeatureEnabled("flag-key"))
{
    // Do something differently for this user
}
```

### Multivariate feature flags

C#

PostHog AI

```csharp
var flag = PostHog.GetFeatureFlag("flag-key");
if (flag.IsEnabled)
{
    string variant = flag.GetVariant("control"); // "control" is the default value
    if (variant == "variant-key") // Replace with your variant key
    {
        // Do something for this variant
    }
}
```

### Feature flag payloads

Access payloads through the feature flag object:

C#

PostHog AI

```csharp
// Define your payload class (must use [Serializable] and public fields for JsonUtility)
[Serializable]
public class CheckoutConfig
{
    public string theme;
    public int maxItems;
    public bool showBanner;
}
// Get flag and access payload
var flag = PostHog.GetFeatureFlag("checkout-config");
if (flag.IsEnabled)
{
    var config = flag.GetPayload<CheckoutConfig>();
    Debug.Log($"Theme: {config.theme}, Max items: {config.maxItems}");
}
// For dynamic/nested payloads, use PostHogJson
var payload = flag.GetPayloadJson();
string theme = payload["theme"].GetString("light");
int maxItems = payload["settings"]["maxItems"].GetInt(10);
```

### Ensuring flags are loaded before usage

Every time a user opens the app, we send a request in the background to fetch the feature flags that apply to that user. We store those flags in storage.

This means that for most screens, the feature flags are available immediately – **except for the first time a user visits**.

To be notified when flags are loaded:

C#

PostHog AI

```csharp
// Via callback during setup
PostHog.Setup(new PostHogConfig
{
    ApiKey = "<ph_project_token>",
    OnFeatureFlagsLoaded = () => Debug.Log("Flags ready!")
});
// Or via event
PostHog.OnFeatureFlagsLoaded += () => UpdateUI();
```

### Reloading feature flags

Feature flag values are cached. If something has changed with your user and you'd like to refetch their flag values, call:

C#

PostHog AI

```csharp
await PostHog.ReloadFeatureFlagsAsync();
```

### Overriding server properties for flags

You can set properties used for flag evaluation:

C#

PostHog AI

```csharp
// Set person properties for targeting
PostHog.SetPersonPropertiesForFlags(new Dictionary<string, object>
{
    { "plan", "premium" },
    { "beta_user", true }
});
// Set group properties for targeting
PostHog.SetGroupPropertiesForFlags("company", new Dictionary<string, object>
{
    { "size", "enterprise" }
});
// Reset properties
PostHog.ResetPersonPropertiesForFlags();
PostHog.ResetGroupPropertiesForFlags();
```

## Experiments (A/B tests)

Since [experiments](/docs/experiments/manual.md) use feature flags, the code for running an experiment is very similar to the feature flags code:

C#

PostHog AI

```csharp
var flag = PostHog.GetFeatureFlag("experiment-feature-flag-key");
if (flag.GetVariant("control") == "variant-name")
{
    // Do something for this variant
}
```

It's also possible to [run experiments without using feature flags](/docs/experiments/running-experiments-without-feature-flags.md).

## Error tracking

The Unity SDK automatically captures unhandled exceptions and sends them to PostHog. This is enabled by default.

### Manual exception capture

For handled exceptions that you want to report:

C#

PostHog AI

```csharp
try
{
    // Risky operation
}
catch (Exception e)
{
    PostHog.CaptureException(e);
    // Handle the error gracefully
}
// With additional properties
PostHog.CaptureException(e, new Dictionary<string, object>
{
    { "context", "checkout_flow" },
    { "item_count", 5 }
});
```

### Configuration

C#

PostHog AI

```csharp
PostHog.Setup(new PostHogConfig
{
    ApiKey = "<ph_project_token>",
    // Exception tracking options
    CaptureExceptions = true,              // Enable automatic capture (default: true)
    ExceptionDebounceIntervalMs = 1000,    // Min ms between captures (default: 1000)
    CaptureExceptionsInEditor = true       // Capture in Unity Editor (default: true)
});
```

### Disabling error tracking

C#

PostHog AI

```csharp
PostHog.Setup(new PostHogConfig
{
    ApiKey = "<ph_project_token>",
    CaptureExceptions = false  // Disable automatic exception capture
});
```

## Session replay

> **Note:** Session replay for Unity is currently **experimental**. Performance impact varies based on your game's complexity and target devices.

Session replay enables you to record and watch user sessions in your Unity game. It captures screenshots, touch/mouse input, network requests, and console logs. Session replay is **disabled by default** and must be explicitly enabled.

The SDK uses `AsyncGPUReadback` to capture screenshots without blocking the main thread, ensuring minimal performance impact during gameplay.

### Enabling session replay

C#

PostHog AI

```csharp
PostHog.Setup(new PostHogConfig
{
    ApiKey = "<ph_project_token>",
    Host = "https://us.i.posthog.com",
    SessionReplay = true
});
```

### Configuration options

You can customize session replay behavior with `SessionReplayConfig`:

C#

PostHog AI

```csharp
PostHog.Setup(new PostHogConfig
{
    ApiKey = "<ph_project_token>",
    SessionReplay = true,
    SessionReplayConfig = new PostHogSessionReplayConfig
    {
        // Screenshot settings
        ThrottleDelaySeconds = 1.0f,    // Min time between screenshots (default: 1.0)
        ScreenshotQuality = 80,          // JPEG quality 1-100 (default: 80)
        ScreenshotScale = 0.75f,         // Resolution scale 0.1-1.0 (default: 0.75)
        // Telemetry capture
        CaptureNetworkTelemetry = true,  // Record HTTP request metadata (default: true)
        CaptureLogs = false,             // Record console logs (default: false)
        MinLogLevel = SessionReplayLogLevel.Warning,  // Log, Warning, or Error
        // Queue settings
        FlushAt = 20,                    // Events before auto-flush (default: 20)
        FlushIntervalSeconds = 30,       // Auto-flush interval (default: 30)
        MaxQueueSize = 100               // Max queued events (default: 100)
    }
});
```

### Manual control

You can manually start and stop session recording:

C#

PostHog AI

```csharp
// Check if session replay is active
if (PostHog.IsSessionReplayActive)
{
    // Stop recording
    PostHog.StopSessionReplay();
}
// Start recording (if not already active)
PostHog.StartSessionReplay();
```

### Recording network requests

Network requests are automatically captured when `CaptureNetworkTelemetry` is enabled. For custom HTTP clients, you can manually record requests:

C#

PostHog AI

```csharp
PostHog.RecordNetworkRequest(
    url: "https://api.example.com/data",
    method: "GET",
    statusCode: 200,
    durationMs: 150,
    responseSize: 1024
);
```

### Platform support for session replay

| Platform | Session Replay Support |
| --- | --- |
| Windows/Mac/Linux | Full |
| iOS | Full |
| Android | Full |
| WebGL | Not supported |

> **Note:** Session replay requires async GPU readback support. On WebGL, session replay is automatically disabled.

### Performance considerations

Session replay captures screenshots which can impact performance. To optimize:

-   Increase `ThrottleDelaySeconds` to reduce capture frequency
-   Lower `ScreenshotScale` to reduce resolution
-   Lower `ScreenshotQuality` to reduce file size
-   Disable `CaptureNetworkTelemetry` and `CaptureLogs` if not needed

## Application lifecycle events

When `CaptureApplicationLifecycleEvents` is enabled (default: `true`), these events are captured automatically:

-   `Application Installed` - First launch
-   `Application Updated` - Version changed
-   `Application Opened` - App foregrounded
-   `Application Backgrounded` - App backgrounded

## Opt out of data capture

For GDPR compliance, you can disable data collection at any time:

C#

PostHog AI

```csharp
// Opt out (stops all tracking, clears queue)
PostHog.OptOut();
// Opt back in
PostHog.OptIn();
// Check status
if (PostHog.IsOptedOut)
{
    // Show consent dialog
}
```

## Debug mode

If you're not seeing the expected events being captured or feature flags being evaluated, enable debug mode to see what's happening:

C#

PostHog AI

```csharp
PostHog.Setup(new PostHogConfig
{
    ApiKey = "<ph_project_token>",
    Host = "https://us.i.posthog.com",
    LogLevel = PostHogLogLevel.Debug
});
```

Available log levels: `None`, `Error`, `Warning`, `Info`, `Debug`

## Manual flush

Force send all queued events immediately:

C#

PostHog AI

```csharp
PostHog.Flush();
```

## Shutdown

Clean up when your app exits:

C#

PostHog AI

```csharp
void OnApplicationQuit()
{
    PostHog.Shutdown();
}
```

> **Note:** The SDK automatically flushes on app quit, so explicit shutdown is optional.

## Platform support

| Platform | Support |
| --- | --- |
| Windows/Mac/Linux | Full |
| iOS | Full |
| Android | Full |
| WebGL | With limitations* |
| Consoles | Untested |

\*WebGL uses PlayerPrefs for storage (limited size) and is subject to CORS restrictions.

## Troubleshooting

### Events not appearing in PostHog

1.  Check your API key is correct
2.  Verify the host URL matches your PostHog instance (e.g., `https://us.i.posthog.com` or `https://eu.i.posthog.com`)
3.  Set `LogLevel = PostHogLogLevel.Debug` to see detailed logs
4.  Ensure you're not opted out (`PostHog.IsOptedOut`)

### WebGL issues

-   Ensure your PostHog instance allows CORS from your domain
-   WebGL has limited storage - consider reducing `MaxQueueSize`

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better