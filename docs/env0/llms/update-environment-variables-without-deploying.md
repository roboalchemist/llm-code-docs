# Source: https://docs.envzero.com/changelogs/2023/07/update-environment-variables-without-deploying.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ✍️ Update Environment Variables without Deploying

> Using an infrastructure-as-code model, variables are used to customize certain aspects of a configuration for a specific deployment, without having to change the code. In this way, a single configuration can be used in different contexts to create different deployments. Now for an environment that already exists,  you can also edit the variables settings under the environment _Variables_ tab without the need to trigger a deployment.

Using an infrastructure-as-code model, variables are used to customize certain aspects of a configuration for a specific deployment, without having to change the code. In this way, a single configuration can be used in different contexts to create different deployments. Now for an environment that already exists,  you can also edit the variables settings under the environment _Variables_ tab **without the need to trigger** a deployment.

## ✨ Saving Variables ✨

In order to change an environment variable, simply go to the environment page, and under the `Variables` tab change the relevant variables and click on the `Save` button.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/07/0648384-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=97c40fe59f3be47fadc8aa3ee43a2505" alt="Feature demonstration screenshot showing new functionality" width="1545" height="976" data-path="images/changelogs/2023/07/0648384-image.png" />
</Frame>

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/envzero-b61043c8/changelogs/2023/07/%3C%3E" alt="Feature demonstration screenshot showing new functionality" />
</Frame>

> 🚧 Limits
>
> Changes to variables for an existing environment will not take effect until the environment is redeployed.  When env0 runs a deployment, it stores the variable names to be used in undeploy so changes for an _Active_ environment will not affect the undeploy process.

Built with [Mintlify](https://mintlify.com).
