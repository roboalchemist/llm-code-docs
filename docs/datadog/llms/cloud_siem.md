# Source: https://docs.datadoghq.com/getting_started/security/cloud_siem.md

# Source: https://docs.datadoghq.com/security/cloud_siem.md

---
title: Cloud SIEM
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Cloud SIEM
---

# Cloud SIEM

{% callout %}
##### Join an enablement webinar session

Learn how Datadog Cloud SIEM and Cloud Security elevate your organization's threat detection and investigation for dynamic, cloud-scale environments.

[SIGN UP](https://www.datadoghq.com/technical-enablement/sessions/?tags.topics-0=Security)
{% /callout %}

## Overview{% #overview %}

Datadog Cloud SIEM (Security Information and Event Management) is a security data analysis and correlation system. It enables your entire security operations team to view, detect, investigate, and respond to security issues. Leveraging Datadog's scalable platform, Cloud SIEM ingests telemetry from both cloud and onâpremises systems using the Datadog Agent and API-based integrations.

Effective security response requires speed, context, insight, and automation. Cloud SIEM continuously analyzes incoming data to detect threats, generate actionable security signals, and correlate them across multiple sources. This empowers your team to investigate incidents and respond quickly.

To keep your team on top of the latest attacks, Datadog also has a team of threat researchers who analyze petabytes of telemetry across cloud and on-premises systems to identify emerging threats and attacker behaviors. See [Datadog Security Labs](https://securitylabs.datadoghq.com/) to read articles about their recent investigations.

### Security and observability{% #security-and-observability %}

Cloud SIEM embeds both cloud and on-premises telemetry directly into security workflows to accelerate investigation and response. And with a shared platform that brings DevOps and Security teams together, organizations can break down silos and respond to threats collaboratively and efficiently.

### Flexible cost control for security data{% #flexible-cost-control-for-security-data %}

As your organization scales, controlling the ingestion cost of security logs without compromising visibility is critical. Cloud SIEM is integrated with Datadog Log Management so you can choose the appropriate retention and querying capability for your security logs. This flexibility helps you balance cost efficiency with your threat detection needs.

Store logs using one of the available options:

- [Standard indexing](https://docs.datadoghq.com/logs/log_configuration/indexes) for logs that need to be queried frequently with the most compute.
- [Flex Logs](https://docs.datadoghq.com/logs/log_configuration/flex_logs/) for logs that need to be retained long-term, but sometimes need to be queried urgently.
- [Log Archives](https://docs.datadoghq.com/logs/log_configuration/archives/) for logs that are infrequently queried and need to be stored long-term.

### Guided security data onboarding{% #guided-security-data-onboarding %}

Cloud SIEM [Content Packs](https://docs.datadoghq.com/security/cloud_siem/content_packs/) are a curated set of Datadog integrations designed for security teams. Each content pack has instructions on how to configure the integration and what is included, such as detection rules, out-of-the-box interactive dashboards, parsers, and SOAR workflows. Content Packs highlight actionable insights specific to each integration to help you investigate security issues.

### Content pack health monitoring{% #content-pack-health-monitoring %}

After a content pack is activated, it gives you the integration's health status and provides troubleshooting steps if something goes wrong so you can get back up and operational as fast as possible.

### Log search and analysis{% #log-search-and-analysis %}

Build searches in the Log Explorer using facets or by clicking fields directly in the logs. Or use Bits AI and natural language search to find important security events. With built-in group-by and table lookup functions as well as pattern analysis and visualizations, security teams can get security insights from their data. See [Log Explorer](https://docs.datadoghq.com/logs/explorer/) and [Log Search Syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/) for more information.

## Get started{% #get-started %}

If you don't already have a Datadog account, sign up for a [free trial](https://www.datadoghq.com/product/cloud-siem/). After you log in to your Datadog account:

1. Navigate to [Cloud SIEM](https://app.datadoghq.com/security/siem/home?).
1. Click **Enable Cloud SIEM**.
1. Follow the onboarding steps.

See the [Getting Started Guide](https://docs.datadoghq.com/getting_started/security/cloud_siem/) for more detailed setup instructions.

## Cloud SIEM Overview page{% #cloud-siem-overview-page %}

Navigate to the [Cloud SIEM Overview page](https://app.datadoghq.com/security/siem/home?). Use this page to see key security insights and act on common workflows for security analysts, security and detection engineers, and Security Operations Center (SOC) managers. From the Overview page, you can:

- Access important signals, open cases, and high-risk entities.
- Complete onboarding tasks and review contentâpack health.
- View and investigate top signals by geography or internet service provider (ISP).
- Analyze signals and rules by MITRE ATT&CK tactics.
- Track detection performance (Mean Time to Detect (MTTD), falseâpositive rates).
- Read the latest [Security Labs](https://securitylabs.datadoghq.com/) research and release notes.

Click **Customize Page** to reorder or hide modules so you can see what is important to you.

Learn more about each Cloud SIEM Overview page section below.

### Security coverage{% #security-coverage %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/landing/01_security_coverage.32e06ff8c03cc44b491095d17d2aa2e3.png?auto=format"
   alt="Security coverage sections showing 11 active and 1 broken content packs and a bar graph of logs analyzed by Cloud SIEM" /%}

Remain aware of any data processing issues or coverage gaps.

#### Enabled content packs and integrations{% #enabled-content-packs-and-integrations %}

View enabled content packs and integrations across the critical categories to provide comprehensive security coverage. Hover over each section of the horizontal bar to see which content packs are enabled in each category.

#### Content pack and logs health KPIs{% #content-pack-and-logs-health-kpis %}

See whether any content packs or integrations are in warning or broken states so that you can resolve any coverage gaps. Click a status tile to view the affected content packs.

#### Logs analyzed{% #logs-analyzed %}

View logging trends across your top log sources and identify any unusual spikes or drops. Click on the legend at the bottom to explore trends on a per source basis.

### Important signals and cases{% #important-signals-and-cases %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/landing/02_important_signals_cases.ad3c86485f6a40ce4243db3ff7bc4c02.png?auto=format"
   alt="" /%}

See important events happening in your environment, such as:

#### Recent open signals grouped by rule{% #recent-open-signals-grouped-by-rule %}

See signals grouped by rule name and sorted by severity to get an overview of the most important signals in your environment. Click on a signal or a severity pill to see more details in a filtered view in the Signal Explorer.

#### Recent open security cases{% #recent-open-security-cases %}

Use [Case Management](https://docs.datadoghq.com/security/cloud_siem/investigate_security_signals/#case-management) to track signals that require further analysis. View active security cases in your environment and click a case to see more details.

### Risk insights{% #risk-insights %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/landing/03_risk_insights.e690efd0fa887c7570ec1cda67129b28.png?auto=format"
   alt="" /%}

Review the risky entities in your environment.

#### Top risky entities{% #top-risky-entities %}

See the entities with the highest risk scores. Click an entity to view more details and take action.

#### Entity type breakdown{% #entity-type-breakdown %}

View the most common entity types in your environment. Click a pie chart wedge to filter the list of entities by type.

#### Entities risk score breakdown{% #entities-risk-score-breakdown %}

View entities by severity. Click a severity tile to see a list of entities with that severity.

### Threat map{% #threat-map %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/landing/04_threat_map.1a2c64cb124b25189672793b33c6836b.png?auto=format"
   alt="" /%}

Get insights from where the signals in your environment are getting generated.

#### Top IPs by country distribution{% #top-ips-by-country-distribution %}

See which IPs are generating the most signals with a breakdown of important and less important signals. Also, use the map to see a list of signals by country.

#### Signals by country{% #signals-by-country %}

See the proportional breakdown of where signals originate. Click a pie chart wedge to filter by country and state or province, and identify signals from unexpected locations.

#### Signals by ISP provider{% #signals-by-isp-provider %}

Review which ISPs are sending signals. Click on a pie chart wedge to scope down by provider and location.

### Security overview{% #security-overview %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/landing/05_security_overview.547f31b7cbb75d2340bf49ae0a6da82d.png?auto=format"
   alt="" /%}

A high-level overview of all signals.

#### Signal Distribution{% #signal-distribution %}

On the left side of the section, see signals grouped by severity and trend over the selected time window. On the right side, see a break down of signal activity by severity, source, and resolution. Click on a node in the sankey diagram to see signals in the Signal Explorer filtered to the specifics of that node.

#### Mean Time to Respond to Signals{% #mean-time-to-respond-to-signals %}

See KPIs of how quickly your team responds. Click a severity tile to view signals set to `under review` or `archive` and filtered to the selected severity.

### MITRE ATT&CK coverage{% #mitre-attck-coverage %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/landing/06_mitre_coverage.9896e1720fbba0fe7ef03c1febaa55c3.png?auto=format"
   alt="" /%}

Detection rule coverage and signal activity by MITRE ATT&CK tactics and techniques.

#### Techniques with at least 1 rule{% #techniques-with-at-least-1-rule %}

See how many techniques are covered by the detection rules enabled in your environment.

#### Rule density KPIs{% #rule-density-kpis %}

See how many techniques have high, medium, or low density or no rules at all. Click on a tile to view a filtered MITRE map.

#### Signals per tactic view{% #signals-per-tactic-view %}

See which MITRE ATT&CK tactics are generating signals. Click a pie chart wedge to view the Signal Explorer filtered by that tactic. Click the dropdown and select **Rules count** to see which tactics have the most rules mapped to it. When viewing by rule count, clicking on a pie chart wedge creates a detection rule explorer view filtered by that tactic.

#### Signals per technique view{% #signals-per-technique-view %}

See which MITRE ATT&CK techniques are generating signals. Click on a pie chart wedge to view the Signal Explorer filtered by technique. Click the dropdown and select **Rules count** to see which techniques have the most rules mapped to it. When viewing by rule count, click on a pie chart wedge to see the detection rule explorer filtered by that technique.

### Detection rules performance{% #detection-rules-performance %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/landing/07_detection_rule_performance.0bc8cb2d32ae7b623b752313e2b1b166.png?auto=format"
   alt="" /%}

Gain a deeper understanding of detection rule performance. This section works best if you triage signals in Cloud SIEM.

#### MTTD KPIs for Cloud SIEM{% #mttd-kpis-for-cloud-siem %}

See the Mean Time to Detect (MTTD) across all signals. The tiles below show MTTD for critical, high, and medium signals. Click a tile to see signals with that severity in the Signal Explorer.

#### Signal activity{% #signal-activity %}

View signal trends over the selected time window. Select the severity checkboxes at the bottom of the bar graph to scope by severity, which can be useful for identifying unusual spikes or drops.

#### Rules by important signal change (1 week){% #rules-by-important-signal-change-1-week %}

See which rules have increased important signal activity compared to the week prior. Click a rule name to view signals in the Signal Explorer filtered by that rule name.

#### Signals by severity change (1 week){% #signals-by-severity-change-1-week %}

View how the severities across all signals have changed compared to the week prior. Click on a severity to view signals with that severity in the Signal Explorer.

#### Important signals by archived reason{% #important-signals-by-archived-reason %}

See how many signals were archived by archive reason. Click on a reason to view the Signal Explorer filtered by that archive reason.

#### Rules archived with true positive (malicious){% #rules-archived-with-true-positive-malicious %}

See which rules were archived as `True Positive: Malicious`. Click on a rule to view the signals in the Signal Explorer.

#### Rules archived with true positive (benign){% #rules-archived-with-true-positive-benign %}

See which rules were archived as `True Positive: Benign`. Click on a rule to view the signals in the Signal Explorer.

#### Rules by false positive rate{% #rules-by-false-positive-rate %}

See which rules are the noisiest by calculating the percentage of signals that are marked as false positive out of all the signals generated by a rule. Click on a rule to view signals for that rule in the Signal Explorer.

## Further reading{% #further-reading %}

- [Simplify log collection and aggregation for MSSPs with Datadog Observability Pipelines](https://www.datadoghq.com/blog/observability-pipelines-mssp)
- [Datadog Cloud SIEM: Driving innovation in security operations](https://www.datadoghq.com/blog/cloud-siem-enterprise-security)
- [Proactively track, triage, and assign issues with Datadog Case Management](https://www.datadoghq.com/blog/track-issues-datadog-case-management/)
- [Automate common security tasks and stay ahead of threats with Datadog Workflows and Cloud SIEM](https://www.datadoghq.com/blog/automate-security-tasks-with-workflows-and-cloud-siem/)
- [Automate identity protection, threat containment, and threat intelligence with Datadog SOAR workflows](https://www.datadoghq.com/blog/soar/)
- [Build compliance, governance, and transparency across your teams with Datadog Audit Trail](https://www.datadoghq.com/blog/compliance-governance-transparency-with-datadog-audit-trail/)
- [AWS threat emulation and detection validation with Stratus Red Team and Datadog Cloud SIEM](https://www.datadoghq.com/blog/aws-threat-emulation-detection-validation-datadog/)
- [Monitor 1Password with Datadog Cloud SIEM](https://www.datadoghq.com/blog/monitor-1password-datadog-cloud-siem/)
- [Build sufficient security coverage for your cloud environment](https://www.datadoghq.com/blog/building-security-coverage-for-cloud-environments/)
- [Monitor DNS logs for network and security analysis](https://www.datadoghq.com/blog/monitor-dns-logs-for-network-and-security-datadog/)
- [Monitor Akamai Zero Trust and Application Security with Datadog Cloud SIEM](https://www.datadoghq.com/blog/akamai-zero-trust-application-security/)
- [How attackers take advantage of Microsoft 365 services](https://www.datadoghq.com/blog/microsoft-365-detections/)
- [Monitor your organization's security posture with Datadog](https://www.datadoghq.com/blog/monitor-security-metrics/)
- [Identify risky behavior in cloud environments](https://www.datadoghq.com/blog/risky-behavior-cloud-environments/)
- [Amazon SES monitoring: Detect phishing campaigns in the cloud](https://www.datadoghq.com/blog/detect-phishing-activity-amazon-ses/)
- [Build, test, and scale detections as code with Datadog Cloud SIEM](https://www.datadoghq.com/blog/detection-as-code-cloud-siem/)
