# Source: https://docs.ox.security/get-started/onboarding-to-ox/prerequisites-and-access/on-prem-preparation-guide.md

# On-Prem Preparation Guide

The OX Platform Readiness Validator checks whether your on-premises server environment is ready for an OX Security deployment.

The tool verifies infrastructure compatibility, validates network settings, and confirms access to required external services. It also generates the configuration file used during installation and creates log files to help with troubleshooting.

On-prem (self-hosted) deployments run in environments that you manage, either in your own data centers or in your cloud accounts. Before installation, you receive a system requirements list. Use the validator to confirm that your environment meets these requirements.

The validator helps you:

* Confirm the environment early with your team and OX engineers
* Reduce time spent in live troubleshooting
* Prevent deployment delays
* Ensure the system is ready before installation or updates

> <mark style="color:purple;">IMPORTANT:</mark> To ensure everything is ready before the installation or update, you must run this tool before the on-prem setup process. **The script does not install or update the platform; it only verifies readiness**.

## System requirements

This section lists the hardware and software requirements required for validation and deployment.

**Software requirements**

<table><thead><tr><th width="337">Requirement</th><th>Value</th></tr></thead><tbody><tr><td>Validator Version</td><td>2.0.0</td></tr><tr><td>Required Privileges</td><td>Root (sudo) access</td></tr><tr><td>Supported OS</td><td>Ubuntu 22.04 LTS, Ubuntu 24.04 LTS</td></tr></tbody></table>

**Minimum hardware requirements**

<table><thead><tr><th width="142">Component</th><th width="196">Requirement</th><th>Purpose</th></tr></thead><tbody><tr><td>CPU Cores</td><td>32+</td><td>High-performance Kubernetes workload processing</td></tr><tr><td>Memory</td><td>64+ GB RAM</td><td>Container orchestration and application memory</td></tr><tr><td>Storage</td><td>512+ GB disk space</td><td>Container images, logs, and persistent data</td></tr><tr><td>Network</td><td>Static IP address</td><td>Stable cluster communication</td></tr></tbody></table>

**Software tools**

<table><thead><tr><th width="141">Tool / Item</th><th>Purpose</th></tr></thead><tbody><tr><td><code>curl</code></td><td>Downloading components and testing connectivity</td></tr><tr><td><code>netstat</code></td><td>Checking port availability</td></tr><tr><td><code>nslookup</code></td><td>Validating DNS resolution</td></tr><tr><td><code>ip</code></td><td>Verifying network interfaces</td></tr><tr><td><code>lsb_release</code></td><td>Detecting OS version</td></tr></tbody></table>

## Validation script

This section describes how the script manages access, data handling, and output to maintain a secure validation process.

**Script functionality**

* The script requires root (sudo) access to perform system-level validations.
* It performs read-only checks and does not modify the system state.
* All output files, including logs and configuration files, are saved locally on the server.
* No sensitive data is transmitted externally at any stage.

When you enter the command listed below, it downloads the script, creates an executable, and then runs the executable automatically using root privileges.

At various points you’ll need to enter the configuration parameters listed in the table.

**To run the validator command on the on-prem server:**

1. Make sure the server has:

* Internet access to reach the S3 location
* `curl` installed
* Permission to run commands with `sudo`

1. Enter the following command in the terminal of the on-prem server to download and start the validator script.

   curl -o script.sh <http://ox-infra-validator.s3-website-eu-west-1.amazonaws.com/> && chmod +x script.sh && sudo ./script.sh
2. During execution, the script prompts you to enter configuration parameters.

<table><thead><tr><th width="124" valign="top">Parameter</th><th width="124" valign="top">Prompt</th><th width="164" valign="top">Format / Options</th><th width="180" valign="top">Purpose</th><th valign="top">Validation / Default</th></tr></thead><tbody><tr><td valign="top">Host IP Address</td><td valign="top">"Host IP Address"</td><td valign="top"><code>xxx.xxx.xxx.xxx</code> (e.g., <code>192.168.1.100</code>)</td><td valign="top">Static IP address for accessing the OX Platform</td><td valign="top">Must be a valid IPv4 and exist on the system</td></tr><tr><td valign="top">Host Name</td><td valign="top">"Host Name"</td><td valign="top">Alphanumeric + hyphens (e.g., <code>ox-platform-server</code>)</td><td valign="top">System hostname for the OX Platform server</td><td valign="top">Must follow standard hostname conventions</td></tr><tr><td valign="top">Server FQDN</td><td valign="top">"Server FQDN (e.g., k8s-master.company.com)"</td><td valign="top"><code>hostname.domain.com</code> (e.g., <code>ox.company.com</code>)</td><td valign="top">Full domain name for accessing the platform</td><td valign="top">Must be a valid FQDN with at least one dot</td></tr><tr><td valign="top">Use Proxy</td><td valign="top">"Use proxy server? (y/n)"</td><td valign="top"><code>y/yes</code> or <code>n/no</code></td><td valign="top">Determine if a proxy is needed for internet access</td><td valign="top">Default: <code>n</code> (no proxy)</td></tr><tr><td valign="top">Proxy URL</td><td valign="top">"Proxy URL (<a href="http://proxy.example.com:8080">http://proxy.example.com:8080</a>)"</td><td valign="top"><code>http://hostname:port</code> or <code>https://hostname:port</code></td><td valign="top">Proxy server for outbound connections (if selected)</td><td valign="top">Valid URL format if proxy is used</td></tr></tbody></table>

## Validation phases

The validation process includes several phases, each validating different items.

### **1. System information display**

| Checks                                                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Shows current system specifications, including:</p><p>Operating System version</p><p>CPU core count</p><p>Total memory (GB)</p><p>Root disk space (GB)</p><p>Assessment timestamp</p> |

### **2. Prerequisite validation**

<table><thead><tr><th valign="top">Checks</th><th valign="top">Possible Issues</th></tr></thead><tbody><tr><td valign="top">Root/sudo privileges<br>Ubuntu OS detection<br>Required system commands availability</td><td valign="top"><p>Running without sudo/root access</p><p>Missing system tools</p><p>Unsupported operating system</p></td></tr></tbody></table>

### **3. System requirements validation**

| Checks                                 |
| -------------------------------------- |
| CPU cores ≥ 32                         |
| <p><br>Memory ≥ 64 GB</p>              |
| <p><br>Disk space ≥ 512 GB</p>         |
| <p><br>OS version (22.04 or 24.04)</p> |

### **4. Network configuration validation**

| Checks                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Host IP exists on system interfaces</p><p>Hostname validation</p><p>DNS resolution for FQDN</p><p>Reverse DNS lookup</p><p>Network CIDR conflict detection</p><p>Kubernetes network planning</p><p><strong>Network CIDRs Used:</strong></p><p><strong>Pod CIDR:</strong> <code>10.244.0.0/16</code> – Internal pod communication</p><p><strong>Service CIDR:</strong> <code>10.96.0.0/12</code> – Kubernetes service networking</p> |

### **5. Proxy configuration validation**

| Checks when a proxy is enabled                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Proxy URL format validation</p><p>HTTP connectivity through proxy</p><p>HTTPS connectivity through proxy</p><p>Ubuntu repository access via proxy</p> |

### **6. Package repository validation**

| Checks                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Ubuntu repository connectivity</p><p>APT package manager functionality</p><p>Security repository access</p><p>Package query capabilities</p> |

### **7. External URL accessibility validation**

| Checks                                                                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The validator verifies that the server can access all external services necessary for container images, package managers, Helm charts, and third-party integrations. |

#### **Container registries**

| Domain              | Purpose                |
| ------------------- | ---------------------- |
| `us-docker.pkg.dev` | OX Security containers |
| `hub.docker.com`    | Common containers      |

#### **Package registries**

| Domain               | Purpose             |
| -------------------- | ------------------- |
| `registry.npmjs.org` | JavaScript packages |
| `pypi.org`           | Python packages     |
| `repo1.maven.org`    | Java packages       |
| `rubygems.org`       | Ruby packages       |
| `api.nuget.org`      | C# packages         |
| `cdn.cocoapods.org`  | iOS packages        |
| `conan.io`           | C++ packages        |

#### **Helm Chart repositories**

| Domain               | Purpose        |
| -------------------- | -------------- |
| `github.io`          | Helm charts    |
| `charts.bitnami.com` | Bitnami charts |
| `rook.io`            | Storage charts |

#### **External services**

| Domain             | Purpose                   |
| ------------------ | ------------------------- |
| `auth0.com`        | Authentication services   |
| `cloud.google.com` | Google Cloud Platform     |
| `deps.dev`         | Dependency analysis       |
| `datadoghq.com`    | Logging and observability |

### **8. Platform readiness validation**

| Checks                                                                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Swap disabled (required for Kubernetes)</p><p>Port availability (80, 443, 8080, 9090)</p><p>Directory write permissions</p><p>OX Platform directory structure</p> |

#### Output files

| File                           | Purpose                                         |
| ------------------------------ | ----------------------------------------------- |
| `setup/config.toml`            | Validated config for installation               |
| `ox_readiness_<timestamp>.log` | Full validation log for support/troubleshooting |

#### Network planning

| CIDR            | Used For                   |
| --------------- | -------------------------- |
| `10.244.0.0/16` | Pod network                |
| `10.96.0.0/12`  | Kubernetes service network |

#### **Required open ports**

| Port | Purpose              |
| ---- | -------------------- |
| 80   | HTTP access          |
| 443  | HTTPS access         |
| 8080 | Management interface |
| 9090 | Monitoring service   |

## Result indicators

<table><thead><tr><th width="125">Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>✅</td><td>All checks passed</td></tr><tr><td>⚠️</td><td>Warnings (non-blocking issues)</td></tr><tr><td>❌</td><td>Errors that must be fixed</td></tr></tbody></table>

## Common warnings, errors and recommended actions

The table lists some common warnings, errors and recommended actions.

<table><thead><tr><th valign="top">Warning / Error</th><th valign="top">Meaning</th><th valign="top">Action required</th></tr></thead><tbody><tr><td valign="top">⚠️Hostname mismatch</td><td valign="top">Input doesn’t match system hostname</td><td valign="top">Will be corrected during install</td></tr><tr><td valign="top">⚠️ Reverse DNS missing</td><td valign="top">No PTR record for IP</td><td valign="top">Add reverse DNS (optional)</td></tr><tr><td valign="top">⚠️ Port in use</td><td valign="top">Port needed by OX is occupied</td><td valign="top">Stop the conflicting service</td></tr><tr><td valign="top">⚠️ Swap enabled</td><td valign="top">Swap memory is active</td><td valign="top">Disable swap before install</td></tr><tr><td valign="top">⚠️ Partial internet access</td><td valign="top">Some repos unreachable</td><td valign="top">Check firewall/proxy settings</td></tr><tr><td valign="top">❌ CPU cores insufficient</td><td valign="top">Less than 32 cores</td><td valign="top">Upgrade server hardware</td></tr><tr><td valign="top">❌ Memory insufficient</td><td valign="top">Less than 64 GB RAM</td><td valign="top">Add RAM</td></tr><tr><td valign="top">❌ Disk space too small</td><td valign="top">Less than 512 GB</td><td valign="top">Resize or expand disk</td></tr><tr><td valign="top">❌ FQDN not resolving</td><td valign="top">DNS issue</td><td valign="top">Create or correct DNS record</td></tr><tr><td valign="top">❌ Repository access failed</td><td valign="top">Proxy/firewall blocking</td><td valign="top">Adjust proxy/firewall settings</td></tr><tr><td valign="top">❌ Required port unavailable</td><td valign="top">In use by another service</td><td valign="top">Free the port</td></tr></tbody></table>

## Troubleshooting

If you experience issues during validation:

1. Review the log file for detailed information on any failed checks or errors.
2. Verify that your system meets all listed requirements.
3. If the issue persists, contact OX Security support and include the log file for assistance.

The table lists some possible issues.

<table><thead><tr><th width="175">Issue</th><th>Purpose</th><th>Command(s)</th></tr></thead><tbody><tr><td>Script Won’t Download</td><td>Check internet connectivity. Download the validator script.</td><td>ping google.com wget http://ox-infra-validator.s3-website-eu-west-1.amazonaws.com/ -O script.sh</td></tr><tr><td>Permission Denied</td><td>Run the script with root privileges. Add execute permission to the script.</td><td><code>sudo ./script.sh</code> <code>chmod +x script.sh</code></td></tr><tr><td>DNS Failures</td><td>Check the DNS configuration Test DNS resolution.</td><td><code>cat /etc/resolv.conf</code> <code>nslookup your-fqdn.com</code></td></tr><tr><td>Proxy Testing</td><td>Verify proxy connectivity.</td><td><code>curl -x http://proxy:port http://google.com</code></td></tr><tr><td>APT Repository Issues</td><td>Refresh package lists. Review repository configuration Test repository reachability</td><td><code>sudo apt update</code> <code>cat /etc/apt/sources.list</code> <code>curl -I http://archive.ubuntu.com/ubuntu/</code></td></tr></tbody></table>

## After validation

Once the validator completes:

1. Open the generated `setup/config.toml` file to review the validated system and network configuration.
2. Save the log file (`ox_readiness_<timestamp>.log`) for future reference or troubleshooting if needed.
3. Once the validation is complete, contact your OX Security support to assist with the installation and deployment.
