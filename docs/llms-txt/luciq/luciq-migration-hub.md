# Source: https://docs.luciq.ai/getting-started/luciq-migration-hub.md

# Migrate Instabug SDK To Luciq SDK

Welcome to the next chapter of our journey together. As you may know, Instabug is evolving. We are thrilled to introduce Luciq, our new identity as the Agentic Observability Platform for Mobile.

This is more than just a name change; it's a strategic evolution of our entire platform, designed to empower you to spend less time firefighting, and more time innovating the things that matter. To deliver on this new vision, our SDK has been completely rebranded. This guide will walk you through the simple, one-time process of migrating your application from the legacy Instabug SDK to the new Luciq SDK.

### Why Migrate to the Luciq SDK?

Upgrading ensures you stay on the edge of mobile observability and continue to receive the full value of our platform. By migrating, you will:

* **Stay Up-to-Date:** Starting today, the legacy Instabug SDK will no longer receive new features or product updates. Critical updates and hotfixes will continue but only until January 2026 - after which that ends. Beyond then, it will continue to work normally as is, but migrating ensures you are on the actively maintained and evolving platform.
* **Unlock New AI-Powered Features:** All future innovation, including our new assistive AI Agents and performance improvements, will be released exclusively on the Luciq SDK.
* **Align with Our Future Vision:** The Luciq SDK is the new foundation of our platform. Upgrading ensures your application is ready for the future of agentic observability and the powerful new workflows we're building.

***

### What to Expect During the Migration?

We have invested heavily in making this a low-effort, predictable process for your development team.

This is a one-time breaking change that involves updating your application's dependency from Instabug to Luciq, and renaming all API calls. For the vast majority of projects, the process is straightforward and can be completed quickly.

**The High-Level Steps:**

* **Update Your Dependency:** Change your project's configuration (e.g., Podfile, build.gradle) to point to the new Luciq SDK package.
* **Run the Automated Migration Script:** We've built a powerful script for each platform that handles roughly 90% of the required code changes automatically.
* **Review & Test:** Follow our platform-specific guide (guides linked below) to handle any edge cases, review the automated changes, and test your application.

For a medium-complexity project, we estimate the entire process, including running the script and testing, to be around **2-3 hours.**

***

### Your Platform-Specific Migration Path

To get started, please select the detailed, step-by-step guide for your specific platform.

**Safety First:** This is a one-time migration that will modify your source code. Before you begin, it is **critical** that you commit all your work to a version control system like Git. This ensures you have a safe backup and can easily review all changes before finalizing them.

Each platform guide begins with a preflight checklist, instructions for using the automated script, and full mapping tables for all API changes - should you proceed with a manual migration or need to fallback to it for overtly complex projects.

At a glance, here are the key areas that will be updated for each platform:

| **Platform**     | **Key Files & Areas Affected**                                     |
| ---------------- | ------------------------------------------------------------------ |
| **iOS**          | `Podfile, .swift/.m files, info.plist`                             |
| **Android**      | `build.gradle, .kt/.java files, AndroidManifest.xml`               |
| **React Native** | `package.json, .js/.ts files, plus all native iOS & Android files` |
| **Flutter**      | `pubspec.yaml, .dart files, plus all native iOS & Android files`   |

Below, you can find the detailed guide for each of our supported platforms:

1. [**iOS Migration Guide**](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/ios-luciq-migration)**:** Migrate your CocoaPods/SPM dependency and update your code from `Instabug.*` and the `IBG*` prefix to `Luciq.*` and the new `LCQ*` prefix.
2. [**Android Migration Guide**](https://app.gitbook.com/s/zyyZGn3dXyNyX4fbdQmV/android-luciq-migration)**:** Migrate your Maven dependency and Gradle plugin, and update your code from `Instabug.*` and the `IBG*` prefix to `Luciq.*`.
3. [**React Native Migration Guide**](https://app.gitbook.com/s/6lIBifTCHAMDxXnztiBK/react-native-luciq-migration)**:** Migrate your npm package from `instabug-reactnative` to `@luciq/react-native` and update your JavaScript and native code.
4. [**Flutter Migration Guide**](https://app.gitbook.com/s/XBLFPXoq7NuMGLdJ6oPk/flutter-luciq-migration)**:** Migrate your pub.dev package from `instabug_flutter` to `luciq_flutter` and update your Dart code.

<br>
