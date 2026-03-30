# Source: https://plivo.com/docs/voice/concepts/ip-address-whitelisting.md

# Source: https://plivo.com/docs/messaging/concepts/ip-address-whitelisting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# IP Address Whitelisting

> Whitelist Plivo IP ranges for messaging API and callback traffic

To ensure that your communication infrastructure doesn’t block communication with Plivo, we encourage you to whitelist these IP address ranges for Messaging API.

Subscribe to be notified of any updates regarding IP address changes via email or RSS feed.

## Callbacks from Plivo

Some Plivo APIs elements support callback events. To make sure those callbacks are not blocked, allow traffic from these Plivo IP addresses to your web applications.

These IP addresses are NAT gateway IPs associated with our HTTP(s) OutProxy instance.

<table>
  <tbody>
    <tr>
      <td>Regions</td>
      <td>IP Addresses</td>
    </tr>

    <tr>
      <td>Ashburn, Virginia, USA</td>
      <td>18.211.55.148/32<br />18.211.27.222/32</td>
    </tr>

    <tr>
      <td>San Jose, California, USA</td>
      <td>13.56.175.187/32<br />13.57.139.231/32</td>
    </tr>
  </tbody>
</table>
