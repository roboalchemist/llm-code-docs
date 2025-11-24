# Source: https://docs.infera.org/node/windows.md

# Windows

> Installing the Infera Node CLI program on Windows.

## Prerequisites

You **MUST** have a **GPU** to run an **Infera Node**.

<Warning>Minimum requirements for the node are 16GB RAM and 8GB VRAM. A node will run with less RAM, but will get significantly less or no jobs.</Warning>

### Installation

<Steps>
  <Step title="Download and Run Ollama for Windows">
    Download [Ollawa for Windows](https://ollama.com/download) and install it. Then run Ollama and it should appear in your system tray. Make sure it is there and running. The Infera node **will not boot up** without Ollama running.

    <img width="100%" src="https://mintlify.s3.us-west-1.amazonaws.com/infera-a106b685/images/node/ollama-windows.webp" />
  </Step>

  <Step title="Download the required executables">
    Download the Infera [install-scripts](https://github.com/inferanetwork/install-scripts) github repository.

    You can do this by navigating to the repository and then pressing `Code` button in the top right corner and selecting `Download ZIP`.

    <img width="100%" src="https://mintlify.s3.us-west-1.amazonaws.com/infera-a106b685/images/node/windows-download.webp" />
  </Step>

  <Step title="Install the Infera Lite browser extension">
    1.  Open the Chrome Browser (if you do not have Chrome installed, download it [here](https://www.google.com/intl/en_ca/chrome/))
    2.  Go to the [Infera Lite](https://chromewebstore.google.com/detail/infera-lite/ffoccnmddajjohmmkccnkobelobgcdmp) extension on the Chrome Web Store.
    3.  Click **"Add to your Chrome"** to install the extension in your browser.
  </Step>

  <Step title="Extract the files out of the ZIP">
    Extract the folder out of the downloaded ZIP, which was downloaded in **Step 1**.
  </Step>

  <Step title="Move executable to Desktop">
    Drag and drop the `infera-node.exe` file to your Desktop for easy access.
  </Step>

  <Step title="Run the Infera Node">
    1.  On your desktop, double-click the `infera-node.exe` icon.
    2.  The Infera node will now boot up.

    <Warning>If Ollama is not running, you will receive an error and the node will not start.</Warning>
  </Step>

  <Step title="Connect to your node">
    Once your node is running, click on the Infera Lite extension in Chrome while your node is running to monitor your node.

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

### Troubleshooting

*   If the installation script fails, ensure your internet connection is active.
*   Make sure you have the latest version of Ollama running before starting the Infera node.
*   If you see this in your terminal ![terminal](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EMkDt5nCEBCMIC62NQoXFQ.jpeg)
    It is NOT an error or an issue at all. This is your chrome extension prompting server for data like points, uptime and other data. Nothing needs to be done about it.
*   If it's stuck on “Uvicorn running” try to close the exe and run it again. Sometimes it helps running the exe as an Administrator but should be fine just relaunching the app.
*   Windows firewall might also pop up, allow running infera-windows.exe in the pop-up or add it to exceptions of your anti-virus software.
*   Make sure your extension has ACTIVE status on the first page. If it doesn't, try pressing the huge Infera logo on the same page
    <img width="50%" src="https://mintlify.s3.us-west-1.amazonaws.com/infera-a106b685/images/node/windows-active.webp" />

### Need Help?

If you have any questions or encounter any issues, join our [Discord Community](https://discord.com/invite/infera) for assistance.
