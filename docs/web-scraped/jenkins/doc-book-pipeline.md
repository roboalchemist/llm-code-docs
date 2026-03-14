# Source: https://www.jenkins.io/doc/book/pipeline/

Title: Pipeline

URL Source: https://www.jenkins.io/doc/book/pipeline/

Published Time: Sat, 14 Mar 2026 05:15:54 GMT

Markdown Content:
Pipeline
===============

[> User Documentation Home](https://www.jenkins.io/doc/)

##### User Handbook

*   [User Handbook Overview](https://www.jenkins.io/doc/book/getting-started/)
*   [Installing Jenkins](https://www.jenkins.io/doc/book/installing/)
*   [Platform Information](https://www.jenkins.io/doc/book/platform-information/)
*   [Using Jenkins](https://www.jenkins.io/doc/book/using/)
*   [Pipeline](https://www.jenkins.io/doc/book/pipeline/)
    *   [Getting started with Pipeline](https://www.jenkins.io/doc/book/pipeline/getting-started/)
    *   [Using a Jenkinsfile](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/)
    *   [Running Pipelines](https://www.jenkins.io/doc/book/pipeline/running-pipelines/)
    *   [Branches and Pull Requests](https://www.jenkins.io/doc/book/pipeline/multibranch/)
    *   [Using Docker with Pipeline](https://www.jenkins.io/doc/book/pipeline/docker/)
    *   [Extending with Shared Libraries](https://www.jenkins.io/doc/book/pipeline/shared-libraries/)
    *   [Pipeline Development Tools](https://www.jenkins.io/doc/book/pipeline/development/)
    *   [Pipeline Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/)
    *   [Pipeline as Code](https://www.jenkins.io/doc/book/pipeline/pipeline-as-code/)
    *   [Pipeline Best Practices](https://www.jenkins.io/doc/book/pipeline/pipeline-best-practices/)
    *   [Scaling Pipelines](https://www.jenkins.io/doc/book/pipeline/scaling-pipeline/)
    *   [Pipeline CPS Method Mismatches](https://www.jenkins.io/doc/book/pipeline/cps-method-mismatches/)

*   [Blue Ocean](https://www.jenkins.io/doc/book/blueocean/)
*   [Managing Jenkins](https://www.jenkins.io/doc/book/managing/)
*   [Securing Jenkins](https://www.jenkins.io/doc/book/security/)
*   [System Administration](https://www.jenkins.io/doc/book/system-administration/)
*   [Scaling Jenkins](https://www.jenkins.io/doc/book/scaling/)
*   [Troubleshooting Jenkins](https://www.jenkins.io/doc/book/troubleshooting/)
*   [Glossary](https://www.jenkins.io/doc/book/glossary/)

##### Tutorials

*   [Guided Tour](https://www.jenkins.io/doc/pipeline/tour/getting-started/)
*   [Jenkins Pipeline](https://www.jenkins.io/doc/tutorials#pipeline)
*   [Using Build Tools](https://www.jenkins.io/doc/tutorials#tools)

##### Resources

*   [Pipeline Syntax reference](https://www.jenkins.io/doc/book/pipeline/syntax/)
*   [Pipeline Steps reference](https://www.jenkins.io/doc/pipeline/steps/)
*   [LTS Upgrade guides](https://www.jenkins.io/doc/upgrade-guide/)

[⇐ Using Jenkins](https://www.jenkins.io/doc/book/using)

[Index](https://www.jenkins.io/doc/book/)

[Getting started with Pipeline ⇒](https://www.jenkins.io/doc/book/pipeline/getting-started)

Pipeline
========

 Chapter Sub-Sections 

*   [Getting started with Pipeline](https://www.jenkins.io/doc/book/pipeline/getting-started)
*   [Using a Jenkinsfile](https://www.jenkins.io/doc/book/pipeline/jenkinsfile)
*   [Running Pipelines](https://www.jenkins.io/doc/book/pipeline/running-pipelines)
*   [Branches and Pull Requests](https://www.jenkins.io/doc/book/pipeline/multibranch)
*   [Using Docker with Pipeline](https://www.jenkins.io/doc/book/pipeline/docker)
*   [Extending with Shared Libraries](https://www.jenkins.io/doc/book/pipeline/shared-libraries)
*   [Pipeline Development Tools](https://www.jenkins.io/doc/book/pipeline/development)
*   [Pipeline Syntax](https://www.jenkins.io/doc/book/pipeline/syntax)
*   [Pipeline as Code](https://www.jenkins.io/doc/book/pipeline/pipeline-as-code)
*   [Pipeline Best Practices](https://www.jenkins.io/doc/book/pipeline/pipeline-best-practices)
*   [Scaling Pipelines](https://www.jenkins.io/doc/book/pipeline/scaling-pipeline)
*   [Pipeline CPS Method Mismatches](https://www.jenkins.io/doc/book/pipeline/cps-method-mismatches)

Table of Contents

*   [What is Jenkins Pipeline?](https://www.jenkins.io/doc/book/pipeline/#overview)
    *   [Declarative versus Scripted Pipeline syntax](https://www.jenkins.io/doc/book/pipeline/#declarative-versus-scripted-pipeline-syntax)

*   [Why Pipeline?](https://www.jenkins.io/doc/book/pipeline/#why)
*   [Pipeline concepts](https://www.jenkins.io/doc/book/pipeline/#pipeline-concepts)
    *   [Pipeline](https://www.jenkins.io/doc/book/pipeline/#pipeline)
    *   [Node](https://www.jenkins.io/doc/book/pipeline/#node)
    *   [Stage](https://www.jenkins.io/doc/book/pipeline/#stage)
    *   [Step](https://www.jenkins.io/doc/book/pipeline/#step)

*   [Pipeline syntax overview](https://www.jenkins.io/doc/book/pipeline/#pipeline-syntax-overview)
    *   [Declarative Pipeline fundamentals](https://www.jenkins.io/doc/book/pipeline/#declarative-pipeline-fundamentals)
    *   [Scripted Pipeline fundamentals](https://www.jenkins.io/doc/book/pipeline/#scripted-pipeline-fundamentals)

*   [Pipeline example](https://www.jenkins.io/doc/book/pipeline/#pipeline-example)

This chapter covers all recommended aspects of Jenkins Pipeline functionality, including how to:

*   [Get started with Pipeline](https://www.jenkins.io/doc/book/pipeline/getting-started), which covers how to [define a Jenkins Pipeline](https://www.jenkins.io/doc/book/pipeline/getting-started#defining-a-pipeline) (your `Pipeline`) through [Blue Ocean](https://www.jenkins.io/doc/book/pipeline/getting-started#through-blue-ocean), through the [classic UI](https://www.jenkins.io/doc/book/pipeline/getting-started#through-the-classic-ui) or in [SCM](https://www.jenkins.io/doc/book/pipeline/getting-started#defining-a-pipeline-in-scm).

*   [Create and use a `Jenkinsfile`](https://www.jenkins.io/doc/book/pipeline/jenkinsfile), which covers use-case scenarios on how to craft and construct your `Jenkinsfile`.

*   Work with [branches and pull requests](https://www.jenkins.io/doc/book/pipeline/multibranch).

*   [Use Docker with Pipeline](https://www.jenkins.io/doc/book/pipeline/docker), covering how Jenkins can invoke Docker containers on agents/nodes (from a `Jenkinsfile`) to build your Pipeline projects.

*   [Extend Pipeline with shared libraries](https://www.jenkins.io/doc/book/pipeline/shared-libraries).

*   Use different [development tools](https://www.jenkins.io/doc/book/pipeline/development) to facilitate the creation of your Pipeline.

*   Work with [Pipeline syntax](https://www.jenkins.io/doc/book/pipeline/syntax), which provides a comprehensive reference of all Declarative Pipeline syntax.

For an overview of content in the Jenkins User Handbook, refer to the [User Handbook Overview](https://www.jenkins.io/doc/book/pipeline/getting-started).

[](https://www.jenkins.io/doc/book/pipeline/#overview)What is Jenkins Pipeline?
-------------------------------------------------------------------------------

Jenkins Pipeline (or simply "Pipeline" with a capital "P") is a suite of plugins which supports implementing and integrating _continuous delivery pipelines_ into Jenkins.

A _continuous delivery (CD) pipeline_ is an automated expression of your process for getting software from version control right through to your users and customers. Every change to your software (committed in source control) goes through a complex process on its way to being released. This process involves building the software in a reliable and repeatable manner, as well as progressing the built software (called a "build") through multiple stages of testing and deployment.

Pipeline provides an extensible set of tools for modeling simple-to-complex delivery pipelines "as code" via the [Pipeline domain-specific language (DSL) syntax](https://www.jenkins.io/doc/book/pipeline/syntax). [[1](https://www.jenkins.io/doc/book/pipeline/#_footnotedef_1 "View footnote.")]

The definition of a Jenkins Pipeline is written into a text file (called a [`Jenkinsfile`](https://www.jenkins.io/doc/book/pipeline/jenkinsfile)) which in turn can be committed to a project’s source control repository. [[2](https://www.jenkins.io/doc/book/pipeline/#_footnotedef_2 "View footnote.")] This is the foundation of "Pipeline-as-code"; treating the CD pipeline as a part of the application to be versioned and reviewed like any other code.

Creating a `Jenkinsfile` and committing it to source control provides a number of immediate benefits:

*   Automatically creates a Pipeline build process for all branches and pull requests.

*   Code review/iteration on the Pipeline (along with the remaining source code).

*   Audit trail for the Pipeline.

*   Single source of truth [[3](https://www.jenkins.io/doc/book/pipeline/#_footnotedef_3 "View footnote.")] for the Pipeline, which can be viewed and edited by multiple members of the project.

While the syntax for defining a Pipeline, either in the web UI or with a `Jenkinsfile` is the same, it is generally considered best practice to define the Pipeline in a `Jenkinsfile` and check that in to source control.

### [](https://www.jenkins.io/doc/book/pipeline/#declarative-versus-scripted-pipeline-syntax)Declarative versus Scripted Pipeline syntax

A `Jenkinsfile` can be written using two types of syntax — Declarative and Scripted.

Declarative and Scripted Pipelines are constructed fundamentally differently. Declarative Pipeline is designed to make writing and reading Pipeline code easier, and provides richer syntactical features over Scripted Pipeline syntax.

Many of the individual syntactical components (or "steps") written into a `Jenkinsfile`, however, are common to both Declarative and Scripted Pipeline. Read more about how these two types of syntax differ in [Pipeline concepts](https://www.jenkins.io/doc/book/pipeline/#pipeline-concepts) and [Pipeline syntax overview](https://www.jenkins.io/doc/book/pipeline/#pipeline-syntax-overview) below.

[](https://www.jenkins.io/doc/book/pipeline/#why)Why Pipeline?
--------------------------------------------------------------

Jenkins is, fundamentally, an automation engine which supports a number of automation patterns. Pipeline adds a powerful set of automation tools onto Jenkins, supporting use cases that span from simple continuous integration to comprehensive CD pipelines. By modeling a series of related tasks, users can take advantage of the many features of Pipeline:

*   **Code**: Pipelines are implemented in code and typically checked into source control, giving teams the ability to edit, review, and iterate upon their delivery pipeline.

*   **Durable**: Pipelines can survive both planned and unplanned restarts of the Jenkins controller.

*   **Pausable**: Pipelines can optionally stop and wait for human input or approval before continuing the Pipeline run.

*   **Versatile**: Pipelines support complex real-world CD requirements, including the ability to fork/join, loop, and perform work in parallel.

*   **Extensible**: The Pipeline plugin supports custom extensions to its DSL [[1](https://www.jenkins.io/doc/book/pipeline/#_footnotedef_1 "View footnote.")] and multiple options for integration with other plugins.

While Jenkins has always allowed rudimentary forms of chaining Freestyle Jobs together to perform sequential tasks, [[4](https://www.jenkins.io/doc/book/pipeline/#_footnotedef_4 "View footnote.")] Pipeline makes this concept a first-class citizen in Jenkins.

What is the difference between Freestyle and Pipeline in Jenkins

Building on the core Jenkins value of extensibility, Pipeline is also extensible both by users with [Pipeline Shared Libraries](https://www.jenkins.io/doc/book/pipeline/shared-libraries) and by plugin developers. [[5](https://www.jenkins.io/doc/book/pipeline/#_footnotedef_5 "View footnote.")]

The flowchart below is an example of one CD scenario easily modeled in Jenkins Pipeline:

![Image 1: Pipeline Flow](https://www.jenkins.io/doc/book/resources/pipeline/realworld-pipeline-flow.png)

[](https://www.jenkins.io/doc/book/pipeline/#pipeline-concepts)Pipeline concepts
--------------------------------------------------------------------------------

The following concepts are key aspects of Jenkins Pipeline, which tie in closely to Pipeline syntax (refer to the [overview](https://www.jenkins.io/doc/book/pipeline/#pipeline-syntax-overview) below).

### [](https://www.jenkins.io/doc/book/pipeline/#pipeline)Pipeline

A Pipeline is a user-defined model of a CD pipeline. A Pipeline’s code defines your entire build process, which typically includes stages for building an application, testing it and then delivering it.

Also, a `pipeline` block is a [key part of Declarative Pipeline syntax](https://www.jenkins.io/doc/book/pipeline/#declarative-pipeline-fundamentals).

### [](https://www.jenkins.io/doc/book/pipeline/#node)Node

A node is a machine which is part of the Jenkins environment and is capable of executing a Pipeline.

Also, a `node` block is a [key part of Scripted Pipeline syntax](https://www.jenkins.io/doc/book/pipeline/#scripted-pipeline-fundamentals).

### [](https://www.jenkins.io/doc/book/pipeline/#stage)Stage

A `stage` block defines a conceptually distinct subset of tasks performed through the entire Pipeline (e.g. "Build", "Test" and "Deploy" stages), which is used by many plugins to visualize or present Jenkins Pipeline status/progress. [[6](https://www.jenkins.io/doc/book/pipeline/#_footnotedef_6 "View footnote.")]

### [](https://www.jenkins.io/doc/book/pipeline/#step)Step

A single task. Fundamentally, a step tells Jenkins _what_ to do at a particular point in time (or "step" in the process). For example, to execute the shell command `make`, use the `sh` step: `sh 'make'`. When a plugin extends the Pipeline DSL, [[1](https://www.jenkins.io/doc/book/pipeline/#_footnotedef_1 "View footnote.")] that typically means the plugin has implemented a new _step_.

[](https://www.jenkins.io/doc/book/pipeline/#pipeline-syntax-overview)Pipeline syntax overview
----------------------------------------------------------------------------------------------

The following Pipeline code skeletons illustrate the fundamental differences between [Declarative Pipeline syntax](https://www.jenkins.io/doc/book/pipeline/#declarative-pipeline-fundamentals) and [Scripted Pipeline syntax](https://www.jenkins.io/doc/book/pipeline/#scripted-pipeline-fundamentals).

Be aware that both [stages](https://www.jenkins.io/doc/book/pipeline/#stage) and [steps](https://www.jenkins.io/doc/book/pipeline/#step) (above) are common elements of both Declarative and Scripted Pipeline syntax.

### [](https://www.jenkins.io/doc/book/pipeline/#declarative-pipeline-fundamentals)Declarative Pipeline fundamentals

In Declarative Pipeline syntax, the `pipeline` block defines all the work done throughout your entire Pipeline.

Jenkinsfile (Declarative Pipeline)

```groovy
pipeline {
    agent any (1)
    stages {
        stage('Build') { (2)
            steps {
                // (3)
            }
        }
        stage('Test') { (4)
            steps {
                // (5)
            }
        }
        stage('Deploy') { (6)
            steps {
                // (7)
            }
        }
    }
}
```

**1**Execute this Pipeline or any of its stages, on any available agent.
**2**Defines the "Build" stage.
**3**Perform some steps related to the "Build" stage.
**4**Defines the "Test" stage.
**5**Perform some steps related to the "Test" stage.
**6**Defines the "Deploy" stage.
**7**Perform some steps related to the "Deploy" stage.

### [](https://www.jenkins.io/doc/book/pipeline/#scripted-pipeline-fundamentals)Scripted Pipeline fundamentals

In Scripted Pipeline syntax, one or more `node` blocks do the core work throughout the entire Pipeline. Although this is not a mandatory requirement of Scripted Pipeline syntax, confining your Pipeline’s work inside of a `node` block does two things:

1.   Schedules the steps contained within the block to run by adding an item to the Jenkins queue. As soon as an executor is free on a node, the steps will run.

2.   Creates a workspace (a directory specific to that particular Pipeline) where work can be done on files checked out from source control.

**Caution:** Depending on your Jenkins configuration, some workspaces may not get automatically cleaned up after a period of inactivity. Refer to the tickets and discussion linked from [JENKINS-2111](https://issue-redirect.jenkins.io/issue/2111) for more information.

Jenkinsfile (Scripted Pipeline)

```groovy
node {  (1)
    stage('Build') { (2)
        // (3)
    }
    stage('Test') { (4)
        // (5)
    }
    stage('Deploy') { (6)
        // (7)
    }
}
```

**1**Execute this Pipeline or any of its stages, on any available agent.
**2**Defines the "Build" stage. `stage` blocks are optional in Scripted Pipeline syntax. However, implementing `stage` blocks in a Scripted Pipeline provides clearer visualization of each `stage`'s subset of tasks/steps in the Jenkins UI.
**3**Perform some steps related to the "Build" stage.
**4**Defines the "Test" stage.
**5**Perform some steps related to the "Test" stage.
**6**Defines the "Deploy" stage.
**7**Perform some steps related to the "Deploy" stage.

[](https://www.jenkins.io/doc/book/pipeline/#pipeline-example)Pipeline example
------------------------------------------------------------------------------

Here is an example of a `Jenkinsfile` using Declarative Pipeline syntax — its Scripted syntax equivalent can be accessed by clicking the **Toggle Scripted Pipeline** link below:

Jenkinsfile (Declarative Pipeline)

```groovy
pipeline { (1)
    agent any (2)
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') { (3)
            steps { (4)
                sh 'make' (5)
            }
        }
        stage('Test'){
            steps {
                sh 'make check'
                junit 'reports/**/*.xml' (6)
            }
        }
        stage('Deploy') {
            steps {
                sh 'make publish' //
            }
        }
    }
}
```

[Toggle Scripted Pipeline](https://www.jenkins.io/doc/book/pipeline/#)_(Advanced)_

Jenkinsfile (Scripted Pipeline)

```groovy
node { //
    stage('Build') { (3)
        sh 'make' (5)
    }
    stage('Test') {
        sh 'make check'
        junit 'reports/**/*.xml' (6)
    }
    if (currentBuild.currentResult == 'SUCCESS') {
        stage('Deploy') {
            sh 'make publish' //
        }
    }
}
```

**1**[`pipeline`](https://www.jenkins.io/doc/book/pipeline/syntax#declarative-pipeline) is Declarative Pipeline-specific syntax that defines a "block" containing all content and instructions for executing the entire Pipeline.
**2**[`agent`](https://www.jenkins.io/doc/book/pipeline/syntax#agent) is Declarative Pipeline-specific syntax that instructs Jenkins to allocate an executor (on a node) and workspace for the entire Pipeline.
**3**`stage` is a syntax block that describes a [stage of this Pipeline](https://www.jenkins.io/doc/book/pipeline/#stage). Read more about `stage` blocks in Declarative Pipeline syntax on the [Pipeline syntax](https://www.jenkins.io/doc/book/pipeline/syntax#stage) page. As mentioned [above](https://www.jenkins.io/doc/book/pipeline/#scripted-pipeline-fundamentals), `stage` blocks are optional in Scripted Pipeline syntax.
**4**[`steps`](https://www.jenkins.io/doc/book/pipeline/syntax#steps) is Declarative Pipeline-specific syntax that describes the steps to be run in this `stage`.
**5**`sh` is a Pipeline [step](https://www.jenkins.io/doc/book/pipeline/syntax#steps) (provided by the [Pipeline: Nodes and Processes plugin](https://plugins.jenkins.io/workflow-durable-task-step)) that executes the given shell command.
**6**`junit` is another Pipeline [step](https://www.jenkins.io/doc/book/pipeline/syntax#steps) (provided by the [JUnit plugin](https://plugins.jenkins.io/junit)) for aggregating test reports.

Read more about Pipeline syntax on the [Pipeline Syntax](https://www.jenkins.io/doc/book/pipeline/syntax) page.

* * *

[1](https://www.jenkins.io/doc/book/pipeline/#_footnoteref_1). [Domain-specific language](https://en.wikipedia.org/wiki/Domain-specific_language)

[2](https://www.jenkins.io/doc/book/pipeline/#_footnoteref_2). [Source control management](https://en.wikipedia.org/wiki/Version_control)

[3](https://www.jenkins.io/doc/book/pipeline/#_footnoteref_3). [Single source of truth](https://en.wikipedia.org/wiki/Single_source_of_truth)

[4](https://www.jenkins.io/doc/book/pipeline/#_footnoteref_4). Additional plugins have been used to implement complex behaviors utilizing Freestyle Jobs such as the Copy Artifact, Parameterized Trigger, and Promoted Builds plugins 

[5](https://www.jenkins.io/doc/book/pipeline/#_footnoteref_5). [GitHub Branch Source plugin](https://plugins.jenkins.io/github-branch-source)

[6](https://www.jenkins.io/doc/book/pipeline/#_footnoteref_6). [Blue Ocean](https://www.jenkins.io/doc/book/blueocean), [Pipeline: Stage View plugin](https://plugins.jenkins.io/pipeline-stage-view)

* * *

[⇐ Using Jenkins](https://www.jenkins.io/doc/book/using)

[Index](https://www.jenkins.io/doc/book/)

[Getting started with Pipeline ⇒](https://www.jenkins.io/doc/book/pipeline/getting-started)

* * *

[Was this page helpful?](https://www.jenkins.io/doc/book/pipeline/#feedback)

Please submit your feedback about this page through this [quick form](https://www.jenkins.io/doc/feedback-form/).

Alternatively, if you don't wish to complete the quick form, you can simply indicate if you found this page helpful?

Yes No

Submit

See existing feedback [here](https://docs.google.com/spreadsheets/d/1IIdpVs39JDYKg0sLQIv-MNO928qcGApAIfdW5ohfD78).
