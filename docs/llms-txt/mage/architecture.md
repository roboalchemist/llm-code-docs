# Source: https://docs.mage.ai/production/deploying-to-cloud/architecture.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Architecture

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

<ProBanner source="architecture" />

<Frame caption="Mage architecture diagram">
  <img alt="Mage OSS rchitecture" diagram src="https://mage-ai.github.io/assets/mage-architecture.png" />
</Frame>

## Server

Mage server runs in an instance or container. Here are the responsibilities of the Mage server.

* Handle all the API requests.
* Interact with the storage to read and write data.
* Run the websocket server to handle websocket requests.
* Execute the pipeline code in the kernel.
* Handle user authentication.

Mage server creates the scheduler process once the server starts. The scheduler process is responsible for
scheduling pipeline runs for active pipeline triggers.

## Storage

In the storage layer, Mage stores the following data:

* **Code files**: Mage stores code files on the local disk. You can use [git](/production/data-sync/git-integration) to sync the code between your local disk and remote the git repository. If you deploy Mage in containers, you can mount an Network File System share in your container to persist the code and data on your disk.
* **Data and log files**: By default, Mage stores data and log files on the local disk. You can also configure it to store [logs](/development/observability/logging#logging-to-external-destination) in an external storage.
* **Pipeline Trigger, Pipeline Run, User data, etc**.: Orchestration related objects and authentication related objects are stored in a database. By default, Mage uses a local SQLite database. In a production environment, You can configure Mage to use a [Postgres database](/production/configuring-production-settings/overview#databases).
* **Secrets**: Mage supports storing [secrets](/development/variables/secrets) in the database. It's also recommended to use an external [Secret Manager](/production/deploying-to-cloud/secrets/AWS) to store secrets.

## Executors

Mage supports different types of executors to execute jobs:

* Local process executor
* ECS executor (AWS)
* GCP Cloud Run executor
* Kubernetes executor

Check out this [doc](/production/configuring-production-settings/compute-resource#2-customize-the-compute-resource-of-the-mage-executor) to learn about how to configure these executors.

## Scale web server and schedulers

By default, Mage runs the web server and scheduler in the same container. Mage supports horizontally scaling by separating the web server and scheduler,
and run multiple replicas of web servers and schedulers.

To separate the web server and scheduler, you can override the container command with the commands below:

* Run scheduler only (The scheduler doesn't need dedicated IP and port)
  ```bash  theme={"system"}
  /app/run_app.sh mage start project_name --instance-type scheduler
  ```
* Run web server only
  ```bash  theme={"system"}
  /app/run_app.sh mage start project_name --instance-type web_server
  ```

To run multiple schedulers simultaneously, you will need to specify the `REDIS_URL` environment variable in your container. The Redis storage is used to coordinate the job scheduling between multiple containers to resolve race conditions. Here is an example Redis URL format: `redis://redis:6379/0`

## Autoscaling

Do you want to run your pipelines at any scale without having to deal with infrastructure setup,
configurations, deployment, and maintenance?

1. Autoscaling orchestration scheduler for maximum pipeline trigger frequency
2. Vertical and horizontal autoscaling data pipelines and block run executions

<ProOnly source="autoscaling" />


Built with [Mintlify](https://mintlify.com).