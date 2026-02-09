# Source: https://docs.datadoghq.com/security/workload_protection/inventory/coverage_map.md

---
title: Coverage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Workload Protection > Coverage and Posture
  Management > Coverage
---

# Coverage

Workload Protection [Coverage](https://app.datadoghq.com/security/workload-protection/inventory/coverage) provides a real-time view of security coverage across all your hosts. Use Coverage to assess protection posture, identify gaps, and take immediate action.

{% image
   source="https://datadog-docs.imgix.net/images/security/cws/workload_protection_coverage_map.64ec9fb745d19c8d8169402ce5564529.png?auto=format"
   alt="Leverage the Coverage map to get real time visibility into the workload protection status across all your hosts and see which policies are effectively applied" /%}

## Key functionality{% #key-functionality %}

- **Real-time visibility**: Coverage updates every five minutes for accurate, current status.
- **Granular filtering**: Search by policy, rule, version, status, tactic, or technique.
- **Direct drill-down**: Drill down from a high-level map to a detailed asset or policy view.
- **Actionable alerts**: Highlight workloads in a warning or failed state so you can respond promptly.
- **Coverage analytics**: Track rule deployment health, stale agents, and configuration issues.

## Key benefits{% #key-benefits %}

- Reduce blind spots by monitoring for unprotected workloads.
- Shorten detection and response times with direct remediation workflows.
- Maintain continuous compliance and policy alignment.
- Integrate posture checks into CI/CD and infrastructure reviews.

## Policy statuses{% #policy-statuses %}

Hosts are identified with the following colors:

- Green: all rules in the policies applied to the host have passed.
- Orange: one or more rules in the policies applied to the host are in error.

{% image
   source="https://datadog-docs.imgix.net/images/security/cws/workload_protection_coverage_map.64ec9fb745d19c8d8169402ce5564529.png?auto=format"
   alt="Leverage the Coverage map to get real time visibility into the workload protection status across all your hosts and see which policies are effectively applied" /%}

Click an orange hexagon to view a host with policy rules in error.

Policies are displayed with the following statuses:

- **Fully Loaded:** all of the policy's rules pass.
- **Partially Loaded:** some of the policy's rules fail.
- **Fully Rejected:** the entire policy is failing.

## Use cases{% #use-cases %}

Here are some ways to use Coverage to improve your workload security.

### Detect and remediate policy deployment issues{% #detect-and-remediate-policy-deployment-issues %}

From the **Incomplete infrastructure coverage** status card on the Coverage page, you can address policy deployment issues:

1. In **Incomplete infrastructure coverage**, click **Warning**, and then select the policies in **Security coverage needs attention**. In the Coverage map, assets with policy deployment problems are displayed as orange hexagons.
1. Review the list of deployed policies. Policies are highlighted with statuses such as **Partially Loaded**, **Fully Rejected**, and so on.
1. In the policy details, do one of the following:
   - [Edit a policy](https://docs.datadoghq.com/security/workload_protection/workload_security_rules/custom_rules).
   - View a policy's rule errors, and then [edit them](https://docs.datadoghq.com/security/workload_protection/workload_security_rules/custom_rules) as needed.
1. Redeploy and confirm the fix in the Coverage map.

### Identify assets missing Workload Protection{% #identify-assets-missing-workload-protection %}

From the **Incomplete infrastructure coverage** status card on the Coverage page, you can review assets without full Workload Protection (WP):

1. In **Improve infrastructure coverage**, click **NO WP**. **NO WP** shows how many hosts are running the Datadog Agent without Workload Protection enabled.
1. Click **Inspect Hosts Without WP**. Fleet Automation appears, allowing you to [set up Workload Protection](https://docs.datadoghq.com/security/workload_protection/setup/).

### Identify assets missing key features{% #identify-assets-missing-key-features %}

From the **Incomplete infrastructure coverage** status card on the Coverage page, you can find assets with gaps in protection.

1. In **Improve infrastructure coverage**, click **INFO** to review the `outdated_agent` flag. The `outdated_agent` flag means an outdated Agent version is running and might not support the latest Workload Protection features.
1. In **Improve infrastructure coverage**, click **NO AGENT**. **NO AGENT** shows how many hosts are not running the Datadog Agent, and therefore can't be evaluated by Workload Protection.
   1. Click **Inspect Hosts Without Agent**. The Resource Catalog appears, allowing you to address hosts missing agents.
1. Filter by **Agent Version** to detect outdated agents lacking recent security updates.
1. Update the Agent to ensure complete coverage.

### Search assets by MITRE ATT&CK techniques and tactics{% #search-assets-by-mitre-attck-techniques-and-tactics %}

From the **Filter by tactics, techniques, and policy types** status card on the Coverage page, built-in filters for **Tactics**, **Techniques**, and **Policies** show exactly which parts of the MITRE ATT&CK framework are covered.

To use these filters to strengthen detection and response alignment with proven MITRE ATT&CK framework threat models, do the following:

1. Click **Tactics** to filter for high-priority tactics (for example, `TA004-privilege-escalation`, `TA004-persistence`), to ensure those are protected across all hosts.
1. After the map updates for the tactic you selected, click **Techniques** and select a technique to identify gaps in technique coverage for critical systems.
1. Click **Policies** and select a policy type to see the distribution of policies across the filtered infrastructure.

For information about the MITRE ATT&CK map available in SIEM or Workload Protection, see [MITRE ATT&CK map](https://docs.datadoghq.com/security/detection_rules/#mitre-attck-map).

### Experiment with new rules{% #experiment-with-new-rules %}

You can use Coverage to test and iterate on custom security rules:

1. Write and deploy a [new custom rule](https://docs.datadoghq.com/security/workload_protection/workload_security_rules/custom_rules).
1. In **Coverage**, search for the rule by rule ID, policy ID, or hostname.
1. Confirm that the agent has loaded the rule successfully.
1. If errors appear, review the details, fix the rule, and redeploy.

## Workload coverage triage and remediation cycle{% #workload-coverage-triage-and-remediation-cycle %}

As an example of how to use Coverage to triage and remediate coverage issues, here is a sequence that starts by establishing a baseline, closing blind spots, and securing the most critical assets. It then verifies enforcement mechanisms, restores agent health, and aligns detection coverage with known adversary behaviors. Finally, it applies rule updates, confirms effectiveness, and records the state for audit and incident reference.

1. Do a full environment view to establish baseline coverage status.
1. Focus on assets that appear fully covered. Validate that their policies, rules, and agents are working as intended before addressing visible gaps. This uncovers silent failures in trusted systems that would otherwise be ignored.
1. Identify all unprotected or partially protected workloads.
1. Prioritize assets with the highest business impact and exposure.
1. Verify policy deployment and enforcement on those assets.
1. Check for outdated or unhealthy agents on all remaining workloads.
1. Map current detection coverage to MITRE ATT&CK to find gaps in tactics and techniques.
1. Deploy or update detection rules to close those gaps.
1. Reassess coverage to confirm posture changes took effect.
1. Log the final state for compliance and future comparison.

## Further reading{% #further-reading %}

- [MITRE ATT&CK map](https://docs.datadoghq.com/security/detection_rules/#mitre-attck-map)
- [Review your Workload Protection coverage with the Coverage map](https://app.datadoghq.com/release-notes/review-your-workload-protection-coverage-with-the-coverage-map)
