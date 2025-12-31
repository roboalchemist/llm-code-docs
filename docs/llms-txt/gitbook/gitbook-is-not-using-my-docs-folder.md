# Source: https://gitbook.com/docs/help-center/integrations/integrations-troubleshooting/git-sync/gitbook-is-not-using-my-docs-folder.md

# ​GitBook is not using my docs folder

By default, GitBook uses the repository's root as a starting point. A specific directory can be specified to scope the markdown files.

If you have a structure where the root of your docs is not the root of your repository, please create a `.gitbook.yaml` file in the root of your repository with the following syntax:

{% tabs %}
{% tab title=".gitbook.yaml" %}

```
root: ./folder/path/here
```

{% endtab %}
{% endtabs %}

Take a look at our documentation on [content configuration](https://gitbook.com/docs/integrations/git-sync/content-configuration#root) for more details and other customization options.
