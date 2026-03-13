# luigi.setup_logging

This module contains helper classes for configuring logging for luigid and
workers via command line arguments and options from config files.

Classes

`BaseLogging`()

`DaemonLogging`()

Configure logging for luigid

`InterfaceLogging`()

Configure logging for worker

class luigi.setup_logging.BaseLogging

config = <luigi.configuration.cfg_parser.LuigiConfigParser object>

classmethod setup(*opts=<class 'luigi.setup_logging.opts'>*)

Setup logging via CLI params and config.

class luigi.setup_logging.DaemonLogging

Configure logging for luigid

class luigi.setup_logging.InterfaceLogging

Configure logging for worker