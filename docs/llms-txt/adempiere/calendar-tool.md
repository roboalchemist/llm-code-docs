# Source: https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/calendar-tool.md

# Calendar Tool

## Calendar

The Calendar Tool provides a calendar to set dates and times.

### &#x20;Access

| Access via ... | By using ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Icon:          | ![Image:Icon\_Calendar24.png](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fbvQ4zPvu-LU5m%2Fcalendar24.gif?generation=1550287161003296\&alt=media)<img src="https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MQKCscAcImifHC%2Fhistoryx24.webicon.png?generation=1550780746510474&#x26;alt=media" alt="" data-size="line"> |
| Menu:          | **Tools -> Calendar**                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Short Cut:     | (none)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Menu Tree:     | (none)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

{% hint style="info" %}
The calendar can also be enabled anytime you are entering date data by clicking on the calendar icon ![Image:Icon\_Calendar24.png](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fbvQ4zPvu-LU5m%2Fcalendar24.gif?generation=1550287161003296\&alt=media)<img src="https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MQKCscAcImifHC%2Fhistoryx24.webicon.png?generation=1550780746510474&#x26;alt=media" alt="" data-size="line"> in the date field.
{% endhint %}

### &#x20;Restrictions

* Dates from 1 January 1900 to 31 December 2100 are allowed.
* The timezone can't be set.
* Double click speed is hard-coded to 1 second.

### &#x20;Description

The Calendar tool provides a method to find dates using a standard month calendar. There are two forms of the Calendar tool, date only or date and time, as shown below. &#x20;

| Format      | Java Client                                                                                                                                                                                                                                                                            | Web                                                                                                                                                                                                                                                                             |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Date        | <img src="https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-M-Pcq6_gW5u_6Uc2rfx%2F-M-PdAV9AuchveoVY-SD%2Fswing_calendarTool_date.png?alt=media&#x26;token=fb08704e-8b67-4b15-a26a-023dd47f83c9" alt="" data-size="original">     | <img src="https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-M-Pcq6_gW5u_6Uc2rfx%2F-M-PgxQq-nKzs-uejdE4%2Fzk_calendarTool_date.png?alt=media&#x26;token=87f658e1-75cc-4ebd-b5b3-6728cf32076a" alt="" data-size="original"> |
| Date + Time | <img src="https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-M-Pcq6_gW5u_6Uc2rfx%2F-M-PdZDKDXJLdz-m1X3Q%2Fswing_calendarTool_dateTime.png?alt=media&#x26;token=6aebf9c8-019e-4207-a3ee-3057511878bc" alt="" data-size="original"> | The Web interface uses a separate field for the time element.                                                                                                                                                                                                                   |

Which form appears depends on the data type of the field being entered. The menu link and most date fields are [date only](https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons/date-field). The time portion will appear if the data type is set to [date & time (time stamp)](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Date.2BTime).

The Web version of the control is much simpler and only allows selection of a date.

Using the Java Client Calendar tool is easy. Use the controls to select the month and year and then **double click** the date. For the date/time version, there is also a handy check mark icon which you can click.

There are three icons to assist you:

* &#x20;C - Clear - will clear the date in the date field
* &#x20;x - Cancel - close the Calendar tool, making no changes
* &#x20;\* - Today - set today's date

The following keyboard controls can be used:

* &#x20;\<Pg Dn> will increment the month
* &#x20;\<Pg Up> will decrement the month
* &#x20;\<Up Arrow> will decrement by a week
* &#x20;\<Down Arrow> will increment by a week
* &#x20;\<Left Arrow> will decrement by a day
* &#x20;\<Right Arrow> will increment by a day
* &#x20;\<Enter> will close the Calendar tool, saving the date/time if the tool was opened from a field.
* &#x20;\<Esc> will cancel the and close the tool.

### &#x20;See Also

* [Entering Data - Fields and Buttons](https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons)
* [Date Field](https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons/date-field)
* [Date + Time Field](https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons/date-+-time-field)
