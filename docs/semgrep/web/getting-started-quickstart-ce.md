# Get started with Semgrep Community Edition

Source: https://semgrep.dev/docs/getting-started/quickstart-ce

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Semgrep Community Edition- Get started**On this page- [quickstart](/docs/tags/quickstart)- [Semgrep CE](/docs/tags/semgrep-ce)Get started with Semgrep Community Edition
Semgrep Community Edition (CE) is an open source static analysis tool that can find insecure coding patterns and security vulnerabilities in source code. Semgrep CE encompasses a SAST scanning engine, community rules, and integrated development environment plugins.

infoSemgrep CE is the open source version of Semgrep Code, a commercial offering recommended for enterprise use cases. Both products share a common command-line interface, but Semgrep Code adds additional capabilities, including a web user interface.

## Prerequisites[​](#prerequisites)
See [Prerequisites](/docs/prerequisites) to ensure your machine meets Semgrep&#x27;s requirements.

## Install Semgrep CE[​](#install-semgrep-ce)
- macOS- Linux- Windows (beta)
- Install the Semgrep CLI and confirm the installation:
`# install through homebrewbrew install semgrep# install through pippython3 -m pip install semgrep# confirm installation succeeded by printing the currently installed versionsemgrep --version`**Homebrew users:** ensure that you&#x27;ve [added Homebrew to your PATH](https://docs.brew.sh/FAQ#my-mac-apps-dont-find-homebrew-utilities).

- Install the Semgrep CLI and confirm the installation:
`# install through pippython3 -m pip install semgrep# if you get the following error &quot;error: externally-managed-environment&quot;,# see semgrep.dev/docs/kb/semgrep-appsec-platform/error-externally-managed-environment # confirm installation succeeded by printing the currently installed versionsemgrep --version`
- 
[Download](https://www.python.org/downloads/) and install Python. Check the box to add python.exe to the PATH; otherwise, you will have difficulty running Pip and Semgrep.

- 
Configure your system to run Python with UTF-8 text encodings by default. In PowerShell, run:

`[System.Environment]::SetEnvironmentVariable(&#x27;PYTHONUTF8&#x27;, &#x27;1&#x27;, &#x27;User&#x27;)`
- Install the Semgrep CLI and confirm the installation. In PowerShell, run:
```
# install through pippip install –upgrade semgrep# if you get the following error &quot;error: externally-managed-environment&quot;,# see semgrep.dev/docs/kb/semgrep-appsec-platform/error-externally-managed-environment # confirm installation succeeded by printing the currently installed versionsemgrep --version
```
## Create a test file for use with Semgrep CE[​](#create-a-test-file-for-use-with-semgrep-ce)
Navigate to the directory of your choice, and create a sample file called `app.py` with the following:

`# app.pyimport osuser_input = input(&quot;Enter a Directory: &quot;)os.system(&quot;ls &quot; + user_input)`
Given this file, you might expect someone to run it as follows:

`$ python3 app.pyEnter a Directory: .app.py`
However, because this file didn&#x27;t follow secure coding principles, a malicious actor might take advantage of the file as follows:

`$ python3 app.pyEnter a Directory: .; cat ~/.ssh/id_*app.py-----BEGIN OPENSSH PRIVATE KEY-----...`
## Scan `app.py` with Semgrep CE[​](#scan-apppy-with-semgrep-ce)
To check your code for security vulnerabilities:

- Navigate to the directory where you saved `app.py` using the terminal.
- Invoke Semgrep CE using `semgrep scan`. The `semgrep scan` command pulls down rules from the [Semgrep Registry](https://semgrep.dev/r), similar to package managers for source code libraries, and stores rules that help define semantic meaning to patterns in source code. By default, Semgrep CE uses open source community rules:

`┌─────────────┐│ Scan Status │└─────────────┘  Scanning 1 file tracked by git with 1062 Code rules:  Language      Rules   Files          Origin      Rules ─────────────────────────────        ───────────────────  python          243       1          Community    1062  &lt;multilang&gt;      48       1`
The specific numbers shown in your Scan Status printed to the terminal may vary, but you can still see that Semgrep is scanning the source code using community rules. There are over 1000 community rules in the default rule set, but because Semgrep recognizes the source code language, only rules relevant to the code being scanned are evaluated.

To fine-tune your scan, you can include the `--config` parameter, which allows you to choose which rules to run:

`semgrep scan --config &quot;p/python-command-injection&quot; app.py`
In the preceding example, the command uses a predefined rule set from the Semgrep Registry focused on command injection vulnerabilities in Python. The specific rules you use during a scan will significantly impact what is detected in your source code.

## View and understand Semgrep Scan output[​](#view-and-understand-semgrep-scan-output)
Semgrep displays your results when the scan is completed.

The Scan Summary printed to the terminal tells you how many rules were run and whether or not there were any findings. A finding indicates that Semgrep detected a potential vulnerability.

`┌──────────────┐│ Scan Summary │└──────────────┘✅ Scan completed successfully. • Findings: 1 (1 blocking) • Rules run: 24 • Targets scanned: 1 • Parsed lines: ~100.0% • No ignore information availableRan 24 rules on 1 file: 1 finding.`
The findings list includes the name of the rule, a brief explanation of the security issue, and the exact line of code that triggered the finding:

`┌────────────────┐│ 1 Code Finding │└────────────────┘    app.py   ❯❯❱ python.lang.security.audit.dangerous-system-call-audit.dangerous-system-call-audit          Found dynamic content used in a system call. This is dangerous if external data can reach this          function call because it allows a malicious actor to execute commands. Use the &#x27;subprocess&#x27; module instead, which is easier to use without accidentally exposing a command injection vulnerability. Details: https://sg.run/2WL0 5┆ os.system(&quot;ls &quot; + user_input)`
Each rule is given a unique namespace to help identify it. For example, Python language issues are prefixed with `python.lang`.

The rule&#x27;s author defines the source code patterns and provides remediation advice or an explanation of the problem. In this example, you can also see the specific expression and line of code where the issue appears.

This example is a [Command Injection](/docs/learn/vulnerabilities/command-injection) vulnerability. The rule advises you to review the [Python Code Injection Cheat Sheet](/docs/cheat-sheets/python-code-injection) to learn more. The link in the output takes you to the **Semgrep Playground**, where you can interactively modify this rule and test it against sample code.

## Next steps[​](#next-steps)
Read Semgrep docs for details on how to:

- [Set up CI/CD pipelines](/docs/deployment/oss-deployment)
- [Install the IDE](/docs/extensions/overview)
- [Write custom rules](/docs/writing-rules/overview)
- [Access learning guides](/docs/learn)
Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [quickstart](/docs/tags/quickstart)- [Semgrep CE](/docs/tags/semgrep-ce)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/getting-started/quickstart-ce.md)Last updated on **Nov 17, 2025**