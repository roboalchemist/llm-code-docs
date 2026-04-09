# luigi.event

Definitions needed for events. See Events and callbacks for info on how to use it.

Classes

`Event`()

class luigi.event.Event

DEPENDENCY_DISCOVERED = 'event.core.dependency.discovered'

DEPENDENCY_MISSING = 'event.core.dependency.missing'

DEPENDENCY_PRESENT = 'event.core.dependency.present'

BROKEN_TASK = 'event.core.task.broken'

START = 'event.core.start'

PROGRESS = 'event.core.progress'

This event can be fired by the task itself while running. The purpose is
for the task to report progress, metadata or any generic info so that
event handler listening for this can keep track of the progress of running task.

FAILURE = 'event.core.failure'

SUCCESS = 'event.core.success'

PROCESSING_TIME = 'event.core.processing_time'

TIMEOUT = 'event.core.timeout'

PROCESS_FAILURE = 'event.core.process_failure'