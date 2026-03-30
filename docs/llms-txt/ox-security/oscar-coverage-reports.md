# Source: https://docs.ox.security/generate-reports/built-in-reports/oscar-coverage-reports.md

# OSCAR Coverage Reports

The OSCAR Coverage Report maps OX detections and findings against the MITRE ATT\&CK framework.

It visualizes how your organization’s security posture aligns with adversarial tactics and techniques, helping you identify which attack vectors are covered and where exposure remains.

By connecting OX findings to the ATT\&CK matrix, the report enables AppSec and DevSecOps teams to track detection coverage, discover visibility gaps, and prioritize mitigation efforts across the attack lifecycle.

Each card within a column corresponds to a technique (TID) that OX can detect, prevent, or monitor.

<figure><img src="broken-reference" alt=""><figcaption></figcaption></figure>

Each technique card includes:

* The **technique ID and name** (for example, T1071: SQL Injection)
* **Coverage indicators** showing which OX modules detect or mitigate the technique
* **Color-coded icons** indicating coverage status and data sources (for example, SBOM, PBOM, CI/CD)
* **Sub-techniques**, if relevant, grouped under their main technique

## Key Elements

<table><thead><tr><th width="251">Element</th><th>Description</th></tr></thead><tbody><tr><td><strong>Technique ID (Txxxx)</strong></td><td>MITRE ATT&#x26;CK reference for the mapped technique.</td></tr><tr><td><strong>Coverage Icons</strong></td><td>Show the OX modules responsible for detecting or mitigating the technique.</td></tr><tr><td><strong>Numbers in Circles</strong></td><td>Indicate the number of findings, controls, or mapped assets.</td></tr><tr><td><strong>Column Headers</strong></td><td>Display the tactic name and the number of techniques covered (for example, 7/11).</td></tr><tr><td><strong>Empty or Faded Cards</strong></td><td>Represent techniques not currently covered by OX.</td></tr></tbody></table>

***

## Example

In the **Execution** column, you might see the following:

* **T1071: SQL Injection** – Covered through PBOM detections.
* **T1059: Command Execution** – Detected through CI/CD log analysis.
* **T1047: Script Execution** – Uncovered technique (faded card).

This view helps AppSec teams quickly identify which vectors are already addressed and where coverage should be expanded.

## Using the Report

1. Go to **Reports > OSCAR Coverage**.
2. Review the coverage per tactic by scrolling horizontally across the MITRE framework.
3. Identify gaps by locating faded or uncovered techniques.
4. Click a technique card to view related detections, data sources, or mapped findings.
5. Export the report to share a coverage summary across your organization.
