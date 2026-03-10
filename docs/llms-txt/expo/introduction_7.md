# Source: https://docs.expo.dev/eas/workflows/introduction

---
modificationDate: March 01, 2026
title: Introduction to EAS Workflows
description: EAS Workflows is a CI/CD service for automating builds, updates, submissions, and tests for React Native and Expo apps.
---

# Introduction to EAS Workflows

EAS Workflows is a CI/CD service for automating builds, updates, submissions, and tests for React Native and Expo apps.

**EAS Workflows** is a CI/CD service from EAS (Expo Application Services) that lets teams automate repeated tasks such as building Android and iOS binaries, publishing over-the-air updates, submitting to app stores, running E2E tests with Maestro, and deploying web apps to EAS Hosting.

EAS Workflows run in managed cloud environments with pre-packaged job types designed specifically for mobile app development. When your EAS project is linked to GitHub, teams can trigger workflows from GitHub events (push, pull request, labels) or schedules (cron), or run them manually via the EAS CLI.

[Watch: Get Started with EAS Workflows](https://www.youtube.com/watch?v=OJ2u9tQCpr4) — Learn how to automate some of the most common processes that every app development team must tackle: creating development builds, publishing preview updates, and deploying to production.

  

## Quick start

> The `eas` commands below require EAS CLI. See [How to install EAS CLI](/eas/cli#installation) for more information.

Workflows are defined as YAML files in the **.eas/workflows/** directory at the root of your project. Each file specifies a `name`, optional triggers (`on`), and one or more `jobs` that run in the cloud. You can run a workflow with EAS CLI with the following command:

```sh
eas workflow:run .eas/workflows/your-workflow.yml
```

## Key features

-   **Pre-packaged for React Native/Expo**: Comes with ready-to-use job types (`build`, `submit`, `update`, `maestro`, `deploy`, and more) that abstract away implementation complexity
-   **No infrastructure to manage**: Runs on EAS with macOS and Linux workers, so you don't need to maintain CI servers or configure Android Studio/Xcode
-   **Unified artifact management**: All build artifacts, updates, and logs appear on EAS dashboard
-   **GitHub integration**: Trigger workflows automatically on push, pull request, or label events with branch and path filtering
-   **Faster iteration**: Combine Fingerprint, Get Build, and Update jobs to avoid redundant native builds and publish OTA (over-the-air) updates when possible
-   **E2E testing built-in**: Run Maestro tests on Android emulators and iOS simulators directly in workflows
-   **Slack notifications**: Send notifications to Slack channels when workflows run successfully or fail
-   **Repack**: Reuse an existing build's metadata and JavaScript bundle to create a compatible build faster

## Workflow trigger types

### Push workflows

Run when commits are pushed to matching branches or tags. Supports branch, tag, and path filtering with glob patterns.

### Pull request workflows

Run when pull requests are opened, updated, or labeled. Useful for preview builds and automated testing before merge.

### Scheduled workflows

Run on a cron schedule (for example, nightly builds or weekly regression tests). Scheduled workflows run on the default branch only.

### Manual workflows

Run on-demand using `eas workflow:run` command. Supports parameterized inputs for flexible execution.

## When to use EAS Workflows

| Scenario | Recommendation |
| --- | --- |
| Automate Android and iOS builds for your Expo and React Native apps | ✓ |
| Submit builds to App Store and Google Play automatically | ✓ |
| Publish over-the-air updates on every commit or merge | ✓ |
| Run E2E tests with Maestro as part of CI | ✓ |
| Trigger builds and updates from GitHub push or pull request events | ✓ |
| Deploy web apps to EAS Hosting | ✓ |
| Use fingerprint-based logic to skip redundant native builds | ✓ |
| CI/CD without managing your own infrastructure or macOS machines | ✓ |
| Highly customized pipelines with non-EAS services (such as Docker, custom runners) | ✗ |
| Matrix builds with multiple configuration variations in parallel | ✗ |
| CI/CD for non-React Native projects | ✗ |

## Frequently asked questions (FAQ)

How do workflows compare to other CI services?

EAS Workflows are designed to help you and your team release your app. It comes preconfigured with pre-packaged job types that can build, submit, update, run Maestro tests, and more. All job types run on EAS, so you'll only have to manage one set of YAML files, and all the artifacts from your job runs will appear on [expo.dev](https://expo.dev/).

Other CI services, like CircleCI and GitHub Actions, are more generalized and have the ability to do more than workflows. However, those services also require you to understand more about the implementation of each job. While that is necessary in some cases, workflows help you get common tasks done quickly by pre-packaging the most essential types of jobs for app developers. In addition, workflows are designed to provide you with the fastest possible cloud machine for the task at hand, and we're constantly updating those for you.

EAS Workflows are great for operations related to your Expo apps, while other CI/CD services will provide a better experience for other types of workflows.

Can I trigger a workflow without GitHub?

Yes. Any workflow can be run manually using `eas workflow:run` regardless of the `on` trigger configuration. You can also use scheduled triggers with cron syntax.

What cloud machines do workflows run on?

Workflows run on EAS's managed infrastructure:

-   **Linux workers**: `linux-medium` (4 vCPU, 16 GB RAM) or `linux-large` (8 vCPU, 32 GB RAM)
-   **Linux with nested virtualization** for Android emulators: `linux-medium-nested-virtualization` or `linux-large-nested-virtualization`
-   **macOS workers** for iOS builds and simulators: `macos-medium` (5 cores, 20 GB RAM) or `macos-large` (10 cores, 40 GB RAM)

Can workflows run jobs in parallel?

Yes. Jobs without dependencies run in parallel by default.

Use `needs` to specify that a job should wait for another job to succeed, or `after` to wait for a job to complete regardless of success or failure.

Can I use environment variables in workflows?

Yes. Workflows support [EAS environment variables](/eas/environment-variables) and inline `env` values. Environment variables can be referenced using `${{ env.VARIABLE_NAME }}` syntax.

What are the current limitations?

No shared workflow configurations (each workflow must be defined independently), and no matrix builds (cannot run multiple variations with different configurations in parallel). See [Limitations](/eas/workflows/limitations) for more details and updates.

Can I run custom scripts in a workflow?

Yes. [Custom jobs](/eas/workflows/syntax#custom-jobs) with `steps` let you run shell commands, use built-in functions like `eas/checkout` and `eas/install_node_modules`, and set outputs for downstream jobs.

Does EAS Workflows work with existing React Native projects?

Yes. EAS Workflows works with both [CNG (Continuous Native Generation)](/workflow/continuous-native-generation) and [existing React Native projects](/bare/overview), as long as the project is configured for EAS Build.

Considering EAS Workflows? Share the following slide in your next team meeting

Share the following slide in your next team meeting to discuss what EAS Workflows are and how they can help your team:

[

EAS Workflows CI/CD sync slide

Learn the benefits of using EAS Workflows to automate your CI/CD processes.

](/static/images/eas-workflows/eas-worfklows-slide.png)

## Get started

[Create your first workflow](/eas/workflows/get-started) — Learn how to create and run your first workflow.

[Pre-packaged jobs](/eas/workflows/pre-packaged-jobs) — Use ready-to-use jobs to build, submit, update, test, and deploy your app.

[Workflow syntax reference](/eas/workflows/syntax) — Learn about the YAML syntax for defining workflows.

[Example workflows](/eas/workflows/examples/introduction) — See common workflows for development builds, preview updates, and production deployments.
