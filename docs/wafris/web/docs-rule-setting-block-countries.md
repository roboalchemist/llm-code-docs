# Source: https://wafris.org/docs/rule_setting/block_countries/

Title: Block Countries

URL Source: https://wafris.org/docs/rule_setting/block_countries/

Markdown Content:
The Block Countries feature allows you to prevent access to your site from specific countries. This can be useful for managing traffic, complying with regional restrictions, or enhancing security.

[](https://wafris.org/docs/rule_setting/block_countries/#how-to-block-countries) How to Block Countries
-------------------------------------------------------------------------------------------------------

1. Navigate to the Block Countries section in your [Wafris Hub](https://hub.wafris.com/) dashboard.
2. You’ll see a user interface with the following elements:

    *   Either choose individual countries or groups of countries:
        *   Africa
        *   Asia
        *   Australia and Oceana
        *   Europe
        *   North America
        *   South America

3.   Use the “Select” buttons to quickly choose groups of countries or manually check/uncheck individual countries.
4.   After making your selection, click the “Update Blocked Countries” button to apply the changes. Changes will not apply until updated.

[](https://wafris.org/docs/rule_setting/block_countries/#important-notes) Important Notes
-----------------------------------------------------------------------------------------

* Some compliance regulations require you to block certain sanctioned countries (ex: US FINCEN regulations require that North Korea be blocked)
* Blocking countries is a good way to reduce the overall attack surface of your site. Not doing business in Burkina Faso? Block access from there.
* Blocking countries temporarily can also help you defend your site from DDoS attacks or other attacks that often originate from certain countries.
* Be aware that some users may use VPNs or proxies to bypass country restrictions. The [Block IPs by Reputation](https://wafris.org/rule_setting/block_ips_by_reputation) feature can help you block abusive VPN and Proxy networks.

[](https://wafris.org/docs/rule_setting/block_countries/#best-practices) Best Practices
---------------------------------------------------------------------------------------

* Regularly review your blocked countries to ensure the restrictions are still necessary and aligned with your business needs.
* Use this feature in conjunction with [Block CIDR Ranges](https://wafris.org/rule_setting/block_cidrs) for more granular control over IP-based access restrictions.
* Be aware of any legal implications or service agreements that may be affected by country-based blocking.
* Consider providing alternative access methods or clear communication for users in blocked countries who may have legitimate reasons to access your site.
* Individual users or networks that have been added to the [Allowed IPs](https://wafris.org/rule_setting/allowed_ips) list will not be blocked.

* * *
