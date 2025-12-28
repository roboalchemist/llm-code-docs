# Source: https://docs.readthedocs.com/platform/latest/pull-requests.html

# Pull request previews[](#pull-request-previews "Link to this heading")

Your project can be configured to build and preview documentation for every new pull request. Previewing changes during review makes it easier to catch formatting and display issues before they go live.

## Features[](#features "Link to this heading")

Build on pull request events

:   We create and build a new version when a pull request is opened, and rebuild it whenever a new commit is pushed.

Build status report

:   Your project's pull request build status will show as one of your pull request's checks. This status will update as the build is running, and will show a success or failure status when the build completes.

    <figure id="id1" class="align-center" style="width: 80%">
    <img src="_images/github-build-status-reporting.gif" alt="GitHub build status reporting for pull requests." />
    <figcaption><p><span class="caption-text">GitHub build status reporting</span><a href="#id1" class="headerlink" title="Link to this image"></a></p></figcaption>
    </figure>

Build overview with changed files

:   We create a comment on the pull request including a link to the preview of the documentation, and a list of the [[files that changed]](visual-diff.html) between the current pull request and the latest version of the project's documentation.

    ::: 
    Note

    This feature is only available for projects connected to a [[GitHub App]](reference/git-integration.html#github-app).
    :::

Pull request notifications

:   A pull request notifications is shown at the top of preview pages, which let readers know they aren't viewing an active version of the project.

[[Visual diff]](visual-diff.html)

:   Visual diff shows proposed changes by visually highlighting the differences between the current pull request and the latest version of the project's documentation.

    Press [`d`] to toggle between Visual diff and normal pull request preview.

See also

[[How to configure pull request builds]](guides/pull-requests.html)

:   A guide to configuring pull request builds on Read the Docs.