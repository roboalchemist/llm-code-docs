# Source: https://documentation.wazuh.com/current/user-manual/capabilities/active-response/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Active Response

Security teams often encounter problems in incident response such as addressing high severity events in a timely manner or providing complete mitigation actions. They might struggle to collect relevant information in real time, which makes it difficult to understand the full scope of an incident. These problems increase the difficulty to contain and mitigate the impact of a cyberattack.

Wazuh SIEM and XDR platform improves incident response by:

- Providing real-time visibility into security events.
- Reducing alert fatigue.
- Automating response actions to threats.
- Providing out-of-the-box response scripts.

Wazuh has an Active Response module that helps security teams automate response actions based on specific triggers, enabling them to effectively manage security incidents.

Automating response actions ensures that high-priority incidents are addressed and remediated in a timely and consistent manner. This is especially valuable in environments where security teams are resource constrained and need to prioritize their response efforts.

In addition, the module includes a range of out-of-the-box response scripts that help respond to threats and mitigate them. For example, some scripts block malicious network access and delete malicious files on monitored endpoints. These actions reduce the workload on security teams and enable them to effectively manage incidents.

The Wazuh Active Response module executes these scripts on monitored endpoints when an alert of a specific rule ID, level, or rule group triggers. You can set any number of scripts to initiate in response to a trigger; however, you must consider these responses carefully. Poor implementation of rules and responses might increase the vulnerability of an endpoint.

The image below shows the Active Response workflow.

<a id="wazuh_image-0"></a>
![](images/manual/active-response/active-response-workflow.png)

### Types of active response

An active response can either be:

- Stateless
- Stateful

Stateless active responses are one-time actions without an event definition to revert or stop them. Stateful responses revert or stop their actions after a period of time.

> ##### Contents
> 
> * [How to configure Active Response](how-to-configure.md)
>   * [Configuring the Wazuh server](how-to-configure.md#configuring-the-wazuh-server)
>   * [Configuring the monitored endpoint](how-to-configure.md#configuring-the-monitored-endpoint)
> * [Default active response scripts](default-active-response-scripts.md)
>   * [Linux, macOS, and Unix-based endpoints](default-active-response-scripts.md#linux-macos-and-unix-based-endpoints)
>   * [Windows endpoints](default-active-response-scripts.md#windows-endpoints)
> * [Custom active response scripts](custom-active-response-scripts.md)
>   * [Programming an active response](custom-active-response-scripts.md#programming-an-active-response)
>   * [Python active response script sample](custom-active-response-scripts.md#python-active-response-script-sample)
> * [Use cases](ar-use-cases/index.md)
>   * [Blocking SSH brute-force attack with Active Response](ar-use-cases/blocking-ssh-brute-force.md)
>   * [Restarting the Wazuh agent with Active Response](ar-use-cases/restarting-wazuh-agent.md)
>   * [Disabling a Linux user account with Active Response](ar-use-cases/disabling-user-account.md)
> * [Additional information](additional-information.md)
>   * [White list](additional-information.md#white-list)
>   * [Increasing blocking time for repeated offenders](additional-information.md#increasing-blocking-time-for-repeated-offenders)
