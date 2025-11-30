# Source: https://developer.1password.com/docs/agentic-autofill

On this page

# Use 1Password to securely provide credentials to AI agents

1Password Agentic Autofill gives you a secure way to provide credentials to AI agents, so they can sign in on your behalf without directly handling your secrets.

Instead of providing credentials to an AI agent using unencrypted methods like plaintext secrets or environment variables, you can tell an agent to sign in to a website using 1Password. When the agent needs to sign in, you\'ll be prompted to approve or deny the request.

After you approve, the 1Password browser extension in the agent\'s headless browser autofills your login details over an end-to-end encrypted channel and signs in to the website. In the future, you\'ll be able to see detailed audit logs that show when, where, and why the agent accessed the item.

During the Early Access, you can use Agentic Autofill with [Browserbase Director ](https://www.director.ai/), Browserbase\'s no-code AI agent that automates web-based tasks using natural language prompts.

## How the Browserbase integration works[â€‹](#how-the-browserbase-integration-works "Direct link to How the Browserbase integration works") 

When you set up the Browserbase integration, 1Password validates its pairing partner is director.ai and rejects any untrusted party, then establishes an end-to-end encrypted channel between your 1Password desktop app and Browserbase.

When the agent needs to sign in, it sends a request over the encrypted channel to autofill items that match the login website you specified, triggering an approval prompt from your 1Password desktop app for each autofill request. If you approve the request, the item is sent encrypted to the headless 1Password browser extension, which injects only the minimum required credential data from the approved item into the login form.

![Diagram of the 1Password secure agentic autofill flow](/img/ai/agentic-autofill-flow.png)![Diagram of the 1Password secure agentic autofill flow](/img/ai/agentic-autofill-flow.png)

1Password protects communication using forward-rotating key material and the Noise framework that protects your data all the way from your approving 1Password device to the remote browser\'s webpage, ensuring your data cannot be leaked accidentally. 1Password and Browserbase exchange new key material after every autofill to provide post-compromise security for all autofills performed prior.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

When Browserbase and 1Password are paired, Browserbase may be able to tell when an item matching an autofill request exists, even if the request is denied.

### What Browserbase can do[â€‹](#what-browserbase-can-do "Direct link to What Browserbase can do") 

When you turn on the integration, Browserbase can:

- Request to autofill items on your behalf

### What Browserbase can\'t do[â€‹](#what-browserbase-cant-do "Direct link to What Browserbase can't do") 

Browserbase cannot:

- Access items without your approval
- See a list of your items
- Modify your items

## Before you get started[â€‹](#before-you-get-started "Direct link to Before you get started") 

Before you get started with the integration, you\'ll need to:

1.  Sign up for [Browserbase Director ](https://www.director.ai/) and [1Password](https://1password.com/pricing/password-manager).
2.  Install the [1Password desktop app](https://1password.com/downloads).
3.  Install the [1Password browser extension](https://1password.com/downloads/browser-extension).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]tip

Make sure to turn on [Touch ID](https://support.1password.com/touch-id-mac/), [Windows Hello](https://support.1password.com/windows-hello/), or a Linux [system authentication option](https://support.1password.com/system-authentication-linux/) in the 1Password app for the best authentication experience.

### Administrators: Turn on the agentic autofill policy[â€‹](#administrators-turn-on-the-agentic-autofill-policy "Direct link to Administrators: Turn on the agentic autofill policy") 

If you\'re using a 1Password Business account, your administrator must turn on the agentic autofill policy for your team before you can use it. To do this, they\'ll need to:

1.  Sign in to their account on 1Password.com.
2.  Select **Policies**, then select **Manage** under \"Sharing and permissions\".
3.  Turn on the policy \"Allow AI Agents to autofill for users\".

## Step 1: Connect 1Password and Browserbase[â€‹](#step-1-connect-1password-and-browserbase "Direct link to Step 1: Connect 1Password and Browserbase") 

To set up the integration with Browserbase:

1.  Sign in to [Browserbase Director ](https://www.director.ai/).
2.  Select **![1Password browser extension](/img/1password-browser-inline-icon.svg)![1Password browser extension](/img/1password-browser-inline-icon.svg) Connect 1Password** beneath the input field. You\'ll be redirected to 1Password.com.
3.  Sign in to the 1Password account you want to use with Browserbase Director, then select **Continue**. If your 1Password desktop app is locked, you\'ll be prompted to unlock it.
4.  Select **Next** to return to Browserbase Director and complete the pairing flow.

After pairing, you should see a check next to the 1Password icon beneath the input field.

![The Browserbase Director prompt with 1Password toggled on](/img/ai/browserbase-agentic-autofill-on-light.png)![The Browserbase Director prompt with 1Password toggled on](/img/ai/browserbase-agentic-autofill-on-dark.png)

To turn off the integration, select the 1Password icon ![1Password browser extension](/img/1password-browser-inline-icon.svg)![1Password browser extension](/img/1password-browser-inline-icon.svg) beneath the input field, then toggle off **1Password Autofill**. You can also select **Disconnect** to unpair 1Password and Browserbase.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

You can currently pair Browserbase with 1Password on one device. If you set up the integration on a second device, 1Password de-authorizes the integration on the original device.

## Step 2: Create an item[â€‹](#step-2-create-an-item "Direct link to Step 2: Create an item") 

You can create an item with sample data for a website like [autofill.me ](https://autofill.me/) to test the integration.

1.  Open and unlock the [1Password desktop app](https://1password.com/downloads/).
2.  Select **+ New Item** to create a new item.
3.  Select **Login** for the item category.
4.  Select the username field and enter an example username like `hello`.
5.  Select the password field, then select **Create a new password** to generate a random password.
6.  Select the website field and enter `https://autofill.me`. If you want to test a different Login item, make sure the website is set to the URL where you sign in to the account.
7.  Select **Save** to create the item.

![An example autofill.me Login](/img/ai/agentic-autofill-item-light.png)![An example autofill.me Login](/img/ai/agentic-autofill-item-dark.png)

## Step 3: Prompt the agent to sign in to a website using 1Password[â€‹](#step-3-prompt-the-agent-to-sign-in-to-a-website-using-1password "Direct link to Step 3: Prompt the agent to sign in to a website using 1Password") 

In the [Browserbase Director ](https://www.director.ai/) input field, instruct the agent to sign in to a website using 1Password and hit enter.

For example, to have the agent sign in to `autofill.me` with the test Login item you created in the previous step, enter the prompt:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

You\'ll get a prompt from 1Password asking you to authorize or cancel the request from Browserbase. If you have multiple items for the same website, you can select the down arrow next to the suggested login to choose a different item.

Authorize the prompt in the same way you unlock your 1Password account, like with Touch ID, and 1Password will fill your login in the remote browser session.\

[If you make a second request to sign in using 1Password in the same workflow, you may need to select the **Log in with 1Password** button in Browserbase Director.]

![The prompt to authorize 1Password to fill credentials through Browserbase](/img/ai/agentic-autofill-request-dark.png)![The prompt to authorize 1Password to fill credentials through Browserbase](/img/ai/agentic-autofill-request.png)

## Troubleshooting[â€‹](#troubleshooting "Direct link to Troubleshooting") 

### If Browserbase and 1Password don\'t pair successfully[â€‹](#if-browserbase-and-1password-dont-pair-successfully "Direct link to If Browserbase and 1Password don't pair successfully") 

If you have trouble pairing 1Password and Browserbase, try the following steps:

#### Make sure the 1Password browser extension and your 1Password desktop app are connected[â€‹](#make-sure-the-1password-browser-extension-and-your-1password-desktop-app-are-connected "Direct link to Make sure the 1Password browser extension and your 1Password desktop app are connected") 

For the pairing process to work successfully, your 1Password browser extension and desktop app must be connected. To check if they\'re connected:

1.  Select ![1Password browser extension](/img/1password-browser-inline-icon.svg)![1Password browser extension](/img/1password-browser-inline-icon.svg) in your browser\'s toolbar, then select your account or collection in the top left \> **Settings**.
2.  Select **General** and make sure the \"Integrate this extension with the 1Password desktop app\" setting is toggled on and the integration status is connected.

If your 1Password browser extension and app aren\'t connected, [turn on the appropriate settings](https://support.1password.com/connect-1password-browser-app#check-your-settings).

#### Make sure your app is open and unlocked[â€‹](#make-sure-your-app-is-open-and-unlocked "Direct link to Make sure your app is open and unlocked") 

Before beginning the pairing process, open the 1Password desktop app and unlock it. Then, follow the steps to [connect 1Password and Browserbase](#step-1-connect-1password-and-browserbase).

### If you see a warning that the request is taking longer than expected[â€‹](#if-you-see-a-warning-that-the-request-is-taking-longer-than-expected "Direct link to If you see a warning that the request is taking longer than expected") 

If you see a warning from Browserbase that the request is taking longer than expected, your 1Password app may be locked. Open the 1Password desktop app and unlock it, then try the request again.

If you\'re still having trouble or want to share feedback, [contact 1Password support](mailto:support@1password.com).

## Learn more[â€‹](#learn-more "Direct link to Learn more") 

- [Closing the credential risk gap for AI agents using a browser](https://blog.1password.com/closing-the-credential-risk-gap-for-browser-use-ai-agents/)
- [The security principles guiding 1Passwordâ€™s approach to AI](https://blog.1password.com/security-principles-guiding-1passwords-approach-to-ai/)