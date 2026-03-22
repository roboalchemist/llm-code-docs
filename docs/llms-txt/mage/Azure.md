# Source: https://docs.mage.ai/production/executors/azure.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure Container Instance executor

> Execute block runs in separate container instances.

export const urls = {
  chat: 'https://www.mage.ai/chat',
  oss: 'https://www.mage.ai/oss',
  pro: 'https://cloud.mage.ai/sign-up'
};

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

If your Mage app is deployed on Microsoft Azure with Mage’s [Terraform](https://github.com/mage-ai/mage-ai-terraform-templates/tree/master/azure)
scripts, you can choose to launch separate Azure container instances to execute blocks.

How to configure pipeline to use Azure Container Instance executor:

1. Update Project's metadata.yaml

```yaml  theme={"system"}
azure_container_instance_config:
  cpu: 1
  memory: 2
```

2. Update the `executor_type` of the block to `azure_container_instance` in pipeline's metadata.yaml and specify `executor_config` optionally.
   The block level executor\_config will override the global executor\_config.

```yaml  theme={"system"}
blocks:
- uuid: example_data_loader
  type: data_loader
  upstream_blocks: []
  downstream_blocks: []
  executor_type: azure_container_instance
  executor_config:
    cpu: 1
    memory: 2
  ...
```

***

## Resource management

<Card title="Get started for free" href={`${urls.pro}?source=azure-executor`}>
  <img src="https://mage-ai.github.io/assets/pro/banner-light.png" className="hidden dark:block" noZoom />

  <img src="https://mage-ai.github.io/assets/pro/banner-dark.png" className="block dark:hidden" noZoom />

  <br />

  A fully managed service, where we maintain the infrastructure, guarantee uptime,
  automatically scale your workloads to handle any volume of pipeline runs,
  automatically upgrade new versions of Mage Pro only features,
  monitor your production pipelines, and provide enterprise level support.
</Card>

<br />

<ProButton source="azure-executor" />


Built with [Mintlify](https://mintlify.com).