# Source: https://www.activepieces.com/docs/install/troubleshooting/websocket-issues.md

# Websocket Issues

> Troubleshoot websocket connection problems

If you're experiencing issues with websocket connections, it's likely due to incorrect proxy configuration. Common symptoms include:

* Test Flow button not working
* Test step in flows not working
* Real-time updates not showing

To resolve these issues:

1. Ensure your reverse proxy is properly configured for websocket connections
2. Check our [Setup HTTPS](/install/guides/setup-ssl) guide for correct configuration examples
3. Some browsers block http websocket connections, please setup SSL to resolve this issue.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.activepieces.com/docs/llms.txt