# Source: https://docs.promptlayer.com/why-promptlayer/agents.md

# Agents

<iframe width="640" height="360" src="https://www.youtube.com/embed/jidwFuKL5tg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

PromptLayer Agents let you quickly build, launch, and manage AI workflows that use multiple LLMs and business rules. You can create and test these AI systems easily using a visual drag-and-drop tool, and then deploy them without needing to worry about complex infrastructure management.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/workflow-dag.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=a85d81c25a267e7198a4e040af8e960a" alt="Agent DAG" data-og-width="1988" width="1988" data-og-height="1438" height="1438" data-path="images/agents/workflow-dag.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/workflow-dag.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=cb59040d21cb09da3ad02ee08cc9e0e3 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/workflow-dag.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=9667a36aa79409ff0e5443172306fd30 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/workflow-dag.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=90708e6caecd519af99de8fa67c5151a 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/workflow-dag.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=cf4f29a478908f057b609033c07a586b 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/workflow-dag.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=46ff790fa788a9b24e741d730064961b 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/workflow-dag.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=449deeaac0ce9ee8b494c9bdb92ad87c 2500w" />

## Use Cases

### 1. **Combining Multiple LLM Calls into a Single Output**

Improve AI-generated responses by using results from multiple LLM calls, either by merging outputs or choosing the best one. This can lead to:

* More thorough and precise outputs
* Enhanced decision-making by considering multiple perspectives
* Higher reliability through comparing multiple AI answers

### 2. **Building Complex Agents**

Create advanced AI systems that can handle multi-step tasks and solve complex problems. These systems can:

* Integrate multiple LLM calls
* Incorporate external data sources
* Automate complex decision-making processes

## Key Concepts

### 1. Input Variables

Input Variables are the data you feed into an Agent. They can be text, numbers, or other information the Agent uses in its various steps to produce the final result.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/input-variables.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=b235c83201ebf2bd4db279b472f8301d" alt="Input Variables" data-og-width="1402" width="1402" data-og-height="1004" height="1004" data-path="images/agents/input-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/input-variables.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=f25ac118063f5c145105cf2643655f1c 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/input-variables.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=0df98d0646529f7e0e0fbabbfbf6b5c0 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/input-variables.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=c70883dfe9591bc4d2aeff9c9a6efb1f 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/input-variables.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=724ddc31e5e230efdb47363ebb61decb 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/input-variables.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=392ada78968a203d2b72d3e87c43a8ab 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/input-variables.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=e975526f338187a17665f8f40624346b 2500w" />

### 2. Nodes

Nodes are the building blocks of the Agent. Each node represents a specific action or decision. Types include:

* **Prompt Template**: Make an LLM call using a specified prompt template and input variables.
* **Callback Endpoint**: Make external API calls (ex: RAG steps) or trigger callback requests after workflow processes finish.
* **Coding Agent**: Execute AI coding agents (such as Claude Code) in a sandboxed environment for data transformations, file processing, and complex analysis. [Learn more about Coding Agent](/features/evaluations/eval-types#coding-agent)
* **Math Operator**: Perform numerical comparisons or calculations between different data sources.
* **Parse Value**: Extract and process specific data types like strings, numbers, or JSON from inputs.

<Info>
  **Want to learn about all available node types?** Agent nodes use the same building blocks as evaluation types. [View all eval types](/features/evaluations/eval-types) to see the full catalog of nodes you can use in your agents, including LLM assertions, data extraction, conversation simulators, and more.
</Info>

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/nodes.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=7d8e9d3e1da1ab0423a9152386a2c63f" alt="Nodes" data-og-width="1584" width="1584" data-og-height="530" height="530" data-path="images/agents/nodes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/nodes.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=bf23e787aa8d575601e582f197e45c90 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/nodes.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=0bd9dc31e12a6b4414d2a7faa7ceb497 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/nodes.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=9149021f805309ffc9d41749d5e8a99a 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/nodes.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=f1408f6d563f56c80c8ecb4437dd8dbb 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/nodes.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=bcc9121fe3264f8a8206d90ba2ac3758 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/nodes.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=fe12d4019c9c70df38693203f558b747 2500w" />

### 3. Conditional Edges

Conditional Edges allow you to create branching logic within your Agent workflows. By clicking on an edge between nodes, you can define conditions that determine the path your workflow will take. Conditions can be combined using logical operators such as **AND** or **OR**, and support comparisons including:

* Equal (`==`)
* Not Equal (`!=`)
* Less Than (`<`)
* Greater Than (`>`)
* Less Than or Equal To (`<=`)
* Greater Than or Equal To (`>=`)

You can compare values against numbers or booleans, and multiple conditions can be combined to create complex branching logic. This enables your Agent to dynamically route execution paths based on intermediate results or external data, allowing for more sophisticated and context-aware workflows.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/conditional-edges.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=0f238a926c54fb6a12b59583dbb913a1" alt="Conditional Edges" data-og-width="1086" width="1086" data-og-height="960" height="960" data-path="images/agents/conditional-edges.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/conditional-edges.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=e9a6eb22c2b52001072c93875548ba29 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/conditional-edges.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=38d37f4c5be3fe21090d8c8a0cdbc2c0 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/conditional-edges.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=0479fa8b1424272cb85618e00cc70aff 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/conditional-edges.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=b0c441d1fca7b593b310b6e8ff9d35c1 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/conditional-edges.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=61329fde3bb1f8d39087e42801606064 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/conditional-edges.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=320eb2a7a824fafa437334ca10c222db 2500w" />

### 4. Output Nodes

Output Nodes determine what your Agent returns as its final result. When using Conditional Edges to create different paths in your workflow, you can place multiple Output Nodes at the end of different branches. Similar to a "return statement" in programming, whichever Output Node executes successfully first will provide the final output. This allows your Agent to deliver different results based on the specific conditions that were met during the workflow.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/output-node.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=1959ee88ed63c1204dd2f052c823ad84" alt="Output Nodes" data-og-width="1050" width="1050" data-og-height="470" height="470" data-path="images/agents/output-node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/output-node.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=7b109dad799e9f2344055984a98ad58f 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/output-node.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=8ccf2da71ef7ff417f872a4ff2bb0d8a 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/output-node.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=28d62c60fac1ef30c61c500d09251672 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/output-node.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=bac443e2b2f35f30299a4f29467e02c3 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/output-node.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=b8f042bd3efca6ed33de8205651bb61b 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/output-node.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=aac9a6e1e3812ee832ad615658b8cf0d 2500w" />

## Versioning

Agent versioning automatically tracks changes over time. Each update creates a new version, allowing you to safely experiment with new ideas while keeping the current production version stable. You can view the full history of your Agent's changes, which helps with team collaboration and iterative development.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/versions.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=415ba5738a289b6f9a5e5b87f408cb42" alt="Versioning" data-og-width="880" width="880" data-og-height="490" height="490" data-path="images/agents/versions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/versions.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=8c2967f392c9c35ad78565f456e694ed 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/versions.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=8e47fcfa605fb6544c12094a04d56b56 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/versions.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=6608a8aedf7f0b43f3e9595fac70a2f8 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/versions.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=f4b49695cbe47beda2a614b2901ead93 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/versions.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=beffc6c3d9cc2c0339850646575e0e78 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/versions.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=081c00bdb227d2753359a6e10189a76f 2500w" />

## Running an Agent

You can run an Agent in three ways: using the [Python or JavaScript SDK](/running-requests/promptlayer-run-agent), via the [REST API with polling](/running-requests/promptlayer-run-agent#run-agents-using-the-rest-api), or with the [REST API using callback webhooks](/running-requests/promptlayer-run-agent#run-agents-with-callback-webhooks) for long-running agents.

After running an Agent, the full trace, including spans from all nodes, will be visible in the left traces menu. This allows you to visualize the execution path and see intermediate outputs at each step, helping you debug and optimize your Agent.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/spans.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=8535d4c092fa6330135ce964b5205456" alt="Traces" data-og-width="1540" width="1540" data-og-height="1252" height="1252" data-path="images/agents/spans.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/spans.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=0b6a5e98efe7fdf500db9b7f1eb06100 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/spans.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=88c3c5e14f00c059118a42b08ba6912b 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/spans.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=24dc6ee5eb4a0c842fe2d7a64e9dde26 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/spans.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=d06e7ff6dfa6a5215df681d3c634183a 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/spans.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=a7fad3e119756d2cd061ae48f79c2dd6 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/agents/spans.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=6267701b8bed1c5baece19c22e39c9ab 2500w" />


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt