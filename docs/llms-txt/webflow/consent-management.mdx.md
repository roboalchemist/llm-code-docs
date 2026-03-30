# Source: https://developers.webflow.com/browser/reference/consent-management.mdx

***

title: Site Tracking and Consent Management
slug: reference/consent-management
description: >-
Manage user tracking consent for Webflow Analyze and Optimize using the
Browser API
hidden: false
'og:title': Site Tracking and Consent Management
'og:description': >-
Manage user tracking consent for Webflow Analyze and Optimize using the
Browser API
subtitle: Create a consent management flow for Webflow Analyze and Optimize
---------------------------------------------------------------------------

Use Webflow's Browser APIs to manage user tracking consent for [Analyze](http://webflow.com/analyze) and [Optimize](http://webflow.com/optimize). Check consent status, control tracking, and integrate with your consent management platform—or build your own custom solution.

<Note title="Analyze or Optimize required">
  These consent management endpoints apply only to Webflow Analyze and Optimize features.
  If you are not using Analyze or Optimize, you cannot use these endpoints and must set up your own consent management banner or platform.
</Note>

## Site tracking

Webflow's [Site tracking](https://help.webflow.com/hc/en-us/articles/33620965657107-Analyze-Optimize-tracking-settings) lets you record analytics, personalize experiences, and run AI-powered tests using Analyze and Optimize. Site tracking must be enabled to use the consent management APIs.

Privacy laws like GDPR and CCPA may require you to obtain visitor consent before tracking, depending on your site’s location and audience. It’s your responsibility to determine which requirements apply to your site. Webflow’s APIs provide the tools you need to implement consent flows for data tracking as needed. [Learn more about compliance requirements](https://help.webflow.com/hc/en-us/articles/34273101581715-Analyze-Optimize-compliance-with-privacy-laws).

## Consent management

A consent management solution lets visitors choose how their data is collected. Typically shown as a banner or menu, it allows users to opt in or out of tracking. Using a consent management solution helps you inform visitors and manage their preferences.

### Consent management apps in the Webflow Marketplace

Webflow offers third-party apps for consent management in the [Webflow Marketplace](https://webflow.com/apps/compliance). These apps help you set up and manage consent workflows without writing code. Additionally, Webflow provides detailed setup guides for the [DataGrail](https://help.webflow.com/hc/en-us/articles/34394688342035) and [Finsweet](https://help.webflow.com/hc/en-us/articles/34394790067859-Integrate-Finsweet-Components-Cookie-Consent-for-consent-management) apps.

### Consent Management using Webflow's APIs

Webflow's Browser APIs let you check a user's tracking preferences and manage consent directly. Use these APIs to build a custom consent management solution tailored to your site and user experience. This approach is ideal for:

* Site owners who need to manage consent themselves
* Developers integrating with existing Consent Management Platforms (CMPs)
* Teams requiring specific customization of the consent experience

## Consent management APIs

The following APIs are available in the Webflow Browser API:

* [Get consent status:](/browser/reference/get-user-tracking-choice) Returns the user's current consent state
* [Allow User Tracking:](/browser/reference/allow-user-tracking) Opts users into Webflow's tracking
* [Deny User Tracking:](/browser/reference/deny-user-tracking) Opts users out of Webflow's tracking

### Integrating with existing consent management platforms

If you already use a consent management platform like OneTrust or TrustArc, you can add [a custom code snippet](https://help.webflow.com/hc/en-us/articles/33961357265299-Custom-code-in-head-and-body-tags) using the consent management APIs in the header of your site to pass user consent choices to Webflow. The following examples show how to detect user consent choices in your consent management platform and update Webflow's tracking preferences in real time.

{/* <!-- vale off --> */}

<Tabs>
  <Tab title="General">
    To respect user consent, detect the visitor's choice in your consent management platform and update Webflow's tracking preferences with the appropriate API call. Most platforms provide a callback or event when consent changes—use this to trigger the `allowUserTracking` or `denyUserTracking` API calls.

    ```javascript
    <Script>
    wf.ready(() => {
       // First, detect the current state
       const isOptedOut = wf.getUserTrackingChoice() === 'deny';
       if (isOptedOut) {
          //
          // Your Consent Management Platform logic to detect an optIn signal goes here
          //
          // Then you call Webflow to let us know there's been an optIn
          wf.allowUserTracking();
       }
       else {
          //
          // Your Consent Management Platform logic to detect an optOut signal goes here
          //
          // Then you call Webflow to let us know there's been an optOut
          wf.denyUserTracking();
       }
    });
    </Script>
    ```
  </Tab>

  <Tab title="OneTrust">
    If you use OneTrust, the following code sample can help your team get started. It checks the OneTrust consent cookie and calls the Webflow Consent Management APIs accordingly.

    ```javascript
    <Script>
    wf.ready(() => {
    // Function to opt in or out based on consent preferences
    const handleWebflowAnalyticsConsent = () => {
       try {
          // Logic to check consent groups from the OneTrust cookie
          const otCookieKey = 'OptanonConsent=';
          const otCookie = document.cookie.split('; ').find(row => row.startsWith(otCookieKey));
          if (!otCookie) {
          throw new Error('OneTrust cookie not found.');
          }
          const otGroupsKey = 'groups=';
          const otGroups = decodeURIComponent(otCookie.split('&').find(row => row.startsWith(otGroupsKey)).split('=')[1]);
          // OneTrust groups: 1 = necessary, 2 = performance, 3 = functional, 4 = targeting
          const OT_FUNCTIONAL_CONSENT = '3:1'; // Ensure this matches your expected consent group
          // Check for functional cookies group
          const hasOptedIn = otGroups.indexOf(OT_FUNCTIONAL_CONSENT) !== -1;
          // Adjust Webflow Analytics opt-in/out based on consent
          if (hasOptedIn) {
          wf.allowUserTracking();
          } else {
          wf.denyUserTracking();
          }
       } catch (e) {
          console.error('Error handling OneTrust consent:', e);
       }
    };
    // Set up the OneTrust consent change listener to check when preferences change
    if (typeof OneTrust !== 'undefined' && OneTrust.OnConsentChanged) {
       OneTrust.OnConsentChanged(() => {
          handleWebflowAnalyticsConsent();
       });
    }
    // Initial check when the page loads
    handleWebflowAnalyticsConsent();
    });
    </Script>
    ```

    <Warning>
      This code sample is provided as-is and isn't supported by Webflow. Your team should customize it for your deployment of OneTrust, including which OneTrust group you check per your policy.
    </Warning>
  </Tab>

  <Tab title="TrustArc">
    If you use TrustArc, the following code sample can help your team get started. It checks the TrustArc consent preferences and calls the Webflow Consent Management APIs accordingly.

    ```javascript
    <Script>
    wf.ready(() => {
    try {
       // Logic to check consent preferences from TrustArc
       const ta_gdpr_prefs = JSON.parse(localStorage.getItem('truste.cookie.notice_gdpr_prefs')).value;
       // TrustArc levels: 0 = required, 1 = functional, 2 = advertising
       const TA_FUNCTIONAL = 1; // Ensure this matches your expected consent group
       // Check for functional cookies group
       const hasOptedIn = ta_gdpr_prefs.indexOf(TA_FUNCTIONAL) >= 0;
       // Adjust Webflow Analytics opt-in/out based on consent
       if (hasOptedIn) {
          wf.allowUserTracking();
       } else {
          wf.denyUserTracking();
       }
    } catch (e) {
       console.error('Error handling TrustArc consent:', e);
    }
    });
    </Script>
    ```

    <Warning>
      This code sample is provided as-is and isn't supported by Webflow. Your team should customize it for your deployment of TrustArc, including which TrustArc level you check per your policy.
    </Warning>
  </Tab>
</Tabs>

{/* <!-- vale on --> */}

### Create your own consent management solution

If you don't use a consent management platform, you can build your own with Webflow's APIs. The following examples show how to add a cookie consent modal to your site and manage user consent.

1. **Add the modal in the Webflow Designer:**<br />
   This code will add a cookie consent modal to a page on your site.
   * Copy the "Designer API Example" code below
   * Open the [Designer API Playground](https://webflow.com/oauth/authorize?response_type=code\&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62\&workspace=webflow-developers-b51a9d)
   * Paste the code into the Playground and run it to add the banner to your page.
   * Optional: To ensure the modal is displayed on every page, you can [convert it into a component](https://help.webflow.com/hc/en-us/articles/33961303934611-Components-overview) and add it to all pages on your site.

2. **Enable consent logic with custom code:** <br />
   This code will connect the modal buttons to Webflow's consent APIs, so clicking "Accept" or "Decline" updates the user's consent status. It also uses GSAP to animate the modal in and out.
   * Copy the "Custom Code Example" code below
   * In your Webflow project, go to your site settings
   * Paste the code into the Header section
   * [Enable GSAP](https://help.webflow.com/hc/en-us/articles/40538857574419-Getting-started-with-GSAP-in-Webflow) in your site settings
   * Publish your site and interact with the modal.

3. **Check consent status in your browser:**<br />
   You can see the current consent status using your browser's Developer Tools.
   * Open your website in a browser (such as Chrome).
   * Right-click anywhere on the page and select **Inspect** to open Developer Tools.
   * Click the **Console** tab at the top of the Developer Tools panel.
   * Paste and run the following command to display the consent status.

     ```javascript
     wf.getUserTrackingChoice();
     ```

<CodeBlocks>
  ```javascript title="Designer API Example" maxLines={15}
  // Webflow Designer API: Cookie Consent Banner Example
  // Paste and run this code in the Designer API Playground

  // 1. Create styles
  const popupStyle = await webflow.createStyle('popupWrapper');
  await popupStyle.setProperties({
      'position': 'fixed',
      'bottom': '2rem',
      'left': '0',
      'right': '0',
      'margin-left': 'auto',
      'margin-right': 'auto',
      'max-width': '420px',
      'z-index': '9999',
      'background-color': '#fff',
      'border-radius': '1rem',
      'box-shadow': '0 4px 24px rgba(0,0,0,0.12)',
      'padding-top': '1.5rem',
      'padding-bottom': '1.5rem',
      'padding-left': '1.5rem',
      'padding-right': '1.5rem',
      'display': 'flex',
      'flex-direction': 'column',
      'align-items': 'flex-start',
      'column-gap': '1rem'
    });

  const buttonStyle = await webflow.createStyle('consentButton');
  await buttonStyle.setProperties({
    'border-radius': '0.5rem',
    'padding-top': '0.5rem',
    'padding-bottom': '0.5rem',
    'padding-left': '1.25rem',
    'padding-right': '1.25rem',
    'font-weight': '500',
    'cursor': 'pointer',
    'border-width': '0px',
    'outline-style': 'none',
    'transition-property': 'background-color,color',
    'transition-duration': '0.2s',
    'transition-timing-function': 'ease-in-out'
  });

  const acceptStyle = await webflow.createStyle('acceptButton');
  await acceptStyle.setProperties({
    'background-color': '#2563eb',
    'color': '#fff'
  });

  // Accept button hover
  await acceptStyle.setProperties({
    'background-color': '#1749b1',
    'color': '#fff'
  }, { pseudo: 'hover' });

  // Accept button pressed/active
  await acceptStyle.setProperties({
    'background-color': '#11306e',
    'color': '#fff'
  }, { pseudo: 'active' });

  const declineStyle = await webflow.createStyle('declineButton');
  await declineStyle.setProperties({
    'background-color': '#f3f4f6',
    'color': '#222'
  });

  // Decline button hover
  await declineStyle.setProperties({
    'background-color': '#e5e7eb',
    'color': '#111827'
  }, { pseudo: 'hover' });

  // Decline button pressed/active
  await declineStyle.setProperties({
    'background-color': '#d1d5db',
    'color': '#111827'
  }, { pseudo: 'active' });

  const buttonRowStyle = await webflow.createStyle('buttonRow');
  await buttonRowStyle.setProperties({
    'display': 'flex',
    'column-gap': '0.75rem',
    'margin-top': '0.5rem'
  });

  const contentDivStyle = await webflow.createStyle('contentDiv');
  await contentDivStyle.setProperties({
    'display': 'flex',
    'flex-direction': 'column',
    'column-gap': '0.5rem'
  });

  const titleStyle = await webflow.createStyle('bannerTitle');
  await titleStyle.setProperties({
    'font-weight': '600',
    'font-size': '1.1rem'
  });

  const messageStyle = await webflow.createStyle('bannerMessage');
  await messageStyle.setProperties({
    'font-size': '0.98rem',
    'color': '#444'
  });

  const linkStyle = await webflow.createStyle('learnMoreLink');
  await linkStyle.setProperties({
    'color': '#2563eb',
    'text-decoration': 'underline'
  });

  // 2. Get the parent element (or use body)
  const parent = await webflow.getSelectedElement();

  // 3. Build the popup wrapper
  const popup = webflow.elementBuilder(webflow.elementPresets.DOM);
  popup.setTag('div');
  popup.setAttribute('id', 'consentPopup');
  popup.setStyles([popupStyle]);

  // 4. Banner content
  const contentDiv = popup.append(webflow.elementPresets.DOM);
  contentDiv.setTag('div');
  contentDiv.setStyles([contentDivStyle]);

  const title = contentDiv.append(webflow.elementPresets.DOM);
  title.setTag('span');
  title.setTextContent('We use cookies');
  title.setStyles([titleStyle]);

  const message = contentDiv.append(webflow.elementPresets.DOM);
  message.setTag('span');
  message.setStyles([messageStyle]);
  message.setTextContent('This site uses cookies to analyze traffic and enhance your experience. ');

  const learnMore = message.append(webflow.elementPresets.DOM);
  learnMore.setTag('a');
  learnMore.setAttribute('href', '/privacy-policy');
  learnMore.setAttribute('target', '_blank');
  learnMore.setAttribute('rel', 'noopener');
  learnMore.setStyles([linkStyle]);
  learnMore.setTextContent('Learn more');

  // 5. Button row
  const buttonRow = popup.append(webflow.elementPresets.DOM);
  buttonRow.setTag('div');
  buttonRow.setStyles([buttonRowStyle]);

  // Accept button
  const acceptBtn = buttonRow.append(webflow.elementPresets.DOM);
  acceptBtn.setTag('button');
  acceptBtn.setAttribute('id', 'optIn');
  acceptBtn.setAttribute('class', 'consentButton');
  acceptBtn.setStyles([buttonStyle, acceptStyle]);
  acceptBtn.setTextContent('Accept');

  // Decline button
  const declineBtn = buttonRow.append(webflow.elementPresets.DOM);
  declineBtn.setTag('button');
  declineBtn.setAttribute('id', 'optOut');
  declineBtn.setAttribute('class', 'consentButton');
  declineBtn.setStyles([buttonStyle, declineStyle]);
  declineBtn.setTextContent('Decline');

  // 6. Add the popup to the page
  if (parent?.children) {
    await parent.append(popup);
    console.log('Cookie consent banner created!');
  }
  ```

  ```javascript title="Custom Code Example" maxLines={15}
  <Script>
  // Cookie Consent Logic with GSAP and Webflow Browser APIs
  // Paste as Custom Code in the <head> tag of your page or site

  // Wait for Webflow Browser APIs to be ready
  wf.ready(() => {
  console.log("Hello World")
    const popup = document.getElementById('consentPopup');
    const acceptBtn = document.getElementById('optIn');
    const declineBtn = document.getElementById('optOut');

    // Helper: Animate in
    function showBanner() {
      gsap.set(popup, { y: 40, opacity: 0, display: 'flex' });
      gsap.to(popup, { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' });
    }

    // Helper: Animate out
    function hideBanner() {
      gsap.to(popup, {
        y: 40,
        opacity: 0,
        duration: 0.5,
        ease: 'power3.in',
        onComplete: () => {
          popup.style.display = 'none';
        }
      });
    }

    // Check consent state
    const choice = wf.getUserTrackingChoice();
    if (choice === 'allow' || choice === 'deny') {
      popup.style.display = 'none';
    } else {
      showBanner();
    }

    // Accept: allow tracking, animate out
    acceptBtn.addEventListener('click', () => {
      wf.allowUserTracking({ activate: true });
      hideBanner();
    });

    // Decline: deny tracking, animate out
    declineBtn.addEventListener('click', () => {
      wf.denyUserTracking();
      hideBanner();
    });
  });
  </Script>
  ```
</CodeBlocks>

<Warning>
  This example is intended as a starting point and may not fully comply with all privacy laws. Customize and validate your consent management implementation to ensure it aligns with your site's privacy policy and the legal requirements applicable to your visitors.
</Warning>
