# Source: https://help.cloudsmith.io/docs/package-tags.md

# Package Tags

<HTMLBlock>
  {`
  <div class="cs-headline">Package tags allow you to add your own custom tags to your packages. You can then use tags to group and sort your packages via search queries (see <a href="https://help.cloudsmith.io/docs/search-packages">Searching/Filtering</a> for details), or to help you organize your packages in a way that suits you.</div>
  `}
</HTMLBlock>

You can also use package tags in association with your [entitlement tokens](https://help.cloudsmith.io/docs/entitlements), in order to limit what packages your customers can access. For example, you can tag your packages and create an associated entitlement token in such a way that "standard edition" customers only have access to the "standard" packages, but "pro edition" customers have access to both "standard" and "pro" packages.

In addition, you can specify that tags you add are immutable. This means that they can only be modified or deleted by a user with repository admin privileges, or by the user that owns the package.

We provide three ways to manage your custom package tags:

* via the Cloudsmith CLI
* via the Cloudsmith API
* via the Website UI

> 📘
>
> Some tags, such as filetype, architecture and other format-specific tags are generated automatically during package upload and processing, and therefore cannot be removed or modified.

## Package Tags via the CLI

For full details of how to install and setup the Cloudsmith CLI, see [Command-Line Interface](https://help.cloudsmith.io/docs/cli).

To add or modify tags using the Cloudsmith CLI, you first need to identify the package you wish to tag or modify.  See [Package Identification](https://help.cloudsmith.io/docs/identifying-a-package) for instructions to do this.

### List Tags

The command to list all tags for a package is:

```shell
cloudsmith tags list OWNER/REPOSITORY/IDENTIFIER
```

Example:

```shell
cloudsmith tags list demo/examples-repo/ptqbzjgm2pq1
```

<Image title="list-tags.png" alt={760} align="center" src="https://files.readme.io/6fe0d48-list-tags.png">
  List tags
</Image>

### Add Tags

The command to add a tag to a package is:

```shell
cloudsmith tags add OWNER/REPOSITORY/IDENTIFIER TAG
```

You can add also add multiple tags:

```shell
cloudsmith tags add OWNER/REPOSITORY/IDENTIFIER TAG1,TAG2,TAG3
```

Example:

```shell
cloudsmith tags add demo/examples-repo/ptqbzjgm2pq1 foo,bar,baz
```

<Image title="add-tags.png" alt={715} align="center" src="https://files.readme.io/06958c2-add-tags.png">
  Add tag(s)
</Image>

To add an immutable tag, use the `--immutable` flag.\
Example:

```shell
cloudsmith tags add demo/examples-repo/ptqbzjgm2pq1 fizz --immutable
```

<Image title="add-immutable-tag.png" alt={759} align="center" src="https://files.readme.io/50dfa6e-add-immutable-tag.png">
  Add immutable tag(s)
</Image>

You may also add tags when a package is uploaded via the `cloudsmith push` command.\
Example:

```shell
cloudsmith push deb OWNER/REPOSITORY/DISTRO/VERSION PACKAGE-NAME.deb --tags TAG1, TAG2 
```

### Replace Tags

The command to replace all tags (except immutable tags) on a package is:

```shell
cloudsmith tags replace OWNER/REPOSITORY/IDENTIFIER TAG
```

Example:

```shell
cloudsmith tags replace demo/examples-repo/ptqbzjgm2pq1 buzz
```

<Image title="replace-tags.png" alt={760} align="center" src="https://files.readme.io/5db866f-replace-tags.png">
  Replace tags
</Image>

### Remove Tags

The command to remove tags from a package is:

```shell
cloudsmith tags remove OWNER/REPOSITORY/IDENTIFIER TAG
```

> 📘
>
> You need to have repository admin privileges or be the package owner to remove immutable tags.

Example

```shell
cloudsmith tags remove demo/examples-repo/ptqbzjgm2pq1 baz
```

<Image title="remove-tags.png" alt={760} align="center" src="https://files.readme.io/de1bb6a-remove-tags.png">
  Remove Tag
</Image>

### Clear Tags

The command to clear all tags (except immutable tags) from a package is:

```shell
cloudsmith tags clear OWNER/REPOSITORY/IDENTIFIER
```

Example:

```shell
cloudsmith tags clear demo/examples-repo/ptqbzjgm2pq1
```

<Image title="clear-tags.png" alt={761} align="center" src="https://files.readme.io/e90dbd8-clear-tags.png">
  Clear tags
</Image>

## Package Tags via the API

You can add and modify tags via the Cloudsmith API.

Please see the full [API Reference](https://help.cloudsmith.io/reference) for details, including an interactive sandbox where you can test your API Calls.

## Package Tags via the Website UI

To add or modify tags using the Website UI, click on the package name first, then click on the blue plus sign within the "Tags" section within the package information:

<Image align="center" src="https://files.readme.io/d068e8d0d58e1b0f922085a5de1cb65d2a9a51cf22e29b525988957870a6b08d-Screenshot_2024-11-08_at_3.40.04_PM.png" />

<br />

You are then presented with the "Edit Package Tags" form where you add, modify or remove tags:

<Image align="center" src="https://files.readme.io/d1bd9face2cc65f3b2fe03c8d468f914cac9fb21b7bdf6355af364069cb973ef-Screenshot_2024-11-08_at_3.43.01_PM.png" />