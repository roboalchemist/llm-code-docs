# Source: https://docs.readthedocs.com/platform/latest/visual-diff.html

# Visual diff[](#visual-diff "Link to this heading")

Get a list of documentation files that changed between the [[pull request]](pull-requests.html) and the latest version of the documentation, and see their differences highlighted visually on the documentation pages.

While seeing changes in source files is helpful, it can be difficult to understand how those changes will look in the rendered documentation, or their impact on the documentation as a whole. Read the Docs makes it easy to see the changes in the rendered documentation.

## Show diff menu in preview[](#show-diff-menu-in-preview "Link to this heading")

To enable or disable this feature for your project:

1.  Go the [Settings] tab of your project.

2.  Click on [Addons], and click on [Visual diff].

3.  Check or uncheck the [Enable visual diff] option.

4.  Click on [Save].

When enabled, a new UI element appears at the top right of the page showing a dropdown selector containing all the files that have changed in that pull request build.

<figure class="align-default">
<a href="_images/screenshot-viz-diff-ui.png" class="reference internal image-reference"><img src="_images/screenshot-viz-diff-ui.png" style="width: 80%;" alt="_images/screenshot-viz-diff-ui.png" /></a>
</figure>

You can select any of those files from the dropdown to jump directly into that page. Once there, you can toggle Visual Diff on and off by pressing the [Show diff] link from the UI element, or pressing the [`d`] key if you have hotkeys enabled.

Visual diff shows all the sections that have changed, highlighting their differences with red/green background colors. You can jump between each of these chunks by clinking on the up/down arrows.

### Show build overview in pull requests[](#show-build-overview-in-pull-requests "Link to this heading")

Note

This feature is only available for projects connected to a [[GitHub App]](reference/git-integration.html#github-app).

To enable or disable this feature for your project:

1.  Go the [Settings] tab of your project.

2.  Click on [Pull request builds].

3.  Check or uncheck the [Show build overview in a comment] option.

4.  Click on [Update].

When enabled, a comment is added to the pull request when changes are detected between the pull request and the latest version of the documentation.

<figure class="align-default">
<img src="_images/build-overview-comment.png" alt="_images/build-overview-comment.png" />
</figure>