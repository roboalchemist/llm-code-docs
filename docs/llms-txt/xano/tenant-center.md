# Source: https://docs.xano.com/enterprise/enterprise-features/tenant-center.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tenant Center

<Info>
  ## **Quick Summary**

  The Tenant Center allows you to deploy your current workspace to multiple tenant environments. Tenants are best utilized for things like separate development, staging, and production environments, or isolating different customers or user groups into their own workspaces, like users in a specific region or your beta testers.

  Each tenant gets its own isolated database, and receives logic from releases you choose to deploy.
</Info>

## What is the Tenant Center?

The Tenant Center is designed to bring a more traditional CI/CD workflow into Xano.

With Tenant Center, you can:

* Easily manage separate development, stage, and production environments

* Isolate your users into separate environments and roll out new releases to them selectively, or all at once

* Create different environments for specific user groups to enable easier deployment of beta or exclusive Features

* Deploy your backend across multiple regions, improving latency and performance for those users and for compliance with data residency requirements

## How do I use the Tenant Center?

### Creating New Tenants

<Steps>
  <Step title="From your main (usually your production or primary development) workspace, head to the Tenant Center from the left-hand navigation menu.">
    You'll find it located under the Marketplace (if you have it enabled) or the Library.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/594627c1-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=800cce8ba82e3d899a43e2d83ea5678a" width="376" height="222" data-path="images/594627c1-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Click Add Tenant to create a new tenant.">
    Click <span class="ui-bubble"><Icon icon="plus" /> Add Tenant</span> to create a new tenant.

    Remember, tenants can be either your own stage and production environments, or actual separate user workspaces.

    When adding a new tenant, you'll need to provide some basic information.

    | Parameter       | Purpose                                                                                                                                                                                                                                              | Example                                                                  |
    | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
    | Display Name    | The name of the tenant workspace                                                                                                                                                                                                                     | StageBeta Customer ABC                                                   |
    | Description     | A description of the tenant workspace                                                                                                                                                                                                                | "Staging changes for testing" "Workspace for customer ABC" "Beta access" |
    | Tags            | Apply tags to your tenants to easily filter them when searching and deploying new changes. Great for things like separating subscription tiers or tagging development-specific, internal tenants. <br />**This is optional, but highly recommended** | dev prod beta                                                            |
    | License         | *See below*                                                                                                                                                                                                                                          |                                                                          |
    | RBAC Override   | Enable this option to set specific user permissions for this tenant. See the [RBAC: Tenant Center](#rbac-tenant-center) section below for more information.                                                                                          |                                                                          |
    | Ingress Enabled | Enable or disable ingress (incoming traffic) for this tenant. Disabling ingress will prevent any API calls from reaching this tenant. Use this if traffic is routed through your own gateway/load balancer instead of Xano’s default ingress.        |                                                                          |
  </Step>
</Steps>

<Info>
  ## **A note on new tenant creation**

  Creating a new tenant does not deploy a release to it by default.
</Info>

### Calling Tenant APIs

Each tenant will have their own base URL, which can be used to call a tenant's APIs directly. You can find this URL and more by clicking <span class="ui-bubble"><Icon icon="ellipsis-vertical" /></span> and choosing <span class="ui-bubble">Details</span>.

You can also utilize the `X-Tenant` header to call a tenant's APIs directly instead of utilizing the tenant's URL. This can make frontend implementation easier depending on your specific use case.

## Tenant Tiers

Some workspaces may have access to different tenant tiers, which determine the infrastructure allocated to each tenant. This includes:

* Hosting a tenant in a different region
* Allocating more resources (CPU, memory, etc.) to a tenant
* Allocating dedicated resources to a tenant

When creating a new tenant, you may see a **Type** dropdown. This allows you to select which tenant tier to assign to the new tenant.

| License            | Tenant Tier                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------- |
| Data Isolation     | **Shared Namespace** — shares resources with the source instance. No extra settings.      |
| Resource Isolation | **Dedicated Namespace** — gets dedicated resources; you choose allocation after creation. |
| Regional Isolation | **Remote Namespace** — runs in a different cluster/region.                                |

### Tiered Tenant Infrastructure

When deploying a *Resource Isolation (Dedicated Namespace)* or *Regional Isolation (Remote Namespace)* tenant, after creating the tenant you'll be prompted to select the specific infrastructure allocation for that tenant. We offer three pre-defined infrastructure packages:

* Small = “Get me live fast.”
  Best for MVPs, prototypes, internal tools, early-stage production, or moderate traffic.

* Medium = “We’re in production and growing.”
  For apps with steady real users, more endpoints, more background jobs, and higher concurrency.

* Large = “We need serious headroom.”
  Built for high traffic, enterprise workloads, heavy automation, larger datasets, and lots of simultaneous users.

### Managing Tenants

Once you've created a tenant, you can click the <span class="ui-bubble">⋮</span> icon to access tenant settings.

#### Edit Tenant

Change the settings applied when creating the tenant, such as the display name or description.

#### Deploy Release

Push a release to this specific tenant.

#### Impersonate

Access the tenant in its current state. Great for troubleshooting tenant-specific issues and manual verification of pushed changes

#### Environment Variables

You can access and manage this tenant's environment variables from here. Use these to store things like API keys and other sensitive information to be used in that tenant's function stacks.

For example, if you are pushing a feature that calls OpenAI, and each tenant has their own OpenAI API key, you'd put that here and just make sure the variable name matches what your function stacks reference.

#### Backups

Create or restore a backup of a tenant

#### Logs

Review logs directly associated with that tenant, such as release deployments, backups, and impersonations.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/3dae731a-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=3ea3412b5534cc833e1eac6d28bd3ed9" width="409" height="245" data-path="images/3dae731a-image.jpeg" />
</Frame>

### Developing and Deploying Releases

<Steps>
  <Step
    title="Make any changes you'd like to deploy in your development tenant. Push them to your stage tenant if you're using one.
"
  >
    Just make sure you're deploying from the tenant that contains your final, tested round of changes to push live to your tenants.
  </Step>

  <Step title="Use the tag selector to filter only the tenants you want to deploy to.">
    Select the appropriate tags and click **Apply**. Remember, you can also deploy to a single tenant by clicking the <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f85fc869-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=71a577199af045fce739e9a72be3dcbd" className="inline m-0" width="10" height="19" data-path="images/f85fc869-image.jpeg" /> icon on that specific tenant.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c44457db-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=ccb50fae43910e841b96135010491ff6" width="407" height="299" data-path="images/c44457db-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Set up a new release by clicking at the top of the page.">
    Set up a new release by clicking

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f85bedb0-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=d3105f806574de36dfb5b7245ab91000" width="84" height="40" data-path="images/f85bedb0-image.jpeg" />
    </Frame>

    at the top of the page.

    In the Releases panel, click <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/65a31a91-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=5488fda2d332dbae9d56e296f48bdcd9" className="inline m-0" width="139" height="26" data-path="images/65a31a91-image.jpeg" />

    Give your new release a name, a description, and choose the source branch you'll be deploying changes from.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/05628d02-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=64bbaca40807e2564fab16d9fd4718d8" width="406" height="219" data-path="images/05628d02-image.jpeg" />
    </Frame>

    When you're ready, click <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/24055003-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=7a96325925accd9cdbe5869825d2dd02" className="inline m-0" width="71" height="42" data-path="images/24055003-image.jpeg" /> at the bottom of the panel.
  </Step>

  <Step title="Select the tenants you'd like to deploy to.">
    You can click the checkbox at the top to select all currently shown tenants, or select individual tenants yourself.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c43c6f90-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=02dfb93e37863e03f0aae1f5b3e9d996" width="366" height="275" data-path="images/c43c6f90-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Deploy Release">
    Click <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/d67529d9-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=7c55a80bfd91fdaac026d5b73079e199" className="inline m-0" width="112" height="26" data-path="images/d67529d9-image.jpeg" /> at the top of the page to deploy a release to your selected tenants.

    Select the release to deploy and click the Deploy button at the bottom of the panel.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/d450e2be-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=a1d967219a405a1b59b632a4183a4b23" width="412" height="325" data-path="images/d450e2be-image.jpeg" />
    </Frame>

    After deployment, the **Release Stats** table at the top will give you quick visibility into your deployment metrics.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e2614260-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=6eb9bd24097ded03f9fe4649f01e320a" width="378" height="100" data-path="images/e2614260-image.jpeg" />
    </Frame>
  </Step>
</Steps>

***

## RBAC: Tenant Center

The Tenant Center addon includes additional [Role-based Access Control (RBAC)](/team-collaboration/role-based-access-control-rbac) settings you can use to manage tenant-related permissions.

These permissions include:

* **Tenant Center** - Enables access to the Tenant Center

* **Tenant Center RBAC** - Enables access to Tenant Center RBAC Override settings *Note: This does not disable the ability to disable/enable Tenant Center RBAC Overrides, but does disable access to editing the specific override settings.*

* **Tenant Center Logs** - Enables access to the logs inside of the Tenant Center

* **Tenant Center Backup** - Determines if a user can modify backup settings or perform backup/restore operations for tenants

* **Tenant Center Deploy** - Determines if a user can deploy releases to tenants

* **Tenant Center Impersonate** - Determines if a user can impersonate (access directly) a tenant

* **Tenant Center Secrets** - Enables access to secrets for a tenant, such as [Environment Variables](/the-function-stack/environment-variables)

### RBAC Override

From the **Edit Tenant** panel, you can enable **RBAC Override**. This option allows you to specify individual user permissions for each tenant by clicking **RBAC** at the top of the Tenant Center.

<Frame caption="Enabling the RBAC Override option">
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2b2fb573-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=59eeb0c3e8405a5fc7dc46daa465e9d6" width="767" height="694" data-path="images/2b2fb573-image.jpeg" />
</Frame>

<Frame caption="An example of available permissions with RBAC Override enabled">
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/064a8081-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=644a57a6394824eb0dfad4bcc4094668" width="1321" height="923" data-path="images/064a8081-image.jpeg" />
</Frame>

## Best Practices

<Steps>
  <Step title="Tag your tenants">
    Using tags is crucial to quick and consistent work inside of the Tenant Center, especially as the number of tenants you have grows.
  </Step>

  <Step title="Follow a traditional deployment framework">
    This would include developing on a **development** tenant, pushing final changes to a **stage** tenant where all of your [QA and testing](/testing-debugging/test-suites) happens, and then deploying releases from **stage**.

    Read more about the entire Development Lifecycle [here](/before-you-begin/the-development-life-cycle).
  </Step>

  <Step title="Inform your users of upcoming deployments">
    In most cases, it's good practice to make sure your users are aware of upcoming changes.
  </Step>

  <Step title="Use backups">
    Tenant backups are incredibly important when deploying new changes, so you can use them to quickly roll back changes.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).