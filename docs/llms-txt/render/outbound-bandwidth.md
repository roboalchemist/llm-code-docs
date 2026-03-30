# Source: https://render.com/docs/outbound-bandwidth.md

# Outbound Bandwidth — Understand how egress traffic is measured and priced on Render.


> *On August 1, 2025, we lowered bandwidth pricing and expanded the types of traffic that are billed.*
>
> This article reflects the new pricing model. For more information about these changes, see the [blog post](/blog/new-bandwidth-pricing-on-render).

Render tracks the amount of network traffic sent from your workspace's services to destinations outside of Render. This traffic is billed as *outbound bandwidth* usage.

Each month, your workspace receives an included amount of outbound bandwidth based on its [plan](/pricing). If your services exceed this amount, Render bills your workspace for an additional 100 GB of bandwidth. Unused bandwidth does not roll over to the next month.

## Billed traffic

All outbound traffic from Render services to the public internet is billed as outbound bandwidth usage.

To understand which traffic is billed, see the diagrams and table below:

[image: Diagram showing traffic billed as outbound bandwidth usage]

[image: Diagram showing traffic not billed as outbound bandwidth usage]

------

###### Traffic type

HTTP responses sent from your [web services](web-services) and [static sites](static-sites) to browsers and other clients over the public internet

###### Billed?

☑️

---

###### Traffic type

WebSocket responses sent from your [web services](web-services) to browsers and other clients over the public internet

###### Billed?

☑️

---

###### Traffic type

**Service-initiated:**

Network communication initiated by any Render service or [one-off job](one-off-jobs) over the public internet

###### Billed?

☑️<sup>\*</sup> Same-region traffic to Amazon S3 or Google Cloud Storage is not billed as outbound bandwidth usage.

---

###### Traffic type

**Service-initiated:**

Query responses from [Render Postgres](postgresql) and [Render Key Value](key-value) datastores to a destination outside of Render

###### Billed?

☑️

---

###### Traffic type

Traffic to a non-Render resource over a [private link connection](private-network#integrating-with-aws-privatelink)

###### Billed?

☑️<sup>\*</sup> This traffic is billed at a significantly lower rate than other outbound traffic.

---

###### Traffic type

<a href="/private-network">Private network</a> traffic between Render services in the same region

###### Billed?

➖

---

###### Traffic type

Inbound traffic from any source to your Render services

###### Billed?

➖

------

## Pricing

Outbound bandwidth is billed at *$15 per 100 GB* beyond your workspace's monthly included amount.

Traffic sent over a [private link connection](private-link) is billed at a significantly lower rate than other outbound traffic.

Each workspace receives a monthly included amount of outbound bandwidth based on the workspace's plan:

| Workspace plan | Included bandwidth |
| --- | --- |
| *Hobby* | 100 GB |
| *Professional* | 500 GB |
| *Organization* | 1 TB |
| *Enterprise* | Custom |

Many workspaces never exceed their included amount, which means they aren't charged for outbound bandwidth at all.

## FAQ

###### Why has Render made changes to outbound bandwidth pricing?

The recent update brings our pricing model in line with industry norms and helps us accurately reflect real infrastructure usage. This change enables us to maintain reliable, high-performance service across the platform while building a sustainable business.

###### Have these changes increased my monthly costs?

*For almost all workspaces, no.* However, your bandwidth costs might increase if:

- Your services send a high volume of traffic over the internet to externally hosted APIs and datastores
- Your web services send a high volume of WebSocket messages to connecting clients

Customers with a significant bill increase were notified and will receive bandwidth support credits for August and September to give them time to optimize and adjust usage.

###### What happens if I exceed my monthly included amount of outbound bandwidth?

- *If you've linked a payment method,* Render bills you for an additional 100 GB of bandwidth.
  - Unused bandwidth does not roll over to the next billing period.
- *Otherwise,* Render spins down your workspace's services until the start of the next month.

###### How do I monitor my outbound bandwidth usage?

- View an individual service's recent usage from its *Metrics* page in the [Render Dashboard](https://dashboard.render.com).
  - The *Outbound Bandwidth* graph displays the service's usage broken out by traffic type. [See details.](service-metrics#outbound-bandwidth)
- View your workspace's total monthly usage from the [Billing page](https://dashboard.render.com/billing) in the Render Dashboard.
