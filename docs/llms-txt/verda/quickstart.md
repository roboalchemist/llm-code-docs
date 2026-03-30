# Source: https://docs.verda.com/storage/container-registry/quickstart.md

# Quickstart

Create registry credentials from the **Container Registry** or **Keys** page:

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2FgDIaFMGE5Z6P1ZOmH47R%2FCreate%20credentials.png?alt=media&#x26;token=f17a45a3-b633-4304-82e6-405728b6a565" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The credentials name will be prefixed with: `vcr-<PROJECT_ID>+`

Example: `credentials-name` and project id `f64a8306-af4e-423c-b4bc-be5b3b4ec560` it would be `vcr-f64a8306-af4e-423c-b4bc-be5b3b4ec560+credentials-name`
{% endhint %}

**In your local environment:**

Use the credentials name and secret to log into the registry. Prefer `--password-stdin` to avoid leaking the secret in shell history.

```bash
echo '<SECRET>' | docker login vccr.io/<PROJECT_ID> -u 'vcr-<PROJECT_ID>+credentials-name' --password-stdin
```

Then tag an image and push it to the registry:

```bash
docker tag <SOURCE_IMAGE>[:TAG] vccr.io/<PROJECT_ID>/<IMAGE-NAME>[:TAG]
docker push vccr.io/<PROJECT_ID>/<IMAGE-NAME>[:TAG]
```

{% code title="Example:" fullWidth="false" expandable="true" %}

```bash
echo 'NOdNc9Vm8skBEx7N5eXJzHdWuHjJOYHC' | docker login vccr.io/f64a8306-af4e-423c-b4bc-be5b3b4ec560 -u 'vcr-f64a8306-af4e-423c-b4bc-be5b3b4ec560+credentials-name' --password-stdin
docker tag hello-world:v1.0.0 vccr.io/f64a8306-af4e-423c-b4bc-be5b3b4ec560/hello-world:v1.0.0
docker push vccr.io/f64a8306-af4e-423c-b4bc-be5b3b4ec560/hello-world:v1.0.0
```

{% endcode %}

***

After pushing an image, you may create a serverless container deployment from it by clicking the **Create deployment** button from the actions menu:

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2FTFD3CPC8Rn5ZnMK2TDyE%2FCreate%20deployment.png?alt=media&#x26;token=697bbb3d-ff12-4f53-b439-dce565915f83" alt=""><figcaption></figcaption></figure>

Alternatively, you can create a serverless container deployment based on your image by entering the image URL and the Verda registry credentials in the **New deployment** page:

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2FcQmeYOl1H75i5s8nb4mj%2FContainer%20deployment.png?alt=media&#x26;token=6490a28d-0846-4191-b9a9-f1691a97e6cf" alt=""><figcaption></figcaption></figure>
