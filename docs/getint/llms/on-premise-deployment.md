# Source: https://docs.getint.io/getting-started-with-the-platform/deployment-options/on-premise-deployment.md

# Getint On-Premise

To meet the data security requirements of different organizations (like fintech, and health tech companies with very sensitive data), we offer the On-Premise deployment version.&#x20;

This is practically the same version as the one created in the SaaS/Cloud model, but possible to be installed directly on customers' servers.

{% hint style="info" %}
The On-Premise version of getint.io allows you to be the **owner and administrator** of the processed data during the integration/synchronization.

With that deployment mode, you can have Getint working **fully behind the firewall**. No requests will be performed, except for the apps you are integrating with.
{% endhint %}

## Comparison

| Feature                                                   | On-Premise                | SaaS (Cloud)               | Data Center                |
| --------------------------------------------------------- | ------------------------- | -------------------------- | -------------------------- |
| Integration run interval                                  | >= 0s                     | min 180 seg (3 mins)       | min 120 seg (2 mins)       |
| Multithreading                                            | Supported                 | -                          | Unsupported                |
| Multi-tenancy                                             | Supported                 | One customer - One tenant  | Unsupported                |
| Software update                                           | Performed by the Customer | Applied by Getint          | Performed by the Customer  |
| Host (Server) maintenance                                 | Customer                  | Getint.io                  | Customer                   |
| Data retention                                            | Configurable              | Fixed. Max 1 month         | Configurable               |
| Health monitoring                                         | Customer responsibility   | Handled by Getint          | Customer responsibility    |
| <p>Max number of items<br>to sync per integration run</p> | Unlimited                 | Connector based (max 1000) | Connector based (max 1000) |
| <p>Max number of items<br>to sync per migration run</p>   | Unlimited                 | 10000                      | 10000                      |

If you have further questions about our pricing, please visit [Getint.io](https://www.getint.io/) or contact us at our [Support Centre](https://getint.io/help-center). Our integration experts are always happy to help.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
