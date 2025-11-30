# Source: https://developer.1password.com/docs/sdks/desktop-app-integrations

On this page

# Use the 1Password desktop app to authenticate 1Password SDKs [Beta]

You can now set up your 1Password SDK integrations to authenticate using secure, local authorization prompts from the 1Password desktop app. During the public beta, you can:

- Build integrations that require minimal setup from end users. Your users can authorize your integration the same way they unlock their 1Password app, like with biometric unlock, their 1Password account password, or other supported methods.
- Enable human-in-the-loop approval for sensitive workflows. Prompts from 1Password clearly detail which account the integration will access and the scope and duration of that access.
- Allow users to securely grant your integration temporary access to their entire 1Password account while the 1Password desktop app is unlocked. Access expires after 10 minutes of inactivity or when the user locks their account in the app.

![A screenshot of a Python script running with an authorization prompt from the 1Password desktop app.](/img/sdks/sdk-auth-prompt.png)![A screenshot of a Python script running with an authorization prompt from the 1Password desktop app.](/img/sdks/sdk-auth-prompt.png)

## Requirements[â€‹](#requirements "Direct link to Requirements") 

- [1Password subscription](https://1password.com/pricing/password-manager).
- The latest [beta release](https://support.1password.com/betas#install-a-prerelease-version-of-the-1password-app) of the 1Password desktop app.
- To use the desktop app integration with Python, you\'ll need Python version 3.10 or later.

## Step 1: Turn on the integration in the 1Password app[â€‹](#step-1-turn-on-the-integration-in-the-1password-app "Direct link to Step 1: Turn on the integration in the 1Password app") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]tip

To get the latest [beta release](https://support.1password.com/betas#install-a-prerelease-version-of-the-1password-app) of the 1Password desktop app, select your account or collection at the top of the sidebar, then select **Settings** \> **Advanced** and set \"Release channel\" to **Beta**. Then navigate to **Settings** \> **About** \> **Check for updates** and restart the app when prompted.

If you don\'t see the option to update to the latest beta in the app, you can download it directly for [Mac](https://releases.1password.com/mac/beta/) or [Linux](https://releases.1password.com/linux/beta/).

- Mac
- Linux

1.  Open and unlock the [1Password app](https://1password.com/downloads/).
2.  Select your account or collection at the top of the sidebar.
3.  Navigate to **Settings** \> **[Developer](onepassword://settings/developers)**.
4.  Under Integrate with the 1Password SDKs, select **Integrate with other apps**.
5.  If you want to authenticate with Touch ID, navigate to **Settings** \> **[Security](onepassword://settings/security)**, then turn on **[Touch ID](https://support.1password.com/touch-id-mac/)**.

![The Integrate with other apps setting](/img/sdks/app-integration-setting-full-light.png)![The Integrate with other apps setting](/img/sdks/app-integration-setting-full-dark.png)

1.  Open and unlock the [1Password app](https://1password.com/downloads/).
2.  Select your account or collection at the top of the sidebar.
3.  Navigate to **Settings** \> **[Developer](onepassword://settings/developers)**.
4.  Under Integrate with the 1Password SDKs, select **Integrate with other apps**.
5.  If you want to authenticate the same way you sign in to your Linux account, navigate to **Settings** \> **[Security](onepassword://settings/security)**, then turn on **[Unlock using system authentication](https://support.1password.com/system-authentication-linux/)**.

![The Integrate with other apps setting](/img/sdks/app-integration-setting-full-light.png)![The Integrate with other apps setting](/img/sdks/app-integration-setting-full-dark.png)

## Step 2: Install the beta SDK[â€‹](#step-2-install-the-beta-sdk "Direct link to Step 2: Install the beta SDK") 

The beta is available on the `sdk-for-desktop-integrations` branch in each 1Password SDK repository ([Go](https://github.com/1Password/onepassword-sdk-go/tree/sdks-for-desktop-integrations), [Python](https://github.com/1Password/onepassword-sdk-python/tree/sdks-for-desktop-integrations), [JS](https://github.com/1Password/onepassword-sdk-js/tree/sdks-for-desktop-integrations)). You\'ll need to install the SDK from that branch.

- Go
- JavaScript
- Python

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Then import the SDK into your project. If you have an existing project, you don\'t need to change your import statements.

- Go
- JavaScript
- Python

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

#### CommonJS

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

#### ES Modules

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

## Step 3: Connect your project to the 1Password app[â€‹](#step-3-connect-your-project-to-the-1password-app "Direct link to Step 3: Connect your project to the 1Password app") 

To get started with the beta SDK, you\'ll create a client instance that authenticates using the 1Password desktop app.

Replace [YourAccountNameAsShownInTheDesktopApp] in the code below with the name of your account as it appears at the top of the left sidebar in the 1Password desktop app. You can also use your account UUID.

You can additionally configure your client to [authenticate with service accounts](/docs/sdks#step-5-initialize-the-sdk) if you want to use both authentication methods.

- Go
- JavaScript
- Python

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

## Step 4: Test authentication with the 1Password app[â€‹](#step-4-test-authentication-with-the-1password-app "Direct link to Step 4: Test authentication with the 1Password app") 

To test the new authentication method, build a simple project that requires access to 1Password, or configure an existing project to authenticate with the 1Password desktop app.

When you run your integration, 1Password will prompt you to authenticate. You\'ll need to reauthorize after ten minutes and authorize each process separately. If your account locks, you\'ll need to unlock your 1Password desktop app and run the integration again.

The following example lists all the vaults in your account. Make sure to replace [YourAccountNameAsShownInTheDesktopApp] with the account name you see at the top left of the sidebar in the 1Password app.

- Go
- JavaScript
- Python

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIGQ9Ik0xNSwzLjQxNDIxMzU2IEwxNSw3IEwxOC41ODU3ODY0LDcgTDE1LDMuNDE0MjEzNTYgWiBNMTksOSBMMTUsOSBDMTMuODk1NDMwNSw5IDEzLDguMTA0NTY5NSAxMyw3IEwxMywzIEw1LDMgTDUsMjEgTDE5LDIxIEwxOSw5IFogTTUsMSBMMTUuNDE0MjEzNiwxIEwyMSw2LjU4NTc4NjQ0IEwyMSwyMSBDMjEsMjIuMTA0NTY5NSAyMC4xMDQ1Njk1LDIzIDE5LDIzIEw1LDIzIEMzLjg5NTQzMDUsMjMgMywyMi4xMDQ1Njk1IDMsMjEgTDMsMyBDMywxLjg5NTQzMDUgMy44OTU0MzA1LDEgNSwxIFogTTExLjcwNzEwNjgsMTUuMjkyODkzMiBMMTAuMjkyODkzMiwxNi43MDcxMDY4IEw2LjU4NTc4NjQ0LDEzIEwxMC4yOTI4OTMyLDkuMjkyODkzMjIgTDExLjcwNzEwNjgsMTAuNzA3MTA2OCBMOS40MTQyMTM1NiwxMyBMMTEuNzA3MTA2OCwxNS4yOTI4OTMyIFogTTEyLjI5Mjg5MzIsMTIuNzA3MTA2OCBMMTMuNzA3MTA2OCwxMS4yOTI4OTMyIEwxNy40MTQyMTM2LDE1IEwxMy43MDcxMDY4LDE4LjcwNzEwNjggTDEyLjI5Mjg5MzIsMTcuMjkyODkzMiBMMTQuNTg1Nzg2NCwxNSBMMTIuMjkyODkzMiwxMi43MDcxMDY4IFoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=)example.go

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIGQ9Ik0xNSwzLjQxNDIxMzU2IEwxNSw3IEwxOC41ODU3ODY0LDcgTDE1LDMuNDE0MjEzNTYgWiBNMTksOSBMMTUsOSBDMTMuODk1NDMwNSw5IDEzLDguMTA0NTY5NSAxMyw3IEwxMywzIEw1LDMgTDUsMjEgTDE5LDIxIEwxOSw5IFogTTUsMSBMMTUuNDE0MjEzNiwxIEwyMSw2LjU4NTc4NjQ0IEwyMSwyMSBDMjEsMjIuMTA0NTY5NSAyMC4xMDQ1Njk1LDIzIDE5LDIzIEw1LDIzIEMzLjg5NTQzMDUsMjMgMywyMi4xMDQ1Njk1IDMsMjEgTDMsMyBDMywxLjg5NTQzMDUgMy44OTU0MzA1LDEgNSwxIFogTTExLjcwNzEwNjgsMTUuMjkyODkzMiBMMTAuMjkyODkzMiwxNi43MDcxMDY4IEw2LjU4NTc4NjQ0LDEzIEwxMC4yOTI4OTMyLDkuMjkyODkzMjIgTDExLjcwNzEwNjgsMTAuNzA3MTA2OCBMOS40MTQyMTM1NiwxMyBMMTEuNzA3MTA2OCwxNS4yOTI4OTMyIFogTTEyLjI5Mjg5MzIsMTIuNzA3MTA2OCBMMTMuNzA3MTA2OCwxMS4yOTI4OTMyIEwxNy40MTQyMTM2LDE1IEwxMy43MDcxMDY4LDE4LjcwNzEwNjggTDEyLjI5Mjg5MzIsMTcuMjkyODkzMiBMMTQuNTg1Nzg2NCwxNSBMMTIuMjkyODkzMiwxMi43MDcxMDY4IFoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=)example.js

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIGQ9Ik0xNSwzLjQxNDIxMzU2IEwxNSw3IEwxOC41ODU3ODY0LDcgTDE1LDMuNDE0MjEzNTYgWiBNMTksOSBMMTUsOSBDMTMuODk1NDMwNSw5IDEzLDguMTA0NTY5NSAxMyw3IEwxMywzIEw1LDMgTDUsMjEgTDE5LDIxIEwxOSw5IFogTTUsMSBMMTUuNDE0MjEzNiwxIEwyMSw2LjU4NTc4NjQ0IEwyMSwyMSBDMjEsMjIuMTA0NTY5NSAyMC4xMDQ1Njk1LDIzIDE5LDIzIEw1LDIzIEMzLjg5NTQzMDUsMjMgMywyMi4xMDQ1Njk1IDMsMjEgTDMsMyBDMywxLjg5NTQzMDUgMy44OTU0MzA1LDEgNSwxIFogTTExLjcwNzEwNjgsMTUuMjkyODkzMiBMMTAuMjkyODkzMiwxNi43MDcxMDY4IEw2LjU4NTc4NjQ0LDEzIEwxMC4yOTI4OTMyLDkuMjkyODkzMjIgTDExLjcwNzEwNjgsMTAuNzA3MTA2OCBMOS40MTQyMTM1NiwxMyBMMTEuNzA3MTA2OCwxNS4yOTI4OTMyIFogTTEyLjI5Mjg5MzIsMTIuNzA3MTA2OCBMMTMuNzA3MTA2OCwxMS4yOTI4OTMyIEwxNy40MTQyMTM2LDE1IEwxMy43MDcxMDY4LDE4LjcwNzEwNjggTDEyLjI5Mjg5MzIsMTcuMjkyODkzMiBMMTQuNTg1Nzg2NCwxNSBMMTIuMjkyODkzMiwxMi43MDcxMDY4IFoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=)example.py

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

You can find more examples on GitHub:

- [Go](https://github.com/1Password/onepassword-sdk-go/blob/beta/example/desktop_app/main.go)
- [JS](https://github.com/1Password/onepassword-sdk-js/tree/beta/examples/index-desktop.cjs)
- [Python](https://github.com/1Password/onepassword-sdk-python/blob/beta/example/desktop_app.py)

## Get help or share feedback[â€‹](#get-help-or-share-feedback "Direct link to Get help or share feedback") 

To share feedback or suggest improvements, create a New Issue in the relevant [SDK GitHub repository](https://github.com/1Password?q=onepassword-sdk&type=all&language=&sort=) using the provided template.

If you have additional questions or feedback, please reach out in the [1Password Developer Slack](https://developer.1password.com/joinslack).