# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/integrating-with-cash-app-pay/comparing-mobile-web-environments.mdx

{/* internal:true */}

# Cash App Pay: Comparing Mobile/Web environments

See the following table to compare the capability of Cash App Pay in different web and mobile environments.

| Scenario / Environment      | Description                                                                                                                                                                                                                                                                             | Production \[Native App]                                                                                                                                                                                | Sandbox \[Native App]                                                                                                                                   | Sandbox \[Web App]                                                                                                                      |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| International Support       | Cash App is available in the United States and the United Kingdom. However, Cash App Pay is currently only supported in the United States.                                                                                                                                              | Only valid US Cash App accounts can take Cash App Pay payments in production.                                                                                                                           | The Sandbox web app can be used globally.                                                                                                               | The Sandbox web app can be used globally.                                                                                               |
| Requires Cash App Installed | Cash App must be downloaded on the customer's mobile device in order to authenticate a Cash App Pay payment.                                                                                                                                                                            | If Cash App is not installed, an interstitial page will be shown where the customer is prompted to install Cash App.                                                                                    | If the Sandbox native app is not installed, the Sandbox web app is used instead where the customer can approve or deny the grant flow in a web browser. | The Sandbox web app does not require an app to be downloaded; instead, the customer can approve or deny the grant flow in a web browser |
| Interstitial Page Shown     | An interstitial page is shown after the Cash App Pay button is clicked if Cash App is not installed or if there are issues deeplinking into Cash App.                                                                                                                                   | This interstitial page is currently only shown in production                                                                                                                                            | N/A - the interstitial page is not shown in Sandbox.                                                                                                    | N/A - the interstitial page is not shown in Sandbox.                                                                                    |
| Mobile Forward Redirect     | When a customer clicks the Cash App Pay button, they are deeplinked into Cash App to complete the grant flow. After the grant flow is approved or declined, the customer is either returned back to the original checkout context via either a forward redirect or a backward redirect. | In production, Cash App will attempt to backward redirect back to the original checkout context. In the scenario where this fails or for non-standard workflows, a forward redirect will occur instead. | The Sandbox native app mirrors production functionality.                                                                                                | The Sandbox web app will always initiate a forward redirect.                                                                            |
| Mobile Backward Redirect    | When a customer clicks the Cash App Pay button, they are deeplinked into Cash App to complete the grant flow. After the grant flow is approved or declined, the customer is either returned back to the original checkout context via either a forward redirect or a backward redirect. | In production, Cash App will attempt to backward redirect back to the original checkout context. In the scenario where this fails or for non-standard workflows, a forward redirect will occur instead. | The sandbox native app mirrors production functionality.                                                                                                | The Sandbox web app does not support backward redirects.                                                                                |
| Approve Grant Flow          | When a customer clicks the Cash App Pay button, they are deeplinked into Cash App to complete the grant flow. If the grant flow is approved, a grant is generated which can be used to authorize a payment.                                                                             | In production, Cash App will automatically approve or decline the payment request without requiring any user action.                                                                                    | In Sandbox, the customer is able to manually approve or decline the payment request.                                                                    | In Sandbox, the customer is able to manually approve or decline the payment request.                                                    |
| Decline Grant Flow          | When a customer clicks the Cash App Pay button, they are deeplinked into Cash App to complete the grant flow. If the grant flow is declined, a grant is NOT generated.                                                                                                                  | In production, Cash App will automatically approve or decline the payment request without requiring any user action.                                                                                    | In Sandbox, the customer is able to manually approve or decline the payment request.                                                                    | In sandbox, the customer is able to manually approve or decline the payment request.                                                    |

{/*

# Cash App Pay: Comparing Mobile/Web environments

We have created the following tables for you to compare the capability of Cash App Pay in different web and mobile environments.
## Cash App

This table describes the behavior of Cash App Pay, in our mobile application Cash App, based on different use cases:

|Use case|Description|
| ----------- | -------- |
| International Support      | Cash App is available in the United States and the United Kingdom. However, Cash App Pay is currently only supported in the United States. |
|Requires Cash App Installed | Cash App must be downloaded on the customer's mobile device to authenticate a Cash App Pay payment. | 
|Interstitial Page Shown | An interstitial page is shown after the Cash App Pay button is clicked if Cash App is not installed or if there are issues deeplinking into Cash App. |
|Mobile Forward Redirect | When a customer clicks the Cash App Pay button, they are deeplinked into Cash App to complete the grant flow. After the grant flow has been approved or declined, the customer is either returned back to the original checkout context via either a forward redirect or a backward redirect. |
|Mobile Backward Redirect | When a customer clicks the Cash App Pay button, they are deeplinked into Cash App to complete the grant flow. After the grant flow has been approved or declined, the customer is either returned back to the original checkout context via either a forward redirect or a backward redirect. |
|Approve Grant Flow | When a customer clicks the Cash App Pay button, they are deeplinked into Cash App to complete the grant flow. If the grant flow is approved, a grant is generated which can be used to authorize a payment. | 
|Decline Grant Flow | When a customer clicks the Cash App Pay button, they are deeplinked into Cash App to complete the grant flow. If the grant flow is declined, a grant is NOT generated. |

 

## Production [Native App]

This table describes the behavior of Cash App Pay within the Production environment based on different use cases: 
|Use case|Description|
| ----------- | -------- |
 | International Support  | Only valid US Cash App accounts can take Cash App Pay payments in production. |    
 | Requires Cash App Installed |If Cash App is not installed, an interstitial page will be shown where the customer is prompted to install Cash App. | 
 | Interstitial Page Shown |This interstitial page is currently only shown in production |
 | Mobile Forward Redirect |  In production, Cash App will attempt to backward redirect back to the original checkout context. In the scenario where this fails or for non-standard workflows, a forward redirect will occur instead. |
 | Mobile Backward Redirect |  In production, Cash App will attempt to backward redirect back to the original checkout context. In the scenario where this fails or for non-standard workflows, a forward redirect will occur instead. |
 | Approve Grant Flow |   In production, Cash App will automatically approve or decline the payment request without requiring any user action. | 
 | Decline Grant Flow |In production, Cash App will automatically approve or decline the payment request without requiring any user action. |




## Sandbox [Native App] 

This table describes the behavior of Cash App Pay within the Sandbox App mobile environment based on different use cases: 
|Use case|Description|
| ----------- | -------- |
 | International Support| The sandbox web app can be used globally.    |      
 | Requires Cash App Installed | If the sandbox native app is not installed, the sandbox web app is used instead where the customer can approve or deny the grant flow in a web browser. |
 | Interstitial Page Shown | N/A - the interstitial page is not shown in sandbox. | 
 | Mobile Forward Redirect |The sandbox native app mirrors production functionality. |
 | Mobile Backward Redirect | In production, Cash App will attempt to backward redirect back to the original checkout context. In the scenario where this fails or for non-standard workflows, a forward redirect will occur instead. |  
 | Approve Grant Flow |In sandbox, the customer is able to manually approve or decline the payment request. | 
 | Decline Grant Flow |In sandbox, the customer is able to manually approve or decline the payment request. |




## Sandbox [Web App]  

This table describes the behavior of Cash App Pay within the Sandbox App web environment based on different use cases:

|Use case|Description|
| ----------- | -------- |
  | International Support   | The sandbox web app can be used globally.  |   
  | Requires Cash App Installed |The sandbox web app does not require an app to be downloaded; instead, the customer can approve or deny the grant flow in a web browser |
  | Interstitial Page Shown | N/A - the interstitial page is not shown in sandbox. |
  | Mobile Forward Redirect |The sandbox web app always initiates a foward redirect. |
  | Mobile Backward Redirect |he sandbox web app does not support backward redirects. | 
  | Approve Grant Flow |In sandbox, the customer is able to manually approve or decline the payment request. |
  | Decline Grant Flow |In sandbox, the customer is able to manually approve or decline the payment request. |

      
*/}

{/*
<table>
<tbody>
  <tr>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td>International Support</td>
    <td>Requires Cash App Installed</td>
    <td>Interstitial Page Shown</td>
    <td>Mobile Forward Redirect</td>
    <td>Mobile Backward Redirect</td>
    <td>Approve Grant Flow</td>
    <td>Decline Grant Flow</td>
  </tr>
  <tr>
    <td colspan="2">DESCRIPTION</td>
    <td>Cash App is available in the United States and the United Kingdom. However, Cash App Pay is currently only supported in the United States. </td>
    <td>Cash App must be downloaded on the customer's mobile device in order to authenticate a Cash App Pay payment. </td>
    <td>An interstitial page is shown after the Cash App Pay button is clicked if Cash App is not installed or if there are issues deeplinking into Cash App.</td>
    <td>When a customer clicks the Cash App Pay button, they are deeplinked into Cash App to complete the grant flow. After the grant flow has been approved or declined, the customer is either returned back to the original checkout context via either a forward redirect or a backward redirect.</td>
    <td>When a customer clicks the Cash App Pay button, they are deeplinked into Cash App to complete the grant flow. After the grant flow has been approved or declined, the customer is either returned back to the original checkout context via either a forward redirect or a backward redirect.</td>
    <td>When a customer clicks the Cash App Pay button, they are deeplinked into Cash App to complete the grant flow. If the grant flow is approved, a grant is generated which can be used to authorize a payment.</td>
    <td>When a customer clicks the Cash App Pay button, they are deeplinked into Cash App to complete the grant flow. If the grant flow is declined, a grant is NOT generated.</td>
  </tr>
  <tr>
    <td colspan="2">Production [Native App]</td>
    <td>Only valid US Cash App accounts can take Cash App Pay payments in production.</td>
    <td>If Cash App is not installed, an interstitial page will be shown where the customer is prompted to install Cash App.</td>
    <td>This interstitial page is currently only shown in production</td>
    <td>In production, Cash App will attempt to backward redirect back to the original checkout context. In the scenario where this fails or for non-standard workflows, a forward redirect will occur instead.</td>
    <td>In production, Cash App will attempt to backward redirect back to the original checkout context. In the scenario where this fails or for non-standard workflows, a forward redirect will occur instead.</td>
    <td>In production, Cash App will automatically approve or decline the payment request without requiring any user action.</td>
    <td>In production, Cash App will automatically approve or decline the payment request without requiring any user action.</td>
  </tr>
  <tr>
    <td colspan="2">Sandbox [Native App]</td>
    <td>The sandbox web app can be used globally.</td>
    <td>If the sandbox native app is not installed, the sandbox web app is used instead where the customer can approve or deny the grant flow in a web browser.</td>
    <td>N/A - the interstitial page is not shown in sandbox.</td>
    <td>The sandbox native app mirrors production functionality.</td>
    <td>In production, Cash App will attempt to backward redirect back to the original checkout context. In the scenario where this fails or for non-standard workflows, a forward redirect will occur instead.</td>
    <td>In sandbox, the customer is able to manually approve or decline the payment request.</td>
    <td>In sandbox, the customer is able to manually approve or decline the payment request.</td>
  </tr>
  <tr>
    <td colspan="2">Sandbox [Web App]</td>
    <td>The sandbox web app can be used globally.</td>
    <td>The sandbox web app does not require an app to be downloaded; instead, the customer can approve or deny the grant flow in a web browser</td>
    <td>N/A - the interstitial page is not shown in sandbox.</td>
    <td>The sandbox web app always initiates a foward redirect.</td>
    <td>The sandbox web app does not support backward redirects.</td>
    <td>In sandbox, the customer is able to manually approve or decline the payment request.</td>
    <td>In sandbox, the customer is able to manually approve or decline the payment request.</td>
  </tr>
</tbody>
</table>
*/}
