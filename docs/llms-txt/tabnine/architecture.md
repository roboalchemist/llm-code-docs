# Source: https://docs.tabnine.com/main/welcome/readme/architecture.md

# Architecture

Tabnine provides a secure, reliable, and resilient platform that's been designed from the ground up based on industry best practices.

Tabnine installs on a Kubernetes cluster on-premises or supported cloud providers.

## High-level architecture

The following diagram displays Tabnine's architecture:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-1136bfda98863206fe5780b2e2d7525717ed45ca%2FTabnine%20cluster%20architecture.png?alt=media" alt=""><figcaption></figcaption></figure>

**The Tabnine platform includes three main components:**

<details>

<summary>Tabnine client (IDE plugin)</summary>

End users install Tabnine as an IDE plugin on their local device.

The Tabnine IDE plugin enables Tabnine’s code completion or chat features within the developer’s IDE.

The client queries a remote Tabnine cluster requesting assistance for the relevant Context Window.

</details>

<details>

<summary>Tabnine cluster</summary>

Tabnine's Kubernetes cluster runs the following services:

* **Inference service:** Runs on a GPU-accelerated node, which serves responses based on the AI models
* **Data plane:** Includes analytics and log services; no code is stored nor sent to the data plane, and user identifiers are always masked
* **Control plane:** Includes identity and user management, an update service, and a configuration service

</details>

<details>

<summary>Tabnine’s AI models</summary>

Tabnine uses two types of proprietary AI models for code completions and chat:

* **Universal models**, trained on public, permissive, state-of-the-art, open source code
* **Fine-tuned AI models** with expanded training of Tabnine’s models with your codebase (Tabnine Enterprise only)

**Pro** users only have access to the universal models.

**Enterprise customers** can have fine-tuned AI models. [Explore plans](https://www.tabnine.com/pricing)

In addition: Tabnine Chat users in Tabnine **Pro** and can switch to **third-party models** not hosted by Tabnine, by accepting their terms of use. Note, the third-party models may offer different code privacy and protection policies. In Tabnine Enterprise, the team admin controls which chat models are available to the organization. For private installation deployment, only the Tabnine Protected model is currently available. [Learn more](https://docs.tabnine.com/main/welcome/readme/ai-models)

</details>

### Deployment types

Tabnine has two deployment types:

**Tabnine SaaS:** The Tabnine server is hosted in the Tabnine Secure Cloud. This is the default Tabnine option for users with all Tabnine plans (Pro & Enterprise).

[**Tabnine private installation**](https://docs.tabnine.com/main/welcome/readme/deployment-options#private-installations-self-hosted-deployments)**:** The Tabnine server is hosted privately by the customer, either on the customer's VPC (AWS, GCP, or Azure) or on-premises. This is an option that's offered to some Tabnine Enterprise customers.
