# Source: https://www.hammerdb.com/docs4.0/ch09s02.html

Title: 2. CLI Commands

URL Source: https://www.hammerdb.com/docs4.0/ch09s02.html

Markdown Content:
buildschema Usage: buildschema Runs the schema build for the database and benchmark selected with dbset and variables selected with diset. Equivalent to the Build command in the graphical interface. Note that the buildschema command will assume the "yes" reply to the Yes or no prompt to proceed with the schema build. This is to prevent the stalling of CLI scripts during builds.
clearscript Usage: clearscript Clears the script. Equivalent to the "Clear the Screen" button in the graphical interface.
customscript Usage: customscript scriptname.tcl Load an external script. Equivalent to the "Open Existing File" button in the graphical interface.
datagenrun Usage: datagenrun Run Data Generation. Equivalent to the Generate option in the graphical interface.
dbset Usage: dbset [db|bm] value Sets the database (db) or benchmark (bm). Equivalent to the Benchmark Menu in the graphical interface. Database value is set by the database prefix in the XML configuration.
dgset Usage: dgset [vu|ware|directory]Set the Datagen options. Equivalent to the Datagen Options dialog in the graphical interface.
diset Usage: diset dict key value Set the dictionary variables for the current database. Equivalent to the Schema Build and Driver Options windows in the graphical interface. Use "print dict" to see what these variables area and diset to change: Example: hammerdb>diset tpcc count_ware 10 Changed tpcc:count_ware from 1 to 10 for Oracle.
distributescript Usage: distributescript In Master mode distributes the script loaded by Master to the connected Slaves.
librarycheck Usage: librarycheck Attempts to load the vendor provided 3rd party library for all databases and reports whether the attempt was successful.
loadscript Usage: loadscript Load the script for the database and benchmark set with dbset and the dictionary variables set with diset. Use "print script" to see the script that is loaded. Equivalent to loading a Driver Script in the Script Editor window in the graphical interface.
print Usage: print [db|bm|dict|script|vuconf |vucreated|vustatus|datagen]prints the current configuration: db: database bm: benchmark dict: the dictionary for the current database ie all active variables script: the loaded script vuconf: the virtual user configuration vucreated: the number of virtual users created vustatus: the status of the virtual users datagen : the configuration to build when datagen is run
quit Usage: quit Shuts down the HammerDB CLI.Calls the exit command and terminates the CLI interface
runtimer runtimer - Usage: runtimer seconds Helper routine to run a timer in the main hammerdbcli thread to keep it busy for a period of time whilst the virtual users run a workload. The timer will return when vucomplete returns true or the timer reaches the seconds value. Usually followed by vudestroy.
switchmode Usage: switchmode [mode] ?PrimaryID? ?PrimaryHostname?Changes the remote mode to Primary, Replica or Local. When Master it will report an id and a hostname. Equivalent to the Mode option in the graphical interface. Mode to switch to must be one of Local, Primary or Replica. If Mode is Replica then the ID and Hostname of the Primary to connect to must be given.
vucomplete Usage: vucomplete Returns "true" or "false" depending on whether all virtual users that started a workload have completed regardless of whether the status was "FINISH SUCCESS" or "FINISH FAILED".
vucreate Usage: vucreate Create the virtual users. Equivalent to the Virtual User Create option in the graphical interface. Use "print vucreated" to see the number created, vustatus to see the status and vucomplete to see whether all active virtual users have finished the workload. A script must be loaded before virtual users can be created.
vudestroy Usage: vudestroy Destroy the virtual users. Equivalent to the Destroy Virtual Users button in the graphical interface that replaces the Create Virtual Users button after virtual user creation.
vurun Usage: vurun Send the loaded script to the created virtual users for execution. Equivalent to the Run command in the graphical interface.
vuset Usage: vuset [vu|delay|repeat|iterations|showoutput |logtotemp|unique|nobuff|timestamps Configure the virtual user options. Equivalent to the Virtual User Options window in the graphical interface.
vustatus Usage: vustatus Show the status of virtual users. Status will be "WAIT IDLE" for virtual users that are created but not running a workload,"RUNNING" for virtual users that are running a workload, "FINISH SUCCESS" for virtual users that completed successfully or "FINISH FAILED" for virtual users that encountered an error.
waittocomplete Usage: waittocomplete Helper routine to enable the main hammerdbcli thread to keep it busy until vucomplete is detected. When vucomplete is detected exit is called causing all virtual users and the main hammerdblci thread to terminate. Often used when calling hammerdb from external scripting commands.
