# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/set-confidence-thresholds-for-your-integrations.md

# Set Confidence Thresholds for your Integrations

Builder users can set the **confidence levels** for their Integrations (such as EnateAI's) in the General Settings section. This gives users a greater level of control and flexiility when implementing Integrations into their operations, letting them quickly and easily adjust Integrations confidence levels as needed to allow more of fewer Work Items to be passed via Agents for verification after AI has taken some action.

### How to find the EnateAI confidence level settings

Within Builder, go to the **General Settings** page, then to the **'Integrations'** section.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FaLxK5JH5f1LIXEbIMntk%2FIntegrations%20Sliders.webp?alt=media&#x26;token=9c641b8d-75a8-4175-9eb4-c35b93216801" alt=""><figcaption></figcaption></figure>

This section allows users to set the confidence Thresholds for all available Integrations which use them. level for:

* **Document Classification Integrations**
* **Email Classifications Integrations**
* **Document Extraction Integrations**
* **Thank You Email Integrations**

### How to set an integration confidence threshold

To set the confidence threshold users simply need to move the slider for the desired integration.&#x20;

#### Threshold values - higher vs. lower

Keep in mind when setting a confidence threshold that a higher setting requires the AI to be very confident in its results if it is to avoid human involvement - e.g. setting to 90% means 'only let results with a 90% confidence value or higher returned move on, get anything lower checked by a human'. Conversely, setting a lower threshold means that work is *less* likely to be routed to a human to check, e.g. 'only require results with a confidence level lower than 70% be checked by a human'.

### What if an integration is not active?

If users do not have a specific integration activated in the Enate Marketplace, there will be a **'Get This Integration'** button displayed instead of the slider. Clicking on this button will take the user to the section of the Enate Marketplace where the Integration offerings for that confidence level option are.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtWdwyy6DxePPl1OoiZYz%2FGet%20Integration.png?alt=media&#x26;token=796f4ff1-fbb5-4da6-8eec-3c2d769ffeec" alt=""><figcaption></figcaption></figure>

### Integrations that do not have confidence levels

For Integrations that do not work with Confidence Thresholds, no sliders are provided. Examples of this are Sentiment Analysis and Email Data Extraction Integrations.

### Other integration technology providers

These confidence threshold sliders control the threshold levels for ALL Integration patterns, no matter which technology provider has been enabled for it in Marketplace.
