# Source: https://docs.firehydrant.com/docs/secrets.md

# Secrets

> 📘 Note:
>
> Organization secrets are currently only usable inside a [Send a Webhook](https://docs.firehydrant.com/docs/runbook-step-send-a-webhook) Runbook step.

When configuring your Runbook webhook step, sometimes you'll want to use secret values such as tokens or other items needed in authorization headers.

You can configure this under **Settings> Integrations > Secrets**.

<Image alt="The Secrets settings page" align="center" width="650px" src="https://files.readme.io/5e80753-image.png">
  The Secrets settings page
</Image>

These secrets are encrypted when stored and will not be visible when used inside the Runbook step or within the UI after initial creation.

You can make use of these secrets by referring to their keys via the `secrets` Liquid variable. For example, for a secret called "my\_token", you would use `{{ secrets.my_token }}` in Liquid.

If you use dashes in the key, Liquid templating will run into issues trying to refer to it using standard dot notation.

So, instead of referring to the variable as `{{ secrets.with-dashes }}`, you should instead use property notation: `{{ secrets['with-dashes'] }}`.