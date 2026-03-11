# Source: https://wafris.org/docs/rule_setting/allow_ips/

Title: Allow IPs

URL Source: https://wafris.org/docs/rule_setting/allow_ips/

Markdown Content:
The Allow IPs feature allows you to whitelist specific IP addresses to ensure they are not blocked by other security features. This can be useful for allowing access to your site from trusted sources, such as your office network or a specific service provider.

[](https://wafris.org/docs/rule_setting/allow_ips/#how-to-allow-ips) How to Allow IPs
-------------------------------------------------------------------------------------

1. Navigate to the Allow IPs section in your dashboard.
2. You’ll see a form with the following fields:

    *   **IP Address**: Enter the IP address you want to allow. For example: “192.168.1.1”
    *   **Note** (optional): Add a date or reason for allowing this IP. This can help you keep track of why certain IPs were allowed.

3.   After entering the IP address and optional note, click the “Save Rule” button to apply the allow rule.

[](https://wafris.org/docs/rule_setting/allow_ips/#best-practices) Best Practices
---------------------------------------------------------------------------------

* Keep a record of why you’ve allowed specific IPs using the Note field.
* Regularly review your allowed IPs to ensure they’re still necessary.
* Combine this feature with other security measures, such as [Block IPs](https://wafris.org/rule_setting/block_ips), [Block CIDR Ranges](https://wafris.org/rule_setting/block_cidrs), and [Block Countries](https://wafris.org/rule_setting/block_countries), to create a robust security strategy.
* Test your allowed IPs regularly to ensure they are not being blocked by other security features.

* * *
