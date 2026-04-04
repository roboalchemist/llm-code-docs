# Source: https://docs.mage.ai/production/configuring-production-settings/compute-resource.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Compute resources

export const ProBanner = ({button = 'Try Mage Pro for free', description, source = 'documentation', title = 'Our fully managed solution for teams is now available!'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        {description && <br />}
        {description && <p className="normal">{description}</p>}
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

<ProBanner source="compute-resources" description="Mage Pro will automatically scale your workloads to handle any volume of pipeline runs, while optimizing resource utilization and minimizing costs." />

Follow the instructions in this [document](/production/deploying-to-cloud/using-terraform) to deploy
Mage in a production environment. When running Mage in production,
you can customize the compute resource for the following services:

1. Front-end application
2. Pipeline executor
3. Block executor

## Front-end application

Customize the compute resource of the Mage web service.

The Mage web service is responsible for running Mage web backend, scheduler service
and local block executions.

You can customize the CPU and memory of the Mage web
service by updating the Terraform variables and then running `terraform apply`.

### Amazon Web Services (AWS)

Update the `ecs_task_cpu` and `ecs_task_memory` variables in the
[`mage-ai-terraform-templates/aws/variables.tf`](https://github.com/mage-ai/mage-ai-terraform-templates/blob/master/aws/variables.tf)
file.

### Google Cloud Platform (GCP)

Update the `container_cpu` and `container_memory` variables in the
[`mage-ai-terraform-templates/gcp/variables.tf`](https://github.com/mage-ai/mage-ai-terraform-templates/blob/master/gcp/variables.tf)
file.

***

## Pipeline executor

Set the pipeline’s executor type to customize the compute resources for pipeline runs.
Here are the available executor types:

* `local_python`
* `k8s`
* `ecs`

### Default for all blocks in a pipeline

You can set the executor type for all the blocks in a pipeline by specifying the `executor_type` at pipeline level.

***

## Block executor

Mage provides multiple executors to execute blocks.
Here are the available executor types:

* `local_python`
* `k8s`
* `ecs`
* `azure_container_instance`
* `gcp_cloud_run`

### Default for all blocks

Mage uses `local_python` executor type by default. If you want to specify another executor\_type as the default executor type for blocks,
you can set the environment variable `DEFAULT_EXECUTOR_TYPE` to one executor type mentioned above.


Built with [Mintlify](https://mintlify.com).