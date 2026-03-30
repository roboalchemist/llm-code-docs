# Source: https://redocly.com/docs/realm/reunite/project/pull-request/open-pull-request.md

# Open a pull request in Reunite

To update your published project in Reunite, open a pull request to merge your development branch with the main branch.

## Before you begin

Make sure you have the following:

- [a new branch](/docs/realm/reunite/project/use-editor#create-a-new-branch) with [commits or updates](/docs/realm/reunite/project/use-editor#commit-updates).


## Open a draft pull request

Pull requests run checks to be sure you are not adding syntax issues or broken links to the production build, create a preview build, and give other users an opportunity to comment on the changes before they are merged with the main branch.

To open a draft pull request:

1. Click the **Create pull request icon**, or the **Create pull request** button on the **Commit** tab.

2. (Optional) In the page that opens:
  - Edit the **Title** to your preference, By default, Reunite uses the first commit message.
  - Provide a short description for the pull request.
3. Click the **Create pull request** button.



After creating your draft pull request, you can continue committing changes to your branch until it is either closed or merged.

Before you merge your updates with the main branch, review them to be sure they contain what you expect.

## Pull request workflows

When your changes are ready to be reviewed, you should [update the pull request's state](/docs/realm/reunite/project/pull-request/manage-pull-requests#update-state) to **Ready for review** and assign reviewers.
This notifies the team that there is a pull request awaiting their attention.

The reviewers will approve the pull request if they agree that the changes are ready to merge.
Once there are approving reviews, the [pull request can be merged](/docs/realm/reunite/project/pull-request/review-pull-request#merge-a-pull-request), bringing your changes into the main branch of the project.

If you no longer want to continue working on a pull request and you do not want it merged with main, you can click the **Close pull request button**.
If you change your mind about that pull request later, you can click the **Reopen pull request** button.

## Resources

- **[Using the editor](/docs/realm/reunite/project/use-editor)** - Create and edit content in Markdown and Markdoc with Reunite's collaborative editing tools and syntax highlighting
- **[Reunite platform overview](/docs/realm/reunite/reunite)** - Explore the features and capabilities of Reunite, Redocly's collaborative content management platform
- **[Reunite configuration reference](/docs/realm/config/reunite)** - Configure Reunite deployment settings including options to publish builds with broken links or syntax issues