# Source: https://docs.envzero.com/guides/admin-guide/templates/pulumi.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pulumi Integration

> Deploy Pulumi stacks with env zero using programming languages like Python, TypeScript, and Go

[Pulumi](https://www.env0.com/blog/what-is-pulumi-and-how-to-use-it-with-env0) is an infrastructure-as-code framework that harnesses popular programming languages such as Go, JS/TS, Python, and .NET Platform. With env zero, you can enjoy all of the benefits that are built on top of it such as Plan on Pull Request, Drift Detection, and more...

Unlike the HCL language that is used in terraform, Pulumi represents the concept of writing IaC by commonly used programming languages. There are many benefits of such concept, for example, strong-type support, homogeneous codebase, testing easiness, etc. You can read more about Pulumi in their [docs.](https://www.pulumi.com/docs/)

## Environment Deployment

In order to manage your Pulumi executions in env zero, you may have to follow the next steps:

1. Create a Pulumi [Template](/guides/admin-guide/templates) first.
2. Create [`env0.yml`](/guides/admin-guide/custom-flows) file in the target repository and inject a required packages installation command\
   (`npm i` for example, see [gist](https://gist.github.com/away168/50b406854197657d8a4631b9f52203e1)).
3. [Connect your cloud account](/guides/getting-started/getting-started/connect-your-cloud-account)
4. Add `PULUMI_ACCESS_TOKEN` environment variable
5. Create an environment, you can set the stack name if you already configured one, if not, env zero will create a random stack name.

<Warning>
  State Storage

  Currently, env zero does not store the stack state, which means that it is saved in Pulumi's remote backend or using a Pulumi self-managed option. See [Pulumi Docs on State Storage](https://www.pulumi.com/docs/concepts/state/)for more details.
</Warning>

## Execution Steps

Beyond the common steps such as Clone, Loading variables, etc. Deploy/Destroy Pulumi environment contains the following steps:

1. Pulumi Login - `pulumi login --non-interactive`
2. Stack Selection - `pulumi stack select --create <stack_name>`
3. Pulumi Preview - `pulumi preview --refresh --diff --show-replacement-steps`
4. Pulumi Up - `pulumi up -f --yes --refresh --diff --show-replacement-steps`
5. Pulumi Stack Output
6. Pulumi Destroy - `pulumi destroy -f --yes --refresh --diff --show-replacement-steps`

<img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/325a55c-screen_shot_2022-03-24_at_15.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=e9e8036088e4d6b547c9071a8d129747" alt="" width="1592" height="837" data-path="images/guides/admin-guide/templates/325a55c-screen_shot_2022-03-24_at_15.png" />

## Additional Configuration

Check out [Pulumi's Environment Variable configurations](https://www.pulumi.com/docs/cli/environment-variables/) to further customize your environment

For example, if you want to use your own S3 remote backend, simply create an Environment Variable in your env zero Environment with `PULUMI_BACKEND_URL=s3://your-pulumi-state-bucket`

Built with [Mintlify](https://mintlify.com).
