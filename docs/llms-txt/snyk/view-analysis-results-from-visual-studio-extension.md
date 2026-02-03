# Source: https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-extension/view-analysis-results-from-visual-studio-extension.md

# View analysis results from Visual Studio extension

## Issues display in the Visual Studio extension

You can filter vulnerabilities by name or by severity.

Filter by name by typing the name of the vulnerability in the search bar.

![Filter by name](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-4589169c8b654c1d54b1eadc8e552dd2751968db%2Freadme_image_3_2_1.png?alt=media\&token=6d91fcb0-9b09-4781-8246-d6236a7d9e36)

Filter by severity by selecting one or more of the severities when you open the search bar filter.

![Filter by severity](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-4aa22178ab2489625cc60c4170b0b1cc8e80f7ff%2Freadme_image_3_2_2.png?alt=media\&token=ed544fe9-e5c2-49c7-9669-97976a840216)

Users can configure the Snyk extension using the **Solution settings** in the **Options**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1d32614715cb581b5cc7bdc6765af51332cc0c3c%2Fimage%20(41).png?alt=media" alt=""><figcaption><p>Add the -d parameter in the Solution settings</p></figcaption></figure>

## Net new Issues versus all issues

For Projects using Git repositories or when you specify a reference folder, Snyk can filter the displayed issues to show only issues introduced in the working branch.

This functionality reduces noise and allows you to focus only on current changes. This helps prevent issues early, thus unblocking your CI/CD pipeline and speeding up your deliveries.

The logic uses your local Git repository or any folder to compare the current findings with those in a base branch or reference folder. Net new issues scanning (delta scanning) shows you the difference between the two branches or folders, highlighting only the new issues.

In version 2.1.0 and later, you can choose **any folder** as your base for scanning.

To apply the filter and only see the new issues, use the **total/new** toggle in the summary panel.

<div align="center" data-full-width="false"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-fc3ff2f8c95e932d950d630a22e65ab9d70cb17b%2Fimage.png?alt=media" alt="" width="375"><figcaption><p>Toggle in summary panel to show the total number of issues<br>and the number of issues in the checked out branch or current folder</p></figcaption></figure></div>

You can also enable net new issues feature in the [scan settings](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-extension-configuration-environment-variables-and-proxy#scan-configuration) for the Visual Studio extension.

For newly created feature branches, there will be no reported issues. That is an intended state that developers would aim for, as shown in the screen image that follows:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3c8a6a7aac34c2cfe897ee4f5f3e8d0f6e01b36b%2Fimage.png?alt=media" alt="" width="481"><figcaption><p>Successful state, no net new issiues found</p></figcaption></figure>

## Changing the base branch

The base branch is usually determined automatically for each Git repository.

You can change the base branch or base folder by following these steps, as illustrated in the screen image that follows:

1. Toggle the total/new filter in the summary panel
2. Click on the top-level node in the Issues tree to change the branch or directory.
3. Use the dropdown selection to choose any branch or reference folder.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ce66510927854990b304f3ca41b33c982bc52a9d%2Fimage.png?alt=media" alt=""><figcaption><p>Change the reference branch or reference directory for calculation of new new issues.</p></figcaption></figure>
