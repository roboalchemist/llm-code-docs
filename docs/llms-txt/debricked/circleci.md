# Source: https://docs.debricked.com/tools-and-integrations/integrations/circleci.md

# CircleCI

CircleCI is supported by using our debricked/debricked-scan Docker image. The CircleCI integration supports the same options as our Bitbucket integration, [read more about the options here.](https://bitbucket.org/debricked/debricked-scan/src/master/)

### **Configure** OpenText Core SCA **token**

Start by [generating an access token](https://docs.debricked.com/product/administration/generate-access-token). Configure your DEBRICKED\_TOKEN variable using the access token, by heading over to your **Project Settings** -> **Environment Variables**, and add DEBRICKED\_TOKEN, as below.

### **Configure CircleCI job**

Depending on what package manager you are using there are different job setups.

In order for us to analyze all dependencies in your project, their versions, and relations, files containing the resolved dependency trees have to be created prior to scanning. Those depend on the package manager used. OpenText Core SCA tries to generate the lacking files, which can negatively affect speed and accuracy.

**Example 1:** If [**npm**](https://www.npmjs.com/) is used in your project you will have a "package.json" file, but in order for us to scan all your dependencies, OpenText Core SCA requires either "package-lock.json" or "yarn.lock" as well.

**Example 2:** If [**Maven**](https://maven.apache.org/) is used in your project, you will have a pom.xml file, but in order for us to resolve all your dependencies, OpenText Core SCA requires a second file, as Maven does not offer a lock file system. Instead, "Maven dependency:tree" plugin can be used to create a file called "*.debricked-maven-dependencies.tgf".*

Add the following template to your *.circleci/config.yml* file (if the file does not exist, create one):

{% @github-files/github-code-block url="<https://github.com/debricked/cli/blob/main/examples/templates/CircleCI/config.yml>" %}

Commit your changes to "*.circleci/config.yml"* and watch the CI run.
