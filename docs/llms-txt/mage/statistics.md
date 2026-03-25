# Source: https://docs.mage.ai/about/statistics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Help improve the tool

> Please contribute usage statistics to help improve the developer experience for you and everyone in the community 🤝.

<Check>
  All usage statistics are completely <b>anonymous</b>.

  It’s <b>impossible</b> for Mage to know which statistics belongs to whom.
</Check>

<Frame>
  <img alt="Combine our powers" src="https://media2.giphy.com/media/0Av9l0VIc01y1isrDw/giphy.gif" />
</Frame>

## 🙏 Why is this important?

By opting into sending usage statistics to [Mage](https://www.mage.ai/),
it’ll help the team and community of contributors (Magers) learn what’s going wrong with the tool
and what improvements can be made.

In addition to helping reduce potential errors,
you’ll help inform which features are useful and which need work.

## 🤔 What usage statistics am I sending?

### Project UUID

Each project will have a universally unique identifier.
This will help Mage count how many projects have been created.

<Note>
  It’s <b>impossible</b> to associate a UUID with a project without knowing the pair together.
</Note>

Your project UUID is stored in the project’s `metadata.yaml` file,
located at the root of your project: `[project_name]/metadata.yaml`.

Here is an example of what it could look like:

```yaml  theme={"system"}
variables_dir: ~/.mage_data

# ...

project_uuid: 4279d28ab1f64644b1f2f4f779be7b7e
```

### Number of pipelines

Sending usage statistics will include the number of pipelines in a single project.
This will help improve the coding experience when building pipelines.

### Number of pipeline runs

Sending usage statistics will include the number of times any pipeline has ran in a single project.
This will help add better pipeline management features.

### Number of users

Sending usage statistics will include the number of users in a single project.
This will help improve the collaboration capabilities of the tool.

<Note>
  This usage statistic is only included if
  [user authentication](/production/authentication/overview) is enabled.
</Note>

### Errors

When an application error occurs in Mage, the error type, error message, and offending line of code
will be included in the usage statistics.
This will help fix bugs and improve the developer experience.

### Platform

The operating system, release, version, etc of the machine that Mage is running on.
This information will help reproduce errors.

## 🤷‍♀️ How does this work?

Usage statistics are anonymously sent to Mage’s online server.

Here’s a sample of the JSON payload containing usage statistics that could be sent:

```json  theme={"system"}
{
  "usage_statistic": {
    "project_uuid": "4279d28ab1f64644b1f2f4f779be7b7e",
    "pipelines": 40,
    "pipeline_runs": 357,
    "users": 13,
    "platform": "Linux-5.15.49-linuxkit-aarch64-with-glibc2.31",
    "version": "0.8.70",
    "error": {
      "message": "...",
      "traceback": "..."
    }
  }
}
```

### Enable

To enable sending usage statistics, add a key in the project’s `metadata.yaml` file called
`help_improve_mage` with the value `true`.

Here is an example:

```yaml  theme={"system"}
project_uuid: 4279d28ab1f64644b1f2f4f779be7b7e
help_improve_mage: true
```

### Disable

To disable, change the value of `help_improve_mage` to `false`.

Here is an example:

```yaml  theme={"system"}
project_uuid: 4279d28ab1f64644b1f2f4f779be7b7e
help_improve_mage: false
```


Built with [Mintlify](https://mintlify.com).