# Source: https://docs.axonius.com/docs/expenses-csv.md

# CSV - Expenses

**CSV - Expenses** File Adapter imports information about transactions related to SaaS from a CSV file.

The adapter parameters are the same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv). Since the CSV - Expenses adapter provides data about transactions only, unlike the generic CSV adapter, there is no option to configure the adapter to contain information about Users, Devices, or any other type of asset.

The functionality of this adapter is the same as the [CSV adapter](/docs/csv).

Note that the *Accepted CSV field* names are case insensitive.

## Which fields are imported with an Expenses file?

The following data is imported as part of the Expenses file.

| Field                   | Accepted CSV Field Name(s)                                                                                                           | Notes                                       | Required?                                              |
| :---------------------- | :----------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------ | :----------------------------------------------------- |
| Transaction ID          | Transaction ID, Report ID, ID, Identifier, Invoice number                                                                            | Internal transaction ID of the CSV’s source | Yes (this is a mandatory field in order to fetch data) |
| Transaction date        | Transaction date, Date, Invoice date, Invoice voucher date                                                                           | Transaction date                            | Yes                                                    |
| Amount                  | Amount, Total amount, Expense line amount, Spend, Spend\_USD                                                                         | Transaction amount                          | Yes                                                    |
| Original currency       | Original currency, Currency                                                                                                          | Transaction original currency               | No (USD is the currently supported currency            |
| Application             | vendor name, Vendor, Supplier, Supplier name, application                                                                            | The SaaS product  purchased                 | Yes                                                    |
| Transaction description | Transaction description, Description, Comments, Invoice description, Invoice line description                                        | Transaction’s description                   | No                                                     |
| Department              | Department, BU, BU name, Business unit                                                                                               | Transaction on behalf of which department   | No                                                     |
| Reported by email       | Reported by email, Employee, Emp Email, submitted by, Submitter, mail, email, usermail, mailaddress, email address, emailprimarywork | Owner (email appearing in the transaction)  | No                                                     |

## Advanced Settings

* **Match application names with Axonius SaaS applications repository** - Select this option to ignore expenses of applications or vendors that are not included in the [SaaS Applications repository](/docs/saas-applications-repository).