# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules/creating-a-schedule.md

# Creating a Schedule

One you have [created a schedule structure](https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules/creating-a-schedule-structure), you then need to create a schedule of dates to use alongside your schedule structure.&#x20;

To find out how to create a schedule, you can watch the following video or read the steps below.&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MjU5Ng==>" %}

To create a schedule, go to the ‘Schedules’ page in Builder. Here you can see any previously created schedules and create new ones.

To create a new schedule, click on the ‘Add Schedule’ link. This will bring up a popup where you select the schedule structure you want your new schedule to use.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpshnNbM_pzEmjOTsa%2Fimage.png?alt=media\&token=2d5156c8-e862-4927-898a-7c051d15e0f1)

After selecting your desired schedule structure, you can then define the name and description of your new schedule.

You can then add as many sets of dates for as many periods as you desire to it by adding a row and defining the dates for the periods as desired.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpskbVm0D6St2m3-BV%2Fimage.png?alt=media\&token=c12c09c3-910d-47f7-b69f-75ad2fbe4707)

{% hint style="info" %}
Points to note:

* You can define as many dates as you wish at this point and must define a year and a period for each.
* You will always have to enter a time component for each date.
* Dates and Times are displayed to the user IN THAT USER’S TIMEZONE. Data is stored in the database in UTC and converted to that user’s time zone when displaying to them here.
* Once you have added you dates, save to complete creation of this schedule.
* This schedule can be [linked to as many different Case processes](https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules/linking-a-schedule-to-a-case) as you desire
* If you wish to hide data from previous periods simply select the relevant flag on screen to do so.
  {% endhint %}

You can always edit the schedule and add more dates to it later on.

Once you have entered dates as desired, you should specify the Status of schedule (you can have it Paused, so it won’t take effect on anything yet, or Resumed, which means the schedule will be in effect and will start a Case for any Case processes it is linked to.

When editing a schedule, you are able to see the activity history of the schedule by clicking on the Show Activity button. You can see when the schedule was created and by who and you can see if any subsequent edits have been made, when they were made and by who.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpsorwRprqhClgfrRn%2Fimage.png?alt=media\&token=668cb8bc-010e-40ff-8955-0ef687aa7ee7)

You can now [link one or more Case processes to that schedule.](https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules/linking-a-schedule-to-a-case)

### Importing Schedule data from an excel file <a href="#d-import-schedule-from-excel-file" id="d-import-schedule-from-excel-file"></a>

In addition to adding new rows manually, you can also upload data for multiple periods using an excel sheet.

To do this, select the 'Import from file' option to bring up the ‘Schedule period bulk upload’ popup.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FqKs003AcbQl9DjjO6cL8%2Fimage.png?alt=media\&token=df123a45-35d1-45e8-a63d-3564884dcd1f)

Add an **.xls** or **xlsx** file with your data, click upload and the data will be added.

Once you've uploaded your file, new rows will be added to your screen containing the dates from your excel. If you’re happy with the uploaded dates, hit save to finish the upload process.

#### File Formatting Criteria

With regards to file formatting, the excel file needs to contain the all of the columns present in the schedule structure - i.e. a header row which matches the grid headings in the Schedule screen. This needs to include: period, year, start date plus all the custom-made schedule date titles you defined in your schedule structure.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpsy_iP92w8f3TwpYr%2Fimage.png?alt=media\&token=3c80f9b0-df17-4e51-b51a-5dd708a6752c)

### Exporting Schedule data in an excel file <a href="#d-import-schedule-from-excel-file" id="d-import-schedule-from-excel-file"></a>

You can export schedule data in an excel file via the export button.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F27nH3SNbDgCkA96P711R%2Fimage.png?alt=media&#x26;token=84714e35-dcec-498c-a84d-eed432a1b0f1" alt=""><figcaption></figcaption></figure>

### **Subsequently Changing the Schedule Status – Impact on Auto-Launching of Cases** <a href="#subsequently-changing-the-schedule-status-impact-on-auto-launching-of-cases" id="subsequently-changing-the-schedule-status-impact-on-auto-launching-of-cases"></a>

* Once a schedule has been created, you can subsequently go in and modify the data, including setting the status to paused / resumed.
* If you resume a schedule after a long period of pause, the system will play catch-up, i.e. it will launch a Case Work Item even for previous date periods - if no Case Work Item has yet been launched (the system tags Case Work Items in the background so it is aware of whether or not a Case has been launched for it).

### Viewing Expired/Expiring Schedules

You can easily view which schedules have already expired or are expiring soon and need you to upload more data on to keep their related processes running.

When you first go to the schedules screen, you'll see the number of schedules that have already expired at the top.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FaTuxO3DdO0e4bT0KoaCw%2Fimage.png?alt=media&#x26;token=dabb494e-e4b4-492b-ba19-8d370629cf40" alt=""><figcaption></figcaption></figure>

You can also use the filter function to see schedules that have already expired or are about to expire in certain time frames.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FTuxzmd81D85jHjvSgNoI%2Fimage-1.png?alt=media&#x26;token=ca409713-1f96-4d20-bb2d-ad4c8e3da736" alt=""><figcaption></figcaption></figure>

The options are:

* Already expired
* Expired/Expiring within next 7 days
* Expired/Expiring within next 30 days
* Expired/Expiring within next 90 days
* Select Date - here you can choose a custom date.
