# Source: https://help.aikido.dev/getting-started/general-information/generate-sbom-based-on-open-source-packages.md

# Generate SBOM Based on Open-Source Packages

Aikido allows you to export both **SBOMs (Software Bill of Materials)** and **VEX (Vulnerability Exploitability eXchange)** files—giving you visibility into your software components and helping you prioritize what actually needs fixing.

**Use Cases:**

* **SBOM Export** (CycloneDX 1.6 , SPDX-2.3 or CSV)
  * Share with customers for compliance (e.g., ISO 27001, SOC2).
  * Feed into third-party risk or procurement tools.
* **VEX Export** (CycloneDX only)

  * Clearly flag which vulnerabilities are **exploitable** and which are **not applicable**.

## Where to find the SBOM <a href="#where-to-find-the-sbom" id="where-to-find-the-sbom"></a>

**Step 1.** Go to Reports > [Licenses & SBOM](https://app.aikido.dev/licenses)

**Step 2.** Download SPDX, CycloneDX or CSV SBOM via the top right action

![Python package license risks overview with filters and SBOM download option.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-46f4f8c55314ffff07437cd1b2ca77ea4c832a79%2Fgenerate-sbom-based-on-open-source-packages_74772dd0-d436-4829-9063-800bb19bb697.png?alt=media)

**Optional.** Filter licenses on different parameters and export the SBOM after. The export takes into account the chosen filter values.

![Filter menu for searching repositories by license, language, risk, and container options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6f6b8a2c274b7b7996cb1cd7814b34a3aa1062f8%2Fgenerate-sbom-based-on-open-source-packages_f7c910f2-edc1-4859-a464-b0155cc6d093.png?alt=media)

If you want to filter on team, you can do this via changing the Team Filter on the top of the page.

![Team selection dropdown for viewing Licenses & SBOM reports.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-644f5ae98897b1517a5dcf159e59369384237810%2Fgenerate-sbom-based-on-open-source-packages_156d14a3-4155-4ba9-bc53-1f4dff0152b5.png?alt=media)

> If you have multi-branch scanning enabled, you can get different SBOMs per legacy branch by selecting the specific legacy branch repo in the dropdown. Contact us via in-app chat for more info.

### Generate and Export via API <a href="#generate-and-export-via-api" id="generate-and-export-via-api"></a>

Aikido also supports generation and download of SBOM via API. More information can be found in our [Apidocs.](https://apidocs.aikido.dev/reference/exportcoderepolicenses)
