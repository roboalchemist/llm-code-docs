# Source: https://gitbook.com/docs/help-center/integrations/integrations-troubleshooting/git-sync/nothing-happens-on-gitbook-after-adding-a-new-file-to-my-repository.md

# ​Nothing happens on GitBook after adding a new file to my repository

{% hint style="warning" %}
**This section specifically addresses problems when a `SUMMARY.md` file already exists**

If your repository does not include a `SUMMARY.md` file, GitBook will automatically create one upon the first sync.&#x20;

This means that if you edited your content from GitBook at least once after setting up Git sync, GitBook should have created this file automatically.‌
{% endhint %}

### I have a SUMMARY.md file in my repository, but my new file still isn't listed

If, after updating your repository by adding a markdown file, you do not see the update reflected on GitBook, and there are no errors during the sync, your modified file(s) is probably not listed in your `SUMMARY.md` file.‌

This could be because you created the file manually in your repository and didn't add the reference to it in your `SUMMARY.md` file. The content of this file mirrors your table of contents on GitBook.
