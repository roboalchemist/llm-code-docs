# Source: https://docs.gitguardian.com/self-hosting/troubleshoot/health-check.md

# Environment health

> Run health checks on your GitGuardian self-hosted installation to verify component connectivity and configuration.

The **Health Check** page provides an overview of all your GitGuardian self-hosted
instance. On this page, you can have access to the status of the services
used by GitGuardian. The page also provides you with information on VCS integration
connected to GitGuardian and the Readiness REST endpoint.

## GitGuardian Services

This section shows you the status of services used by your GitGuardian instance to
function. In case one of those services is somehow unreachable or broken, it will be
indicated as such.

![Health Check page](/img/self-hosting/troubleshoot/health_check_services.png)

## Readiness

The REST endpoint checks the readiness of your GitGuardian instance.
The URL of that endpoint is displayed on the Health Check page. The endpoint is
protected, you can use it only with an API key (refer to the [API authentication documentation](../../api-docs/authentication))

It is easy to use the endpoint, for instance using curl (`XXXX` should be
replaced with your API key):

```bash
curl -H "Authorization: Token XXXX" https://gitguardian.example.com/exposed/v1/readiness
```

Example of the reply:

```
{
    "db": "ok",
    "redis": "ok",
    "status": "ok"
}
```

## Integration Connectivity

Integration health checks ([VCS](../../internal-monitoring/integrate-sources/vcs-integrations/github),
[Messaging](../../internal-monitoring/integrate-sources/messaging-integrations/slack),
[Ticketing](../../internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud), ...) are accessible
through _Settings > Workspace > Integrations_, providing an overview of the **source integration status and any errors** encountered.
In the event of an integration failure, detailed information on resolving the issue will be displayed.
Additionally, there's an option to manually re-check the integration connection, along with timestamps
indicating the last execution and the most recent successful connection.

You can set up your account to receive email alerts when an integration fails. Find more information [here](../../platform/user-account/email-preferences).

The interval between periodic health checks can be customized using the `spread_periodic_range_minutes` preference in [the Health Checks section of the admin area preferences](../../self-hosting/management/application-management/preferences.md).

### Example of Failure

![Health Check Failure](/img/self-hosting/troubleshoot/health_check_vcs_failure.png)

### Example of Success

![Health Check Success](/img/self-hosting/troubleshoot/health_check_vcs_success.png)
