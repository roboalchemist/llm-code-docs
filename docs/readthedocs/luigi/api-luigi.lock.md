# luigi.lock

Locking functionality when launching things from the command line.
Uses a pidfile.
This prevents multiple identical workflows to be launched simultaneously.

Functions

`acquire_for`(pid_dir[, num_available, ...])

Makes sure the process is only run once at the same time with the same name.

`get_info`(pid_dir[, my_pid])

`getpcmd`(pid)

Returns command of process.

luigi.lock.getpcmd(*pid*)

Returns command of process.

Parameters:

**pid**

luigi.lock.get_info(*pid_dir*, *my_pid=None*)

luigi.lock.acquire_for(*pid_dir*, *num_available=1*, *kill_signal=None*)

Makes sure the process is only run once at the same time with the same name.

Notice that we since we check the process name, different parameters to the same
command can spawn multiple processes at the same time, i.e. running
“/usr/bin/my_process” does not prevent anyone from launching
“/usr/bin/my_process –foo bar”.