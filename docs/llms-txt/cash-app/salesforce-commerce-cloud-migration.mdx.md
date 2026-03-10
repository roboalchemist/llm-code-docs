# Source: https://developers.cash.app/cash-app-afterpay/guides/welcome/migrate-from-afterpay-to-cash-app-afterpay/platforms/salesforce-commerce-cloud-migration.mdx

***

## stoplight-id: 0asudig8pidha

# Salesforce Commerce Cloud Migration

To migrate from Afterpay to Cash App Afterpay, update your cartridge. When you upgrade the Afterpay cartridge, you automatically receive the user experience benefits of Cash App Afterpay.

* Update the cartridge to v24.1.3 or higher

See the instructions below:

1. To use the Cash App Afterpay product with Salesforce, download the latest version of the Afterpay cartridge [here](https://github.com/afterpay/afterpay-salesforce-commerce-cloud).

2. See the [Install the Cartridge and Import the Metadata](#install-the-cartridge-and-import-the-metadata) section below to install the new cartridge and integrate it with your systems.

<Note>
  The SFCC cartridge and the Business Manager call Cash App Afterpay by the single word Afterpay. This doesn't affect any of the instructions or advice below.
</Note>

## Install the Cartridge and Import the Metadata

To install the lastest version of the cartridge, do the following:

1. Download the cartridge

   * The current version of the cartridge is available directly from [Cash App Afterpay](https://github.com/afterpay/afterpay-salesforce-commerce-cloud)
   * It’s also hosted on Salesforce’s [AppExchange platform](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N3u00000R8GgbEAF\&tab=e)

2. Build the client-side Resources. These are the client-side CSS (Cascading Style Sheets) and JS (JavaScript) files that are specific to Cash App Afterpay; this is a required step.

   * Confirm that `package.json` contains the correct reference to the location of the SFRA base cartridge (Only for SFRA):

3. Set the path. Set the path to the base cartridge of SFCC which is required for the Cash App Afterpay cartridge to work.

   ```
   "paths": {
   "base": "../storefront-reference-architecture/cartridges/app_storefront_base/"
   },
   ```

4. Install/Run commands. These commands install the node in our cartridge onto your local storage and compiles the JS and CSS files residing in our cartridge.

   ```
   $ npm install
   $ npm run compile:js
   $ npm run compile:scss
   ```

5. Import the cartridge. Use **UX Studio** to import the cartridge. Alternatively, you can also use **Node Package Manager (npm)** and run **uploadCartridge**, or the **VSCode Prophet** plugin.

Once you have completed the five steps above, you are ready to import the metadata. See the section below.

### Import the Metadata

For the Cash App Afterpay integration to work, the following object structures (metadata) must be imported and configured in the **Business Manager**. Do the following:

1. In the cartridge bundle go to the folder *metadata/afterpay-meta-import/sites*.

2. Rename the *RefArch* folder to the ID of your site. You can find the site ID in *Administration* > *Sites* > *Manage Sites* in the *Business Manager*.

3. Compress the  *afterpay-meta-import* folder to generate the `afterpay-meta-import.zip` file.

4. In the *Business Manager*, go to *Administration* > *Site Development* > *Site Import & Export* and import the zipped file.

Once you have imported the metadata, you are ready to make some final checks. See the section below.

### Check For File Conflicts/Changes.

1. If you are using *SiteGenesis*, see the [SiteGenesis code changes](/cash-app-afterpay/guides/platforms/salesforce-commerce-cloud/site-genesis-code-changes) page to add Cash App Afterpay-specific code changes to your base store cartridges.

2. If you are using *SFRA*, see the [SFRA Files change review](/cash-app-afterpay/guides/platforms/salesforce-commerce-cloud/sfra-files-change-review) page to see the files that override the files in the base cartridge.

## Brand Assets

There are new Cash App Afterpay brand assets to use at checkout and across your site. See the [Brand Assets](/cash-app-afterpay/guides/welcome/migrate-from-afterpay-to-cash-app-afterpay/brand-assets) page in this guide for these new assets.

The table below has examples of the changes:

|         | Afterpay                                                | Cash App Afterpay                                       |
| ------- | ------------------------------------------------------- | ------------------------------------------------------- |
| Logos   | <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/ap-logo-resized.png" /> | <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/caap-white-logo-resized.png" /> |
| Buttons | <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/ap-button.png" /> | <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/caap-button.png" /> |

## Messaging

Messaging is automatically updated if you use On-Site Messaging, our current messaging product, or its predecessor that used the JavaScript library for messaging. In both cases wait for the automatic update process to occur. Monitor your email for advance notice of this automatic update.

See the table below for an example of the changes:

| Afterpay                                                | Cash App Afterpay                                       |
| ------------------------------------------------------- | ------------------------------------------------------- |
| <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/ap-mess-2.png" /> | <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/caap-mess-1.png" /> |

The automatic Messaging update includes changes to *learn more*/lightbox asset if you use that.

If you use elements of Afterpay Messaging but not the standard Onsite Messaging Widget, then update the Afterpay elements with new Cash App Afterpay elements. See the [Brand Assets](#brand-assets) section above.

Any custom messaging updates must be reviewed by your Account Manager.

## FAQs

If you have a technical question on the migration, see our [FAQs for the Migration](/cash-app-afterpay/guides/welcome/migrate-from-afterpay-to-cash-app-afterpay/migration-fa-qs) page.
