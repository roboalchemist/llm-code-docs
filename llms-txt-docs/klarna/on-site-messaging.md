# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/sap-commerce-cloud/conversion-boosters/on-site-messaging.md

# On-Site Messaging on SAP Commerce Cloud

## This guide provides step-by-step instructions to install and configure the Klarna On-Site Messaging (KOSM) add-on for SAP Commerce.

### Installation Steps

#### Step 1: Unpack the add-on

Extract the archive and place the `klarnaosmaddon` and `klarnaosmbackoffice` folders into the `custom` folder of the SAP Commerce Suite:

``` javascript
<hybris_home>/bin/custom
```

#### Step 2: Update `localextensions.xml`

- **Verify Add-on Support:** Ensure the following extension is present:

``` xml
<extension name="addonsupport"></extension>
```

- **Add Klarna Extensions:** Add the following entries to `localextensions.xml`

``` xml
<extension name="klarnaosmaddon"></extension>
<extension name="klarnaosmbackoffice"></extension>
```

- **Check Target Storefront Extension:** Confirm that the correct storefront extension is referenced.

#### Step 3.: Stop the SAP Commerce server

Stop the server by using one of the following methods based on your setup:

- **Embedded Mode:** Press `Ctrl+C`.
- **Service Mode:**
  - Windows: Run `hybrisserver.bat stop`.
  - Unix: Run `./hybrisserver.sh stop`.

#### Step 4: Set up the environment

Run the environment setup script; navigate to <hybris_home>`/bin/platform` and execute:

- Windows: `setantenv.bat`
- Unix: `./setantenv.sh`

#### Step 5: Install the add-on

Run the installation command:

``` bash
ant addoninstall -Daddonnames="klarnaosmaddon" -DaddonStorefront.yacceleratorstorefront="yacceleratorstorefront"
```

**Note:** Replace `yacceleratorstorefront` with your project-specific storefront name.

#### Step 6: Configure Klarna URLs and tags

Set up script URLs and tags. In the SAP Commerce Backoffice, configure the following for both playground and production environments:

- **Script (Library) URL**: URL for Klarna's JavaScript library.
- **UCI (Unique Client ID)**: Merchant identifier provided by Klarna (`data-client-id`), you can find this in Merchant portal.
- **Country**: The target country for Klarna On-Site Messaging.
- **Placement Tag IDs**: Unique identifiers for each placement location (e.g., product page, cart page).

#### Step 7: Modify code for KOSM integration

**Update the Master Tag:** Modify the master tag to include:

``` jsp
<c:if test="${osmConfigData.active == true}">
<script async="" data-client-id="${uci}" src="${scriptUrlKOSM}"></script>
</c:if>
```

**Update the PDP Page:** Modify `productPricePanel.tag` .

- Add the tag library.

``` jsp
<%@ taglib prefix="osm" tagdir="/WEB-INF/tags/addons/klarnaosmaddon/responsive/osm/" %>
```

- <span>Add `osmproduct` tag.</span>

``` jsp
<osm:osmproduct price="${product.price.value}"></osm:osmproduct>
```

- Make sure to include the osm tag at the end.

``` jsp
<osm:osm></osm:osm>
```

**Modify the cart page:** For the cart page, update c`artTotals.tag` as follows:

- Set the final price based on the tax setting

``` jsp
<div class="col-xs-6 cart-totals-right text-right grand-total">
<ycommerce:testid code="cart_totalPrice_label">
<c:choose>
<c:when test="${showTax}">
<c:set value="${cartData.totalPriceWithTax}" var="finalPrice"></c:set>
<format:price pricedata="${cartData.totalPriceWithTax}"></format:price>
</c:when>
<c:otherwise>
<c:set value="${cartData.totalPrice}" var="finalPrice"></c:set>
<format:price pricedata="${cartData.totalPrice}"></format:price>
</c:otherwise>
</c:choose>
</ycommerce:testid>
```

- Include the cart tag:

``` jsp
<osm:osmcart price="${finalPrice.value}"></osm:osmcart>
```

#### Step 8: Rebuild the system

Rebuild the system by running the following command: `ant clean all`

#### Step 9: Update the system

1.  **Perform a full initialization (if this is the first installation):** Use the Hybris Administration Console (HAC).
2.  **Update the system:**
    - Open a browser and go to **HAC → Platform → Update**.
    - Under **General Settings**, select:
      - Update running system
      - Localize types
    - Under **Project Data Settings**, check:
      - `klarnaosmaddon`
      - `klarnaosmbackoffice`
    - Click **Update**.

### Configuration

#### Create a Klarna OSM configuration

**Log in to Backoffice**

1.  Open a web browser and navigate to the SAP Commerce Backoffice login page.
2.  Log in with your administrator account credentials.

**Navigate to Klarna On-Site Messaging** In Backoffice, go to **Klarna**\> **Klarna On-Site Messaging**.


![Backoffice navigation to OSM in SAP](Draft:On-Site_Messaging_on_SAP_Commerce_Cloud_1737650537250.png)
*Backoffice navigation to OSM in SAP*

**Create a new configuration** Click **Create** to add a new Klarna On-Site Messaging configuration.


![Creating a new OSM configuration in SAP](Draft:On-Site_Messaging_on_SAP_Commerce_Cloud_1737650600909.png)
*Creating a new OSM configuration in SAP*

**Fill in configuration details** Enter the required values for configuring On-Site Messaging.


![Draft:On-Site_Messaging_on_SAP_Commerce_Cloud_1737650790324.png](Draft:On-Site_Messaging_on_SAP_Commerce_Cloud_1737650790324.png)
*Draft:On-Site_Messaging_on_SAP_Commerce_Cloud_1737650790324.png*

**Save the configuration** Click **Done** to save your configuration.

### Map KOSM to common configuration, credentials, and base store

**Navigate to Klarna Common Configuration**

1.  In Backoffice, go to **Klarna**\> **Klarna Common Configuration**.
2.  Double-click the Klarna Common Configuration entry to open it for editing.


![Draft:On-Site_Messaging_on_SAP_Commerce_Cloud_1737650823342.png](Draft:On-Site_Messaging_on_SAP_Commerce_Cloud_1737650823342.png)
*Draft:On-Site_Messaging_on_SAP_Commerce_Cloud_1737650823342.png*

**Assign base store**

1.  Go to the **General** tab.
2.  In the **Essentials** section, select the relevant base stores where the Klarna On-Site Messaging should appear.


![Credentials settings in SAP](Draft:On-Site_Messaging_on_SAP_Commerce_Cloud_1737650956438.png)
*Credentials settings in SAP*

**Assign credentials**

1.  In the **Klarna Credentials** section, select the appropriate credentials to use with the Klarna On-Site Messaging configuration.
2.  If needed, click **+ Create Klarna Activation** to create new credentials.


![Klarna Activation in SAP](Draft:On-Site_Messaging_on_SAP_Commerce_Cloud_1737650992530.png)
*Klarna Activation in SAP*

**Assign the Klarna On-Site Messaging configuration** In the **Klarna On-Site Messaging Configuration** section, select the newly created OSM configuration.


![Klarna OSM configuration in SAP](Draft:On-Site_Messaging_on_SAP_Commerce_Cloud_1737651023864.png)
*Klarna OSM configuration in SAP*

**Save changes** Click **Save** to apply your changes to the Klarna Common Configuration.

### <span>Configuration Fields</span>
<table>
<thead>
<tr>
<th><p><strong>Attribute</strong></p></th>
<th><p><strong>Mandatory</strong></p></th>
<th><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><strong>Code</strong></p></td>
<td><p>Yes</p></td>
<td><p>Provide a unique name or code to identify this Klarna OSM configuration internally within SAP Commerce.</p></td>
</tr>
<tr>
<td><p><strong>Active</strong></p></td>
<td><p>Yes</p></td>
<td><p>Check this option to activate the configuration. Leave unchecked to keep it inactive.</p></td>
</tr>
<tr>
<td><p><strong>Client Id</strong></p></td>
<td><p>Yes</p></td>
<td><p>Enter the UCI value retrieved from the Klarna Merchant Portal (data-client-id). This can be configured under <strong>Klarna</strong>> <strong>Klarna Activation</strong>.</p></td>
</tr>
<tr>
<td><p><strong>Placements</strong></p></td>
<td><p>Yes</p></td>
<td><p>Choose multiple placement options (e.g., Cart or PDP) where the Klarna On-Site Messaging should appear.</p></td>
</tr>
<tr>
<td><p><strong>Theme</strong></p></td>
<td><p>Yes</p></td>
<td><p>Select a theme from the dropdown for the Cart Page or PDP. If custom styling is configured in the Klarna Merchant Portal, choose the custom option.</p></td>
</tr>
<tr>
<td><p><strong>Custom Style</strong></p></td>
<td><p>No</p></td>
<td><p>Add custom styles to OSM elements using the ::part API. Use a <code></code></p>
<style>
<p></code> tag to define the custom style. Example: ​<code></p>
<style type='text/css'>
<p></code> <code>#osm-product-strip::part(osm-container) {    background-color: #d9b259; }</code> <code>#osm-product-strip::part(osm-cta) {    font-size: 14px;  }  </code> <code>#osm-cart-strip::part(osm-container) {    background-color: #d4d122; }</code> <code></p>
</style>
<p></p></td>
</tr>
</tbody>
</table></div></hybris_home></hybris_home>