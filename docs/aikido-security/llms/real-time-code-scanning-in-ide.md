# Source: https://help.aikido.dev/ide-plugins/features/real-time-code-scanning-in-ide.md

# Real-Time Code Scanning in IDE

The Aikido IDE plugin helps you catch security issues the moment they’re introduced. Every time you open or save a file, Aikido runs a quick scan in the background and highlights problems directly in your editor.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FhgPAZVyETjcy2iGugwBo%2Fsecret_flag.gif?alt=media&#x26;token=0608b3fc-b651-4743-81cc-b3e9571c4354" alt=""><figcaption></figcaption></figure>

#### What It Scans

Aikido performs two types of scans in real time:

* SAST (Static Application Security Testing): Detects insecure coding patterns, potential injections, unsafe deserialization, and other code-level vulnerabilities.
* Secrets: Finds exposed credentials such as API keys, passwords, or tokens.
* IAC: (Infrastructure as Code): Detects cloud and infrastructure misconfigurations in Terraform, CloudFormation, Dockerfiles, and similar files.

#### How It Works

When you open or save a file, Aikido scans the code using the same analysis engine as the Aikido platform.

Detected issues appear:

* Inline, underlined or highlighted in the editor.
* In the Aikido sidebar, grouped by severity and category.
* In the Problems panel, for quick navigation.

Hover over any finding to see context and remediation details. For supported findings, you can [analyse using AI Autotriage or apply an AI AutoFix](https://help.aikido.dev/ide-plugins/features/aikido-ai-in-ide) to safely patch the issue without leaving your IDE.
