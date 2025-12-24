# Source: https://support.anydesk.com/docs/install-anydesk

> 🦉[  Before installing AnyDesk, make sure your device is running one of the ][[**supported operating systems**]](/v1/docs/supported-operating-systems)[.]

You can use AnyDesk as a **portable (uninstalled)** or **installed** application for full functionality. For differences between installation types, see [Installation](/v1/docs/installation).

------------------------------------------------------------------------

## System requirements 

To ensure stable performance of AnyDesk, your device should meet the following requirements:

-   **Hardware-accelerated graphics card** - required for smooth rendering and session responsiveness.

-   **Full-screen mode** - improves performance by allowing exclusive GPU access.

-   **Aero theme (Windows)** - disabling Aero on Windows 7 and earlier can enhance rendering efficiency.

-   **[Mirror Driver]** (Windows XP or 7) - recommended for better screen capture and lower latency.

-   **Older systems** - on single-core or resource-limited devices, AnyDesk automatically reduces image quality (e.g., switches to 16-bit color) to maintain stability.

-   **Display settings** - adjust the **Display Quality** to \"Balance\" under session settings to optimize performance and resource usage.

-   **Network considerations** - check the **upload speed on the remote device** and the **download speed on the local device** to ensure sufficient bandwidth for smooth sessions.

------------------------------------------------------------------------

## **Installing AnyDesk** 

**Windows**

**macOS**

**Linux**

**Raspberry Pi**

**iOS/iPadOS/tvOS**

**Android/ChromeOS**

AnyDesk offers two installation formats for Windows: *executable (.exe)* and *installer (.msi)* files.

### Executable (.exe) file 

You can use the *AnyDesk executable (.exe)* file in portable or installed mode.

To install:

1.  Open the downloaded *executable (.exe)* file.

2.  In the AnyDesk window, click **Install AnyDesk**.

3.  Follow the on-screen instructions to complete the installation.

### Installer (.msi) file 

The *AnyDesk installer (.msi) file* must be installed and does not support portable use. This option installs both the client and the AnyDesk Service.

### Command-line installation 

Both installation formats support command-line options for automated deployments. For syntax and parameters, refer to [[Command-Line Interface] for Windows](/v1/docs/command-line-interface).

There are three installation options for macOS depending on your requirements:

### Full installation via DMG 

This method installs both the **AnyDesk client** and the **AnyDesk Service**, enabling features such as:

-   [Remote Access] when the user is logged out

-   Access during the user account switching

-   [Unattended Access]

-   Reconnect after system restart

To install:

1.  Open the DMG file and double-click the AnyDesk app.

2.  In the main window, click **Install Now**.

3.  Accept the **Terms and Conditions** to complete the installation.

------------------------------------------------------------------------

### Portable installation 

This option installs only the **AnyDesk client.** The AnyDesk Service is not included, which limits certain features such as:

-   Reconnecting after a system restart

-   Access when the [Remote User] is logged out

-   Unattended Access

To install:

1.  Open the DMG file.

2.  Drag and drop the AnyDesk app into the **Applications** folder.

If you installed AnyDesk in portable mode but need to upgrade to full installation later:

-   Open AnyDesk \> click **AnyDesk** in the top menu bar \> select **Install AnyDesk Service...**

------------------------------------------------------------------------

### Full installation via PKG 

This method is available for **custom AnyDesk clients** only and installs both the **AnyDesk client** and the **AnyDesk Service**, enabling full functionality.

There are two ways of installation:

-   Double-click the PKG file and follow the on-screen prompts.

-   Run the following command in Terminal:

    ``` 
    sudo installer -pkg AnyDesk.pkg -target /
    ```

> ::: blockquote-title
> 💡 **NOTE**
> :::
>
> Portable mode is not supported with this installation method.  

------------------------------------------------------------------------

### **Updating to new version troubleshooting** 

If you encounter an error when updating AnyDesk on macOS by replacing an existing version in the **Applications** folder by dragging a new version

![](https://7940397.fs1.hubspotusercontent-na1.net/hubfs/7940397/sequoia-png.png)

To resolve this issue:

1.  Open the **Applications** folder and locate the current AnyDesk application.

2.  Delete the current AnyDesk app.

3.  Reopen the DMG file and drag the new AnyDesk app into the **Applications** folder.

If the issue persists, use the **Full installation via DMG** method.

AnyDesk supports several Linux distributions and offers both portable and installed options.

### DEB and RPM packages 

These are the primary installation formats for **Debian-based** and **Red Hat-based** distributions. This method installs both the **AnyDesk client** and the **AnyDesk Service**, enabling full feature support.

To install:

1.  Download the appropriate **.deb** or **.rpm** package from the [AnyDesk website](https://anydesk.com/en/downloads/linux) or [DEB repository](http://deb.anydesk.com/howto.html) / [RPM repository](http://rpm.anydesk.com/howto.html)

2.  Install using your distribution's package manager (`apt` ,`dnf`, etc.).

This is recommended for systems requiring regular updates via repository and managed environments using package automation.

------------------------------------------------------------------------

### Compressed archive (.tar.gz) 

This method provides a **portable version** of the AnyDesk client without installing the AnyDesk Service.

-   No installation required

-   Can be used without administrative privileges

-   Does not support Unattended Access, reconnect after reboot, or login screen access

To use:

1.  Download and extract the `.tar.gz` file.

2.  Run the AnyDesk client directly from the extracted folder.

> ::: blockquote-title
> 💡 **NOTE**
> :::
>
> Installation of the service from `.tar.gz` is **not supported**.

------------------------------------------------------------------------

### Command-line installation 

All Linux versions of AnyDesk, **.deb**, **.rpm**, and `.tar.gz`, can be installed or run using the terminal, making them suitable for automated deployments and scripts.

> 🦉[ For syntax and parameters, see ][[**Command-Line Interface for Linux**]](/v1/docs/command-line-interface-for-linux)[. ]

------------------------------------------------------------------------

### Required dependencies 

Make sure the following packages are installed to run AnyDesk successfully:

-   libc6 (\>= 2.7)

-   libgcc1 (\>= 1:4.1.1)

-   libglib2.0-0 (\>= 2.16.0)

-   libgtk2.0-0 (\>= 2.20.1)

-   libstdc++6 (\>= 4.1.1)

-   libx11-6, libxcb1, libxcb-shm0

-   libpango1.0-0, libcairo2

-   libxrandr2 (\>= 1.3), libx11-xcb1

-   libxtst6, libxfixes3, libxdamage1

-   libgtkglext1

We provide a DEB installer specifically for Raspberry Pi devices running Raspberry Pi OS. Supports Raspberry Pi 2 and later.  

To install:

1.  Download the DEB installer for Raspberry Pi from the [AnyDesk website](https://anydesk.com/en/downloads/raspberry-pi).

2.  Use the terminal and package manager (e.g., `apt`) to install.

You can install AnyDesk on your Apple mobile or TV device through the **Apple App Store**.

To install:

1.  Open the **App Store** on your device.

2.  Search for **AnyDesk**.

3.  Tap **Get** to download and install the app.

It offers secure remote access and session features optimized for mobile use. Some features may differ from desktop versions due to platform limitations.

AnyDesk offers several ways to install on Android and ChromeOS devices.

### Google Play Store installation 

We recommend installing AnyDesk from the *Google Play Store* for automatic updates and maximum compatibility.

To install:

1.  Open the [**Google Play Store**](https://play.google.com/store/apps/details?id=com.anydesk.anydeskandroid).

2.  Search for **AnyDesk**.

3.  Tap **Install**.

You can also install AnyDesk from the [*Amazon App Store*](https://www.amazon.com/dp/B07WL74Y8Z)*,* [*Huawei App Gallery*](https://appgallery.huawei.com/#/app/C100140863)*,* [*Samsung Galaxy Store*](https://galaxystore.samsung.com/detail/com.anydesk.anydeskandroid). Follow the same steps as with the Play Store.

### Manual installation via APK 

For advanced users, the *AnyDesk APK file* is available for download and sideloading.

To install:

1.  Download the APK from [AnyDesk website](https://anydesk.com/en/downloads/chrome-os) or [my.anydesk](http://my.anydesk.com).

2.  Enable APK installation from unknown sources on your device.

3.  Open the file and follow the prompts to complete installation.

> ::: blockquote-title
> 💡 **NOTE**
> :::
>
> If you installed AnyDesk using the APK file, please note that it won't update automatically. We recommend checking our official website regularly to download the latest version.

A display driver that improves screen capture performance on older Windows systems, particularly relevant for systems that do not fully support modern rendering methods.

A tool that allows administrators and advanced users to automate installation, configuration, and client management tasks using command-line commands.

The ability to access and control a device from a different location using AnyDesk, facilitating remote support and work.

A feature that allows connections to a remote device without requiring manual approval on the other end, enabling access using just a password.

An individual whose device is being accessed or controlled by someone else using AnyDesk.