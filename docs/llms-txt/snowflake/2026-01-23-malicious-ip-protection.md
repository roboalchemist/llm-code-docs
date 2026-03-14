# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-01-23-malicious-ip-protection.md

# Jan 23, 2026: Malicious IP Protection updates

These updates enhance Malicious IP Protection to provide visibility of blocked login attempts and the option to disable blocking for IP
addresses that are categorized as low-risk.

View blocked login attempts:
:   You can now use the new LOGIN_DETAILS column in the Account Usage [LOGIN_HISTORY view](../../../sql-reference/account-usage/login_history.md) to see details of
    network access attempts that the Malicious IP Protection service has blocked.

Manage opt-out for low-risk categories:
:   If you determine that blocking certain low-risk categories blocks legitimate users, you can opt out of blocking for specific
    categories by using the new [SYSTEM$OPT_OUT_MALICIOUS_IP_PROTECTION_BY_CATEGORY](../../../sql-reference/functions/system_opt_out_malicious_ip_protection_by_category.md) function.

For more information, see [Malicious IP Protection](../../../user-guide/malicious-ip-protection.md).
