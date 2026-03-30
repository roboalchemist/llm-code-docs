# Source: https://docs.debricked.com/tools-and-integrations/integrations/buildkite.md

# BuildKite

BuildKite is supported by using [debricked/debricked-scan](https://github.com/debricked/debricked-scan).

The BuildKite integration supports the same options as Bitbucket integration, you can read more about the options here: <https://bitbucket.org/debricked/debricked-scan>.

### **Configure** OpenText Core SCA **token**

Start by [generating an access token](https://docs.debricked.com/product/administration/generate-access-token). Copy the token, so that you can use it in the next step.

Create a [pipeline secret](https://buildkite.com/docs/pipelines/secrets), that is called DEBRICKED\_TOKEN and has the previously created access token as its value.

### **Configure BuildKite**

If you do not have a BuildKite pipeline set up for your repository, make sure to [create one](https://buildkite.com/docs/tutorials/getting-started#add-the-sample-pipeline).

In order for us to analyze all dependencies in your project, their versions, and relations, files containing the resolved dependency trees have to be created prior to scanning. Those depend on the package manager used. OpenText Core SCA tries to generate the lacking files, which can negatively affect speed and accuracy.

**Example 1:** If [**npm**](https://www.npmjs.com/) is used in your project you will have a "package.json" file, but in order for us to scan all your dependencies, OpenText Core SCA requires either "package-lock.json" or "yarn.lock" as well.

**Example 2:** If [**Maven**](https://maven.apache.org/) is used in your project, you will have a pom.xml file, but in order for us to resolve all your dependencies, OpenText Core SCA requires a second file, as Maven does not offer a lock file system. Instead, "Maven dependency:tree" plugin can be used to create a file called "*.debricked-maven-dependencies.tgf".*

Add the template to your ".circleci/config.yml" file (if the file does not exist, create one):

{% @github-files/github-code-block url="<https://github.com/debricked/cli/blob/main/examples/templates/BuildKite/pipeline.yml>" %}

Commit your changes to ".buildkite/pipeline.yml" and watch the CI run.
