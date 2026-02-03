# Source: https://docs.crewai.com/en/enterprise/guides/deploy-to-amp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy to AMP

> Deploy your Crew or Flow to CrewAI AMP

<Note>
  After creating a Crew or Flow locally (or through Crew Studio), the next step is
  deploying it to the CrewAI AMP platform. This guide covers multiple deployment
  methods to help you choose the best approach for your workflow.
</Note>

## Prerequisites

<CardGroup cols={2}>
  <Card title="Project Ready for Deployment" icon="check-circle">
    You should have a working Crew or Flow that runs successfully locally.
    Follow our [preparation guide](/en/enterprise/guides/prepare-for-deployment) to verify your project structure.
  </Card>

  <Card title="GitHub Repository" icon="github">
    Your code should be in a GitHub repository (for GitHub integration
    method)
  </Card>
</CardGroup>

<Info>
  **Crews vs Flows**: Both project types can be deployed as "automations" on CrewAI AMP.
  The deployment process is the same, but they have different project structures.
  See [Prepare for Deployment](/en/enterprise/guides/prepare-for-deployment) for details.
</Info>

## Option 1: Deploy Using CrewAI CLI

The CLI provides the fastest way to deploy locally developed Crews or Flows to the AMP platform.
The CLI automatically detects your project type from `pyproject.toml` and builds accordingly.

<Steps>
  <Step title="Install CrewAI CLI">
    If you haven't already, install the CrewAI CLI:

    ```bash  theme={null}
    pip install crewai[tools]
    ```

    <Tip>
      The CLI comes with the main CrewAI package, but the `[tools]` extra ensures you have all deployment dependencies.
    </Tip>
  </Step>

  <Step title="Authenticate with the Enterprise Platform">
    First, you need to authenticate your CLI with the CrewAI AMP platform:

    ```bash  theme={null}
    # If you already have a CrewAI AMP account, or want to create one:
    crewai login
    ```

    When you run either command, the CLI will:

    1. Display a URL and a unique device code
    2. Open your browser to the authentication page
    3. Prompt you to confirm the device
    4. Complete the authentication process

    Upon successful authentication, you'll see a confirmation message in your terminal!
  </Step>

  <Step title="Create a Deployment">
    From your project directory, run:

    ```bash  theme={null}
    crewai deploy create
    ```

    This command will:

    1. Detect your GitHub repository information
    2. Identify environment variables in your local `.env` file
    3. Securely transfer these variables to the Enterprise platform
    4. Create a new deployment with a unique identifier

    On successful creation, you'll see a message like:

    ```shell  theme={null}
    Deployment created successfully!
    Name: your_project_name
    Deployment ID: 01234567-89ab-cdef-0123-456789abcdef
    Current Status: Deploy Enqueued
    ```
  </Step>

  <Step title="Monitor Deployment Progress">
    Track the deployment status with:

    ```bash  theme={null}
    crewai deploy status
    ```

    For detailed logs of the build process:

    ```bash  theme={null}
    crewai deploy logs
    ```

    <Tip>
      The first deployment typically takes 10-15 minutes as it builds the container images. Subsequent deployments are much faster.
    </Tip>
  </Step>
</Steps>

## Additional CLI Commands

The CrewAI CLI offers several commands to manage your deployments:

```bash  theme={null}
# List all your deployments
crewai deploy list

# Get the status of your deployment
crewai deploy status

# View the logs of your deployment
crewai deploy logs

# Push updates after code changes
crewai deploy push

# Remove a deployment
crewai deploy remove <deployment_id>
```

## Option 2: Deploy Directly via Web Interface

You can also deploy your Crews or Flows directly through the CrewAI AMP web interface by connecting your GitHub account. This approach doesn't require using the CLI on your local machine. The platform automatically detects your project type and handles the build appropriately.

<Steps>
  <Step title="Pushing to GitHub">
    You need to push your crew to a GitHub repository. If you haven't created a crew yet, you can [follow this tutorial](/en/quickstart).
  </Step>

  <Step title="Connecting GitHub to CrewAI AMP">
    1. Log in to [CrewAI AMP](https://app.crewai.com)
    2. Click on the button "Connect GitHub"

    <Frame>
            <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e622053d392d9ca0033bb88b34d82f8d" alt="Connect GitHub Button" data-og-width="1021" width="1021" data-og-height="327" height="327" data-path="images/enterprise/connect-github.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=67a2ba40e2c5dabacfafcb2359e569cf 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=533ddd0da6106dc71b9cbcd010f89a5c 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=d8a3f55321172ab1e4179c6d05f30b4d 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=5dc5f7c278ecc22125a1f641454cec2d 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1d8f3da31bd39d97f37b7f405ef3b048 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7ce7bda27a7f94bb173f25fe9845a1cb 2500w" />
    </Frame>
  </Step>

  <Step title="Select the Repository">
    After connecting your GitHub account, you'll be able to select which repository to deploy:

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=937cf62f283090f134e299aa157aad22" alt="Select Repository" data-og-width="3366" width="3366" data-og-height="956" height="956" data-path="images/enterprise/select-repo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3f5167362c6836f644ab356b61c7f8db 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c1293a61ff1fba1b19b8669b942595da 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8ac1c94be313ab5c3c3f64741e3696be 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7991df0620583adeb443551dfbf8eeb8 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1bf91d7875849fb251fa92c24c1564aa 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=17ab305443f30d6f4796b2415564a3dc 2500w" />
    </Frame>
  </Step>

  <Step title="Set Environment Variables">
    Before deploying, you'll need to set up your environment variables to connect to your LLM provider or other services:

    1. You can add variables individually or in bulk
    2. Enter your environment variables in `KEY=VALUE` format (one per line)

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=84aa7644b9a1e20eb2e38309ce274ccb" alt="Set Environment Variables" data-og-width="3386" width="3386" data-og-height="606" height="606" data-path="images/enterprise/set-env-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c5521837a0ea86776e2ac13883f72750 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=98882c7ba545f4a09bc2248af54bc1ac 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=884ffc4ddc80104657dd60429f262254 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6f811c643a2268d264d95a3701a4d151 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=efd5564b6b4ffe6d68654cbdc8e515cc 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=51fb85358802539cb78c5dc7cf997b92 2500w" />
    </Frame>
  </Step>

  <Step title="Deploy Your Crew">
    1. Click the "Deploy" button to start the deployment process
    2. You can monitor the progress through the progress bar
    3. The first deployment typically takes around 10-15 minutes; subsequent deployments will be faster

    <Frame>
            <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=2eb5fa4cf040c65462a372b6667adc60" alt="Deploy Progress" data-og-width="3386" width="3386" data-og-height="1170" height="1170" data-path="images/enterprise/deploy-progress.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=91d47e6e3edc1df183acb360cbc6af1f 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f917ef44ece66ef051db174b4dea47d8 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=dfc99edd2ff1678afa564ae33cb9c784 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=522b1ce917f9ecd15aee60c0e2241965 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=62ab85baa7a80d6fb98c50fdb7d588c7 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3190fa0b08cfbcdc75d385bde06535fa 2500w" />
    </Frame>

    Once deployment is complete, you'll see:

    * Your crew's unique URL
    * A Bearer token to protect your crew API
    * A "Delete" button if you need to remove the deployment
  </Step>
</Steps>

## Option 3: Redeploy Using API (CI/CD Integration)

For automated deployments in CI/CD pipelines, you can use the CrewAI API to trigger redeployments of existing crews. This is particularly useful for GitHub Actions, Jenkins, or other automation workflows.

<Steps>
  <Step title="Get Your Personal Access Token">
    Navigate to your CrewAI AMP account settings to generate an API token:

    1. Go to [app.crewai.com](https://app.crewai.com)
    2. Click on **Settings** → **Account** → **Personal Access Token**
    3. Generate a new token and copy it securely
    4. Store this token as a secret in your CI/CD system
  </Step>

  <Step title="Find Your Automation UUID">
    Locate the unique identifier for your deployed crew:

    1. Go to **Automations** in your CrewAI AMP dashboard
    2. Select your existing automation/crew
    3. Click on **Additional Details**
    4. Copy the **UUID** - this identifies your specific crew deployment
  </Step>

  <Step title="Trigger Redeployment via API">
    Use the Deploy API endpoint to trigger a redeployment:

    ```bash  theme={null}
    curl -i -X POST \
         -H "Authorization: Bearer YOUR_PERSONAL_ACCESS_TOKEN" \
         https://app.crewai.com/crewai_plus/api/v1/crews/YOUR-AUTOMATION-UUID/deploy

    # HTTP/2 200
    # content-type: application/json
    #
    # {
    #   "uuid": "your-automation-uuid",
    #   "status": "Deploy Enqueued",
    #   "public_url": "https://your-crew-deployment.crewai.com",
    #   "token": "your-bearer-token"
    # }
    ```

    <Info>
      If your automation was first created connected to Git, the API will automatically pull the latest changes from your repository before redeploying.
    </Info>
  </Step>

  <Step title="GitHub Actions Integration Example">
    Here's a GitHub Actions workflow with more complex deployment triggers:

    ```yaml  theme={null}
    name: Deploy CrewAI Automation

    on:
      push:
        branches: [ main ]
      pull_request:
        types: [ labeled ]
      release:
        types: [ published ]

    jobs:
      deploy:
        runs-on: ubuntu-latest
        if: |
          (github.event_name == 'push' && github.ref == 'refs/heads/main') ||
          (github.event_name == 'pull_request' && contains(github.event.pull_request.labels.*.name, 'deploy')) ||
          (github.event_name == 'release')
        steps:
          - name: Trigger CrewAI Redeployment
            run: |
              curl -X POST \
                   -H "Authorization: Bearer ${{ secrets.CREWAI_PAT }}" \
                   https://app.crewai.com/crewai_plus/api/v1/crews/${{ secrets.CREWAI_AUTOMATION_UUID }}/deploy
    ```

    <Tip>
      Add `CREWAI_PAT` and `CREWAI_AUTOMATION_UUID` as repository secrets. For PR deployments, add a "deploy" label to trigger the workflow.
    </Tip>
  </Step>
</Steps>

## Interact with Your Deployed Automation

Once deployment is complete, you can access your crew through:

1. **REST API**: The platform generates a unique HTTPS endpoint with these key routes:

   * `/inputs`: Lists the required input parameters
   * `/kickoff`: Initiates an execution with provided inputs
   * `/status/{kickoff_id}`: Checks the execution status

2. **Web Interface**: Visit [app.crewai.com](https://app.crewai.com) to access:
   * **Status tab**: View deployment information, API endpoint details, and authentication token
   * **Run tab**: Visual representation of your crew's structure
   * **Executions tab**: History of all executions
   * **Metrics tab**: Performance analytics
   * **Traces tab**: Detailed execution insights

### Trigger an Execution

From the Enterprise dashboard, you can:

1. Click on your crew's name to open its details
2. Select "Trigger Crew" from the management interface
3. Enter the required inputs in the modal that appears
4. Monitor progress as the execution moves through the pipeline

### Monitoring and Analytics

The Enterprise platform provides comprehensive observability features:

* **Execution Management**: Track active and completed runs
* **Traces**: Detailed breakdowns of each execution
* **Metrics**: Token usage, execution times, and costs
* **Timeline View**: Visual representation of task sequences

### Advanced Features

The Enterprise platform also offers:

* **Environment Variables Management**: Securely store and manage API keys
* **LLM Connections**: Configure integrations with various LLM providers
* **Custom Tools Repository**: Create, share, and install tools
* **Crew Studio**: Build crews through a chat interface without writing code

## Troubleshooting Deployment Failures

If your deployment fails, check these common issues:

### Build Failures

#### Missing uv.lock File

**Symptom**: Build fails early with dependency resolution errors

**Solution**: Generate and commit the lock file:

```bash  theme={null}
uv lock
git add uv.lock
git commit -m "Add uv.lock for deployment"
git push
```

<Warning>
  The `uv.lock` file is required for all deployments. Without it, the platform
  cannot reliably install your dependencies.
</Warning>

#### Wrong Project Structure

**Symptom**: "Could not find entry point" or "Module not found" errors

**Solution**: Verify your project matches the expected structure:

* **Both Crews and Flows**: Must have entry point at `src/project_name/main.py`
* **Crews**: Use a `run()` function as entry point
* **Flows**: Use a `kickoff()` function as entry point

See [Prepare for Deployment](/en/enterprise/guides/prepare-for-deployment) for detailed structure diagrams.

#### Missing CrewBase Decorator

**Symptom**: "Crew not found", "Config not found", or agent/task configuration errors

**Solution**: Ensure **all** crew classes use the `@CrewBase` decorator:

```python  theme={null}
from crewai.project import CrewBase, agent, crew, task

@CrewBase  # This decorator is REQUIRED
class YourCrew():
    """Your crew description"""

    @agent
    def my_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['my_agent'],  # type: ignore[index]
            verbose=True
        )

    # ... rest of crew definition
```

<Info>
  This applies to standalone Crews AND crews embedded inside Flow projects.
  Every crew class needs the decorator.
</Info>

#### Incorrect pyproject.toml Type

**Symptom**: Build succeeds but runtime fails, or unexpected behavior

**Solution**: Verify the `[tool.crewai]` section matches your project type:

```toml  theme={null}
# For Crew projects:
[tool.crewai]
type = "crew"

# For Flow projects:
[tool.crewai]
type = "flow"
```

### Runtime Failures

#### LLM Connection Failures

**Symptom**: API key errors, "model not found", or authentication failures

**Solution**:

1. Verify your LLM provider's API key is correctly set in environment variables
2. Ensure the environment variable names match what your code expects
3. Test locally with the exact same environment variables before deploying

#### Crew Execution Errors

**Symptom**: Crew starts but fails during execution

**Solution**:

1. Check the execution logs in the AMP dashboard (Traces tab)
2. Verify all tools have required API keys configured
3. Ensure agent configurations in `agents.yaml` are valid
4. Check task configurations in `tasks.yaml` for syntax errors

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with deployment issues or questions
  about the AMP platform.
</Card>
