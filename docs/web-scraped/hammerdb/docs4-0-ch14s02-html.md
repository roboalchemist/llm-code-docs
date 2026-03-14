# Source: https://www.hammerdb.com/docs4.0/ch14s02.html

Title: 2. Converting Oracle Trace Files

URL Source: https://www.hammerdb.com/docs4.0/ch14s02.html

Markdown Content:
It is important to note that to convert Oracle trace files you must have selected Oracle from the treeview. If another database is selected the button to convert Oracle trace files is disabled Copy the trace file to the client machine or location where HammerDB is running and use the File:Open menu option or the “Open an existing file button” under the Edit Menu to display the Open File dialogue

**Figure 14.2.Open File**

![Image 1: Open File](https://www.hammerdb.com/docs4.0/resources/ch12-2.PNG)

The Open File dialog allows the specifying of the Directory and a filter for the file type, by default this is *.tcl. Change the file extension to ‘trc’ and change directory to the location of your files, select the trace file you previously generated and select OK.

**Figure 14.3.Trace Loaded**

![Image 2: Trace Loaded](https://www.hammerdb.com/docs4.0/resources/ch12-3.PNG)

Select the Trace Conversion button at the bottom of the Edit menu

**Figure 14.4.Convert Trace**

![Image 3: Convert Trace](https://www.hammerdb.com/docs4.0/resources/ch12-4.PNG)

and the trace file is converted into a format that can replayed against the database.

**Figure 14.5.Trace Converted**

![Image 4: Trace Converted](https://www.hammerdb.com/docs4.0/resources/ch12-5.PNG)

Note that the trace file never records a users’ authentication details. Therefore the connect string must always be modified manually after conversion. Remove the comment before the “set connect” line on line 4 and enter the correct username and password. The SID will be set by default to the SID that the trace file was taken from and therefore if using a pluggable database then the correct container must also be set to the correct identifier. Once the connect string is updated the generated script is ready for running against the database and contains the original statements that were traced. The save menu option or “Save current file” button can be used to save the generated script for reloading at a later point in time.
