# 3D Secure Test Scenarios | PayPal Developer

## If you accept cookies, we’ll use them to improve and customize your experience and enable our partners to show you personalized PayPal ads when you visit other sites. [Manage cookies and learn more](https://www.paypal.com/myaccount/privacy/cookiePrefs?locale=en_US)

---

## Test cases and card details for purchase flows

The PayPal sandbox supports end-to-end testing for purchase flows using payment methods issued by Visa, Mastercard, American Express, Discover, Diners, and other card brands.

Use the test cards in the following table to:

- Simulate a purchase.
- Generate a 3D Secure response.

The test cards in this section only work for purchase flows. Don’t use the cards in this section to test [Save payment methods](/docs/checkout/save-payment-methods/).

Find test cases and card details for the following countries:

- United States
- Great Britain
- China
- Australia
- France
- Germany
- Italy
- Japan
- Mexico
- Spain

**info**
**Tip:** Enter a future expiration date and any 3-digit CVV, or 4-digit CVV for American Express, to proceed.

### United States

| Scenario | Test cards | API response |
| --- | --- | --- |
| Test Case 1: Successful Frictionless Authentication | Visa: 4868719196829038<br>Mastercard: 5329879707824603<br>Discover: 6507720016523241<br>JCB: 3636500013811265<br>Diners: 3613285017849035<br>CUP: 6011270016527338 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 2: Failed Frictionless Authentication | Visa: 4868719158130060<br>Mastercard: 5329879769571910<br>Discover: 6507720026574622<br>JCB: 3636500029449373<br>Diners: 3613285026969303<br>CUP: 6011270026518392 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "N" } |
| Test Case 3: Attempts Stand-In Frictionless Authentication | Visa: 4868719581920723<br>Mastercard: 5329879715396727<br>Discover: 6507720036528600<br>JCB: 3636500036026768<br>Diners: 3613285032453102<br>CUP: 6011270036572314 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "A" } |
| Test Case 4: Unavailable Frictionless Authentication | Visa: 4868719033482561<br>Mastercard: 5329879705777613<br>Discover: 6507720046586499<br>JCB: 3636500042364807<br>Diners: 3613285046621520<br>CUP: 6011270046547272 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "U" } |
| Test Case 5: Rejected Frictionless Authentication | Visa: 4868719081564153<br>Mastercard: 5319541865518409<br>Discover: 6507720056587320<br>JCB: 3636500056727543<br>Diners: 3613285054207154<br>CUP: 6011270056539078 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "R" } |
| Test Case 6: Authentication Not Available on Lookup | Visa: 4868719488651967<br>Mastercard: 5329879714462553<br>Discover: 6507720066510627<br>JCB: 3636500063958628<br>Diners: 3613285065837494<br>CUP: 6011270066581029 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "U" } |
| Test Case 7: Successful Step-up Authentication | Visa: 4868719166101368<br>Mastercard: 5329879735316929<br>Discover: 6507720106578071<br>JCB: 3636500107547155<br>Diners: 3613285107233215<br>CUP: 6011270106573127 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 8: Failed Step-Up Authentication | Visa: 4868719181895556<br>Mastercard: 5329879768013724<br>Discover: 6507720116568591<br>JCB: 3636500118802441<br>Diners: 3613285118398817<br>CUP: 6011270116539514 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "N" } |
| Test Case 9: Step-Up Authentication is Unavailable | Visa: 4868719557718580<br>Mastercard: 5329879734808405<br>Discover: 6507720126556792<br>JCB: 3636500129164682<br>Diners: 3613285124482902<br>CUP: 6011270126552846 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "U" } |

### Great Britain

| Scenario | Test cards | API response |
| --- | --- | --- |
| Test Case 1: Successful Frictionless Authentication | Visa: 4462603042343024<br>Mastercard: 5120069996018452<br>Amex: 374576301040603 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 2: Failed Frictionless Authentication | Visa: 4462603045503384<br>Mastercard: 5120069996477518<br>Amex: 374576302793937 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "N" } |
| Test Case 3: Attempts Stand-In Frictionless Authentication | Visa: 4462603046653873<br>Mastercard: 5120069996491832<br>Amex: 374576303323882 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "A" } |
| Test Case 4: Unavailable Frictionless Authentication | Visa: 4462603040650784<br>Mastercard: 5120069996100821<br>Amex: 374576304897561 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "U" } |
| Test Case 5: Rejected Frictionless Authentication | Visa: 4462603047907062<br>Mastercard: 5120069996727748<br>Amex: 374576305201532 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "R" } |
| Test Case 6: Authentication Not Available on Lookup | Visa: 4462603049870995<br>Mastercard: 5120069996936430<br>Amex: 374576306743755 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "U" } |
| Test Case 7: Successful Step-up Authentication | Visa: 4462603040971339<br>Mastercard: 5120069996617055<br>Amex: 374576310765125 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 8: Failed Step-Up Authentication | Visa: 4462603043025620<br>Mastercard: 5120069996452719<br>Amex: 374576311529389 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "N" } |
| Test Case 9: Step-Up Authentication is Unavailable | Visa: 4462603040318820<br>Mastercard: 5120069996698402<br>Amex: 374576312273961 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "U" } |

### China

| Scenario | Test cards | API response |
| --- | --- | --- |
| Test Case 1: Successful Frictionless Authentication | CUP: 6029070012371891 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 2: Failed Frictionless Authentication | CUP: 6029070022371899 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "N" } |
| Test Case 3: Attempts Stand-In Frictionless Authentication | CUP: 6029070032371897 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "A" } |
| Test Case 4: Unavailable Frictionless Authentication | CUP: 6029070042371895 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "U" } |
| Test Case 5: Rejected Frictionless Authentication | CUP: 6029070052371892 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "R" } |
| Test Case 6: Authentication Not Available on Lookup | CUP: 6029070062371890 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "U" } |
| Test Case 7: Successful Step-up Authentication | CUP: 6029070102371892 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 8: Failed Step-Up Authentication | CUP: 6029070112371890 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "N" } |
| Test Case 9: Step-Up Authentication is Unavailable | CUP: 6029070122371898 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "U" } |

### Australia

| Scenario | Test cards | API response |
| --- | --- | --- |
| Test Case 1: Successful Frictionless Authentication | EFTPOS Mastercard: 5188680063997235<br>EFTPOS Mastercard: 5188680085804575 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 2: Successful Frictionless Authentication | EFTPOS Visa: 4687380000000107 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |

### France

| Scenario | Test cards | API response |
| --- | --- | --- |
| Test Case 1: Successful Frictionless Authentication | Visa: 4147044347484424<br>Mastercard: 5131016099426568<br>CB Visa: 4973730096543597<br>CB Mastercard: 5294692013549108<br>Amex: 377451301969853 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 2: Failed Frictionless Authentication | Visa: 4147044332973480<br>Mastercard: 5131016060646798<br>CB Visa: 4973730090795029<br>CB Mastercard: 5294692024183798<br>Amex: 377451302438379 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "N" } |
| Test Case 3: Attempts Stand-In Frictionless Authentication | Visa: 4147044352661890<br>Mastercard: 5131016071891243<br>CB Visa: 4973730083020005<br>CB Mastercard: 5294692039496284<br>Amex: 377451303722144 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "A" } |
| Test Case 4: Unavailable Frictionless Authentication | Visa: 4147044328260272<br>Mastercard: 5131016051319397<br>CB Visa: 4973730021799686<br>CB Mastercard: 5294692043530193<br>Amex: 377451304264435 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "U" } |
| Test Case 5: Rejected Frictionless Authentication | Visa: 4147044349862668<br>Mastercard: 5131016014864117<br>CB Visa: 4973730063113135<br>CB Mastercard: 5294692057014837<br>Amex: 377451305380032 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "R" } |
| Test Case 6: Authentication Not Available on Lookup | Visa: 4147044395282514<br>Mastercard: 5131016037556989<br>CB Visa: 4973730075769619<br>CB Mastercard: 5294692066416528<br>Amex: 377451306933888 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "U" } |
| Test Case 7: Successful Step-up Authentication | Visa: 4147044387320066<br>Mastercard: 5131016013297020<br>CB Visa: 4973730070212326<br>CB Mastercard: 5294692102269881<br>Amex: 377451310828959 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 8: Failed Step-Up Authentication | Visa: 4147044332857790<br>Mastercard: 5131016076508925<br>CB Visa: 4973730002779426<br>CB Mastercard: 5294692113967192<br>Amex: 377451311846547 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "N" } |
| Test Case 9: Step-Up Authentication is Unavailable | Visa: 4147044366839813<br>Mastercard: 5131016002794250<br>CB Visa: 4973730014083692<br>CB Mastercard: 5294692129581979<br>Amex: 377451312279706 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "U" } |

### Germany

| Scenario | Test cards | API response |
| --- | --- | --- |
| Test Case 1: Successful Frictionless Authentication | Visa: 4779131010696190<br>Mastercard: 5232747082012365 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 2: Failed Frictionless Authentication | Visa: 4779131029887282<br>Mastercard: 5232747082026340 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "N" } |
| Test Case 3: Attempts Stand-In Frictionless Authentication | Visa: 4779131034444012<br>Mastercard: 5232747082037925 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "A" } |
| Test Case 4: Unavailable Frictionless Authentication | Visa: 4779131043637366<br>Mastercard: 5232747082040184 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "U" } |
| Test Case 5: Rejected Frictionless Authentication | Visa: 4779131051776981<br>Mastercard: 5232747082050118<br>Amex: 374576301478908<br>Diners: 36677850174767 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "R" } |
| Test Case 2: Authentication Not Available on Lookup | Visa: 4779131067504989<br>Mastercard: 5232747082060125<br>Amex: 374576306743755<br>Diners: 36677850669980<br>CUP: 6011270066581029 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "U" } |
| Test Case 7: Successful Step-up Authentication | Visa: 4779131109317713<br>Mastercard: 5232747082106928<br>Amex: 374576310976611<br>Diners: 36677851000136 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 8: Failed Step-Up Authentication | Visa: 4779131113498285<br>Mastercard: 5232747082118238<br>Amex: 374576311142908<br>Diners: 36677851132475 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "N" } |
| Test Case 9: Step-Up Authentication is Unavailable | Visa: 4779131126041981<br>Mastercard: 5232747082125225<br>Amex: 374576312319315<br>Diners: 36677851286297 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "U" } |

### Italy

| Scenario | Test cards | API response |
| --- | --- | --- |
| Test Case 1: Successful Frictionless Authentication | Visa: 4444385659642475<br>Mastercard: 5356586342391841<br>Amex: 375255301652530 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 2: Failed Frictionless Authentication | Visa: 4444385687543430<br>Mastercard: 5356586607301766<br>Amex: 375255302715567 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "N" } |
| Test Case 3: Attempts Stand-In Frictionless Authentication | Visa: 4444385601333769<br>Mastercard: 5356586428447392<br>Amex: 375255303067018 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "A" } |
| Test Case 4: Unavailable Frictionless Authentication | Visa: 4444385668578231<br>Mastercard: 5356586058044832<br>Amex: 375255304651984 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "U" } |
| Test Case 5: Rejected Frictionless Authentication | Visa: 4444385690220737<br>Mastercard: 5356586672163869<br>Amex: 375255305110030 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "R" } |
| Test Case 6: Authentication Not Available on Lookup | Visa: 4444385638350414<br>Mastercard: 5356586104283632<br>Amex: 375255306096741<br>Diners: 3613285065837494<br>CUP: 6011270066581029 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "U" } |
| Test Case 7: Successful Step-up Authentication | Visa: 4444385699062981<br>Mastercard: 5356586654031019<br>Amex: 375255310219230<br>Diners: 3613285107233215<br>CUP: 6011270106573127 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 8: Failed Step-Up Authentication | Visa: 4444385664948453<br>Mastercard: 5356586695482403<br>Amex: 375255311341314<br>Diners: 3613285118398817<br>CUP: 6011270116539514 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "N" } |
| Test Case 9: Step-Up Authentication is Unavailable | Visa: 4444385633098885<br>Mastercard: 5356586239584342<br>Amex: 375255312279706<br>Diners: 36132851286297 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "U" } |

### Japan

| Scenario | Test cards | API response |
| --- | --- | --- |
| Test Case 1: Successful Frictionless Authentication | JCB: 3566632400173084<br>Visa: 4980261010966483<br>Mastercard: 5214982012358214<br>Amex: 376515301478908<br>Diners: 36677850174767 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 2: Failed Frictionless Authentication | JCB: 3566632400217204<br>Visa: 4980261025507249<br>Mastercard: 5214982027870120<br>Amex: 376515302605798<br>Diners: 36677850279053 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "N" } |
| Test Case 3: Attempts Stand-In Frictionless Authentication | JCB: 3566632400337754<br>Visa: 4980261035853047<br>Mastercard: 5214982030287924<br>Amex: 376515303004975<br>Diners: 36677850397566 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "A" } |
| Test Case 4: Unavailable Frictionless Authentication | JCB: 3566632400461224<br>Visa: 4980261043485733<br>Mastercard: 5214982048381859<br>Amex: 376515304008900<br>Diners: 36677850418214 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "U" } |
| Test Case 5: Rejected Frictionless Authentication | JCB: 3566632400503165<br>Visa: 4980261056545746<br>Mastercard: 5214982056641020<br>Amex: 376515305443064<br>Diners: 36677850502975 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status": "R" } |
| Test Case 6: Authentication Not Available on Lookup | JCB: 3566632400624110<br>Visa: 4980261061849109<br>Mastercard: 5214982065169807<br>Amex: 376515306677421<br>Diners: 36677850669980 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "U" } |
| Test Case 7: Successful Step-up Authentication | JCB: 3566632401070610<br>Visa: 4980261104232164<br>Mastercard: 5214982106067481<br>Amex: 376515310976611<br>Diners: 36677851000136 | "authentication_result": { "liability_shift": "POSSIBLE", "enrollment_status": "Y", "authentication_status": "Y" } |
| Test Case 8: Failed Step-Up Authentication | JCB: 3566632401190277<br>Visa: 4980261118319031<br>Mastercard: 5214982119079002<br>Amex: 376515311142908<br>Diners: 36677851132475 | "authentication_result": { "liability_shift": "NO", "enrollment_status": "Y", "authentication_status":