# Source: https://docs.debricked.com/tools-and-integrations/integrations/travis-ci.md

# Travis CI

You can integrate your Travis CI pipeline with OpenText Core SCA by using our debricked/debricked-scan Docker image. Just like our other CI integrations it just takes a few minutes to set up!

### **Configure** OpenText Core SCA **token**

1. Start by [generating an access token](https://docs.debricked.com/product/administration/generate-access-token). Copy the token to use in the next step.
2. Set your DEBRICKED\_TOKEN variable by going to your repository, click **More options -> settings** and go the section **Environment Variables**. Use the access token created in the previous step. Be sure to disable the **Show value in build log** button, so that you do not expose your login credentials to the world.

### **Configure Travis CI workflow**

Depending on what package manager you are using there are different step setups.

In order to analyze all dependencies in your project, their versions, and relations, files containing the resolved dependency trees have to be created prior to scanning. Those depend on the package manager used. OpenText Core SCA tries to generate the lacking files, which can negatively affect speed and accuracy.

**Example 1:** If [**npm**](https://www.npmjs.com/) is used in your project you will have a "package.json" file, but in order to scan all your dependencies, OpenText Core SCA requires either "package-lock.json" or "yarn.lock" as well.

**Example 2:** If [**Maven**](https://maven.apache.org/) is used in your project, you will have a "pom.xml" file, but in order to resolve all your dependencies, OpenText Core SCA requires a second file, as Maven does not offer a lock file system. Instead, "Maven dependency:tree" plugin can be used to create a file called "*.debricked-maven-dependencies.tgf".*

1. Choose one of the following templates and add it to your "travis.yml" file. If the file does not exist, create one:

{% @github-files/github-code-block url="<https://github.com/debricked/cli/blob/main/examples/templates/Travis/travis.yml>" %}

2. Commit your changes on the ".travis.yml" file and watch the CI run.
