# Source: https://www.hammerdb.com/docs4.0/ch05s03.html

Title: 3. Extending Autopilot to start automatically

URL Source: https://www.hammerdb.com/docs4.0/ch05s03.html

Markdown Content:
Autopilot can be started automatically by adding the keyword “auto” followed by the name of a script to run, this script must end in the extension .tcl.

./hammerdb auto
Usage: hammerdb [ auto [ script_to_autoload.tcl  ] ]

For example

./hammerdb auto newtpccscript.tcl
On doing so HammerDB will now load the script newtpccscript.tcl at startup and immediately enter the autopilot sequence defined in config.xml. Upon completion HammerDB will exit. This functionality enables the potential to run scripted workloads with the HammerDB GUI such as the following with multiple sequences of autopilot interspersed with a database refresh.

#!/bin/bash

set -e
SEQ1="4 6 8 10"
SEQ2="12 14 16 18"
SEQ3="20 22 24 26"
CONFIGFILE='/usr/local/hammerDB/config.xml'
RUNS=6

for x in $(eval echo "{1..$RUNS}")
do
        # Running a number of passes for this autopilot sequence
        echo "running run $x of $RUNS"

        for s in "$SEQ1" "$SEQ2" "$SEQ3"
        do
                echo "Running tests for series: $s"
                sed -i "s/<autopilot_sequence>.*<\/autopilot_sequence>/<autopilot_sequence>${s}<\/autopilot_sequence>/" $CONFIGFILE

                (cd /usr/local/hammerDB/ && ./hammerdb auto TPCC.postgres.tcl)

                echo "Reloading data"
                ssh postgres@postgres  '/var/lib/pgsql/reloadData.sh'
        done
done
