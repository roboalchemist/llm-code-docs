# Source: https://docs.logrocket.com/reference/apple-privacy-questionnaire.md

# Apple Privacy Questionnaire

When utilizing the LogRocket Mobile SDK in your iOS Application it will be necessary to answer Apple's Privacy Questionnaire for application submissions. This article presents a guide for how to answer this questionnaire with the LogRocket Mobile SDK installed.

> 📘
>
> The recommended responses provided in this article only accounts for general usage of our Mobile SDK for iOS. Data your application collects and other third-party SDKs are not covered by this article.

For more detailed information on the questionnaire review [Apple's documentation on the topic](https://developer.apple.com/app-store/app-privacy-details).

Any content captured for our replay tool (presented on the screen or in network requests) should be taken into consideration when completing the questionnaire.

<HTMLBlock>
  {`
  <style>
  .privacy-table, .privacy-table tr, .privacy-table td, .privacy-table th {
    border: 1px solid #764abc;
    border-collapse: collapse;
  }
  .privacy-table th {
    padding: 0.5rem;
    text-align: left;
    white-space: nowrap;
    color: #764abc;
    background-color: rgb(241, 237, 248);
  }
  .privacy-table th:first-child {
    font-size: 1.2rem;
  }
  .privacy-table th:last-child {
    font-size: .8rem;
  }
  .privacy-table th[colspan="2"] {
    font-size: 1rem;
  }
  .privacy-table td {
    padding: 0.5rem;
  }
  </style>

  <table class="privacy-table">
    <tr>
      <th>Data Collection Questions</th>
      <th>Recommended Response</th>
    </tr>
    <tr>
      <td>Do you or your third-party partners collect data from this app?</td>
      <td><strong>Yes,</strong> we collect data from this app</td>
    </tr>
    <tr>
      <th>Types of Data Collected</th>
      <th>Recommended Response</th>
    </tr>
    <tr>
      <th colspan="2">Contact Info</th>
    </tr>
    <tr>
      <td>Name</td>
      <td>✓ (if Identifying Users)</td>
    </tr>
    <tr>
      <td>Email Address</td>
      <td>✓ (if Identifying Users)</td>
    </tr>
    <tr>
      <td>Phone Number</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Physical Address</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Other User Contact Info</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Health &amp; Fitness</th>
    </tr>
    <tr>
      <td>Health</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Fitness</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Financial Info</th>
    </tr>
    <tr>
      <td>Payment Info</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Credit Info</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Other Financial Info</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Location</th>
    </tr>
    <tr>
      <td>Precise Location</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Coarse Location</td>
      <td>✓ [1]</td>
    </tr>
    <tr>
      <th colspan="2">Sensitive Info</th>
    </tr>
    <tr>
      <td>Sensitive Info</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Contacts</th>
    </tr>
    <tr>
      <td>Contacts</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">User Content</th>
    </tr>
    <tr>
      <td>Emails or Text Messages</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Photos or Videos</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Audio Data</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Gameplay Content</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Customer Support</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Other User Content</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Browsing History</th>
    </tr>
    <tr>
      <td>Browsing History</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Search History</th>
    </tr>
    <tr>
      <td>Search History</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Identifiers</th>
    </tr>
    <tr>
      <td>User ID</td>
      <td>✓ (if Identifying Users)</td>
    </tr>
    <tr>
      <td>Device ID</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Purchases</th>
    </tr>
    <tr>
      <td>Purchase History</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Usage Data</th>
    </tr>
    <tr>
      <td>Product Interaction</td>
      <td>✓</td>
    </tr>
    <tr>
      <td>Advertising Data</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Other Usage Data</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Diagnostics</th>
    </tr>
    <tr>
      <td>Crash Data</td>
      <td>✓</td>
    </tr>
    <tr>
      <td>Performance Data</td>
      <td>✓</td>
    </tr>
    <tr>
      <td>Other Diagnostic Data</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Other Data</th>
    </tr>
    <tr>
      <td>Other Data Types</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th>Product Interaction Usage Questions</th>
      <th>Recommended Response</th>
    </tr>
    <tr>
      <td>Third-party Advertising</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Developer's Advertising or Marketing</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Analytics</td>
      <td>✓</td>
    </tr>
    <tr>
      <td>Product Personalization</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>App Functionality</td>
      <td>✓</td>
    </tr>
    <tr>
      <td>Other Purposes</td>
      <td>&nbsp;</td>
    </tr>
  </table>
  `}
</HTMLBlock>

1. Coarse Location is calculated from the device's IP Address. Collection of this data can be disabled when initializing the SDKs.