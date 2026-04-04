# Source: https://plivo.com/docs/aiagent/aistudio/nodereference/sendmessage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Message

> Send messages across call, WhatsApp, chat, and SMS channels

The **Send Message Node** allows you to send messages across various communication channels, including **Call**, **WhatsApp**, **Chat**, and **SMS**. The format of the message and media varies depending on the selected channel. You can send both static and dynamic content in the message, including the use of agent variables.

#### Configuration

1. **Source Number**: The number from which the message is sent. This can be set as an **agent variable** to dynamically pull data from earlier in the workflow.
2. **Destination Number**: The recipient's number or identifier. Like the source number, it can also be set as an **agent variable**.
3. **Message Type**: The type of message that will be sent is dependent on the selected channel:
   * **Static Message**: A fixed message that doesn’t change.
   * **Template Message**: A pre-approved template with placeholders for dynamic variables (e.g., customer names, order details, etc.). Template messages are commonly used in channels like WhatsApp.

This node gives you full flexibility to deliver personalized messages across different channels, tailoring the content with dynamic variables as needed.
