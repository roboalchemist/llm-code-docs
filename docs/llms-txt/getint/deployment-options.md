# Source: https://docs.getint.io/getting-started-with-the-platform/deployment-options.md

# Deployment Options

Getint is engineered to cater to a diverse range of customer needs, including those with their own infrastructure (on-premise/data center), those preferring cloud-based services (SaaS), and organizations with stringent security requirements. Recognizing security as a pivotal concern for our customers and ourselves, we offer the option of on-premise deployment on the customer's own servers. This flexibility sets us apart in the market, offering tailored deployment options to meet specific needs.

**Deployment Choices:**

* **Jira Cloud - Cloud Hosted by Getint**: Our cloud-hosted solution provides a dedicated platform instance on Getint servers, with a separate database for each instance. This model is the standard for Jira Cloud applications. Jira Cloud customers looking for alternative deployment options can reach out to us at <support@getint.io> for personalized solutions.
* **Data Center – Native Application (Jira-Specific)**:&#x20;

  For organizations already running Jira Data Center, Getint offers a native application deployment. Unlike the standalone platform, this version is installed via the Atlassian Marketplace and resides within your existing Jira infrastructure.

  * **Host (Server) Maintenance**: Managed by the customer as part of their Jira Data Center maintenance.
  * **Architecture**: The app runs as a native plugin. For multi-node Jira clusters, Getint uses a cluster lock mechanism to ensure that synchronization tasks are executed on only one node at a time, preventing data duplication or conflicts.
  * **Data Residency**: All configuration details, logs, and synced item information are stored within your Jira instance's database and `JIRA_HOME` directory. This ensures that no data ever leaves your internal network.
  * **Security**: Operates entirely behind your firewall. Since it is a native app, it inherits the security protocols and user permissions already established in your Jira Data Center environment.
* **On-Premise - Hosted by the Customer**: To accommodate organizations with critical data security needs, such as those in the fintech and health tech sectors, we offer an On-Premise deployment option. This allows for the Getint platform to be installed on customer-owned servers, mirroring the functionality of our SaaS/Cloud model. Once installed and licensed, the platform operates independently of Getint servers, connecting only to authenticated applications set up by the client. All data, logs, passwords, and configurations are securely managed on the client's servers. This model is standard for Jira Server/Data Center applications, ensuring data security and autonomy.

**Why Choose Getint?**

Our commitment to security, coupled with the versatility of our deployment models, underscores our dedication to providing solutions that not only meet but exceed our clients' expectations. Whether you prioritize the control and security of on-premise hosting or the convenience and scalability of cloud services, Getint accommodates your specific requirements, ensuring that your data is handled with the utmost care and respect.

For more information on our deployment options or to discuss the best solution for your organization, please get in touch with us at our [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

<br>
