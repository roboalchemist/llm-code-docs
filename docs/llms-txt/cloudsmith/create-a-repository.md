# Source: https://help.cloudsmith.io/docs/create-a-repository.md

# Create a Repository

You can create a new repository in three ways:

* Via the Cloudsmith CLI
* Via the Website UI
* Via the Cloudsmith API

## Via the Cloudsmith CLI

In the following examples:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Identifier
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        OWNER
      </td>

      <td>
        A Cloudsmith organization / workspace / namespace account name
      </td>
    </tr>

    <tr>
      <td>
        REPO-NAME
      </td>

      <td>
        A name for your repository. Maximum 50 characters.
      </td>
    </tr>

    <tr>
      <td>
        REPO-DESC
      </td>

      <td>
        Description for your Repository
      </td>
    </tr>

    <tr>
      <td>
        REPO-TYPE
      </td>

      <td>
        The type of repository - "Public" or "Private"
      </td>
    </tr>

    <tr>
      <td>
        <span class="nobr">REPO-IDENTIFIER</span>
      </td>

      <td>
        (Optional) A unique identifier for the repository, also referred to as a 'slug'. This will form part of the URI for your repository. It can only contain lowercase alphanumeric characters, hyphens, and underscores and must be a minimum of 2 characters.
      </td>
    </tr>
  </tbody>
</Table>

> 📘 NOTE
>
> If you do not specify a repository identifier, we will generate one for you. We will try to base this on the repository name where possible but may also append some characters to it. If you require a specific repository identifier, we recommend that you do specify one.

Create a `REPO-CONFIG.json` file with the following:

```json
{
    "name": "REPO-NAME",
    "description": "REPO-DESC",
    "repository_type_str": "REPO-TYPE",
    "slug": "REPO-IDENTIFIER"
}
```

You can create then a repository via the [Cloudsmith CLI](https://help.cloudsmith.io/docs/cli) using the following command:

```
cloudsmith repos create OWNER REPO-CONFIG.json
```

### Example

`example-repo-config.json` file:

```json
{
    "name": "Example Repository",
    "description": "Example packages repository",
    "repository_type_str": "Private",
    "slug": "example-repo1"
}
```

Create repository command:

```shell
cloudsmith repos create demo example-repo-config.json
```

<Image title="repo-create.png" alt={842} align="center" src="https://files.readme.io/12b8126-repo-create.png">
  cloudsmith repos create command
</Image>

***

## Via the Website UI

You can create a repository by navigating to the Repositories overview and clicking the "New repository" button.

<Image align="center" src="https://files.readme.io/5c579b6db69372fc661ddbee38b30cf4908cbfe1bf51f6eb3b859e745905eb08-create-repository.png" />

That will take you to the "Create a new Repository" form:

<Image align="center" width="80%" src="https://files.readme.io/92ff99444bad9c24826e2964901365d3286245ff96bfbcfa403ddd544f279cee-create-a-new-repo.png" />

Here, you simply name your repository and click "Create Repository," and you will create a new private repository.

> 📘 Multi-Format Repositories
>
> All Cloudsmith repositories are multi-format. This means you can store artifacts of different formats in the same logical grouping. A Maven package can sit beside a Debian package, a Ruby Gem or a Python package!

You can manage your Repository by navigating to your new repository and selecting Settings.

<Image align="center" src="https://files.readme.io/28d77d9f603f2f346671ced886d5f1f537f6580dd709b46fa1fb57acec3542c3-repo-settings.png" />

From there, you can manage:

* General settings
* Access control
* Retention rules
* EULA enforcement
* GEO / IP rules
* Key management
* Webhooks

> 📘 Changing Repository Settings
>
> The good thing about Cloudsmith is that you can change everything later. The name, slug, description, repository type can all be changed if necessary. Although once shared, if you change the settings or naming you may need to communicate this to all interested parties.

### Private Repositories

All paid accounts come with unlimited Private repositories.

Private repositories are private. If required, external access to any files in a private repository is controlled by our Entitlement system. See "[How To: Sharing a Private Package](https://help.cloudsmith.io/docs/sharing-a-private-package)" for more details.

### Broadcasts

> 📘 Early Access Feature
>
> Broadcasts is currently an early access feature. If you would like to try this feature, please [Contact Us](https://help.cloudsmith.io/docs/contact-us).

You can create a branded public repository using our new distribution feature, Broadcasts. Enabling broadcasting during repository creation creates a public page where users can browse, search, and download repository packages without requiring authentication. See [Broadcasts](https://help.cloudsmith.io/docs/broadcasts)  for more information.

<Image align="center" src="https://files.readme.io/6c6bd740e89732b90146ae3152dd14384d570a3c31f47e174fb7d5a2842a9d37-enable-broadcasting.png" />

***

## Via the Cloudsmith API

For details on how to create a repository via the Cloudsmith API, please see the "Create a Repository" section of the [API Reference](https://help.cloudsmith.io/reference#repos_create), including an interactive sandbox where you can test your API Calls.

> 📘 NOTE
>
> It is not currently possible to create Open Source repositories via the Cloudsmith API.