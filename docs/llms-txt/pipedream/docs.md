# Source: https://pipedream.com/docs/index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction To Pipedream

export const PUBLIC_APPS = '3,000';

Pipedream provides the toolkit to add thousands of integrations to your app and enables you to automate any process.

<Columns cols={2}>
  <Card title="Connect tools" icon="plug" href="/connect">
    Add thousands of customer-facing integrations to your app or AI agent
  </Card>

  <Card title="Build workflows" icon="diagram-project" href="/workflows">
    Build, test, and deploy complex workflows to automate any process
  </Card>
</Columns>

The Pipedream platform includes:

* A [serverless runtime](/workflows/building-workflows/code/) and [workflow service](/workflows/building-workflows/)
* SDKs to handle [user authentication](/connect/) for {PUBLIC_APPS}+ APIs
* Source-available [triggers](/workflows/building-workflows/triggers/) and [actions](/workflows/building-workflows/actions/) for [thousands of integrated apps](https://pipedream.com/explore/)
* One-click [OAuth and key-based authentication](/apps/connected-accounts/) for more than {PUBLIC_APPS} APIs (use tokens directly in code or with pre-built actions)

## Getting Started

To get started, [sign up for a free account](https://pipedream.com/auth/signup) (no credit card required):

* **Building integrations for your app?** Follow our [Connect quickstart](/connect/quickstart) to add integrations using the CLI
* **Building workflows?** Follow our [workflow quickstart](/workflows/quickstart) to create your first automation

<Note>
  Learn how to provide Pipedream's documentation as context for your AI assistant or IDE [here](/ai-tooling).
</Note>

## Use Cases

Pipedream supports use cases from prototype to production and is trusted by more than 1 million developers from startups to Fortune 500 companies:

<Frame caption="">
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/2edb6b2f-logos_kcbviz.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=44586ae8cbfb4ab4bc1678700ec2a17e" width="1303" height="239" data-path="images/2edb6b2f-logos_kcbviz.png" />
</Frame>

The platform processes billions of events and is built and [priced](https://pipedream.com/pricing/) for use at scale. [Our team](https://pipedream.com/about) has built internet scale applications and managed data pipelines in excess of 10 million events per second (EPS) at startups and high-growth environments like BrightRoll, Yahoo!, Affirm, and Dropbox.

Our [community](https://pipedream.com/support) uses Pipedream for a wide variety of use cases including:

* AI agents and chatbots
* Workflow builders and SaaS automation
* API orchestration and automation
* Database automations
* Custom notifications and alerting
* Event queueing and concurrency management
* Webhook inspection and routing
* Prototyping and demos

## Source-available

Pipedream maintains a [source-available component registry](https://github.com/PipedreamHQ/pipedream) on GitHub so you can avoid writing boilerplate code for common API integrations. Use components as no code building blocks in workflows, or use them to scaffold code that you can customize. You can also [create a PR to contribute new components](/components/contributing/#contribution-process) via GitHub.

## Contributing

We hope that by providing a generous free tier, you will not only get value from Pipedream, but you will give back to help us improve the product for the entire community and grow the platform by:

* [Contributing components](/components/contributing/) to the [Pipedream registry](https://github.com/PipedreamHQ/pipedream) or sharing via your own GitHub repo
* Asking and answering questions in our [public community](https://pipedream.com/community/)
* [Reporting bugs](https://pipedream.com/community/c/bugs/9) and [requesting features](https://github.com/PipedreamHQ/pipedream/issues/new?assignees=\&labels=enhancement\&template=feature_request.md\&title=%5BFEATURE%5D+) that help us build a better product
* Following us on [Twitter](https://twitter.com/pipedream), starring our [GitHub repo](https://github.com/PipedreamHQ/pipedream) and subscribing to our [YouTube channel](https://www.youtube.com/c/pipedreamhq)
* Recommending us to your friends and colleagues

Learn about [all the ways you can contribute](https://pipedream.com/contributing).

## Support & Community

If you have any questions or feedback, please [reach out in our community forum](https://pipedream.com/community) or [to our support team](https://pipedream.com/support).

## Service Status

Pipedream operates a status page at [https://status.pipedream.com](https://status.pipedream.com/). That page displays the uptime history and current status of every Pipedream service.

When incidents occur, updates are published to the **#incidents** channel of [Pipedream’s Slack Community](https://pipedream.com/support) and to the [@PipedreamStatus](https://twitter.com/PipedreamStatus) account on Twitter. On the status page itself, you can also subscribe to updates directly.

Built with [Mintlify](https://mintlify.com).
