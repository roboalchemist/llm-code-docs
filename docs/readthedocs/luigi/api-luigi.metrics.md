# luigi.metrics

Classes

`MetricsCollector`()

Abstractable MetricsCollector base class that can be replace by tool specific implementation.

`MetricsCollectors`(*values)

`NoMetricsCollector`()

Empty MetricsCollector when no collector is being used

class luigi.metrics.MetricsCollectors(**values*)

custom = -1

default = 1

none = 1

datadog = 2

prometheus = 3

classmethod get(*which*, *custom_import=None*)

class luigi.metrics.MetricsCollector

Abstractable MetricsCollector base class that can be replace by tool
specific implementation.

abstractmethod handle_task_started(*task*)

abstractmethod handle_task_failed(*task*)

abstractmethod handle_task_disabled(*task*, *config*)

abstractmethod handle_task_done(*task*)

handle_task_statistics(*task*, *statistics*)

generate_latest()

configure_http_handler(*http_handler*)

class luigi.metrics.NoMetricsCollector

Empty MetricsCollector when no collector is being used

handle_task_started(*task*)

handle_task_failed(*task*)

handle_task_disabled(*task*, *config*)

handle_task_done(*task*)