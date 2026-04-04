# Source: https://docs.replit.com/replit-workspace/workspace-features/secrets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Secrets

> The Secrets workspace tool lets you securely store sensitive information your app needs as encrypted environment variables.

The Secrets tool stores and encrypts **secrets**, your Replit App's sensitive information, such as API keys, authentication tokens, and database connection strings.

When you add a secret, the tool automatically encrypts the data and makes it available to your Replit App as an environment variable.
This approach lets you eliminate hard-coding secrets in your code and reduce the risk of exposing them.

<Frame>
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/qE_2Z8ReyWI" title="Secrets workspace tool" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
</Frame>

Hard-coding secrets in your codebase can lead to accidental exposure in the following scenarios:

* Sharing your code with others through a public Replit App or copy-paste
* Checking your code into version control in a public repository
* Live streaming or screen sharing your code

Use the Secrets tool to confidently share your code without worrying about exposing credentials.

<Frame caption="Secrets workspace tool">
  <img src="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/secrets-tool.png?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=5e5454a3daaa5fc3f30d823e6c8c3c79" alt="screenshot of the Secrets tool" data-og-width="2276" width="2276" data-og-height="1136" height="1136" data-path="images/workspace/secrets-tool.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/secrets-tool.png?w=280&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=64a606c42011cafadbef5a4026db1e01 280w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/secrets-tool.png?w=560&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=03a88ef8a9b7f9dbd8e52c8657eaaca1 560w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/secrets-tool.png?w=840&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=02cfca6f888c1d7580f603cbdfd2c027 840w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/secrets-tool.png?w=1100&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=f7abf52003fc66afe8da7dc017c7013f 1100w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/secrets-tool.png?w=1650&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=dee3ca372bb8c1f04a76222011c835e4 1650w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/secrets-tool.png?w=2500&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=0a9e484145afbbbfed7a85e74eaffae4 2500w" />
</Frame>

## Features

Secrets include the following features:

* **End-to-end encryption**: Automatically protect your data using AES-256 encryption at rest and TLS encryption in transit
* **App-level secrets**: Store and manage secrets that are specific to a Replit App
* **Account-level secrets**: Store and manage secrets that you can make available across all your Replit Apps
* **Environment variable access**: Access your secrets from your code using environment variables
* **Collaborative access**: Share secrets with collaborators and team members

## Usage

<Note>
  Secrets are available for all deployment types except Static Deployments.
</Note>

You can access Secrets in the Secrets workspace tool.

<Accordion title="How to access Secrets">
  From the left **Tool dock**:

  1. Select <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5b2c72713cc17ac272098bcbfd624d84" alt="All tools icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/workspace-all-tools-button.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=284639f38f8e91da05d14611e44a9ae6 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d0e802a9c50a81e5c825cf1ddce00a64 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=b5c4e38a7cf923221d2412e904bbdc94 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3b43a87adf314fbb300376b404ab8a22 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a11f8a405c4156ff625219a372c2ceca 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=7c86d2f1bfa4611aeca168daf29d08ff 2500w" /> **All tools** to see a list of workspace tools.
  2. Select <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/lock.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=bf707361895221f07972dea2af22ce12" alt="Secrets icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/lock.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/lock.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=da39ba7154af6d1a1fd13336371baa5e 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/lock.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=da5d50fce5aba0c48839faa1e08744c8 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/lock.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=ddc77db2c6740eba86f113046be9fffc 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/lock.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e3c612b54aa26b81626b0ce3beeda0fc 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/lock.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=afc39667bdd3507f016afec0bdc228dc 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/lock.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=8aad3e1cd4b3a321d3760db645128afd 2500w" /> **Secrets**.

  From the **Search bar**:

  1. Select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4a0eb8f6b17ff6761d53167334a68b30" alt="magnifying glass icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/workspace-search-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=baa20919b2c8e7db2fad2562c732edd0 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5fcfa3935da89ed6c1c6f893998c4f4a 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=2a24f3fcc4dd990d9062598eab165cff 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a3258e068d5ead6bacadcbe6e5785575 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d08ebecb3063ed18a657beb563ac9c3c 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e63dd2009929a4b375b86e44ed6d7732 2500w" /> magnifying glass at the top to open the search tool
  2. Type "Secrets" to locate the tool and select it from the results.
</Accordion>

### Manage App Secrets

You can manage your app-level secrets in the **App Secrets** tab in the **Secrets** pane.
This tab displays a list of all secrets associated with your Replit App.

<Accordion title="Add App Secrets">
  To add a secret:

  1. Select **New Secret**.
  2. Enter a **Key**, the name of the secret, and a **Value**, the secret itself.
  3. Select **Add Secret** to save the entry.
</Accordion>

<Accordion title="Edit App Secrets">
  To edit a secret:

  1. Select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d6ac2757eaf25e61d31ce51316ec91ad" alt="three vertical dots icon" height="16" width="16" data-og-width="24" data-og-height="24" data-path="images/icons/vertical-dots.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=cf215ef22f55bf163c0037f923584e37 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=9659b713156cc159f2b9107450cc0fbd 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=73cb1af8587233823aba8f0aec72d1d9 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5d633ba6d10d1d6d6d179b3086869257 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5255815ba3d626d74ede11e23698ccbd 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=15dffd4252b85614141c73a628671cf1 2500w" /> vertical dots menu next to the secret.
  2. Select **Edit** from the contextual menu.
  3. Update the text in the **Key** or **Value** field and select **Update Secret** to save changes or **Cancel** to discard changes.

  You can also modify the entire list of App Secrets by selecting **Edit as JSON** or **Edit as .env** at the bottom of the tab.
</Accordion>

<Accordion title="View App Secrets">
  To view a secret, select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=7079fc956e29af9b424e7ebb698a45a7" alt="eye icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/eye.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=317ec5fd6c6b79d803aac063a78f9568 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a903c9a1c99b7cf63c6d73a8747655d9 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=97a66096841ce0b1f887d212ae94bd73 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e0747ce2aa09c30b172c5c996d2d8987 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=c1d86c81d578db02f4fea8cf02e450d0 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=10907b48c07ec82131726ce73527e96b 2500w" /> eye icon next to the secret.

  To hide the secret, select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye-slash.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=ae8689a686f591b697e1a9a9fd23d7ad" alt="eye with a slash icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/eye-slash.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye-slash.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d2d04539bdea500781b4eeff8cd6cc84 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye-slash.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=f0efb4c7ebe7510a2f227529957c69e3 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye-slash.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4a05ebd6d98894f0c0950124eee4fca1 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye-slash.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4ac412db5867aefe8e8bbc21d07dce60 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye-slash.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=9210692825e23123e892b0f67aaf5599 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye-slash.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e321ddb1fd92451a44d0e30f289848f4 2500w" /> eye with slash icon.
</Accordion>

<Accordion title="Delete App Secrets">
  To delete a secret, select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d6ac2757eaf25e61d31ce51316ec91ad" alt="three vertical dots icon" height="16" width="16" data-og-width="24" data-og-height="24" data-path="images/icons/vertical-dots.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=cf215ef22f55bf163c0037f923584e37 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=9659b713156cc159f2b9107450cc0fbd 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=73cb1af8587233823aba8f0aec72d1d9 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5d633ba6d10d1d6d6d179b3086869257 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5255815ba3d626d74ede11e23698ccbd 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=15dffd4252b85614141c73a628671cf1 2500w" /> vertical dots menu next to the secret and select **Delete**.
</Accordion>

### Manage Account Secrets

You can manage your account-level secrets in the **Account Secrets** tab in the **Secrets** pane.
This tab displays a list of only secrets associated with your Replit account.

<Accordion title="Add Account Secrets">
  To add an account-level secret:

  1. Navigate to the **Account Secrets** tab.
  2. Select <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=39c5a0a4872b7416378ddad9f2bef608" alt="gear icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/settings-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e0a36e6a9a2078c02467d2abf0b8ba9e 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3be97f139b63f478d536ccaa51518c9a 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4eba230fefbe9836ffd37672275aa7d1 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=97e5099639faf4a5490d8e000c00149a 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4d9552209cee3306d2bc2a02e747ecb6 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d84a81284c0c9af295e0b86273d5c291 2500w" /> **Manage Account**.
  3. Select **New Secret** to add a secret.
  4. Enter a **Key**, the name of the secret, and a **Value**, the secret itself.
  5. Select **Save** to save the entry.
</Accordion>

<Accordion title="Edit Account Secrets">
  To edit a secret:

  1. Select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/pencil-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=9fe8b0d62049a6cc25ff54186cd82167" alt="pencil icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/pencil-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/pencil-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=70f222a550c10565fda88d2a405f0919 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/pencil-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=2e0254eba779d03f1854e9dceaca64f3 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/pencil-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=63823efefad606fd66371d96f5d4069a 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/pencil-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=0529386335540e80fc49377dbccc8cdd 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/pencil-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=0479fb149fec299ab1c26d5c723a534f 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/pencil-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a9a6290741fad3dcd5d918c07bd79adc 2500w" /> pencil icon next to the secret.
  2. Update the text in the **Key** or **Value** field and select **Save** to save changes or **Cancel** to discard changes.
</Accordion>

<Accordion title="View Account Secrets">
  To view a secret, select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=7079fc956e29af9b424e7ebb698a45a7" alt="eye icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/eye.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=317ec5fd6c6b79d803aac063a78f9568 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a903c9a1c99b7cf63c6d73a8747655d9 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=97a66096841ce0b1f887d212ae94bd73 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e0747ce2aa09c30b172c5c996d2d8987 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=c1d86c81d578db02f4fea8cf02e450d0 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=10907b48c07ec82131726ce73527e96b 2500w" /> eye icon next to the secret.

  To hide the secret, select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye-slash.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=ae8689a686f591b697e1a9a9fd23d7ad" alt="eye with a slash icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/eye-slash.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye-slash.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d2d04539bdea500781b4eeff8cd6cc84 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye-slash.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=f0efb4c7ebe7510a2f227529957c69e3 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye-slash.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4a05ebd6d98894f0c0950124eee4fca1 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye-slash.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4ac412db5867aefe8e8bbc21d07dce60 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye-slash.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=9210692825e23123e892b0f67aaf5599 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/eye-slash.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e321ddb1fd92451a44d0e30f289848f4 2500w" /> eye with slash icon.
</Accordion>

<Accordion title="Link Account Secrets">
  To use an account-level secret in a Replit App, you must link it to the app.
  To link an account-level secret:

  1. Navigate to the **App Secrets** tab.
  2. Select the checkbox to the left of the secret.
  3. Select **Link to this App**.

  To unlink a secret:

  1. Navigate to the **App Secrets** tab.
  2. Select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d6ac2757eaf25e61d31ce51316ec91ad" width="16" height="16" alt="three vertical dots icon" data-og-width="24" data-og-height="24" data-path="images/icons/vertical-dots.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=cf215ef22f55bf163c0037f923584e37 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=9659b713156cc159f2b9107450cc0fbd 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=73cb1af8587233823aba8f0aec72d1d9 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5d633ba6d10d1d6d6d179b3086869257 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5255815ba3d626d74ede11e23698ccbd 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=15dffd4252b85614141c73a628671cf1 2500w" /> vertical dots menu next to the secret.
  3. Select **Unlink**.
</Accordion>

<Accordion title="Delete Account Secrets">
  1. Select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/pencil-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=9fe8b0d62049a6cc25ff54186cd82167" alt="pencil icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/pencil-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/pencil-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=70f222a550c10565fda88d2a405f0919 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/pencil-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=2e0254eba779d03f1854e9dceaca64f3 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/pencil-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=63823efefad606fd66371d96f5d4069a 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/pencil-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=0529386335540e80fc49377dbccc8cdd 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/pencil-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=0479fb149fec299ab1c26d5c723a534f 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/pencil-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a9a6290741fad3dcd5d918c07bd79adc 2500w" /> pencil icon next to the secret.
  2. Select **Delete**.
</Accordion>

### Access secrets in your code

<CodeGroup>
  ```python Python theme={null}
  import os
  print(os.getenv("MY_SECRET"))
  ```

  ```javascript JavaScript theme={null}
  console.log(process.env.MY_SECRET);
  ```

  ```java Java theme={null}
  System.out.println(System.getenv("MY_SECRET"))
  ```

  ```csharp C# theme={null}
  using System;
  Console.WriteLine(Environment.GetEnvironmentVariable("MY_SECRET"));
  ```

  ```go Go theme={null}
  package main
  import (
      "fmt"
      "os"
  )
  func main() {
      fmt.Println(os.Getenv("MY_SECRET"))
  }
  ```

  ```ruby Ruby theme={null}
  puts ENV["MY_SECRET"]
  ```
</CodeGroup>

### Managing secrets visibility

Secrets visibility depends on your access to a Replit App and whether you authored it.

You can use one of the options to share your Replit App:

* **Multiplayer**: Invite Replit users to collaborate in real-time
* **Cover page**: Show a preview of your Replit App with the option to remix it
* **Remix**: Make your individual or organization's Replit App public so others can create their version

The following table shows secret name and value visibility in the different scenarios:

| Access Method      | Who                                        | Can See Names | Can See Values |
| ------------------ | ------------------------------------------ | ------------- | -------------- |
| Multiplayer        | Multiplayer collaborator                   | ✓             | ✓              |
| Multiplayer        | Organization member (Owner role)           | ✓             | ✓              |
| Multiplayer        | Organization member (Non-owner)            | ✓             |                |
| Cover Page         | Any visitor                                |               |                |
| Remix              | Owner/collaborator remixing own Replit App | ✓             | ✓              |
| Remix              | Non-owner/collaborator remixing Replit App | ✓             |                |
| Remix              | Anyone remixing from cover page            | ✓             |                |
| Organization Remix | Organization member with Owner role        | ✓             | ✓              |
| Organization Remix | Organization member without Owner role     | ✓             |                |

<Warning>
  Organization members without the Owner role cannot view secret values in a Replit App, but can access their values by printing the environment variables.
</Warning>

## Database and storage related secrets

When you add Replit's database or object storage, the workspace automatically creates the following secrets:

| Secret         | Description                    |
| -------------- | ------------------------------ |
| `DATABASE_URL` | SQL database connection string |
| `PGHOST`       | PostgreSQL hostname            |
| `PGUSER`       | PostgreSQL username            |
| `PGPASSWORD`   | PostgreSQL password            |
| `PGDATABASE`   | PostgreSQL database name       |
| `PGPORT`       | PostgreSQL port                |

To view all environment variables in your Replit App, run `printenv` in the Shell workspace tool or print them from your code.

## Predefined environment variables

Replit automatically sets the following environment variables that you can access from your app:

| Environment Variable | Description                                                                            |
| -------------------- | -------------------------------------------------------------------------------------- |
| `REPLIT_DOMAINS`     | Comma-separated list of all domains associated with your Replit App                    |
| `REPLIT_USER`        | Username of the current editor, which may vary in Multiplayer sessions                 |
| `REPLIT_DEPLOYMENT`  | Set to `1` if the code is running in a published app, unset otherwise                  |
| `REPLIT_DEV_DOMAIN`  | Development URL on the `replit.dev` domain, which is different from the Deployment URL |

These are not listed in the Secrets tool, but you can access them in your code using the `os.environ` object or running `printenv` in the Shell.
