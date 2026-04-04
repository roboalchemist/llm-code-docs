# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/views-of-your-data.md

# Advanced Search

The advanced search feature gives you a flexible way to view the work items in your business area by allowing you to specify multiple different combinations of search criteria, letting you view your work item data precisely how you want to.

You can access the ‘Advanced Search’ tab from the Nav section. When you hover over the 'Advanced Search' option here, you'll also see a list of your [Saved Views](#d-saving-your-views) (if you have any), sorted in alphabetical order. You can easily created Saved Views from the Advanced Search feature so you don't have to enter your search criteria each time.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQwNzYzOA==>" %}

{% hint style="info" %}
Note: Access to this Export feature is not switched on for standard Team Member and Team Leader Roles. To give users access to this feature, a [Custom Role](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/user-roles-and-feature-access) must be created via the User Management section of Builder, with the 'Can Export Advanced Search views to Excel' option switched on in the 'Advanced Search' feature access section.
{% endhint %}

## Searching

To use the Advanced Search feature, enter your search criteria by setting its Field, Condition (e.g. Equals, Greater Than etc.), and Value against which to evaluate the Condition.

The table below gives more detailed information about the standard fields available in the system.&#x20;

<table><thead><tr><th width="189">Field Name</th><th>Description of Field</th><th width="175">Type of condition that can be used</th><th>Value</th></tr></thead><tbody><tr><td>Action Type</td><td>This lets you search for Actions of a particular type. </td><td><p>Begins With</p><p>Equals</p></td><td>Select from: Manual, Manual with Peer Review, Send Email, Send Email and Wait, Start Case, ABBYY OCR, Wait for Sub Cases to Complete, and Trigger External API.</td></tr><tr><td>Assigned To</td><td>This lets you search for work items based on who they are assigned to or whether or not they have been assigned to someone.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a worker</td></tr><tr><td>Context</td><td>This lets you search for work items with a specific context i.e. customer, contract, service</td><td>Equals</td><td>Select a customer, contract and service from the dropdown</td></tr><tr><td>Due</td><td>This lets you search for work items based on when they are due. </td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td>Select a date</td></tr><tr><td>End Date</td><td>This lets you search work items based on when they have been completed i.e. they have been marked as Closed.</td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td>Select a date</td></tr><tr><td>Has Been Reopened</td><td>This lets you search for work items that have been reopened from a Resolved state.</td><td>Equals</td><td>Select from Yes or No</td></tr><tr><td>Initial Request On</td><td>If a further work item has been created from an original request (when a Sub Case is created, when a Ticket is converted into a Case, when a Case or Action gets reworked, when an Action is created via the 'Start Action' option or when a new linked work item is created), this due date method captures the start date of the original request, allowing you to capture the entire length of time it has taken to complete a request, as opposed to just the length of time an individual work item has been being worked on.</td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td>Select a date</td></tr><tr><td>Is Overdue</td><td>This lets you search for work items that are overdue.</td><td>Equals</td><td>Select from Yes or No</td></tr><tr><td>Last Reopened By</td><td>This lets you search for who last reopened a work item from a Resolved state. </td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a worker</td></tr><tr><td>Last Reopened On</td><td>This lets you search for the last time when a work item was reopened from a Resolved state.</td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td>Select a date</td></tr><tr><td><p></p><p>Last Updated By</p></td><td>This lets you search for work items based on the human/digital worker who last updated the work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a worker</td></tr><tr><td>Last Updated On</td><td>This lets you search for work items based on the datetime the item was last updated by a human/digital worker.</td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td>Select a date</td></tr><tr><td>Original Requester Email</td><td>This lets you search for work items based on the email address of the original requester of a work item, i.e. the person who initially raised the request.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td>Original Requester Name</td><td>This lets you search for work items based on the name of the original requester of a work item, i.e. the person who initially raised the request.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td>Owned By</td><td>This lets you search for work items based on the owner of the item i.e. the person who currently has ultimate responsibility for the work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a worker</td></tr><tr><td>Overdue By Days</td><td>This shows how many days or working days (depending upon the due date configuration) a work item is overdue by.</td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td>Enter the desired number of days.</td></tr><tr><td>Parent Process Name</td><td>This lets you search for work items based on their parent process e.g. searching for the name of a Case will return the Actions of the Case in your search.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a parent process</td></tr><tr><td>Parent Reference</td><td>The reference number of the work item which started this one, e.g. parent Case<strong>.</strong></td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter a reference number</td></tr><tr><td>Primary Contact Email</td><td>This lets you search for work items based on the email address of the primary contact of a work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td>Primary Contact Name</td><td>This lets you search for work items based on the name of the primary contact of a work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td><p>Queue</p><p></p></td><td>The work Queue which Cases/Tickets/Actions get sent to based on their routing rule.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a Queue</td></tr><tr><td>Reference</td><td>The unique reference number e.g. 101342-T.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter a reference number</td></tr><tr><td>Requester Email</td><td>This lets you search for work items based on the email address of the requester of a work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td>Requester Name</td><td>This lets you search for work items based on the name of the requester of a work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td>Running</td><td>This lets you search for work items based on their status. Running work items are work items in a state or To Do, In Progress, Waiting</td><td>Equals</td><td><p>Select Yes if you want to search for work items that are in a state of To Do, In Progress or Waiting.</p><p>Select No if you want to search for work items that are not in a state of To Do, In Progress or Waiting.</p></td></tr><tr><td>Schedule</td><td>This lets you search for Cases based on their <a href="https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules/creating-a-schedule">schedule</a></td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, select a schedule from the dropdown</td></tr><tr><td>Schedule Period</td><td>This lets you search for Cases based on their <a href="https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules/creating-a-schedule">schedule period</a>. </td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter a schedule period</td></tr><tr><td>Schedule Structure</td><td>This lets you search for Cases based on their <a href="https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules/creating-a-schedule-structure">schedule structure</a>. </td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, select a schedule structure from the dropdown</td></tr><tr><td>Schedule Year</td><td>This lets you search for Cases based on their <a href="https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules/creating-a-schedule">schedule year</a>. </td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td><p>If the condition you have selected is Equals, Not Equal, Greater Than, </p><p>Greater Than Or Equals To, Less Than or Less Than Or Equals To then enter a year. </p><p></p><p>If the condition you have selected is Between, enter the two different years that you want to search between.</p></td></tr><tr><td>Service Line</td><td>This lets you search for work items based on the overall area of the business the work item runs under, e.g. ‘Payroll’.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>Select a service line from the dropdown</td></tr><tr><td>Service Provider</td><td>This lets you search for work items based on the company delivering service for the work item, usually <em>your</em> company.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>Select a service provider from the dropdown</td></tr><tr><td>Started</td><td>This lets you search for work items based on when the when the work item was started.</td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td>Select a date</td></tr><tr><td>Started By</td><td>This lets you search for work items based on who started the work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a worker</td></tr><tr><td>Started By Method</td><td>This lets you search for work items based on how they got started, e.g. incoming email, automatic schedule, manually.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, select from: Workflow, Manual, Self Service, Robotics, Email, Ticket, Bulk Upload, Schedule, Linked Work Item</td></tr><tr><td>Status</td><td>This lets you search for work items based on their current status.</td><td><p>Equals </p><p>Not Equal</p></td><td><p>Draft</p><p>To Do</p><p>In Progress</p><p>Waiting</p><p>Resolved</p><p>Closed</p></td></tr><tr><td>Status Reason</td><td>This lets you search for work items based on their current status reason.</td><td><p>Equals </p><p>Not Equal</p></td><td><p>Action Unable to Complete</p><p>All relevant Actions completed</p><p>All Split Tickets Completed</p><p>Blocked By Business Rule</p><p>Cancelled</p><p>Completed</p><p>Failed</p><p>Feedback Received</p><p>Feedback Window Passed</p><p>File not found during IDP extraction</p><p>Marketplace not configured</p><p>New Information Received</p><p>Newly Created</p><p>One or more Actions not completed successfully</p><p>Previous Step Completed</p><p>Reopened By Resource</p><p>Rework</p><p>Schedule Date and Time Reached</p><p>Sub Case Completed</p><p>Sub Case Cancelled</p><p>Sub Case Not Yet Started</p><p>Timeout</p><p>Unknown</p><p>Updated by Enate</p><p>Updated by Enate (as End Case Action reached)</p><p>Updated By Integration</p><p>Updated By Resource</p><p>Updated By Support Team</p><p>Waiting for Human Validation</p><p>Waiting for Marketplace</p></td></tr><tr><td>Subject Email</td><td>This lets you search for work items based on the email address of the subject of a work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td>Subject Name</td><td>This lets you search for work items based on the name of the subject of a work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td>Ticket Category Level 1</td><td>This lets you search for Tickets based on their Ticket category level 1 i.e. the highest level of Ticket categorisation e.g. ‘Healthcare Request’.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter a Ticket Category Level 1 value</td></tr><tr><td>Ticket Category Level 2</td><td>This lets you search for Tickets based on their Ticket category level 2 i.e. the next level of Ticket categorisation e.g. ‘International Travel Coverage’.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter a Ticket Category Level 2 value</td></tr><tr><td>Ticket Category Level 3</td><td>This lets you search for Tickets based on their Ticket category level 3 i.e. the most detailed-level of Ticket categorisation e.g. ‘Eligibility Query’.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter a Ticket Category Level 3 value</td></tr><tr><td>Title</td><td>This lets you search for work items based on their title - a brief text description of the work item, often the subject of the original email.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter a title of the work item</td></tr><tr><td>Wait Type</td><td>This lets you search for work items based on their wait type i.e. if they have a wait type of 'Waiting for more information', etc.</td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal</p></td><td><p>External System</p><p>Pause</p><p>Related Work Items</p><p>Wait for more information</p><p>Wait Until</p></td></tr><tr><td>Work Item Type</td><td>This lets you search for work items based on their work item type i.e. if they're a Ticket, Case or Action.</td><td>Equals</td><td>Select Case, Ticket or Action</td></tr></tbody></table>

You can also select Fields based on any [custom data fields that have been configured in your system](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration/creating-custom-data-fields), excluding custom data tables.

You can add as many additional sets of conditions as you wish by clicking on the green plus icon.

Once you have entered your search conditions, click Search to reveal your search results. Your total number of search results will be shown at the top of the grid.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYtIGa1fzfRh5j7mWcw%2F-MYtv2hLoeSBnTaMcjeo%2FExample-View-Search.gif?alt=media\&token=57e6a52d-885d-4ab6-a504-2a8968120d51)

## Choosing which data to see in Search Results <a href="#b-choosing-which-data-columns-to-see-in-search-results" id="b-choosing-which-data-columns-to-see-in-search-results"></a>

As with your Work Inbox and Owned work grids, you can choose which data columns you wish to see or hide in your search results grid by clicking on the Cog icon above the Search Results grid.

A ‘Display and Columns Settings’ popup will appear, allowing you to select which data columns you would like your search results to display.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYtz7NIF5ed0SdI8MIe%2F-MYu-kenHwpZZG5g3Dsh%2FOrder-Views-Data-Columns.gif?alt=media\&token=05996cb2-015b-4df9-b8a7-611bf66e686b)

{% hint style="info" %}
Note: These custom data column preferences will stay the same when you do multiple searches, and when you next log back in.
{% endhint %}

## Grouping and Ordering <a href="#c-grouping-and-ordering" id="c-grouping-and-ordering"></a>

You are also able to Group and Order your search results by selecting your Group By and Order By preferences from their respective dropdown lists.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYtz7NIF5ed0SdI8MIe%2F-MYuRfsx8PRyTd41m_Xv%2FGrouping-Views-Searches.gif?alt=media\&token=4155693a-8007-47d7-bafa-585ea9cf8a0e)

{% hint style="info" %}
Note: Only a single grouping criteria can be specified, and results will be loaded when you click on and expand an individual group.
{% endhint %}

## Saving Your Advanced Searches <a href="#d-saving-your-views" id="d-saving-your-views"></a>

You can also save your Advanced Searches as views which allows you to call them up again whenever you want. There is no limit to the number of views that you can save.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fr7fAR2GPKOylTDyXrdA4%2FSaved-Views.gif?alt=media&#x26;token=0ae3d4d0-0e11-402f-b60d-8f777c320502" alt=""><figcaption></figcaption></figure>

You can access your Saved Views by clicking on the Saved Views link.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8YLpozrh6IEX97caDNGD%2Fimage.png?alt=media\&token=40324e8f-4f35-409b-b620-9eb03c242abe)

Here you can search for a specific Saved View and rename and delete your Saved Views.

You can copy the name of your Saved View by clicking on the copy button on the tab:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fh0nOnpI9DoeMhLhc9ZSN%2Fimage.png?alt=media\&token=338e56d8-d88c-4c1c-b485-42878c9112c8)

## Exporting Advanced Search Views into Excel

You can export your views data from your Advances Searches into Excel. Watch this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQwNzYzOQ==>" %}

To export your views data into an Excel spreadsheet, enter your search criteria in the Advanced Search page and then click to 'Switch to Export'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FSRBBn5B9LITmtAR2GHwA%2Fimage.png?alt=media&#x26;token=1067adfb-4b51-496b-9d2d-f30f2132d7fd" alt=""><figcaption></figcaption></figure>

This will show you a list of all of your previously exported files, as well as when they were downloaded, the size of the file, the total number of rows in the file, when the file export was requested, when the export began and when it was completed.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F530WLNQs3Um548Jd3Ro1%2Fimage.png?alt=media&#x26;token=79ea2d5b-ae95-44a6-808e-b83bc0c7361d" alt=""><figcaption></figcaption></figure>

Before you export your search, you can edit the name of the file it will be exported as.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQgFvclpsc0PYsC98o8gt%2Fimage.png?alt=media&#x26;token=1cff9746-47e0-4040-a1aa-4438a8a0e95c" alt=""><figcaption></figcaption></figure>

You can also adjust which columns you would like to view in your excel export by clicking on 'Select columns'. The columns selected in your search will be automatically selected, but you can adjust your selection here too.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FKRTEZDlJlq1iN84eY7QM%2Fimage.png?alt=media&#x26;token=6aaf1620-06c7-4b24-9492-188d47144f8b" alt=""><figcaption></figcaption></figure>

Then click to 'Export'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fw5dMVGkg1OfFXxJyF8Sw%2Fimage.png?alt=media&#x26;token=1a1a3a26-4b3d-474d-ba71-0b2dff0ecad2" alt=""><figcaption></figcaption></figure>

Your file will appear as a new row in the Exported Files section with a 'queued' icon next to it. Click to refresh the grid.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FsiBdI1ORI0vQnSB6XgBG%2Fimage.png?alt=media&#x26;token=ad3962be-10b0-482b-ab3b-ef5c1a40675f" alt=""><figcaption></figcaption></figure>

Once refreshed, the icon will change to a green single tick to show that the export is complete.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FfGBza8YOgfKc2WjpmZsU%2Fimage.png?alt=media&#x26;token=28c331c1-0421-453a-bf1a-6385e35ecd03" alt=""><figcaption></figcaption></figure>

If there has been an error in exporting the file, a red warning icon will appear next to it.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6ywCwvG0Whd1vmwR6YGV%2Fimage.png?alt=media&#x26;token=e5dc0f48-3825-489b-accf-f2bdcb1c8e32" alt=""><figcaption></figcaption></figure>

You can download the file by clicking on the file name.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FpykMJd6up8FgKV5WxH9l%2Fimage.png?alt=media&#x26;token=4ea3ab3b-d51f-41b6-8a8d-349ba790f100" alt=""><figcaption></figcaption></figure>

Once it has been downloaded, the icon will change to a green double tick to show that it has been downloaded.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDfFQRe3sTydmifx9gr3d%2Fimage.png?alt=media&#x26;token=42b0bda2-34e8-4dad-9239-f1767554fd6f" alt=""><figcaption></figcaption></figure>

The time and date that it was downloaded will then appear in the 'Downloaded On' column.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FBb7ernbWDEyt7URjoReX%2Fimage.png?alt=media&#x26;token=1478be1c-28de-4e43-b3a4-0461cca0b1ec" alt=""><figcaption></figcaption></figure>

The data from your Advanced Search will have been exported into a .xlsx file, including the column titles selected.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FdeM8tLrMWpNsM8gv4Dlx%2Fimage.png?alt=media&#x26;token=24a2c623-796f-454e-9c33-249c80dd29fb" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Please note that in this initial release, column titles will only appear in English. They will be localized in a future release.

Additionally, please note that you can export up to a maximum of one million rows.

Column names in the exported file are different to the names that are displayed in the UI in the Advanced Search page.
{% endhint %}

## Copy/Paste into Excel <a href="#e-copy-paste-into-excel" id="e-copy-paste-into-excel"></a>

You can copy and paste information from the Advanced Search grid into an Excel spreadsheet by selecting the information you want to copy and using Ctrl C and Ctrl V. The information that is copied and pasted includes any applied filters. The column titles will automatically be copied and pasted as well.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYuS6h2QRhLllsba5Dk%2F-MYuTgl-EXI_C_I4eJLQ%2FCopy-Views-to-Excel.gif?alt=media\&token=e89b9890-c260-48f0-867c-6ab7bd5293c4)

You are also able to to copy and paste all of the information from the Views grid by using Ctrl-A.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYuS6h2QRhLllsba5Dk%2F-MYuUled-D4l_4a1Z5V4%2FCtrl-A-Into-Excel-from-Views.gif?alt=media\&token=a1c81a29-3b81-4b31-aa1d-903abe8ba7a0)

{% hint style="info" %}
Note: only information that has loaded in the Advanced Search grid will be copied across.
{% endhint %}
