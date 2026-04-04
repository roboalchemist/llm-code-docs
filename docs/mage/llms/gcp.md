# Source: https://docs.mage.ai/production/executors/gcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GCP Cloud Run executor

> Execute block runs in separate jobs.

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

If your Mage app is deployed on GCP Cloud Run, you can choose to launch separate GCP Cloud Run jobs to execute blocks.

How to configure pipeline to use GCP cloud run executor:

1. Update Project's metadata.yaml

```yaml  theme={"system"}
gcp_cloud_run_config:
  path_to_credentials_json_file: "/path/to/credentials_json_file"
  project_id: project_id
  timeout_seconds: 600
```

2. Update the `executor_type` of block to `gcp_cloud_run` in pipeline's metadata.yaml:

```yaml  theme={"system"}
blocks:
- uuid: example_data_loader
  type: data_loader
  upstream_blocks: []
  downstream_blocks: []
  executor_type: gcp_cloud_run
  ...
```

Customizing compute resource for GCP Cloud Run executor is coming soon.

***

## Resource management

<Card title="Get started for free" href={`${urls.pro}?source=gcp-executor`}>
  <img src="https://mage-ai.github.io/assets/pro/banner-light.png" className="hidden dark:block" noZoom />

  <img src="https://mage-ai.github.io/assets/pro/banner-dark.png" className="block dark:hidden" noZoom />

  <br />

  A fully managed service, where we maintain the infrastructure, guarantee uptime,
  automatically scale your workloads to handle any volume of pipeline runs,
  automatically upgrade new versions of Mage Pro only features,
  monitor your production pipelines, and provide enterprise level support.
</Card>

<br />

<ProButton source="gcp-executor" />


Built with [Mintlify](https://mintlify.com).