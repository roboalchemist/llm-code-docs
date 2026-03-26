# Source: https://docs.debricked.com/product/exporting-sbom/sbom-export.md

# SBOM export

{% hint style="info" %}
T*his feature is only available for enterprise users. Already have an account?* [*Click here to upgrade.*](https://debricked.com/app/en/repositories?billingModal=enterprise,free)
{% endhint %}

### **What is an SBOM?** <a href="#whatissbom" id="whatissbom"></a>

A **Software Bill of Materials (SBOM)** is a record of the supply chain relationships between the components used when creating software. The record lists all components of a product, including all open source software, which can be helpful for both the developers and other stakeholders, such as investors and legal teams.&#x20;

The SBOM includes the following data points:

* Proof of license - A reference to the source from where the license information is fetched. This field is applicable only for CycloneDX SBOM.&#x20;
* License text - The actual text that the license consists of. This field is applicable only for CycloneDX SBOM.&#x20;
* Copyright statement - Displays the person or organization who holds the copyright.
* Open Source Select[ ](https://portal.debricked.com/open-source-select-58)link - A link to the dependency page in Open Source Select, where you can find additional information on the specific open-source package.
* Dependency relations - Contains information on each component and their direct dependencies. See the Dependency relations sections on the [CycloneDX SBOM export](https://docs.debricked.com/overview/language-support/cyclonedx-sbom) and [SPDX SBOM export](https://docs.debricked.com/product/exporting-sbom/sbom-export/spdx-sbom-export) pages for more details.
* Root Fixes - This data can be found under *Recommendation.* It consists of information about the first version of the specific vulnerable dependency that is safe, as well as the first version of the root or direct dependency that does not contain a vulnerable version of the indirect dependency. See the section Root Fixes for more details. This field is applicable only for CycloneDX SBOM.&#x20;
* Reachability Analysis - Displays the Reachability Analysis results for each vulnerability (if Reachability Analysis has been run). This field is applicable only for CycloneDX SBOM.
  * Reachable - Vulnerability confirmed reachable in code.
  * Not Reachable - Vulnerability not reachable through any execution path.
  * Unknown - Insufficient information to determine reachability.

Keep in mind that license information may differ depending on the package and the specific version used.

### **Export a CycloneDX or SPDX SBOM using web tool** <a href="#exportingacyclonedxsbomusingourwebtool" id="exportingacyclonedxsbomusingourwebtool"></a>

{% hint style="info" %}
*Keep in mind that this feature is only available for enterprise users.*
{% endhint %}

In order to generate the CycloneDX or SPDX SBOM Export:

1. Click **Generate export** on the top right corner of the page.
2. Under **Scope**, choose one of the following options:
   1. **Global export:** Export the SBOM for all repositories you have access to.
   2. **Repositories:** Select specific repositories for which you want to view the data and then choose the corresponding branch. If you select multiple repositories, the **Branch** drop-down will display only the branches common to all the selected repositories.
   3. **Groups:** Export the SBOM for a specific group of repositories.
3. Under **Export Type**, select **CycloneDX** or **SPDX** under **SBOM**.
4. Click **Generate.**
5. Check your email for the exported data, which will be sent to you in the .json format. If you cannot find the email in your inbox, check the spam folder.

#### **Export a CycloneDX or SPDX SBOM using web tool - video guide** <a href="#exportingacyclonedxsbomusingourwebtool-videoguide" id="exportingacyclonedxsbomusingourwebtool-videoguide"></a>

{% embed url="<https://www.youtube.com/watch?v=UMcqdpDp74M>" %}

### **Export a CycloneDX or SPDX SBOM to email using API** <a href="#exportingacyclonedxsbomtoemailusingtheapi" id="exportingacyclonedxsbomtoemailusingtheapi"></a>

If you have already integrated your repository with OpenText Core SCA, you can generate a CycloneDX or SPDX SBOM by fetching your data through the API.&#x20;

To use OpenText Core SCA REST API, you should authenticate first.

Endpoint: /api/{1.0}/open/sbom/generate

Following is an example of a request using curl to generate an SPDX SBOM (to generate a CycloneDX SBOM use `"format": "CycloneDX"`):

```
curl -X 'POST' \
  'https://debricked.com/api/1.0/open/sbom/generate' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{
  "format": "SPDX-2.3",
  "email": "user1@debricked.com",
  "repositoryIds": [
    1
  ],
  "vulnerabilities": true,
  "rootFixes": true,
  "licenses": true,
  "sendEmail": true
}'
```

You can send the following parameters in the body of the request: *commitId*, *email*, *repositoryIds*, *branch*, *locale*. You can choose to add license and vulnerability data, using *licenses: true/false* and *vulnerabilities: true/false*.

If you provide a *commitId*, the *branch* and *repositoryIds* will be ignored. If you leave the *branch* field empty, the report is generated for the identified default branch (most likely 'main' or 'master', if applicable) of the selected repository. It is also possible to create an SBOM for all repositories by not specifying any *repositoryIds*.&#x20;

Once you send the request, you will receive your SBOM via email, which will be sent to you in the *.json* format. If you can’t find the email in your inbox, make sure to check the SPAM folder. If you do not provide an *email* address, the SBOM will be sent to the email of the user who created the request.

#### **Export a CycloneDX or SPDX SBOM to email using API - video guide** <a href="#exportingacyclonedxsbomtoemailusingtheapi-videoguide" id="exportingacyclonedxsbomtoemailusingtheapi-videoguide"></a>

{% embed url="<https://www.youtube.com/watch?v=3NSHvZnX3Gg>" %}

### **Export a CycloneDX or SPDX SBOM directly from API** <a href="#exportingcyclonedxsbomdirectlyfromtheapi" id="exportingcyclonedxsbomdirectlyfromtheapi"></a>

It is also possible to generate a CycloneDX or SPDX SBOM and download it directly through the API.\
As part of the response of the `/api/1.0/open/sbom/generate` endpoint, a reportUuid is sent, which can be used in the `/api/1.0/open/sbom/download` endpoint.

Following is an example response from the `/api/1.0/open/sbom/generate` endpoint:

```
{
  "message": "The report has started generating and can be downloaded through the 'download' endpoint once ready, by using the reportUuId stated below. Be aware that it might take some time before it's finished",
  "reportUuid": "<report_uuid>",
  "notes": [
    "Example note"
  ]
}
```

Following is an example request for the `/api/1.0/open/sbom/download` endpoint:

```
curl -X 'GET' \
  'https://debricked.com/api/1.0/open/sbom/download?reportUuid=<report_uuid>' \
  -H 'accept: */*' \
  -H 'Authorization: Bearer <token>'
```

If you do not want the report to also be sent to your email, it is possible to turn this off by setting the "sendEmail" value to "false" in the `/api/1.0/open/sbom/generate` endpoint.

Click the following link for an example on exporting CycloneDX SBOM:

### [CycloneDX SBOM file example](https://github.com/debricked/blog-snippets/blob/main/example-sbom-report/SBOM_2022-12-14.json)

Click the following link to view the list of commands to create an SBOM using the CLI.

#### [Manually create an SBOM using the CLI](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli#report)

#### [Automatically create an SBOM after scanning, using the CLI](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli#scan)

<table data-view="cards"><thead><tr><th></th></tr></thead><tbody><tr><td><a href="sbom-export/cyclonedx-sbom-export">CycloneDX SBOM export</a></td></tr><tr><td><a href="sbom-export/spdx-sbom-export">SPDX SBOM export</a></td></tr></tbody></table>
