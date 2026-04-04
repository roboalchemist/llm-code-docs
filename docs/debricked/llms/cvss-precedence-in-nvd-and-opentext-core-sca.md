# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/cvss-precedence-in-nvd-and-opentext-core-sca.md

# CVSS precedence in NVD and OpenText Core SCA

> This blog was published on 11th January, 2024.

The CVSS score is an industry standard for ranking the severity of a vulnerability. It is developed and maintained by FIRST, which recently published the fourth version of the specification, CVSS v4.0. Here we take a closer look at the CVSS score in the NVD database and discuss why it can have multiple sources and what that means. We also clarify which score is used by OpenText Core SCA when there is more than one to choose from.

Vulnerabilities enumerated with a CVE identifier are given a CVSS severity score in the [NVD database](https://nvd.nist.gov/). Looking at the vulnerability information on NVD reveals that this score can be provided either by NVD, by the CVE numbering authority, or both. When there are two scores, they also always differ. To understand this, and also to understand how to interpret this, let us look at what is happening here.

First, we must note that scoring a severity according to the CVSS specification is not an exact science. Despite the specification and user guide provided by [FIRST](https://www.first.org/), there is still room for interpretation in individual cases. Still, with some experience and by using the knowledge of how previous vulnerabilities have been interpreted and scored, we can expect a convergence towards one unique true score.&#x20;

Second, the CVSS score must not be confused with a risk rating. The score assumes a worst-case scenario and assumes that vulnerable configurations are used if such a configuration is reasonable. It does not take organization-specific defenses, tools, and processes. So even if we have one true severity score, this is not directly applicable to a given organization, system, or application. The score must be used only as a starting indicator e.g., for prioritizing triage.

### CVSS vectors

When we talk about the CVSS score, we typically mean the base score that ranges from 0 to 10. This is in turn based on the CVSS vector which takes a few more granular aspects into account. When doing triage, the CVSS vector is a good starting point since it provides more information. The information both indicates how easy a vulnerability is to exploit, which can be interpreted as the probability of exploitation, and the impact of such an exploitation. These aspects are divided into several metrics.

Based on the [CVSS specification and user guide](https://www.first.org/cvss/), the metrics can be determined using knowledge of the vulnerability. The metrics are both summarized in a CVSS vector and collapsed into a CVSS score.

For each new vulnerability with a CVE identifier, NVD determines the CVSS vector and computes the corresponding CVSS base score.

### CVSS vectors submitted by CNAs

NVD also allows for a [CVE Numbering Authority (CNA)](https://nvd.nist.gov/general/cna-counting) to submit CVSS vectors for inclusion in the NVD database. This is through a process called [CVMAP](https://nvd.nist.gov/vuln/cvmap) (Collaborative Vulnerability Metadata Acceptance Process), which controls how a metadata for CVEs can be submitted to NVD. This submitted CVSS vector may or may not equal the vector provided by NVD. Since the metrics require human interpretation, slight differences in the interpretation can cause a discrepancy. It could also be that either of the analysts are lacking some information that is available to the other at the time of scoring.&#x20;

It can be noted that CVMAP also includes an Authorized Data Publisher (ADP) role. These can provide CVE metadata without being a CNA. In the following we will just use CNA, but this implicitly also includes ADPs.

Allowing a CNA to provide a CVSS vector opens up for more inclusive and open research related to vulnerabilities. It also distributes the burden of keeping up with providing detailed information in a world with an increasing number of vulnerabilities. Still, discrepancies have to be handled in some way. NVD does this by analyzing the submitted CVSS vectors and comparing them to their own.&#x20;

### CNA acceptance levels

Using the NVD interpretation as the ground truth, NVD records how accurate the submitted vector is. This accuracy is accumulated over time for each CNA, using the last 40 CVEs that the CNA provided a CVSS vector for. By becoming more accurate and aligned with the NVD interpretation, the CNA can be considered more trustworthy (in terms of providing accurate CVSS vectors).&#x20;

Through this accuracy, the CNA will be attributed an [acceptance level](https://nvd.nist.gov/vuln/cvmap/Understanding-Acceptance-Levels). The acceptance levels start at “Reference”, then moves to “Contributor”, and finally if submitted data agrees with NVD-provided data at least 95% of the time (counting the eight metrics for the last 40 CVSS vectors), then you can get the highest acceptance level of “Provider”.

For “Providers”, the NVD trusts the data provided by the CNA and does have to compute its own CVSS score. For these CNAs, NVD only audits 10% of the submitted CVSS vectors, meaning that they compute their own CVSS vector and compare it with the one provided by the CNA.

### NVD webpage information

With this background, we can understand the different variants of CVSS provided by NVD. Let us start with the webpage information.&#x20;

If the CNA CVSS agrees with the NVD CVSS, then only the CNA CVSS is listed. To clarify this agreement there is a green checkmark on the icon for the CNA acceptance level. An example is [CVE-2023-41699](https://nvd.nist.gov/vuln/detail/CVE-2023-41699). If the two CVSS vectors do not agree, then both are listed as can be seen in e.g., [CVE-2023-47688](https://nvd.nist.gov/vuln/detail/CVE-2023-47688).&#x20;

If the CNA did not provide a CVSS vector upon submitting the vulnerability to NVD, obviously only the NVD CVSS score and vector is provided on the webpage. An example is [CVE-2023-38313](https://nvd.nist.gov/vuln/detail/CVE-2023-38313).

If the CNA acceptance level has reached “Provider”, there is only the CVSS score given by the provider. An example is [CVE-2023-44324](https://nvd.nist.gov/vuln/detail/CVE-2023-44324). An exception is if the CVSS vector has been chosen for audit. If it then matches the NVD CVSS, there is a green checkmark and if there is a discrepancy, both are listed. Examples of this is [CVE-2023-21559](https://nvd.nist.gov/vuln/detail/CVE-2023-21559) and [CVE-2023-21557](https://nvd.nist.gov/vuln/detail/CVE-2023-21557) respectively.

To help improve the scoring process across the community, NVD also records the reason for the two scores not being the same. This record can be seen in the history of the [CVE Naming Authority Status](https://nvd.nist.gov/vuln/cvmap/search).

### API information

Vulnerability information, including the CVSS vector, can also be retrieved from the NVD API. Here we will only focus on [API 2.0](https://nvd.nist.gov/developers/vulnerabilities).&#x20;

If there is a CNA and an NVD provided CVSS vector, both are provided in the JSON response. To prioritize between the two vectors, NVD sets a “type” value that can be either “Primary” or “Secondary”.&#x20;

If the CNA has reached the acceptance level of “Provider” and the information is audited, then the CNA CVSS vector is given a type value of “Primary”, and the NVD CVSS vector has a type value of “Secondary”.&#x20;

Giving precedence to CNAs with high acceptance level gives visibility to the CNA and incentivises the CNA to provide reliable CVSS scores.

If the CNA has an acceptance level that is either “reference” or “contributor” the NVD CVSS vector is seen as the “Primary” vector and the CNA is “Secondary”.

### CVSS vector provided by Debricked

For each CVE, Debricked provides one CVSS vector to help our customers prioritize vulnerabilities. Here we aim to stay aligned with NVD by providing the vector and score that is marked as “Primary” in the API.

This means that the CVSS vector and score sometimes is the one computed by NVD and sometimes it can be the one provided by the CNA (or both if they are equal). The latter is the case if the CNA has proven itself over time of being able to accurately score the vulnerability according to the practices used by the NVD researchers. In other words, they have reached an acceptance level of “Provider”, meaning that they have had the same assessment as NVD at least 95% of the time. As noted, audited CVSS vectors will set NVD as “Primary.”

### Conclusion

The CVSS vector can be provided by different entities, often resulting in different scores. The same vulnerability can be considered critical by one entity and high by another. This can create confusion when interpreting the severity. Debricked adopts the use of a primary vector as provided by NVD. This seems to be a logical and reasonable choice since it matches the overall assessment of NVD and how they choose to prioritize vulnerability severity scoring.
