# Source: https://www.promptfoo.dev/docs/enterprise/red-teams/

# Running Red Teams

Promptfoo Enterprise allows you to configure targets, plugin collections, and scan configurations that can be shared among your team.

## Connecting to Promptfoo

Promptfoo requires access to [*.promptfoo.app](https://promptfoo.app/) to function.

If you are using a proxy or VPN, you may need to add these domains to your whitelist before you can generate red teams.

## Creating Targets

Targets are the LLM entities that are being tested. They can be a web application, agent, foundation model, or any other LLM entity. When you create a target, this target can be accessed by other users in your team to run scans.

You can create a target by navigating to the "Targets" tab and clicking "Create Target".

The "General Settings" section is where you identify the type of target you are testing and provide the technical details to connect to the target, pass probes, and parse responses.

The "Context" section is where you provide any additional information about the target that will help Promptfoo generate adversarial probes. This is where you provide context about the target's primary objective and any rules it should follow, as well as what type of user the red team should impersonate.

The more information you provide, the better the red team attacks and grading will be.

### Accessing External Systems

If your target has RAG orchestration or is an agent, you can select the "Accessing External Systems" option to provide additional details about the target's connection to external systems. Providing additional context about the target's access to external systems will help Promptfoo generate more accurate red team attacks and grading.

If your target is an agent, you can provide additional context about the agent's access to tools and functions in the question "What external systems are connected to this application?" This will help Promptfoo ascertain whether it was able to successfully enumerate tools and functions when running the [tool discovery plugin](/docs/red-team/plugins/tool-discovery/).

## Creating Plugin Collections

You can create plugin collections to share among your team. These plugin collections allow you to create specific presets to run tests against your targets, including establishing custom policies and prompts.

To create a plugin collection, navigate to the "Plugin Collections" tab under the "Red team" navigation header and click "Create Plugin Collection".

![Creating a new plugin collection](/assets/images/create-plugin-collection-0a48966b122072d9a108fba04d1bca6f.gif)

## Configuring Scans

When you want to run a new red team scan, navigate to the "Red team" navigation header and click on "Scan Configurations". You will see a list of all the scan configurations that your team has created. Click on "New Scan" to create a new scan.

![Create Scan Configuration interface](/assets/images/create-scan-9c00c4a07c2370aa62716983465ee22a.png)

If you have already created a scan configuration from the open-source version of Promptfoo or local usage, you can import the YAML file to use it in Promptfoo Enterprise.

Click on "Create Scan" to configure a new scan. You will then be prompted to select a target. Alternatively, you can create a new target.

![Select Target screen](/assets/images/select-target-d85643a41c1b3e8cd221ad0ee7372a17.png)

Once you have selected a target, you will be prompted to select a plugin collection. If you do not have a plugin collection, you can create a new one.

![Select Plugin Collection screen](/assets/images/choose-plugins-1c70f723e41b783964fd4a07d0bb8c16.png)

Once you have selected a plugin collection, you will be prompted to select the strategies. [Promptfoo strategies](/docs/red-team/strategies/) are the ways in which adversarial probes are delivered to maximize attack success rates.

![Select Strategies screen](/assets/images/select-strategies-8dcb777fb0de1bc52e9476f4f20bb1ea.png)

## Running a Scan

Once you have configured a scan by selecting a target, plugin collection, and strategies, you can generate a red team scan by navigating to the "Review" section. Click on "Save Configuration" for Promptfoo to generate a CLI command. You will need to [authenticate](/docs/enterprise/authentication/) into the CLI to run the scan and share the results.

![Run Scan configuration screen](/assets/images/run-scan-36207c3e9ed604c4e9b70c00dea411d3.png)

Alternatively, you can download the Promptfoo YAML file and run the scan locally.

When you enter the command into your terminal, Promptfoo will generate the adversarial probes and write the test cases locally.

![Running scan in CLI](/assets/images/run-scan-cli-176d18dcda96800917c4c33a92d6bcdc.png)

Once generated, Promptfoo will execute the test cases against your target and upload the results to Promptfoo Enterprise. You can review the results by clicking on the evaluation link that is generated in the terminal or by navigating to Promptfoo Enterprise.

## See Also

- [Findings and Reports](/docs/enterprise/findings/)
- [Authentication](/docs/enterprise/authentication/)
- [Service Accounts](/docs/enterprise/service-accounts/)