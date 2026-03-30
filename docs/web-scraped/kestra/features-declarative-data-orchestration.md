# Source: https://kestra.io/features/declarative-data-orchestration

Title: Declarative Orchestration with Kestra | Kestra

URL Source: https://kestra.io/features/declarative-data-orchestration

Markdown Content:
Bring Infrastructure as Code Best Practices to All Workflows

![Image 1: A screenshot of the user interface of Kestra's application](https://kestra.io/landing/features/declarative/header.svg)

Simple Workflow Definition in YAML
----------------------------------

YAML is easy to learn. The simple syntax allows more people in the organization to collaborate on building workflows together.

Kestra's built-in syntax validation ensures that your YAML code is error-free before execution, reducing the risk of runtime errors in production.

YAML is a superset of JSON, therefore it works extraordinaly well with REST APIs, while remaining human-readable and easy to understand.

Since you describe your workflow in a single YAML configuration, it's easy to track changes over time, collaborate on pull request reviews, and roll back when needed.

Due to separation of your orchestration logic from the business logic, you don't need any modifications to your existing code to orchestrate it with Kestra.

Need to adjust your workflow? Just edit the YAML file. No need for redeploying code and complex code packaging in CI/CD.

id: hello_world

namespace: dev

tasks:

- id: greeting

type: io.kestra.plugin.core.log.Log

message: Hello from a declarative workflow!

triggers:

- id: schedule

type: io.kestra.plugin.core.trigger.Schedule

cron: "@hourly"

Simple Yet Powerful
-------------------

The declarative syntax in a YAML format significantly reduces the barrier to entry. You can onboard new team members quickly, and maintain your workflows with minimal effort.

In just a few lines of YAML configuration, anyone in your team can build their first scheduled workflow. With that first success, your team members can start automating more advanced use cases with confidence.

Easily adapt workflows by updating your declarative configuration. No need for complex CI/CD pipelines.

Simplifies your codebase by eliminating boilerplate code. No need to write code to deploy code — each Kestra flow includes everything it needs to run.

Build workflows that are easy to read and understand for both technical and non-technical team members.

### YAML for Declarative Orchestration

- **Data structures:** YAML supports various data structures, such as mappings, sequences, and scalars, allowing for the flexible representation of complex data workflows.
- **Comments:** Inline comments in YAML files facilitate better communication and documentation within data teams, ensuring clarity and understanding of workflow logic.
- **Custom tags and types:** YAML allows for the definition of custom tags and types, enabling the creation of domain-specific languages and abstractions tailored to your data orchestration needs.

![Image 2: A YAML sample of code for declarative language and construction of Kestra's flows](https://kestra.io/landing/features/declarative/features_1.svg)

### Empower Your Team with Declarative Orchestration

- **Accelerate time to value:** Declarative orchestration modernized the creation and maintenance of data pipelines, enabling data teams to deliver results faster and more efficiently.
- **Speed up your development cycles:** By using a declarative approach, data teams can quickly adapt to changing business requirements without the need to overhaul complex procedural code.
- **Reduce maintenance burden:** Declarative workflows help minimize errors by allowing data teams to focus on defining the desired outcome, while Kestra's orchestrator takes care of the execution.

![Image 3: Image of execution of a task on Kestra with event or time based triggering](https://kestra.io/landing/features/declarative/features_2.svg)

1200+ Plugins

That Integrate With

Your  Stack
-----------------------------------------------

Integrate With

Your Stack
--------------------------

Connect with third-party systems, data sources, and applications. And if you require a custom integration, our platform makes it easy to build custom plugins.

[See All Plugins](https://kestra.io/plugins)
