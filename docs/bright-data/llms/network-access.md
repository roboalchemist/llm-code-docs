# Source: https://docs.brightdata.com/proxy-networks/residential/network-access.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Residential Network Access Policy

> To safeguard our expansive and ethical Residential network, Bright Data applies monitoring rules to ensure all Residential proxy traffic aligns with approved use cases and compliance policies.

Bright Data offers two distinct modes for accessing its Residential network:

<CardGroup cols={2}>
  <Card title="Immediate access (default)" href="/proxy-networks/residential/network-access#immediate-access">
    Begin targeting with our Residential network immediately after sign up, without the need for KYC
  </Card>

  <Card title="Full access (recommended)" href="/proxy-networks/residential/network-access#full-access">
    Expand your Residential network access for your approved use case by completing KYC
  </Card>
</CardGroup>

On initial setup of your Residential proxy, by default you are given [**Immediate access**](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) and can get started targeting a wide range of domains right away.

If during your initial targeting you encounter a [402 Residential Failed (bad\_endpoint)](https://docs.brightdata.com/proxy-networks/errorCatalog#http-error-402) or `robots.txt` error, you will need to request [**Full access**](https://docs.brightdata.com/proxy-networks/residential/network-access#full-access), which can be granted once we get to know you and your use case better through [KYC](https://brightdata.com/cp/kyc).

## Immediate access

<Warning>
  An [SSL certificate](https://docs.brightdata.com/general/account/ssl-certificate) must be installed on your device when accessing our Residential network with *Immediate access*.
</Warning>

* Access a wide range of domains without KYC, under the following limitations:
  * Domains restricted by their own 'robots.txt' rules.
  * Domains restricted by Bright Data’s compliance policy for Immediate access.
  * Use of certain HTTP methods (POST, PUT, DELETE) is not permitted.
  * Automatic throttling may be applied if request volume exceeds acceptable thresholds (`status code: 502`, `error: sr_rate_limit`).
  * Note: Attempting to access restricted domains or methods will result in a `402 Residential Failed (bad_endpoint)` error and you'll need to apply for [Full access](https://docs.brightdata.com/proxy-networks/residential/network-access#full-access) mode instead.

<Tip>
  Completing [KYC](https://brightdata.com/cp/kyc) removes the above restrictions and automatically grants you **Full access** to domains under the Residential network, tailored to your approved use case.
</Tip>

<AccordionGroup>
  <Accordion title="Why does Immediate access mode require an SSL certificate?">
    ### Secure and Ethical Usage

    Our SSL certificate ensures compliance with Bright Data's ethical guidelines while providing secure encryption. Since Immediate Access does not require KYC, the SSL certificate acts as an added layer of assurance, enabling Bright Data to enforce compliance and safeguard the ethical use of our Residential network. This ensures that the network is used responsibly while protecting both users and our infrastructure.

    If you don't install our SSL certificate, your requests may be rejected with security errors like "SSL/TLS handshake failure" or "certificate validation error", indicating an insecure connection. While you can bypass and ignore SSL errors, this is not recommended as it compromises your long-term security.
  </Accordion>

  <Accordion title="Why installing an SSL certificate is simple and secure">
    By installing the SSL certificate, you can immediately start using the Residential network with minimal friction, while enjoying the peace of mind that your traffic is handled ethically and securely.

    Installing an SSL certificate may sound daunting, but it’s a quick, secure, and one-time setup process that unlocks Immediate Access. Here’s why it’s worth considering:

    ### Temporary and Limited Data Handling

    Bright Data accesses minimal data (e.g., web pages visited, access times) only for troubleshooting and compliance purposes. This data is stored temporarily and is not shared with third parties, except where legally required.

    ### Privacy-Focused Approach

    We prioritize your privacy above all else. Learn more in our [Privacy Policy](https://brightdata.com/privacy)

    ### Still prefer not to install an SSL certificate?

    If you prefer not to install an SSL certificate, you can complete the [KYC process](https://brightdata.com/cp/kyc) to unlock Full Access, eliminating the need for SSL while enabling broader network capabilities.
  </Accordion>

  <Accordion title="What is robots.txt and how does it affect Immediate access?">
    `robots.txt` is a file that website owners use to define which areas of their site can be accessed by automated systems. In **Immediate access** mode, Bright Data adheres to these rules to ensure ethical compliance. Requests to blocked areas will return a `402 Residential Failed (bad_endpoint)` error. For unrestricted **Full access**, complete [KYC](https://brightdata.com/cp/kyc).
  </Accordion>

  <Accordion title="Why can't I add dedicated residential proxies?" defaultOpen="false">
    Our dedicated residential proxies are available only to customers who complete our verification process. In Bright Data control panel, when you add a residential proxies zone, under "Proxy type" selection, the "Dedicated" proxies will appear disabled until you pass our verification process. You can use our "Shared" residential proxies in immediate access mode, after installing our certificate or ignoring SSL errors.
  </Accordion>
</AccordionGroup>

## Full access

* After completing [KYC](https://brightdata.com/cp/kyc), you will have Full Access to the Residential network, tailored to your approved use case.
* Allows the use of HTTP methods in your request
* SSL certificate is **not** required
* The option to submit a KYC form is only open to customers that signed up on behalf of a registered company. You will be required to add a user with a company email domain to your account and submit a company registration document during the process.

## FAQ: What is Bright Data KYC (Know Your Customer) verification process?

<AccordionGroup>
  <Accordion title="Why do you require KYC for Full Access?">
    * Our KYC (“Know Your Customer”) process is a mandatory step for all new customers who wish to join our residential proxy network or gain special access rights.
    * The purpose of this stage is to ensure that we maintain the highest possible compliance and ethics standards by verifying your business and use case.
    * If you were asked to complete the process that means you requested access to our residential network or require a special access right that is not allowed by default in our system.
  </Accordion>

  <Accordion title="What is the process for KYC verification?">
    To complete KYC, you’ll need to submit details about your yourself and your scraping use case to verify eligibility by our Compliance team. This process removes the need for an SSL certificate and unlocks access to sites not pre-approved in Immediate Access. Start the KYC process below:

    [Start KYC Verification](https://brightdata.com/cp/kyc)

    <Warning>
      The KYC process is not available in [Playground](https://docs.brightdata.com/general/faqs#what-is-playground-mode)/[Limited Trial](https://docs.brightdata.com/general/faqs#what-is-limited-trial-mode) modes. The process can be started only after adding real funds to the account balance.
    </Warning>
  </Accordion>

  <Accordion title="How much time does it take to get my KYC approved?" defaultOpen="false">
    * Completing the form should only take a few minutes.
    * Once submitted, our team validates the information in the submission and the KYC undergoes our compliance review.
    * You can see the status of your request in your Bright Data control panel, under Account Settings > Profile.
    * We will update you in up to 48 hours from the time of completing the process regarding your KYC status.
  </Accordion>

  <Accordion title="How do I know that my KYC has been approved? " defaultOpen="false">
    * You can check out the status of your KYC process at any time in your control panel. A notification regarding the submission of your KYC and approval or decline of your request will be sent to your email once the process is completed.
    * The status will be under Settings -> Profile , showing "Account verification status"
  </Accordion>

  <Accordion title="Do I have to complete the KYC process to gain Residential network access? ">
    * On initial setup of your Residential proxy, by default you are given Immediate access to the residential network and can get started targeting a wide range of domains right away.
    * If during your initial targeting you encounter a 402 Residential Failed (bad\_endpoint) or robots.txt error, you will need to request Full access, which can be granted once we get to know you and your use case better through KYC.
  </Accordion>

  <Accordion title="Is this a one-time process?">
    The KYC information is documented in our systems to allow us to review your use case if needed in the future. Although we want to make it a one-time process, we also monitor our network 24/7 and we may reach out to you for additional clarifications or information in order to make sure that our network remains safe.
  </Accordion>

  <Accordion title="Who is eligible for the KYC process?">
    Bright Data accepts KYC applications from registered businesses with a company domain. To submit a KYC request, please ensure you verify a company email address.
  </Accordion>

  <Accordion title="What information will I need to share?">
    The KYC process requires some basic information about your business, such as a description of your use case and general contact information.

    The more information we have about your business and your use case the easier it will be for our Compliance & Ethics team to evaluate and approve your request.

    We may require further clarification, validation, or identification, so if needed we will follow up accordingly once you complete the KYC.
  </Accordion>

  <Accordion title="Why might I need to provide identification?">
    In accordance with our verification process, we may request a valid form of identification, such as a driver's license, passport, or other government-issued ID, to verify the identity of the point of contact. This measure helps ensure the safety and integrity of our network. As our IP addresses are linked to 100% real peers, verifying identities is an essential part of our commitment to maintaining a secure and reliable network environment.
  </Accordion>

  <Accordion title="Do I need to set up a video call?">
    We may request a brief video call to verify additional information about your business or intended use case. This step ensures our compliance with policy and ethical standards during the review process.
  </Accordion>

  <Accordion title="What is a company registration form/certificate of incorporation?">
    A company registration form (also referred to as a “Certificate of incorporation”) is used by government offices as proof of registering new businesses. The form usually contains the company's official information, including the company's formal name, registered office address, company registration unique identifier, and more. The form is usually available to the company legal counsel, financial department, or similar and can be publicly shared as part of the company's routine business activity as proof of registration according to local regulations.
  </Accordion>

  <Accordion title="Can I still use Bright Data services while my KYC is inspected?">
    * You can use all our other products and services while your KYC request is being processed.
  </Accordion>

  <Accordion title="Can I still use Datacenter and ISP if my KYC for residential access was declined?">
    * If your KYC was not approved you may still use one of our other products and services according to Bright Data's [license](https://brightdata.com/license).
  </Accordion>

  <Accordion title="What happens during the KYC video call?">
    * In the call, we would like to make sure we support your needs as best as possible, by learning more about your company and your activities, understanding your use case and specific requirements, and viewing relevant systems and workflow.
  </Accordion>

  <Accordion title="What if I don't have a LinkedIn or website?">
    * Our verification process requires vetting a company website and an active online presence. If you have any other form of online presence besides LinkedIn (like a portfolio, GitHub, or alternative business profiles), please share those when submitting your application.
  </Accordion>

  <Accordion title="What if I don't want to do a video call?">
    * If you were requested to do a video call, it is a mandatory step. It helps us verify your identity and clearly understand your use case. Without completing the call, we won't be able to grant you access to the residential network.
  </Accordion>

  <Accordion title="Can I use Bright Data for personal projects?">
    * No. Bright Data is a B2B platform. We only support business-related use cases. If your project is personal (like scraping for a hobby or side project), it won’t be approved.
  </Accordion>

  <Accordion title="What kind of use cases are not allowed?">
    * For Acceptable Use Policy please refer to our [Acceptable Use Policy](https://brightdata.com/acceptable-use-policy).
  </Accordion>

  <Accordion title="I submitted my KYC but haven’t heard back, what should I do?">
    * You should expect an update from us within 48 hours from the time of the KYC submission. If it's been longer, you can check the status in your Control Panel under Account Settings > Profile, or reach out to your account manager or our support team.
  </Accordion>
</AccordionGroup>
