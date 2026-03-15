# Source: https://docs.firehydrant.com/docs/status-page-setup-and-configuration.md

# Setup and Configuration

> 📘 Note:
>
> This article is about FireHydrant's built-in status pages. For information about Atlassian Statuspages, visit [Atlassian Statuspage documentation](https://docs.firehydrant.com/docs/atlassian-statuspage-integration) instead.

<Image align="center" alt="FireHydrant Status Pages" border={false} caption="FireHydrant Status Pages" src="https://files.readme.io/d53139e-status-pages.png" width="650px" />

You can create a [new Status Page](https://app.firehydrant.io/status_pages/new) in FireHydrant by clicking **Status Pages** in the top nav, then "+ Create status page." Throughout the creation process, you will be able to see a preview of all changes made on the right hand side panel. If you do not see this preview, you will need to widen your window.

## General Settings

Within the General Settings tab of the status page setup, you will be setting the host name, branding to include your logo, and configuring the conditions to show on all created status pages.

### Details

<Image border={false} src="https://files.readme.io/70d3b2fe1c52febc9aafb58b13be3637302abfcd734ba3eb206c01311779e072-image.png" />

<Table>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Name**
      </td>

      <td>
        ***(Required)*** The name FireHydrant uses internally to refer to your status page. This is not visible to external viewers
      </td>
    </tr>

    <tr>
      <td>
        **Host name**
      </td>

      <td>
        ***(Required)*** The host name of your status page.

        **THIS CANNOT BE CHANGED ONCE SET**
      </td>
    </tr>
  </tbody>
</Table>

### Branding

<Image border={false} src="https://files.readme.io/0c988fc0eda61e8aadf98481b2fe7305cb52751a52f2a7e59ce9346246de7e7c-image.png" />

<Table>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Light Mode Logo**
      </td>

      <td>
        A logo to display when a user is viewing the status page in light mode.

        Default is no logo.
      </td>
    </tr>

    <tr>
      <td>
        **Dark Mode Logo**
      </td>

      <td>
        A logo to display when a user is viewing the page in dark mode.

        Default is no logo.
      </td>
    </tr>

    <tr>
      <td>
        **Favicon**
      </td>

      <td>
        Default is no logoFavicon for your status page.

        Default is no favicon.
      </td>
    </tr>

    <tr>
      <td>
        **Open Graph Image**
      </td>

      <td>
        The image displayed in social media or link previews when linking the status page on other websites.

        Default is no image.
      </td>
    </tr>
  </tbody>
</Table>

### Conditions

<Image border={false} src="https://files.readme.io/6135fbb77cd1a891cef46ed3f39f22eb95b6ac9de225cf32fb425ea826b9f152-image.png" />

By default, FireHydrant comes with "Operational", "Unavailable", "Degraded", and "Bug" as available conditions.

These can be configured and customized in your settings under **Settings> Incidents > Conditions** in the application. To learn more, visit [Service Catalog Conditions](https://docs.firehydrant.com/docs/conditions).

| **Field**       | **Description**                                                                                           |
| --------------- | --------------------------------------------------------------------------------------------------------- |
| **Operational** | What condition(s) to show as "Operational" on the status page. Typically, "Operational" is inserted here. |
| **Degraded**    | What condition(s) to show as "Degraded" on the status page. Typically, "Degraded" is inserted here.       |
| **Unavailable** | What conditions to show as "Unavailable" on the status page. Typically, "Unavailable" is inserted here.   |

## System Status Page

The following configuration will apply to the system status page. This will be the page initially presented to your viewers when navigating to your status page. The system status page shows the overall system status as well as the status of any component and component groups you designate.

### Content

<Image border={false} src="https://files.readme.io/eaceaf02cabe21cc027ae06d7c375ec54846eb21dce539765a9f931711f178c7-image.png" />

When users navigate to your status page, they will see an overview page, showing the current system status and the status of any configured components. Customize the system status page by configuring the following options.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Page title**
      </td>

      <td>
        ***(Required)*** An externally-facing page title displayed when there's no logo and the name of the page tab or window.
      </td>
    </tr>

    <tr>
      <td>
        **Heading**
      </td>

      <td>
        A greeting/headline for the page.

        Defaults to nothing
      </td>
    </tr>

    <tr>
      <td>
        **Description**
      </td>

      <td>
        A message to help your viewers understand the content and goals of the page.

        Defaults to nothing
      </td>
    </tr>

    <tr>
      <td>
        **Operational Message**
      </td>

      <td>
        A message to display when all systems and services are operational.

        Defaults to "Nothing to report."
      </td>
    </tr>

    <tr>
      <td>
        **External Links**\
        (maximum of 2)
      </td>

      <td>
        Arbitrary additional links to display on the page in the header area.
      </td>
    </tr>
  </tbody>
</Table>

<br />

### Components

<Image border={false} src="https://files.readme.io/d601b3f4ed1e06bc996663eebdb58205a0c89ee32fa5f00eea31a8e9cbb34615-image.png" />

Designate which Service Catalog items you'd like to display on the status page. We typically see people show their Functionalities, but you can choose from Environments, Functionalities, or Services to display. You can add components to groups and subgroups to roll-up component conditions.

To create a group, click "Add component group." Then, you'll be prompted to name your group and add components. Once you added at least one group, you can nest any additional groups underneath another group, creating subgroups. When components are grouped, they will create a roll-up status and 90-day history of status based on the child components.

<Image align="center" alt="Example with component group &#x22;US-East 1&#x22;" border={false} caption="Example of status pages with 90-day history and component grouping &#x22;US-East 1&#x22;" src="https://files.readme.io/b6c058e-status-page-components-groups.png" width="650px" />

## Incident Details Page

<Image border={false} src="https://files.readme.io/49f52a22f3aad64952063b07069e00ef70072be1bc70c3836e8fd648c94b0b64-image.png" />

In the event of an incident, your viewers will also have the ability to follow incident updates on an incident specific status page. You may configure this page to include any number of incident fields on the right hand side.

Aside from standard [Incident Fields](https://docs.firehydrant.com/docs/incident-fields), there are specific items available to show on status pages:

* **Related Incidents** - Normally shown in the [The Command Center](https://docs.firehydrant.com/docs/the-command-center), you can also display related incidents on the status page
* **Links** - The list of links attached to the incident, including tickets and [external links](https://docs.firehydrant.com/docs/adding-external-links) but excluding conference bridges and incident channels
* **Slack Channel** - If you want to show the link to the incident Slack channel (e.g., the status page is authenticated and internal), you may do so
* **Conference Bridges** - If you want to show the links to any bridges (e.g., the status page is authenticated and internal), you may do so
* **Command Center Link** - If you want to show the direct link to the incident in FireHydrant, you can (would require logging in to FireHydrant to access anyway)

## Authentication

<Image border={false} src="https://files.readme.io/a67dfd72dee9b14927e1d9c41a50481ed9765179326d017f5f547c5526afe2e4-image.png" />

### Domain Configuration

<Image border={false} src="https://files.readme.io/6581bbad3cacccb5bbc1cf306c080a0777ce35ded67864faacdec30f442223da-image.png" />

After creating your page, you are presented with a CNAME target to point your domain at our system. You can see more notes on configuring your CNAME record below in [CNAME Configuration](#cname-configuration).

### Publish Status Page

<Image border={false} src="https://files.readme.io/ea2a9cd0df51b512aa6e094a63769b17b094f49661c9a87137be09e7adca6ee9-image.png" />

We will soon be enabling the ability for you to automatically publish new status pages upon DNS verification. When this feature is available, you will be able to enable this toggle and the created status page will be published and available as soon as the DNS record has been verified within our system.

### Authentication

<Image border={false} src="https://files.readme.io/1798e8f4ede99cc63929aa03780ca1c6496fc6068c2050da852eb958b5ababda-image.png" />

You can limit the audience of your status page to your employees or other groups of customers by configuring authenticated status pages. To enable, visit the appropriate instructions for your SSO provider:

* [Microsoft Entra for Status Pages](https://docs.firehydrant.com/docs/microsoft-entra-for-status-pages)
* [Google Auth for Status Pages](https://docs.firehydrant.com/docs/google-auth-for-status-pages)
* [Okta for Status Pages](https://docs.firehydrant.com/docs/okta-for-status-pages)

> 🚧 Note:
>
> If you have existing authenticated Status Pages, please reach out to our support team to transition to the new configuration.

## DNS Verification and Publishing

<Image border={false} src="https://files.readme.io/239d1e52d24767b1a04c4d8922df26c685f9d17e8d3cdd401df11d6c5fcf2d34-image.png" />

Once your Status page has been fully configured, we will automatically verify your DNS record, and upon successful verification will prompt you to publish your Status Page from the Status Page overview. You may also unpublish, edit, or delete the status page from this table as well as view the list of subscribers per status page.

### CNAME Configuration

You will want to find and use the documentation for whichever DNS provider you use. Generally, you'll need to create a CNAME record for your domain/subdomain and point it to the generated CNAME value FireHydrant provides. The example below is from Namecheap and points the `acme` subdomain of this domain to the status page:

<Image align="center" alt="Example of configuring a CNAME record in Namecheap" border={false} caption="Example of configuring a CNAME record in Namecheap" src="https://files.readme.io/f88ff4c-namecheap.png" width="650px" />

Depending on the DNS provider, it can take from several minutes to hours before the records propagate. Check your provider's documentation to see how long the expected wait time is. Then, to confirm that your DNS is configured correctly, use `dig` from the command line or [Google's DNS toolbox.](https://toolbox.googleapps.com/apps/dig/)

```Text Command Line
➜ ~ dig +short acme.example.com aabbccddeeff.sp-production.firehydrant-customer.com
```

<Image align="center" alt="Using Google's DNS toolbox" border={false} caption="Using Google's DNS toolbox" src="https://files.readme.io/2a209dd-image.png" width="650px" />

> 🚧 Note:
>
> FireHydrant's system automatically purges status page records after 2 weeks if CNAME records don't resolve. Please ensure you create the CNAME DNS record within 2 weeks of creating your FireHydrant status page.

### CAA Records

CAA records are a way to specify publicly that you've only authorized certificates for your domain to be made with very specific parameters. FireHydrant's status pages use self-issued certs with Let's Encrypt, which can sometimes cause issues with CAA records that exist for custom domains.

If there is a problem with FireHydrant status page certs and your CAA, you may see a warning from your browser when visiting your custom status page domain, such as: `The certificate is not trusted because it is self-signed.`

To fix this, we recommend amending the CAA record to include Let's Encrypt. These are the lines you'd need to add:

```
issue "letsencrypt.org"
iodef "mailto:ops@firehydrant.io"
```

## Next Steps

* Learn how to [use your new FireHydrant status page on incidents](https://docs.firehydrant.com/docs/status-page-usage)!