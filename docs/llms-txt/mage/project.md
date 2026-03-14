# Source: https://docs.mage.ai/extensibility/env-config/project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Project configuration environment overrides

> Add environment-specific overrides for your project configuration.

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

<ProOnly source="env-specific-config" />

### Location of project configuration

Each project in Mage has a `metadata.yaml` configuration file located in the
project's root directory. For example, if you had a project called `your_project`,
the folder structure for that project might look something like this:

```
your_project/
├─ pipelines/
├─ data_loaders/
├─ transformers/
├─ data_exporters/
├─ .../
├─ io_config.yaml
├─ metadata.yaml
├─ requirements.txt
├─ ...
```

### **Override project config based on environment**

In the project's `metadata.yaml` config file, add an `overrides` key at the top-level
(no indentations) with the name of your environment (e.g. `prod`, `dev`, `test`) under
the `overrides` key and indented once. Then under the environment name key, add the
properties of your base project config that you want to override. Make sure the
indentations of the properties match those of the base config. Any environment-specific
overrides will REPLACE the matching property in the base config, so be careful when
overriding properties with nested values.

<Note>
  The environment name should match the environment defined in the `ENV`
  [environment variable](https://docs.mage.ai/development/variables/environment-variables).
</Note>

### Example project config file with environment overrides

```yaml  theme={"system"}
# your_project/metadata.yaml
project_type: standalone

variables_dir: ~/.mage_data
remote_variables_dir: s3://bucket/path_prefix

variables_retention_period: '90d'

emr_config:
  master_instance_type: 'r5.4xlarge'
  slave_instance_type: 'r5.4xlarge'
  master_security_group: 'sg-xxxxxxxxxxxx'
  slave_security_group: 'sg-yyyyyyyyyyyy'
  ec2_key_name: '[ec2_key_pair_name]'

spark_config:
  app_name: 'my spark app'
  spark_master: 'local'
  executor_env: {}
  spark_jars: []
  spark_home:
  others: {}
  use_custom_session: false
  custom_session_var_name: 'spark'

help_improve_mage: true
notification_config:
  alert_on:
  - trigger_failure
  - trigger_passed_sla
  slack_config:
    webhook_url: "{{ env_var('MAGE_SLACK_WEBHOOK_URL') }}"
  teams_config:
    webhook_url: "{{ env_var('MAGE_TEAMS_WEBHOOK_URL') }}"
project_uuid: 123456781234abcd1234abcde123456
features:
  add_new_block_v2: true
  code_block_v2: true
  command_center: true
  custom_design: true
  data_integration_in_batch_pipeline: true
  dbt_v2: true
  interactions: true
  display_local_timezone: true
  notebook_block_output_split_view: true
  operation_history: true
  polars: true
  automatic_kernel_cleanup: false
pipelines:
  settings:
    triggers:
      save_in_code_automatically: true

overrides:
  dev:
    help_improve_mage: false
    pipelines:
      settings:
        triggers:
          save_in_code_automatically: false
    features:
      automatic_kernel_cleanup: true
      global_hooks: true
```

In the example above when in the `dev` environment, the project's nested configuration
property of `save_in_code_automatically` will be overridden to be `false` (instead of
`true` as defined in the base config). The other properties (i.e. `help_improve_mage`,
`automatic_kernel_cleanup`, and `global_hooks`) will also be overridden.
Other environments (not `dev`) will not utilize the `overrides` section.


Built with [Mintlify](https://mintlify.com).