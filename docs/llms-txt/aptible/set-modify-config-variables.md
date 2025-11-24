# Source: https://www.aptible.com/docs/how-to-guides/app-guides/set-modify-config-variables.md

# How to set and modify configuration variables

Learn how to set and modify app [configuration variables](/core-concepts/apps/deploying-apps/configuration). Setting or modifying app configuration variables always restarts the app to apply the changes. Follow our [synchronize configuration and code changes guide](/how-to-guides/app-guides/synchronize-config-code-changes) to update the app configuration and deploy code using a single deployment.&#x20;

## Using the Dashboard

Configuration variables can be set or modified in the Dashboard in the following ways:

* While deploying new code by:

  * Using the [**Deploy**](https://app.aptible.com/create) tool will allow you to set environment variables as you deploy your code <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/config-var1.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=321d06902821e61cc2531a40a5bcb944" alt="" data-og-width="2000" width="2000" data-og-height="2000" height="2000" data-path="images/config-var1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/config-var1.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=05fc9bd061992a3562329adc05d2d34f 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/config-var1.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=18947b6a1f38a568b66bd0a6eadb0958 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/config-var1.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=72953272c9fc7fa0cb2e13367d6cc6f3 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/config-var1.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=f5f26e141bf4fdea402073db0f985276 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/config-var1.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=5882316bfba1818d128866eaf9cf800c 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/config-var1.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=eb1c244e117a1b7409552ec912e919d3 2500w" />

* For existing apps by:

  * Navigating to the respective app

  * Selecting the **Configuration** tab

  * Selecting **Edit** within Edit Environment Variables <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/config-var2.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ed3627d46fa098c2ca022af3d5e4f9ee" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/config-var2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/config-var2.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=92fc6da045262715601067d42c0b39b3 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/config-var2.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=d9cd37b9f7132793ef89ccf1f1439fb0 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/config-var2.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=e5f1d3c5596d446f7de0f20c188fcd5d 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/config-var2.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=3814d031d958365695824c4f160eb52b 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/config-var2.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ad5db8393dc60cd84931209952207742 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/config-var2.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=22e9f755ec58d6c9fe835d3f34f69f89 2500w" />

## Using the CLI

Configuration variables can be set or modified via the CLI in the following ways:

* Using [`aptible deploy`](/reference/aptible-cli/cli-commands/cli-deploy) command

* Using the [`aptible config:set`](/reference/aptible-cli/cli-commands/cli-config-set) command

## Size Limits

A practical limit for configuration variable length is 65,536 characters.
