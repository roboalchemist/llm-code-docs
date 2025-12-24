# Source: https://headscale.net/stable/usage/connect/apple/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/usage/connect/apple.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/usage/connect/apple.md "View source of this page")

# Connecting an Apple client[¶](#connecting-an-apple-client "Permanent link")

This documentation has the goal of showing how a user can use the official iOS and macOS [Tailscale](https://tailscale.com) clients with headscale.

Instructions on your headscale instance

An endpoint with information on how to connect your Apple device is also available at `/apple` on your running instance.

## iOS[¶](#ios "Permanent link")

### Installation[¶](#installation "Permanent link")

Install the official Tailscale iOS client from the [App Store](https://apps.apple.com/app/tailscale/id1470499037).

### Configuring the headscale URL[¶](#configuring-the-headscale-url "Permanent link")

- Open the Tailscale app
- Click the account icon in the top-right corner and select `Log in…`.
- Tap the top-right options menu button and select `Use custom coordination server`.
- Enter your instance url (e.g `https://headscale.example.com`)
- Enter your credentials and log in. Headscale should now be working on your iOS device.

## macOS[¶](#macos "Permanent link")

### Installation[¶](#installation_1 "Permanent link") 

Choose one of the available [Tailscale clients for macOS](https://tailscale.com/kb/1065/macos-variants) and install it.

### Configuring the headscale URL[¶](#configuring-the-headscale-url_1 "Permanent link") 

#### Command line[¶](#command-line "Permanent link")

Use Tailscale\'s login command to connect with your headscale instance (e.g `https://headscale.example.com`):

    tailscale login --login-server <YOUR_HEADSCALE_URL>

#### GUI[¶](#gui "Permanent link")

- Option + Click the Tailscale icon in the menu and hover over the Debug menu
- Under `Custom Login Server`, select `Add Account...`
- Enter the URL of your headscale instance (e.g `https://headscale.example.com`) and press `Add Account`
- Follow the login procedure in the browser

## tvOS[¶](#tvos "Permanent link")

### Installation[¶](#installation_2 "Permanent link") 

Install the official Tailscale tvOS client from the [App Store](https://apps.apple.com/app/tailscale/id1470499037).

Danger

**Don\'t** open the Tailscale App after installation!

### Configuring the headscale URL[¶](#configuring-the-headscale-url_2 "Permanent link") 

- Open Settings (the Apple tvOS settings) \> Apps \> Tailscale
- Under `ALTERNATE COORDINATION SERVER URL`, select `URL`
- Enter the URL of your headscale instance (e.g `https://headscale.example.com`) and press `OK`
- Return to the tvOS Home screen
- Open Tailscale
- Click the button `Install VPN configuration` and confirm the appearing popup by clicking the `Allow` button
- Scan the QR code and follow the login procedure