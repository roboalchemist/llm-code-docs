# Source: https://docs.kubearmor.io/kubearmor/use-cases/modelarmor.md

# ModelArmor Overview

**ModelArmor** is a Zero Trust security solution purpose-built to protect AI/ML/LLM workloads from runtime threats. It safeguards against the unique risks of agentic AI systems and untrusted models by sandboxing deployments and enforcing granular runtime policies.

**ModelArmor** uses KubeArmor as a sandboxing engine to ensure that the untrusted models execution is constrained and within required checks. AI/ML Models are essentially processes and allowing untrusted models to execute in AI environments have significant risks such as possibility of cryptomining attacks leveraging GPUs, remote command injections, etc. KubeArmor's preemptive mitigation mechanism provides a suitable framework for constraining the execution environment of models.

ModelArmor can be used to enforce security policies on the model execution environment.

## Why ModelArmor?

ModelArmor enables secure deployment of **agentic AI applications** and **ML models**, addressing critical security gaps that traditional guardrails and static scanning cannot solve.

It is designed for:

* **Agentic AI workloads** using autonomous, tool-using agents.
* **ML pipelines** importing untrusted models from public repositories.
* Environments where **guardrails alone are not sufficient**.

ModelArmor protects the **entire AI lifecycle**, from development to deployment, using **sandboxing** and **policy enforcement** to neutralize malicious behavior at runtime.

## The Problem: Security Risks in Agentic AI

### 1. Arbitrary Code Execution

Agentic AI systems can **execute arbitrary system commands** due to their autonomy and access to tools.

* Prompt engineering can bypass LLM guardrails.
* Attackers can instruct agents to run harmful commands, download malware, or scan networks.

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-2918d2f3a9ab16a318f695b8640842e85634fee7%2Fdemo1.png?alt=media)

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-1f6a5a0a71a5f238d914a6a1d868ce2a5d80b8cc%2Fdemo2.png?alt=media)

### 2. Model Supply Chain Attacks

Malicious models uploaded to public repositories (e.g., Hugging Face) can contain embedded payloads.

* Loading such models allows **hidden code execution**, leading to system compromise and C\&C communication.

![Code Execution Cannot Be Governed Traditionally](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-4875f47d7ff4640683ce05065e94a2983cb78405%2Frisk1.png?alt=media)

### 3. Prompt Injection Attacks

Crafted prompts can manipulate the agent into performing unauthorized actions:

* Reading sensitive files (e.g., `/root/.aws/credentials`).
* Installing tools (`apk add nmap`) or scanning networks.
* Fetching and executing external scripts.

> Traditional container security cannot detect these because they exploit application behavior, not the container itself.

![Guardrails are not enough against sophisticated prompt engineering](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-034373818b9ccfd4423162acda106467290fd5c4%2Frisk2.png?alt=media)

## The Solution

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-1f68ab6f3df6e4d26e150db2e56a608f592255fc%2Fissuesfixed.png?alt=media)

### Sandboxing Agentic AI

ModelArmor **isolates agentic AI apps** and ML workloads at runtime, blocking unauthorized actions even if guardrails or code reviews are bypassed.

![Zero Trust Policy Enforcement](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-b8833b2d46705a54f0c36b824cb38113536d0b16%2Fuse3.png?alt=media)

### Zero Trust Policy Enforcement

Define **fine-grained security policies** to:

* **Restrict file system access** (e.g., block `/root/.aws/credentials`).
* **Control process execution** (allow only trusted binaries).
* **Limit network activity** (disable raw sockets, ICMP, or outbound traffic).

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-1f469b3c22871ae12996945af9d8634a9f5994d6%2Fuse4.png?alt=media)

### Automated Red Teaming

Simulate adversarial scenarios like malicious model imports and prompt injections to **identify vulnerabilities pre-deployment**.

### Protection Across the Stack

ModelArmor works across frameworks and environments:

* Supports any **language runtime** or **AI framework**.
* Requires no code changes to your application.
* Lightweight and **cost-efficient**, avoiding the overhead of MicroVMs or full isolation environments.

![Granular Policy Enforcement for Process, Network, Volumes and AI flows](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-1e4a0b98fbb97e6a7759c0a33bc5d0e7581d3822%2Fuse5.png?alt=media)

## TensorFlow Based Use Cases

### FGSM Adversarial Input Attack

An FGSM attack manipulates input data by adding imperceptible noise, creating adversarial examples that force the TensorFlow model to misclassify (e.g., predicting “5” for an image of “2”).

Traditional container security fails here because the model and container remain unchanged; the attack happens through crafted input.

**ModelArmor Protection:**

* Proactively simulates adversarial attacks using *Automated Red Teaming*.
* Secures model behavior with input validation and anomaly detection, akin to an *LLM Prompt Firewall* for ML workloads.
* Protects against sophisticated input-level manipulations.

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-af2209794482426decc0463693063aa4be821190%2Fuse2.png?alt=media)

[▶️ Watch FGSM Attack Video](https://drive.google.com/file/d/1EnmsIiR4G4bYmoxBIHTk1bDkW2XatM4N/preview)

### Keras Model Injection Attack

A deployed TensorFlow model in a Docker container is vulnerable to compromise via a malicious Keras Lambda layer. This attack involves:

* Installing Python inside the container or
* Copying malicious scripts (e.g., into `/tmp`) to execute unauthorized system commands.

**ModelArmor Protection:**

* Blocks unauthorized installations (e.g., Python) and filesystem modifications (e.g., writing to `/tmp`).
* Uses *Automated Red Teaming* to detect such vulnerabilities pre-deployment.
* Isolates workloads (like TensorFlow) with *Sandboxing Agentic AI* to prevent code injection.

![Keras Model Injection Attack Mitigation](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-87d573fb1b240cc7155b1fac75bb4098f9c40636%2Fuse1.png?alt=media)

[▶️ Watch Keras Inject Video](https://drive.google.com/file/d/1olGBz3WUoJqmcAVdRY7uImKTHggRX6nK/preview)

***

## Securing NVIDIA NIM

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-d47e50ae66250fc5ba635359b53f1281a8fc6363%2Fnvidia1.png?alt=media)

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-9d8b0ace26182b93b0712df9ae1160b481ef9b5a%2Fnvidia2.png?alt=media)

📄 [View PDF: Securing\_NVIDIA\_NIM.pdf](https://drive.google.com/file/d/16DjsSyOAWr1S4EwSTBSx63SLDHPFnSAh/preview)
