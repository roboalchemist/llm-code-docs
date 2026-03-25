# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/understanding-pipeline-scan-results/pipeline-issues.md

# Pipeline Issues

The Pipeline Issues page presents all the issues found during pipeline scans with the actions Block, Alert, and Discovered.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3c2f1188975323892977b64e7d8074e70425d358%2FPipeline_Issues_full.png?alt=media" alt=""><figcaption></figcaption></figure>

Pipeline issues include an additional status field that does not exist in the Active Issues page:

* **New**: Issue did not appear in previous scans.
* **Old**: Issue already exists in the Active Issues page.

You can configure [pipeline workflows](https://docs.ox.security/automate-with-ox-workflows/pipeline-workflows) to react differently to new vs. old issues.
