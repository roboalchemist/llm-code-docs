# Source: https://docs.mage.ai/production/executors/aws.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# AWS ECS executor

> Execute block runs in separate tasks.

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

You can choose to launch separate AWS ECS tasks to executor blocks by specifying
block executor\_type to be `ecs` in pipeline's metadata.yaml file.

There're 2 ways to customize the ECS executor config,

1. Specify the `ecs_config` in project's metadata.yaml file. Example config:

   ```yaml  theme={"system"}
   ecs_config:
     cpu: 1024
     memory: 2048
   ```

   2. Add the `executor_config` at block level in pipeline's metadata.yaml file. Example config:

   ```yaml  theme={"system"}
   blocks:
   - uuid: example_data_loader
     type: data_loader
     upstream_blocks: []
     downstream_blocks: []
     executor_type: ecs
     executor_config:
       cpu: 1024
       memory: 2048
   ```

To run the whole pipeline in one ECS executor, you can set the `executor_type` at pipeline level and set `run_pipeline_in_one_process` to true.
`executor_config` can also be set at pipeline level. Here is the example pipeline metadata.yaml:

```yaml  theme={"system"}
blocks:
- ...
- ...
executor_type: ecs
run_pipeline_in_one_process: true
name: example_pipeline
...
```

## Configurations

| Field name               | Description                                                                                                                                       | Example values              |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| assign\_public\_ip       | Whether to assign public IP to the ECS task.                                                                                                      | true/false (default: true)  |
| cpu                      | The CPU allocated to the ECS task.                                                                                                                | 1024                        |
| enable\_execute\_command | Whether to [enable execute command for debugging](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html)                      | true/false (default: false) |
| launch\_type             | The launch type of the ECS task.                                                                                                                  | FARGATE                     |
| memory                   | The memory allocated to the ECS task.                                                                                                             | 2048                        |
| tags                     | The tags of the ECS task.                                                                                                                         | \['tag1', 'tag2']           |
| wait\_timeout            | The maximum wait time for the ECS task (in seconds). The default wait timeout for the ECS task is 10 minutes. Setting to -1 will disable waiting. | 1200 (default: 600)         |

### Example

```yaml  theme={"system"}
ecs_config:
  cpu: 1024
  memory: 2048
  assign_public_ip: false
  enable_execute_command: true
  wait_timeout: 1200
```

## IAM permissions

Required IAM permissions for using ECS executor:

```json  theme={"system"}
[
  "ec2:DescribeNetworkInterfaces",
  "ecs:DescribeTasks",
  "ecs:ListTasks",
  "ecs:RunTask",
  "iam:PassRole"
]
```

***

## Resource management

<Card title="Get started for free" href={`${urls.pro}?source=aws-executor`}>
  <img src="https://mage-ai.github.io/assets/pro/banner-light.png" className="hidden dark:block" noZoom />

  <img src="https://mage-ai.github.io/assets/pro/banner-dark.png" className="block dark:hidden" noZoom />

  <br />

  A fully managed service, where we maintain the infrastructure, guarantee uptime,
  automatically scale your workloads to handle any volume of pipeline runs,
  automatically upgrade new versions of Mage Pro only features,
  monitor your production pipelines, and provide enterprise level support.
</Card>

<br />

<ProButton source="aws-executor" />


Built with [Mintlify](https://mintlify.com).