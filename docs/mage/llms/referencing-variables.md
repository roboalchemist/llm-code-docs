# Source: https://docs.mage.ai/development/variables/referencing-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Accessing variables in Mage

> You've got all of these great variables and secrets, now let's put them to use. Learn how to access them in your code. 🦸🏻‍♂️

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

Mage allows users to interpolate variables specific to your [pipeline](/getting-started/runtime-variable) or [project](/development/variables/environment-variables). The following syntax is specific to `yaml` and `SQL` files.

Here's a list of the different variables and functions you can use in your code:

| Syntax                              | Description                                                                            |
| ----------------------------------- | -------------------------------------------------------------------------------------- |
| `{{ env_var('secret') }}`           | Get secret from [environment variables](/development/variables/environment-variables). |
| `{{ variables('secret') }}`         | Get secret from [runtime variables](/getting-started/runtime-variable).                |
| `{{ mage_secret_var('secret') }}`   | Get secret from [Mage secrets](/development/variables/secrets).                        |
| `{{ aws_secret_var('secret') }}`    | Get secret from [AWS Secrets Manager](/production/deploying-to-cloud/secrets/AWS).     |
| `{{ azure_secret_var('secret') }}`  | Get secret from [Azure Key Vault](/production/deploying-to-cloud/secrets/Azure).       |
| `{{ json_value(json_obj, 'key') }}` | Extract value from a JSON string.                                                      |
| `{{ n_days_ago(N) }}`               | Get the date `N` days ago (data integration pipelines only).                           |

## Mage Pro only variable syntax

<ProOnly source="variables" />

| Syntax                           | Description                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `{{ file('path/to/file.txt') }}` | Load the contents of a [local file](/development/variables/referencing-variables#file-content-syntax). |

### File content syntax

This is useful for dynamically loading configuration files, secrets, or text assets during pipeline execution.
The path can be either absolute path or relative path to the project.

**Example Usage**

```jinja  theme={"system"}
{{ file('secrets.txt') }}`
{{ file('/home/src/default_repo/settings.json') }}`
```

If you want to get a json field from the local file, you can use it together with the `json_value` syntax like

```
{{ json_value(file('path/to/file.json'), 'key') }}`
```


Built with [Mintlify](https://mintlify.com).