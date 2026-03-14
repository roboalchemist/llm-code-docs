# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/power-automate.md

# Power Automate

## Enate Integration Architecture

Enate supports a number of RPA technologies including UiPath, Blue Prism, Automation Anywhere and Power Automate.&#x20;

Enterprise organisations need to connect large numbers of business applications together to build their technology stack.

Currently, the best practice recommendation for enterprise architectures is to use a **Composable Architecture** approach. The headlines from Gartner’s latest paper, “Future of Applications: Delivering the Composable Enterprise,” help give some insights into this:

* A Composable Enterprise is an organization that can innovate and adapt to changing business needs through the assembly and combination of packaged business capabilities.
* Packaged business capabilities will be sourced from third parties or composed internally. They will deliver more unique and customized application experiences to application users.
* To enable the composable enterprise, organizations will need to adapt the way they source and deliver applications as vendors deliver more modular capabilities.

#### What does this mean for your Enate implementation?

Running a Composable Architecture means using a decoupled architecture rather than creating a very tightly coupled integration directly between Enate and each individual Line of Business system. This decoupling is achieved using specialist integration components that are tailored to the job.

Microsoft Power Automate is a citizen developer integration platform designed for precisely this purpose. Enate links seamlessly with Power Automate provide giving you the power of Microsoft’s standard connectors with Enate managing the end-to-end process orchestration for business users. &#x20;

MS Power Automate provides out-of-the-box integrations for a huge number of the most widely used business applications such as SAP, Salesforce, and Workday. A full list can be found here- [List of supported connectors | Microsoft Power Automate](https://flow.microsoft.com/en-us/connectors/) and is growing every day. Bringing MS Power Automate to bear reduces setup time and simplifies the approach to integration; the drag and drop interface provides a low-code approach to integration.

### Example - Enate Orchestrates SAP Integration wth Power Automate

This example shows you how Enate updates to SAP by triggering Power Automate:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mdv8aCd9yxJbHMaqHqd%2F-MdvBAwOMFNJOTr7_ZlB%2Fimage.png?alt=media\&token=fcf9286b-749d-4ef0-97bd-cc819b01992b)

1. Invoice extraction & validation (which may be manual or through Intelligent Document Processing) creates a new work item in Enate with invoice details and line-item detail.
2. Enate then posts an API call to MS Power Automate, passing through all data which Power Automate needs to update the target system. Enate also provides a call-back URL, allowing Power Automate to update Enate on progress.
3. MS Power Automate then updates SAP with all relevant data using the standard connector calling either SAP’s BAPI or RFC interface.
4. If the update fails, Enate’s in-built ‘airbag’ features kick in and bring a human user into the loop to manage the situation and ensure the transaction is corrected.

The Power Automate SAP connector allows both BAPI and RFCs to be called on either SAP S4HANA or SAP ECC. In both cases, the On-premise Data Gateway should be installed, giving Power Automate appropriate access to SAP. Authentication can either be through SAP authentication or Windows authentication.

### MS Power Automate Licensing

Most enterprise organisations already have MS Power Automate licenses as part of their MS Enterprise bundles. Please see the pricing here: [Pricing | Microsoft Power Automate](https://flow.microsoft.com/en-us/pricing/). A download link to the detailed license guide can be found here: <https://go.microsoft.com/fwlink/?LinkId=2085130&clcid=0x409>.

Typical cost for running 5 MS Power flows triggered from Enate for 100 invoices per day would be c$500/month.

### Configuring Enate Case to call Post url

For each tailored integration that you create in Power Automate, a post URL like the one shown below will be generated. You simply configure your Enate Case process to call this URL at runtime. See the [External API Action](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/external-api-action-info-tab) section for details of how to do this in your Case flows in Builder.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mdv8aCd9yxJbHMaqHqd%2F-MdvAJRNs7MxCUzuC-wB%2Fimage.png?alt=media\&token=0188722b-b7d6-4603-bc4f-87a117f15865)

At runtime, Enate will call the above URL, passing in relevant data for the activity. A sample of the kind of information which would be passed is shown below:

```
{
"Action":{
  "Instruction": "update SAP with this invoice data",
  "Comments": "",
  "Invoice ID": 123,
  "Invoice Date": 2021-06-22,
  "Invoice Amount": 1000,
  "Invoice currency ": USD,
  "RobotRejectedReason": null,
   ………
  "CallBackURL":""
}
}
```

More details about Enate integration can be found in the [APIs](https://docs.enate.net/enate-help/integrations/enate-integrations/apis) section.

## Sample Integration Patterns Using Power Automate

{% content-ref url="example-how-to-set-up-a-bot-status-monitor-in-power-automate" %}
[example-how-to-set-up-a-bot-status-monitor-in-power-automate](https://docs.enate.net/enate-help/integrations/enate-integrations/example-how-to-set-up-a-bot-status-monitor-in-power-automate)
{% endcontent-ref %}

{% content-ref url="sample-extracting-email-and-attachments-to-sharepoint-with-power-automate" %}
[sample-extracting-email-and-attachments-to-sharepoint-with-power-automate](https://docs.enate.net/enate-help/integrations/enate-integrations/sample-extracting-email-and-attachments-to-sharepoint-with-power-automate)
{% endcontent-ref %}
