# Source: https://help.cloudsmith.io/docs/deny-list.md

# Deny Policy

Package deny policy rules let you control which packages can be downloaded from your organization's repositories.

Deny Policies allow users to specify criteria, in the form of a `package_query_string`, to identify packages that should be blocked from download. By defining these rules, organizations can enforce stricter security measures and maintain tighter control over their software artifacts.

## Supported Package Formats

This feature applies to all formats.

## Scope

Deny Policies are applied at the organization level.

## View Deny Policies

To view the license policies in your organization, go to your organization's “Settings”->"Manage policies"->"Package Deny Policies" page.

<Image alt="Package Deny Policies" align="center" src="https://files.readme.io/7e404fe4ae434d837861b82fad3c4df7775eb56d406b516be996572e5130e70b-Screenshot_2024-10-18_at_22.01.26.png">
  Package Deny Policies
</Image>

## Create Deny Policies

To create a new Deny Policy, go to your organization's "Settings" page and select "Package Deny Policies" from the left side menu. Then click the "Create new policy" button.

<Image align="center" width="7px" src="https://files.readme.io/b4a0b04-Screenshot_2024-02-21_at_17.58.56.png" />

You are then presented with the “Create Package Deny Policy” form:

<Image align="center" width="600px" src="https://files.readme.io/4acb1661a774dc4b8ce3d71812838f65f1e1efd02fdd766e1e42b70e23ddce6e-Screenshot_2024-10-18_at_21.59.36.png" />

<br />

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
        **Policy Name**
      </td>

      <td>
        A display name for the Deny Policy. This name will be visible to users who view a package that violates this policy, as a reason for the violation.
      </td>
    </tr>

    <tr>
      <td>
        **Description**
      </td>

      <td>
        A description of the Deny Policy.  This description will be visible to users who view a package that violates this policy, as a reason for the violation.
      </td>
    </tr>

    <tr>
      <td>
        **Package Query**
      </td>

      <td>
        A search query that you can use to target this policy at a specific repository, package format or package name. See [Searching / Filtering](https://help.cloudsmith.io/docs/search-packages) for more details on the available fields you can filter on.

        The query string box (limited to 256 chars in length) to specify a search-query string to match packages against. Matched packages will then be blocked across the org.

        TIP:  To ensure your search query will block the packages you want to block from download, test your search query first, using the "Search all packages..." box at the top of the Repositories page.  Make sure the results of your query are the packages that you intend to block.
      </td>
    </tr>

    <tr>
      <td>
        **Enabled**
      </td>

      <td>
        You can disable a rule temporarily, without deleting the rule.
      </td>
    </tr>
  </tbody>
</Table>

## Propagating a Newly Created Deny Policy

When a new Deny Policy is created, Cloudsmith runs the policy against all packages in all repositories in your organization. This can take some time, depending on how many artifacts are stored in your repositories.

You can check the status of a newly created Deny Policy via our [Get a package deny policy](https://help.cloudsmith.io/reference/orgs_deny-policy_read) REST API call, which will return a `status` of "Pending" while the new policy is being propagated; the `status` will change to "Complete" when the policy is fully implemented across your organization.  (You'll need to get the slug\_perm identifier for your newly created Deny Policy first - use the [Get a list of all package deny policies](https://help.cloudsmith.io/reference/orgs_deny-policy_list) REST API call for this.)

Even after a new Deny Policy is fully propagated, a user who has recently downloaded a package may still be able to download it again for a short period of time, due to CDN caching.  You can still confirm that your Deny Policy has been successfully applied to a package by confirming the policy violation identifier appears on that package (see below).

## What Gets Blocked

Download requests are blocked for a specific package (or version of a package, if your search string specifies one).  This includes the first download of the package, even if the package is proxied through from an upstream.

## Policy Violation Identifiers

When local packages are blocked by a deny rule, it’s available in the application as a red-flag, and the download link on the right-hand-side is faded-out and will not click.

![](https://files.readme.io/b93756e-Screenshot_2024-02-28_at_16.38.16.png)

When you click into the package itself, you'll be able to see which deny rule is blocking the package.

![](https://files.readme.io/ddee1fe-Screenshot_2024-02-28_at_16.36.01.png)

You can use the `deny_policy_violated:true` search facet to see all packages that have been denied by Deny Policies.

![](https://files.readme.io/e5e20db-image.png)

## Audit Logs

There are also audit logs for whenever users configure (create, update or delete) Deny Policies:

![](https://files.readme.io/23ec126-Screenshot_2024-02-28_at_16.27.36.png)

## Unblock a package that violates a policy

To remove a policy violation, you have several options (depending on your user permissions):

* Delete the Deny Policy.
* Upgrade the package to a version outside of the Deny Policy.
* Edit the Deny Policy to allow this package using the query string language syntax.
* Temporarily disable the Deny Policy.