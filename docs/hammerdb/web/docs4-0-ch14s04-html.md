# Source: https://www.hammerdb.com/docs4.0/ch14s04.html

Title: 4. Capturing Errors from Trace File Workloads

URL Source: https://www.hammerdb.com/docs4.0/ch14s04.html

Markdown Content:
It must be remembered that although the previous workloads shown are suitable for directly replaying, with some applications replaying data from a previous transaction may result in constraint violations or updates of data that no longer exists that results in errors during replay. One of the most common error messages received is is the standard PL/SQL failure reported by Oratcl oraplexec: SQL execution failed. To get the actual Oracle error message underlying this error you can use the TCL "catch" command to capture the error and print it out inline. For example if you wanted to see the error in the neword procedure of the TPROC-C script change the oraplexec line to look like the following :

if {[ catch {oraplexec $curn1 $sql5 :no_w_id $no_w_id :no_max_w_id $w_id_input :no_d_id $no_d_id :no_c_id $no_c_id :no_o_ol_cnt $ol_cnt :no_c_discount {NULL} :no_c_last {NULL} :no_c_credit {NULL} :no_d_tax {NULL} :no_w_tax {NULL} :no_d_next_o_id {0} :timestamp $date} message]} {
puts $message
puts [ oramsg $curn1 all ]
}

So you are adding the statements as below to the oraplexec statement

if {[ catch { ... } message] } {
puts $message
puts [ oramsg $curn1 all ]
}

Note that the cursor variable $curn1 used in oramsg is the same variable used in the previous oraplexec. You can then run the script by pressing the test current code button ( or running one user thread with an output window ) The $message variable will contain and print out ( using the "puts" command ) any TCL error and the [ oramsg $curn1 all ] command will then print out the oracle error from the cursor $curn1. An example is if the procedure neword has not yet been created: This then gives the full output from Oracle as shown here instead of just the standard message :

new order
{6550 {ORA-06550: line 1, column 7:
PLS-00201: identifier 'NEWORD' must be declared
ORA-06550: line 1, column 7:
PL/SQL: Statement ignored} 0 0 4 8}
