# Source: https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/set-up-insights/set-up-insights-associating-snyk-open-source-code-and-container-projects.md

# Set up Insights: associating Snyk Open Source, Code, and Container Projects

After you have set up insights, Snyk can set up the required linking for the chosen application.

To prioritize your Snyk Code and Snyk Open Source vulnerabilities, Snyk needs to understand the relationships between those imported Snyk Projects and the Container Project. Snyk uses the relationships between these Projects as a proxy to understand the composition of the container image.

The Set up Insights UI displays a variety of asset types, including but not limited to:

* Repository assets
* Packages
* Container images
* Scanned artifacts

These assets are directly linked to the ones displayed on the [Snyk Inventory](https://docs.snyk.io/manage-assets/assets-inventory-components) view.

{% hint style="info" %}
For more details regarding supported assets, you can navigate to the [Asset](https://docs.snyk.io/manage-assets/assets-inventory-components#asset) and [Issue](https://docs.snyk.io/manage-assets/assets-inventory-components#issues) pages.
{% endhint %}

The container image is the build artifact that is deployed and running on your Kubernetes cluster, so Snyk can map your application from its source code to its deployed state by understanding the following:

* The link between the Source Code and Open Source Dependencies and the image.
* What images are deployed to Kubernetes, and how are they configured.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ff3ba524b00b6d4c5f5dd8ffdeda8bcd7efcb597%2FAssociating%20Snyk%20OS%2C%20Code%20and%20Container%20projects.png?alt=media" alt="Mapping your application"><figcaption><p>Mapping your application</p></figcaption></figure>

## Use Project tags to link Projects

Add Snyk [Project tags](https://docs.snyk.io/snyk-platform-administration/snyk-projects/project-tags) to all the Projects used by your application to link these Projects together and allow Snyk to represent the whole application that you are testing.

To associate two Projects together, add the exact same tag to both Projects. For example, add the same tag to your Snyk Open Source Projects and Snyk Container Project if they are related to each other.

See the examples at the end of this section.

## Requirements for Project tags

* The same tag must be applied to the container image and Code or Open Source Projects,
* The tag must follow the specified format,
* The Projects do not have to be in the same Snyk Organization to be mapped but must be in the same Snyk Group,

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-d41aac64f35775117f16b1c587bf8059be93e729%2FScreenshot%202023-06-06%20at%2023.29.29.png?alt=media" alt="Project tags"><figcaption><p>Project tags</p></figcaption></figure>

## Examples of Project tags

### **Single repo to a single image**

In this example, a single repository contains your package.json, which is built into an image called image-A.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-d06e8bc658c0b37623612814dca59d9d3e49844b%2FExample%20-%20Single%20repo%20Single%20image.png?alt=media" alt="Example: single repo to single image"><figcaption><p>Example: single repo to single image</p></figcaption></figure>

To map these associations, you would have the following tags set up:

<table><thead><tr><th width="165">Location</th><th width="161">Asset</th><th width="213">Snyk Project Location</th><th width="238">Tag(s)</th><th>Notes</th></tr></thead><tbody><tr><td>github.com/my-team/front-end</td><td><code>package.json</code></td><td><p>Snyk Org: my-team</p><p><br>Project name: package.json</p></td><td><code>component=pkg:github/my-team/front-end@main</code></td><td>The same tag is applied to both sides</td></tr><tr><td><br></td><td>Built container image called <code>image-A</code></td><td><p>Snyk Org: my-team<br></p><p>Project name: image-A</p></td><td><code>component=pkg:github/my-team/front-end@main</code></td><td></td></tr></tbody></table>

### **Multiple repos to a single image**

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-7339c1834e944cd2a55c5b1af3191595ade2ddd9%2FExample%20-%20Multiple%20repos%20Single%20image.png?alt=media" alt="Example: multiple repos to single image"><figcaption><p>Example: multiple repos to single image</p></figcaption></figure>

For this scenario, there are two contributing repositories.

There is a front-end repository containing the package.json scanned by Snyk Open Source and a back-end repository containing go code scanned by Snyk Code.

To map these associations, you would have the following tags set up:

<table><thead><tr><th width="180">Location</th><th>Asset</th><th>Snyk Project Location</th><th>Tag(s)</th><th>Notes</th></tr></thead><tbody><tr><td>github.com/my-team/front-end</td><td><code>package.json</code></td><td><p>Snyk Org: my-team</p><p><br></p><p>Project name: package.json</p></td><td><code>component=pkg:github/my-team/front-end@main</code></td><td><br></td></tr><tr><td>github.com/my-team/back-end</td><td><code>Go source code</code></td><td><p>Snyk Org: my-team</p><p><br></p><p>Project name: Code</p></td><td><code>component=pkg:github/my-team/back-end@main</code></td><td><br></td></tr><tr><td><br></td><td>Built container image called <code>image-A</code></td><td><p>Snyk Org: my-team</p><p><br></p><p>Project name: image-A</p></td><td><p><code>component=pkg:github/my-team/front-end@main</code></p><p><code>component=pkg:github/my-team/back-end@main</code></p></td><td><p>The image has two tags applied, as there are two upstream dependencies which have different tags.<br></p><p>You can apply multiple tags to an image.</p></td></tr></tbody></table>

### **Monorepo to many images**

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-15854970f68ec2bb81f314ac8f49549aefb7a953%2FExample%20-%20Multiple%20repos%20Single%20image-2.png?alt=media" alt="Example: monorepo to multiple images"><figcaption><p>Example: monorepo to multiple images</p></figcaption></figure>

In this example, the application team is using a monorepo approach. The contents of the repository are built into different container images as they may be run separately.

Here, we need to further differentiate the tags by scoping them more accurately.

<table><thead><tr><th>Location</th><th width="168">Asset</th><th>Snyk Project Location</th><th>Tag(s)</th><th></th></tr></thead><tbody><tr><td>github.com/my-team/service</td><td><code>package.json</code></td><td><p>Snyk Org: my-team</p><p><br></p><p>Project name: package.json</p></td><td><code>component=pkg:github/my-team/service/front-end@main</code></td><td>The tag is further scoped by specifying /front-end at the end</td></tr><tr><td><br></td><td>Built container image called <code>my-app-frontend:latest</code></td><td><p>Snyk Org: my-team</p><p><br></p><p>Project name: my-app-frontend:latest</p></td><td><code>component=pkg:github/my-team/service/front-end@main</code></td><td></td></tr></tbody></table>

<table><thead><tr><th width="161">Location</th><th>Asset</th><th>Snyk Project Location</th><th>Tag(s)</th><th>Notes</th></tr></thead><tbody><tr><td>github.com/my-team/service</td><td><code>Go source code</code></td><td><p>Snyk Org: my-team</p><p><br></p><p>Project name: Code</p></td><td><code>component=pkg:github/my-team/service/back-end@main</code></td><td>The tag is further scoped by specifying /back-end at the end</td></tr><tr><td><br></td><td>Built container image called <code>my-app-backend:latest</code></td><td><p>Snyk Org: my-team</p><p><br></p><p>Project name: my-app-backend:latest</p></td><td><code>component=pkg:github/my-team/service/back-end@main</code></td><td></td></tr></tbody></table>

## Tags application

Project Tags can be applied as follows:

<table><thead><tr><th width="185.33333333333331">Product</th><th width="197">Method</th><th>Project Source</th></tr></thead><tbody><tr><td>Snyk Code</td><td><ul><li>API</li><li>UI</li></ul></td><td><p>For projects created by</p><ul><li>Git Import</li></ul></td></tr><tr><td>Snyk Open Source</td><td><ul><li>API</li><li>UI</li><li>CLI</li></ul></td><td><p>For projects created by</p><ul><li>Git Import</li><li>CLI Monitor</li></ul></td></tr><tr><td>Snyk Container</td><td><ul><li>API</li><li>UI</li><li>CLI</li></ul></td><td><p>For projects created by</p><ul><li>Git Import</li><li>CLI Monitor</li><li>Container Registry Integration</li></ul></td></tr></tbody></table>

{% hint style="info" %}
Snyk recommends applying the tags through the API in order to automate the process. For more information, see the endpoint [Add a tag to a project](https://docs.snyk.io/snyk-api/reference/projects-v1#org-orgid-project-projectid-tags).
{% endhint %}

## UI example for Project tags

<div align="center"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-99115a84f51c567990f2f5c2d8ca68cca22200d9%2FuiExample.png?alt=media" alt="UI example for Project tags"><figcaption><p>UI example for Project tags</p></figcaption></figure></div>

### CLI Example

`snyk monitor --project-tags=component=pkg:github/my-team/back-end@main`

### API Example

See the [Project Update documentation](https://docs.snyk.io/snyk-api/reference/projects-v1#org-orgid-project-projectid).

Example:

```
 "tags": [
    {
      "key": "component",
      "value": "pkg:github/my-team/back-end@main"
    }
  ],
```

{% hint style="info" %}
To ensure you have set up your Kubernetes Connector properly, navigate to the **Set up Insights** tab on the **Insights** page and check the **Image composition** section to view the data Insights has access to.
{% endhint %}
