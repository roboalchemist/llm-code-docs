# Source: https://dub.co/docs/api-reference/publishable-keys.md

# Publishable keys

> Learn how publishable keys work on Dub.

Publishable keys on Dub allow you to safely embed authentication in client-side applications.
These keys are specifically designed to be used with [Dub's client-side SDKs](/sdks/client-side/introduction) for features like [conversion tracking](/sdks/client-side/features/conversion-tracking).

Unlike [API keys](/api-reference/tokens) which must be kept secret, publishable keys can be safely exposed in your frontend code since they have limited capabilities.

Publishable keys on Dub follow the format:

```bash .env theme={null}
DUB_PUBLISHABLE_KEY=dub_pk_xxxxxxxxxxxxxxxxxxxxxxxx
```

## Create a publishable key

You can create a publishable key by following these steps:

<Steps>
  <Step title="Generate your publishable key">
    Before you can track conversions on the client-side, you need to generate a [publishable key](/api-reference/publishable-keys) from your Dub workspace.

    To do that, navigate to your [workspace's Analytics settings page](https://app.dub.co/settings/analytics) and generate a new publishable key under the **Publishable Key** section.

    <Frame>
      <img src="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=76add1f30a997ba897f10acdc21b51b5" alt="Enabling conversion tracking for a workspace" data-og-width="2985" width="2985" data-og-height="2021" height="2021" data-path="images/conversions/publishable-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=280&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=f0f995d217914793d81c0a42ccda502a 280w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=560&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=62a390272e2b24b6ae8cf3ba98dac66f 560w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=840&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=cdb86db75f933f33be21d4a0e8293227 840w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=1100&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=ab9b7ec6577587e197e1fefeaa250216 1100w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=1650&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=ab5f37e61472d2c6118f7b640a5fdb50 1650w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=2500&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=6d83d47d0988ee0d895606f8b2e683c6 2500w" />
    </Frame>
  </Step>

  <Step title="Allowlist your site's domain">
    Then, you'll need to allowlist your site's domain to allow the client-side conversion events to be ingested by Dub.

    To do that, navigate to your [workspace's Analytics settings page](https://app.dub.co/settings/analytics) and add your site's domain to the **Allowed Hostnames** list.

    This provides an additional layer of security by ensuring only authorized domains can track conversions using your publishable key.

    <Frame>
      <img src="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=da26eba128e89211e7bfd7cf46ba32e0" alt="Enabling conversion tracking for a workspace" data-og-width="2979" width="2979" data-og-height="2018" height="2018" data-path="images/conversions/allowed-hostnames.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=280&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=58dbd9580cedff38a40a0f6ad6fe7188 280w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=560&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=ace60f5cf513d21281be79ead24189e6 560w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=840&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=33fff99044f2b77702dcc24ade6f67d7 840w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=1100&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=134d6038e2ad8da21e39a7b8e797fee2 1100w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=1650&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=b3051b73df5fdf2bd16b5db5aa4d34a5 1650w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=2500&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=e3f56a578de0f460c8a77f08aa33e437 2500w" />
    </Frame>

    You can group your hostnames when adding them to the allow list:

    * `example.com`: Tracks traffic **only** from `example.com`.
    * `*.example.com`: Tracks traffic from **all subdomains** of `example.com`, but **not** from `example.com` itself.

    <Tip>
      When testing things out locally, you can add `localhost` to the **Allowed
      Hostnames** list temporarily. This will allow local events to be ingested by
      Dub. Don't forget to remove it once you're ready to go live!
    </Tip>
  </Step>

  <Step title="Use your publishable key">
    You can now use your publishable key to authenticate client-side requests in your application. Usage will depend on the client-side SDK you are using.
  </Step>
</Steps>
