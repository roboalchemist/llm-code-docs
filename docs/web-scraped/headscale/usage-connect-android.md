# Source: https://headscale.net/stable/usage/connect/android/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/usage/connect/android.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/usage/connect/android.md "View source of this page")

# Connecting an Android client[¶](#connecting-an-android-client "Permanent link")

This documentation has the goal of showing how a user can use the official Android [Tailscale](https://tailscale.com) client with headscale.

## Installation[¶](#installation "Permanent link")

Install the official Tailscale Android client from the [Google Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) or [F-Droid](https://f-droid.org/packages/com.tailscale.ipn/).

## Connect via normal, interactive login[¶](#connect-via-normal-interactive-login "Permanent link")

- Open the app and select the settings menu in the upper-right corner
- Tap on `Accounts`
- In the kebab menu icon (three dots) in the upper-right corner select `Use an alternate server`
- Enter your server URL (e.g `https://headscale.example.com`) and follow the instructions
- The client connects automatically as soon as the node registration is complete on headscale. Until then, nothing is visible in the server logs.

## Connect using a preauthkey[¶](#connect-using-a-preauthkey "Permanent link")

- Open the app and select the settings menu in the upper-right corner
- Tap on `Accounts`
- In the kebab menu icon (three dots) in the upper-right corner select `Use an alternate server`
- Enter your server URL (e.g `https://headscale.example.com`). If login prompts open, close it and continue
- Open the settings menu in the upper-right corner
- Tap on `Accounts`
- In the kebab menu icon (three dots) in the upper-right corner select `Use an auth key`
- Enter your [preauthkey generated from headscale](../../getting-started/#using-a-preauthkey)
- If needed, tap `Log in` on the main screen. You should now be connected to your headscale.