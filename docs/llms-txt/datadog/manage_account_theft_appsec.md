# Source: https://docs.datadoghq.com/security/application_security/guide/manage_account_theft_appsec.md

---
title: Managing Account Theft with AAP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > App and API Protection
  Guides > Managing Account Theft with AAP
---

# Managing Account Theft with AAP

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Users are trusted entities in your systems with access to sensitive information and the ability to perform sensitive actions. Malicious actors have identified users as an opportunity to target websites and steal valuable data and resources.

Datadog App and API Protection (AAP) provides [built-in](https://docs.datadoghq.com/security/account_takeover_protection/) detection and protection capabilities to help you manage this threat.

This guide describes how to use AAP to prepare for and respond to account takeover (ATO) campaigns. This guide is divided into three phases:

1. Collecting login information:
   - Enable and verify login activity collection in Datadog AAP using automatic or manual instrumentation methods.
   - Use remote configuration options if you cannot modify your service code.
   - Troubleshoot missing or incorrect data.
1. Preparing for account takeover campaigns:
   - Prepare for ATO campaigns detected by AAP.
   - Configure notifications for attack alerts.
   - Validate proper data propagation for accurate attacker identification.
   - Set up automatic IP blocking for immediate mitigation.
   - Learn about the importance of temporary blocking due to dynamic attacker IPs.
1. Reacting to account takeover campaigns:
   - Learn how to react to ATO campaigns, including attacker strategies, triage, response, investigation, monitoring, and cleanup.

## Phase 1: Collecting login information{% #phase-1-collecting-login-information %}

To detect malicious patterns, AAP requires visibility into your users' login activity. This phase describes how to enable and validate this visibility.

### Step 1.1: Ensure AAP is enabled on your identity service{% #step-11-ensure-aap-is-enabled-on-your-identity-service %}

This step describes how to set up your service to use AAP.

{% alert level="info" %}
If your service is already using AAP, you can go to Step 1.3: Validating whether login information is automatically collected.
{% /alert %}

1. Go to [**Software Catalog**](https://app.datadoghq.com/services?query=service%3Auser-auth&env=%2A&fromUser=false&hostGroup=%2A&lens=Security&sort=-fave%2C-team&start=1735636008863&end=1735639608863), click the **Security** lens, and search for your login service name.

   {% image
      source="https://datadog-docs.imgix.net/images/security/ato/guide_service_catalog.c466056c94bd01c0a28e4e5db4576a47.png?auto=format"
      alt="Software Catalog with a service managing authentication" /%}

1. Click on the service to open its details. If the **Threat management** pill is green, AAP is enabled and you may move to Step 1.3: Validating whether login information is automatically collected.

   {% image
      source="https://datadog-docs.imgix.net/images/security/ato/guide_service_catalog_enabled.718730dac7afddc5beed3d1759358656.png?auto=format"
      alt="Software Catalog with a service side-panel expended, showing Threat Management enabled" /%}

If AAP isn't enabled, the panel displays the **Discover AAP** button.

   {% image
      source="https://datadog-docs.imgix.net/images/security/ato/guide_service_catalog_disabled.ad378de746edda0953efa25651f1aa87.png?auto=format"
      alt="Software Catalog with a service side-panel expended, showing Threat Management isn't enabled and showing a link to learn more" /%}

To set up AAP, move to Step 1.2: Enabling AAP on login service.

### Step 1.2: Enabling AAP on your login service{% #step-12-enabling-aap-on-your-login-service %}

To enable AAP on your login service, ensure you meet the following requirements:

- Similarly to Datadog APM, AAP requires a library integration in your services and a running Datadog Agent.
- AAP generally benefits from using the newest library possible; however, minimum supported versions are documented in [Compatibility Requirements](https://docs.datadoghq.com/security/application_security/setup/compatibility/).
- At a minimum, **Threat Detection** must be enabled. Ideally, **Automatic user activity event tracking** should be enabled as well.

To enable AAP using a new deployment, use the `APPSEC_ENABLED` environment variable/library configuration or [Remote Configuration](https://docs.datadoghq.com/tracing/guide/remote_config/). You can use either method, but Remote Configuration can be set up using the Datadog UI.

**To enable AAP using Remote Configuration**, and without having to restart your services, do the following:

1. Go to [AAP onboarding](https://app.datadoghq.com/security/appsec/onboarding).
1. Click **Enable App & API Protection**.
1. In **Activate on your APM services**, click **Select Services.**
1. Select your service(s), and then click **Next** and proceed with the setup instructions.

When you see traces from your service in [AAP Traces](https://app.datadoghq.com/security/appsec/traces?query=&agg_m=count&agg_m_source=base&agg_t=count&fromUser=false&track=appsecspan&start=1735036043639&end=1735640843639&paused=false), move to Step 1.3: Validating login information is automatically collected.

For more detailed instructions on using a new deployment, see [Enabling AAP Threat Detection using Datadog Tracing Libraries](https://docs.datadoghq.com/security/application_security/setup/threat_detection/).

### Step 1.3: Validating login information is automatically collected{% #step-13-validating-login-information-is-automatically-collected %}

After you have enabled AAP, you can validate that login information is collected by Datadog.

**Note:** After AAP is enabled on a service, wait a few minutes for users to log into the service or log into the service yourself.

To validate login information is collected, do the following:

1. Go to [Traces](https://app.datadoghq.com/security/appsec/traces?query=%40appsec.security_activity%3Abusiness_logic.users.login.%2A&agg_m=count&agg_m_source=base&agg_t=count&fromUser=false&track=appsecspan&start=1735036164646&end=1735640964646&paused=false) in AAP.
1. Look for traces tagged with login activity from your login service. For example, in **Search for**, you might have `@appsec.security_activity:business_logic.users.login.*`.
1. Check if all your login services are reporting login activity. You can see this in the **Service** facet.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_trace_explorer.69d1b04a4cb37b5803d9167aca8b3551.png?auto=format"
   alt="AAP Trace explorer showing a steady state of login failures and successes, with a few spikes" /%}

**If you don't see login activity from a service**, go to Step 1.5: Manually instrumenting your services.

### Step 1.4: Validating login metadata is automatically collected{% #step-14-validating-login-metadata-is-automatically-collected %}

To validate that login metadata is collected, do the following:

1. Go to [Traces](https://app.datadoghq.com/security/appsec/traces?query=%40appsec.security_activity%3Abusiness_logic.users.login.%2A&agg_m=count&agg_m_source=base&agg_t=count&fromUser=false&track=appsecspan&start=1735036164646&end=1735640964646&paused=false) in AAP.
1. Look for traces tagged with successful and failed login activity from your login service. You can update the search query in **Search for** to filter `business_logic.users.login.success` or `business_logic.users.login.failure`.
1. Open a trace.
1. On the **Security** tab, review the **Business Logic Event**.
1. Check if the event is for a false user.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_trace_login_fail.87a455507a09a18d7da6787a260d8c23.png?auto=format"
   alt="AAP login trace showing a login failure event and complete metadata" /%}

Review a few traces, both login successes and login failures. For login failures, look for traces with `usr.exists` as `true` (failed login attempt by an existing user) and `false`.

The checks must be done whether or not the user exists.

In the event of a **false** user (`usr.exists:false`), look for the following issues:

- A single event: if the trace contains multiple login events, such as both successes and failures, this might be caused by incorrect auto-instrumentation. To change auto-instrumentation, go to Step 1.5: Manually instrumenting your services.
- Does the event contain the mandatory metadata? It might appear as a user attribution section in the case of a login success. The mandatory metadata is `usr.login` and `usr.exists` in the case of login failure, and `usr.login` and `usr.id` in the case of login success. If some metadata is missing, go to Step 1.5: Manually instrumenting your services.

**If the instrumentation is correct, go to Phase 2: Preparing for Account Takeover campaigns.**

### Step 1.5: Manually instrumenting your services{% #step-15-manually-instrumenting-your-services %}

AAP collects login information and metadata using an SDK embedded in the Datadog libraries. Instrumentation is performed by calling the SDK when a user login is successful/fails and by providing the SDK with the metadata of the login. The SDK attaches the login and the metadata to the trace and sends it to Datadog where it is retained.

{% alert level="info" %}
For an alternative to modifying the service's code, go to Step 1.6: Remote instrumentation of your services.
{% /alert %}

To manually instrument your services, do the following:

1. If auto-instrumentation is providing incorrect data (multiple events in a single trace), see [Disable auto-instrumentation](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info/?tab=set_user#disabling-user-activity-event-tracking).
1. For detailed instrumentation instructions for each language, go to [Adding business logic information (login success, login failure, any business logic) to traces](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info/?tab=set_user#adding-business-logic-information-login-success-login-failure-any-business-logic-to-traces). Make sure to add the following metadata:
   - `usr.login`: **Mandatory for login success and failure**. This field contains the *name* used to log into the account. The name might be an email address, a phone number, a username, or something else. The purpose of this field is to identify targeted accounts even if they don't exist in your systems because a user might be able to change those accounts. Also, this field provides information on the location of the database used by the attacker. This value shouldn't be confused with `usr.id`.
   - `usr.exists`: **Mandatory for login failures**. This field is required for some default detections. The field helps to lower the priority of attempts targeted at accounts that don't exist in your systems.
   - `usr.exists`: **Mandatory for login failures**. This field is required for some default detections. The field helps to lower the priority of attempts targeted at accounts that don't exist in your systems.

**After deploying the code, validate the instrumentation is correct by following the steps in** Step 1.4: Validating login metadata is automatically collected.

### Step 1.6: Remote instrumentation of your services{% #step-16-remote-instrumentation-of-your-services %}

AAP can use custom In-App WAF rules to flag login attempts and extract the metadata from the request needed by detection rules.

This approach requires that [Remote Configuration](https://docs.datadoghq.com/tracing/guide/remote_config/) is enabled and working. Verify Remote Configuration is running for this service in [Remote Configuration](https://app.datadoghq.com/organization-settings/remote-config?resource_type=agents).

To use custom In-App WAF rules, do the following:

1. Open the [In-App WAF custom rule creation form](https://app.datadoghq.com/security/appsec/in-app-waf?column=services-count&config_by=custom-rules&ruleId=newRule).

1. Name your rule and select the **Business Logic** category.

1. Set the rule type as `users.login.failure` for login failures and `users.login.success` for login successes.

   {% image
      source="https://datadog-docs.imgix.net/images/security/ato/guide_waf_instrumentation.7d26c0d6f56afc1c8d14a42fd96c87fb.png?auto=format"
      alt="Custom WAF rule creation form populated with a new login instrumentation rule" /%}



1. Select your service and write the rule to match the login attempts. Typically, you match the method (`POST`), the URI with a regex (`^/login`), and the status code (403 for failures, 302 or 200 for success).

1. Collect the tags required by detection rules. The most important tag is `usr.login`. Assuming the login was provided in the request, you can add a condition and set `store value as tag` as the operator.

   {% image
      source="https://datadog-docs.imgix.net/images/security/ato/guide_waf_instrumentation_operator.9c4b213b911de839f86fa8ff32c09461.png?auto=format"
      alt="Operator dropdown in the custom WAF rule creation form, with store value as tag highlighted" /%}



1. Select a specific user parameter as an input, either in the body or the query.

1. Set the `Tag` field to the name of the tag where you want to save the value captured using `usr.login`.

   {% image
      source="https://datadog-docs.imgix.net/images/security/ato/guide_waf_instrumentation_tagged.bc6be5493351d32aa6ad60e15a72e6ad.png?auto=format"
      alt="Custom WAF rule creation form, with a complete condition selecting a parameter named login and storing it in a tag called usr.login" /%}



1. Click **Save**. The rule is automatically sent to every instance of the service and then begins capturing login failures.

**To validate that the instrumentation is correct**, see Step 1.4: Validating login metadata is automatically collected.

For more details, see [Tracking business logic information without modifying the code](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info/?tab=set_user#tracking-business-logic-information-without-modifying-the-code).

## Phase 2: Preparing for ATO campaigns{% #phase-2-preparing-for-ato-campaigns %}

After setting up instrumentation for your services, AAP monitors for attack campaigns. You can review the traffic in the [Attacks overview](https://app.datadoghq.com/security/appsec/threat) **Business logic** section.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_overview_card.15742ee2d28ee633cad28103f4adb02e.png?auto=format"
   alt="Overview of the login activity and of ATO-related signals" /%}

AAP detects [multiple attacker strategies](https://docs.datadoghq.com/security/account_takeover_protection/#attacker-strategies). Upon detecting an attack with a high level of confidence, the [built-in detection rules](https://app.datadoghq.com/security/appsec/detection-rules?query=type%3Aapplication_security%20tag%3A%22category%3Aaccount_takeover%22&deprecated=hide&groupBy=none&sort=date&viz=rules) generate a signal.

The severity of the signal is set based on the urgency of the threat: from **Low** in case of unsuccessful attacks to **Critical** in case of successful account compromises.

The actions covered in the next sections help you to identify and leverage detections faster.

### Step 2.1: Configuring notifications{% #step-21-configuring-notifications %}

[Notifications](https://docs.datadoghq.com/security/notifications/) provide a warning on your preferred channel when a signal is triggered. To create a notification rule, do the following:

1. Open [Create a new rule](https://app.datadoghq.com/security/configuration/notification-rules/new?notificationData=).
1. Enter a name for the rule.
1. Select **Signal** and remove all entries except **App and API Protection**.
1. Restrict the rule to `category:account_takeover`, and expand the severities to include `Medium`.
1. Add notification recipients (Slack, Teams, PagerDuty). To learn more, see [Notification channels](https://docs.datadoghq.com/security/notifications/#notification-channels).
1. Test, and then save the rule.
   {% image
      source="https://datadog-docs.imgix.net/images/security/ato/guide_notification_config.73cd7bca6588271e035a272396fff062.png?auto=format"
      alt="Notification creation form populated to notify for the most relevant ATO signals" /%}
The notification is sent the next time a signal is generated.

### Step 2.2: Validate proper data propagation{% #step-22-validate-proper-data-propagation %}

In microservice environments, services are generally reached by internal hosts running other services. This internal environment makes it challenging to identify the unique traits of the original attacker's request, such as IP, user agent, fingerprint, etc.

[AAP Traces](https://app.datadoghq.com/security/appsec/traces?query=%40appsec.security_activity%3Abusiness_logic.users.login.%2A&agg_m=count&agg_m_source=base&agg_t=count&fromUser=false&track=appsecspan&start=1735222832468&end=1735827632468&paused=false) can help you validate that the login event is properly tagged with the source IPs, user agent, etc. To validate, review login traces in [Traces](https://app.datadoghq.com/security/appsec/traces?query=%40appsec.security_activity%3Abusiness_logic.users.login.%2A&agg_m=count&agg_m_source=base&agg_t=count&fromUser=false&track=appsecspan&start=1735222832468&end=1735827632468&paused=false) and check for the following:

- Source IPs (`@http.client_ip`) are varied and public IPs.
  - **Problem:** If login attempts are coming from a few IPs only, this might be a proxy that you can't block without risking availability.
  - **Solution:** Forward the client IP of the initial request through a HTTP header, such as `X-Forwarded-For`. You can use a custom header for [better security](https://securitylabs.datadoghq.com/articles/challenges-with-ip-spoofing-in-cloud-environments/#what-should-you-do) and configure the tracer to read it using the `DD_TRACE_CLIENT_IP_HEADER` environment variable.
- The user agent (`@http.user_agent`) is consistent with the expected traffic (web browser, mobile app, etc.)
  - **Problem:** The user agent could be replaced by the user agent in the calling microservice network library.
  - **Solution:** Use the client user agent when calling subsequent services.
- Multiple headers are populated. You can see this in a trace's **See more details** in the **Request** block.
  - **Problem:** Normal request headers (for example, `accept-encoding`) aren't forwarded to the instrumented service. This impairs the generation of fingerprints (`@appsec.fingerprint.*`) and degrades the signal's ability to isolate an attacker's activity.
  - **Solution:** Forward those headers when calling a subsequent microservice.

### Step 2.3: Configure automatic blocking{% #step-23-configure-automatic-blocking %}

{% alert level="info" %}
Before you begin: Verify that the IP addresses are properly configured, as described in Step 2.2: Validate proper data propagation.
{% /alert %}

AAP automatic blocking can be used to block attacks at any time of the day. Automatic blocking can help block attacks before your team members are online, providing security during off hours. Within an ATO, automatic blocking can help mitigate the load issues caused by the increase in failed login attempts or prevent the attacker from using compromised accounts.

You can configure automatic blocking to block IPs identified as part of an attack. This is only a partial remediation because attackers can change IPs; however, it can give you more time to implement comprehensive remediation.

To configure automatic blocking, do the following:

1. Go to **AAP** > **Policies** > [Detection Rules](https://app.datadoghq.com/security/appsec/detection-rules?query=type%3Aapplication_security%20tag%3A%22category%3Aaccount_takeover%22&deprecated=hide&groupBy=none&sort=date&viz=rules).
1. In **Search**, enter `tag:"category:account_takeover"`.
1. Open the rules where you want to turn on blocking. Datadog recommends turning IP blocking on for **High** or **Critical** severity.
1. In the rule, in **Define Conditions**, in **Security Responses**, enable **IP automated blocking**. You may also enable **User automated blocking**.You can control the blocking behavior per condition. Each rule can have multiple conditions based on your confidence and the attack success.

**Datadog does not recommend permanent blocking of IP addresses**. Attackers are unlikely to reuse IPs and permanent blocking could result in blocking users. Moreover, AAP has a limit of how many IPs it can block (`~10000`), and this could fill this list with unnecessary IPs.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_blocking_config.660ab26c0047ddc9c5b9b9f6386d53a1.png?auto=format"
   alt="Condition section of the detection rule page where blocking can be configured" /%}

## Phase 3: Reacting to ATO campaigns{% #phase-3-reacting-to-ato-campaigns %}

This section describes common account takeover hacker behavior and how to triage, investigate, and monitor detections.

### How attackers run their campaigns{% #how-attackers-run-their-campaigns %}

Eventually, your systems come under attack. The wave of malicious login attempts can often eclipse the volume of normal login activity the service is expecting. The load might increase causing availability problems and the attacker could at any time successfully log into an account.

The actions the attackers take depend on their strategy and the configurations of your systems. Some attackers might decide to immediately abuse their access to extract value before you've had time to freeze their compromised accounts. Others might keep the accounts dormant until a later time.

Many strategies are available, but it's important to understand that the value chain of attacks is often carefully divided:

1. The actor who initiates the attack often buys a database of credentials from a vendor (likely acquired by the compromise of another service).
1. The actor procures a script designed to automate login attempts while evading detection (randomizing headers, trying to look as similar to normal traffic as possible).
1. The actor buys access to a botnet, letting them leverage many different IPs to run their attack. There are extreme cases where large campaigns with 500k+ attempts were so distributed that Datadog saw an average of 1.01 requests per IP and a single attempt per account.
1. When valid credentials are discovered, they might be sold downstream to another actor to leverage them to some end such as financial theft, spam, abuse, etc.

When an attack begins against your systems, the system generates signals labeled **Credential Stuffing**, **Distributed Credential Stuffing**, or **Bruteforce**, depending on the attacker's strategy.

### Step 3.1: Triage{% #step-31-triage %}

The first step is to confirm that the detection is correct. Certain behaviors, such as a security scan on a login endpoint or a lot of token rotation, might appear to the detection as an attack. The analysis depends on the signal, and the following examples provide general guidance that should be customized for your situation.

{% tab title="Bruteforce" %}
The signal is looking for an attempt to steal a user account by trying many different passwords for this account. Generally, a small number of accounts are targeted by these campaigns.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_signal_bruteforce.dd7bb9b9016ff5a853aefa7fb0d583a7.png?auto=format"
   alt="Signal side-panel showing a bruteforce signal with a compromised user" /%}

Review the accounts flagged as compromised. Click on a user to open a summary of recent activity.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_user_menu.cfa26004a84d61643131efbae14bf139.png?auto=format"
   alt="Menu shown when hovering over a user pill. A button allowing to open the user side panel is highlighted in the top right" /%}

Questions for triage:

- Has there been a sharp increase of activity?
- Is it the first time those IPs are attempting logins?
- Are they flagged by threat intelligence?

If the answer to those questions is yes, the signal is likely legitimate.

You can adapt your response based on the sensitivity of the account. For example, a free account with limited access versus an admin account.
{% /tab %}

{% tab title="Credential Stuffing" %}
This signal is looking for a large number of accounts with failed logins coming from a small number of IPs. This is often caused by unsophisticated attackers.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_signal_credential_stuffing.b858a3d7c345ccbc54f408eab7167829.png?auto=format"
   alt="Signal side-panel showing a credential stuffing signal with a compromised user" /%}

Review the accounts flagged as targeted for similarities and to establish those users' sensitivity.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_user_table.019e095eada39388321be07ea13f9484.png?auto=format"
   alt="Table showing the users targeted by the attack. One user is shown in a pill because we have a side-panel with more activity on them" /%}

If they share attributes, such as all coming from one institution, check whether the IP might be a proxy for this institution by reviewing its past activity by hovering over it and opening the side panel.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_ip_menu.aee77108f7c48b322b578602c04adbba.png?auto=format"
   alt="Menu shown when hovering over a user pill. A button allowing to open the user side panel is highlighted in the top right" /%}

Questions for triage:

- Has there been a sharp increase of activity?
- Are the accounts uncorrelated?
- Are IPs flagged by threat intelligence?
- Are there many more login failures than successes ?

If the answer to those questions is yes, the signal is likely legitimate.You can adapt your response based on the scale of the attack and whether accounts are being compromised.
{% /tab %}

{% tab title="Distributed Credential Stuffing" %}
This signal is looking for a large increase in the overall number of login failures on a service. This is caused by sophisticated attackers leveraging a botnet.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_signal_distributed_credential_stuffing.cf458a919e74938a36dfdf9eeb14325f.png?auto=format"
   alt="Signal side-panel showing a distributed stuffing signal" /%}

Datadog tries to identify common attributes between the login failures in your service. This can surface defects in the attacker script that can be used to isolate the malicious activity. When found, a section called **Attacker Attributes** is shown. If present, review whether this is legitimate activity by selecting the cluster and clicking on **Explore clusters**.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_cluster_table.9e0fb938af166e3f5fccf97de0a96a03.png?auto=format"
   alt="Table showing the clusters of user attributes detected during the attack. Rows can be selected to narrow the investigation on the activity matching those attributes" /%}

If accurate, the activity of the cluster should closely match the increase in login failures while also being low/nonexistent before.If no cluster is available, click **Investigate in full screen** and review the targeted users/IPs for outliers.

If the list is truncated, click **View in AAP Traces Explorer** and run the investigation with the Traces explorer. For additional tools, see Step 3.3: Investigation.
{% /tab %}

If the conclusion of the triage is that the signal is a false positive, you can flag it as a false positive and close it.

If the false positive was caused by a unique setting in your service, you can add suppression filters to silence false positives.

**If the signal is legitimate**, move to step Step 3.2: Preliminary response.

### Step 3.2: Disrupting the attacker as a preliminary response{% #step-32-disrupting-the-attacker-as-a-preliminary-response %}

If the attack is ongoing, you might want to disrupt the attacker as you investigate further. Disrupting the attacker slows down the attack and reduce the number of compromised accounts.

{% alert level="info" %}
This is a common step, although you might want to skip this step in the following circumstances:
- The accounts have little immediate value. You can block these post-compromise without causing harm.
- You want to maintain maximum visibility into the attack by avoiding any action that alerts the attacker to the investigation and causes them to change tactics.

{% /alert %}

Enforcing this preliminary response requires that [Remote Configuration](https://docs.datadoghq.com/tracing/guide/remote_config/) is enabled for your services.

If you want to initiate a partial response, do the following:

{% tab title="Bruteforce or Credential Stuffing" %}
The attackers are likely using a small number of IPs. To block them, open the signal and use Next Steps. You can set the duration of blocking.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_next_steps.f4fb549a21437247554586aa0cee8dab.png?auto=format"
   alt="Menu shown quick responses to the signal, from triaging the signal, to responding to the signal by blocking IPs or compromised users, to enabling automatic blocking" /%}

Datadog recommends **12h**, which is enough for the attack to stop and avoid blocking legitimate users when, after the attack, those IPs get recycled to legitimate users. Datadog does not recommend permanent blocking.You can also block compromised users, although a better approach would be to extract them and reset their credentials using your own systems.

Finally, you can enable automated IP blocking from the Next Step section so that new IPs are automatically blocked while you're running your investigation.
{% /tab %}

{% tab title="Distributed Credential Stuffing" %}
These attacks often use a large number of disposable IPs. Due to Datadog's latency, it's impractical to block login attempts by blocking the IP before the attacker drops it from their pool.

Instead, block traits of the request that are unique to the malicious attempt (a user agent, a specific header, a fingerprint, etc.).

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_cluster_table.9e0fb938af166e3f5fccf97de0a96a03.png?auto=format"
   alt="Table showing the clusters of user attributes detected during the attack. Rows can be selected to narrow the investigation on the activity matching those attributes" /%}

In a **Distributed Credential Stuffing campaign** signal, Datadog automatically identifies clear traits and presents them as **Attacker Attributes**.

Before blocking, Datadog recommends that you review the activity from the cluster to confirm that the activity is indeed malicious.

The questions you're trying to answer are:

- Is the traffic malicious? Did this traffic exist before the beginning of the attack?
- Can a meaningful volume of legitimate traffic be caught?
- Can blocking based on this cluster be effective?

To do so, select your cluster and click on **Explore clusters**.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_cluster_table_select.6ccb3ab6dfb2f531cb17ee37fbfc3dfe.png?auto=format"
   alt="Table showing the clusters of user attributes detected during the attack. A row a selected and the button Explore clusters is in focus" /%}

The **Investigate** explorer appears and provides cluster traffic indicators: a large share of the traffic from the attack and a high proportion of IPs flagged by Threat Intelligence.

Those are two important indicators:

- Threat Intel %

- Traffic Distribution

  {% image
     source="https://datadog-docs.imgix.net/images/security/ato/guide_cluster_explorer.853b57b60ddf35d8c34426c3dc860cb4.png?auto=format"
     alt="Cluster explorer showing the cluster we selected before" /%}

Click an indicator to see further information about the cluster traffic.

In **Cluster Activity**, there is a visualization of the volume of the overall APM traffic matching this cluster. While comparing it to the AAP data, beware the scale, since APM data may be sampled while AAP's isn't.

In the following example, a lot of traffic comes from before the attack. This means a legitimate activity matches this cluster in normal traffic and it would get blocked if you were to take action. You don't need to escalate or click **Block All Attacking IPs** in the signal.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_cluster_explorer_fp.ae8bd5820414eeb4b97d68926512ede7.png?auto=format"
   alt="Cluster activity showing a steady rate of traffic matching those attributes, a strong hint that most of this traffic is legitimate and that the cluster can't be used for blocking" /%}

In a different example, the activity from the cluster started with the attack. This means there shouldn't be collateral damage and you can proceed to block.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_cluster_explorer_tp.0a596ab549897c5fa3285467511959fd.png?auto=format"
   alt="Graph showing on a logarithmic scale very little traffic outside of the attacks" /%}

After confirming that the traits match the attackers, you can push an In-App WAF rule to block requests matching those traits. This is supported for user agent-based traits only.

To create the rule, do the following:

1. Go to **AAP** > **Policies** > **In-App WAF** > [Custom Rules][28]].

1. Click **Create New Rule** and complete the configuration.

1. Follow the steps in **Define your custom rule**.

1. In **Select the services you want this rule to apply to**, select your login service, or the services where you want to block requests. You can also target blocking to the login route.

   {% image
      source="https://datadog-docs.imgix.net/images/security/ato/guide_waf_blocking.bcd8f7e5061b17733a653b1ef9501482.png?auto=format"
      alt="Screenshot of the WAF rule creation modal selecting a specific route on a specific service" /%}

1. In **If incoming requests match these conditions**, configure the conditions of the rule.

   1. If you want to block a specific user agent, paste it in **Values**. In **Operator**, you can use **matches value in list**, or, if you want more flexibility, you can also use **Matches RegEx**.

   {% image
      source="https://datadog-docs.imgix.net/images/security/ato/guide_waf_blocking_ua.c1e8259d47e13e64464e059fd105baa3.png?auto=format"
      alt="A screenshot of a user agent getting blocked" /%}

1. Use the **Preview matching traces** section as a final review of the rule's impact. If no unexpected traces are shown, select a blocking mode and save the rule.

   {% image
      source="https://datadog-docs.imgix.net/images/security/ato/guide_waf_blocking_traces.ca1d2299db25f40c7e787d98f30e444b.png?auto=format"
      alt="Table showing traces matching your rules" /%}

Multiple blocking actions are available. Depending on the sophistication of the attackers, you might want a more stealthy answer so that they don't immediately realize they were blocked.
{% /tab %}

### Step 3.3: Investigation{% #step-33-investigation %}

When you have disrupted the attacker as a preliminary response, you can identify the following:

- Accounts compromised by the attackers so you can reset their credentials.
- Hints about the source of the targeted accounts, which you can use for proactive password resets or higher scrutiny.
- Data on the attacker infrastructure, which you can use to catch future attempts or other malicious activity (credit card stuffing, abuse, etc.).

The first step is to isolate the attacker activity from the overall traffic of the application.

#### Isolate attacker activity{% #isolate-attacker-activity %}

While isolating attacker activity, ensure that your current filters are exhaustive through two tests:

1. Go to [Traces](https://app.datadoghq.com/security/appsec/traces), and then *exclude* traces based on the filters you identify. The goal is to have the remaining traffic volume similar to your normal traffic volume. If you're still seeing a spike of logins during the attack, it means further filters are necessary to comprehensively isolate the attack.
1. Look at the traffic matching your filters over an expanded time frame (for example, if the attack lasted an hour, use one day). Any traffic matched before or after the attack is likely be a false positive.

Next, start by isolating the attack's activity.

{% tab title="Bruteforce" %}
Extract the list of targeted users by going to [Signals](https://app.datadoghq.com/security?query=%40workflow.rule.type%3A%22Application%20Security%22%20category%3Aaccount_takeover&product=appsec).

You can query the traces for the targeted users by clicking on the **login attempts** link in **Security Traces**.

If you want direct access to the targeted users, you can extract the list from the signal side panel.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_bruteforce_users.6df82a10dce21b9a7b62954e7e4c0d8d.png?auto=format"
   alt="Table showing attacked users" /%}

From this list of users, you can craft a [Traces](https://app.datadoghq.com/security/appsec/traces) query to review all the activity from targeted users. Follow this template:

`@appsec.security_activity:business_logic.users.login.* @appsec.events_data.usr.login:(<users>)`

Successful logins should be considered suspicious.
{% /tab %}

{% tab title="Credential Stuffing" %}
This signal flagged a lot of activity coming from a few IPs and is closely related to its distributed variant. You might need to use the distributed credential stuffing method if parts of the attack were missed by the signal.

You can query the traces matched by the attacking IPs by clicking on the **login attempts** link in **Security Traces**.

If you want direct access to the attacking IPs, you may extract the list from the signal side panel.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_credential_stuffing_ip.41a5a45c1b0117b099a4ff54fc1c1006.png?auto=format"
   alt="Table showing attacking IPs" /%}

From the list of IPs, you can craft a [Traces](https://app.datadoghq.com/security/appsec/traces) query to review all the activity from suspected IPs. Follow this template:

`@appsec.security_activity:business_logic.users.login.* @http.client_ip:(<IPs>)`

Successful logins should be considered suspicious.
{% /tab %}

{% tab title="Distributed Credential Stuffing" %}
This signal flagged a large increase in login failures in one service. If the attack is large enough, this signal might also trigger either the Bruteforce or Credential Stuffing signals. The signal is also able to detect diffuse attacks more comprehensively.

In the diffuse attacks case, attacker attributes are available in the signal.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_signal_distributed_credential_stuffing.cf458a919e74938a36dfdf9eeb14325f.png?auto=format"
   alt="Screenshot of a distributed credential stuffing signal" /%}

1. After opening the signal in the side panel, click **Investigate in full screen**.
1. In **Attacker Attributes**, select the cluster and click on **Filter this signal by selection**. Next, in **Traces**, click **View in AAP Traces Explorer**.

This gets you to the trace explorer with filters set to the flagged attributes. You can start the investigation with the current query, but you should expand it to also match login successes on top of the failures. You can do that by replacing `@appsec.security_activity:business_logic.users.login.failure` with `@appsec.security_activity:business_logic.users.login.*`. Review the exhaustiveness and accuracy of the filter using the technique described above.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_distributed_credential_stuffing_traces.59ec9c07c3a55002831da7fca04a34e9.png?auto=format"
   alt="Traces explorer filtered by the cluster attributes" /%}

In the case those attributes are inaccurate or incomplete, you may try to identify further traits to isolate the attacker activity. Going back to the full page signal and scrolling down to the **Traces** section, you'll find an **Analysis** button. This opens a view where the traffic from the attack is sliced by a large variety of attributes.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_investigate_overview.732e4e9aca88647e3209e294ce89709c.png?auto=format"
   alt="Analysis side panel opened with an attack and some suggested attributes in a table" /%}

The most common attributes are presented at the top of a table, but you can visualize their impact by scrolling down. Each row shows the share of traffic that matches this attribute and how closely this traffic matches the "shape" of the increase in trafic. Your goal is to identify the attributes that together isolate this increase in activity while excluding the steady-state traffic. Be mindful of the scale of the graphs, since not all traces may be tagged with every attribute (for instance, Threat Intelligence). Moreover, take note that some fields can't be used for blocking (Threat Intelligence, ASNs & IP geo).

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_investigate_correlation.7ed6bdba1a69953bcf57d8732b71cf0e.png?auto=format"
   alt="Some timeseries from the Analysis tab demonstrating sometimes low correlation, and sometimes high correlation" /%}

Upon identifying the attributes, select them from the list and double check their exhaustiveness by toggling on and off the **Filtering enabled** button. Once you're satisfied, click on **View Traces** to dive further into the impacted users.
{% /tab %}

#### Review login successes and failures{% #review-login-successes-and-failures %}

Reviewing login successes and failures helps to identify the following:

- What the attackers are after so that you can block them.
- What the attackers are doing so that you can catch them, even if they change their scripts.
- How successful the attackers are so that you can take back the accounts they took control of and see how much time you have to react.

When attacker activity is isolated, review login successes and consider the following questions:

- Have any accounts been compromised?
- Are attackers doing something with their compromised accounts or are they leaving them dormant?
- Are the accounts then accessed by a different infrastructure?
- Is there any past activity from this infrastructure?

For the login failures, consider the following questions:

- Are attackers targeting a specific subset of users?
- How successful are they? The accuracy of the attacks should be in the 1/100-1/1000 range.
- Are they defeating captchas or multifactor authentication?

As your investigation progresses, you can go back and forth between this step and the next as you're ready to enforce a response based on your findings.

### Step 3.4: Response{% #step-34-response %}

Datadog's investigation capabilities are enriched by data from its backend, which isn't available to the library running the response. Because of that, not all fields are compatible with enforcing a response.

Motivated attackers try to circumvent your response as soon as they become aware of it. In anticipation of this approach, do the following:

1. Ensure you don't lose visibility on the attack.
1. Make blocking as hard as possible to *identify* by the attacker. For example, make the blocking response the same as your login failure. This can confuse attackers and lead them to believe their attack is still successful.
1. Make blocking as hard as possible to *circumvent* by the attacker. Use subtle traits, such as specific header values, instead of IPs.

You can either use Datadog's built-in blocking capabilities to deny any request that matches some criteria, or export the data automatically to one of your systems to perform a response (credentials reset, mimic login failures upon blocking, etc.).

### Datadog blocking{% #datadog-blocking %}

Users that are part of the traffic blocked by Datadog see a **You're blocked** page, or receive a custom status code, such as a redirection. Blocking can be applied through two mechanisms, each with different performance characteristics: the Denylist and custom WAF rules.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_blocked.ae1c16585031b77d8d128f9c9006041f.png?auto=format"
   alt="Page shown when user is blocked. Page say 'Sorry, you cannot access this page. Please contact the customer service team'" /%}

#### Denylist{% #denylist %}

The [Denylist](https://app.datadoghq.com/security/appsec/denylist) is an efficient way to block a large number of entries, but is limited to IPs and users. If your investigation uncovered a small set of IPs responsible for the attack (`<1000`), blocking these IPs is the best course of action.

The Denylist can be managed and automated using the Datadog platform by clicking **Automate Attacker Blocking** in the signal.

Use the **Automate Attacker Blocking** or **Block All Attacking IPs** signal options to block all attacking IPs for a few hours, a week, or permanently. Similarly, you can block compromised users. As a reminder, Datadog doesn't recommend blocking IPs permanently due to risks of blocking legitimate traffic after IPs get recycled into public pools.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_next_steps.f4fb549a21437247554586aa0cee8dab.png?auto=format"
   alt="Menu shown quick responses to the signal, from triaging the signal, to responding to the signal by blocking IPs or compromised users, to enabling automatic blocking" /%}

The blocking can be rescinded or extended from the [Denylist](https://app.datadoghq.com/security/appsec/denylist).

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_denylist_menu.9accc68bb4ce77e5856df037980262cd.png?auto=format"
   alt="Menu letting you access the denylist, Policies followed by Denylist" /%}

If the signal wasn't accurate, you can extract the list or users or IPs and add it to the Denylist manually.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_denylist_new.2fd3a9fa75600eb7e624e9e737e24154.png?auto=format"
   alt="Prompt enabling you to add a new IP, user or user agent to the denylist" /%}

#### In-App WAF rules{% #in-app-waf-rules %}

If the Denylist isn't sufficient, you can create a WAF rule. A WAF rule evaluates slower than the Denylist, but it is more flexible.

To create a new rule, do the following:

1. Go to **AAP** > **Policies** > **In-App WAF** > [Custom Rules](https://docs.datadoghq.com/api/latest/webhooks-integration/)].
1. Click **Create New Rule** and complete the configuration.
1. Follow the steps in **Define your custom rule**.
1. In **Select the services you want this rule to apply to**, select your login service, or whichever services where you want to block requests. You can also target the blocking to the login route.
   {% image
      source="https://datadog-docs.imgix.net/images/security/ato/guide_waf_blocking.bcd8f7e5061b17733a653b1ef9501482.png?auto=format"
      alt="Screenshot of the WAF rule creation modal selecting a specific route on a specific service" /%}
1. In **If incoming requests match these conditions**, configure the conditions of the rule.
   1. If you want to block a specific user agent, you can paste it in **Values**. In **Operator**, you can use **matches value in list**, or if you want more flexibility, you can also use a **Matches RegEx**.
      {% image
         source="https://datadog-docs.imgix.net/images/security/ato/guide_waf_blocking_ua.c1e8259d47e13e64464e059fd105baa3.png?auto=format"
         alt="A screenshot of a user agent getting blocked" /%}
1. Use the **Preview matching traces** section as a final review of the rule's impact. If no unexpected traces are shown, select a blocking mode and save the rule.

The response is pushed to tracers automatically and blocked traces appear in the [Traces explorer](https://app.datadoghq.com/security/appsec/traces).

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_waf_blocking_traces.ca1d2299db25f40c7e787d98f30e444b.png?auto=format"
   alt="Table showing traces matching your rules" /%}

Multiple blocking actions are available. Depending on the sophistication of the attackers, you might want a stealthier response so that attackers don't immediately realize they were blocked.

For more information, see [In-App WAF Rules](https://app.datadoghq.com/security/appsec/detection-rules?query=type%3Aapplication_security%20tag%3A%22category%3Aaccount_takeover%22&deprecated=hide&groupBy=none&mitreFilters=%7B%22visualize%22%3A%7B%22value%22%3A%5B%22all%22%5D%2C%22excluded%22%3Afalse%7D%2C%22ruleDensity%22%3A%7B%22value%22%3A%5B%5D%2C%22excluded%22%3Afalse%7D%7D&sort=date&viz=rules).

#### Automated data export{% #automated-data-export %}

You can configure a signal to push any user ID using a webhook. This method can be used to push compromised users to your systems and reset their credentials or restrict them. The goal is to make those accounts useless to the attacker.

{% alert level="info" %}
Not all rules are compatible with this feature. From the OOTB rules, the compatible rules are:
- Distributed Credential Stuffing campaign (attacker fingerprint)
- Bruteforce attack
- Credential Stuffing attack

{% /alert %}

To configure a signal to push a user ID using a webhook, do the following:

1. Configuring a [standard webhook target](https://docs.datadoghq.com/api/latest/webhooks-integration/). To see how this works in Cloud SIEM, go to [Automate the Remediation of Detected Threats with Webhooks](https://docs.datadoghq.com/security/cloud_siem/guide/automate-the-remediation-of-detected-threats/).
1. In [Detection Rules](https://app.datadoghq.com/security/appsec/detection-rules?query=type%3Aapplication_security%20tag%3A%22category%3Aaccount_takeover%22&deprecated=hide&groupBy=none&mitreFilters=%7B%22visualize%22%3A%7B%22value%22%3A%5B%22all%22%5D%2C%22excluded%22%3Afalse%7D%2C%22ruleDensity%22%3A%7B%22value%22%3A%5B%5D%2C%22excluded%22%3Afalse%7D%7D&sort=date&viz=rules), open the rules you want to configure.
   {% image
      source="https://datadog-docs.imgix.net/images/security/ato/guide_detection_rules.aa28d97867c9e8ba16bf70f2c69d722d.png?auto=format"
      alt="Tables of ATO-related detection rules" /%}
1. Go to the notification settings in a detection rule condition.
1. Add a recipient and turn on **Notify** for every new `@usr.id` detected. This allows you to export the list when updates occur.

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/threats/notify-on-update.ed4e77e0d95468507903ccadb8a53529.png?auto=format"
   alt="Notify on update toggle on detection rule editor" /%}

Notification targets set in the detection rule condition receive a message when new user IDs are detected. Notification profiles monitoring these signals do not receive alerts for new user IDs.

To receive targeted and compromised user IDs with a webhook, set up a webhook using the Datadog webhook integration. Include the `$SECURITY_SIGNAL_ATTRIBUTES` variable in the webhook payload. The user IDs are stored under the `@usr.id` path in the JSON payload.

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/threats/notify-on-update-payload.c6b92b782480a44f463f786ed0477a49.png?auto=format"
   alt="Notify on update example payload" /%}

By parsing the payload, you can act upon the IDs in your own systems.

**Important:** The list only contains the IDs detected since the last notification. IDs aren't deduplicated if they log in again.

### Step 3.5: Monitor{% #step-35-monitor %}

After the attacker introduces the response, they might suspend or adapt their attack. Keep monitoring the rate of login attempts after introducing the response, especially failures. Attacks might drop off only to resume after a few minutes, hours, or days.

If a large-scale attack resumes, the Distributed Credential Stuffing signal should re-execute. In this case, review the following considerations:

- Persistent attackers often require multiple iterations of defensive measures before giving up.
- The ideal defense is a robust blocking strategy that the attacker cannot circumvent.
- Attackers frequently attempt to evade detection by altering IPs and user agents. They're less likely to deeply modify the script they procured to send their login attempts so headers are a more resilient target.
- Effective strategies include fingerprint-based or correlation methods that identify rare header combinations.
- Monitor blocked traffic resulting from previous defensive responses.
- Blocking attacker traffic may inadvertently block legitimate traffic. Implement mechanisms to unblock legitimate traffic, either adapt the Datadog response or ensure it is unblocked post attack.

### Step 3.6: Cleanup{% #step-36-cleanup %}

After a few days with no significant attacker activity, you might consider the attack over and move to a cleanup phase.

The goals of the cleanup phase are the following:

- Disable any mitigations that were added.
- Ensure no legitimate traffic is blocked.
- Identify opportunities to harden services against future attacks.
- Identify the source of the data the attacker used against users.

#### Disabling mitigations{% #disabling-mitigations %}

User blocking should be based on the timer you set when you selected **Block All Attacking IPs** in the signal. This user blocking configuration doesn't require any further action.

If you configured permanent blocking, unblock users and IPs from the Denylist by doing the following:

1. Open the [Denylist](https://app.datadoghq.com/security/appsec/denylist).
1. Click **Blocked IPs** or **Blocked users**.
1. In the entity list, locate the IP or user, and then click **Unblock**.

#### Disable or delete any custom In-App WAF rule(s){% #disable-or-delete-any-custom-in-app-waf-rules %}

To disable or delete In-App WAF rule(s), go to the [custom In-App WAF rules page](https://docs.datadoghq.com/api/latest/webhooks-integration/) and disable the rules by clicking on **Monitoring** or **Blocking**, and selecting **Disable Rule**.

If the rule is no longer relevant, you can delete it by clicking more options (**â¦**) and selecting **Delete**.

#### Validate no legitimate traffic is blocked{% #validate-no-legitimate-traffic-is-blocked %}

To validate that no legitimate traffic is blocked, the volume of traffic should match that of the attack closely, with virtually no blocked traces outside the main waves.

To validate that no legitimate traffic is blocked, do the following:

1. Go to [Traces](https://app.datadoghq.com/security/appsec/traces) and search for blocked traces with the search `@appsec.blocked:true`.
1. If you see significant traffic blocked on an ongoing basis, the traffic is likely legitimate users.
   1. Disable the incorrect blocking rule to avoid blocking further users.
   1. Prioritize unblocking that traffic from the [Denylist](https://app.datadoghq.com/security/appsec/denylist).

#### Hardening your services{% #hardening-your-services %}

Large ATO campaigns are rarely an isolated occurrence. You might want to leverage the time between attacks to harden your services and establish configurations you can leverage during subsequent attacks.

Here are some common hardening examples:

- **Rate limit login attempt per IP/user/network range/user agent:** This soft-blocking feature lets you aggressively curtail the scale of the attack in some circumstances with minimal impact on normal users, even if they happen to share traits with the attacker
- **Adding friction at login:** To break attackers' automation without significantly impacting users, use captchas or modifying the login flow during an attack (for example, require that a token is fetched from a new endpoint).
- **Enforce multi-factor authentication (MFA):** Datadog found MFA extremely effective in stopping account compromise. You could require your most privileged users to use MFA, especially during attacks.
- **Limiting sensitive actions for users:** If your services allow users to perform sensitive actions (spending money, accessing sensitive information, changing contact information, etc.), you might want to prohibit high risk users with suspicious logins until they are reviewed manually or through multifactor authentication. Suspicious logins can be programmatically fed to your systems by Datadog through a webhook.
- **Ability to consume signal findings programmatically:** Create an endpoint to consume Datadog webhooks and automatically take action against suspected users/IPs/traits.

#### Identifying the attacker data source{% #identifying-the-attacker-data-source %}

Attackers acquire lists of compromised accounts in bulk. By identifying the source of their database, you can proactively identify users at risk.

To identify the source of their database, export users impacted by the attack using one of these options:

- In the signal details, in **Targeted users**, click **Export to CSV**. This option exports up to 10k users.
- If you need to export more than 10k users, manually paginate your query by performing manual [API calls](https://docs.datadoghq.com/api/latest/spans/#aggregate-spans). The Traces explorer performs similar calls, so you can base your requests on the call it's performing by grouping by `@appsec.events_data.usr.login`. Set the limit to 10000 and use smaller time ranges to avoid the backend cap.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/guide_user_table.019e095eada39388321be07ea13f9484.png?auto=format"
   alt="Table showing the users targeted by the attack. One user is shown in a pill because we have a side-panel with more activity on them" /%}

When you have a list, review it for common attributes:

- If all users are coming from one region or one customer.
- A large majority of users share any known compromise (use the [Have I Been Pwned](https://haveibeenpwned.com/) API).

When the source of the database is identified, proactively force a password reset of those customers or flag them as higher risk. This increases confidence that future suspicious logins were indeed compromised.

#### Review additional attacker activity{% #review-additional-attacker-activity %}

Leveraging the signature from the attacker, expand filters to look at what non-login activity they performed.

This filter can be less accurate. For example, a filter that matches the signature of a mobile application with legitimate traffic but that was cloned by the attacker for their attack. The filter might show research done by the attacker ahead of time, and share hints on what the attacker may be looking to do next.

You can also pivot on the infrastructure used by the attacker. Did those malicious IPs do anything but logins? Are they accessing other sensitive APIs?

## Conclusion{% #conclusion %}

Account theft is a common threat but also much more complex than traditional injection exploits. Catching them requires tight integration with your systems and involves enough uncertainty that automated responses aren't possible for the most advanced attacks.

In this guide, you did the following:

- Learned what account takeover campaigns can look like, how to triage them, and how to counter them.
- Instrumented your login services to provide Datadog AAP with all the context it needs.
- Configured your login services to provide every capability at the time of the attack.

This is general guidance. Depending on your applications and environments, there might be a need for additional response strategies.
