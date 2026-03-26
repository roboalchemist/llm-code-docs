# Source: https://momentic.ai/docs/mobile-cli/emulators.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Emulators

> Learn about the different emulator options offered by Momentic.

Momentic offers two options for automating Android apps.

**Remote** emulators are hosted through a third-party provider and offer a
scalable fleet of instances that boot within seconds. Simply upload the APK you
wish to test, and we'll take care of the rest.

**Local** emulators use your local Android Studio installation to create an
emulator that runs on your own machine. In this setup, you'll have to specify an
[Android Virtual Device](https://developer.android.com/studio/run/managing-avds)
(AVD) and APK file that already exist locally.

## Choosing a platform

We recommend that teams use either remote or local emulators for all tests, and
avoid mixing the two.

The platform can be chosen when creating or editing a test through the Region
dropdown menu. Choosing the `Local` region activates the local emulator mode;
selecting any other region activates the remote emulator mode.

## Remote emulators

When using remote emulators, Momentic provides fresh Android instances on-demand
when launching the local app or executing a mobile test. Average provisioning
time is under 1 second.

### Configuration

#### APK

APK installation for remote emulators is managed through **channels** and
**tags**. APKs can be uploaded through the Momentic Mobile app in the Assets
page, or via the `momentic-mobile assets upload`
[command](/mobile-cli/commands/assets).

<Warning>
  If the uploaded APK contains Android `WebView` content that you want to
  automate, enable WebView debugging with
  `WebView.setWebContentsDebuggingEnabled(true)` so Momentic can attach to the
  WebView.
</Warning>

Channels are generally distinct release environments, such as `dev`, `staging`,
and `production`. You can also use channels to separate different apps, such as
`production-trading` and `production-banking`.

Tags are versions within a particular channel. We recommend that teams use
[semver](https://semver.org/) tags, such as `0.0.1` and `1.2.0`, or some other
identifier that can be easily tied to code changes.

When creating or editing a test that uses remote emulators, you will be prompted
to choose a channel and tag.

#### Region

The Region property on each test's settings defines where your emulator will be
created. If unset, the closest region to your IP address will be chosen.

Currently, Momentic's emulator provider supports two regions: US West and EU
North. If you are located far away from both regions, we highly recommend using
local emulators instead for improved latency.

#### Android version

Currently, Android 14 and 15 are supported. This setting can be configured in
each test's options.

## Local emulators

### Configuration

When using local emulators, users are responsible for building, storing, and
sharing AVDs that have the desired settings, including the Android version, Play
Store version, and device size. Users then provide this AVD ID to Momentic.

To install an APK, there are several options:

1. **Install APK step**: Given an APK path that is accessible on disk, you can
   use a preset `Install APK` step at any point in a test.
2. **Test-level APK path setting**: An APK path can be specified in each test's
   settings. This APK will be automatically installed on emulator start.
3. **Inherit APK settings from the environment**: see the section
   [below](#environment-based-settings) on how to read configuration from
   environment variables.

### Environment-based settings

Some teams may not share APKs or AVDs during development. In this case, it can
be cumbersome to constantly change the AVD ID or APK path at the test level.

Configuring these settings at the environment level instead solves this problem.
Specifically, rather than setting AVD ID or APK path at the test level, users
can define the `LOCAL_AVD_ID` and `LOCAL_APK_PATH` keys in an environment. Then,
users can leverage Momentic's ability to interpolate environment variables using
the shell to achieve dynamic behavior on each developer's machine.

For example, the environment below will first read the `LOCAL_AVD_ID` from the
`MOMENTIC_AVD_ID` env var from the surrounding shell, and default to
`Pixel_9_API_35` if this env var is unset. Similarly, the local APK path will
first be read from the `MOMENTIC_APK_PATH` env var.

```yaml momentic.config.yaml theme={null}
environments:
  - name: local
    envVariables:
      LOCAL_AVD_ID: ${MOMENTIC_AVD_ID:-Pixel_9_API_35}
      LOCAL_APK_PATH: ${MOMENTIC_APK_PATH:-../../data/android-test-apks/drag-drop-native/app-debug.apk}
```

Each developer then can set their own `MOMENTIC_AVD_ID` and `MOMENTIC_APK_PATH`
in a `.env` file or in their `~/.zshrc`, avoiding the need to commit these
configuration changes to source control.

Note that environment-based configuration is only active if the test is set to
run in that environment. In addition, there cannot be any overrides at the test
level.

### Overrides in CI

When executing tests in CI, Momentic's [run](/mobile-cli/commands/run) command
supports the `--local-avd-id` and `--local-apk-path` flags to make overriding
local emulator configuration easy. These flags take precedence over all other
configuration.


Built with [Mintlify](https://mintlify.com).