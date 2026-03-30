# Source: https://wafris.org/docs/rule_setting/block_cidrs/

Title: Block CIDRs

URL Source: https://wafris.org/docs/rule_setting/block_cidrs/

Markdown Content:
[](https://wafris.org/docs/rule_setting/block_cidrs/#block-cidr-ranges) Block CIDR Ranges
-----------------------------------------------------------------------------------------

The Block CIDR Ranges feature allows you to prevent specific IP address ranges from accessing your site. This can be useful for security purposes or to manage traffic from certain networks.

[](https://wafris.org/docs/rule_setting/block_cidrs/#how-to-block-cidr-ranges) How to Block CIDR Ranges
-------------------------------------------------------------------------------------------------------

1. Navigate to the Block CIDR Ranges section in your dashboard.
2. You’ll see a form with the following fields:

    *   **CIDR Range**: Enter the CIDR network you want to block. For example: “1.2.3.4/24”
    *   **Note** (optional): Add a date or reason for blocking this range. This can help you keep track of why certain ranges were blocked.

3.   After entering the CIDR range and optional note, click the “Save Rule” button to apply the block.

[](https://wafris.org/docs/rule_setting/block_cidrs/#important-notes) Important Notes
-------------------------------------------------------------------------------------

* You can enter multiple CIDR ranges by adding them one at a time.
* The system will display the current number of ranges being blocked at the bottom of the form.
* Use the “Back” button to return to the previous screen without saving changes.

[](https://wafris.org/docs/rule_setting/block_cidrs/#cidr-notation) CIDR Notation
---------------------------------------------------------------------------------

CIDR (Classless Inter-Domain Routing) notation is a compact method for specifying IP addresses and their associated routing prefix. The notation is constructed from:

* An IP address (e.g., 192.168.100.0)
* Followed by a slash (“/”)
* The number of bits in the routing prefix (e.g., 24)

For example, 192.168.100.0/24 represents the IPv4 addresses from 192.168.100.0 to 192.168.100.255, and 2001:0db8:85a3:0000:0000:8a2e:0370:7334/64 represents the IPv6 addresses from 2001:0db8:85a3:0000:0000:8a2e:0370:7334 to 2001:0db8:85a3:0000:0000:8a2e:0370:7334.

[](https://wafris.org/docs/rule_setting/block_cidrs/#best-practices) Best Practices
-----------------------------------------------------------------------------------

* Keep a record of why you’ve blocked specific CIDR ranges using the Note field.
* Regularly review your blocked ranges to ensure they’re still necessary.
* Be cautious when blocking large CIDR ranges to avoid unintentionally blocking legitimate traffic. Often mobile networks present as a single IP or range for a massive amount of devices.
* Leverage the [Block IPs by Reputation](https://wafris.org/rule_setting/block_ips_by_reputation) to automatically block entire networks based on their reputation.
* Use the [Block Countries](https://wafris.org/rule_setting/block_countries) feature to block all networks from specific countries.

* * *
