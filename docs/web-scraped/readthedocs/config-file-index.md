# Source: https://docs.readthedocs.com/platform/latest/config-file/index.html

# Configuration file overview[](#configuration-file-overview "Link to this heading")

As part of the initial set up of a Read the Docs project, you need to create a **configuration file** called [`.readthedocs.yaml`]. The configuration file tells Read the Docs what specific settings to use for your project.

This tutorial covers:

-   [Where to put your configuration file](#where-to-put-your-configuration-file)

-   [Getting started with a template](#getting-started-with-a-template)

-   [Editing the template](#editing-the-template)

-   [Next steps](#next-steps)

## [Where to put your configuration file](#id3)[](#where-to-put-your-configuration-file "Link to this heading")

The [`.readthedocs.yaml`] file should be placed in the top-most directory of your project's repository. When you have changed the configuration file, you need to commit and push the changes to your Git repository. Read the Docs will then automatically find and use the configuration to build your project.

Note

The Read the Docs configuration file is a [YAML](https://yaml.org/) file. YAML is a human-friendly data serialization language for all programming languages. To learn more about the structure of these files, see the [YAML language overview](https://yaml.org/spec/1.2.2/#chapter-1-introduction-to-yaml).