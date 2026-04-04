---
---
title: Angular
description: "Learn how to set up Sentry in your Angular application and capture your first errors."
---

## Prerequisites

You need:

- A Sentry [account](https://sentry.io/signup/) and [project](/product/projects/)
- Your application up and running
- Angular version `17.0.0` or above

If you're using Angular 16 or older, install and Set Up the SDK Manually. The Sentry Angular SDK still works for Angular versions 14 and newer but the installation wizards requires
at least Angular 17.

## Step 1: Install

To install Sentry, run the following command within your project:

```bash
npx @sentry/wizard@latest -i angular
```

The wizard then guides you through the setup process, asking you to enable additional (optional) Sentry features for your application beyond error monitoring.

This guide assumes that you enable all features and allow the wizard to add an example component to your application. You can add or remove features at any time, but setting them up now will save you the effort of configuring them manually later.

- Adds a `Sentry.init()` call into your `main.ts` file
- Registers the Sentry `ErrorHandler` and `TraceService` in your `app.config.ts` file
- Creates `.sentryclirc` with an auth token to upload source maps (this file is automatically added to `.gitignore`)
- Walks you through enabling source maps upload when making a production build, locally as well as in CI
- Adds an example component to your application to help verify your Sentry setup

## Step 2: Avoid Ad Blockers With Tunneling (Optional)

## Step 3: Verify

If you haven't tested your Sentry configuration yet, let's do it now. You can confirm that the Sentry SDK is sending data to your Sentry project by using the example component created by the installation wizard:

1. Open the page you added the example component to in your browser.
2. Click the "Throw error" button. This triggers an error.

Sentry captures this error for you. Additionally, the button click starts a trace to measure the time it takes for the error to be thrown.

Don't forget to explore the example component's code in your project to understand what's happening after your button click.

### View Captured Data in Sentry

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

## Next Steps

At this point, you should have integrated Sentry into Angular application and should already be sending error and tracing data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics.
Our next recommended steps for you are:

- Extend Sentry to your backend using one of our [SDKs](/)
- Continue to customize your configuration
- Make use of Angular-specific features
- Learn how to manually capture errors

- If you encountered issues with our installation wizard, try setting up Sentry manually
- [Get support](https://sentry.zendesk.com/hc/en-us/)

