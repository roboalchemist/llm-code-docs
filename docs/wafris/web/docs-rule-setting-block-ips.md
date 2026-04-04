# Source: https://wafris.org/docs/rule_setting/block_ips/

Title: Block IPs

URL Source: https://wafris.org/docs/rule_setting/block_ips/

Markdown Content:
The Block IPs feature allows you to prevent specific IP addresses from accessing your site. This can be useful for security purposes or to manage traffic from certain IP addresses. For example, you might find an IP address that is persistently making requests to your site, and you want to block it.

[](https://wafris.org/docs/rule_setting/block_ips/#how-to-block-ips) How to Block IPs
-------------------------------------------------------------------------------------

1. Navigate to the Block IPs section in your dashboard.
2. You’ll see a form with the following fields:

    *   **IP Address**: Enter the IP address you want to block. For example: “192.168.1.1”
    *   **Note** (optional): Add a date or reason for blocking this IP. This can help you keep track of why certain IPs were blocked.

3.   After entering the IP address and optional note, click the “Save Rule” button to apply the block.

[](https://wafris.org/docs/rule_setting/block_ips/#best-practices) Best Practices
---------------------------------------------------------------------------------

* Keep a record of why you’ve blocked specific IPs using the Note field.
* Leverage the [Block CIDR Ranges](https://wafris.org/rule_setting/block_cidrs) to block entire networks based on their IP address ranges.
* Use the [Block Countries](https://wafris.org/rule_setting/block_countries) feature to block all IPs from specific countries.
* Block IPs based on their past behavior with the [Block IPs by Reputation](https://wafris.org/rule_setting/block_ips_by_reputation) feature.

* * *
