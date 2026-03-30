# Source: https://adempiere.gitbook.io/docs/introduction/system-administration/managing-organizations/document-status-indicators.md

# Document Status Indicators

The Web Application dashboard includes a panel showing Document Tasks as shown below.

![Dashboard Document tasks panel](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ9vtCKO6mt2Z4eXD%2Fwebui_dashboard_doctasks.PNG?generation=1550287157761043\&alt=media)

The information displayed to the User is configured in the **Document Status Indicator** window in the **System Administration > Organizational Rules** menu. Access to the Document Tasks panel in the Dashboard also has to be enabled for the User in the **Role** window, **Dashboard Access** tab found in the **System Administration > General Rules > Security** menu.

{% hint style="warning" %}
Configuring Document Status Indicators requires an understanding of the underlying database tables and columns which represent "documents" in ADempiere and SQL queries.
{% endhint %}

![Document Status Indicator window](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJAeL2c3Pq7y3HBJV%2Fwebui_win_documentstatusindicator.PNG?generation=1550287167492757\&alt=media)

There can be many Document Status Indicator records for an Organization or Client. The selection of which indicators are displayed to a particular User is based on the following:

* Only ***Active*** indicators are shown
* From the same ***Client***
* Where the ***User/Contact*** field is blank or matches the User
* AND where the **Role** field is blank or matches the User's Role.

The sequence that the indicators are shown in is determined by the ***Sequence*** field, with lower numbers being shown first.

The ***Table*** **\*\*field identifies the document of interest and the \_**&#x53;QL Where ***field selects the relevant document records from the*** Table\*\*\_.

The display in the Document Tasks panel is a count of the documents of interest. The link beside the number is based on the ***Name*** field.

{% hint style="warning" %}
The name field is not translated.
{% endhint %}

The count of the documents and the link to those documents is made using an SQL Where clause that is constructed from the ***SQL Where*** field plus a few other constraints:

* Only documents within the same ***Client***
* If the ***Organization*** field is not All (**\***), then only documents that match the ***Organization***
* If the **Projec**t field is not blank, then only documents that match that **Project**

If the User clicks on a status indicator and a ***Window*** is specified, the window will be opened and loaded with the selected documents. If the ***Window*** field is blank and the ***Special Form*** field identifies a form, the form will be opened and loaded with the documents.

{% hint style="warning" %}
If both the ***Window*** and ***Special Form*** fields are blank, nothing will happen when the User clicks on the link in the Document Status panel.
{% endhint %}

{% hint style="info" %}
The ***Name Font***, ***Name Color***, ***Number Font*** and ***Number Color*** fields are not used.
{% endhint %}

## Example - Unpaid AR Invoices

As an example using the Garden World client, assume that Garden User needs to see unpaid invoices to ensure payment allocations are made and to personally dun (collect) the amount owed. The GardenAdmin user is not interested in this. The Document task panel for the GardenUser should look like the following:

![GardenUser Dashboard entry for Document tasks showing the Unpaid Invoices entry](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJAeP7PkscydhmAf6%2Fwebui_dashboard_doctaskexample.PNG?generation=1550287167442464\&alt=media)

1. Login as GardenAdmin and the GardenAdmin role.
2. Open the **Document Status Indicator** window and create a new record.  Set the fields as follows and save the record.:
   1. ***Client*** - will default to Garden World
   2. ***Organization*** - \*
   3. ***Name*** - Unpaid Invoices
   4. ***User*** - GardenUser
   5. ***Sequence*** - 10
   6. ***Table*** - C\_Invoice
   7. ***SQL Where*** - C\_Invoice.IsSOTrx='Y' AND C\_Invoice.DocStatus='CO' AND C\_Invoice.IsPaid='N' AND PaymentTermDueDays(C\_Invoice.C\_PaymentTerm\_ID, C\_Invoice.DateInvoiced, getdate()) > 0
   8. ***Window*** - Invoice (Customer)
3. Verify that a **Dashboard Content Edit** entry exists for the *Document tasks*. The System Client entry will do.
4. Open the **Role** window and find the record for the *GardenWorld User* role.
   1. In the **Dashboard Access** tab, add an entry and set the ***Dashboard Content*** to *Document tasks*, if it doesn't already exist. Save the record.
5. Verify that there are paid and unpaid/due customer invoices in the system. Create some if necessary.
6. Log in as GardenUser and verify that the *Document tasks* panel shows the correct number of unpaid invoices.  Click on the link and ensure that only unpaid invoices appear in the **Invoice (Customer)** window when it opens.
7. Make a full payment to one of the invoices.  Return to the dashboard and verify that the *Document tasks* entry has been updated. (Note that it may take a minute to update.  The dashboard refresh happens every 60 seconds.)
8. Log in as GardenAdmin, verify that the "Unpaid Invoices" item does not appear in the *Document tasks* panel.

   .
