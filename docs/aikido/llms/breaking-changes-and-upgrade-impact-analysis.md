# Source: https://help.aikido.dev/aikido-autofix/breaking-changes-and-upgrade-impact-analysis.md

# Breaking changes & upgrade impact analysis

## Breaking changes

Aikido makes an assessement on whether a version upgrade contains breaking changes by looking at the changelogs of the library.

Clicking on an open-source dependency issue in the Aikido feed will pop up the issue details showing the minimal version upgrade required to fix the issue. In this Spring Security example below, CVE-2023-34034 will be fixed by upgrading from version 6.1.0 to version 6.1.2. Aikido has determined that there are no breaking changes in this update, shown by the :white\_check\_mark:.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FKzC86WzHfyEhVpEAXPQO%2Fimage.png?alt=media&#x26;token=538afb5b-237e-43c9-bebb-01690d824db3" alt=""><figcaption></figcaption></figure>

Clicking the :white\_check\_mark: reveals the details and a link to the changelogs. In this case there are no breaking changes.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FUEA7g7RsdVkv6gq1B0Z0%2Fimage.png?alt=media&#x26;token=22d5abf8-e224-4d25-b9c6-a13378aaad9d" alt=""><figcaption></figcaption></figure>

If there are breaking changes like for this Tomcat upgrade from version 8.5.11 to version 9.0.99, Aikido shows a :warning: icon.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FSvsK6sGusieCv2lXc071%2Fimage.png?alt=media&#x26;token=533036a9-21d9-4026-87c7-fb80d83199f6" alt=""><figcaption></figcaption></figure>

Clicking the :warning: reveals a description of the breaking changes and a link to the changelog.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FD5297nrqJQ3CxPJxq7dY%2Fimage.png?alt=media&#x26;token=95cf6ff2-1c6e-4ea5-b67d-f5ba57be02a6" alt=""><figcaption></figcaption></figure>

## Upgrade impact analysis

Even if there are breaking changes in the dependency update, this does not mean your code is affected by these changes. The breaking changes could be in a function that is not used in your codebase. Upgrade impact analysis goes one step further by scanning the codebase for usages of the library to determine whether the breaking changes are impacting your codebase.

Aikido AutoFix performs upgrade impact analysis when a pull request is created. The description of the pull request will contain the result of the analysis, falling into 1 of these 3 categories:

* There are no breaking changes in the library upgrade :white\_check\_mark:
* There are breaking changes but they are not affecting your codebase :white\_check\_mark:
* There are breaking changes that affect your codebase, manual mitigation is required :warning:

In the example below mongoose is updated from version 5.13.21 to 6.13.6. The pull request shows there are 2 breaking changes affecting the codebase and outlines which files are affected and what the impact is:

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FWHFiFQpJLockgP99Y9i6%2Fimage.png?alt=media&#x26;token=a7769cde-4757-4893-983c-c6048d30ef39" alt=""><figcaption></figcaption></figure>
