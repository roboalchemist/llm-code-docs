# Source: https://docs.infera.org/node/managing-node.md

# Managing Your Node

## How to use the Infera Lite Extension

Before opening the extension, make sure your node is running on your device

*   On Windows: run the `infera-node.exe` file
*   On Mac/Linux: run `init-infera` in your Terminal.

### Main Dashboard

The **Home screen** is the landing page of the extension and gives an overview of the node's current status.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infera-a106b685/images/node/extension/main-page.png" />

*   **Start/Stop Button:** Allows you to toggle the node on or off.
*   **Active Status:** Indicates whether the node is running, displaying either “Active” (active and awaiting jobs) or “Inactive” (node deactivated).
*   **Points:** Displays the points earned from processed tasks and uptime on the network.
*   **Uptime:** Shows the node's total uptime.

### Reputation & Node Details

This section provides a real-time snapshot of your node's performance:

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infera-a106b685/images/node/extension/stats-page.png" />

*   **Device details:** Displays information about the node's GPU, CPU, RAM, VRAM, and available RAM.
*   **Tasks Completed:** Shows the number of inference tasks your node has processed.
*   **Reputation:** A pie chart representing your node's reputation on the Infera network based on speed and reliability.

### Installing New Models

This page lists all the LLM models that users can install to support the Infera network, starting with every state-of-the-art open-source model.

Click on the download icon next to a model's name in order to download the model onto your **Infera Node**.

<img width="50%" style={{borderRadius: '10px'}} src="https://mintlify.s3.us-west-1.amazonaws.com/infera-a106b685/images/node/extension/install-model.webp" />

## Node Management via CLI

If you fancy managing your node via a terminal interface, you can follow this [guide](https://medium.com/@alex_85908/node-management-in-cli-be725a90d1c8).
