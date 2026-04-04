# Source: https://docs.envzero.com/guides/admin-guide/remote-backend/remote-plan.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Running Remote Plan

> Run terraform plan locally while executing remotely on env zero with shared state, variables, and audit trails

## Remote Plan

Remote Backend allows running your Terraform plan locally by triggering a remote plan in env zero.\
The remote plan uses your local Terraform files but actually runs it remotely in env zero while using the shared state and variables set for the env zero environment. Each remote plan creates a deployment in env zero so you will have an audit for each deployment.\
By running a remote plan you can build your IaC faster, and test your changes locally **before committing** them.

Additional benefits are the rest of the env zero features that are automatically integrated into your plan logs. It includes:

* [Role Based Access](/guides/admin-guide/user-role-and-team-management/user-management)
* [Custom Flows](/guides/admin-guide/custom-flows)
* [Cost Estimation](/guides/cost-monitoring/cost-monitoring/#cost-estimation)
* [Variables and Secrets](/guides/admin-guide/variables)
* [Policies](/guides/policies-governance/policies)
* [Plugins](/guides/integrations/plugins)

<img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/remote-backend/56b8b73-image_5.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=41097d22f532e17c97138333b874409e" alt="" width="2910" height="1412" data-path="images/guides/admin-guide/remote-backend/56b8b73-image_5.png" />.png")

<img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/remote-backend/a29345c-image_6.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=01bb411d0563ce1121e3a5e141b5ad32" alt="" width="2174" height="544" data-path="images/guides/admin-guide/remote-backend/a29345c-image_6.png" />.png")

## .terraformignore

If cases where your gitrepo is particularly large, this will cause the remote plan to take a longer time to process (due to compressing and decompressing the gitrepo).  You can save time on the remote plan by adding a [`.terraformignore`](https://opentofu.org/docs/cli/cloud/settings/#excluding-files-from-upload-with-terraformignore) to the root of the repo.

```.terraformignore  theme={null}
/**
!my-working-dir/
my-working-dir/.terraform
my-working-dir/.terraform/**
```

<Warning>
  ignore the local `.terraform` folder

  If you have a local `.terraform` folder, please add it to the ignore list (like in the example above), otherwise you may get some errors such as `workspace not supported`
</Warning>

## Auditing

env zero UI can show you each remote plan deployment that has occurred, accesses its plan logs, and gives you visibility and audit on who actually trigged it from their local environment.

<img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/remote-backend/ff2b45e-image_4.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=2496b102e557e75501df60da4ed15da5" alt="" width="2768" height="692" data-path="images/guides/admin-guide/remote-backend/ff2b45e-image_4.png" />.png")

## Local Executions

If you still wish to run a `plan` or `apply` locally, without a remote execution by env zero - you can do it by enabling terraform's `TF_FORCE_LOCAL_BACKEND` environment variable.

```shell  theme={null}
TF_FORCE_LOCAL_BACKEND=1 terraform apply
```

<Warning>
  Local Execution

  When running `plan` or `apply` locally, those deployments are not audited in env zero and RBAC and policy control are not enforced. In addition since the code you are running is not commited, we can't attach that deployment to a certain commit or a branch.

  You should avoid using Local Execution as much as possible.
</Warning>

Built with [Mintlify](https://mintlify.com).
