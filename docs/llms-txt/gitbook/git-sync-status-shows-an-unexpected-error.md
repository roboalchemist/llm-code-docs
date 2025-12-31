# Source: https://gitbook.com/docs/help-center/integrations/integrations-troubleshooting/git-sync/git-sync-status-shows-an-unexpected-error.md

# Git Sync status shows an unexpected error

### When I was merging a change request from GitBook

Please try creating a new change request in GitBook with a small change, such as adding a word or space somewhere in your documentation. Merging this change request should retrigger sync and GitBook will export your content again.

When doing this new export, all content will be exported again, including the previous sync where the error happened.

### When I was merging a commit from GitHub/GitLab

Please try creating a new commit in your repository with a small change, such as adding a word somewhere in your documentation. When this commit is merged, GitBook will attempt to import your content again as the sync process will be retriggered.

When doing this new commit, all content from your repository will be imported again, including the previous sync where the error happened.

### When I was trying to set up Git Sync for the first time

Please remove the integration you are using (GitLab or GitHub) and enable it again in your space. Please go through the setup process one more time.

If the steps mentioned above do not prove to be helpful, kindly get in touch with our support team.
