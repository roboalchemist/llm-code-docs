# Source: https://docs.debricked.com/product/vulnerability-management/reachability-analysis/set-up-reachability-analysis.md

# Set up Reachability Analysis for Java

To enable Reachability Analysis for Java, you need to generate a call graph. This can be done using the [OpenText Core SCA CLI](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli) `callgraph` command, which can be added to your integration, so that it is generated appropriately before making a OpenText Core SCA scan. To find out more about the command and the various available flags, run:

```
debricked callgraph -h
```

Reachability Analysis is supported for all Java projects using Maven. To produce a callgraph, OpenText Core SCA requires the compiled code for your project and access to the libraries it uses. By default, the command will attempt to do all the preparation work for the command to be successful. The success of the preparation depends on the specific project structure and configurations. In the event of failure, it is possible to configure the command not to run the preparation steps using the `--no-build` flag, and instead set it up separately before running the command.

### Set up call graph generation in your pipeline

When successful, the `callgraph` command will generate a debricked-call-graph file that is automatically picked up when running the `debricked scan` command and sent to OpenText Core SCA, together with the dependency files, for analysis. For many projects, it will be possible to run the default configuration of the `callgraph` command, doing the preparation steps as part of the command. In this case, all that is needed is to add running `debricked callgraph` in your configuration, before running the scan, ensuring that the scan has access to the generated call graph file. For GitHub Action integrations, there is also Actions setup that can be found in the [GitHub Actions repository](https://github.com/debricked/actions/tree/master).

If the build step of the `callgraph` command fails, or if you are already building the project in a previous stage of the pipeline, it’s highly recommended to build the project separately before running the `callgraph` command with the `—no-build` flag. Just make sure that the files resulting from the build are included in the stage where call graph generation is run.

The examples below use a OpenText Core SCA CLI docker image to ensure that there is a compatible maven version included for the commands to succeed. OpenText Core SCA recommendation is that you incorporate the `scan` and `callgraph` commands in your build image/steps whenever possible, to ensure that versions of the underlying tools correlate with your environment.

#### Example: Building the project during the callgraph command

In this example, the `callgraph` command is run with its default configuration, which builds the project and prepares the necessary files automatically before generating the call graph.

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

#### Example: Using a separate build step

The example below is using maven to build the project and generate the files needed for call graph generation. The generated files must be reachable in the stage where the `callgraph` command is run, so that it has all pre-requisites to be run successfully.

```bash
# GitLab CI/CD template

image: debricked/cli:2-resolution-debian

stages:
    - build_project
    - scan

scan_preparation:
  stage: build_project

  script:
    # Build project based on the root pom.xml. If no root pom.xml is found, all pom.xml files will be built individually.
    - mvn package -q -DskipTests -e

  # Save class files from the target/ folder for use in the next stage.
  artifacts:
    expire_in: 1 day
    paths:
      - target/

debricked-scan:
  stage: scan

  script:
    - debricked callgraph --no-build
    - debricked scan
```

### Common issues

Multiple issues can occur when trying to generate the callgraph which prohibits success. Some common issues are:

* Unsupported Java version. If your project requires a Java version older than 11, Debricked may not be able to produce a callgraph. Debricked may also not be able to generate a callgraph if your project uses new lanugage features from a version above 21.
* Unsupported language features. Some advanced language features can make callgraph generation impossible for the tool that is used to generate the callgraphs.
