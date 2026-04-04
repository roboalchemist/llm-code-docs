# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/sap-commerce-cloud/conversion-boosters/sign-in-with-klarna.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/salesforce-commerce-cloud/conversion-boosters/sign-in-with-klarna.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/conversion-boosters/sign-in-with-klarna.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/sap-commerce-cloud/conversion-boosters/sign-in-with-klarna.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/salesforce-commerce-cloud/conversion-boosters/sign-in-with-klarna.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/conversion-boosters/sign-in-with-klarna.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/sap-commerce-cloud/conversion-boosters/sign-in-with-klarna.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/salesforce-commerce-cloud/conversion-boosters/sign-in-with-klarna.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/conversion-boosters/sign-in-with-klarna.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/sap-commerce-cloud/conversion-boosters/sign-in-with-klarna.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/salesforce-commerce-cloud/conversion-boosters/sign-in-with-klarna.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/conversion-boosters/sign-in-with-klarna.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/sap-commerce-cloud/conversion-boosters/sign-in-with-klarna.md

# Sign in with Klarna on SAP Commerce Cloud

## The *Sign in with Klarna* feature is included in the **Klarna Add-on**, so no separate installation is necessary. However, a clean build of the package and an update of the database schema are required to generate new data models and data transfer objects (DTOs).

### Prerequisites

Before proceeding, ensure the following:

- You have the [**latest** **package**](https://github.com/klarna/SAP-Commerce-klarna-payments) updated in the `HYBRIS_HOME/bin/custom` and `HYBRIS_HOME/config` folders.
- You have access to SAP Commerce Backoffice for configuration.
- You have administrative rights to perform system updates and resets.

### Mandatory code changes

#### Update the `master.tag` file

1.  Open the file located at <hybris_home>`\bin\modules\baseaccelerator\deprecated\yacceleratorstorefront\web\webroot\WEB-INF\tags\responsive\template\master.tag`
2.  Paste the following code snippet directly below <jsp:dobody></jsp:dobody>:

``` jsp
<c:if test="${isKlarnaSignInEnabled}">
<input id="currentLocale" name="currentLocale" type="hidden" value="${currentLocale}"/>
<input id="clientId" name="clientId" type="hidden" value="${klarnaConfigData.credential.clientId}"/>
<input id="environment" name="environment" type="hidden" value="${klarnaConfigData.environment}"/>
<input id="country" name="country" type="hidden" value="${klarnaConfigData.credential.marketCountry}"/>
<input id="scopeData" name="scopeData" type="hidden" value="${klarnaConfigData.siwkConfig.scopeData}"/>
<input id="redirectUri" name="redirectUri" type="hidden" value="${klarnaConfigData.siwkConfig.redirectUri}"/>
<input id="buttonTheme" name="buttonTheme" type="hidden" value="${klarnaConfigData.siwkConfig.buttonTheme}"/>
<input id="buttonShape" name="buttonShape" type="hidden" value="${klarnaConfigData.siwkConfig.buttonShape}"/>
<input id="buttonLogoAlignment" name="buttonLogoAlignment" type="hidden" value="${klarnaConfigData.siwkConfig.buttonLogoAlignment}"/>
<input id="showInLoginPage" name="showInLoginPage" type="hidden" value="${klarnaConfigData.siwkConfig.showInLoginPage}"/>
<input id="showInRegisterPage" name="showInRegisterPage" type="hidden" value="${klarnaConfigData.siwkConfig.showInRegisterPage}"/>
<input id="showInCheckoutLoginPage" name="showInCheckoutLoginPage" type="hidden" value="${klarnaConfigData.siwkConfig.showInCheckoutLoginPage}"/>
<script defer="" src="${fn:escapeXml(scriptUrlSIWK)}"></script>
</c:if>
```

#### Update the `login.tag` file

1.  Open the file located at <hybris_home>`\bin\modules\base-accelerator\deprecated\yacceleratorstorefront\web\webroot\WEB-INF\tags\responsive\user\login.tag`
2.  Insert the following code inside the <form:form action="${action}" method="post" modelattribute="loginForm"> segment, directly below the <ycommerce:testid code="loginAndCheckoutButton"> segment:

``` jsp
<c:if test="${isKlarnaSignInEnabled}">
<br/>
<div id="klarna-signin-container" style="overflow:auto"><sec:csrfinput></sec:csrfinput>
<c:set var="signinErr"><spring:message code="klarna.signin.error"></spring:message></c:set>
<input id="signinErrHidden" type="hidden" value="${signinErr}"/>
<div id="klarna-signin-err" title="Klarna Error Message"><span></span>
<br/>
</div></div></c:if>
```

### Building and updating the database

1.  Navigate to the `HYBRIS_HOME/bin/platform` directory.
2.  Perform a clean build by running the following command: `ant clean all`
3.  Once the build completes successfully, start the server: `hybrisserver.bat`
4.  Update the system via HAC:
    - Go to **hac\> platform\> update**.
    - Check the **Update running system** and **Localize types** options.
    - And select the following extensions:
      - Klarnapayment
      - Klarnapaymentaddon
      - Klarnapaymentbackoffice

### Backoffice reset

1.  Log in to SAP Commerce Backoffice.
2.  Press `F4` to open the advanced mode menu.
3.  In the top-right dropdown menu, select **Reset All**.
4.  After the reset completes, press `F4` again to return to normal Backoffice mode.

### Activation and configuration

#### Create Sign in with Klarna configuration:

1.  Search for *Sign in with Klarna* in Backoffice.
2.  Click **Sign in with Klarna** config.
3.  Select **Create New Item** (+ icon).
4.  Fill in the following fields:
    - **Unique Identifier/Code** (Klarna client identifier from Klarna's merchant portal)
    - **Scope**: `openid`, `offline_access`, `profile_name`, `profile_email`, `profile_phone`, `profile_billing_address`
    - **Redirect URL**
    - **Placements**
    - **Theme**
    - **Button Shape**
    - **Button Alignment**

#### Map Sign in with Klarna to common configuration:

1.  Navigate to **Klarna → Klarna Common Configuration** in Backoffice.
2.  Under the **General** tab, scroll to *Sign in with Klarna Configuration*.
3.  Select the previously created configuration and click **Save**.

### Configuration fields

|  |  |  |
|----|----|----|
| **Attribute** | **Mandatory** | **Description** |
| Code | Yes | Input any name/code. This will be the internal reference used to recognize and manage Sign in with Klarna configuration within SAP Commerce. |
| Scope | `openid,` `offline_access, profile_name, profile_email, profile_phone, profile_billing_address,` `profile_country,` `payments_create_session,` `profile_national_id` | Select Scope to get the information of the user. Mandatory to select (openid , offline_access, profile_name, profile_email, profile_phone) |
| Active | Yes | Check to activate Sign in with Klarna configuration; leave unchecked for it to remain inactive. |
| Redirect URL | Yes | This is for redirection in case the storefront is accessed from mobile devices. |
| Placements | Yes | Multi select option to show the button in Login Page and Checkout Login Page. |
| Theme | No | Color theme of the Sign in with Klarna button: default/light/dark |
| Button Shape | No | Shape of the Sign in with Klarna button: Default, Rect, pill |
| Button Alignment | No | Button Logo Alignment: Left, Right, Center |

### How to test Sign in with Klarna

1.  Open a new incognito browser window.
2.  Navigate to the login page of a storefront.
3.  Click **Continue with Klarna**.
4.  Use the email and phone number provided in the [sample data](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data.md).


![Sign_in_with_Klarna_login_page_on_SAP_Commerce_Cloud.png](Sign_in_with_Klarna_login_page_on_SAP_Commerce_Cloud.png)
*Sign_in_with_Klarna_login_page_on_SAP_Commerce_Cloud.png*

### Expected outcomes

- If the account exists in Klarna and SAP Storefront, the user is logged in, and the accounts are merged automatically.
- If the account exists in Klarna but not in SAP Storefront, a consent page appears. Upon consent, the account is created in the storefront.
- If the account does not exist in Klarna, login fails, and the user can proceed with the normal login flow.</ycommerce:testid></form:form></hybris_home></hybris_home>