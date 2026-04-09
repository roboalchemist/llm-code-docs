# luigi.process

Contains some helper functions to run luigid in daemon mode

Functions

`check_pid`(pidfile)

`daemonize`(cmd[, pidfile, logdir, api_port, ...])

`get_log_format`()

`get_spool_handler`(filename)

`write_pid`(pidfile)

luigi.process.check_pid(*pidfile*)

luigi.process.write_pid(*pidfile*)

luigi.process.get_log_format()

luigi.process.get_spool_handler(*filename*)

luigi.process.daemonize(*cmd*, *pidfile=None*, *logdir=None*, *api_port=8082*, *address=None*, *unix_socket=None*)