# Source: https://docs.xano.com/xano-features/instance-settings/static-ip-outgoing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Static IP (Outgoing)

<Info>
  At this time, Static IP is only available for instances in the United States, Saudi Arabia, France, Indonesia, South Korea, and Japan.

  For users who have had long-standing instances on the United States region, you may not immediately have Static IP available as an option. Please reach out to our Support team for further clarification and next steps.
</Info>

Static IP address is available on any paid plan address for outgoing API requests. This is commonly required by 3rd party API providers requiring an IP whitelist.

Your static IP will only apply to outgoing requests -- meaning requests you make to third-party APIs using the [External API Request](/the-function-stack/functions/apis-and-lambdas/external-api-request) function.

### How to Enable Static IP

To add Static IP to your Xano instance, head to your Billing screen, and choose Change Plan.

On the next screen, choose Select Additional Upgrades, and then choose to enable Static IP from the panel that opens.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/72371800-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=6f4e600f74a74afb344ece4643b3e1a2" width="875" height="495" data-path="images/72371800-image.jpeg" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e6ae37b0-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=cc2d3f4c90a98d2edd01d2c991439b2c" width="473" height="248" data-path="images/e6ae37b0-image.jpeg" />
</Frame>

After proceeding through checkout, you'll be taken to the instance selection screen where you'll see that your instance has a pending upgrade.

Adding Static IP to your Xano plan requires migrating your data to a new instance. This means that your API endpoint base URL will change. We do not process the migration manually to give you time to update any connections that may be necessary prior to the transition. Just click the prompt whenever you're ready.

### Finding your Static IP

From your instance selection screen, click the⚙️ icon.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/0e6e7460-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=f101682eec5dac73e8d38cd415e0afb5" width="933" height="208" data-path="images/0e6e7460-image.jpeg" />
</Frame>

On the panel that opens, choose Instance Details.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/6a94b357-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=ee1e34e8db1daebd983f938c62f51fbd" width="434" height="421" data-path="images/6a94b357-image.jpeg" />
</Frame>

On the next pane, you can scroll down to the bottom and see your new static IP address for outgoing requests, which you can then provide to any third-party services that require it.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/90d070f5-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=ff91a7f663ec2f3da27789977a57be55" width="592" height="1388" data-path="images/90d070f5-image.jpeg" />
</Frame>


Built with [Mintlify](https://mintlify.com).