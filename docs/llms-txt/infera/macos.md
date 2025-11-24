# Source: https://docs.infera.org/node/macos.md

# Mac OS

> Installing the Infera Node CLI program on Mac OS.

### Prerequisites

You **MUST** have a **GPU** to run an **Infera Node**.

<Warning>Minimum requirements for the node are 16GB RAM and 8GB VRAM. A node will run with less RAM, but will get significantly less or no jobs.</Warning>

### Installation

<Steps>
  <Step title="Install and Run Ollama">
    [Ollama](https://ollama.com/) is required to run an **Infera Node**.

    You can download it from [Ollama's official website](https://ollama.com/download).
  </Step>

  <Step title="Install the Infera Lite browser extension">
    1.  Open the Chrome Browser (if you do not have Chrome installed, download it [here](https://www.google.com/intl/en_ca/chrome/))
    2.  Go to the [Infera Lite](https://chromewebstore.google.com/detail/infera-lite/ffoccnmddajjohmmkccnkobelobgcdmp) extension on the Chrome Web Store.
    3.  Click **"Add to your Chrome"** to install the extension in your browser.
  </Step>

  <Step title="Open your terminal">
    Open the **Terminal** application on your Linux system. You can usually find it in your applications menu or by pressing `Ctrl + Alt + T`.
  </Step>

  <Step title="Download the installation script">
    Copy paste the following commands in your command line and press enter to install your Infera node. The first command removes previous installations of infera if they are present.

    **For M series chip**

    ```bash
    curl -sSL http://downloads.infera.org/infera-apple-m.sh | bash
    echo "alias init-infera='~/infera'" >> ~/.zshrc && source ~/.zshrc
    ```
  </Step>

  <Step title="Running an Infera Node">
    After installing, run the following command to start your node:

    ```bash
    init-infera
    ```
  </Step>

  <Step title="Verify that your Infera Node is running">
    If your node is running correctly, your terminal will display a message like this:

    <img width="100%" src="https://mintlify.s3.us-west-1.amazonaws.com/infera-a106b685/images/node/node-running.png" />
  </Step>

  <Step title="Connect to your node">
    Click on the Infera Lite extension in Chrome while your node is running to monitor your node.

    If your node is running, the extension should automatically detect your node.

    Go to the [Infera Lite Guide](/node/infera-lite) to learn more about how you can use the extension to monitor your node.
  </Step>

  <Step title="Link the Node">
    If this is your first time, you may see a message saying

    ```
    ERROR: node verification failed
    ```

    This is because you must link your node to your **Infera Account**. Linking your node to your account is neccessary to withdraw tokens earned from completing jobs on the network.

    To link your node, follow the [Link Node to Account](https://medium.com/@alex_85908/how-to-link-a-node-to-your-infera-account-d2f746e52fa2). This must be done once for every node you run.

    **If you have already linked your node**, it should just start up and you will see messages in terminal counting uptime. That means your node is running!

    **If your node gets a job**, you will see a message saying Starting job in terminal.
  </Step>
</Steps>

***

### Updating Infera

To update the Infera Node on your computer, enter the following command into your Terminal to remove and replace the depricated version of Infera.

**Apple M series**

```bash
rm -rf ~/infera
curl -sSL http://downloads.infera.org/infera-apple-m.sh | bash
```

<Note>If you are experiencing trouble updating your Node, it may help to reboot your PC after running the `rm -rf ~/infera` command</Note>

***

### Uninstalling Infera

To delete infera from your computer, enter the following command into your Terminal.

```bash
rm -rf ~/infera
```

***

### Troubleshooting

*   If the installation script fails, ensure your internet connection is active.
*   Make sure you have the latest version of Ollama running before starting the Infera node.
*   Make sure your computer has a **GPU**
*   If having issues with updating Infera, try rebooting your PC after running `rm -rf ~/infera` command

If you have any questions or encounter any issues, join our [Discord Community](https://discord.com/invite/infera) for assistance.
