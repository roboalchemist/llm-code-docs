# Source: https://wafris.org/docs/rule_setting/allow_cidrs/

Title: Allow CIDRs

URL Source: https://wafris.org/docs/rule_setting/allow_cidrs/

Markdown Content:
The Allow CIDRs feature allows you to whitelist specific IP address ranges using CIDR notation to ensure they are not blocked by other security features. This can be useful for allowing access to your site from trusted networks or services.

[](https://wafris.org/docs/rule_setting/allow_cidrs/#how-to-allow-cidrs) How to Allow CIDRs
-------------------------------------------------------------------------------------------

1. Navigate to the Allow CIDRs section in your dashboard.
2. You’ll see a form with the following fields:

    *   **CIDR Range**: Enter the CIDR range you want to allow. For example: “192.168.1.0/24”
    *   **Note** (optional): Add a date or reason for allowing this CIDR range. This can help you keep track of why certain CIDR ranges were allowed.

3.   After entering the CIDR range and optional note, click the “Save Rule” button to apply the allow rule.

[](https://wafris.org/docs/rule_setting/allow_cidrs/#cidr-notation) CIDR Notation
---------------------------------------------------------------------------------

CIDR (Classless Inter-Domain Routing) notation is a compact method for specifying IP addresses and their associated routing prefix. The notation is constructed from:

* An IP address (e.g., 192.168.100.0)
* Followed by a slash (“/”)
* The number of bits in the routing prefix (e.g., 24)

For example, 192.168.100.0/24 represents the IPv4 addresses from 192.168.100.0 to 192.168.100.255, and 2001:0db8:85a3:0000:0000:8a2e:0370:7334/64 represents the IPv6 addresses from 2001:0db8:85a3:0000:0000:8a2e:0370:7334 to 2001:0db8:85a3:0000:0000:8a2e:0370:7334.

[](https://wafris.org/docs/rule_setting/allow_cidrs/#best-practices) Best Practices
-----------------------------------------------------------------------------------

* Keep a record of why you’ve allowed specific CIDR ranges using the Note field.
* Regularly review your allowed CIDR ranges to ensure they’re still necessary.
* Combine this feature with other security measures, such as [Block IPs](https://wafris.org/rule_setting/block_ips), [Block CIDR Ranges](https://wafris.org/rule_setting/block_cidrs), and [Block Countries](https://wafris.org/rule_setting/block_countries), to create a robust security strategy.
* Test your allowed CIDR ranges regularly to ensure they are not being blocked by other security features.

* * *
