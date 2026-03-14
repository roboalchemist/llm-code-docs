# Source: https://docs.ox.security/inventory-with-ox-bom/api-bom.md

# API BOM

{% hint style="success" %}
**At a glance:** Review a detailed list of all API endpoints exposed by your applications. Map specific detected issues to the APIs that expose them (for APIs written in supported languages).
{% endhint %}

{% hint style="warning" %}
See the list of [languages and web frameworks](https://gitlab.com/oxsecurity/ox-docs/docs/-/blob/main/a-tour-of-ox/broken-reference/README.md) currently supported for:

• API detection\
• API/issue correlation
{% endhint %}

## Overview

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-68f1f8bf43198660a604f1e43b4b7dc7cc2a5853%2Fapi_bom.png?alt=media" alt=""><figcaption></figcaption></figure></div>

**API BOM** provides you with a detailed inventory of the API endpoints (both internal and external) defined in your application code. It identifies APIs:

* <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-09e6786f2070729388dafacd5d3d7c578f3ab966%2Fcode_icon.png?alt=media" alt="" data-size="original"> Directly referenced by your code.
* <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a79e7b0d56bb6eca610a4772fc86baa803249c27%2Fopenapi_icon.png?alt=media" alt="" data-size="original"> Defined by OpenAPI specification files in your repositories.

{% hint style="info" %}
**Why does it matter?**

1. **API BOM** gives you the ability to better understand your app exposure, making it easier to:
   * Ensure that all your APIs have undergone appropriate security review procedures. This is especially helpful in managing the review of newly added APIs.
   * Manage particularly risky elements of your APIs even when they are legitimately and intentionally included in code.
     * Consider, for example, an API containing a <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5643494805848a46a72b8a2ed056d2ba3001b915%2Fdelete_method_icon.png?alt=media" alt="" data-size="line"> method that could potentially alter your application or user data. At the very least, it's important to be aware that this method exists in your code so that you can manage potential risks.
2. **API BOM** allows you to prioritize issues exposed by APIs (which makes it more likely that there is a path for an attacker to exploit them).
   {% endhint %}

## Supported Languages

| Language                   | Web framework              | API detection | API/issue correlation¹ |
| -------------------------- | -------------------------- | ------------- | ---------------------- |
| OpenAPI specification file | –                          | Yes           | nan                    |
| Python                     | Flask                      | Yes           | Yes                    |
| Python                     | FastAPI                    | Yes           | Yes                    |
| Python                     | Django                     | Yes           | Yes                    |
| Python                     | Connexion                  | Yes           | Yes                    |
| JavaScript & TypeScript    | Express.js                 | Yes           | Yes                    |
| JavaScript & TypeScript    | NestJS                     | Yes           | Yes                    |
| JavaScript & TypeScript    | Koa                        | Yes           | Yes                    |
| JavaScript & TypeScript    | Apollo GraphQL             | Yes           | Yes                    |
| Java                       | SpringBoot                 | Yes           | Yes                    |
| Go                         | Gin                        | Yes           | nan                    |
| Scala                      | Play                       | Yes           | Yes                    |
| Scala                      | SpringBoot                 | Yes           | Yes                    |
| Kotlin                     | SpringBoot                 | Yes           | Yes                    |
| Kotlin                     | Ktor                       | Yes           | Yes                    |
| C#                         | Microsoft ASP.NET Core MVC | Yes           | Yes                    |

### **API/issue correlation**

**API BOM** maps specific **Code security** and **Open source security** issues to the APIs that expose them when **both** of the following conditions are met:

* <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-09e6786f2070729388dafacd5d3d7c578f3ab966%2Fcode_icon.png?alt=media" alt="" data-size="original"> The API is discovered in code.
* The API is written in a [language/web framework](https://gitlab.com/oxsecurity/ox-docs/docs/-/blob/main/a-tour-of-ox/broken-reference/README.md) for which this feature is supported.

**An issue is considered to be exposed by an API** when there is a function call path between the API handler function and the function containing the issue.

## Summary table

The API BOM **summary table** provides detailed information about each API discovered. A specific API (Title) is listed **once for each endpoint/method combination** it references.

In the **summary table:**

* Click on the title of any column to sort the table by that column. (By default, the table is sorted by **First seen**.)
* Use the filters on the left side of the page to view specific information in the table according to your preferences.
* Click the <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ec0b73c8d2ef577d1ae1c36d63d758904adf186b%2Fexport_button.png?alt=media" alt="Export" data-size="line"> button to export the full or filtered table as a CSV file.

### Summary table data

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-122fb5df99e6f9a3d15b0ce77cfab30be42fec43%2Fapi_bom_annotated.png?alt=media" alt=""><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80" align="center"></th><th></th></tr></thead><tbody><tr><td align="center"><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-efa7b1bc84e78ccfe97c7a1fb7904dae10fa0b91%2FA.png?alt=media" alt="" data-size="line"></td><td><p><strong>Title:</strong> The name of the API</p><ul><li><p><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-09e6786f2070729388dafacd5d3d7c578f3ab966%2Fcode_icon.png?alt=media" alt="" data-size="original"> <strong>For APIs discovered in code,</strong> the <strong>Title</strong> is the word <em>API</em> appended to the end of the application name (repository) in which the API is referenced<em>.</em></p><ul><li>For example, the <strong>Title</strong> of an API discovered in the <em>millennium-falcon</em> repository is <em>millennium-falcon API</em>.</li></ul></li><li><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a79e7b0d56bb6eca610a4772fc86baa803249c27%2Fopenapi_icon.png?alt=media" alt="" data-size="original"> <strong>For APIs discovered in OpenAPI specification files,</strong> the <strong>Title</strong> matches the title defined in the file.</li></ul></td></tr><tr><td align="center"><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-07b5299eaddf61b3b4ea19f71cb2f552d14284a9%2FB.png?alt=media" alt="" data-size="line"></td><td><p><strong>Highest severity exposed issues:</strong> The number of issues exposed by the API in each of the 3 highest severity levels.</p><ul><li>This column contains data only when the conditions for <a href="#api-issue-correlation">API/issue correlation</a> are met.</li><li>Click a circled number in the column <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3139fed3305adafdaf8658904cb149284034fc8e%2Fhighest_severity_issues_icon.png?alt=media" alt="" data-size="line"> to view the <a href="https://docs.ox.security/a-tour-of-ox/issues"><strong>Issues</strong></a> page pre-filtered by these issues.</li></ul></td></tr><tr><td align="center"><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0d07f58017690c1ac55e226f293d601ccd8cb2eb%2FC.png?alt=media" alt="" data-size="line"></td><td><strong>Endpoint:</strong> The URL of the endpoint referenced by the code or OpenAPI file.</td></tr><tr><td align="center"><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-00faf6595c357af93fd6522246707b464764d553%2FD.png?alt=media" alt="" data-size="line"></td><td><strong>Method:</strong> The HTTP method for the endpoint.</td></tr><tr><td align="center"><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-cf011be75a8af7fe193e112d78f0ce8402c7784a%2FE.png?alt=media" alt="" data-size="line"></td><td><p><strong>Functions:</strong> The functions called by the API.</p><ul><li>This column contains data only when the API was discovered in code <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-09e6786f2070729388dafacd5d3d7c578f3ab966%2Fcode_icon.png?alt=media" alt="" data-size="original">.</li><li>Click on a function link to view the function at its precise location in your code repository (in a new browser tab).</li></ul></td></tr><tr><td align="center"><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9e1d287453be6d87b158416a4b5a7e8052183d6d%2FF.png?alt=media" alt="" data-size="line"></td><td><p><strong>First seen:</strong> The date the API was first detected by OX.</p><ul><li>This is the date of first detection, not the date on which the API was added to the code.</li></ul></td></tr><tr><td align="center"><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-42c26bb3b171e04f06bbe96398038f909e920cb5%2FG.png?alt=media" alt="" data-size="line"></td><td><p><strong>Source:</strong></p><ul><li><p><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-09e6786f2070729388dafacd5d3d7c578f3ab966%2Fcode_icon.png?alt=media" alt="" data-size="original"> = API discovered in code.</p><ul><li>Click the icon to view the API reference at its precise location in your code repository (in a new browser tab).</li></ul></li><li><p><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a79e7b0d56bb6eca610a4772fc86baa803249c27%2Fopenapi_icon.png?alt=media" alt="" data-size="original"> = API discovered in OpenAPI specification file.</p><ul><li>Click the icon to view the OpenAPI file in your code repository (in a new browser tab). Note that this link takes you to the OpenAPI file, not to the specific line within the file that references the API.</li></ul></li></ul></td></tr><tr><td align="center"><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-92528544d63d0fa866d2575b39eaaf88fbee9d5d%2FH.png?alt=media" alt="" data-size="line"></td><td><p><strong>App name:</strong> The app (repository) in which the API is referenced.</p><ul><li>Click the link to view the app on the <a href="../scan-and-analyze-with-ox/analyzing-scan-results/applications"><strong>Active applications</strong></a> page.</li></ul></td></tr></tbody></table>

## API details

Select a row in the summary table to open **detailed API information** at the bottom of the page.

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2512fe00d12e9f60d86a315e996d234de1fb1fce%2Fapi_details_pane.png?alt=media" alt=""><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80" align="center"></th><th></th></tr></thead><tbody><tr><td align="center"><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-efa7b1bc84e78ccfe97c7a1fb7904dae10fa0b91%2FA.png?alt=media" alt="" data-size="line"></td><td><p>Click the <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2c4bda48544ed548d04b58135b0d196bbc79d38a%2Fexposed_code_issues_button.png?alt=media" alt="Exposed code issues" data-size="line"> button to view the <a href="https://docs.ox.security/a-tour-of-ox/issues"><strong>Issues</strong></a> page pre-filtered by the issues exposed by the API.</p><ul><li>This button is displayed when the conditions for <a href="#api-issue-correlation">API/issue correlation</a> are met.</li></ul></td></tr><tr><td align="center"><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-07b5299eaddf61b3b4ea19f71cb2f552d14284a9%2FB.png?alt=media" alt="" data-size="line"></td><td><p><strong>Tabs:</strong> Switch among tabs to navigate the types of detailed information available:</p><ul><li>The <strong>Exposed issue statistics</strong> tab is displayed when the conditions for <a href="#api-issue-correlation">API/issue correlation</a> are met.</li><li>The <strong>Parameters</strong> and <strong>Responses</strong> tabs are displayed when OX is able to detect this information for the API.</li></ul></td></tr></tbody></table>
