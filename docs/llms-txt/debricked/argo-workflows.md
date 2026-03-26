# Source: https://docs.debricked.com/tools-and-integrations/integrations/argo-workflows.md

# Argo workflows

Argo Workflows is supported by using our "debricked/debricked-scan Docker" image.&#x20;

Our Argo workflows integration support the same options as our Bitbucket integration, read more about the options here <https://bitbucket.org/debricked/debricked-scan>

### **Configure** OpenText Core SCA **token**

Start by [generating an access token](https://docs.debricked.com/product/administration/generate-access-token). Copy the token so that you can use it in the next step.

### **Configure Argo workflow**

Depending on what package manager you are using there are different step setups.

In order to analyze all dependencies in your project, their versions, and relations, files containing the resolved dependency trees should be created prior to scanning. The file creation depends on the package manager used. OpenText Core SCA tries to generate the lacking files, which can negatively affect speed and accuracy.

**Example 1:** If [**npm**](https://www.npmjs.com/) is used in your project, you will have a "package.json" file, but in order to scan all your dependencies, OpenText Core SCA requires either "package-lock.json" or "yarn.lock" as well.

**Example 2:** If [**Maven**](https://maven.apache.org/) is used in your project, you will have a "pom.xml" file, but in order to resolve all your dependencies, OpenText Core SCA requires a second file, as Maven does not offer a lock file system. Instead, "Maven dependency:tree "plugin can be used to create a file called "*.debricked-maven-dependencies.tgf".*

1. Add the [template](http://github.com/debricked/cli/tree/main/examples/templates/Argo) to your ".circleci/config.yml" file (if the file does not exist, create one):

{% @github-files/github-code-block url="<https://github.com/debricked/cli/blob/main/examples/templates/Argo/argo.yml>" %}

Consider [using kubernetes](https://github.com/argoproj/argo-workflows/blob/master/examples/secrets.yaml) secrets instead of parameter binding with -p.

* <pre class="language-bash"><code class="lang-bash"><strong>argo submit -n {namespace} --watch {template} \
  </strong>-p debricked-token={debricked-token} \
  -p git-url={git-url}
  </code></pre>
