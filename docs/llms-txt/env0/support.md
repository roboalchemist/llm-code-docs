# Source: https://docs.envzero.com/guides/community-and-resources/support-and-help/support.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Support

env zero is committed to enabling our customer's use of the platform. We offer structured support depending on your subscriptions and unique needs. Please refer to your contract to understand which level applies.

## Public Documentation

Our documentation contains the solution to many problems that may arise while using env zero. Before opening a support request, please consult our public documentation as this will be the fastest resolution.

## How to Contact Support

Depending on your plan and support package, you can reach out via:

* Our shared Slack or MS Teams channel (for Cloud Pilot customers)
* Email at [support@env0.com](mailto:support@env0.com) (the preferred channel for Basic customers).
* For billing, purchase, or subscription questions - contact [ar@env0.com](mailto:ar@env0.com) (or your Customer Success Manager).

## Service Level Agreement (SLA)

The SLA times listed below are the timeframes in which you can expect the first response. env zero will make a reasonable effort to adhere to the response times provided below and resolve any issues to your satisfaction as quickly as possible. However, the SLA times are not to be considered an expected time to resolution.

| **Severity**         | **Silver** (free, included with your license) | **Gold** | **Platinum** |
| :------------------- | :-------------------------------------------- | :------- | :----------- |
| **Critical**         | 4 hours                                       | 2 hours  | 1 hour       |
| **Serious**          | Best Effort                                   | 8 hours  | 4 hours      |
| **Minor**            | Best Effort                                   | 24 hours | 24 hours     |
| **General Guidance** | Best Effort                                   | One week | 72 hours     |

*All first response timelines can be expected from 4 am - 8 pm ET Monday-Friday, with the exception of federal U.S. Holidays.*

### Severity Definitions

**Severity Level 1 ("Critical")**. A Severity Level 1 problem means any of the following:

* A complete outage.
* Loss of data with no ability to retrieve it back

**Severity Level 2 ("Serious")**. A Severity Level 2 problem means any of the following:

* A significant degradation of the service occurs
* Results are materially different from those described in the product definition.

**Severity Level 3 ("Minor")**. A Severity Level 3 problem means any of the following:

* A minor degradation of the service delivery occurs.
* Recent modifications to the system cause services to operate in a way that is materially different from those described in the product definition for non essential features.

**Severity Level 4 ("General Guidance")**. A Severity Level 4 problem means any of the following:

* Implementation or production use continues and work is not impeded.
* E.g. information, an enhancement, or documentation clarification is requested.

## What's In-Scope & What's Not

We support env zero features and common integrations - including assisting with deployments, diagnosing failed runs, and helping with supported integrations (e.g., cloud accounts, VCS providers, IaC tooling). In contrast, we don't provide full hands-on support for third-party technologies, custom infrastructure design, or deep architecture consulting.

| Area                                                                            | In-Scope                                                                                                                                      | Out-of-Scope                                                                                                |
| :------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| env zero core features & workflows                                              | Troubleshooting run failures, debugging stack/environment configs, permissions and integration setups, basic VCS/cloud-account linkage issues | Redesigning your entire IaC layout or repository structure                                                  |
| Cloud providers / Accounts / Permissions                                        | Helping verify that credentials and permissions are configured correctly for env zero                                                         | Designing cloud architecture, enforcing best practices, or managing non-env zero resources                  |
| IaC tools (Terraform, Pulumi, etc.) within env zero context                     | Assisting with runs execution, environment variables, module invocation failures                                                              | Teaching IaC fundamentals, writing custom Terraform modules from scratch, or providing general IaC training |
| VCS / Repository integrations                                                   | Diagnosing why changes are not triggering runs; ensuring integration is set up per spec                                                       | Reviewing or restructuring codebase, code review, or optimizing repo layout for IaC                         |
| Supported integrations with third-party tooling (e.g. notifications, CLI usage) | Helping with env-zero integration steps, configuration errors, or env zero-related failures                                                   | Providing support for the third-party tool itself beyond its interaction with env zero                      |

*Support beyond these boundaries may, in rare cases, be offered at the discretion of the support engineer - but should be considered a courtesy, not a guarantee.*

## Uptime and Availability

We will use commercially reasonable efforts to:

* Maintain uptime of the SaaS services provided by env zero 99.9% of the time measured in a given calendar month.
* Give 24 hour prior notice for all scheduled maintenance of the SaaS services provided by env zero.

You can check the current SaaS services' availability status at our [status page](https://status.env0.com/).

Please be aware that the availability of the services provided by env zero might be affected by factors beyond our control, such as third party failures, interruptions or outages (which are not taken into account to calculate the uptime).

Built with [Mintlify](https://mintlify.com).
