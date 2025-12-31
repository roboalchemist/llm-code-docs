# Source: https://mintlify.com/docs/editor/publish.md

# Publish changes in the web editor

> Save your work and publish changes to your documentation site.

## Publishing workflows

The editor supports two workflows for publishing documentation updates. The workflow you use depends on your repository's branch protection rules and the branch you work on.

If your repository has branch protection rules requiring review, the editor creates a pull request. Team members can review your changes before they go live. For collaboration workflows and team review processes, see [Collaborate](/editor/collaborate).

If there are no protection rules, your changes merge to the deployment branch and deploy immediately.

| Branch type                                                                                                                                              | Branch protection      | What happens when you publish                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ----------------------------------------------- |
| <Tooltip headline="Deployment branch" tip="The branch that publishes to your live documentation site, typically 'main'.">Deployment branch</Tooltip>     | None                   | Commits and deploys changes                     |
| Deployment branch                                                                                                                                        | Pull requests required | Creates a pull request                          |
| <Tooltip headline="Feature branch" tip="An isolated branch where you work on updates before merging to your deployment branch.">Feature branch</Tooltip> | None                   | Merges changes to deployment branch and deploys |
| Feature branch                                                                                                                                           | Pull requests required | Creates a pull request                          |

<Tip>
  Configure branch protection rules in your Git provider to require pull requests. See [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) in the GitHub docs or [Protected branches](https://docs.gitlab.com/user/project/repository/branches/protected/) in the GitLab docs.
</Tip>

## Save changes

As you edit, the editor tracks your changes.

* New or deleted files.
* Content edits in pages.
* Navigation structure changes.
* Media uploads and organization.
* Configuration updates.

<Frame>
  <img src="https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-light.png?fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=efde7a0f763db2116c4ee8ee2189c031" alt="Web editor toolbar showing one pending change." className="block dark:hidden" data-og-width="884" width="884" data-og-height="84" height="84" data-path="images/editor/toolbar-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-light.png?w=280&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=ac883fedaf1a089036caa686abb256d3 280w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-light.png?w=560&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=909b439184d2253b21d0f44343cbc835 560w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-light.png?w=840&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=57f77d31e7486f3b2cda7af1c255b369 840w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-light.png?w=1100&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=0f0f92d9ce2619fe01d675724940bb4d 1100w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-light.png?w=1650&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=44eeaca68a144e4824c116509fb99029 1650w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-light.png?w=2500&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=9ff89b91f29406c65bced9ac800da277 2500w" />

  <img src="https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-dark.png?fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=1687db26e20f029dee0e824cdf45ee1c" alt="Web editor toolbar showing one pending change." className="hidden dark:block" data-og-width="884" width="884" data-og-height="84" height="84" data-path="images/editor/toolbar-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-dark.png?w=280&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=a82d959b6fa0b079d916ddc3eec07833 280w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-dark.png?w=560&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=7f33e4fdc6122be0aa3533f5a098c1d7 560w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-dark.png?w=840&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=8bfa95ed184d0bab4fd0c927e4e53b9d 840w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-dark.png?w=1100&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=300ce440f7bef0201921ec32047ecf84 1100w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-dark.png?w=1650&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=93f10616482705e42e0a6579684df811 1650w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-dark.png?w=2500&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=1fbecfc0d7459e7947af156c2cabfe96 2500w" />
</Frame>

When you work on your deployment branch, changes are saved automatically.

When you work on a feature branch, you can save changes to the branch as <Tooltip headline="Commit" tip="A commit is a saved snapshot of your changes in Git.">commits</Tooltip>.

<Frame>
  <img src="https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-branch-light.png?fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=42bdbeaea7772e86fd6cdac02e415c74" alt="Web editor toolbar showing one pending change and the Save as commit button on a feature branch." className="block dark:hidden" data-og-width="1180" width="1180" data-og-height="84" height="84" data-path="images/editor/toolbar-branch-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-branch-light.png?w=280&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=c0105392ba81ac9564ea039307bf7384 280w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-branch-light.png?w=560&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=a912d5a2caa6f328c05252a142e7d1d9 560w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-branch-light.png?w=840&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=27034b7d7234602425a66630b4989d61 840w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-branch-light.png?w=1100&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=f541274f5a1f26574e8cefff93d607ee 1100w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-branch-light.png?w=1650&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=58852b07ceb4e060044187f008d33f29 1650w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-branch-light.png?w=2500&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=7bc7260e294c42668576a874b8770ae5 2500w" />

  <img src="https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-branch-dark.png?fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=67fc18a74266c7974bf278e8f6d5b2d0" alt="Web editor toolbar showing one pending change and the Save as commit button on a feature branch." className="hidden dark:block" data-og-width="1180" width="1180" data-og-height="84" height="84" data-path="images/editor/toolbar-branch-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-branch-dark.png?w=280&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=f3c7b5e9107a20633953d0e999aecd23 280w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-branch-dark.png?w=560&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=8e826cf75173f726ed98ec764131c712 560w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-branch-dark.png?w=840&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=5917f831cd4a588f9da39d5b40411ba4 840w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-branch-dark.png?w=1100&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=df4425001747c7beb203dc734dc15441 1100w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-branch-dark.png?w=1650&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=d13cd6d9ae0f23eda9ab6c5983ac2931 1650w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/toolbar-branch-dark.png?w=2500&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=1787d4bb987875bdef44bbb48893d4d6 2500w" />
</Frame>

To discard changes, click **Undo changes** beside a file name in the **Changes** dropdown.

### Publish your changes

If you are on your deployment branch, click **Publish** in the toolbar. Depending on your workflow, your changes are live as soon as your site redeploys or create a pull request and merge it in your Git provider.

If you are on a feature branch, save your changes and then click **Publish** in the toolbar. Depending on your workflow, your changes are live as soon as your site redeploys or create a pull request and merge it in your Git provider.

## Resolve conflicts

Conflicts occur when your branch and the deployment branch have incompatible changes to the same files.

### What causes conflicts

Conflicts happen when:

* You and another team member edit the same lines in a file.
* Files are moved or deleted in one branch but modified in another.

### Resolve conflicts

The editor displays warnings when conflicts prevent operations like publishing or switching branches. To resolve conflicts, follow the instructions in the editor to choose which changes to keep.

## Commit signing

Sign commits with your GitHub account by authorizing it in your [account settings](https://dashboard.mintlify.com/settings/account). Without authorization, the Mintlify GitHub App signs commits made in the web editor.

Attributing commits to your account maintains an accurate history of who made changes to your documentation.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://mintlify.com/docs/llms.txt