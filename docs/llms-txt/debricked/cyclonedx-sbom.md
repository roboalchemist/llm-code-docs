# Source: https://docs.debricked.com/overview/language-support/cyclonedx-sbom.md

# CycloneDX SBOM

OpenText Core SCA supports tracking dependencies in [CycloneDX SBOM](https://cyclonedx.org/) using files in JSON and XML formats.

To ensure that OpenText Core SCA identifes the SBOM files as CycloneDX SBOMs, please name them using one of the following conventions:

* *.bom..json*
* *.\*cdx.json*
* *.\*cdx.xml*
* *.bom..xm*l

The specific features available for the SBOM will depend on the libraries included and the individual package managers used.

### **Supported file formats and features**

<table data-full-width="true"><thead><tr><th>Language</th><th>Supported file formats</th><th data-type="checkbox">Root dependencies </th><th data-type="checkbox">Indirect dependencies</th><th data-type="checkbox">Dependency trees</th><th data-type="checkbox">Security scanning</th><th data-type="checkbox">License scanning</th><th data-type="checkbox">Root fix</th><th data-type="checkbox">Pull Request</th><th data-type="checkbox">Rachability Analysis</th><th>High Performance Scan</th></tr></thead><tbody><tr><td>CycloneDX SBOM</td><td><em>bom.json, cdx.json</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>true</td><td>Yes*</td></tr></tbody></table>

**\***&#x54;his is a native lock file format. Native lock file formats are the fastest formats to scan.

### Analyzing external SBOM files using OpenText Core SCA - video guide

{% embed url="<https://www.youtube.com/watch?v=H4Ud5QqZE-0>" %}
