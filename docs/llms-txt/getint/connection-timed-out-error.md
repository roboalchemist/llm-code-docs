# Source: https://docs.getint.io/support-legal-and-others/troubleshooting-guide-for-getint-users/connection-timed-out-error.md

# Connection Timed Out Error

**Issue**: Intermittent connectivity issues between Getint and respective Apps

**Description**: After a successful connection between Getint and respective Apps (JIRA, ServiceNow, Freshdesk, etc.) has been established, there might be a connection failure in certain instances. And the following error message would be displayed (in this case, ServiceNow).

**\[ERROR] 2024-01-09T13:47:19.747Z - \[main-0-1408647-119] Error occurred when performing flow**\
**org.apache.http.conn.HttpHostConnectException: Connect to** 123&#x34;**.service-now\.com:443 \[**&#x53;erviceNow **] failed: Connection timed out (Connection timed out)**

**Solution**:

This error would occur when a network connection could not be established. Getint will not be able to investigate in such scenarios; instead, the customer's network team should investigate and resolve such issues.
