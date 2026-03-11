# Source: https://docs.envzero.com/guides/admin-guide/private-registry/modules.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Module Overview

> Share and reuse Terraform and OpenTofu modules securely with the env zero private module registry

## env zero Module Registry

The env zero Module Registry is a private registry for sharing and reusing [OpenTofu/Terraform modules](https://www.terraform.io/docs/language/modules/syntax.html), within your organization. You can access your organization's module registry through the Registry tab in the Organization Menu.

Using env zero's private registry enhances security by ensuring that only authorized users have access to approved infrastructure modules, reducing the risk of deploying unverified code. It also offers improved version control, customization, and compliance, helping teams maintain consistency and enforce governance across different environments.

By centralizing the management of Terraform modules, teams can ensure they are using standardized, reliable code while retaining flexibility to adapt to specific needs.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/private-registry/registry_menu.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=86eed0a5bf0f6eada751f82de625ec8d" alt="Private registry menu interface showing module management options" width="482" height="834" data-path="images/guides/admin-guide/private-registry/registry_menu.png" />
</Frame>

<img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/private-registry/modules_tab.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=6490c13dd460bf59a687c2ac5686db2f" alt="" width="1487" height="772" data-path="images/guides/admin-guide/private-registry/modules_tab.png" />

## Adding a module to the registry

In order to add a module to your registry, go to the Module Registry screen and click on “CREATE NEW MODULE” in the top right. Only organization administrators are authorized to create new modules.

<img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/private-registry/271bba4-2.jpg?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=700d35b6598bafbc35df2334de3fc86d" alt="" width="1413" height="453" data-path="images/guides/admin-guide/private-registry/271bba4-2.jpg" />

First, you must enter the general details for your module:

* A name for your module - This can be any string of your choice.
* The provider the module belongs to - This too can be any string of your choice.

These two choices will affect how your module is used (see 'Using a module in your code'). The combination of name and provider must be unique within your organization’s modules.

The description will be shown to members of your team when they browse the module registry. It is a useful way of summarizing what the module does and when it should be used.

<img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/private-registry/5baa027-image.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=7ace20c33d2ccfc0c77f4873525a3623" alt="" width="1497" height="802" data-path="images/guides/admin-guide/private-registry/5baa027-image.png" />

Next, you must connect to the VCS provider, where your module’s source code is stored.

Click on the VCS provider you'd like to use. After you've authorized env zero to access your repositories, select a repository from the dropdown menu and enter the folder where module files are stored (defaults to root folder).

That’s it! Click “Create” to save your work and create the new module.

## Module versioning

In order to use a module, it must be versioned using a SemVer format (e.g. `1.0.0`). The versions must be applied to your source repository as [Git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging).

### Versioning modules for mono-repo

When using a mono-repo for managing several modules, a team might come across the need to tag and manage versions for each module individually.

In order to do that, you have to assign a tag prefix to identify a specific module's version in env zero.

<img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/private-registry/58f2b8d-image.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=5fa3148b4115d4f89114f6952185e597" alt="" width="1503" height="802" data-path="images/guides/admin-guide/private-registry/58f2b8d-image.png" />

For example, to tag a module named `module1`, we may assign the prefix `m1`.\
When we'd use the tags `m1/1.0.0`, `m1/1.2.4`, the versions for the module in env zero will be `1.0.0` and `1.2.4`

The delimiter is a single dash / and there is no need to write it in the Tag Prefix input.

<Info>
  **Terraform restrictions on tags**

  Terraform enforces using a valid SemVer string as a version. Tagging with a prefix will only allow you to use the SemVer part and not the tag directly when using a module from env zero's private registry that is configured to use the tag prefix.
</Info>

## Using a module in your code

In order to use a module from the env zero Module Registry in your Terraform code, you must reference it like this:

```hcl  theme={null}
module "my-module" {
  source = "api.env0.com/{organization-id}/{module-name}/{module-provider}"
  version = "1.0.0"
}
```

You can find this exact snippet, pre-filled with your values, in the Instructions tab of your module page.

<Note>
  **Using a module from Gitlab Enterprise Edition or BitBucket Server**

  In order to enable Gitlab Enterprise or Bitbucket Server as a module registry you are required to set an [env zero custom flow](/guides/admin-guide/custom-flows) that will run the following command on after setup variables.

  ```bash  theme={null}
  git config --global url.https://$ENV0_VCS_ACCESS_TOKEN@$GIT_ADDR/.insteadOf https://$GIT_ADDR/
  ```

  This command will instruct git CLI to use the authorized URL for checking out the code, where `ENV0_VCS_ACCESS_TOKEN` is an environment variable populated by env zero with the access token for the VCS system and `GIT_ADDR` is the domain of your VCS.

  ```yaml env0.yml theme={null}
  version: 2
   
  deploy:
    steps:  
      setupVariables:  
        after:  
          - export GIT_ADDR="mygleeserver.example"  
          - git config --global url.https://$ENV0_VCS_ACCESS_TOKEN@$GIT_ADDR/.insteadOf https://$GIT_ADDR/
  ```

</Note>

## Using a module locally (or from a different env zero Organization)

When you deploy your Terraform code through env zero, login to the env zero Module Registry is handled for you. If you'd like to run the same code locally, in a CI environment, or in a different env zero Organization, you will need to supply the authentication details to Terraform. Follow the guide on [how to authorize when using a private registry](/guides/admin-guide/private-registry/#authorization) for more info.

## The Modules List

The Modules List page is available to every user in the organization by clicking on “Module Registry” in the organization’s menu (bottom left of the screen).

On this page you can see which modules have been set up for your organization. You can use the search box to locate specific modules by name, provider, description, or the users who created them.

<img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/private-registry/e5ea366-modules_list.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=6d08247726286fe88f3bd08f59e013f9" alt="" width="1570" height="879" data-path="images/guides/admin-guide/private-registry/e5ea366-modules_list.png" />

## The Module Page

You can get to the Module page by clicking on a module from the Modules List.

<img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/private-registry/b8f9132-5.jpg?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=9b10361256d3c3d3bcd7832624239679" alt="" width="1434" height="585" data-path="images/guides/admin-guide/private-registry/b8f9132-5.jpg" />

Here you can see the details of your Module.

The Versions dropdown menu at the top right allows you to switch between the different versions of your module. Versions are linked to [Git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) in your repository, which match the [semantic versioning](https://semver.org/) schema.

The **Readme tab** will show the contents of the `README.md` in your repository.

The **Instructions tab** will include instructions on how the module can be used in your Terraform code.

<Warning>
  **HTML in README**

  For security reasons, HTML tags such as `<a>` or `<div>` will be rendered as regular text inside the README tab.

  If you would like to have a link for example, please use the markdown syntax (e.g. `[link text](http://example-link.com/)`) rather than the HTML syntax (e.g. `<a href="http://example-link.com/">link text</a>` )
</Warning>

## Submodules

Rather than creating a dedicated repository for each module, you can create a single repository and place submodules within this larger repository.  Using the submodules in code is achieved in the same way as referencing submodules within Git – by using the double slash; "//" and then folder location.

```hcl  theme={null}
module "my-module" {
  source = "api.env0.com/{organization-id}/{module-name}/{module-provider}//submodule"
  version = "1.0.0"
}
```

## Finding My Module ID

Sometimes you may need your module ID for our [terraform provider](https://registry.terraform.io/providers/env0/env0/latest) or for some [API calls](/api-reference/getting-started/authentication).

You can find it in the Module card in the `Modules` tab under the `Registry` page.

<img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/private-registry/5a50d57-image.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=4242af675fedce88d674430fa8161d2a" alt="" width="1471" height="170" data-path="images/guides/admin-guide/private-registry/5a50d57-image.png" />

## Suggested Blog Content

[Terraform Modules Guide](https://www.env0.com/blog/terraform-modules)

[Terraform Plan Examples](https://www.env0.com/blog/terraform-plan)

[Managing Terraform Variable Hierarchy](https://www.env0.com/blog/managing-terraform-variable-hierarchy)

[Manage Terraform Remote State with a Remote Backend](https://www.env0.com/blog/terraform-remote-state-using-a-remote-backend)

Built with [Mintlify](https://mintlify.com).
