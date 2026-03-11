# Source: https://docs.axonius.com/docs/licenses-csv.md

# CSV - Licenses

**CSV - Licenses** adapter imports information about SaaS licenses from a CSV file.

The adapter parameters are the same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv).  Since the **CSV - Licenses** adapter provides data about licenses only, unlike the generic CSV adapter, there is no option to configure the adapter to contain information about Users, Devices, or any other type of asset.

The functionality of this adapter is the same as the [CSV adapter](/docs/csv).
Note that the *Accepted CSV field*  names are case insensitive.

## Which fields are imported with a Licenses file?

The following data is imported as part of the Licenses file.

The information imported is then displayed on the relevant asset page. Please note that it is important to enter appropriate information in each field in order to obtain an optimum display.

In some cases the fields a specific company uses might not match the fields here. We therefore recommend the following:

Some companies list license names in their databases according to the business unit that uses them (Example: Slack - marketing, Slack (R\&d), etc) in the vendor name or license name field. In order to render the CSV correctly we recommend as a best practice to enter the official (or actual) vendor name and license names in those fields, and use the Connection label field (account) for such additional data.

License Name - If your database does not use the official vendor name but uses a general term for the license name (such a google, rather than Google enterprise standard), then the data such as the business unit can be entered in the license name field (google (marketing), google-R\&d, etc).

| Field                    | Accepted CSV Field Name(s)                                                    | Description                                                                                                                                            | Required?                         |
| :----------------------- | :---------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------- |
| Application              | vendor name, Vendor, Supplier, Supplier name, application, app                | The license vendor                                                                                                                                     | Yes                               |
| Application Account Name | account, Connection Label                                                     | Account name/Instance name                                                                                                                             | Yes                               |
| License name             | License name, License, Name, SKU                                              | The name of the specific license                                                                                                                       | Yes                               |
| Start date               | Start Date, Start, From                                                       | Start of license duration                                                                                                                              | Yes                               |
| End date                 | End date, Expiration date, Renewal date, Finish, Until                        | End of license duration                                                                                                                                | Yes                               |
| Subscription term        | Subscription Term, Cadence, Renewal                                           | Yearly/Monthly/Other/Expiration (Whether users subscribe to a monthly renewal, yearly renewal, a different renewal cadence or does the license expire) | Yes                               |
| Total cost               | Amount, Total amount, License cost, total cost, License value                 | The entire value of the license (price per unit \*quantity)                                                                                            | Yes                               |
| Unit price               | Unit Price, unit cost, cost per unit, price per unit                          | Price of each unit (user, seat, etc)                                                                                                                   | No                                |
| Original currency        | Original currency, Currency                                                   | Currency in which the license is priced; can be either of the following values: USD, EUR, GBP, AUD                                                     | No                                |
| Quantity                 | Quantity, number of units, Units, # of units, License units                   | Number of units paid for                                                                                                                               | Yes                               |
| Pricing unit             | Pricing unit, Unit                                                            | Seats, Users, or Other                                                                                                                                 | No (if not provided, enter other) |
| Owner                    | Owner, License owner, email, employee email, owner email, license owner email | Email of license owner (as appears on contract or PO)                                                                                                  | No                                |
| License payment          | license type, licensetype, license payment, payment type                      | Paid/Free/Trial                                                                                                                                        | Yes                               |