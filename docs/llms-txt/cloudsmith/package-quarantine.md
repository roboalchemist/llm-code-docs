# Source: https://help.cloudsmith.io/docs/package-quarantine.md

# Package Quarantine

Package quarantine allows you to temporarily block any downloads of a package until you release the package from quarantine.

This is useful in any case where you wish to remove the ability to access a package that is present in your Cloudsmith repository, for example, in a case where a security vulnerability is discovered after you have published a package. Unlike deleting a package, you can restore access to the specified package at a later stage if required.

We provide the ability to quarantine a package in three ways:

* Quarantine via the Website UI.
* Quarantine via the Cloudsmith CLI
* Quarantine via the Cloudsmith API

***

In the following examples:

| Identifier | Description                                                                                                                                  |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| OWNER      | Your Cloudsmith account name or organization name (namespace)                                                                                |
| REPOSITORY | Your Cloudsmith Repository name (also called "slug")                                                                                         |
| PACKAGE    | The unique identifier for a package, see [Package Identification](https://help.cloudsmith.io/docs/identifying-a-package) for further details |

***

## Quarantine via the Website UI

### Add to quarantine

You can quarantine a package using the quarantine button on the Package Details page, or from the packages view using the Package Actions:

<Image title="quarantine-pkg-details.png" alt={1313} align="center" border={true} src="https://files.readme.io/7e258c70af8c0c7a27775543b219eb12302327c39d75cb53e8fd83cfd5463940-app.cloudsmith.com_demo_product-b_rpm_cloudsmith-rpm-example_1.0-1_COhhH8fjPOlhiPad_Pro.png">
  Quarantine Button on Package Details
</Image>

<Image title="quarantine-pkg-view.png" alt={1321} align="center" border={true} src="https://files.readme.io/eb1beb53b63b68259de530e1b8adcfaacac7b7ae43d3ada5f55caec91554141f-app.cloudsmith.com_demo_product-b_rpm_cloudsmith-rpm-example_1.0-1_COhhH8fjPOlhiPad_Pro_1.png">
  Confirmation that you'd like to quarantine the package
</Image>

Once you have quarantined a package, the synchronization status will change from "Completed" to "Quarantined".

### Release from quarantine

You can remove a package from quarantine using the Unquarantine button on the Package Details page:

<Image title="quarantine-restore-package-details.png" alt={1341} align="center" border={true} src="https://files.readme.io/a12a4311fecf79ba83a58e2a9257d807fcbb7d59f6c049f711722230a5b6a313-app.cloudsmith.com_demo_product-b_rpm_cloudsmith-rpm-example_1.0-1_COhhH8fjPOlhiPad_Pro_2.png">
  Unquarantine Button on Package Details
</Image>

<Image align="center" className="border" border={true} src="https://files.readme.io/028ad37c85b9f411e0d8292031799177e3f659ae79faca31341a141c353a4721-app.cloudsmith.com_demo_product-b_rpm_cloudsmith-rpm-example_1.0-1_COhhH8fjPOlhiPad_Pro_3.png" />

***

## Quarantine via the Cloudsmith CLI

Quarantine operations via the Cloudsmith CLI are performed using the `cloudsmith quarantine` command.

Before you can add or remove a package from quarantine using the CLI, you first need to identify the package.  See [Package Identification](https://help.cloudsmith.io/docs/identifying-a-package) for full instructions on identifying packages.

### Add to quarantine

To quarantine a package, use the command `cloudsmith quarantine add` as follows:

`cloudsmith quarantine add OWNER/REPOSITORY/PACKAGE`

For example:

`cloudsmith quarantine add demo/examples-repo/IB6FYhIvaoAy`

<Image title="cli-quarantine-add.png" alt={1106} align="center" src="https://files.readme.io/d5d860b-cli-quarantine-add.png">
  CLI add to quarantine
</Image>

### Release from quarantine

To release a package from quarantine, use the command `cloudsmith quarantine remove|rm|restore` as follows:

`cloudsmith quarantine remove OWNER/REPOSITORY/PACKAGE`

For example:

`cloudsmith quarantine remove demo/examples-repo/IB6FYhIvaoAy`

<Image title="cil-quarantine-remove.png" alt={1157} align="center" src="https://files.readme.io/ab7eff5-cil-quarantine-remove.png">
  CLI remove from quarantine
</Image>

***

## Quarantine via the Cloudsmith API

Please see the Cloudsmith [Interactive API Reference](https://help.cloudsmith.io/reference/packages_quarantine) for details on the Quarantine Package API endpoint

***

## Client behaviour

When a quarantined package is requested by native tooling e.g. pip install, mvn install, npm install, etc., the repository returns **HTTP 403 Forbidden**. Builds will fail with a 403 error such as:

```
ERROR: HTTP error 403 while getting <https://dl.cloudsmith.io/…/requests-2.6.1…>
```

This confirms the package is quarantined.