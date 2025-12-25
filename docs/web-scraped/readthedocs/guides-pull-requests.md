# Source: https://docs.readthedocs.com/platform/latest/guides/pull-requests.html

# How to configure pull request builds[](#how-to-configure-pull-request-builds "Link to this heading")

In this section, you can learn how to configure [[pull request builds]](../pull-requests.html).

To enable pull request builds for your project, your Read the Docs project needs to be connected to a repository from a supported Git provider. See [Limitations](#limitations) for more information.

1.  Go to your project dashboard

2.  Go to [Settings], then [Pull request builds]

3.  Enable the [Build pull requests for this project] option

4.  Click on [Update]

Tip

Pull requests opened before enabling pull request builds will not trigger new builds automatically. Push a new commit to the pull request to trigger its first build.

## Privacy levels[](#privacy-levels "Link to this heading")

Note

Privacy levels are only supported on [[Business hosting]](../commercial/index.html).

If you didn't import your project manually and your repository is public, the privacy level of pull request previews will be set to *Public*, otherwise it will be set to *Private*. Public pull request previews are available to anyone with the link to the preview, while private previews are only available to users with access to the Read the Docs project.

Warning

If you set the privacy level of pull request previews to *Private*, make sure that only trusted users can open pull requests in your repository.

Setting pull request previews to private on a public repository can allow a malicious user to access read-only APIs using the user's session that is reading the pull request preview. Similar to [GHSA-pw32-ffxw-68rh](https://github.com/readthedocs/readthedocs.org/security/advisories/GHSA-pw32-ffxw-68rh).

To change the privacy level:

1.  Go to your project dashboard

2.  Go to [Settings], then [Pull request builds]

3.  Select your option in [Privacy level of builds from pull requests]

4.  Click on [Update]

Privacy levels work the same way as [[normal versions]](../versions.html#version-states).