# Source: https://docs.envzero.com/guides/policies-governance/cost-estimation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Estimate Costs

> Set up Infracost integration in env zero to estimate deployment costs before applying changes

## Cost Estimation

Cost estimation is a 3rd party tool provided by Infracost that can be used to help reviewers of deployment plans. Once activated for a project, every deployment plan would trigger a cost estimation calculation. This way, you can view a plan and its cost estimation, and decide whether or not to deploy this plan.

<Note>
  Frameworks Support

  Cost estimation is supported for deployments using Terraform, OpenTofu, or Terragrunt, including Terragrunt `run-all` deployments.
</Note>

<Warning>
  Temporary API key

  For the first 30 days, env zero supplies an infracost API key so you can try out cost estimation feature. Please make sure to create your dedicated API key as soon as possible if you decide to use it further. More details and pricing can be found [here](https://www.infracost.io/pricing/).
</Warning>

# Set Up Infracost Integration

Infracost integration can be set for both SaaS and Self-hosted agents.

## SaaS

1. Create an API key for infracost - see [infracost documentation](https://www.infracost.io/docs/#2-get-api-key).
2. Go to organization variables and create an `INFRACOST_API_KEY` secret environment variable in env zero

<img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/4373a82-image.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=1afb93cf738777ccd81d97bfa1406a44" alt="" width="2738" height="728" data-path="images/guides/policies-governance/4373a82-image.png" />

## Self Hosted Agent

1. Create an API key for infracost - see [infracost documentation](https://www.infracost.io/docs/#2-get-api-key).
2. Base64 encode the API key and deploy it with your agent configuration.  See [self-hosted agent documentation](/guides/admin-guide/self-hosted-kubernetes-agent/#customoptional-configuration) for more details, or
3. Save that API key in your AWS Secrets Manager as **plaintext**, and
4. Go to organization variables and create an `INFRACOST_API_KEY` secret environment variable in env zero, referencing the API key stored in Secrets Manager

<img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/247b1e9-b15dbe8-screen_shot_2021-04-26_at_18.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=02e5eea81906a588b4b2d4d8b694cc4e" alt="" width="1436" height="282" data-path="images/guides/policies-governance/247b1e9-b15dbe8-screen_shot_2021-04-26_at_18.png" />

# Enable Cost Estimation for your Project

To activatate cost estimation for your project, go to "Project Settings", and then to the "Policies" tab. Check the "Cost estimation" checkbox, and save.

<img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/209c199-3a89415-screen_shot_2021-04-26_at_18.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=a192d1f104094b4ca0cecc63729c8ecf" alt="" width="1439" height="368" data-path="images/guides/policies-governance/209c199-3a89415-screen_shot_2021-04-26_at_18.png" />

<img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/6c36061-d8c789c-cost-estimation-update.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=b248623224a3b13b2e04255ce075b094" alt="" width="2802" height="962" data-path="images/guides/policies-governance/6c36061-d8c789c-cost-estimation-update.png" />

<img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/247b1e9-b15dbe8-screen_shot_2021-04-26_at_18.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=02e5eea81906a588b4b2d4d8b694cc4e" alt="" width="1436" height="282" data-path="images/guides/policies-governance/247b1e9-b15dbe8-screen_shot_2021-04-26_at_18.png" />

Built with [Mintlify](https://mintlify.com).
