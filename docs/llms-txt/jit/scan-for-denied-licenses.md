# Source: https://docs.jit.io/docs/scan-for-denied-licenses.md

# Open Source License Detection

## Key things to know about Jit Open Source License Detection

* **Brief overview:** Jit scans your codebase to maintain a continuously updated inventory of the OSS software components, dependencies, and their associated open source licenses. Jit also scans every code change to flag copyleft licensed open source code before developers commit it.
* **Scanning process:** Jit automatically scans your codebase daily to document OSS Licenses in Jit's [SBOM](https://docs.jit.io/v5.0/docs/sbom) product.
* **How to get started:** Go to **Security Plans** and select **Jit Max Security**, scroll down the **Scan your code for license violations** line item and hit **Activate**.
* **Based on OSV Scanner:** Jit unifies and enhances the leading open source scanners for all product security scanning technologies. For OSS License Detection, Jit leverages OSV Scanner to scan your codebase and identify OSS components.

> 📘 Premium Feature
>
> Open Source License Detection is only available for paying Jit customers.

## Understanding the License Deny List

License checking in Jit ensures that your project adheres to the defined licensing requirements by scanning your codebase for unpermitted licenses. This feature helps maintain compliance with legal obligations associated with third-party components and mitigates the risk of licensing issues.

By default, Jit employs a deny-list approach, prohibiting licenses such as GPL and EU Public License. However, users have the flexibility to customize this list according to their project's specific needs by adjusting the jit-config.yml file.

Deny-list: Jit maintains a default deny-list of licenses that are not permitted within your project. This includes licenses such as GPL.

dual\_license can have either the **restrictive** or **permissive** value.

* Restrictive Dual License: By default, Jit operates in restrictive dual license mode. In this mode, if one of the licenses associated with a dual-licensed component is found in the deny-list, the user will be alerted. For example, if a component has licenses GPL or MIT, and GPL is in the deny-list, a finding will be created.
* Permissive Dual License: Alternatively, users can opt for permissive dual license mode. In this mode, if one of the licenses associated with a dual-licensed component is not found in the deny-list, no alert will be generated. For example, if a component has licenses GPL or MIT, and neither GPL nor MIT are in the deny-list, no finding will be created.

### Deny List Customization

Users can override the default deny-list by modifying the jit-config.yml file located at User's organization/.jit/.jit/jit-config.yml.

```Text yml
license-compliance:
  deny_list:
    - EUPL*
    - GPL*
  dual_license: restrictive # or permissive
```

Wildcard Usage: Wildcard (\*) can be employed to match licenses that contain a specific string. For instance, Apache\* matches licenses like Apache-2.0, L-Apache, etc.

Case Insensitivity: License matching is case-insensitive. For example, MIT is considered the same as mit.

<br />

## Pull Request Enforcement

Upon the creation or update of a Pull Request (PR), the License Checker will automatically initiate a scan to detect any license violations. If violations are identified, the PR will be halted until the issues are resolved, ensuring that only compliant code is merged into the repository.

![](https://files.readme.io/5cd396f-image.png)

![](https://files.readme.io/c2b9928-image.png)

## Scheduled Scans

In addition to PR enforcement, the License Checker runs on a predefined schedule to conduct regular scans of the codebase. If any violations are detected during these scheduled scans, the License Checker will automatically open findings in the Findings page, alerting the team to address the violations promptly.

By employing both real-time PR enforcement and scheduled scans, the License Checker provides comprehensive coverage to maintain compliance with licensing requirements throughout the development lifecycle.

## Supported package types

* npm
* Pip