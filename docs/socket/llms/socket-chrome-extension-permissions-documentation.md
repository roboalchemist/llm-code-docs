# Source: https://docs.socket.dev/docs/socket-chrome-extension-permissions-documentation.md

# Extension Permissions

The [Socket Security browser extension](https://chromewebstore.google.com/detail/jbcobpbfgkhmjfpjjepkcocalmpkiaop) offers advanced protection by integrating security metrics directly into your browsing experience on NPM, PyPI, Go, and Maven package pages and search results. This extension helps you identify and mitigate risks from open-source packages before they impact your projects. To function effectively, the extension requires specific permissions, which you can configure through your Chrome browser settings.

#### Key Features of the Socket Chrome Extension

* **Instant Security Metrics**: Provides security insights directly on NPM, PyPI, Go, and Maven package pages and search results.
* **Real-Time Risk Detection**: Identifies potential threats such as malware, typo-squatting, and vulnerable dependencies.
* **Customizable Site Access**: You can control the sites where the extension is active.
* **Total Threats Display:** Instantly view the total number of threats detected.
* **Low, Medium, High, and Critical Threat Alerts:** Differentiate between varying severity levels to prioritize your security efforts.

<Image align="center" width="64% " src="https://files.readme.io/b1a6b3b-Screenshot_2024-08-14_at_12.17.53_PM.png" />

For more detailed insights, visit the [Socket Blog on the Web Extension](https://socket.dev/blog/new-socket-web-extension-take-socket-with-you).

#### Privacy Considerations

The Socket Chrome Extension is designed with your privacy in mind. The extension only communicates package names if any are found on the page you are visiting. If no package is detected, there is absolutely no request to Socket's servers being made. This ensures that your browsing activities remain private and secure.

#### Configuring Site Access for the Socket Chrome Extension

The Socket Chrome Extension requires several permissions to function optimally. Below is a breakdown of these permissions:

<Image align="center" width="75% " src="https://files.readme.io/cad61c5-Screenshot_2024-08-14_at_10.26.10_AM.png" />

1. **Extension Overview:**
   * The Socket Security extension is designed to help you secure your supply chain.
   * **Version:** 1.0.0
   * **Size:** \< 1 MB
   * **Permissions:** The extension requires permission to read and modify data on websites you visit.

2. **Configuring Site Access:**
   * **Site Access Options:**
     * **On all sites:** Grants the extension access to all websites you visit.
     * **On specific sites:** Limits the extension's activity to specified sites.
     * **On click:** Activates the extension only when you click on it.

3. **Adding a Specific Site:**
   * Choose "On specific sites" to limit the extension’s access.
   * Click on "Add a site."
   * Enter the site’s URL where you want the extension to be active (e.g., [https://www.npmjs.com/](https://www.npmjs.com/)).
   * Confirm by clicking the "Add" button.

4. **Additional Settings:**
   * **Allow in Incognito:** Enable the extension in incognito mode, although it may not record browsing history.
   * **Allow access to file URLs:** This allows the extension to access files on your computer if necessary.

5. **Managing Permissions:**
   * Access and modify the extension settings via Chrome’s extension management settings or the Chrome Web Store.
   * You can adjust or revoke permissions anytime.

#### Minimal Recommended Site Access

If you choose to run the extension on specific sites, we recommend adding the following:

* [https://github.com](https://github.com)
* [https://www.npmjs.com](https://www.npmjs.com)
* [https://pypi.org](https://pypi.org)
* [https://pkg.go.dev](https://pkg.go.dev)
* [https://central.sonatype.com](https://central.sonatype.com)