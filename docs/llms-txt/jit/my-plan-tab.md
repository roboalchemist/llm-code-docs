# Source: https://docs.jit.io/docs/my-plan-tab.md

# Specific Plan Page

The Jit platform has a page for each security plan:

* Each security plan has a similar structure.
* Security requirements can be activated and configured for each plan.

For a list of all security plans, see [Product Security Plans](https://docs.jit.io/docs/security-plans). For more details about Jit security plans, controls, and tools, see [Security plan reference](https://docs.jit.io/docs/introduction-2).

## Plan structure

### Plan summary

This section displays:

1. Plan version and description.
2. `Set as Goal`, Jit streamlines your progress with automated control activation and targeted recommendations.
3. `Export Plan Results`, use this option to download an `.xlsx` file, to be used as a Compliance report.
4. Widgets, to see the total score, requirements, and findings.

### Security Controls (requirements)

![](https://files.readme.io/eee87a9-image.png)

![](https://files.readme.io/cc9942c-image.png)

#### Security plan list of security controls

1. Filter by Activation state and pass/fail/error/pending status (based on the security findings).
2. Jit identifier per control with a notion indicating whether this control is automatic or manual.
   1. Automatic controls might require user input (configuration) to run.
   2. Manual controls, users must set the status of the control manually.
3. Security control names and the security tools they run with the last evaluated time. Learn more on [Security Controls](https://docs.jit.io/docs/security-controls) and [Security Tools](https://docs.jit.io/docs/security-tools).
4. Each activated security control has a status and a link to all the relevant security findings detected by it.
5. To be activated, some security controls need configurations or integrations. For example, `Scan infrastructure for runtime misconfigurations` requires integration with your organization's cloud provider.
6. To test a `code` security requirement, click **Test me** to create a test pull request in a pipeline in the [Pipelines page](https://docs.jit.io/docs/pipelines-page).  For more test instructions, see [Pipelines test](https://docs.jit.io/docs/pipelines-page#testing-newly-activated-security-requirements).

#### Viewing a security control's (requirement) details

To view more details about a security control, select the control in the table and a right panel will be opened.

![](https://files.readme.io/8a19e06-image.png)