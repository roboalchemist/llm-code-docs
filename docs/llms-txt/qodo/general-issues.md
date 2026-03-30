# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/troubleshooting/general-issues.md

# General Issues

### Chat Response Issues

If you encounter unexpected or missing responses in Qodo IDE Plugin chat, we recommend attaching the **Request ID** when reporting the issue.

You can copy the Request ID from the chat message in two ways:

* **From the message menu**: Click the 3 dots (…) on the message → **Copy Request ID**
* **From the context menu**: Right-click on the message → **Copy Request ID**

Include the Request ID when opening a support ticket so we can quickly investigate.

***

### Extracting Logs for General Troubleshooting

When facing login problems, unusual behaviors, or other issues, please include IDE logs in your support ticket.

#### VSCode

1. Open the **Output** window in the bottom panel.
2. In the dropdown, select **Qodo**.
3. Click the **3 dots menu** in the top-right corner.
4. Select **Save Output As…** and save the file.
5. Attach the file to your ticket.

**JetBrains (IntelliJ, PyCharm, etc.)**

1. In the IDE menu, go to **Help** → **Show Log in Finder / Explorer** (depending on your OS).&#x20;
2. This opens the log directory (e.g. `idea.log`, `idea.log.1` etc.).
3. Copy the relevant log files (or multiple recent ones) and attach them (or zip them) to your support ticket.&#x20;

If you don’t see the “Show Log” option (or your IDE version omits it), you can manually find the log directory:

* **Windows**: `%LOCALAPPDATA%\JetBrains\<IDE-Name><version>\log`
* **macOS**: `~/Library/Logs/JetBrains/<IDE-Name><version>`
* **Linux**: `~/.cache/JetBrains/<IDE-Name><version>/log`&#x20;
