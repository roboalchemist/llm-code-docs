# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/getting-started/git-sync/commits.md

# Source: https://gitbook.com/docs/documentation/zh/getting-started/git-sync/commits.md

# Source: https://gitbook.com/docs/documentation/fr/getting-started/git-sync/commits.md

# Source: https://gitbook.com/docs/getting-started/git-sync/commits.md

# Commit messages & Autolink

By default, when exporting content from GitBook to the Git repository, GitBook will generate a commit message based on the merged change request:

```
GITBOOK-14: Improve documentation about users management
```

## Autolink `GITBOOK-<num>` in GitHub and GitLab

If you want to automatically resolve your GitBook change request IDs (e.g. *GITBOOK-123*) in commits to links, you can enable this using GitHub’s *Autolink references* feature. See instructions on [GitHub](https://help.github.com/en/github/administering-a-repository/configuring-autolinks-to-reference-external-resources).

Use the following URL format, where `spaceId` corresponds to your space’s URL:

`<https://app.gitbook.com/s/{spaceId}/~/changes/<num>/`

<div data-full-width="false"><figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FXMOX8gtwZIZGwdSWhSdX%2Fgitsync-autolink%402x.png?alt=media&#x26;token=bebbbb78-1a5f-4e90-af21-29803b3d2a7a" alt="A GitBook screenshot showing autolink setup"><figcaption><p>Autolink setup.</p></figcaption></figure></div>

## Customize the commit message template

When using GitBook with a [monorepo](https://gitbook.com/docs/getting-started/git-sync/monorepos), or when you have specific guidelines for commit messages; you might want to customize the message used by GitBook when pushing a commit to Git.

The template can contain the following placeholders:

* `{change_request_number}` unique numeric ID for the change request
* `{change_request_subject}` the subject of the change request when merged, or `No subject` if none has been provided.

The default template is:

```
GITBOOK-{change_request_number}: {change_request_subject}
```
