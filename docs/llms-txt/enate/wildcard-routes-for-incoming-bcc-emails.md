# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/incoming-emails-processing-logic/wildcard-routes-for-incoming-bcc-emails.md

# Wildcard Routes for incoming BCC Emails

When incoming emails have the relevant Enate email address as the Bcc'd, they do not have a 'To' address visible to the system and so are plaeced in the Unprocessed emails list.&#x20;

To help reduce the ocurrences of such mails landing in 'Unprocessed emails' in this situation, you can configure Wilcard Email Routes which essentially use the knowledge of which email addresses these mails come ***from*** to allow it to be processed. These Routes are set to match with a wildcard '\*' email address (The To address of the incoming mail) and a known email address (or addresses) in the 'Sender List includes' (The From address of the incoming mail). Set in this way, they able to match even a BCC'd email if the from address matches.

### Creating a 'Wildcard' Email Route

Wildcard routes are created in the same way non-wildcard routes are created, via the 'Routes' page in the Email section of Builder. Simply click to create a new email route and fill in the email route pop-up information as required. To set this as a Wildcard Route to handle Bcc scenario, when filling out the Routing Rules information users should put a '\*' wildcard asterisk as the 'Email Address', and then in the 'Sender List Includes' field, set the name of the known email address that such mails would be coming from. Multiple such addresses can be added to a single Route, with a ';' semicolon character between.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FeXlUs9c6Jnp4CxG7PxHo%2FEdit%20Email%20Route.webp?alt=media&#x26;token=fcef7daa-b260-447d-8b1f-ed8604a26914" alt=""><figcaption></figcaption></figure>

You should create as many such Wildcard Routes for a single Email Connector as there are different Work Item types you wish to be creating from that connector.&#x20;

#### Ordering of Wildcard Routes with Other Routes

When ordering their email routes into a hierarchy, users should always ensure that non-wildcard routes appear above wildcard routes, with overall fallback routes appearing *after* the wildcard routes at the very bottom of the list.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPEyidZwEwFkLQ1GyJBwE%2FAnkita%20Test.png?alt=media&#x26;token=86c00d1d-874c-44cc-b904-6e46c004bd40" alt=""><figcaption></figcaption></figure>

## Rules when setting up Wildcard Email Routes

When creating an email route containing a wildcard route, there are some important rules that apply, to keep routing of incoming emails working consistently at runeimt. See the table below for a full list of rules regarding the use of working with Email Routes if wildcard (i.e. '\*') email routes are involved.

Note: The system will show error messages when a user attempts an activity which may break these rules.

<table><thead><tr><th>Activity</th><th width="336">Rule</th><th>Related API</th></tr></thead><tbody><tr><td>Updating an Email Route</td><td><strong>Updating a NON-wildcard email route to a wildcard email route is now restricted.</strong></td><td><strong>Email Route - Update</strong></td></tr><tr><td>Updating an Email Route</td><td><strong>Updating a wildcard email route to a NON-wildcard email route is now restricted.</strong></td><td><strong>Email Route - Update</strong></td></tr><tr><td>Creating or Updating an Email Route</td><td><strong>The system does not allow using a wildcard address for the sender list when the route's email address is also a wildcard.</strong></td><td><strong>Email Route - Create Email Route - Update</strong></td></tr><tr><td>Creating or Updating an Email Route</td><td><strong>A wildcard route requires a sender list to be included.</strong></td><td><strong>Email Route - Create Email Route - Update</strong></td></tr><tr><td>Ordering Multiple Routes</td><td><strong>When using a wildcard, a strict routing order exists:</strong><br><strong>1. Non-wildcard Routes</strong><br><strong>2. Wildcard Routes</strong><br><strong>3. Fallback Routes</strong></td><td><strong>Email Route - Get All For Connector</strong></td></tr><tr><td>Creating an Email Route</td><td><strong>When a email route is created, whether it is a wildcard or not, its order is based on the criteria is determined by the order (stated above). Route orders can be adjusted accordingly after creation.</strong></td><td><strong>Email Route - Create</strong></td></tr><tr><td>Moving an Email Route</td><td><strong>Routes can only be rearranged within their respective type ranges. For example, if it's a wild card route, the system allows moving it within the wild card order range (min-max). The same applies to non-wildcard routes, where the system permits movement within the non-wildcard order range (min-max). If routes are moved beyond their designated range, the system will generate an error.</strong></td><td><strong>Email Route - Move Route</strong></td></tr></tbody></table>

#### Example of screen popups to help ensure consistent ordering of such routes:

If a user attempts to move a route into an order that does not correspond with the required hierarchy, the route will return to where it was and a error message will be displayed.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FoW9yfNnyG8OBYA5bDbF0%2Fimage.png?alt=media&#x26;token=d9a3814b-46ac-4e28-9727-ebbceccd0803" alt=""><figcaption></figcaption></figure>
