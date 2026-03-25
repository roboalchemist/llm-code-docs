# Source: https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops

Title: Define variables - Azure Pipelines

URL Source: https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

Variables provide a convenient way to include key data in various parts of the pipeline. The most common use of variables is to define a value that you can use throughout your pipeline. All variables are strings and are mutable. The value of a variable can change from run to run or job to job in your pipeline.

When you define the same variable in multiple places with the same name, the most locally scoped variable takes precedence. So, a variable defined at the job level can override a variable set at the stage level. A variable defined at the stage level overrides a variable set at the pipeline root level. A variable set in the pipeline root level overrides a variable set in the Pipeline settings UI. To learn more about how to work with variables defined at the job, stage, and root level, see [Variable scope](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#variable-scopes).

You can use variables with [expressions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/expressions?view=azure-devops) to conditionally assign values and further customize pipelines.

Variables differ from [runtime parameters](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/runtime-parameters?view=azure-devops). Runtime parameters are typed and available during template parsing.

When you define a variable, use [different syntaxes (macro, template expression, or runtime)](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#understand-variable-syntax). The syntax you choose determines where in the pipeline your variable renders.

In YAML pipelines, set variables at the root, stage, and job levels. You can also specify variables outside of a YAML pipeline in the UI. When you set a variable in the UI, you can encrypt the variable and set it as secret.

User-defined variables can be [set as read-only](https://learn.microsoft.com/en-us/azure/devops/pipelines/security/inputs?view=azure-devops). There are [naming restrictions for variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#variable-naming-restrictions) (example: you can't use `secret` at the start of a variable name).

You can [use a variable group](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups?view=azure-devops) to make variables available across multiple pipelines.

To define variables in one file for use in multiple pipelines, use [templates](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/templates?view=azure-devops).

Azure DevOps supports multi-line variables but there are a few limitations.

Downstream components such as pipeline tasks might not handle the variable values correctly.

Azure DevOps doesn't alter user-defined variable values. You need to format variable values correctly before passing them as multi-line variables. When formatting your variable, avoid special characters, don't use restricted names, and make sure you use a line ending format that works for the operating system of your agent.

Multi-line variables behave differently depending on the operating system. To avoid this problem, make sure that you format multi-line variables correctly for the target operating system.

Azure DevOps never alters variable values, even if you provide unsupported formatting.

In addition to user-defined variables, Azure Pipelines has system variables with predefined values. For example, the predefined variable [Build.BuildId](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops#build-variables-devops-services) gives the ID of each build and can be used to identify different pipeline runs. You can use the `Build.BuildId` variable in scripts or tasks when you need to a unique value.

If you're using YAML or classic build pipelines, see [predefined variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops) for a comprehensive list of system variables.

If you're using classic release pipelines, see [release variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/release/variables?view=azure-devops).

When you run the pipeline, the system variables set their current value. Some variables are set automatically. As a pipeline author or end user, you can change the value of a system variable before the pipeline runs.

System variables are read-only.

Environment variables are specific to the operating system you're using. You inject them into a pipeline in platform-specific ways. The format corresponds to how environment variables get formatted for your specific scripting platform.

On UNIX systems (macOS and Linux), environment variables have the format `$NAME`. On Windows, the format is `%NAME%` for batch and `$env:NAME` in PowerShell.

System and user-defined variables (except secret variables) also get injected as environment variables for your platform. When variables convert into environment variables, variable names become uppercase, and periods turn into underscores. For example, the variable name `any.variable` becomes the variable name `$ANY_VARIABLE`.

There are [variable naming restrictions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#variable-naming-restrictions) for environment variables (example: you can't use `secret` at the start of a variable name).

User-defined and environment variables can consist of letters, numbers, `.`, and `_` characters. Don't use variable prefixes reserved by the system. These prefixes are: `endpoint`, `input`, `secret`, `path`, and `securefile`. Any variable that begins with one of these strings (regardless of capitalization) won't be available to your tasks and scripts. Don't use spaces in variables. For additional constraints, see [Azure Pipelines naming restrictions](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/naming-restrictions?view=azure-devops#azure-pipelines).

Azure Pipelines supports three different ways to reference variables: macro, template expression, and runtime expression. You can use each syntax for a different purpose and each has some limitations.

In a pipeline, template expression variables (`${{ variables.var }}`) get processed at compile time, before runtime starts. Macro syntax variables (`$(var)`) get processed during runtime before a task runs. Runtime expressions (`$[variables.var]`) also get processed during runtime but are intended to be used with [conditions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/conditions?view=azure-devops) and [expressions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/expressions?view=azure-devops). When you use a runtime expression, it must take up the entire right side of a definition.

In this example, you can see that the template expression still has the initial value of the variable after the variable is updated. The value of the macro syntax variable updates. The template expression value doesn't change because the pipeline processes all template expression variables at compile time before tasks run. In contrast, macro syntax variables evaluate before each task runs.

```
variables:
- name: one
  value: initialValue 

steps:
  - script: |
      echo ${{ variables.one }} # outputs initialValue
      echo $(one)
    displayName: First variable pass
  - bash: echo "##vso[task.setvariable variable=one]secondValue"
    displayName: Set new variable value
  - script: |
      echo ${{ variables.one }} # outputs initialValue
      echo $(one) # outputs secondValue
    displayName: Second variable pass
```

Most documentation examples use macro syntax (`$(var)`). Use macro syntax to interpolate variable values into task inputs and into other variables.

The system processes variables with macro syntax before a task executes during runtime. Runtime happens [after template expansion](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/runs?view=azure-devops#process-the-pipeline). When the system encounters a macro expression, it replaces the expression with the contents of the variable. If there's no variable by that name, the macro expression doesn't change. For example, if `$(var)` can't be replaced, it remains as `$(var)`.

Macro syntax variables remain unchanged when they have no value because an empty value like `$()` might mean something to the task you're running and the agent shouldn't assume you want that value replaced. For example, if you use `$(foo)` to reference variable `foo` in a Bash task, replacing all `$()` expressions in the input to the task could break your Bash scripts.

Macro variables only expand when they're used for a value, not as a keyword. Values appear on the right side of a pipeline definition. The following is valid: `key: $(value)`. The following isn't valid: `$(key): value`. Macro variables aren't expanded when used to display a job name inline. Instead, you must use the `displayName` property.

Note

The system only expands macro syntax variables for **task inputs** within `stages`, `jobs`, and `steps`. It **doesn't** expand them in pipeline keywords that resolve at compile time, such as `resources`, `trigger`, or the `checkout` step's repository reference value (for example, `checkout: git://MyProject/MyRepo@$(var)` doesn't work). To parameterize these values, use [template expressions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/template-expressions?view=azure-devops) (`${{ }}`) or [runtime parameters](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/runtime-parameters?view=azure-devops) instead.

This example uses macro syntax with Bash, PowerShell, and a script task. The syntax for calling a variable by using macro syntax is the same for all three.

```
variables:
 - name: projectName
   value: contoso

steps: 
- bash: echo $(projectName)
- powershell: echo $(projectName)
- script: echo $(projectName)
```

Use template expression syntax to expand both [template parameters](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/template-parameters?view=azure-devops) and variables (`${{ variables.var }}`). The system processes template variables at compile time, and replaces them before runtime starts. Use template expressions for reusing parts of YAML as templates.

Template variables silently coalesce to empty strings when a replacement value isn't found. Template expressions, unlike macro and runtime expressions, can appear as either keys (left side) or values (right side). The following is valid: `${{ variables.key }} : ${{ variables.value }}`.

Use runtime expression syntax for variables that expand at runtime (`$[variables.var]`). Runtime expression variables silently coalesce to empty strings when a replacement value isn't found. Use runtime expressions in job conditions to support conditional execution of jobs or whole stages.

Runtime expression variables only expand when they're used for a value, not as a keyword. Values appear on the right side of a pipeline definition. The following is valid: `key: $[variables.value]`. The following isn't valid: `$[variables.key]: value`. The runtime expression must take up the entire right side of a key-value pair. For example, `key: $[variables.value]` is valid but `key: $[variables.value] foo` isn't.

| Syntax | Example | When is it processed? | Where does it expand in a pipeline definition? | How does it render when not found? |
| --- | --- | --- | --- | --- |
| macro | `$(var)` | runtime before a task executes | value (right side) | prints `$(var)` |
| template expression | `${{ variables.var }}` | compile time | key or value (left or right side) | empty string |
| runtime expression | `$[variables.var]` | runtime | value (right side) | empty string |

Use macro syntax if you're providing a secure string or a [predefined variable](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables) input for a task.

Choose a runtime expression if you're working with [conditions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/conditions?view=azure-devops) and [expressions](expressions.md]. However, don't use a runtime expression if you don't want your empty variable to print (example: `$[variables.var]`). For example, if you have conditional logic that relies on a variable having a specific value or no value, use a macro expression.

Typically, a template variable is the standard to use. By leveraging template variables, your pipeline fully injects the variable value into your pipeline at pipeline compilation. This injection is helpful when attempting to debug pipelines. You can download the log files and evaluate the fully expanded value that is being substituted in. Since the variable is substituted in, don't leverage template syntax for sensitive values.

This example prompt for Copilot Chat identifies what types of variables are used in a pipeline and when the variables resolve. Highlight your YAML code and then enter the following Copilot Chat prompt.

```
What types of Azure DevOps variables are used in this YAML pipeline? Give specific examples.
When does each variable process in the pipeline? 
How will each variable render when not found? 
What stages and jobs will the variables be available for?
```

Customize your prompt to add specifics as needed.

Copilot is powered by AI, so surprises and mistakes are possible. For more information, see [Copilot FAQs](https://aka.ms/copilot-general-use-faqs).

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_1_yaml)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_1_classic)
*   [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_1_azure-devops-cli)

In the most common case, set the variables and use them within the YAML file. This approach lets you track changes to the variable in your version control system. You can also define variables in the pipeline settings UI (see the Classic tab) and reference them in your YAML.

The following example shows how to set two variables, `configuration` and `platform`, and use them later in steps. To use a variable in a YAML statement, wrap it in `$()`. You can't use variables to define a `repository` in a YAML statement.

```
# Set variables once
variables:
  configuration: debug
  platform: x64

steps:

# Use them once
- task: MSBuild@1
  inputs:
    solution: solution1.sln
    configuration: $(configuration) # Use the variable
    platform: $(platform)

# Use them again
- task: MSBuild@1
  inputs:
    solution: solution2.sln
    configuration: $(configuration) # Use the variable
    platform: $(platform)
```

In the YAML file, set a variable at various scopes:

*   At the root level, to make it available to all jobs in the pipeline.
*   At the stage level, to make it available only to a specific stage.
*   At the job level, to make it available only to a specific job.

When you define a variable at the top of a YAML, the variable is available to all jobs and stages in the pipeline and is a global variable. Global variables defined in a YAML aren't visible in the pipeline settings UI.

Variables at the job level override variables at the root and stage level. Variables at the stage level override variables at the root level.

```
variables:
  global_variable: value    # this is available to all jobs

jobs:
- job: job1
  pool:
    vmImage: 'ubuntu-latest'
  variables:
    job_variable1: value1    # this is only available in job1
  steps:
  - bash: echo $(global_variable)
  - bash: echo $(job_variable1)
  - bash: echo $JOB_VARIABLE1 # variables are available in the script environment too

- job: job2
  pool:
    vmImage: 'ubuntu-latest'
  variables:
    job_variable2: value2    # this is only available in job2
  steps:
  - bash: echo $(global_variable)
  - bash: echo $(job_variable2)
  - bash: echo $GLOBAL_VARIABLE
```

The output from both jobs looks like this:

```
# job1
value 
value1
value1

# job2
value
value2
value
```

In the preceding examples, the `variables` keyword is followed by a list of key-value pairs. The keys are the variable names and the values are the variable values.

Another syntax is useful when you want to use [templates](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/templates?view=azure-devops) for variables or [variable groups](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups?view=azure-devops).

By using [templates](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/templates?view=azure-devops#variable-reuse), you can define variables in one YAML file and include them in another YAML file.

Variable groups are a set of variables that you can use across multiple pipelines. By using variable groups, you can manage and organize variables that are common to various stages in one place.

Use this syntax for variable templates and variable groups at the root level of a pipeline.

In this alternate syntax, the `variables` keyword takes a list of variable specifiers. The variable specifiers are `name` for a regular variable, `group` for a variable group, and `template` to include a variable template. The following example demonstrates all three.

```
variables:
# a regular variable
- name: myvariable
  value: myvalue
# a variable group
- group: myvariablegroup
# a reference to a variable template
- template: myvariabletemplate.yml
```

To learn more, see [variable reuse with templates](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/templates?view=azure-devops).

Notice that variables are also made available to scripts through environment variables. The syntax for using these environment variables depends on the scripting language.

The name is upper-cased, and the `.` is replaced with the `_`. This is automatically inserted into the process environment. Here are some examples:

*   Batch script: `%VARIABLE_NAME%`
*   PowerShell script: `$env:VARIABLE_NAME`
*   Bash script: `$VARIABLE_NAME`

Important

Predefined variables that contain file paths are translated to the appropriate styling (Windows style C:\foo\ versus Unix style /foo/) based on agent host type and shell type. If you are running bash script tasks on Windows, you should use the environment variable method for accessing these variables rather than the pipeline variable method to ensure you have the correct file path styling.

Tip

Secret variables aren't automatically exported as environment variables. To use secret variables in your scripts, explicitly map them to environment variables. For more information, see [Set secret variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/set-secret-variables?view=azure-devops).

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_2_yaml)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_2_classic)
*   [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_2_azure-devops-cli)

Don't set secret variables in your YAML file. Operating systems often log commands for the processes that they run, and you wouldn't want the log to include a secret that you passed in as an input. Use the script's environment or map the variable within the `variables` block to pass secrets to your pipeline.

Note

Azure Pipelines makes an effort to mask secrets when emitting data to pipeline logs, so you may see additional variables and data masked in output and logs that are not set as secrets.

You need to set secret variables in the pipeline settings UI for your pipeline. These variables are scoped to the pipeline where they're set. You can also set [secret variables in variable groups](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#reference-secret-variables-in-variable-groups).

To set secrets in the web interface, follow these steps:

1.   Go to the **Pipelines** page, select the appropriate pipeline, and then select **Edit**.
2.   Locate the **Variables** for this pipeline.
3.   Add or update the variable.
4.   Select the option to **Keep this value secret** to store the variable in an encrypted manner.
5.   Save the pipeline.

Secret variables are encrypted at rest with a 2048-bit RSA key. Secrets are available on the agent for tasks and scripts to use. Be careful about who has access to alter your pipeline.

Important

We make an effort to mask secrets from appearing in Azure Pipelines output, but you still need to take precautions. Never echo secrets as output. Some operating systems log command line arguments. Never pass secrets on the command line. Instead, we suggest that you map your secrets into environment variables.

We never mask substrings of secrets. If, for example, "abc123" is set as a secret, "abc" isn't masked from the logs. This is to avoid masking secrets at too granular of a level, making the logs unreadable. For this reason, secrets should not contain structured data. If, for example, "{ "foo": "bar" }" is set as a secret, "bar" isn't masked from the logs.

Unlike a normal variable, they are not automatically decrypted into environment variables for scripts. You need to explicitly map secret variables.

The following example shows how to map and use a secret variable called `mySecret` in PowerShell and Bash scripts. Two global variables are defined. `GLOBAL_MYSECRET` is assigned the value of a secret variable `mySecret`, and `GLOBAL_MY_MAPPED_ENV_VAR` is assigned the value of a non-secret variable `nonSecretVariable`. Unlike a normal pipeline variable, there's no environment variable called `MYSECRET`.

The PowerShell task runs a script to print the variables.

*   `$(mySecret)`: This is a direct reference to the secret variable and works.
*   `$env:MYSECRET`: This attempts to access the secret variable as an environment variable, which doesn't work because secret variables aren't automatically mapped to environment variables.
*   `$env:GLOBAL_MYSECRET`: This attempts to access the secret variable through a global variable, which also doesn't work because secret variables can't be mapped this way.
*   `$env:GLOBAL_MY_MAPPED_ENV_VAR`: This accesses the non-secret variable through a global variable, which works.
*   `$env:MY_MAPPED_ENV_VAR`: This accesses the secret variable through a task-specific environment variable, which is the recommended way to map secret variables to environment variables.

```
variables:
 GLOBAL_MYSECRET: $(mySecret) # this will not work because the secret variable needs to be mapped as env
 GLOBAL_MY_MAPPED_ENV_VAR: $(nonSecretVariable) # this works because it's not a secret.

steps:

- powershell: |
    Write-Host "Using an input-macro works: $(mySecret)"
    Write-Host "Using the env var directly does not work: $env:MYSECRET"
    Write-Host "Using a global secret var mapped in the pipeline does not work either: $env:GLOBAL_MYSECRET"
    Write-Host "Using a global non-secret var mapped in the pipeline works: $env:GLOBAL_MY_MAPPED_ENV_VAR" 
    Write-Host "Using the mapped env var for this task works and is recommended: $env:MY_MAPPED_ENV_VAR"
  env:
    MY_MAPPED_ENV_VAR: $(mySecret) # the recommended way to map to an env variable

- bash: |
    echo "Using an input-macro works: $(mySecret)"
    echo "Using the env var directly does not work: $MYSECRET"
    echo "Using a global secret var mapped in the pipeline does not work either: $GLOBAL_MYSECRET"
    echo "Using a global non-secret var mapped in the pipeline works: $GLOBAL_MY_MAPPED_ENV_VAR" 
    echo "Using the mapped env var for this task works and is recommended: $MY_MAPPED_ENV_VAR"
  env:
    MY_MAPPED_ENV_VAR: $(mySecret) # the recommended way to map to an env variable
```

The output from both tasks in the preceding script looks like this:

```
Using an input-macro works: ***
Using the env var directly does not work:
Using a global secret var mapped in the pipeline does not work either:
Using a global non-secret var mapped in the pipeline works: foo
Using the mapped env var for this task works and is recommended: ***
```

You can also use secret variables outside of scripts. For example, you can map secret variables to tasks by using the `variables` definition. This example shows how to use secret variables `$(vmsUser)` and `$(vmsAdminPass)` in an Azure file copy task.

```
variables:
  VMS_USER: $(vmsUser)
  VMS_PASS: $(vmsAdminPass)

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: AzureFileCopy@6
  inputs:
    SourcePath: 'my/path' # Specify the source path
    azureSubscription: 'my-subscription' # Azure subscription name
    Destination: 'AzureVMs' # Destination type
    storage: 'my-storage' # Azure storage account name
    resourceGroup: 'my-resource-group' # Resource group name
    vmsAdminUserName: $(VMS_USER) # Admin username for the VM
    vmsAdminPassword: $(VMS_PASS) # Admin password for the VM
    CleanTargetBeforeCopy: false # Do not clean the target before copying
```

This example shows how to reference a variable group in your YAML file, and also how to add variables within the YAML. The example uses two variables from the variable group: `user` and `token`. The `token` variable is secret, and is mapped to the environment variable `$env:MY_MAPPED_TOKEN` so that you can reference it in the YAML.

This YAML makes a REST call to retrieve a list of releases, and outputs the result.

```
variables: 
- group: 'my-var-group' # variable group
- name: 'devopsAccount' # new variable defined in YAML
  value: 'contoso'
- name: 'projectName' # new variable defined in YAML
  value: 'contosoads'

steps:
- task: PowerShell@2
  inputs:
    targetType: 'inline'
    script: |
        # Encode the Personal Access Token (PAT)
        # $env:USER is a normal variable in the variable group
        # $env:MY_MAPPED_TOKEN is a mapped secret variable
        $base64AuthInfo = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(("{0}:{1}" -f $env:USER,$env:MY_MAPPED_TOKEN)))

        # Get a list of releases
        $uri = "https://vsrm.dev.azure.com/$(devopsAccount)/$(projectName)/_apis/release/releases?api-version=5.1"

        # Invoke the REST call
        $result = Invoke-RestMethod -Uri $uri -Method Get -ContentType "application/json" -Headers @{Authorization=("Basic {0}" -f $base64AuthInfo)}

        # Output releases in JSON
        Write-Host $result.value
  env:
    MY_MAPPED_TOKEN: $(token) # Maps the secret variable $(token) from my-var-group
```

Important

By default, with GitHub repositories, pull request builds of forks can't access secret variables associated with your pipeline. For more information, see [Contributions from forks](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/github?view=azure-devops#contributions-from-forks).

To share variables across multiple pipelines in your project, use the web interface. Under **Library**, use [variable groups](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups?view=azure-devops).

Some tasks define output variables, which you can use in downstream steps, jobs, and stages. In YAML, you can access variables across jobs and stages by using [dependencies](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/expressions?view=azure-devops#dependencies).

When referencing matrix jobs in downstream tasks, use a different syntax. See [Set a multi-job output variable](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#set-a-multi-job-output-variable). You also need to use a different syntax for variables in deployment jobs. See [Support for output variables in deployment jobs](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/deployment-jobs?view=azure-devops#support-for-output-variables).

*   To reference a variable from a different task within the same job, use `TASK.VARIABLE`.
*   To reference a variable from a task from a different job, use `dependencies.JOB.outputs['TASK.VARIABLE']`.

Note

By default, each stage in a pipeline depends on the one just before it in the YAML file. If you need to refer to a stage that isn't immediately prior to the current one, you can override this automatic default by adding a `dependsOn` section to the stage.

Note

The following examples use standard pipeline syntax. If you're using deployment pipelines, both variable and conditional variable syntax will differ. For information about the specific syntax to use, see [Deployment jobs](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/deployment-jobs?view=azure-devops).

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_3_yaml)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_3_classic)
*   [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_3_azure-devops-cli)

For these examples, assume you have a task named `MyTask`, which sets an output variable named `MyVar`. Learn more about the syntax in [Expressions - Dependencies](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/expressions?view=azure-devops#dependencies).

```
steps:
- task: MyTask@1  # this step generates the output variable
  name: ProduceVar  # because we're going to depend on it, we need to name the step
- script: echo $(ProduceVar.MyVar) # this step uses the output variable
```

```
jobs:
- job: A
  steps:
  # assume that MyTask generates an output variable called "MyVar"
  # (you would learn that from the task's documentation)
  - task: MyTask@1
    name: ProduceVar  # because we're going to depend on it, we need to name the step
- job: B
  dependsOn: A
  variables:
    # map the output variable from A into this job
    varFromA: $[ dependencies.A.outputs['ProduceVar.MyVar'] ]
  steps:
  - script: echo $(varFromA) # this step uses the mapped-in variable
```

To use the output from a different stage, use the format `stageDependencies.STAGE.JOB.outputs['TASK.VARIABLE']` to reference variables. At the stage level, but not the job level, you can use these variables in conditions.

Output variables are only available in the next downstream stage. If multiple stages consume the same output variable, use the `dependsOn` condition.

```
stages:
- stage: One
  jobs:
  - job: A
    steps:
    - task: MyTask@1  # this step generates the output variable
      name: ProduceVar  # because we're going to depend on it, we need to name the step

- stage: Two
  dependsOn:
  - One
  jobs:
  - job: B
    variables:
      # map the output variable from A into this job
      varFromA: $[ stageDependencies.One.A.outputs['ProduceVar.MyVar'] ]
    steps:
    - script: echo $(varFromA) # this step uses the mapped-in variable

- stage: Three
  dependsOn:
  - One
  - Two
  jobs:
  - job: C
    variables:
      # map the output variable from A into this job
      varFromA: $[ stageDependencies.One.A.outputs['ProduceVar.MyVar'] ]
    steps:
    - script: echo $(varFromA) # this step uses the mapped-in variable
```

You can also pass variables between stages by using a file input. To do so, you need to define variables in the second stage at the job level, and then pass the variables as `env:` inputs.

```
## script-a.sh
echo "##vso[task.setvariable variable=sauce;isOutput=true]crushed tomatoes"
```

```
## script-b.sh
echo 'Hello file version'
echo $skipMe
echo $StageSauce
```

```
## azure-pipelines.yml
stages:

- stage: one
  jobs:
  - job: A
    steps:
    - task: Bash@3
      inputs:
          filePath: 'script-a.sh'
      name: setvar
    - bash: |
       echo "##vso[task.setvariable variable=skipsubsequent;isOutput=true]true"
      name: skipstep

- stage: two
  jobs:
  - job: B
    variables:
      - name: StageSauce
        value: $[ stageDependencies.one.A.outputs['setvar.sauce'] ]
      - name: skipMe
        value: $[ stageDependencies.one.A.outputs['skipstep.skipsubsequent'] ]
    steps:
    - task: Bash@3
      inputs:
        filePath: 'script-b.sh'
      name: fileversion
      env:
        StageSauce: $(StageSauce) # predefined in variables section
        skipMe: $(skipMe) # predefined in variables section
    - task: Bash@3
      inputs:
        targetType: 'inline'
        script: |
          echo 'Hello inline version'
          echo $(skipMe) 
          echo $(StageSauce)
```

The output from stages in the preceding pipeline looks like this:

```
Hello inline version
true
crushed tomatoes
```

List all variables in your pipeline by using the [az pipelines variable list](https://learn.microsoft.com/en-us/cli/azure/pipelines/variable#az-pipelines-variable-list) command. To get started, see [Get started with Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/cli/?view=azure-devops).

```
az pipelines variable list [--org]
                           [--pipeline-id]
                           [--pipeline-name]
                           [--project]
```

*   **org**: Azure DevOps organization URL. Configure the default organization by using `az devops configure -d organization=ORG_URL`. Required if not configured as default or picked up by using `git config`. Example: `--org https://dev.azure.com/MyOrganizationName/`.
*   **pipeline-id**: Required if **pipeline-name** isn't supplied. ID of the pipeline.
*   **pipeline-name**: Required if **pipeline-id** isn't supplied, but ignored if **pipeline-id** is supplied. Name of the pipeline.
*   **project**: Name or ID of the project. Configure the default project by using `az devops configure -d project=NAME_OR_ID`. Required if not configured as default or picked up by using `git config`.

The following command lists all of the variables in the pipeline with ID **12** and shows the result in table format.

```
az pipelines variable list --pipeline-id 12 --output table

Name           Allow Override    Is Secret    Value
-------------  ----------------  -----------  ------------
MyVariable     False             False        platform
NextVariable   False             True         platform
Configuration  False             False        config.debug
```

Scripts can define variables that later steps in the pipeline consume. All variables set by this method are treated as strings. To set a variable from a script, use a command syntax and print to stdout.

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_4_yaml)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_4_classic)
*   [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_4_azure-devops-cli)

To set a variable from a script, use the `task.setvariable`[logging command](https://learn.microsoft.com/en-us/azure/devops/pipelines/scripts/logging-commands?view=azure-devops). This command updates the environment variables for subsequent jobs. Subsequent jobs can access the new variable by using [macro syntax](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#understand-variable-syntax) and in tasks as environment variables.

When you set `issecret` to true, the value of the variable is saved as secret and masked from the log. For more information about secret variables, see [logging commands](https://learn.microsoft.com/en-us/azure/devops/pipelines/scripts/logging-commands?view=azure-devops).

```
steps:
# Create a variable
- bash: |
    echo "##vso[task.setvariable variable=sauce]crushed tomatoes" # remember to use double quotes

# Use the variable
# "$(sauce)" is replaced by the contents of the `sauce` variable by Azure Pipelines
# before handing the body of the script to the shell.
- bash: |
    echo my pipeline variable is $(sauce)
```

Subsequent steps also have the pipeline variable added to their environment. You can't use the variable in the step that it's defined.

```
steps:
# Create a variable
# Note that this does not update the environment of the current script.
- bash: |
    echo "##vso[task.setvariable variable=sauce]crushed tomatoes"

# An environment variable called `SAUCE` has been added to all downstream steps
- bash: |
    echo "my environment variable is $SAUCE"
- pwsh: |
    Write-Host "my environment variable is $env:SAUCE"
```

The output from the preceding pipeline.

```
my environment variable is crushed tomatoes
my environment variable is crushed tomatoes
```

If you want to make a variable available to future jobs, you must mark it as an output variable by using `isOutput=true`. Then you can map it into future jobs by using the `$[]` syntax and including the step name that set the variable. Multi-job output variables only work for jobs in the same stage.

To pass variables to jobs in different stages, use the [stage dependencies](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/expressions?view=azure-devops#dependencies) syntax.

Note

By default, each stage in a pipeline depends on the one just before it in the YAML file. Therefore, each stage can use output variables from the prior stage. To access further stages, you will need to alter the dependency graph, for instance, if stage 3 requires a variable from stage 1, you will need to declare an explicit dependency on stage 1.

When you create a multi-job output variable, you should assign the expression to a variable. In this YAML, `$[ dependencies.A.outputs['setvarStep.myOutputVar'] ]` is assigned to the variable `$(myVarFromJobA)`.

```
jobs:
# Set an output variable from job A
- job: A
  pool:
    vmImage: 'windows-latest'
  steps:
  - powershell: echo "##vso[task.setvariable variable=myOutputVar;isOutput=true]this is the value"
    name: setvarStep
  - script: echo $(setvarStep.myOutputVar)
    name: echovar

# Map the variable into job B
- job: B
  dependsOn: A
  pool:
    vmImage: 'ubuntu-latest'
  variables:
    myVarFromJobA: $[ dependencies.A.outputs['setvarStep.myOutputVar'] ]  # map in the variable
                                                                          # remember, expressions require single quotes
  steps:
  - script: echo $(myVarFromJobA)
    name: echovar
```

The output from the preceding pipeline.

```
this is the value
this is the value
```

If you're setting a variable from one stage to another, use `stageDependencies`.

```
stages:
- stage: A
  jobs:
  - job: A1
    steps:
     - bash: echo "##vso[task.setvariable variable=myStageOutputVar;isOutput=true]this is a stage output var"
       name: printvar

- stage: B
  dependsOn: A
  variables:
    myVarfromStageA: $[ stageDependencies.A.A1.outputs['printvar.myStageOutputVar'] ]
  jobs:
  - job: B1
    steps:
    - script: echo $(myVarfromStageA)
```

If you're setting a variable from a [matrix](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/phases?view=azure-devops&tab=yaml#multi-job-configuration) or [slice](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/phases?view=azure-devops&tab=yaml#slicing), then to reference the variable when you access it from a downstream job, you must include:

*   The name of the job.
*   The step.

```
jobs:

# Set an output variable from a job with a matrix
- job: A
  pool:
    vmImage: 'ubuntu-latest'
  strategy:
    maxParallel: 2
    matrix:
      debugJob:
        configuration: debug
        platform: x64
      releaseJob:
        configuration: release
        platform: x64
  steps:
  - bash: echo "##vso[task.setvariable variable=myOutputVar;isOutput=true]this is the $(configuration) value"
    name: setvarStep
  - bash: echo $(setvarStep.myOutputVar)
    name: echovar

# Map the variable from the debug job
- job: B
  dependsOn: A
  pool:
    vmImage: 'ubuntu-latest'
  variables:
    myVarFromJobADebug: $[ dependencies.A.outputs['debugJob.setvarStep.myOutputVar'] ]
  steps:
  - script: echo $(myVarFromJobADebug)
    name: echovar
```

```
jobs:

# Set an output variable from a job with slicing
- job: A
  pool:
    vmImage: 'ubuntu-latest'
    parallel: 2 # Two slices
  steps:
  - bash: echo "##vso[task.setvariable variable=myOutputVar;isOutput=true]this is the slice $(system.jobPositionInPhase) value"
    name: setvarStep
  - script: echo $(setvarStep.myOutputVar)
    name: echovar

# Map the variable from the job for the first slice
- job: B
  dependsOn: A
  pool:
    vmImage: 'ubuntu-latest'
  variables:
    myVarFromJobsA1: $[ dependencies.A.outputs['job1.setvarStep.myOutputVar'] ]
  steps:
  - script: "echo $(myVarFromJobsA1)"
    name: echovar
```

Be sure to prefix the job name to the output variables of a [deployment](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/deployment-jobs?view=azure-devops) job. In this case, the job name is `A`:

```
jobs:

# Set an output variable from a deployment
- deployment: A
  pool:
    vmImage: 'ubuntu-latest'
  environment: staging
  strategy:
    runOnce:
      deploy:
        steps:
        - bash: echo "##vso[task.setvariable variable=myOutputVar;isOutput=true]this is the deployment variable value"
          name: setvarStep
        - bash: echo $(setvarStep.myOutputVar)
          name: echovar

# Map the variable from the job for the first slice
- job: B
  dependsOn: A
  pool:
    vmImage: 'ubuntu-latest'
  variables:
    myVarFromDeploymentJob: $[ dependencies.A.outputs['A.setvarStep.myOutputVar'] ]
  steps:
  - bash: "echo $(myVarFromDeploymentJob)"
    name: echovar
```

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_5_yaml)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_5_classic)
*   [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_5_azure-devops-cli)

You can set a variable by using an expression. You already encountered one case of this approach when you set a variable to the output of another variable from a previous job.

```
- job: B
  dependsOn: A
  variables:
    myVarFromJobsA1: $[ dependencies.A.outputs['job1.setvarStep.myOutputVar'] ] # remember to use single quotes
```

You can use any of the supported expressions for setting a variable. Here's an example of setting a variable to act as a counter that starts at 100, gets incremented by 1 for every run, and gets reset to 100 every day.

```
jobs:
- job:
  variables:
    a: $[counter(format('{0:yyyyMMdd}', pipeline.startTime), 100)]
  steps:
  - bash: echo $(a)
```

For more information about counters, dependencies, and other expressions, see [expressions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/expressions?view=azure-devops).

You can define `settableVariables` within a step or specify that no variables can be set.

In this example, the script can't set a variable.

```
steps:
- script: echo This is a step
  target:
    settableVariables: none
```

In the following example, the script can set the variable `sauce` but can't set the variable `secretSauce`. You see a warning on the pipeline run page.

![Image 1: Warning that you can't set secretSauce.](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/media/set-vars-warning.png?view=azure-devops)

```
steps:
  - bash: |
      echo "##vso[task.setvariable variable=Sauce;]crushed tomatoes"
      echo "##vso[task.setvariable variable=secretSauce;]crushed tomatoes with garlic"
    target:
     settableVariables:
      - sauce
    name: SetVars
  - bash: 
      echo "Sauce is $(sauce)"
      echo "secretSauce is $(secretSauce)"
    name: OutputVars
```

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_6_yaml)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_6_classic)
*   [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_6_azure-devops-cli)

If a variable appears in the `variables` block of a YAML file, its value is fixed and users can't override it at queue time. Define your variables in a YAML file, but there are times when this approach doesn't make sense. For example, you might want to define a secret variable and not expose it in your YAML. Or, you might need to manually set a variable value during the pipeline run.

You have two options for defining queue-time values. You can define a variable in the UI and select the option to **Let users override this value when running this pipeline** or you can use [runtime parameters](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/runtime-parameters?view=azure-devops) instead. If your variable isn't a secret, the best practice is to use [runtime parameters](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/runtime-parameters?view=azure-devops).

To set a variable at queue time, add a new variable within your pipeline and select the override option. Only users with the _Edit queue build configuration_ permission can change a variable's value.

![Image 2: Set a variable at queue time.](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/media/set-queue-time-variable.png?view=azure-devops)

To allow a variable to be set at queue time, make sure the variable doesn't also appear in the `variables` block of a pipeline or job. If you define a variable in both the variables block of a YAML and in the UI, the value in the YAML has priority.

For added security, use a predefined set of values for settable at queue time variables and safe types such as booleans and integers. For strings, use a predefined set of values.

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_7_yaml)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_7_classic)
*   [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops#tabpanel_7_azure-devops-cli)

When you set a variable with the same name in multiple scopes, the following precedence applies (highest precedence first):

1.   Job level variable set in the YAML file
2.   Stage level variable set in the YAML file
3.   Pipeline level variable set in the YAML file
4.   Variable set at queue time
5.   Pipeline variable set in Pipeline settings UI

In the following example, the same variable `a` is set at the pipeline level and job level in the YAML file. It's also set in a variable group `G`, and as a variable in the Pipeline settings UI.

```
variables:
  a: 'pipeline yaml'

stages:
- stage: one
  displayName: one
  variables:
  - name: a
    value: 'stage yaml'

  jobs:
  - job: A
    variables:
    - name: a
      value: 'job yaml'
    steps:
    - bash: echo $(a)        # This will be 'job yaml'
```

When you set a variable with the same name in the same scope, the last set value takes precedence.

```
stages:
- stage: one
  displayName: Stage One
  variables: 
    - name: a
      value: alpha
    - name: a
      value: beta
  jobs: 
  - job: I
    displayName: Job I
    variables:
      - name: b
        value: uno
      - name: b
        value: dos
    steps: 
    - script: echo $(a) #outputs beta
    - script: echo $(b) #outputs dos
```

Note

When you set a variable in the YAML file, don't define it in the web editor as settable at queue time. You can't currently change variables that are set in the YAML file at queue time. If you need a variable to be settable at queue time, don't set it in the YAML file.

Variables are expanded once when the run starts, and again at the beginning of each step. For example:

```
jobs:
- job: A
  variables:
    a: 10
  steps:
  - bash: |
      echo $(a)            # This will be 10
      echo '##vso[task.setvariable variable=a]20'
      echo $(a)            # This will also be 10, since the expansion of $(a) happens before the step
  - bash: echo $(a)        # This will be 20, since the variables are expanded just before the step
```

There are two steps in the preceding example. The expansion of `$(a)` happens once at the beginning of the job, and once at the beginning of each of the two steps.

Because variables are expanded at the beginning of a job, you can't use them in a strategy. In the following example, you can't use the variable `a` to expand the job matrix, because the variable is only available at the beginning of each expanded job.

```
jobs:
- job: A
  variables:
    a: 10
  strategy:
    matrix:
      x:
        some_variable: $(a)    # This does not work
```

If the variable `a` is an output variable from a previous job, then you can use it in a future job.

```
- job: A
  steps:
  - powershell: echo "##vso[task.setvariable variable=a;isOutput=true]10"
    name: a_step

# Map the variable into job B
- job: B
  dependsOn: A
  variables:
    some_variable: $[ dependencies.A.outputs['a_step.a'] ]
```

On the agent, variables referenced using `$( )` syntax are recursively expanded. For example:

```
variables:
  myInner: someValue
  myOuter: $(myInner)

steps:
- script: echo $(myOuter)  # prints "someValue"
  displayName: Variable is $(myOuter)  # display name is "Variable is someValue"
```

*   [Set variables in scripts](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/set-variables-scripts?view=azure-devops)
*   [Use predefined variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops)
*   [Expressions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/expressions?view=azure-devops)
*   [Variable group](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups?view=azure-devops)
