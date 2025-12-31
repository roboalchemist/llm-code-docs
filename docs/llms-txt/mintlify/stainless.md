# Source: https://mintlify.com/docs/integrations/sdks/stainless.md

# Stainless

> Automate SDK code samples in your API playground.

## Prerequisites

* Have a [Stainless](https://app.stainless.com) account.

## Integrate with Stainless

<Steps>
  <Step title="Set up OpenAPI decoration in Stainless.">
    In your `stainless.yml` config file, add `openapi.code_samples: 'mintlify'`. See the [Stainless documentation](https://app.stainless.com/docs/guides/integrate-docs) for more information.
  </Step>

  <Step title="Publish the URL to your OpenAPI spec.">
    In your Stainless project:

    1. Select the **Release** tab.
    2. Select **Setup OpenAPI publishing**.
    3. Copy the URL to your publicly accessible OpenAPI spec.

    <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/stainless-public-OpenAPI-spec.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=74e968242d6e3c42818a57f2523ecdfe" alt="Stainless release page with the OpenAPI spec URL highlighted with a green box." data-og-width="2124" width="2124" data-og-height="1104" height="1104" data-path="images/stainless-public-OpenAPI-spec.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/stainless-public-OpenAPI-spec.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=747726b4e3e0b16569489d1c4fc079f0 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/stainless-public-OpenAPI-spec.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e07b40dc864d23bfddc83454fe247789 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/stainless-public-OpenAPI-spec.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=cd9e6775af76098ed9c2a03221d07aca 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/stainless-public-OpenAPI-spec.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=27f330e38be672687f720beea97705bd 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/stainless-public-OpenAPI-spec.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=cc11946cfa1f54a50b72c4058548f2b3 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/stainless-public-OpenAPI-spec.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=81a2899ea97575ebbe3f189be611b424 2500w" />
  </Step>

  <Step title={<>Add your OpenAPI spec URL to your <code>docs.json</code>.</>}>
    In your `docs.json` file, add the URL from Stainless to the `openapi` field. See [OpenAPI Setup](/api-playground/openapi-setup) for more information.
  </Step>
</Steps>
