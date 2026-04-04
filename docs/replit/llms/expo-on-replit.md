# Source: https://docs.replit.com/tutorials/expo-on-replit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Building Mobile Apps with Expo and Replit

> Replit is the fastest way to create and publish cross-platform mobile apps using Expo, without any setup or configuration.

Apps are the new websites, and everyone should be able to create them. By combining Replit's browser-based development environment [with Expo](https://expo.dev/blog/from-idea-to-app-with-replit-and-expo), mobile app creation is now as simple as building a website.

<Note>
  This tutorial will guide you through creating a mobile app using Replit and Expo, from setting up your environment to publishing your app to your device.
</Note>

Watch Replit's two-part video series to learn how to create and publish a mobile app using Replit and Expo.

## Part 1: Create a mobile app in five minutes

Learn how to create a native iPhone/Android app using Replit and Expo in just five minutes - perfect for beginners.

<Frame>
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/mTm_dCF53qk" title="Create a MOBILE app in 5 minutes with Replit and Expo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
</Frame>

### Getting started with Replit and Expo

<Steps>
  <Step title="Prerequisites">
    Before getting started, you'll need:

    * A Replit account (free)
    * [Expo Go app](https://expo.dev/go) installed on your mobile device
    * An Expo EAS account (free)

    For publishing to App Stores later, you'll need:

    * An [Apple Developer account](https://developer.apple.com/programs/) (\$99/year) for iOS
    * A [Google Play Developer account](https://play.google.com/console/signup) (\$25 one-time) for Android
  </Step>

  <Step title="Remix the Template">
    Start by visiting the [Expo Template on Replit](https://replit.com/@replit/Expo?v=1) and selecting "Remix" to create your own copy. This creates a complete copy of the Template in your Replit account, including all the files, configurations, and dependencies.
  </Step>

  <Step title="Run the Template">
    Select the "Run" button in your Workspace. The Console will display a QR code that links the Expo Go app to your Replit project.
  </Step>

  <Step title="Preview on your device">
    Open the Expo Go app on your phone and scan the QR code displayed in your Workspace. This will load your app directly on your phone. It may take a minute or two for the project to compile.
  </Step>
</Steps>

Expo uses React Native to help you build apps for iOS, Android, and the web from a single codebase. This means you can build an app once and have it available on all platforms.

<Note>
  The democratization of mobile development through Replit and Expo makes app creation accessible to everyone, not just professional developers.
</Note>

### Customizing your app with Agent

<Steps>
  <Step title="Choose your AI tool">
    Use [Agent](/replitai/agent) to build your Expo app:

    * **Build mode**: Best for complex features and major changes. The Expo template uses [General Agent](/replitai/general-agent), which supports any framework.
    * **Fast mode**: Best for smaller changes and code explanations.
    * **Plan mode**: Best for planning and brainstorming.
  </Step>

  <Step title="Use natural language to build your app">
    Describe what you want your app to do in natural language. For example, you might ask: "Create an app that shows me a random image of a cat every time I press a button."
  </Step>

  <Step title="Iterate on mobile">
    One of the most powerful features is the ability to continue developing on your mobile device:

    1. Open the Replit Mobile App
    2. Find your project
    3. Use Agent to make changes and improvements
    4. See updates appear in real-time
  </Step>
</Steps>

<Tip>
  Want to build a mobile app from scratch with Agent? Check out [Building
  Mobile Apps with Agent](/replitai/building-mobile-apps) to learn about
  creating Expo React Native apps directly from the Replit homepage.
</Tip>

## Part 2: Publish your mobile app

Learn how to deploy your Replit Expo app to iOS in under 10 minutes - from development to installation on your iPhone.

<Frame>
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/wLQusAwfjdY" title="PUBLISH your mobile app with Replit and Expo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
</Frame>

### Publishing your app to your device

<Note>
  While this guide focuses on iOS deployment, the same Replit and Expo steps apply to Android development. For Android, follow the [Expo Android deployment guide](https://docs.expo.dev/build/setup/) and [Google Play Console process](https://play.google.com/console/about/).
</Note>

<Steps>
  <Step title="Prerequisites">
    Before publishing, you'll need:

    * Your Replit App from Part 1
    * An [Apple Developer account](https://developer.apple.com/programs/) (\$99/year) if publishing to iOS
    * An iPhone (for iOS deployment)
    * An [Expo account](https://expo.dev/signup)

    Note: After setting up your Apple Developer account, you may need to wait 16-24 hours for Apple to approve your profile.
  </Step>

  <Step title="Initialize EAS">
    [EAS (Expo Application Services)](https://docs.expo.dev/eas/) acts as the interface between your build and Expo, as well as the App Store.

    1. Stop your app if it's running
    2. From the dropdown menu in your Workspace, select "EAS init"
    3. Log in to your Expo account when prompted
    4. Create a new project or select an existing one

    This step authenticates your application with your Expo account.
  </Step>

  <Step title="Run EAS update">
    This initialization step helps configure your project and link it to your Apple Developer account.

    1. From the dropdown menu, select "EAS update"
    2. Wait for the Metro bundler to start and complete the export process

    You'll know this step is successful when you see that bundles have been uploaded and a branch has been created.
  </Step>

  <Step title="Build for iOS">
    Now it's time to create a preview build for your iOS device.

    1. From the dropdown menu, select "EAS publish preview iOS"
    2. Enter an iOS bundle identifier (e.g., com.yourname.yourappname)
    3. Log in to your [App Store Connect](https://appstoreconnect.apple.com/) account when prompted
    4. Select your individual developer team
    5. Generate the device distribution certificates when asked

    Learn more about [iOS certificates and provisioning profiles](https://docs.expo.dev/app-signing/ios-certificates/).
  </Step>

  <Step title="Register your device">
    To install development apps on your iPhone, you need to register your device.

    1. When prompted, select "website" to register your device
    2. Scan the QR code that appears with your iPhone
    3. Download the development profile when prompted
    4. Go to Settings on your iPhone
    5. Select "Profile Downloaded" at the top
    6. Install the profile and enter your passcode when prompted
    7. Go back to your Workspace and press any key to continue
  </Step>

  <Step title="Wait for the build">
    Expo will now build your app, which takes about 10-15 minutes depending on the complexity of your application.

    1. The build will be queued
    2. You can check progress in your [Expo dashboard](https://expo.dev) under the "Builds" tab
    3. Once complete, a new QR code will appear for installing the app
  </Step>

  <Step title="Install the app on your device">
    When the build is complete, install the app on your iPhone.

    1. Scan the installation QR code with your iPhone
    2. Select "Install" when prompted
    3. The app will begin installing on your home screen
  </Step>

  <Step title="Enable developer mode">
    Before you can open the app, you need to enable developer mode on your iPhone.

    1. Go to Settings > Privacy & Security
    2. Scroll to the bottom and find "Developer Mode"
    3. Toggle it on
    4. Restart your device when prompted
    5. After restarting, you can open and use your app!
  </Step>
</Steps>

## What you've accomplished

By following this tutorial, you now have a real, native mobile app on your device. Most developers would need days or weeks to achieve this, but you've done it in about an hour.

<Accordion title="Next steps">
  After completing this tutorial, you can:

  * Continue refining your app with more features
  * Add [authentication](https://docs.expo.dev/develop/authentication/) and data storage
  * Implement native device features like [camera](https://docs.expo.dev/versions/latest/sdk/camera/) or [location](https://docs.expo.dev/versions/latest/sdk/location/)
  * [Submit your app to the App Store](https://docs.expo.dev/deploy/submit-to-app-stores/) for public distribution
  * Create an Android version using similar steps
</Accordion>

### Common issues and solutions

<AccordionGroup>
  <Accordion title="App won't connect to Expo Go">
    * Ensure your phone and computer are on the same Wi-Fi network
    * Try using ["Tunnel" connection mode](https://docs.expo.dev/more/expo-cli/?redirected#tunneling) instead of "LAN"
    * Check if your firewall is blocking connections
    * See [Expo's troubleshooting guide](https://docs.expo.dev/troubleshooting/networking/)
  </Accordion>

  <Accordion title="Changes not reflecting in app">
    * Try reloading the app (shake device and select "Reload")
    * Ensure you've saved your changes in your Workspace
    * Check the Console for any errors
    * Review [Expo's development mode documentation](https://docs.expo.dev/workflow/development-mode/)
  </Accordion>

  <Accordion title="Build fails on EAS">
    * Verify your [app.json configuration](https://docs.expo.dev/workflow/configuration/)
    * Check if all dependencies are compatible
    * Ensure you have the correct [permissions](https://docs.expo.dev/guides/permissions/) set up
    * Review any error messages in the build logs
    * See [EAS Build troubleshooting](https://docs.expo.dev/build-reference/troubleshooting/)
  </Accordion>
</AccordionGroup>

### Conclusion

With Replit and Expo, building mobile apps has never been easier or faster. You can go from idea to app in a matter of hours, not weeks or months. The combination of browser-based development and cross-platform mobile framework removes traditional barriers to entry for mobile development.

<Note>
  For more detailed information, check out:

  * [Expo documentation](https://docs.expo.dev/)
  * [React Native documentation](https://reactnative.dev/docs/getting-started)
  * [Apple App Store guidelines](https://developer.apple.com/app-store/guidelines/)
  * [Google Play Store guidelines](https://play.google.com/console/about/guides/)
  * [Replit documentation](https://docs.replit.com/)
</Note>
