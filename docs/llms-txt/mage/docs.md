# Source: https://docs.mage.ai/guides/dbt/docs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Serve dbt docs in production

> To serve dbt docs in production, you will need to enable a container to host the dbt docs webserver in the cloud service you are using.

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

## Mage Pro (auto-generate and serve)

<ProOnly source="dbt" />

If you're using Mage Pro, dbt docs can be automatically generated and served when the app starts.

* Set the environment variable `ENABLE_DBT_DOCS=true`.
* Mage will discover dbt projects under `/dbt`, generate docs (if missing), and serve them.
* Open a project's docs from the UI:
  * In File Browser, right-click the dbt project folder and click "Open dbt docs".
  * The docs are available at `/dbt_docs/[dbt_project_name]`.
  * The path `/dbt_docs` shows the status for all dbt projects (running port, errors, etc.).

To regenerate docs manually, add a generic dbt block in a pipeline and run `dbt docs generate`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/0zB2Sc5BCBM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

## Generating docs

Before enabling dbt docs in production, we need to make sure the static files for the docs are generated.

1. Configure the dbt super project.
   * Your dbt projects should be in the `/path/to/<mage_project>/dbt` directory.
     * The `/dbt` directory will serve as a "super-project" for all of your dbt projects in your Mage project.
   * Make sure the `/.../<mage_project>/dbt` directory has the files `dbt_project.yml`, `profiles.yml`, and `packages.yml`. These files are needed for dbt to create docs for all the projects within this directory.
     1. `dbt_project.yml`
        ```yaml  theme={"system"}
        name: 'base'
        version: '1.0.0'
        config-version: 2
        profile: 'base'
        target-path: "target"
        clean-targets:
          - "target"
          - "dbt_packages"
        ```
     2. `profiles.yml`: The config in this file is not used, but it needs to still be a valid output target in order for the project to compile.
        ```yaml  theme={"system"}
        base:
          target: dev
          outputs:
            dev:
              <output_config>
        ```
     3. `packages.yml`: Add all projects that you want to be included in the documentation.
        ```yaml  theme={"system"}
        packages:
          - local: ./project1
          - local: ./project2
        ```
2. Generate the dbt docs
   ```bash  theme={"system"}
     dbt deps
     dbt docs generate
   ```

## Terraform

### GCP

In the [mage-ai-terraform-templates](https://github.com/mage-ai/mage-ai-terraform-templates) repository, the terraform templates for GCP have commented out resources at the end of the following files for enabling the dbt docs service.

* [main.tf](https://github.com/mage-ai/mage-ai-terraform-templates/blob/master/gcp/main.tf#L184)
* [load\_balancer.tf](https://github.com/mage-ai/mage-ai-terraform-templates/blob/master/gcp/load_balancer.tf#L81)

Once you uncomment those resources, you should see an output `docs_service_ip` at the end of `terraform apply` with the IP to access the dbt docs in the cloud.

```bash  theme={"system"}
Outputs:
docs_service_ip = "<dbt_docs_ip>"
service_ip = "<mage_ip>"
```

### AWS

Coming soon...


Built with [Mintlify](https://mintlify.com).