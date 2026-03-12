# Source: https://help.cloudsmith.io/docs/license-policy.md

# License Policy

License Policies allow you to define which package licenses are allowed within your organization. You can specify one or more licenses to exclude and an action to perform when a specified license is detected.

This is useful when you need to flag or optionally automatically quarantine a package based on the associated license.

## Supported Package formats

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Format
      </th>

      <th>
        <div className="cs-center">License Support </div>
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        [Alpine](https://help.cloudsmith.io/docs/alpine-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Cargo](https://help.cloudsmith.io/docs/cargo-registry)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Cocoapods](https://help.cloudsmith.io/docs/cocoapods-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Composer](https://help.cloudsmith.io/docs/composer-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Conan](https://help.cloudsmith.io/docs/conan-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Conda](https://help.cloudsmith.io/docs/conda-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [CRAN](https://help.cloudsmith.io/docs/cran-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Dart](https://help.cloudsmith.io/docs/dart-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Debian](https://help.cloudsmith.io/docs/debian-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/2fe13f1-cross_red.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Docker](https://help.cloudsmith.io/docs/docker-registry)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/2fe13f1-cross_red.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Go](https://help.cloudsmith.io/docs/go-registry)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Helm](doc:https://help.cloudsmith.io/docs/helm-chart-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Hex](https://help.cloudsmith.io/docs/hex-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [LuaRocks](https://help.cloudsmith.io/docs/luarocks-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Maven](https://help.cloudsmith.io/docs/maven-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [npm](https://help.cloudsmith.io/docs/npm-registry)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [NuGet](https://help.cloudsmith.io/docs/nuget-feed)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Python](https://help.cloudsmith.io/docs/python-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [RPM](https://help.cloudsmith.io/docs/redhat-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Ruby](https://help.cloudsmith.io/docs/ruby-repository)

        (Beta)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/006a7b5-tick_green.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Terraform](https://help.cloudsmith.io/docs/terraform-modules-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/2fe13f1-cross_red.png" />
        </div>
      </td>
    </tr>

    <tr>
      <td>
        [Vagrant](https://help.cloudsmith.io/docs/vagrant-repository)
      </td>

      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/2fe13f1-cross_red.png" />
        </div>
      </td>
    </tr>
  </tbody>
</Table>

## View License Policies

To manage the license policies in your workspace, go to your workspace's Settings page and select Manage Policies >> License Policies from the left-hand menu.

> 🚧

Deactivating a policy is not supported at this time, resulting in any policy created being active until deleted.

<Image align="center" src="https://files.readme.io/c003d4c5f13c07f716c7eeb9a58ff08cd09e12983a40ed4840e8a4662705680b-settings-manage-license-policies.png" />

## Create License Policy

To add a new license to the deny list, click “Create License Policy”.

<Image title="view_policy_new.png" alt={1239} align="center" src="https://files.readme.io/e5f0379d7b25a175eca1fc975a05e040995a96ec13f4f4e97a9b558f8e4a6bff-create-license.png">
  Create License Policy Button
</Image>

You are then presented with the “Create a License Policy” form:

<Image align="center" src="https://files.readme.io/0fe4ba308b83f6772b9f2a5872de71ce98c5be053ef31e85e8ba5408af891810-create-license-policy-form.png" />

Here you can define the following:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th />

      <th />
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Name
      </td>

      <td>
        A display name for the License Policy.
      </td>
    </tr>

    <tr>
      <td>
        Description
      </td>

      <td>
        A description of the License Policy.
      </td>
    </tr>

    <tr>
      <td>
        Allow unknown or absent licenses
      </td>

      <td>
        Set to “Yes” to ignore packages with missing or unknown licenses. Set to “No” to flag and quarantine packages with a missing or unknown license.

        Note: SPDX License List is used as the license source. If a package has a license that is not listed in the [SPDX License List](https://spdx.org/licenses/), this will be treated as an unknown license.
      </td>
    </tr>

    <tr>
      <td>
        Quarantine on violation
      </td>

      <td>
        If set to "Yes", any package that violates this license policy is flagged and automatically quarantined.

        If set to "No", packages that violate this license policy are flagged, but not automatically quarantined.
      </td>
    </tr>

    <tr>
      <td>
        Select licenses to deny
      </td>

      <td>
        Select the licenses to be denied as part of this policy. The licenses listed in this table are sourced from the [SPDX License List](https://spdx.org/licenses/).
      </td>
    </tr>
  </tbody>
</Table>

Once saved, the policy is enabled across your workspace and the policy compliance check will be performed automatically during the package synchronisation process. This process occurs when a package is uploaded, moved, copied, or cached (such as in upstream caching).

You can also manually trigger a synchronisation of a package using the resync functionality. See [Package Resynchronization](https://help.cloudsmith.io/docs/resync-a-package) for instructions on how to do this.

## Policy Violations

License policy violations can be viewed on the workspace and repository compliance dashboards. By selecting License Policy Violations from the overview, the table will filter to show all license policy violations across the workspace or repository.

<Image align="center" src="https://files.readme.io/cd0067c990f994778f786fec0722a9762c2d763676e9a96de7dea493e0f071f5-violation.png" />

You can also search for policy violations using `policy_violated:true`.

<Image align="center" src="https://files.readme.io/e11a1a83691e4515c5e9a687c1d658e3e1d93c2d78907ddb94ebd7bffa436ee2-search-policy-violations.png" />

> 📘

You can view this violation list at any time using our package search [(link)](https://help.cloudsmith.io/docs/search-packages#searching-packages-via-the-website-ui) feature and setting the filter to `policy_violated:true` for all policy violations, or `license_policy_violated:true` to only return license policy violations.

## Policy Violation Identifiers

Within a repository, packages with policy violations are identified with the Policy Violation and Vulnerabilities icons.

<Image title="violation indicators.png" alt={1126} align="center" src="https://files.readme.io/d0f4b2db2730243492ebc82e00223d3b40bea851dff71e286229de93da55ca3c-icons.png">
  Policy Violation Indicators
</Image>

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th />

      <th />

      <th />
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/a351636-red_flag.png" />
        </div>
      </td>

      <td>
        Policy Violation
      </td>

      <td>
        This package is in violation of policy. Click on the package to view more details.
      </td>
    </tr>

    <tr>
      <td>
        <div className="cs-center">
          <img src="https://files.readme.io/a40d9a3-quarantine_icon.png" />
        </div>
      </td>

      <td>
        Quarantined
      </td>

      <td>
        This package has been quarantined, downloads will be blocked until the package is released from quarantine.

        Reason given: the package was quarantined as a result of a policy violation
      </td>
    </tr>
  </tbody>
</Table>

Clicking on the package name displays the Package overview, which provides details on the policy violations for the package.

<Image align="center" src="https://files.readme.io/37b3010d2d23eafca8f93e5246acbded37595d3dc23f45b2552298ec003b7485-view-policy-violation.png" />

By selecting License Policy Violation from the summary, you can view a list of all license policies the package violates and view and modify the policies from there.

<Image align="center" src="https://files.readme.io/11290e4d631f45d7a3a4ea12a312a371c0d66e2dca7d2c0a9780dd00efa57495-edit-license-policy.png" />

## Package Logs

Logs of policy violations and quarantining actions are also displayed within the Package Logs page.

> 📘

Hover over the “policy violation” text to display additional details on the policy and license violation.

## Restore a package that violates a policy

It's important to note that packages cannot be restored from quarantine if they are still in violation of an existing policy which has **Quarantine on violation** set to "Yes".

To remove a package from quarantine, you have four options:

* Change the package license to an allowed license via the [license compliance](https://help.cloudsmith.io/docs/license-compliance#edit-a-license) section of the package's repository.
* Apply a manual license override of "ignored" or "purchased" via the [license compliance](https://help.cloudsmith.io/docs/license-compliance#edit-a-license) section of the package's repository.
* Edit the license policy to remove the license from the deny list.
* Edit the license policy to set **Quarantine on violation** to "No".

If you change the package license, the package will be resynchronized and automatically undergo the policy check again. If the new license is not on the deny list, the package will no longer be marked as a policy violation and can be manually removed from quarantine.

If you update the policy to remove the license from the deny list or set **Quarantine on violation** set to "No", the package can be manually removed from quarantine.

See [Package Quarantine](https://help.cloudsmith.io/docs/package-quarantine#release-from-quarantine) for instructions on restoring a package from quarantine.