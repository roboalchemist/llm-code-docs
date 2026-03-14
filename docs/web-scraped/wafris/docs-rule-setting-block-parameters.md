# Source: https://wafris.org/docs/rule_setting/block_parameters/

Title: Block Parameters

URL Source: https://wafris.org/docs/rule_setting/block_parameters/

Markdown Content:
The Block Parameters feature allows you to block specific URL parameters from being passed in requests to your site. For example, you might want to block requests from compromised API keys, fraudlent affiliate codes, or other parameters that are known to be malicious.

[](https://wafris.org/docs/rule_setting/block_parameters/#how-to-block-parameters) How to Block Parameters
----------------------------------------------------------------------------------------------------------

1. Navigate to the Block Parameters section in your dashboard.
2. You’ll see a form with the following fields:

    *   **Pattern**: Enter the substring pattern of the parameter you want to block. For example: “api_key” or “my_bad_affiliate_code”
    *   **Note** (optional): Add a date or reason for blocking this parameter. This can help you keep track of why certain parameters were blocked.

3.   After entering the parameter, optional value, and optional note, click the “Save Rule” button to apply the block.

[](https://wafris.org/docs/rule_setting/block_parameters/#best-practices) Best Practices
----------------------------------------------------------------------------------------

* Keep a record of why you’ve blocked specific parameters using the Note field.
* Regularly review your blocked parameters to ensure they’re still necessary.
* Leverage the [Block IPs](https://wafris.org/rule_setting/block_ips) feature to block entire IP addresses based on their past behavior.
* Use the [Block Countries](https://wafris.org/rule_setting/block_countries) feature to block all requests from specific countries.

* * *
