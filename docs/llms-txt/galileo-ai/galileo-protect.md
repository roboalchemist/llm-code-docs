# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect.md

# Overview of Galileo Protect

> Explore Galileo Protect to safeguard AI applications with customizable rulesets, error detection, and robust metrics for enhanced AI governance.

**Proactive GenAI security is here** -- Protect intercepts prompts and outputs to prevent unwanted behaviors and safeguard your brand and your end-users.

With Protect you can protect your system and your users from:

* Harmful requests and security threats (e.g. Prompt Injections, toxic language)
* Data Privacy protection (e.g. PII leakage)
* Hallucinations

Protect leverages [Galileo's Guardrail Metrics](/galileo/gen-ai-studio-products/galileo-guardrail-metrics) to power its safeguards.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/protect-api-background.gif)

### The Workflow

<Steps>
  <Step title="Establish your rules">
    Define you need protection from. Choose a set of metrics and conditions to
    help you achieve that. Determine what your system should do when those rules are broken.
  </Step>

  <Step title="Iterate on your conditions">
    Run your Protect rules through a comprehensive evaluation to ensure Protect
    is working for you. Run your evaluation set and check for any over- or
    under-triggering. Iterate on your conditions until you're satisfied.
  </Step>

  <Step title="Take Protect to production">
    Deploy your Protect checks to production. (Optional) Register your stages so
    they can be updated on the fly.

    Use Observe to monitor your system in production.
  </Step>
</Steps>

### Getting Started

<CardGroup cols={1}>
  <Card title="Quickstart" icon="chevron-right" href="/galileo/gen-ai-studio-products/galileo-protect/quickstart" horizontal />
</CardGroup>
