# Source: https://docs.carv.io/carv-ecosystem/carv-play/carv-intro/carv-id-telegram-sdk.md

# CARV ID Telegram SDK

## Overview

The **CARV ID Telegram SDK** provides a seamless solution for third-party games and Telegram-based applications to integrate CARV ID functionality.&#x20;

With this SDK, you can connect users to their CARV IDs, enable third-party account binding, and empower developers with access to powerful data insights and analytics powered by CARV ID.

It features both **light and dark modes** for optimal user experience and a **customizable plugin appearance** to match your brand and app design.

## How Does it Work?

The CARV ID Telegram SDK leverages the robust CARV ID suite to simplify authentication and account integration. The following illustration provides an overview of how the CARV ID ecosystem integrates with Telegram applications.

<figure><img src="https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2FFaBvJktzUrTmtbaJti4I%2Fimage.png?alt=media&#x26;token=9b40d6cf-fb5e-4d0a-84e8-d6b6f3b34a7d" alt=""><figcaption></figcaption></figure>

## Getting Started

The SDK implements the OAuth 2.0 standard, ensuring secure and reliable authentication. You would need to register your application first with CARV.

{% hint style="info" %}
How to register your application:

* **Determining Necessary Permissions**: Begin by reviewing the [application scopes available](#scopes) to identify the permissions your application will need.
* Provide Application Information: Share your application's **Redirect URL** and the **scopes** you've selected based on your needs. Additionally, provide the following information:
  * **Name Displayed on OAuth Screen**: The name of your application as it will appear during the authentication process.
  * **Home Page URL**: The main URL of your application, where users can learn more about your service.
  * **Logo Image URL**: A URL pointing to your logo image, which will be displayed during the authentication process.
  * **Privacy Policy URL**: The URL of your privacy policy page.
  * **Terms of Service URL**: The URL of your terms of service page.
* After we receive this information, we will set up your OAuth configuration and provide you with a Client ID and Client Secret. Keep these confidential.
  {% endhint %}

## Implementation&#x20;

Once you receive your client ID and secret, you integrate the SDK into your Telegram bot. Use the SDK's prebuilt methods to handle user authentication and launch of CARV ID account center.&#x20;

Please refer to our detailed documentation in the Github repository for step-by-step guide via [**https://github.com/carv-protocol/carv-id-sdk**](https://github.com/carv-protocol/carv-id-sdk). You can also access a **demo project and the source code there.**
