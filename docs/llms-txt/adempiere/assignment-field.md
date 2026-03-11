# Source: https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons/assignment-field.md

# Assignment Field

![Assignment Field example](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r-CZMvdfyTgatli%2Fswing_field_assignmentexample.PNG?generation=1551809344729523\&alt=media)

Icon: ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r-EgqIh61MMUCci%2Fassignment24.gif?generation=1551809344740125\&alt=media)

The Resource Assignment field provides a way to assign resources to schedule slots. If a resource assignment exists, the field will show the resource name, the date of the assignment and the number of slots used or it will display the resource assignment ID.

The Assignment field is typically found on the **Sales Order** window on the **Order Line** tab.

There is no way to enter data directly in the field. You have to use the helper functions. Clicking the Assignment helper function ( ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r-GBsaybgXcb9lJ%2Fassignment24.gif?generation=1551809344720715\&alt=media) ) will do the following:

* If the Assignment field is blank, it will open the [Schedule Info](http://wiki.adempiere.net/Schedule_Info) window where you can double-click on a the starting schedule slot. The double-click will open the [Resource Assignment Dialog](http://wiki.adempiere.net/Resource_Assignment_Dialog) which displays information about the assignment.
* If the assignment already exists, the [Resource Assignment Dialog](http://wiki.adempiere.net/Resource_Assignment_Dialog) will open directly.

Confirming and closing the [Resource Assignment Dialog](http://wiki.adempiere.net/Resource_Assignment_Dialog) will save the assignment to the Assignment field. Canceling the Resource Assignment Dialog will clear the Assignment field.

The pop-up menu (mouse right-click) will display the following entries:

* [![Image:Icon\_Zoom24.png](http://wiki.adempiere.net/images/7/7c/Icon_Zoom24.png)](http://wiki.adempiere.net/File:Icon_Zoom24.png) Resource Info
* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) Change Log

For more information see:

* Schedule Info
* Resource Info
* Resource Assignment Dialog
