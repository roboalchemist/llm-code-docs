# Source: https://docs.hoppscotch.io/documentation/clients/desktop.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.hoppscotch.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Hoppscotch Desktop App

> Cross-platform desktop application that runs on macOS, Windows, and Linux.

Hoppscotch Desktop App is a cross-platform desktop application that helps you create and manage API requests. It is built on top of the [Hoppscotch Web Client](/documentation/clients/web) and is powered by [Tauri](https://tauri.app).

<Frame>
  <img className="block border border-black/5 rounded-md dark:border-white/5 dark:hidden" src="https://mintcdn.com/hoppscotch/WCaaGbVhL02n1fVh/images/hoppscotch-light.png?fit=max&auto=format&n=WCaaGbVhL02n1fVh&q=85&s=c4d7d5571a6a500ddaa3194486100a3c" width="1697" height="960" data-path="images/hoppscotch-light.png" />

  <img className="hidden border border-black/5 rounded-md dark:border-white/5 dark:block" src="https://mintcdn.com/hoppscotch/WCaaGbVhL02n1fVh/images/hoppscotch-dark.png?fit=max&auto=format&n=WCaaGbVhL02n1fVh&q=85&s=c91e23909f2e7196f56560a16b6b5a2a" width="1697" height="960" data-path="images/hoppscotch-dark.png" />
</Frame>

## Download Hoppscotch Desktop App

Download the latest version of Hoppscotch Desktop App for your operating system:

<AccordionGroup>
  <Accordion title="Mac" icon="apple">
    <Card title="Apple Silicon (.dmg)" href="https://github.com/hoppscotch/releases/releases/latest/download/Hoppscotch_mac_aarch64.dmg">
      Download for Apple Silicon-based Mac.
    </Card>

    <Card title="Intel (.dmg)" href="https://github.com/hoppscotch/releases/releases/latest/download/Hoppscotch_mac_x64.dmg">
      Download for Intel-based Mac.
    </Card>
  </Accordion>

  <Accordion title="Windows" icon="windows">
    <Card title="Windows Installer (.msi)" href="https://github.com/hoppscotch/releases/releases/latest/download/Hoppscotch_win_x64.msi">
      Download the installer for Windows (64-bit).
    </Card>

    <Card title="Windows Portable (.exe)" href="https://github.com/hoppscotch/releases/releases/latest/download/Hoppscotch_Cloud_win_x64_portable.zip">
      Download the portable version for Windows (64-bit).
    </Card>
  </Accordion>

  <Accordion title="Linux" icon="linux">
    <Card title="Debian (.deb)" href="https://github.com/hoppscotch/releases/releases/latest/download/Hoppscotch_linux_x64.deb">
      Download the Debian package for Debian-based Linux distributions.
    </Card>

    <Card title="App Image (.AppImage)" href="https://github.com/hoppscotch/releases/releases/latest/download/Hoppscotch_linux_x64.AppImage">
      Download the AppImage for Linux.
    </Card>
  </Accordion>
</AccordionGroup>

## Install Hoppscotch Desktop App

1. Download the latest version of Hoppscotch Desktop App from the links above or from [official website](https://hoppscotch.com/download).
2. Open the downloaded file.
3. Follow the on-screen instructions to install Hoppscotch Desktop App.
4. Open Hoppscotch Desktop App.
5. If you see a warning message, click "**Open**".

## Access Hoppscotch

### Hoppscotch Cloud Edition for Individuals

Seamlessly access Hoppscotch Cloud Edition from Hoppscotch Desktop App:

1. Open Hoppscotch Desktop App.
2. Click the Hoppscotch logo in the top-left corner.
3. Click "**HOPPSCOTCH CLOUD**".
4. Sign in with your Hoppscotch Cloud account to access your workspaces and collections.

### Hoppscotch Cloud Edition for Organizations

<Note>
  This feature is coming soon.
</Note>

### Hoppscotch Self-Hosted Edition for Community

<Warning>
  To enable desktop app support for your self-hosted Hoppscotch instance, make sure to update the `WHITELISTED_ORIGINS` environment variable in your `.env` file with your deployment URL.
</Warning>

<Note>
  e.g. to allow connection to `https://hoppscotch.my-domain.com` you need to add `app://hoppscotch_my_domain_com` and `http://app.hoppscotch_my_domain_com` to the `WHITELISTED_ORIGINS` environment variable.

  ```bash  theme={null}
  WHITELISTED_ORIGINS=...existing_origins,app://hoppscotch_my_domain_com,http://app.hoppscotch_my_domain_com
  ```

  <Tip>
    *app\://hoppscotch\_my\_domain\_com*   for Linux and macOS machines.
  </Tip>

  <Tip>
    *http\://app.hoppscotch\_my\_domain\_com*   for Windows machine.
  </Tip>
</Note>

Add your self-hosted Hoppscotch Community Edition instance to Hoppscotch Desktop App:

1. Open Hoppscotch Desktop App.
2. Click the Hoppscotch logo in the top-left corner.
3. Click "**Add an instance**".
4. Enter the URL of your self-hosted Hoppscotch instance.
5. Click "**Connect**".

<Tip>You can also self-host Hoppscotch Desktop App. Follow the instructions in the [Hoppscotch GitHub repository](https://github.com/hoppscotch/hoppscotch/tree/main/packages/hoppscotch-desktop).</Tip>

### Hoppscotch Self-Hosted Edition for Enterprise

<Warning>
  To enable desktop app support for your self-hosted Hoppscotch instance, make sure to update the `WHITELISTED_ORIGINS` environment variable in your `.env` file with your deployment URL.
</Warning>

<Note>
  e.g. to allow connection to `https://hoppscotch.my-domain.com` you need to add `app://hoppscotch_my_domain_com` and `http://app.hoppscotch_my_domain_com` to the `WHITELISTED_ORIGINS` environment variable.

  ```bash  theme={null}
  WHITELISTED_ORIGINS=...existing_origins,app://hoppscotch_my_domain_com,http://app.hoppscotch_my_domain_com
  ```

  <Tip>
    *app\://hoppscotch\_my\_domain\_com*   for Linux and macOS machines.
  </Tip>

  <Tip>
    *http\://app.hoppscotch\_my\_domain\_com*   for Windows machine.
  </Tip>
</Note>

Add your self-hosted Hoppscotch Enterprise Edition instance to Hoppscotch Desktop App:

1. Open Hoppscotch Desktop App.
2. Click the Hoppscotch logo in the top-left corner.
3. Click "**Add an instance**".
4. Enter the URL of your self-hosted Hoppscotch instance.
5. Click "**Connect**".

<Tip>You can also self-host Hoppscotch Desktop App. Follow the instructions in the [Hoppscotch GitHub repository](https://github.com/hoppscotch/hoppscotch/tree/main/packages/hoppscotch-desktop).</Tip>


Built with [Mintlify](https://mintlify.com).