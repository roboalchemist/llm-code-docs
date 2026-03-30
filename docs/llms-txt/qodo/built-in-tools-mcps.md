# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/tools-mcps/built-in-tools-mcps.md

# Built-in Tools (MCPs)

In order to understand your code better and help you perform various actions, Qodo uses multiple services and [Agentic Tools ](https://docs.qodo.ai/qodo-documentation/qodo-gen/tools-mcps/agentic-tools-mcps)behind the scenes.

When using these tools, Qodo will let you know which tools are being used, and ask whether you **approve or deny** their usage.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FttIQHIonHrUGZxDmIadL%2FScreenshot%202025-05-21%20at%2014.51.14.png?alt=media&#x26;token=4767cddf-03db-44d7-98c7-43f752e9735f" alt="" width="375"><figcaption></figcaption></figure>

The current internal tools Qodo uses are:

### **Git Service**

Provides Git repository insights.

**Sub-tools:**

* `git_remote_url`: Gets the remote repository URL.
* `git_branches`: Lists all branches.
* `git_changes`: Shows uncommitted changes.
* `git_file_history`: Displays commit history for a file.

### **Code Navigation Service**

Analyzes and tracks code structure.

**Sub-tools:**

* `get_code_dependencies`: Finds dependencies for a function or class.
* `find_code_usages`: Identifies where a function, class, or variable is used.

### **File System Service**

Manages files and directories.

**Sub-tools:**

* `read_files`: Read and return the full contents of a text file.
* `write_to_file`: Write content to a file. Creates the file if it doesn’t exist and ensures parent directories are also created.\
  Switching this sub-tool off allows you to approve file changes one by one, or deny them.
* `replace_in_file`: Modify a file using a structured multi-block diff string.
* `directory_traversal`: Generate a recursive tree view of a directory.
* `search_files`: Search for a regex or string pattern across file contents within a directory.
* `get_file_info`: Retrieve metadata about a file or directory, including type, size, timestamps, and permissions.

### **Terminal**

Use terminal command line tools.

**Sub-tools:**

* `terminal_execute_command`: Runs a shell command, and returns its output.
* `terminal_get_latest_output`: Gets the latest output from a terminal. Response includes content with terminal output text.
* `terminal_terminate_command`: Terminates a running command. Response includes content with result message and isError flag indicating success or failure.

{% hint style="info" %}
**Note:** Due to a new Beta terminal introduced to JetBrains IDEs, some JetBrains IDE users might not be able to use the terminal tool initially.

In order to enable the terminal tool, click the three dots **...** icon on the bottom right above the in-IDE terminal, choose **Terminal Engine** from the dropdown list, then select **Classic Terminal**.

<img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FZthxpXwqYFyEaoHjAZpl%2FScreenshot%202025-06-19%20at%2016.47.20.png?alt=media&#x26;token=f3fe29e3-4755-427a-96a0-ed5333153358" alt="" data-size="original">
{% endhint %}

#### Terminal Commands allow list

In Qodo's [Chat Preferences](https://docs.qodo.ai/qodo-documentation/qodo-gen/chat/chat-preferences), you can set a terminal commands allow list:

1. **Allowed commands**: Set terminal commands that will be automatically executed by the agent, no approval needed. Other terminal commands will require approval.
2. **Blocked commands:** Set terminal commands that will be automatically blocked by the agent.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2F8Ub53l8NEpTrFbdBzwlY%2FScreenshot%202025-07-22%20at%2011.52.11.png?alt=media&#x26;token=4a885ab6-1a30-4aec-87a4-9dff5aedd081" alt="" width="344"><figcaption></figcaption></figure>

### **Web Search**

Preforms web search.

Toggle by clicking the web search button.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FPx6EimQRvpWD3Ugay7b6%2FScreenshot%202025-08-04%20at%2014.28.56.png?alt=media&#x26;token=07c65972-0dec-48dc-9568-ed01c13b597d" alt=""><figcaption></figcaption></figure>
