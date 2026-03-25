# Source: https://docs.knock.app/cli/overview/configuring-your-project.md

# Configuring your project

You can configure your Knock project by creating a `knock.json` file or by using the `knock init` command to generate one for you. This
    file is a project-level configuration file that tells the Knock CLI where to
    find your Knock resources.

    For example, if you want to store your Knock resources in the `.knock/` directory, you can create a `knock.json` file with the following content:

```json title="Example knock.json file"
{
  "knockDir": ".knock/"
}
```

    Once you have created the `knock.json` file, all subsequent `knock pull` and `knock push` commands will use the `.knock/` directory as the default target directory relative to the location of the `knock.json` file, regardless of the directory you are currently in.

    If you need to specify a different target directory for a single command, you can use the `--knock-dir` flag, or the `--{resource-type}-dir` flag for specific resource types.
