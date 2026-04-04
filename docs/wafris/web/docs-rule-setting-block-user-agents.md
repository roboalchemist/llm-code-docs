# Source: https://wafris.org/docs/rule_setting/block_user_agents/

Title: Block User Agents

URL Source: https://wafris.org/docs/rule_setting/block_user_agents/

Markdown Content:
The Block User Agents feature allows you to block specific user agents from accessing your site. This can be useful for security purposes or to manage traffic from certain user agents. For example, you might want to block access from AI Scraping bots or a bot user agents.

While the user-agent header on requests is easily spoofed, in practice, it remains a useful filter for identifying and blocking requests.

[](https://wafris.org/docs/rule_setting/block_user_agents/#how-to-block-user-agents) How to Block User Agents
-------------------------------------------------------------------------------------------------------------

1. Navigate to the Block User Agents section in your dashboard.
2. You’ll see a form with the following fields:

    *   **User Agent**: Enter the substring of the user agent you want to block. This is much more effective than blocking the entire user agent string. (ex: “Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3” -> “58.0.3029.110”)
    *   **Note** (optional): Add a date or reason for blocking this user agent. This can help you keep track of why certain user agents were blocked.

3.   After entering the user agent and optional note, click the “Save Rule” button to apply the block.

[](https://wafris.org/docs/rule_setting/block_user_agents/#best-practices) Best Practices
-----------------------------------------------------------------------------------------

* Keep a record of why you’ve blocked specific user agents using the Note field.
* Regularly review your blocked user agents to ensure they’re still necessary.
* Leverage the [Block IPs](https://wafris.org/rule_setting/block_ips) feature to block entire IP addresses based on their past behavior.
* Use the [Block Countries](https://wafris.org/rule_setting/block_countries) feature to block all requests from specific countries.
* Combine this feature with other security measures, such as [Block IPs by Reputation](https://wafris.org/rule_setting/block_ips_by_reputation), [Block CIDR Ranges](https://wafris.org/rule_setting/block_cidrs), and [Block Hosts](https://wafris.org/rule_setting/block_hosts), to create a robust security strategy.

* * *
