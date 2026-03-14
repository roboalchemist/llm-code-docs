# Source: https://docs.ox.security/scan-and-analyze-with-ox/analyzing-scan-results/ai-severity-simulator.md

# AI Severity Simulator

The OX AI Severity simulator reviews Open Source Security issues and proposes a severity level that reflects the actual risk inside your environment. The simulator checks CVEs and determines if they are reachable and exploitable. The results help you focus on the issues that matter most.

## What the simulator does

The simulator reviews the CVE severity of each Open Source Security issue and performs these actions:

* Checks impact and asset importance
* Evaluates exploitability of CVEs
* Adds CVE evidence and code snippets when they are exploitable

The results form part of active issues and are flagged with a red or green robot.

* <mark style="color:red;">Red</mark> robot: The CVE is exploitable.
* <mark style="color:green;">Green</mark> robot: The CVE is not exploitable.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7d05ab773813d8f47fcffe9e8631e1e71462c71a%2Fai%20simulator%20red%20and%20green%20robot%20icons.png?alt=media" alt=""><figcaption></figcaption></figure>

## View AI simulator issues

1. Open the **Active Issues** page.
2. Enter ‘AI Simulated’ in the **Severity Factor** filter search.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-97b2334cb19489e12eb8b02a8f0b6f830ca2caa9%2Fai%20simulator%20query%20filter%20(1).png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
3. Select an issue, click the **Vulnerabilities** tab, and hover over the robot icon to view evidence and related code snippets.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-af16a52317480d7b9925483aaa9cb9560c0b4b18%2Fai%20simulator%20vulnerabilities%20tab%20with%20red%20robot%20hover.png?alt=media" alt=""><figcaption></figcaption></figure>
4. To view changes in severity and get details of exploitable packages, click the **Summary** tab.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-fd8fe7773ebb087a676672fb6f1027f225df0f2f%2Fai%20simulator%20summary%20tab.png?alt=media" alt=""><figcaption></figcaption></figure>
