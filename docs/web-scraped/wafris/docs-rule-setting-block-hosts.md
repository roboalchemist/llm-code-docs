# Source: https://wafris.org/docs/rule_setting/block_hosts/

Title: Block Hosts

URL Source: https://wafris.org/docs/rule_setting/block_hosts/

Markdown Content:
The Block Hosts feature allows you to prevent specific hosts from accessing your site. This can be useful for security purposes or to manage traffic from certain hosts. For example, you might specify a subdomain like `admin.example.com` which you want to block all traffic to by default, only allowing explitly allowed requests from [Allowed IPs](https://wafris.org/rule_setting/allowed_ips).

[](https://wafris.org/docs/rule_setting/block_hosts/#how-to-block-hosts) How to Block Hosts
-------------------------------------------------------------------------------------------

1. Navigate to the Block Hosts section in your dashboard.
2. You’ll see a form with the following fields:

    *   **Host**: Enter the hostname you want to block. For example: “example.com”
    *   **Note** (optional): Add a date or reason for blocking this host. This can help you keep track of why certain hosts were blocked.

3.   After entering the hostname and optional note, click the “Save Rule” button to apply the block.

[](https://wafris.org/docs/rule_setting/block_hosts/#best-practices) Best Practices
-----------------------------------------------------------------------------------

* Keep a record of why you’ve blocked specific hosts using the Note field.
* Regularly review your blocked hosts to ensure they’re still necessary.
* Leverage the [Block CIDR Ranges](https://wafris.org/rule_setting/block_cidrs) to block entire networks based on their IP address ranges.
* Use the [Block Countries](https://wafris.org/rule_setting/block_countries) feature to block all hosts from specific countries.

* * *
