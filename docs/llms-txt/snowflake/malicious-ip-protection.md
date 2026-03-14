# Source: https://docs.snowflake.com/en/user-guide/malicious-ip-protection.md

# Malicious IP Protection

## Overview

The Malicious IP Protection service continuously detects network access attempts that originate from IP addresses that are maintained on a
curated list. The service protects the Snowflake instance by blocking network access attempts that originate from those IP addresses. The
service hardens both Snowflake’s and the customer’s security posture by reducing the risk of unauthorized access, data breaches, and
malicious activity.

Snowflake maintains and curates a list of IP addresses, based on data that is obtained from third-party cybersecurity data sources that provide
external threat intelligence. The IP addresses are from known bad actors. The following table lists and describes how Snowflake categorizes
IP addresses based on impact analysis:

| IP Category | Description |
| --- | --- |
| ANONYMOUS_VPN | IP addresses associated with anonymous VPN services. |
| ANONYMOUS_PROXIES | IP addresses associated with anonymous proxy servers. |
| MALICIOUS_BEHAVIOR | IP addresses associated with known malware and behavior such as automated brute force login attempts. |
| TOR_EXITS | IP addresses used as exit nodes for the Tor network. |

The Malicious IP Protection service blocks network access attempts that originate from IP addresses in all categories on this curated list
by default.

## View network login details

You can use the Account Usage [LOGIN_HISTORY view](../sql-reference/account-usage/login_history.md) to see details of network access attempts that the Malicious
IP Protection service has blocked. For example, to view login events for your account, run the following query:

```sqlexample
SELECT *
  FROM SNOWFLAKE.ACCOUNT_USAGE.LOGIN_HISTORY
  WHERE NOT is_success AND login_details IS NOT NULL
  ORDER BY event_timestamp DESC;
```

Next, examine the `is_success` and `login_details` columns of the LOGIN_HISTORY view output for your account.

`NO` appears in the `is_success` column for blocked network access attempts.

The following examples show output that appears in the `login_details` column for blocked IP addresses:

Example — blocked IP categorized as “LOW” risk:

```json
{
  "malicious_ip_protection_info":"{\"result\":\"BLOCKED\",\"riskClassification\":\"LOW\",\"categories\":[\"MALICIOUS_BEHAVIOR\"]}"
}
```

Example — blocked IP categorized as “HIGH” risk:

```json
{
  "malicious_ip_protection_info":"{\"result\":\"BLOCKED\",\"riskClassification\":\"HIGH\",\"categories\":[\"ANONYMOUS_VPN\",\"ANONYMOUS_PROXIES\"]}"
}
```

The IP address that corresponds to each result appears in the `ip_address` column.

If you notice that IP addresses that were categorized as low-risk were blocked, you might choose to opt out of blocking that category.

## Manage Malicious IP Protection for low-risk categories

You can manage Malicious IP Protection by opting out of blocking IP addresses that are categorized as low-risk. You can’t opt out of blocking
IP addresses that are categorized as high-risk.

To opt out of blocking a category, run the [SYSTEM$OPT_OUT_MALICIOUS_IP_PROTECTION_BY_CATEGORY](../sql-reference/functions/system_opt_out_malicious_ip_protection_by_category.md) function and
provide a low-risk category name as an argument. For example:

```sqlexample
USE ROLE ACCOUNTADMIN;
SELECT SYSTEM$OPT_OUT_MALICIOUS_IP_PROTECTION_BY_CATEGORY('MALICIOUS_BEHAVIOR');
```

To opt out of blocking for a another category, run the [SYSTEM$OPT_OUT_MALICIOUS_IP_PROTECTION_BY_CATEGORY](../sql-reference/functions/system_opt_out_malicious_ip_protection_by_category.md)
function again and provide *both* low-risk category names as arguments. For example:

```sqlexample
USE ROLE ACCOUNTADMIN;
SELECT SYSTEM$OPT_OUT_MALICIOUS_IP_PROTECTION_BY_CATEGORY('ANONYMOUS_VPN,MALICIOUS_BEHAVIOR');
```

To re-enable blocking IP addresses, run the SYSTEM$OPT_OUT_MALICIOUS_IP_PROTECTION_BY_CATEGORY function and provide `''` as an argument.
For example:

```sqlexample
USE ROLE ACCOUNTADMIN;
SELECT SYSTEM$OPT_OUT_MALICIOUS_IP_PROTECTION_BY_CATEGORY('');
```

Optionally, run the function and provide a user name as the second argument to either opt out of, or re-enable, blocking of IP addresses for
only the user that you specify. For example, to disable Malicious IP Protection for IP addresses in the `ANONYMOUS_VPN` category for the
specific user `JSMITH`, run the following commands:

```sqlexample
USE ROLE ACCOUNTADMIN;
SELECT SYSTEM$OPT_OUT_MALICIOUS_IP_PROTECTION_BY_CATEGORY('ANONYMOUS_VPN', 'JSMITH');
```

The following example shows Account Usage LOGIN_HISTORY view output in the `login_details` column. The IP address for this result was opted
out of blocking the MALICIOUS_BEHAVIOR category by running the SYSTEM$OPT_OUT_MALICIOUS_IP_PROTECTION_BY_CATEGORY function:

Example — unblocked IP categorized as “LOW” risk:

```json
{
  "malicious_ip_protection_info":"{\"result\":\"OPTED_OUT\",\"riskClassification\":\"LOW\",\"categories\":[\"MALICIOUS_BEHAVIOR\"]}"
}
```
