# Source: https://docs.kedro.org/en/stable/create/customise_project/index.md

# Customise a new project

As you saw from the [First steps](https://docs.kedro.org/en/stable/create/new_project/index.md) section, after you have [set up Kedro](https://docs.kedro.org/en/stable/getting-started/install/index.md), you can create a new project with `kedro new`. You can then customise the code added to that project for its tooling and example code requirements.

The pages in this section describe in detail the various options available.

## Tools to customise a new Kedro project

- [Tools and example code options](https://docs.kedro.org/en/stable/create/new_project_tools/index.md)

## Kedro starters

- [Starters](https://docs.kedro.org/en/stable/create/starters/index.md)

**Use `kedro new` to create a basic project**\
Run `kedro new` to create a project and choose from [tools and example code options](https://docs.kedro.org/en/stable/create/new_project_tools/index.md) to extend the basic project.

**Use `kedro new` with `--config`**\
Similarly, you can use `kedro new` and also pass in a configuration file, for example:

```
kedro new --config=config.yml
```

The file enables you to customise details such as the project folder name and package name.

The configuration file must contain:

- `output_dir`: The path in which to create the project directory, which can be set to `~` for the home directory or `.` for the current working directory.
- `project_name`
- `repo_name`
- `python_package`

The configuration file may also contain:

- `tools`: The tools to customise your project setup with. Select from comma-separated values `lint, test, log, docs, data, pyspark, viz` or `all/none`. Omitting this from your configuration file will result in the default selection of `none`.
- `example_pipeline`: Set to `yes` or `no` to choose whether you would like your project to be populated with example code. Omitting this from your configuration file will result in the default selection of `no`.

The `output_dir` can be specified as `~` for the home directory or `.` for the current working directory. Here is an example `config.yml`, which assumes that a directory named `~/code` already exists:

```
output_dir: ~/code
project_name: My First Kedro Project
repo_name: testing-kedro
python_package: test_kedro
```

Note

When the `--config` flag is used together with `--name`, `--tools`, or `--example`, the values provided directly on the CLI will overwrite those specified in the configuration file.

**Use `kedro new` with a `--starter`**\
You can create a new Kedro project with a [starter](https://docs.kedro.org/en/stable/create/starters/index.md) that adds code for a common project use case.

Warning

You cannot combine the use of a Kedro starter with the tools and example code options listed above.
