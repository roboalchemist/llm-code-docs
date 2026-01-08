# Source: https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/group-projects-by-branch-or-version-for-monitoring.md

# Group Projects by branch or version for monitoring

{% hint style="info" %}
**Feature availability**

Grouping Projects by branch or version is available only for Enterprise plans. For more information, see [Plans and pricing](https://snyk.io/plans).

The feature is supported for areas of Open Source.
{% endhint %}

Your Project may have multiple states that you want to monitor separately, for example, branches, releases, or deployments. You can use the `--target-reference` option to separate Projects into these specific groupings.

`--target-reference` takes any text so you can combine it with a command to automatically set it to a value. Examples follow.

Set `--target-reference` to the current Git branch.

```
snyk monitor --target-reference="$(git branch --show-current)"
```

Use the latest Git tag.

```
snyk monitor --target-reference="$(git describe --tags --abbrev=0)"
```

You can adjust the option for the developer tools used in your project. Any valid Git target can be used.

`--target-reference` allows you to create sub-groupings on the Projects page.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c680e0094adb1fe2c280cfa2f63e54498f6f0204%2Fproject-grouping-with-sub-groups.png?alt=media" alt="A Project page with sub-groups"><figcaption><p>A Project page with sub-groups.</p></figcaption></figure>
