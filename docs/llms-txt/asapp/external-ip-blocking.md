# Source: https://docs.asapp.com/security/external-ip-blocking.md

# External IP Blocking

> Use External IP Blocking to block IP addresses from accessing your data.

ASAPP has tools in place to monitor and automatically block activity based on malicious behavior and bad reputation sources (IPs). This blocking inhibits traffic from IPs that could damage, disable, overburden, disrupt or impair any ASAPP servers or APIs.

By default, ASAPP does not block IPs of end users who exhibit abusive behaviors towards agents. IP blocking is trivial to evade and often causes unintended collateral damage to normal users since IP address are dynamic.

It can happen that a previously blocked IP address become the IP address for a valid user, preventing the valid user from using ASAPP and your product.

While we do not recommend IP blocking, you are still able to block users by IP address to help address urgent protection needs.

## Blocking IP Addresses on AI Console

AI-Console provides the ability for administrators with the correct permissions to block external IP addresses that may present a threat to your organization.

To block an IP Address in AI Console:

1. Manually enter (or copy) an individual IP address in the Denylist
2. Click Save and Deploy to save the changes to production

You are able to access IP Addresses in Conversation Manager, giving you insight into the IP address associated with potentially malicious users.

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-372e0f2b-7357-8f03-3120-540923097202.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=9327070a3ad2f38afece80e4c3fb2ead" data-og-width="1440" width="1440" data-og-height="900" height="900" data-path="image/uuid-372e0f2b-7357-8f03-3120-540923097202.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-372e0f2b-7357-8f03-3120-540923097202.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=03e5bcb46213a7469732dbc6e64201a5 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-372e0f2b-7357-8f03-3120-540923097202.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=6cc8fd03e4c5320a8d69232e6630cebd 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-372e0f2b-7357-8f03-3120-540923097202.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=ec3b94125ee56473838687eeb0e299d6 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-372e0f2b-7357-8f03-3120-540923097202.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=a69e9cc3f43308f0038b175622da0302 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-372e0f2b-7357-8f03-3120-540923097202.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=746dd41defbed575730de047d1a09b98 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-372e0f2b-7357-8f03-3120-540923097202.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=e0b0beec1ff1cff9c06122c6c8613bae 2500w" />
</Frame>

IP Addresses can be unblocked by clicking the trash icon on the blocked IP's row, and then saving and deploying the updated list.

<Note>
  Blocked users receive an error message and the Chat bubble will not appear at the end of their screen.

  From the API perspective,  *shouldDisplayWebChat* will return a **503 Forbidden** error
</Note>

## Additional Contextual Information

Dynamic's ISP IP rotates quite often. This means that the 1-1 relationship between a public IP and an individual/device/client is merely temporary and the assignment will continually change in the future as described below.

**ISP Assignation within the Time**

IP(1) --- UserA

IP(2) --- UserB

IP(3) --- UserC

.......................

IP(1) --- UserC

IP(2) --- UserB

IP(3) --- UserA

If ASAPP prevents UserA from reaching our platform by blocking IP(1), there is a risk that ISPs assign IP(1) to UserB or UserC at some point in the future.

There are also many scenarios where legitimate users share a single IP with abusive users, such as public WiFi networks:

* Company named networks
* College or corporate campuses that route many users from a single outbound IP
* Personal and corporate VPN devices that aggregate many uses to a single IP

Blocking those IP's will prevent many other legitimate users from access to the ASAPP platform.
