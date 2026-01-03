# Source: https://docs.lunary.ai/docs/more/self-hosting/kubernetes.md

# Kubernetes

Lunary was designed to be surprisingly simple to self-host, through a Helm Chart which includes the frontend, the API, and workers.<br />

<Note>
  Note: The Kubernetes setup is available only with [Lunary Enterprise
  Edition](https://lunary.ai/pricing)
</Note>

## Steps

<Steps>
  <Step title="Set up a PostgreSQL database">
    Set up a PostgreSQL database to store your Lunary data (version 15 or higher).
  </Step>

  <Step title="Log in to the private Docker Repository">
    Run the following command:

    ```bash  theme={null}
    helm registry login registry-1.docker.io -u lunarycustomer -p <your_organization_access_token>
    ```

    Your Organization's Access Token, will be provided by Lunary when your subscription is activated.
  </Step>

  <Step title="Download the Helm Chart">
    ```bash  theme={null}
    kubectl create ns lunary
    helm pull oci://registry-1.docker.io/lunary/lunary --untar --version '1.2.11' # contact Lunary support to get the latest version list
    ```
  </Step>

  <Step title="Set up mandatory secrets">
    ```bash  theme={null}
    kubectl create secret -n lunary docker-registry regcred --docker-server=docker.io --docker-username=lunarycustomer --docker-password=<your_organization_access_token>
    kubectl create secret -n lunary generic db-connection --from-literal=url="postgres://<username>:<password>@<host>:5432/lunary"
    kubectl create secret -n lunary generic license-key --from-literal=LICENSE_KEY='<license_key>'
    kubectl create secret -n lunary generic jwt-secret --from-literal=JWT_SECRET='<jwt_secret>' # You can generate a random string using `openssl rand -base64 32`
    ```

    Your License Key will be provided by Lunary when your subscription is activated.
    The Organization Access Token is the same one you used to log in with `helm login`.
  </Step>

  <Step title="(Optional) Set up API Keys and SMTP client">
    In order to use the Prompt Playground and [Evaluations](https://lunary.ai/docs/features/evals) features, you need to set up at least one of the following secrets:

    ```bash  theme={null}
    kubectl create secret -n lunary generic api-keys \
      --from-literal=OPENAI_API_KEY='<your-openai-api-key>' \
      # Or if using Azure
      --from-literal=AZURE_OPENAI_API_KEY='<your-azure-openai-api-key>' \
      --from-literal=AZURE_OPENAI_RESOURCE_NAME='<your-azure-openai-resource-name>' \
      --from-literal=AZURE_OPENAI_DEPLOYMENT_ID='<your-azure-openai-deployment-id>' \
      --from-literal=ANTHROPIC_API_KEY='<your-anthropic-api-key>' \
      --from-literal=OPENROUTER_API_KEY='<your-openrouter-api-key>' \
      --from-literal=PALM_API_KEY='<your-palm-api-key>'

    ```

    You can also use your custom email server to send invitations to members of your organization:

    ```bash  theme={null}
    kubectl create secret -n lunary generic smtp-config \
      --from-literal=EMAIL_SENDER_ADDRESS='<your-email-sender-address>' \
      --from-literal=SMTP_HOST='<your-smtp-host>' \
      --from-literal=SMTP_PORT='<your-smtp-port>' \
      --from-literal=SMTP_USER='<your-smtp-user>' \
      --from-literal=SMTP_PASSWORD='<your-smtp-password>
    ```

    Then, configure the corresponding values in `values.yaml`, in the Helm Chart's root directory:

    ```yaml  theme={null}
     ---
    global:
      ...
      secrets:
        useCustomSMTP: true
        useOpenAI: false
        useAzureOpenAI: true
        useAnthropic: true
        useOpenRouter: true
        usePalm: true
    ...

    ```
  </Step>

  <Step title="Install the Helm Chart">
    <Alert>
      Note: Before installing, please review at least the top-level values.yaml file. If you wish, it may also be useful to dive into the individual subchart values.yaml files for more custom configuration.
    </Alert>

    ```bash  theme={null}
    cd lunary
    helm upgrade --install -n lunary lunary .
    ```
  </Step>

  <Step title="🎉 Done!">
    The Helm Chart should be installed and ready to go.<br />
    You can now set up an ingress controller to expose the services.
  </Step>
</Steps>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt