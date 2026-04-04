# Source: https://docs.agent.ai/actions/send_message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Message

## Overview

Send messages to specified recipients, such as emails with formatted content or notifications. All messages are sent from [agent@agentaimail.com](mailto:agent@agentaimail.com).

### Use Cases

* **Customer Communication**: Notify users about updates or confirmations.
* **Team Collaboration**: Share workflow results via email.

<iframe width="560" height="315" src="https://www.youtube.com/embed/dimzBWcPcX0?si=lNJ0mWxvj-9YDR-F" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Configuration Fields

### Message Type

* **Description**: Select the type of message to send.
* **Options**: Email
* **Required**: Yes

### Send To

* **Description**: Enter the recipient's address.
* **Example**: "[john.doe@example.com](mailto:john.doe@example.com)."
* **Required**: Yes

### Email Subject

* **Description:** The subject line of the email to be sent
* **Example:** "Agent results for Agent X"
* **Required:** yes

### Output Formatted

* **Description**: Provide the message content, formatted as needed.
* **Example**: "Hello, your order is confirmed!" or formatted HTML for emails.
* **Required**: Yes
