# Source: https://docs.pentaho.com/install/9.3-install/pentaho-upgrade-cp/download-the-pentaho-upgrade-file-pentaho-upgrade.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/download-the-pentaho-upgrade-file-pentaho-upgrade.md

# Download the Pentaho upgrade file

The upgrade process includes using the update file for your platform and the installer hash files, which you must download from the [Support Portal](https://support.pentaho.com/home) before running the upgrade installer.

Perform the following steps to download the update file and installer hash files.

1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho support username and password provided in your Pentaho Welcome Packet.
2. In the Pentaho card, click **Download**.

   The Downloads page opens.
3. Click **See all \<number> articles** to see the full list of **10.x** downloads.

   The **10.x** page opens.
4. Click **Pentaho 10.2 GA Release**.

   The **Pentaho 10.2 GA Release** page opens.
5. At the bottom of the page, in the file component section, navigate to the `Utilities and Tools/Pentaho Server Upgrade Installer` folder.
6. Depending on your platform, download one of the following files:

   * **Linux**

     `pentaho-update-10.2<.x.y-build number>.bin`
   * **Windows**

     `pentaho-update-10.2<.x.y-build number>.exe`

   Where `x`, `y`, and `build number` indicate the version to which you are upgrading.
7. From the **Pentaho 10.2 GA Release** page, navigate back to the **10.x** page.
8. Click the **Installer Hash Files** link.

   **Note:** The installer hash files are required for installing 9.3.0.3, 9.4.0.1, and later.

   The Installer Hash Files Support page opens.
9. In the file component section, download the `installer-hash-files-<release number>-<build number>.zip` file, but do not extract it. Later, during the upgrade process, you are prompted for the location of this file.

   **Note:** The release number for the `installer-hash-files-<release number>-<build number>.zip` file does not relate to the release number for the version of Pentaho that you are upgrading. Always use the latest version of the `installer-hash-files-<release number>-<build number>.zip` file that is posted on the [Support Portal](https://support.pentaho.com/home) to upgrade Pentaho.
10. (Optional) If needed, move the downloaded files to a temporary location on your workstation.

You are now prepared to begin your upgrade to Pentaho 10.2.
