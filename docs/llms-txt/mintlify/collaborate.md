# Source: https://www.mintlify.com/docs/editor/collaborate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Collaborate in the web editor

> Work together on documentation with branches, pull requests, and preview deployments.

Collaborate with your team on documentation using branch-based workflows, pull requests, and preview deployments.

If you aren't familiar with Git, see [Git concepts](/guides/git-concepts).

## Branch-based collaboration

Use branches to work on documentation updates in parallel without affecting your live site.

### Why use branches

* **Isolate changes**: Work on updates without affecting your live documentation.
* **Review before publishing**: Get feedback from team members before changes go live.
* **Parallel work**: Multiple team members can work on different branches simultaneously.

## Recommended workflow

Use pull requests to propose changes and collaborate with your team before merging to your live documentation. This workflow ensures your team reviews changes before publishing and maintains a clear history of updates.

<Steps>
  <Step title="Create a pull request">
    Create a pull request from the editor when you're ready to publish your changes. See <a href="/editor/publish">Publish changes in the web editor</a> for more information on using pull requests.
  </Step>

  <Step title="Review pull requests">
    Review pull requests in your Git provider like GitHub or GitLab.
  </Step>

  <Step title="Respond to feedback">
    When reviewers request changes, make the requested changes and save your changes. Additional changes automatically push to the existing pull request.
  </Step>

  <Step title="Merge pull requests">
    Merge your pull request after addressing all requested changes, required reviewers approve the pull request, and any automated checks pass.
  </Step>
</Steps>

## Preview deployments

Preview deployments create temporary URLs where you can see your changes before they go live.

### Access preview deployments

1. Click **Share** in the editor tool bar.
2. Click **Preview** to open the preview deployment in a new tab.
3. The preview URL shows your documentation with all saved changes applied.

<Frame>
  <img src="https://mintcdn.com/mintlify/fv0sH0FEeyPeiSH6/images/editor/share-preview-light.png?fit=max&auto=format&n=fv0sH0FEeyPeiSH6&q=85&s=d525d944b4f1fd68321f8370b24a58fc" className="block dark:hidden" alt="Share button in the editor toolbar" data-og-width="1188" width="1188" data-og-height="362" height="362" data-path="images/editor/share-preview-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/fv0sH0FEeyPeiSH6/images/editor/share-preview-light.png?w=280&fit=max&auto=format&n=fv0sH0FEeyPeiSH6&q=85&s=24ea0fce594cd080d02651fd8cef82dc 280w, https://mintcdn.com/mintlify/fv0sH0FEeyPeiSH6/images/editor/share-preview-light.png?w=560&fit=max&auto=format&n=fv0sH0FEeyPeiSH6&q=85&s=d6ea6a57e709673e9490479f794fa0fa 560w, https://mintcdn.com/mintlify/fv0sH0FEeyPeiSH6/images/editor/share-preview-light.png?w=840&fit=max&auto=format&n=fv0sH0FEeyPeiSH6&q=85&s=06fa1abf0e27e1e6a8ee3e6aaaa80d3d 840w, https://mintcdn.com/mintlify/fv0sH0FEeyPeiSH6/images/editor/share-preview-light.png?w=1100&fit=max&auto=format&n=fv0sH0FEeyPeiSH6&q=85&s=2ff3da402471059370d7e2557d7094e9 1100w, https://mintcdn.com/mintlify/fv0sH0FEeyPeiSH6/images/editor/share-preview-light.png?w=1650&fit=max&auto=format&n=fv0sH0FEeyPeiSH6&q=85&s=86d602c52b2e5edec484d6cf944a351f 1650w, https://mintcdn.com/mintlify/fv0sH0FEeyPeiSH6/images/editor/share-preview-light.png?w=2500&fit=max&auto=format&n=fv0sH0FEeyPeiSH6&q=85&s=a52b98fc0373122de4effebfe3281162 2500w" />

  <img src="https://mintcdn.com/mintlify/fv0sH0FEeyPeiSH6/images/editor/share-preview-dark.png?fit=max&auto=format&n=fv0sH0FEeyPeiSH6&q=85&s=7f06c3db7134f80d0727264c9df7c153" className="hidden dark:block" alt="Share button in the editor toolbar" data-og-width="1190" width="1190" data-og-height="364" height="364" data-path="images/editor/share-preview-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/fv0sH0FEeyPeiSH6/images/editor/share-preview-dark.png?w=280&fit=max&auto=format&n=fv0sH0FEeyPeiSH6&q=85&s=7d873529936cfd7451d84c99b3aaf724 280w, https://mintcdn.com/mintlify/fv0sH0FEeyPeiSH6/images/editor/share-preview-dark.png?w=560&fit=max&auto=format&n=fv0sH0FEeyPeiSH6&q=85&s=90e5a356f8cc65ff51f9287b0fddfdcf 560w, https://mintcdn.com/mintlify/fv0sH0FEeyPeiSH6/images/editor/share-preview-dark.png?w=840&fit=max&auto=format&n=fv0sH0FEeyPeiSH6&q=85&s=1fc0407015adb4d4194d16cb95bc9b45 840w, https://mintcdn.com/mintlify/fv0sH0FEeyPeiSH6/images/editor/share-preview-dark.png?w=1100&fit=max&auto=format&n=fv0sH0FEeyPeiSH6&q=85&s=2e95e4443d7b9162b48ad44cf6140ef7 1100w, https://mintcdn.com/mintlify/fv0sH0FEeyPeiSH6/images/editor/share-preview-dark.png?w=1650&fit=max&auto=format&n=fv0sH0FEeyPeiSH6&q=85&s=e8a4ae4c8a350e3b7da52092d0355d21 1650w, https://mintcdn.com/mintlify/fv0sH0FEeyPeiSH6/images/editor/share-preview-dark.png?w=2500&fit=max&auto=format&n=fv0sH0FEeyPeiSH6&q=85&s=d74972a4ddd11eadbc4d477a0e5f416c 2500w" />
</Frame>

### Share previews

Share the preview deployment URL with team members to gather feedback. Previews update automatically when you save additional changes.

### Preview authentication

Preview URLs are publicly accessible by default. Enable preview authentication in the [Add-ons](https://dashboard.mintlify.com/products/addons) page of your dashboard to restrict access to authenticated organization members.
