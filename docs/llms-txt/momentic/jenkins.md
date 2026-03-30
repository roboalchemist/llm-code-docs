# Source: https://momentic.ai/docs/ci/jenkins.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Jenkins

The following example shows how to use Momentic with
[Jenkins](https://www.jenkins.io/).

For more usage examples, see the
[momentic-ai/examples](https://github.com/momentic-ai/examples) repository.

For a given root `package.json`:

```json package.json theme={null}
{
  "name": "my-momentic-repo",
  "scripts": {},
  "devDependencies": {
    "momentic": "latest"
  }
}
```

Create a file called `Jenkinsfile` in your repository with the following
contents:

```java Jenkinsfile theme={null}
pipeline {
    agent any

    tools {
        nodejs 'NodeJS 20'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm ci'
            }
        }

        stage('Install Browsers for Momentic') {
            steps {
                sh 'npx momentic install-browsers --all'
            }
        }

        stage('Run Momentic Tests and Upload Results') {
            steps {
                sh 'npx momentic run'
            }
            post {
                always {
                    sh 'npx momentic results upload test-results'
                }
            }
        }
    }
}
```

## Authentication

To run any commands, you must authenticate with Momentic. You can do this by
adding the `momentic-api-key` credential to your Jenkins instance.

1. Create an API key in
   [Momentic Cloud](https://app.momentic.ai/settings/api-keys).

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/create-api-key.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=54eb9f3c01e00a3ae7d71996760dcd39" width="3616" height="2434" data-path="images/create-api-key.png" />
</Frame>

Copy the value to a safe place. You'll need it in a moment.

2. Add a new global credential to your Jenkins controller.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/ci/jenkins-credentials.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=9a3ab99eaf8a2c514dd4f12910ee57f3" width="1440" height="861" data-path="images/ci/jenkins-credentials.png" />
</Frame>

3. At the top of your `Jenkinsfile`, provide the following environment variables
   to the pipeline:

```java Jenkinsfile {4-7} theme={null}
pipeline {
    agent any

    // To authenticate, set the following environment variables.
    environment {
        MOMENTIC_API_KEY = credentials('momentic-api-key')
    }

    // ...
}
```


Built with [Mintlify](https://mintlify.com).