# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe.md

# Overview of Galileo Observe

> Monitor and analyze generative AI models with Galileo Observe, using real-time data insights to maintain performance and ensure quality outputs.

LLMs and LLM applications can have unpredictable behaviors. Mission-critical generative AI applications in production
require meticulous observability to ensure performance, security and positive user experience.

Galileo Observe helps you monitor your generative AI applications in production. With Observe you will understand how
your users are using your application and identify where things are going wrong. Keep tabs on your production system,
instantly receive alerts when bad things happen, and perform deep root cause analysis though the Observe dashboard.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/observe-3-screenshots.svg" width="100%" height="480px" />

## Core features

#### Real-time Monitoring

Keep a close watch on your Large Language Model (LLM) applications in production. Monitor the performance, behavior,
and health of your applications in real-time.

#### Guardrail Metrics

Galileo has built a number of [Guardrail Metrics](/galileo/gen-ai-studio-products/galileo-guardrail-metrics) to monitor
the quality and safety of your LLM applications in production. The same set of metrics you used during Evaluation and
Experimentation in pre-production can be used to keep tabs on your productionized system:

* Context Adherence
* Completeness
* Correctness
* Instruction Adherence
* Prompt Injections
* PII
* And more.

#### Custom Metrics

Every use case is different. And out-of-the-box metrics won't cover all your needs. Galileo allows you to customize our Guardrail Metrics
or to register your own.

#### Insights and Alerts

Always on, Galileo Observe sends you an alert when things go south. Trace errors down to the LLM call, Agent plan or
Vector Store lookup.
Stay informed about potential issues, anomalies, or improvements that require your attention.

### The Workflow

<Steps>
  <Step title="Log your production traffic">Integrate Observe into your production system</Step>
  <Step title="Set up your metrics and alerts">Define what you want to measure and set your expectations. Get alerted when anything goes wrong.</Step>
  <Step title="Debug, re-test">Debug and perform root cause analysis. Form hypothesis and test them using Evaluate, or use Protect to block these scenarios from occurring again.</Step>
</Steps>

### Getting Started

<CardGroup cols={1}>
  <Card title="Quickstart" icon="chevron-right" href="/galileo/gen-ai-studio-products/galileo-observe/getting-started" horizontal />
</CardGroup>
