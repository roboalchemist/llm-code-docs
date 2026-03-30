# Source: https://docs.tabnine.com/main/welcome/readme/architecture/deployment-options.md

# Deployment options

### Deployment options

* **Secure SaaS**
* **Private installation** (self-hosted deployments):

  * Virtual private cloud (VPC)
  * On-premises

  \* Private installations can be deployed in a completely air-gapped environment.

Free and Pro users only have access to the secure SaaS deployment. [Explore plans](https://www.tabnine.com/pricing)

Enterprise customers are also offered private deployment options. [Contact Sales](https://www.tabnine.com/contact-us/?utm_source=docs\&utm_medium=organic\&utm_campaign=docs)

{% hint style="info" %}
**Follow the right docs**

The client installation and management instructions are slightly different between **Tabnine SaaS** and **Tabnine private installation**.
{% endhint %}

***

### Secure SaaS

This type of deployment is available for Starter, Pro, and Enterprise customers.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-00e999c63081c005671fe040ae611b368db2d256%2FNew%20Architecture%20red%20brand%202.png?alt=media" alt=""><figcaption></figcaption></figure>

The solution is hosted, managed, and monitored by Tabnine, and is frequently updated.

Tabnine is committed to maintaining the highest levels of security and privacy for our clients. With our SaaS deployment, we’ve implemented an end-to-end encryption system to ensure that the communication between our client’s users and our servers remains completely secure. [Read more about the security](https://trust.tabnine.com/) we provide.

**Continuous monitoring and audits:** Our security team continuously monitors for vulnerabilities and conducts regular audits to ensure that our security infrastructure is up to the latest standards. This ensures that our customers' data is handled with the utmost care and security.

Please check our [Trust Center](https://trust.tabnine.com/) for more information.

***

### Private installations (self-hosted deployments)

These are the private installation options that are offered for Tabnine Enterprise:

### VPC

This is an option for [Tabnine Enterprise](https://www.tabnine.com/enterprise) customers.

<figure><img src="https://d16xvuom8mr9m8.cloudfront.net/_next/static/images/vpc-8be1ddc4d06d3c5267e175e28171d1e8.png" alt=""><figcaption></figcaption></figure>

In a VPC setup, the Tabnine cluster is a Kubernetes-hosted unit on your virtual private cloud (**GCP**, **AWS,** or **Azure**). Tabnine doesn't have access to the customer environment. Periodic software updates are done in a controlled way.

Learn more about the [system requirements](https://docs.tabnine.com/main/welcome/system-requirements#tabnine-cluster) for the cluster.

***

### **On-premises**

This is an option for [Tabnine Enterprise](https://www.tabnine.com/enterprise) customers.

<figure><img src="https://d16xvuom8mr9m8.cloudfront.net/_next/static/images/on_perm-629b5cad01ee5a49b072229071f07a68.png" alt=""><figcaption></figcaption></figure>

In an on-premises private installation, the Tabnine cluster is a Kubernetes cluster hosted on the customer's servers on their private network. Tabnine doesn't have access to the customer environment. Periodic software updates are done in a controlled way.

Learn more about [system requirements](https://docs.tabnine.com/main/welcome/system-requirements#tabnine-cluster) for the cluster.

***

### Fully air-gapped private installation

This is an option for [Tabnine Enterprise](https://www.tabnine.com/enterprise) customers.

<figure><img src="https://d16xvuom8mr9m8.cloudfront.net/_next/static/images/cluster-f2082de03a46eb63781b73bd83d5eb0c.png" alt=""><figcaption></figcaption></figure>

The Tabnine solution can also be deployed in a completely air-gapped environment.
