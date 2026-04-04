# Source: https://wafris.org/docs/rule_setting/block_paths/

Title: Block Paths

URL Source: https://wafris.org/docs/rule_setting/block_paths/

Markdown Content:
The Block Paths feature allows you to block specific URL paths from being accessed on your site. This can be useful for security purposes or to manage traffic to certain areas of your site. For example, you might want to block access by default to a specific directory or a sensitive page.

[](https://wafris.org/docs/rule_setting/block_paths/#how-to-block-paths) How to Block Paths
-------------------------------------------------------------------------------------------

1. Navigate to the Block Paths section in your dashboard.
2. You’ll see a form with the following fields:

    *   **Path**: Enter the URL path you want to block. For example: “/admin” or “/secret-page”
    *   **Note** (optional): Add a date or reason for blocking this path. This can help you keep track of why certain paths were blocked.

3.   After entering the path and optional note, click the “Save Rule” button to apply the block.

[](https://wafris.org/docs/rule_setting/block_paths/#best-practices) Best Practices
-----------------------------------------------------------------------------------

* Keep a record of why you’ve blocked specific paths using the Note field.
* Regularly review your blocked paths to ensure they’re still necessary.
* Leverage the [Block IPs](https://wafris.org/rule_setting/block_ips) feature to block entire IP addresses based on their past behavior.
* Use the [Block Countries](https://wafris.org/rule_setting/block_countries) feature to block all requests from specific countries.
* Combine this feature with other security measures, such as [Block IPs by Reputation](https://wafris.org/rule_setting/block_ips_by_reputation), [Block CIDR Ranges](https://wafris.org/rule_setting/block_cidrs), and [Block Hosts](https://wafris.org/rule_setting/block_hosts), to create a robust security strategy.

* * *
