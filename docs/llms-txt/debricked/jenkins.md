# Source: https://docs.debricked.com/tools-and-integrations/integrations/jenkins.md

# Jenkins

You can integrate your Jenkins pipeline with OpenText Core SCA, so that a vulnerability scan is performed every time the pipeline is triggered.&#x20;

### **Configure** OpenText Core SCA **token**

1. Start by [generating an access token](https://docs.debricked.com/product/administration/generate-access-token). Copy the token to use it in the next step.
2. Create the DEBRICKED\_TOKEN, which the pipeline will use. Inside Jenkins, go to your pipeline, click **Add Credentials**, and select the correct folder.&#x20;
3. Create a new credential with "Kind" set to secret text.&#x20;
4. In the **secret** field, insert the access token you created in the previous step. As ID, enter DEBRICKED\_TOKEN and click **Create**. See the image below:

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2Fn5GlH3ZdHHfPgL8OKIz3%2Fimage.png?alt=media&#x26;token=f1ba5a23-679a-460a-a706-0150e9b860fd" alt="Image show setting up Jenkins credentials for Debricked Scan"><figcaption><p>Setting up Jenkins credentials for Debricked Scan</p></figcaption></figure>

### **Configure Jenkins CI workflow or pipeline**

OpenText Core SCA assumes you already have a Jenkinsfile in your repository, describing a declarative pipeline. You now need to add a new stage to this pipeline.

Add the following template to the file:

{% @github-files/github-code-block url="<https://github.com/debricked/cli/blob/main/examples/templates/Jenkins/Jenkinsfile>" %}

Commit your changes to Jenkinsfile and watch the CI run.
