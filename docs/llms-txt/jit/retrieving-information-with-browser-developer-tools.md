# Source: https://docs.jit.io/docs/retrieving-information-with-browser-developer-tools.md

# Retrieving Authentication Information With Browser Developer Tools

## Overview

For security requirements (such as [Run a Web Application Scanner](https://docs.jit.io/docs/run-a-web-application-scanner) and [Ensure Your APIs are Secure (DAST)](https://docs.jit.io/docs/ensure-your-api-is-secure)) that utilize the ZAP [security tool](https://docs.jit.io/docs/security-tools), Jit requires you to retrieve HTTP message information for authentication purposes. Developer tools, available in browsers such as Google Chrome, can be an easy and convenient way to accomplish this.

## Retrieving form selectors with Chrome Developer Tools

**To retrieve a form selector with Chrome Developer Tools—**

1. From Google Chrome, navigate to the page that contains the form selector you wish to retrieve.
2. Open the *Elements* tab in Chrome Developer Tools using the keyboard shortcut Command + Shift + c in macOS or Ctrl + Shift + c in Windows.
3. Mouse over the webpage until you have located the field you wish to select. Click the field. The corresponding HTML element is highlighted in the Developer Tools panel.
4. Right-click the highlighted HTML element and select **Copy > Copy selector**. Paste this information into the Jit Platform as needed.

![](https://files.readme.io/2e46347-how_to_find_username_selector.png)

## Retrieving cookie values with Chrome Developer Tools

**To retrieve a cookie value with Chrome Developer Tools—**

1. From Google Chrome, navigate to your application.
2. Open Chrome Developer Tools using the keyboard shortcut Command + Shift + c in macOS or Ctrl + Shift + c in Windows.
3. Select the **Network** tab in the Developer Tools panel.
4. Refresh your page.
5. Click one of the request rows. This opens a new panel with additional details about the request.
6. From the **Headers** tab, scroll to the *Request Headers* section and right click the item titled **Cookie:**.
7. Select **Copy value**. Paste this information into the Jit Platform as needed.

![](https://files.readme.io/db20727-how_to_retrieve_cookie_header.png)

## Retrieving custom header information with Chrome Developer Tools

**To retrieve a custom header value with Chrome Developer Tools—**

1. From Google Chrome, navigate to your application.
2. Open Chrome Developer Tools using the keyboard shortcut Command + Shift + c in macOS or Ctrl + Shift + c in Windows.
3. Select the **Network** tab in the Developer Tools panel.
4. Refresh your page.
5. Click one of the request rows. This opens a new panel with additional details about the request.
6. From the **Headers** tab, scroll to locate your custom header and right click to select it.
7. Select **Copy value**. Paste this information into the Jit Platform as needed. Note that Jit will also likely require the key in addition to the value.