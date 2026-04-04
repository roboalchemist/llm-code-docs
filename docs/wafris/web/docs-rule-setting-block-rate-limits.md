# Source: https://wafris.org/docs/rule_setting/block_rate_limits/

Title: Block Rate Limits

URL Source: https://wafris.org/docs/rule_setting/block_rate_limits/

Markdown Content:
The Block Rate Limits feature allows you to limit the number of requests from a single IP address within a specified time frame. This can be useful for preventing brute-force attacks, denial-of-service (DoS) attacks, or other malicious activities that involve a high volume of requests.

[](https://wafris.org/docs/rule_setting/block_rate_limits/#how-to-block-rate-limits) How to Block Rate Limits
-------------------------------------------------------------------------------------------------------------

1. Navigate to the Block Rate Limits section in your dashboard.
2. Define the conditions for the rate limit.
    ***Path**: Specify the URL path you want to apply rate limits to. For example: “/api/v1/login”
    *   **Method**: Choose the HTTP method you want to apply rate limits to. For example: “GET”, “POST”, “PUT”, “DELETE”

3. Define the limits for that condition.

    *   **Max Requests**: Enter the maximum number of requests allowed within the time frame.
    *   **Time Interval**: Enter the time frame in seconds (e.g. 60 for 1 minute, 300 for 5 minutes, 3600 for 1 hour, 86400 for 1 day).
    *   **Note** (optional): Add a date or reason for applying rate limits to this IP. This can help you keep track of why certain IPs have rate limits.

4.   After entering the IP address, rate limit, time frame, and optional note, click the “Save Rule” button to apply the rate limit.

[](https://wafris.org/docs/rule_setting/block_rate_limits/#best-practices) Best Practices
-----------------------------------------------------------------------------------------

* Set rate limits for sensitive paths like authentication endpoints
* Adjust rate limits based on the IP’s behavior over time.
* Combine this feature with other security measures, such as [Block IPs](https://wafris.org/rule_setting/block_ips), [Block CIDR Ranges](https://wafris.org/rule_setting/block_cidrs), and [Block Countries](https://wafris.org/rule_setting/block_countries), to create a robust security strategy.
* Regularly review your rate limits to ensure they’re still necessary and adjust them as needed.

* * *
