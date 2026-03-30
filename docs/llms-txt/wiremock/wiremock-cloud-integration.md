# Source: https://docs.wiremock.io/ide-integrations/jetbrains/wiremock-cloud-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Integration with WireMock Cloud

> Log in to your WireMock Cloud account in the IDE and create mock APIs from your local files

This IDE plugin provides support for various WireMock OSS features as well as integration with WireMock Cloud.

## Install the WireMock plugin

The plugin is available on the [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/23695-wiremock).

1. Press <kbd>⌘Сmd</kbd><kbd>,</kbd> on Mac or <kbd>Ctrl</kbd><kbd>Alt</kbd><kbd>S</kbd> on other platforms to open settings and then select **Plugins**.
2. Open the **Marketplace** tab, find the *WireMock* plugin, and click **Install** (restart the IDE if prompted).

## Setup

The WireMock plugin comes with features that utilize users' existing WireMock Cloud accounts and integrates local
files with them, e.g. creating remote mock APIs from local stub mappings.

So, if you have a WireMock Cloud account and want to connect to it and use Cloud specific features, head to the plugin settings
at **Settings | Tools | WireMock** and log in to your account.

Otherwise, no specific setup is required.

## Log in to WireMock Cloud

When WireMock is first installed, it is necessary to log in to your WireMock Cloud account, in order to be able to use related features.

Logging in can happen at two different locations: via an editor notification after opening stub mappings files, or from the plugin's settings UI.

<Note>
  Credentials are stored safely by the IDE (on the IDE level), so

  <ul>
    <li>they are completely separate from any WireMock CLI installation on the system,</li>
    <li>and if you are using the plugin in multiple IDEs, you have to log in in each of them.</li>
  </ul>
</Note>

### From the editor notification

Upon opening a stub mapping JSON file, the following notification appears at the top of the editor.
It provides a way to create an account if you haven't already, or to use your existing account.

<img src="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-login-editor-notification.png?fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=284e5e1576fb96f971c48b21798814fa" alt="WireMock Cloud editor notification when not logged in" data-og-width="991" width="991" data-og-height="203" height="203" data-path="images/ides/jetbrains/wiremock-cloud-login-editor-notification.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-login-editor-notification.png?w=280&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=90f896cf4a981884613824658ea7b15a 280w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-login-editor-notification.png?w=560&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=09c02af4e96dd8ac71aa8835d8241cb6 560w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-login-editor-notification.png?w=840&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=2c6ade5ca3914cc100e94128eb21acfb 840w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-login-editor-notification.png?w=1100&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=19a25025c8c8c5cc3c4d2e4881a1b6d8 1100w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-login-editor-notification.png?w=1650&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=46ffdf0a3bd34d72889286c4bcfa18eb 1650w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-login-editor-notification.png?w=2500&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=aef71991599c337be0294dae2c1557cd 2500w" />

To start the login process, click on the **Log in** link. This performs two things:

* shows a balloon popup with your verification code
* opens the login page in your web browser showing you a verification code

In case the page would not open, you can copy the verification URL from the popup.

<img src="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-authentication-balloon.png?fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=8301dd6f565308f169198a380301cd3a" alt="WireMock Cloud authentication confirmation balloon" data-og-width="411" width="411" data-og-height="167" height="167" data-path="images/ides/jetbrains/wiremock-cloud-authentication-balloon.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-authentication-balloon.png?w=280&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=e831f4d261c1c1c464c39b2451f85a03 280w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-authentication-balloon.png?w=560&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=4ec7e8123be035d5b31c50cbcfbca7e5 560w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-authentication-balloon.png?w=840&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=a4652b995cb6ee532e7748f0a5fa9b80 840w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-authentication-balloon.png?w=1100&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=ca05a9b1067c1f1670d06ffcda5e3240 1100w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-authentication-balloon.png?w=1650&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=5c11476ce3f2865556c13172e500fddd 1650w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-authentication-balloon.png?w=2500&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=4de340d40d0ee12305660912dfa50a60 2500w" />

Make sure that the two codes match, then confirm the device code. In a few seconds the IDE will show you another balloon
confirming your login.

### From the plugin settings

You can also log in to your account via the plugin settings at **Settings | Tools | WireMock**.
The flow is similar to the one described in the previous section, but it is handled entirely on the settings UI,
and you also have the option to **Cancel Login**.

<img src="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-settings-logged-out.png?fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=231321a6d36a7685f9c20af1a97ea1f7" alt="WireMock Cloud settings not logged in" data-og-width="614" width="614" data-og-height="148" height="148" data-path="images/ides/jetbrains/wiremock-cloud-settings-logged-out.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-settings-logged-out.png?w=280&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=29fd15335408c5dfc2a126100ce976e9 280w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-settings-logged-out.png?w=560&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=6d11af6ca2c7fe145c51342be4dd64cf 560w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-settings-logged-out.png?w=840&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=756a55dc909ee19f8c2c92252c7d7a9b 840w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-settings-logged-out.png?w=1100&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=53030f0ebc48f15b2661d344957b1471 1100w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-settings-logged-out.png?w=1650&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=6d6b793dd759083262729addd8b654cf 1650w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-settings-logged-out.png?w=2500&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=358524187b3cf6a001bb7c1a2d992a21 2500w" />

When the login is successful, the UI will show you the email address you are logged in with,
or will notify you if a problem occurred during the login.

#### Use with On-Premise Edition

The plugin also supports work with the on-premise edition of WireMock Cloud. To turn on this feature, enable
the **Use with On-Premise Edition** option, update the necessary configuration values, and log in.

If you are already logged into a different installment of WireMock Cloud, make sure to log out, save the settings,
and log in again.

<img src="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-settings-on-premise.png?fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=51a8e18eee89c8205ab77fe6e6c24a1a" alt="WireMock Cloud settings on-premise" data-og-width="677" width="677" data-og-height="362" height="362" data-path="images/ides/jetbrains/wiremock-cloud-settings-on-premise.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-settings-on-premise.png?w=280&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=f42598b0d10a68e4748f34a7da74a543 280w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-settings-on-premise.png?w=560&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=ab4d7bf26450e524d6847f22a0289183 560w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-settings-on-premise.png?w=840&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=3ea38b924e8117a5ea47891b3d0e1173 840w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-settings-on-premise.png?w=1100&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=7642416dca1992a2fff8563ea7a054f5 1100w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-settings-on-premise.png?w=1650&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=a6301d0ef6def43e2843f522c58843dd 1650w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-settings-on-premise.png?w=2500&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=3fc90c7dca730961afffe558ff4b41aa 2500w" />

## Create mock APIs and import stubs

If you want to convert local stub mappings to remotely hosted WireMock Cloud mock APIs, you can do so: open a stub mapping file,
then click on the **Create mock API** link in the top notification,
or the <img src="https://resources.jetbrains.com/help/img/idea/2025.3/app-client.expui.general.export.svg" style={{display: 'inline-block', margin: 'inherit'}} /> icon
in the floating toolbar.

<img src="https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-create-mock-api.png?fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=48034433623a5dc4dfeb786cc97e9f6a" alt="WireMock Cloud create mock API options" data-og-width="985" width="985" data-og-height="219" height="219" data-path="images/ides/jetbrains/wiremock-cloud-create-mock-api.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-create-mock-api.png?w=280&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=9e3bf1378c11531a6c7666cd6f554f03 280w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-create-mock-api.png?w=560&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=d445b99f73f6943ffb8e67e74873834c 560w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-create-mock-api.png?w=840&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=308a34e9466b3b2540cdb996e3d2d438 840w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-create-mock-api.png?w=1100&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=653a987ae83741cda44a8335a34a6333 1100w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-create-mock-api.png?w=1650&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=e03e0f48fb1afb844f16dfdff2841139 1650w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-create-mock-api.png?w=2500&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=994cc8dd287478f85b75e1e84f56e196 2500w" />

<Note>
  These actions are shown only when you are logged in to a WireMock Cloud account.
</Note>

This will display a dialog (detailed in the sections below) to specify the properties of the new mock API.

Submitting the dialog creates an empty, remote mock API with the specified name and custom hostname, and immediately imports/uploads the
stubs from the open mapping file into that new API.

### Mock API properties and types

When you initiate the mock API creation, you are presented with a dialog to specify the API name, an optional custom hostname
and the type of the API to create.

<img src="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog.png?fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=29fb54d18eec6e58ff07fef9e8e99e8a" alt="WireMock Cloud create mock API dialog" data-og-width="486" width="486" data-og-height="219" height="219" data-path="images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog.png?w=280&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=eef29129be35655ffb731be9a9ae8046 280w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog.png?w=560&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=f4629aaad66f64a7b11a2ef3debebce3 560w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog.png?w=840&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=ea36d629efc690156c4b947bd9014f12 840w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog.png?w=1100&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=6dbdc4dc2c006bb47591fa249c06a36b 1100w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog.png?w=1650&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=9904c467c61490ea878093071c7e8cc5 1650w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog.png?w=2500&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=88ba3b46b99fecc41542de5092532b45 2500w" />

The following API types are supported:

* Unstructured (WireMock)
* REST
* [GraphQL](/graphql/overview) (+ non-federated schema)
* [gRPC](/grpc/overview) (+ descriptor file)

If you choose GraphQL or gRPC you must also upload a schema/descriptor file with them. Creating a mock API without them is not permitted.

<img src="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog-graphql.png?fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=5ab27c2febbfa056ab75fe5dace34e5c" alt="WireMock Cloud create mock API with GraphQL" data-og-width="486" width="486" data-og-height="325" height="325" data-path="images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog-graphql.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog-graphql.png?w=280&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=81eaaf246a01d078030e78f1ba1f80a6 280w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog-graphql.png?w=560&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=fef7aa52c5616738e213a51f7359e9c2 560w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog-graphql.png?w=840&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=f0026f1a8d2484818db41045795d3659 840w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog-graphql.png?w=1100&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=ba6083690b550715e5c9bc37f60c6fde 1100w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog-graphql.png?w=1650&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=3f6cc1344e66565854af18ff31e554a7 1650w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-dialog-graphql.png?w=2500&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=b253a565e5190a3d03a5b69fbbe7f2be 2500w" />

### Completion of the API creation

The creation of the mock API and data upload into it is performed in two or three separate phases depending on the API type:

* API creation and stub upload for Unstructured and REST,
* API creation, stub upload and schema/descriptor upload for GraphQL and gRPC

Thus, when all phases finish without any issue, a separate balloon notification appears for each phase.
The first one also provides a link with which you can easily open the new API in your browser.

<img src="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-successful.png?fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=64fe9b6c46f9b81579fa0ebce3c160f4" alt="WireMock Cloud create mock API with GraphQL" data-og-width="409" width="409" data-og-height="200" height="200" data-path="images/ides/jetbrains/wiremock-cloud-create-mock-api-successful.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-successful.png?w=280&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=1b195dd4957ba10b9016480c1da7e845 280w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-successful.png?w=560&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=af9ec6c3e4e61720e7548a2c6129e8f5 560w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-successful.png?w=840&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=e37281125b1a99b6faa023c2aea9c8ab 840w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-successful.png?w=1100&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=34e4c69cdb51d6a0598d8bb94bd44b4a 1100w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-successful.png?w=1650&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=d2722645aa518776cabf8433c4222a91 1650w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-cloud-create-mock-api-successful.png?w=2500&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=3b3c16783bcf726124dbdd643f027d5c 2500w" />

If any phase fails for any reason, notifications with appropriate messages will let you know of the failure and the reason of it.

## Import stubs into existing mock APIs

Besides uploading stubs into newly created APIs, you can also upload them into APIs that already exist in your WireMock Cloud account.
You can do so by opening a stub mapping file, then clicking on the
<img src="https://resources.jetbrains.com/help/img/idea/2025.3/app-client.expui.general.upload.svg" style={{display: 'inline-block', margin: 'inherit'}} /> icon in the floating toolbar.

<img src="https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-import-stubs-into-existing-api.png?fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=594001de82ac2574e7b1f61f51f0e084" alt="WireMock Cloud import stubs into existing mock API options" data-og-width="999" width="999" data-og-height="220" height="220" data-path="images/ides/jetbrains/wiremock-cloud-import-stubs-into-existing-api.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-import-stubs-into-existing-api.png?w=280&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=0ba64767b3d4ce34e2db2cab4c35abab 280w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-import-stubs-into-existing-api.png?w=560&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=63f3f62b4f6321772ea906e0aa569839 560w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-import-stubs-into-existing-api.png?w=840&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=898fd2df085a43a8812e851b01107e1b 840w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-import-stubs-into-existing-api.png?w=1100&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=efd565a33c15ed52c116470e0e20542b 1100w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-import-stubs-into-existing-api.png?w=1650&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=911e01e964cbac8b1ed6f9ddf65feb5a 1650w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-import-stubs-into-existing-api.png?w=2500&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=c3ac450403c5cb7eec8ec90b2f43218c 2500w" />

<Note>
  This action is shown only when you are logged in to a WireMock Cloud account.

  This feature adds the uploaded stubs to the target mock API without deleting existing stubs.
</Note>

In the appearing dialog you can find and select the target API to upload stubs into.

<img src="https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog.png?fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=7b520f213e84c76fe44d7d9119998ff1" alt="WireMock Cloud select mock API dialog" data-og-width="836" width="836" data-og-height="544" height="544" data-path="images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog.png?w=280&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=1cfc8ea0584d2b9e2c7754270c7f89dd 280w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog.png?w=560&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=4ee1fe1a7525f9a1b7455cb69c18a8d9 560w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog.png?w=840&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=befe065ccb5ec30237008a43f3cce6f4 840w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog.png?w=1100&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=a7b0f7c6d95541299a8574a8dc52b6c8 1100w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog.png?w=1650&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=32a0bf978b3051e9ac7284afbdc6c5a3 1650w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog.png?w=2500&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=b127875eb1248083c9c3dad1827543eb 2500w" />

### Search

When opening the dialog, it displays all available mock APIs. After that you can perform searches with arbitrary query strings (it is case-insensitive)
either by clicking the <img src="https://resources.jetbrains.com/help/img/idea/2025.3/app-client.expui.general.search.svg" style={{display: 'inline-block', margin: 'inherit'}} /> button or by hitting <kbd>Enter</kbd>.

It looks for matches in APIs' names, base URLs and descriptions too. (Showing descriptions is not yet supported.)

If you'd like to reset the results and see all available mock APIs, perform a search with an empty string.

### Mock APIs list

The matching mock APIs are listed in this table with their names, base URLs and types shown.

Each result page shows up to 20 items (that value is not customizable), and the table allows selecting at most 1
mock API as the target. If no API is selected, the dialog cannot be OKed.

On top of initiating the stub import using the **OK** button, double-clicking on a mock API also does the same.

To locate an API easier on the current page, you can use speed search: click somewhere in the table, then start typing.
When there is a match, the first matching row will be selected.

<img src="https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-speed-search.png?fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=91651c77fecd60d37721557b05bdf694" alt="WireMock Cloud select mock API speed search" data-og-width="837" width="837" data-og-height="300" height="300" data-path="images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-speed-search.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-speed-search.png?w=280&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=77579ebc781c1b60501e2b708f4abf08 280w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-speed-search.png?w=560&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=7330439c0e18a68fce3f19d7a5fc9cdf 560w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-speed-search.png?w=840&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=30743243369a0289423e3529bbfd4332 840w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-speed-search.png?w=1100&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=501606e69c9ebc7e5cf93822238a760d 1100w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-speed-search.png?w=1650&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=ad2d0a941d41a9ef14ee82c780e744ae 1650w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-speed-search.png?w=2500&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=92896cf2c6a138f1b5c87e850c27481d 2500w" />

### Pagination

This component lets you navigate through the current result set. It supports moving to the **First**, **Previous**, **Next** and **Last** pages when applicable,
as well as to arbitrary pages.

To initiate the navigation to a specific page, specify a valid page number and hit <kbd>Enter</kbd>. If it is initiated with a number

* less than 1, or a non-integer, it will load the first page
* greater than the total number of pages, it will load the last page

In addition, when an invalid page number is entered, the field displays an appropriate message, for example:

<img src="https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-pagination-error.png?fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=c8109fe4f94eb4ce13ad591455b16ddf" alt="WireMock Cloud select mock API pagination error" data-og-width="841" width="841" data-og-height="183" height="183" data-path="images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-pagination-error.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-pagination-error.png?w=280&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=db25c549a8f2b613e4c8901148a995fb 280w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-pagination-error.png?w=560&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=884a90db04e7ba268d7e36894c92352e 560w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-pagination-error.png?w=840&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=c6146112fe5cf6a097741d0570a0479d 840w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-pagination-error.png?w=1100&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=82da114160bfb6db596fc624a93a51f7 1100w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-pagination-error.png?w=1650&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=ae14c366f475b170081317ba1ff0a217 1650w, https://mintcdn.com/wiremockinc/3dfMUJo65AXlEMtQ/images/ides/jetbrains/wiremock-cloud-select-mock-api-dialog-pagination-error.png?w=2500&fit=max&auto=format&n=3dfMUJo65AXlEMtQ&q=85&s=b29c1707e024aaa405cfe1109c9dfaeb 2500w" />

### Initiating the stub import

When the dialog is OKed, the stub import begins, and the same logic, including handling failure scenarios,
is performed as when uploading stubs via the [Create mock APIs and import stubs](#create-mock-apis-and-import-stubs) feature.
