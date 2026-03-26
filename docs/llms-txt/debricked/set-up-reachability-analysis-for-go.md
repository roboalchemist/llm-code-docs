# Source: https://docs.debricked.com/product/vulnerability-management/reachability-analysis/set-up-reachability-analysis-for-go.md

# Set up Reachability Analysis for Go

Reachability Analysis is supported for all Go projects. You need the compiled code and the libraries used by your Go project to enable Reachability Analysis.

You need to generate a call graph to enable Reachability Analysis for Go. To generate a call graph, add the [OpenText Core SCA CLI](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli) `callgraph` command to your integration before running a OpenText Core SCA scan. To find out more about the command and the various available flags, run:

```
debricked callgraph -h
```

{% hint style="info" %}
*The success of CLI call graph generation depends on the complexity of the application being analyzed. If an application contains a language feature that is not supported by the algorithm, the* `callgraph` *command fails and you cannot set up Reachability Analysis for that application.*&#x20;
{% endhint %}

When successful, the `callgraph` command generates a `debricked-call-graph` file. This file is automatically sent to OpenText Core SCA with the dependency files for analysis, when running the debricked scan command.

### Set up call graph generation in your pipeline

For many projects, running the `callgraph` command with the default configuration might be enough to run the preparation steps. In this case, before running the `debricked scan`, to add the command to run `debricked callgraph` in your configuration to ensure that the scan has access to the generated call graph file.

For GitHub Action integrations, OpenText Core SCA must also add Actions setup that can be found in the [GitHub Actions repository](https://github.com/debricked/actions/tree/master).

#### Example: Building the project during the callgraph command

In this example, the `callgraph` command is run with default configuration to build the project and prepare the necessary files automatically before generating the call graph.

```bash
# GitLab CI/CD template

image: debricked/cli:2-resolution-debian

stages:
  - scan
debricked:
  stage: scan
  script:
    - debricked callgraph
    - debricked scan
```
