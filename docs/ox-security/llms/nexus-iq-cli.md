# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/open-source-security/nexus-iq-cli.md

# Nexus IQ CLI

OX Security integrates with Nexus IQ CLI, a tool from Sonatype, to analyze vulnerabilities in customer-selected repositories.

OX leverages Sonatype’s security capabilities to scan these repositories and identify risks related to the libraries they use.

This integration enhances the OX system’s visibility into software dependencies and potential security threats

The process includes identifying security risks associated with the libraries used in the repository. OX Security enhances these results by enriching the findings beyond the standard tool capabilities, including the following:

* whether a library is direct or indirect
* if it is actively used
* who committed it
* when it was committed
* what is the commit message

OX aggregates this data for a more comprehensive security assessment. Then the enriched results are displayed at the policy level within OX.

Additionally, the some base findings from Nexus IQ CLI are sent back to the Nexus platform, allowing customers to view them there under the corresponding repository name.

The enriched insights are not shared with Nexus, as the enrichment is exclusive to OX Security.
