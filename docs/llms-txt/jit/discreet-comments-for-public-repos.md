# Source: https://docs.jit.io/docs/discreet-comments-for-public-repos.md

# Concealed Public Repos

## Overview

This feature enables you to conceal Jit’s security review comments (which might highlight mistakenly pushed secrets) in public repositories— by instead providing a summarized comment with a link to the associated [pipeline](https://docs.jit.io/docs/pipelines-page) on the Jit platform, accessible only to members of your GitHub organization.

**To configure concealed public repos in GitHub**

Add the following lines to your `​​jit-config.yml` file, which can be found in the `.jit` folder of the repo where you installed Jit's configuration files. Once configured, *all* public repos will use the concealed comment format.

```yaml jit-config.yml
pr_security_reviews:
  public_repo_concealed_review: true
```

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/be7760e-securecomment.png",
        null,
        "Example secure comment"
      ],
      "align": "center",
      "caption": "Example comment"
    }
  ]
}
[/block]

**To configure concealed public repos in other SCMs**

Use Jit's 'Update configuration file' API endpoint to enable a concealment of Jit’s security review comments. For more information, please see [API: Update configuration file.](https://docs.jit.io/reference/tenant-7ddaef1e-4ba5-4c0d-964b-d62a699c9e2f)