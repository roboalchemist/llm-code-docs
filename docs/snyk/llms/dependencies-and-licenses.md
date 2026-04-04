# Source: https://docs.snyk.io/manage-risk/reporting/dependencies-and-licenses.md

# Dependencies and licenses

You can [view dependencies](https://docs.snyk.io/manage-risk/reporting/dependencies-and-licenses/view-dependencies) and [license information](https://docs.snyk.io/manage-risk/reporting/dependencies-and-licenses/view-licenses) for all Projects in your Group or Organization using the **Dependencies** option in your Group or Organization menu:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-faecc94f0233a35180f72ab817dc68014d298740%2FScreenshot%202023-05-11%20at%2012.45.48.png?alt=media" alt="Dependencies tab for an Organization"><figcaption><p>Dependencies tab for an Organization</p></figcaption></figure>

{% hint style="info" %}
When you import or re-test a Project, changes will be reflected on the **Dependencies** UI after a ten-second delay.
{% endhint %}

For both dependencies and licenses, you can filter by Project or other filter criteria:

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ba34bd0e94d943e2d2184d08034219aa38cd3a68%2FScreenshot%202023-05-11%20at%2013.11.22.png?alt=media" alt="Select Projects and filters"><figcaption><p>Select Projects and filters</p></figcaption></figure></div>

* From the **Projects** dropdown, select specific Projects.
* From the **Filters** dropdown, check the applicable boxes to filter by [Severity level](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/severity-levels) or Project type.

{% hint style="info" %}
Results from the Dockerfile Project type are filtered out by default in the filter criteria as they can result in duplication of results from scans of the images resulting from building the Dockerfiles. To match results from [AP](https://docs.snyk.io/snyk-api/reference/reporting-api-v1)I calls, either filter out Dockerfiles from the API results or turn on Dockfiles in the Project type column of the filter.
{% endhint %}
