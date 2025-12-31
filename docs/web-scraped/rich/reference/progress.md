# Source: https://rich.readthedocs.io/en/latest/reference/progress.html

[]

# rich.progress[](#module-rich.progress "Link to this heading")

*[[class]][ ]*[[rich.progress.]][[BarColumn]][(]*[[bar_width]][[=]][[40]]*, *[[style]][[=]][[\'bar.back\']]*, *[[complete_style]][[=]][[\'bar.complete\']]*, *[[finished_style]][[=]][[\'bar.finished\']]*, *[[pulse_style]][[=]][[\'bar.pulse\']]*, *[[table_column]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/progress.html#BarColumn)[](#rich.progress.BarColumn "Link to this definition")

:   Renders a visual progress bar.

    Parameters[:]

    :   -   **bar_width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Width of bar or None for full width. Defaults to 40.

        -   **style** (*StyleType,* *optional*) -- Style for the bar background. Defaults to "bar.back".

        -   **complete_style** (*StyleType,* *optional*) -- Style for the completed bar. Defaults to "bar.complete".

        -   **finished_style** (*StyleType,* *optional*) -- Style for a finished bar. Defaults to "bar.finished".

        -   **pulse_style** (*StyleType,* *optional*) -- Style for pulsing bars. Defaults to "bar.pulse".

        -   **table_column** (*Optional\[*[*Column*](table.html#rich.table.Column "rich.table.Column")*\]*)

    [[render]][(]*[[task]]*[)][[[\[source\]]]](../_modules/rich/progress.html#BarColumn.render)[](#rich.progress.BarColumn.render "Link to this definition")

    :   Gets a progress bar widget for a task.

        Parameters[:]

        :   **task** ([*Task*](#rich.progress.Task "rich.progress.Task"))

        Return type[:]

        :   [*ProgressBar*](progress_bar.html#rich.progress_bar.ProgressBar "rich.progress_bar.ProgressBar")

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[DownloadColumn]][(]*[[binary_units]][[=]][[False]]*, *[[table_column]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/progress.html#DownloadColumn)[](#rich.progress.DownloadColumn "Link to this definition")

:   Renders file size downloaded and total, e.g. '0.5/2.3 GB'.

    Parameters[:]

    :   -   **binary_units** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Use binary units, KiB, MiB etc. Defaults to False.

        -   **table_column** (*Optional\[*[*Column*](table.html#rich.table.Column "rich.table.Column")*\]*)

    [[render]][(]*[[task]]*[)][[[\[source\]]]](../_modules/rich/progress.html#DownloadColumn.render)[](#rich.progress.DownloadColumn.render "Link to this definition")

    :   Calculate common unit for completed and total.

        Parameters[:]

        :   **task** ([*Task*](#rich.progress.Task "rich.progress.Task"))

        Return type[:]

        :   [*Text*](text.html#rich.text.Text "rich.text.Text")

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[FileSizeColumn]][(]*[[table_column]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/progress.html#FileSizeColumn)[](#rich.progress.FileSizeColumn "Link to this definition")

:   Renders completed filesize.

    Parameters[:]

    :   **table_column** (*Optional\[*[*Column*](table.html#rich.table.Column "rich.table.Column")*\]*)

    [[render]][(]*[[task]]*[)][[[\[source\]]]](../_modules/rich/progress.html#FileSizeColumn.render)[](#rich.progress.FileSizeColumn.render "Link to this definition")

    :   Show data completed.

        Parameters[:]

        :   **task** ([*Task*](#rich.progress.Task "rich.progress.Task"))

        Return type[:]

        :   [*Text*](text.html#rich.text.Text "rich.text.Text")

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[MofNCompleteColumn]][(]*[[separator]][[=]][[\'/\']]*, *[[table_column]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/progress.html#MofNCompleteColumn)[](#rich.progress.MofNCompleteColumn "Link to this definition")

:   Renders completed count/total, e.g. ' 10/1000'.

    Best for bounded tasks with int quantities.

    Space pads the completed count so that progress length does not change as task progresses past powers of 10.

    Parameters[:]

    :   -   **separator** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Text to separate completed and total values. Defaults to "/".

        -   **table_column** (*Optional\[*[*Column*](table.html#rich.table.Column "rich.table.Column")*\]*)

    [[render]][(]*[[task]]*[)][[[\[source\]]]](../_modules/rich/progress.html#MofNCompleteColumn.render)[](#rich.progress.MofNCompleteColumn.render "Link to this definition")

    :   Show completed/total.

        Parameters[:]

        :   **task** ([*Task*](#rich.progress.Task "rich.progress.Task"))

        Return type[:]

        :   [*Text*](text.html#rich.text.Text "rich.text.Text")

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[Progress]][(]*[[\*]][[columns]]*, *[[console]][[=]][[None]]*, *[[auto_refresh]][[=]][[True]]*, *[[refresh_per_second]][[=]][[10]]*, *[[speed_estimate_period]][[=]][[30.0]]*, *[[transient]][[=]][[False]]*, *[[redirect_stdout]][[=]][[True]]*, *[[redirect_stderr]][[=]][[True]]*, *[[get_time]][[=]][[None]]*, *[[disable]][[=]][[False]]*, *[[expand]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/progress.html#Progress)[](#rich.progress.Progress "Link to this definition")

:   Renders an auto-updating progress bar(s).

    Parameters[:]

    :   -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")*,* *optional*) -- Optional Console instance. Defaults to an internal Console instance writing to stdout.

        -   **auto_refresh** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable auto refresh. If disabled, you will need to call refresh().

        -   **refresh_per_second** (*Optional\[*[*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*\],* *optional*) -- Number of times per second to refresh the progress information or None to use default (10). Defaults to None.

        -   **speed_estimate_period** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")) -- (float, optional): Period (in seconds) used to calculate the speed estimate. Defaults to 30.

        -   **transient** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")) -- (bool, optional): Clear the progress on exit. Defaults to False.

        -   **redirect_stdout** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")) -- (bool, optional): Enable redirection of stdout, so [`print`] may be used. Defaults to True.

        -   **redirect_stderr** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")) -- (bool, optional): Enable redirection of stderr. Defaults to True.

        -   **get_time** (*Optional\[GetTimeCallable\]*) -- (Callable, optional): A callable that gets the current time, or None to use Console.get_time. Defaults to None.

        -   **disable** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Disable progress display. Defaults to False

        -   **expand** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Expand tasks table to fit width. Defaults to False.

        -   **columns** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*ProgressColumn*](#rich.progress.ProgressColumn "rich.progress.ProgressColumn")*\]*)

    [[add_task]][(]*[[description]]*, *[[start]][[=]][[True]]*, *[[total]][[=]][[100.0]]*, *[[completed]][[=]][[0]]*, *[[visible]][[=]][[True]]*, *[[\*\*]][[fields]]*[)][[[\[source\]]]](../_modules/rich/progress.html#Progress.add_task)[](#rich.progress.Progress.add_task "Link to this definition")

    :   Add a new 'task' to the Progress display.

        Parameters[:]

        :   -   **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- A description of the task.

            -   **start** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Start the task immediately (to calculate elapsed time). If set to False, you will need to call start manually. Defaults to True.

            -   **total** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Number of total steps in the progress if known. Set to None to render a pulsing animation. Defaults to 100.

            -   **completed** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Number of steps completed so far. Defaults to 0.

            -   **visible** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable display of the task. Defaults to True.

            -   **\*\*fields** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Additional data fields required for rendering.

        Returns[:]

        :   An ID you can use when calling update.

        Return type[:]

        :   TaskID

    [[advance]][(]*[[task_id]]*, *[[advance]][[=]][[1]]*[)][[[\[source\]]]](../_modules/rich/progress.html#Progress.advance)[](#rich.progress.Progress.advance "Link to this definition")

    :   Advance task by a number of steps.

        Parameters[:]

        :   -   **task_id** (*TaskID*) -- ID of task.

            -   **advance** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")) -- Number of steps to advance. Default is 1.

        Return type[:]

        :   None

    *[[property]][ ]*[[finished]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.progress.Progress.finished "Link to this definition")

    :   Check if all tasks have been completed.

    *[[classmethod]][ ]*[[get_default_columns]][(][)][[[\[source\]]]](../_modules/rich/progress.html#Progress.get_default_columns)[](#rich.progress.Progress.get_default_columns "Link to this definition")

    :   

        Get the default columns used for a new Progress instance:

        :   -   a text column for the description (TextColumn)

            -   the bar itself (BarColumn)

            -   a text column showing completion percentage (TextColumn)

            -   an estimated-time-remaining column (TimeRemainingColumn)

        If the Progress instance is created without passing a columns argument, the default columns defined here will be used.

        You can also create a Progress instance using custom columns before and/or after the defaults, as in this example:

        > <div>
        >
        > progress = Progress(
        >
        > :   SpinnerColumn(), [[\*]](#id1)Progress.get_default_columns(), "Elapsed:", TimeElapsedColumn(),
        >
        > )
        >
        > </div>

        This code shows the creation of a Progress display, containing a spinner to the left, the default columns, and a labeled elapsed time column.

        Return type[:]

        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")\[[*ProgressColumn*](#rich.progress.ProgressColumn "rich.progress.ProgressColumn"), ...\]

    [[get_renderable]][(][)][[[\[source\]]]](../_modules/rich/progress.html#Progress.get_renderable)[](#rich.progress.Progress.get_renderable "Link to this definition")

    :   Get a renderable for the progress display.

        Return type[:]

        :   [*ConsoleRenderable*](console.html#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable") \| [*RichCast*](console.html#rich.console.RichCast "rich.console.RichCast") \| [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    [[get_renderables]][(][)][[[\[source\]]]](../_modules/rich/progress.html#Progress.get_renderables)[](#rich.progress.Progress.get_renderables "Link to this definition")

    :   Get a number of renderables for the progress display.

        Return type[:]

        :   [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.13)")\[[*ConsoleRenderable*](console.html#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable") \| [*RichCast*](console.html#rich.console.RichCast "rich.console.RichCast") \| [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]

    [[make_tasks_table]][(]*[[tasks]]*[)][[[\[source\]]]](../_modules/rich/progress.html#Progress.make_tasks_table)[](#rich.progress.Progress.make_tasks_table "Link to this definition")

    :   Get a table to render the Progress display.

        Parameters[:]

        :   **tasks** (*Iterable\[*[*Task*](#rich.progress.Task "rich.progress.Task")*\]*) -- An iterable of Task instances, one per row of the table.

        Returns[:]

        :   A table instance.

        Return type[:]

        :   [Table](table.html#rich.table.Table "rich.table.Table")

    [[open]][(]*[[file]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[PathLike]](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.13)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[[\]]][ ][[\|]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.13)")]*, *[[mode]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[[\[]][[\'rb\']][[\]]]]*, *[[buffering]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")][ ][[=]][ ][[-1]]*, *[[encoding]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[errors]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[newline]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[total]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[task_id]][[:]][ ][[TaskID][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[description]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")][ ][[=]][ ][[\'Reading\...\']]*[)] [[→] [[[BinaryIO]](https://docs.python.org/3/library/typing.html#typing.BinaryIO "(in Python v3.13)")]][[[\[source\]]]](../_modules/rich/progress.html#Progress.open)[](#rich.progress.Progress.open "Link to this definition")\
    [[open]][(]*[[file]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[PathLike]](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.13)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[[\]]][ ][[\|]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.13)")]*, *[[mode]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[[\[]][[\'r\']][[,]][ ][[\'rt\']][[\]]]]*, *[[buffering]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")][ ][[=]][ ][[-1]]*, *[[encoding]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[errors]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[newline]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[total]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[task_id]][[:]][ ][[TaskID][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[description]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")][ ][[=]][ ][[\'Reading\...\']]*[)] [[→] [[[TextIO]](https://docs.python.org/3/library/typing.html#typing.TextIO "(in Python v3.13)")]]

    :   Track progress while reading from a binary file.

        Parameters[:]

        :   -   **path** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *PathLike\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]\]*) -- The path to the file to read.

            -   **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- The mode to use to open the file. Only supports "r", "rb" or "rt".

            -   **buffering** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- The buffering strategy to use, see [[`io.open()`]](https://docs.python.org/3/library/io.html#io.open "(in Python v3.13)").

            -   **encoding** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- The encoding to use when reading in text mode, see [[`io.open()`]](https://docs.python.org/3/library/io.html#io.open "(in Python v3.13)").

            -   **errors** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- The error handling strategy for decoding errors, see [[`io.open()`]](https://docs.python.org/3/library/io.html#io.open "(in Python v3.13)").

            -   **newline** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- The strategy for handling newlines in text mode, see [[`io.open()`]](https://docs.python.org/3/library/io.html#io.open "(in Python v3.13)").

            -   **total** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Total number of bytes to read. If none given, os.stat(path).st_size is used.

            -   **task_id** (*TaskID*) -- Task to track. Default is new task.

            -   **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Description of task, if new task is created.

        Returns[:]

        :   A readable file-like object in binary mode.

        Return type[:]

        :   BinaryIO

        Raises[:]

        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.13)") -- When an invalid mode is given.

    [[refresh]][(][)][[[\[source\]]]](../_modules/rich/progress.html#Progress.refresh)[](#rich.progress.Progress.refresh "Link to this definition")

    :   Refresh (render) the progress information.

        Return type[:]

        :   None

    [[remove_task]][(]*[[task_id]]*[)][[[\[source\]]]](../_modules/rich/progress.html#Progress.remove_task)[](#rich.progress.Progress.remove_task "Link to this definition")

    :   Delete a task if it exists.

        Parameters[:]

        :   **task_id** (*TaskID*) -- A task ID.

        Return type[:]

        :   None

    [[reset]][(]*[[task_id]]*, *[[\*]]*, *[[start]][[=]][[True]]*, *[[total]][[=]][[None]]*, *[[completed]][[=]][[0]]*, *[[visible]][[=]][[None]]*, *[[description]][[=]][[None]]*, *[[\*\*]][[fields]]*[)][[[\[source\]]]](../_modules/rich/progress.html#Progress.reset)[](#rich.progress.Progress.reset "Link to this definition")

    :   Reset a task so completed is 0 and the clock is reset.

        Parameters[:]

        :   -   **task_id** (*TaskID*) -- ID of task.

            -   **start** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Start the task after reset. Defaults to True.

            -   **total** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- New total steps in task, or None to use current total. Defaults to None.

            -   **completed** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Number of steps completed. Defaults to 0.

            -   **visible** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable display of the task. Defaults to True.

            -   **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Change task description if not None. Defaults to None.

            -   **\*\*fields** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Additional data fields required for rendering.

        Return type[:]

        :   None

    [[start]][(][)][[[\[source\]]]](../_modules/rich/progress.html#Progress.start)[](#rich.progress.Progress.start "Link to this definition")

    :   Start the progress display.

        Return type[:]

        :   None

    [[start_task]][(]*[[task_id]]*[)][[[\[source\]]]](../_modules/rich/progress.html#Progress.start_task)[](#rich.progress.Progress.start_task "Link to this definition")

    :   Start a task.

        Starts a task (used when calculating elapsed time). You may need to call this manually, if you called [`add_task`] with [`start=False`].

        Parameters[:]

        :   **task_id** (*TaskID*) -- ID of task.

        Return type[:]

        :   None

    [[stop]][(][)][[[\[source\]]]](../_modules/rich/progress.html#Progress.stop)[](#rich.progress.Progress.stop "Link to this definition")

    :   Stop the progress display.

        Return type[:]

        :   None

    [[stop_task]][(]*[[task_id]]*[)][[[\[source\]]]](../_modules/rich/progress.html#Progress.stop_task)[](#rich.progress.Progress.stop_task "Link to this definition")

    :   Stop a task.

        This will freeze the elapsed time on the task.

        Parameters[:]

        :   **task_id** (*TaskID*) -- ID of task.

        Return type[:]

        :   None

    *[[property]][ ]*[[task_ids]]*[[:]][ ][[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")[[\[]][TaskID][[\]]]*[](#rich.progress.Progress.task_ids "Link to this definition")

    :   A list of task IDs.

    *[[property]][ ]*[[tasks]]*[[:]][ ][[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")[[\[]][[Task]](#rich.progress.Task "rich.progress.Task")[[\]]]*[](#rich.progress.Progress.tasks "Link to this definition")

    :   Get a list of Task instances.

    [[track]][(]*[[sequence]]*, *[[total]][[=]][[None]]*, *[[completed]][[=]][[0]]*, *[[task_id]][[=]][[None]]*, *[[description]][[=]][[\'Working\...\']]*, *[[update_period]][[=]][[0.1]]*[)][[[\[source\]]]](../_modules/rich/progress.html#Progress.track)[](#rich.progress.Progress.track "Link to this definition")

    :   Track progress by iterating over a sequence.

        You can also track progress of an iterable, which might require that you additionally specify [`total`].

        Parameters[:]

        :   -   **sequence** (*Iterable\[ProgressType\]*) -- Values you want to iterate over and track progress.

            -   **total** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") *\|* *None*) -- (float, optional): Total number of steps. Default is len(sequence).

            -   **completed** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Number of steps completed so far. Defaults to 0.

            -   **task_id** (*TaskID* *\|* *None*) -- (TaskID): Task to track. Default is new task.

            -   **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- (str, optional): Description of task, if new task is created.

            -   **update_period** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Minimum time (in seconds) between calls to update(). Defaults to 0.1.

        Returns[:]

        :   An iterable of values taken from the provided sequence.

        Return type[:]

        :   Iterable\[ProgressType\]

    [[update]][(]*[[task_id]]*, *[[\*]]*, *[[total]][[=]][[None]]*, *[[completed]][[=]][[None]]*, *[[advance]][[=]][[None]]*, *[[description]][[=]][[None]]*, *[[visible]][[=]][[None]]*, *[[refresh]][[=]][[False]]*, *[[\*\*]][[fields]]*[)][[[\[source\]]]](../_modules/rich/progress.html#Progress.update)[](#rich.progress.Progress.update "Link to this definition")

    :   Update information associated with a task.

        Parameters[:]

        :   -   **task_id** (*TaskID*) -- Task id (returned by add_task).

            -   **total** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Updates task.total if not None.

            -   **completed** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Updates task.completed if not None.

            -   **advance** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Add a value to task.completed if not None.

            -   **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Change task description if not None.

            -   **visible** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Set visible flag if not None.

            -   **refresh** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")) -- Force a refresh of progress information. Default is False.

            -   **\*\*fields** (*Any*) -- Additional data fields required for rendering.

        Return type[:]

        :   None

    [[wrap_file]][(]*[[file]]*, *[[total]][[=]][[None]]*, *[[\*]]*, *[[task_id]][[=]][[None]]*, *[[description]][[=]][[\'Reading\...\']]*[)][[[\[source\]]]](../_modules/rich/progress.html#Progress.wrap_file)[](#rich.progress.Progress.wrap_file "Link to this definition")

    :   Track progress file reading from a binary file.

        Parameters[:]

        :   -   **file** (*BinaryIO*) -- A file-like object opened in binary mode.

            -   **total** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Total number of bytes to read. This must be provided unless a task with a total is also given.

            -   **task_id** (*TaskID*) -- Task to track. Default is new task.

            -   **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Description of task, if new task is created.

        Returns[:]

        :   A readable file-like object in binary mode.

        Return type[:]

        :   BinaryIO

        Raises[:]

        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.13)") -- When no total value can be extracted from the arguments or the task.

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[ProgressColumn]][(]*[[table_column]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/progress.html#ProgressColumn)[](#rich.progress.ProgressColumn "Link to this definition")

:   Base class for a widget to use in progress display.

    Parameters[:]

    :   **table_column** (*Optional\[*[*Column*](table.html#rich.table.Column "rich.table.Column")*\]*)

    [[get_table_column]][(][)][[[\[source\]]]](../_modules/rich/progress.html#ProgressColumn.get_table_column)[](#rich.progress.ProgressColumn.get_table_column "Link to this definition")

    :   Get a table column, used to build tasks table.

        Return type[:]

        :   [*Column*](table.html#rich.table.Column "rich.table.Column")

    *[[abstractmethod]][ ]*[[render]][(]*[[task]]*[)][[[\[source\]]]](../_modules/rich/progress.html#ProgressColumn.render)[](#rich.progress.ProgressColumn.render "Link to this definition")

    :   Should return a renderable object.

        Parameters[:]

        :   **task** ([*Task*](#rich.progress.Task "rich.progress.Task"))

        Return type[:]

        :   [*ConsoleRenderable*](console.html#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable") \| [*RichCast*](console.html#rich.console.RichCast "rich.console.RichCast") \| [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[ProgressSample]][(]*[[timestamp]]*, *[[completed]]*[)][[[\[source\]]]](../_modules/rich/progress.html#ProgressSample)[](#rich.progress.ProgressSample "Link to this definition")

:   Sample of progress for a given time.

    Parameters[:]

    :   -   **timestamp** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"))

        -   **completed** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"))

    [[completed]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*[](#rich.progress.ProgressSample.completed "Link to this definition")

    :   Number of steps completed.

    [[timestamp]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*[](#rich.progress.ProgressSample.timestamp "Link to this definition")

    :   Timestamp of sample.

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[RenderableColumn]][(]*[[renderable]][[=]][[\'\']]*, *[[\*]]*, *[[table_column]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/progress.html#RenderableColumn)[](#rich.progress.RenderableColumn "Link to this definition")

:   A column to insert an arbitrary column.

    Parameters[:]

    :   -   **renderable** (*RenderableType,* *optional*) -- Any renderable. Defaults to empty string.

        -   **table_column** (*Optional\[*[*Column*](table.html#rich.table.Column "rich.table.Column")*\]*)

    [[render]][(]*[[task]]*[)][[[\[source\]]]](../_modules/rich/progress.html#RenderableColumn.render)[](#rich.progress.RenderableColumn.render "Link to this definition")

    :   Should return a renderable object.

        Parameters[:]

        :   **task** ([*Task*](#rich.progress.Task "rich.progress.Task"))

        Return type[:]

        :   [*ConsoleRenderable*](console.html#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable") \| [*RichCast*](console.html#rich.console.RichCast "rich.console.RichCast") \| [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[SpinnerColumn]][(]*[[spinner_name]][[=]][[\'dots\']]*, *[[style]][[=]][[\'progress.spinner\']]*, *[[speed]][[=]][[1.0]]*, *[[finished_text]][[=]][[\'] [\']]*, *[[table_column]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/progress.html#SpinnerColumn)[](#rich.progress.SpinnerColumn "Link to this definition")

:   A column with a 'spinner' animation.

    Parameters[:]

    :   -   **spinner_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Name of spinner animation. Defaults to "dots".

        -   **style** (*StyleType,* *optional*) -- Style of spinner. Defaults to "progress.spinner".

        -   **speed** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Speed factor of spinner. Defaults to 1.0.

        -   **finished_text** (*TextType,* *optional*) -- Text used when task is finished. Defaults to " ".

        -   **table_column** (*Optional\[*[*Column*](table.html#rich.table.Column "rich.table.Column")*\]*)

    [[render]][(]*[[task]]*[)][[[\[source\]]]](../_modules/rich/progress.html#SpinnerColumn.render)[](#rich.progress.SpinnerColumn.render "Link to this definition")

    :   Should return a renderable object.

        Parameters[:]

        :   **task** ([*Task*](#rich.progress.Task "rich.progress.Task"))

        Return type[:]

        :   [*ConsoleRenderable*](console.html#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable") \| [*RichCast*](console.html#rich.console.RichCast "rich.console.RichCast") \| [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    [[set_spinner]][(]*[[spinner_name]]*, *[[spinner_style]][[=]][[\'progress.spinner\']]*, *[[speed]][[=]][[1.0]]*[)][[[\[source\]]]](../_modules/rich/progress.html#SpinnerColumn.set_spinner)[](#rich.progress.SpinnerColumn.set_spinner "Link to this definition")

    :   Set a new spinner.

        Parameters[:]

        :   -   **spinner_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Spinner name, see python -m rich.spinner.

            -   **spinner_style** (*Optional\[StyleType\],* *optional*) -- Spinner style. Defaults to "progress.spinner".

            -   **speed** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Speed factor of spinner. Defaults to 1.0.

        Return type[:]

        :   None

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[Task]][(]*[[id]]*, *[[description]]*, *[[total]]*, *[[completed]]*, *[[\_get_time]]*, *[[finished_time=None]]*, *[[visible=True]]*, *[[fields=\<factory\>]]*, *[[finished_speed=None]]*, *[[\_lock=\<factory\>]]*[)][[[\[source\]]]](../_modules/rich/progress.html#Task)[](#rich.progress.Task "Link to this definition")

:   Information regarding a progress task.

    This object should be considered read-only outside of the [[`Progress`]](#rich.progress.Progress "rich.progress.Progress") class.

    Parameters[:]

    :   -   **id** (*TaskID*)

        -   **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **total** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") *\|* *None*)

        -   **completed** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"))

        -   **\_get_time** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.13)")*\[\[\],* [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*\]*)

        -   **finished_time** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") *\|* *None*)

        -   **visible** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **fields** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.13)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)")*\]*)

        -   **finished_speed** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") *\|* *None*)

        -   **\_lock** ([*RLock*](https://docs.python.org/3/library/threading.html#threading.RLock "(in Python v3.13)"))

    [[completed]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*[](#rich.progress.Task.completed "Link to this definition")

    :   Number of steps completed

        Type[:]

        :   [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

    [[description]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*[](#rich.progress.Task.description "Link to this definition")

    :   Description of the task.

        Type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    *[[property]][ ]*[[elapsed]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.progress.Task.elapsed "Link to this definition")

    :   Time elapsed since task was started, or [`None`] if the task hasn't started.

        Type[:]

        :   Optional\[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")\]

    [[fields]]*[[:]][ ][[Dict]](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.13)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)")[[\]]]*[](#rich.progress.Task.fields "Link to this definition")

    :   Arbitrary fields passed in via Progress.update.

        Type[:]

        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")

    *[[property]][ ]*[[finished]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.progress.Task.finished "Link to this definition")

    :   Check if the task has finished.

    [[finished_speed]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[ ][[=]][ ][None]*[](#rich.progress.Task.finished_speed "Link to this definition")

    :   The last speed for a finished task.

        Type[:]

        :   Optional\[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")\]

    [[finished_time]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[ ][[=]][ ][None]*[](#rich.progress.Task.finished_time "Link to this definition")

    :   Time task was finished.

        Type[:]

        :   [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

    [[get_time]][(][)][[[\[source\]]]](../_modules/rich/progress.html#Task.get_time)[](#rich.progress.Task.get_time "Link to this definition")

    :   float: Get the current time, in seconds.

        Return type[:]

        :   [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

    [[id]]*[[:]][ ][TaskID]*[](#rich.progress.Task.id "Link to this definition")

    :   Task ID associated with this task (used in Progress methods).

    *[[property]][ ]*[[percentage]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*[](#rich.progress.Task.percentage "Link to this definition")

    :   Get progress of task as a percentage. If a None total was set, returns 0

        Type[:]

        :   [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

    *[[property]][ ]*[[remaining]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.progress.Task.remaining "Link to this definition")

    :   Get the number of steps remaining, if a non-None total was set.

        Type[:]

        :   Optional\[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")\]

    *[[property]][ ]*[[speed]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.progress.Task.speed "Link to this definition")

    :   Get the estimated speed in steps per second.

        Type[:]

        :   Optional\[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")\]

    [[start_time]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[ ][[=]][ ][None]*[](#rich.progress.Task.start_time "Link to this definition")

    :   Time this task was started, or None if not started.

        Type[:]

        :   Optional\[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")\]

    *[[property]][ ]*[[started]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.progress.Task.started "Link to this definition")

    :   Check if the task as started.

        Type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    [[stop_time]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[ ][[=]][ ][None]*[](#rich.progress.Task.stop_time "Link to this definition")

    :   Time this task was stopped, or None if not stopped.

        Type[:]

        :   Optional\[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")\]

    *[[property]][ ]*[[time_remaining]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.progress.Task.time_remaining "Link to this definition")

    :   Get estimated time to completion, or [`None`] if no data.

        Type[:]

        :   Optional\[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")\]

    [[total]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.progress.Task.total "Link to this definition")

    :   Total number of steps in this task.

        Type[:]

        :   Optional\[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")\]

    [[visible]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[ ][[=]][ ][True]*[](#rich.progress.Task.visible "Link to this definition")

    :   Indicates if this task is visible in the progress display.

        Type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[TaskProgressColumn]][(]*[[text_format]][[=]][[\'\[progress.percentage\]%\']]*, *[[text_format_no_percentage]][[=]][[\'\']]*, *[[style]][[=]][[\'none\']]*, *[[justify]][[=]][[\'left\']]*, *[[markup]][[=]][[True]]*, *[[highlighter]][[=]][[None]]*, *[[table_column]][[=]][[None]]*, *[[show_speed]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/progress.html#TaskProgressColumn)[](#rich.progress.TaskProgressColumn "Link to this definition")

:   Show task progress as a percentage.

    Parameters[:]

    :   -   **text_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Format for percentage display. Defaults to "\[progress.percentage\]%".

        -   **text_format_no_percentage** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Format if percentage is unknown. Defaults to "".

        -   **style** (*StyleType,* *optional*) -- Style of output. Defaults to "none".

        -   **justify** (*JustifyMethod,* *optional*) -- Text justification. Defaults to "left".

        -   **markup** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable markup. Defaults to True.

        -   **highlighter** (*Optional\[*[*Highlighter*](highlighter.html#rich.highlighter.Highlighter "rich.highlighter.Highlighter")*\],* *optional*) -- Highlighter to apply to output. Defaults to None.

        -   **table_column** (*Optional\[*[*Column*](table.html#rich.table.Column "rich.table.Column")*\],* *optional*) -- Table Column to use. Defaults to None.

        -   **show_speed** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show speed if total is unknown. Defaults to False.

    [[render]][(]*[[task]]*[)][[[\[source\]]]](../_modules/rich/progress.html#TaskProgressColumn.render)[](#rich.progress.TaskProgressColumn.render "Link to this definition")

    :   Should return a renderable object.

        Parameters[:]

        :   **task** ([*Task*](#rich.progress.Task "rich.progress.Task"))

        Return type[:]

        :   [*Text*](text.html#rich.text.Text "rich.text.Text")

    *[[classmethod]][ ]*[[render_speed]][(]*[[speed]]*[)][[[\[source\]]]](../_modules/rich/progress.html#TaskProgressColumn.render_speed)[](#rich.progress.TaskProgressColumn.render_speed "Link to this definition")

    :   Render the speed in iterations per second.

        Parameters[:]

        :   -   **task** ([*Task*](#rich.progress.Task "rich.progress.Task")) -- A Task object.

            -   **speed** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") *\|* *None*)

        Returns[:]

        :   Text object containing the task speed.

        Return type[:]

        :   [Text](text.html#rich.text.Text "rich.text.Text")

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[TextColumn]][(]*[[text_format]]*, *[[style]][[=]][[\'none\']]*, *[[justify]][[=]][[\'left\']]*, *[[markup]][[=]][[True]]*, *[[highlighter]][[=]][[None]]*, *[[table_column]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/progress.html#TextColumn)[](#rich.progress.TextColumn "Link to this definition")

:   A column containing text.

    Parameters[:]

    :   -   **text_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **style** (*StyleType*)

        -   **justify** (*JustifyMethod*)

        -   **markup** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **highlighter** (*Optional\[*[*Highlighter*](highlighter.html#rich.highlighter.Highlighter "rich.highlighter.Highlighter")*\]*)

        -   **table_column** (*Optional\[*[*Column*](table.html#rich.table.Column "rich.table.Column")*\]*)

    [[render]][(]*[[task]]*[)][[[\[source\]]]](../_modules/rich/progress.html#TextColumn.render)[](#rich.progress.TextColumn.render "Link to this definition")

    :   Should return a renderable object.

        Parameters[:]

        :   **task** ([*Task*](#rich.progress.Task "rich.progress.Task"))

        Return type[:]

        :   [*Text*](text.html#rich.text.Text "rich.text.Text")

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[TimeElapsedColumn]][(]*[[table_column]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/progress.html#TimeElapsedColumn)[](#rich.progress.TimeElapsedColumn "Link to this definition")

:   Renders time elapsed.

    Parameters[:]

    :   **table_column** (*Optional\[*[*Column*](table.html#rich.table.Column "rich.table.Column")*\]*)

    [[render]][(]*[[task]]*[)][[[\[source\]]]](../_modules/rich/progress.html#TimeElapsedColumn.render)[](#rich.progress.TimeElapsedColumn.render "Link to this definition")

    :   Show time elapsed.

        Parameters[:]

        :   **task** ([*Task*](#rich.progress.Task "rich.progress.Task"))

        Return type[:]

        :   [*Text*](text.html#rich.text.Text "rich.text.Text")

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[TimeRemainingColumn]][(]*[[compact]][[=]][[False]]*, *[[elapsed_when_finished]][[=]][[False]]*, *[[table_column]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/progress.html#TimeRemainingColumn)[](#rich.progress.TimeRemainingColumn "Link to this definition")

:   Renders estimated time remaining.

    Parameters[:]

    :   -   **compact** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Render MM:SS when time remaining is less than an hour. Defaults to False.

        -   **elapsed_when_finished** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Render time elapsed when the task is finished. Defaults to False.

        -   **table_column** (*Optional\[*[*Column*](table.html#rich.table.Column "rich.table.Column")*\]*)

    [[render]][(]*[[task]]*[)][[[\[source\]]]](../_modules/rich/progress.html#TimeRemainingColumn.render)[](#rich.progress.TimeRemainingColumn.render "Link to this definition")

    :   Show time remaining.

        Parameters[:]

        :   **task** ([*Task*](#rich.progress.Task "rich.progress.Task"))

        Return type[:]

        :   [*Text*](text.html#rich.text.Text "rich.text.Text")

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[TotalFileSizeColumn]][(]*[[table_column]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/progress.html#TotalFileSizeColumn)[](#rich.progress.TotalFileSizeColumn "Link to this definition")

:   Renders total filesize.

    Parameters[:]

    :   **table_column** (*Optional\[*[*Column*](table.html#rich.table.Column "rich.table.Column")*\]*)

    [[render]][(]*[[task]]*[)][[[\[source\]]]](../_modules/rich/progress.html#TotalFileSizeColumn.render)[](#rich.progress.TotalFileSizeColumn.render "Link to this definition")

    :   Show data completed.

        Parameters[:]

        :   **task** ([*Task*](#rich.progress.Task "rich.progress.Task"))

        Return type[:]

        :   [*Text*](text.html#rich.text.Text "rich.text.Text")

```
<!-- -->
```

*[[class]][ ]*[[rich.progress.]][[TransferSpeedColumn]][(]*[[table_column]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/progress.html#TransferSpeedColumn)[](#rich.progress.TransferSpeedColumn "Link to this definition")

:   Renders human readable transfer speed.

    Parameters[:]

    :   **table_column** (*Optional\[*[*Column*](table.html#rich.table.Column "rich.table.Column")*\]*)

    [[render]][(]*[[task]]*[)][[[\[source\]]]](../_modules/rich/progress.html#TransferSpeedColumn.render)[](#rich.progress.TransferSpeedColumn.render "Link to this definition")

    :   Show data transfer speed.

        Parameters[:]

        :   **task** ([*Task*](#rich.progress.Task "rich.progress.Task"))

        Return type[:]

        :   [*Text*](text.html#rich.text.Text "rich.text.Text")

```
<!-- -->
```

[[rich.progress.]][[open]][(]*[[file]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[PathLike]](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.13)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[[\]]][ ][[\|]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.13)")]*, *[[mode]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[[\[]][[\'rt\']][[,]][ ][[\'r\']][[\]]]]*, *[[buffering]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")][ ][[=]][ ][[-1]]*, *[[encoding]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[errors]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[newline]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[total]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[description]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")][ ][[=]][ ][[\'Reading\...\']]*, *[[auto_refresh]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")][ ][[=]][ ][[True]]*, *[[console]][[:]][ ][[[Console]](console.html#rich.console.Console "rich.console.Console")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[transient]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")][ ][[=]][ ][[False]]*, *[[get_time]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.13)")[[\[]][[\[]][[\]]][[,]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[refresh_per_second]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")][ ][[=]][ ][[10]]*, *[[style]][[:]][ ][[StyleType]][ ][[=]][ ][[\'bar.back\']]*, *[[complete_style]][[:]][ ][[StyleType]][ ][[=]][ ][[\'bar.complete\']]*, *[[finished_style]][[:]][ ][[StyleType]][ ][[=]][ ][[\'bar.finished\']]*, *[[pulse_style]][[:]][ ][[StyleType]][ ][[=]][ ][[\'bar.pulse\']]*, *[[disable]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")][ ][[=]][ ][[False]]*[)] [[→] [[[ContextManager]](https://docs.python.org/3/library/typing.html#typing.ContextManager "(in Python v3.13)")[[\[]][[TextIO]](https://docs.python.org/3/library/typing.html#typing.TextIO "(in Python v3.13)")[[\]]]]][[[\[source\]]]](../_modules/rich/progress.html#open)[](#rich.progress.open "Link to this definition")\
[[rich.progress.]][[open]][(]*[[file]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[PathLike]](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.13)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[[\]]][ ][[\|]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.13)")]*, *[[mode]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[[\[]][[\'rb\']][[\]]]]*, *[[buffering]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")][ ][[=]][ ][[-1]]*, *[[encoding]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[errors]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[newline]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[total]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[description]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")][ ][[=]][ ][[\'Reading\...\']]*, *[[auto_refresh]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")][ ][[=]][ ][[True]]*, *[[console]][[:]][ ][[[Console]](console.html#rich.console.Console "rich.console.Console")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[transient]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")][ ][[=]][ ][[False]]*, *[[get_time]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.13)")[[\[]][[\[]][[\]]][[,]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[refresh_per_second]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")][ ][[=]][ ][[10]]*, *[[style]][[:]][ ][[StyleType]][ ][[=]][ ][[\'bar.back\']]*, *[[complete_style]][[:]][ ][[StyleType]][ ][[=]][ ][[\'bar.complete\']]*, *[[finished_style]][[:]][ ][[StyleType]][ ][[=]][ ][[\'bar.finished\']]*, *[[pulse_style]][[:]][ ][[StyleType]][ ][[=]][ ][[\'bar.pulse\']]*, *[[disable]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")][ ][[=]][ ][[False]]*[)] [[→] [[[ContextManager]](https://docs.python.org/3/library/typing.html#typing.ContextManager "(in Python v3.13)")[[\[]][[BinaryIO]](https://docs.python.org/3/library/typing.html#typing.BinaryIO "(in Python v3.13)")[[\]]]]]

:   Read bytes from a file while tracking progress.

    Parameters[:]

    :   -   **path** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *PathLike\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *BinaryIO\]*) -- The path to the file to read, or a file-like object in binary mode.

        -   **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- The mode to use to open the file. Only supports "r", "rb" or "rt".

        -   **buffering** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- The buffering strategy to use, see [[`io.open()`]](https://docs.python.org/3/library/io.html#io.open "(in Python v3.13)").

        -   **encoding** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- The encoding to use when reading in text mode, see [[`io.open()`]](https://docs.python.org/3/library/io.html#io.open "(in Python v3.13)").

        -   **errors** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- The error handling strategy for decoding errors, see [[`io.open()`]](https://docs.python.org/3/library/io.html#io.open "(in Python v3.13)").

        -   **newline** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- The strategy for handling newlines in text mode, see [[`io.open()`]](https://docs.python.org/3/library/io.html#io.open "(in Python v3.13)")

        -   **total** -- (int, optional): Total number of bytes to read. Must be provided if reading from a file handle. Default for a path is os.stat(file).st_size.

        -   **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Description of task show next to progress bar. Defaults to "Reading".

        -   **auto_refresh** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Automatic refresh, disable to force a refresh after each iteration. Default is True.

        -   **transient** -- (bool, optional): Clear the progress on exit. Defaults to False.

        -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")*,* *optional*) -- Console to write to. Default creates internal Console instance.

        -   **refresh_per_second** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")) -- Number of times per second to refresh the progress information. Defaults to 10.

        -   **style** (*StyleType,* *optional*) -- Style for the bar background. Defaults to "bar.back".

        -   **complete_style** (*StyleType,* *optional*) -- Style for the completed bar. Defaults to "bar.complete".

        -   **finished_style** (*StyleType,* *optional*) -- Style for a finished bar. Defaults to "bar.finished".

        -   **pulse_style** (*StyleType,* *optional*) -- Style for pulsing bars. Defaults to "bar.pulse".

        -   **disable** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Disable display of progress.

        -   **encoding** -- The encoding to use when reading in text mode.

    Returns[:]

    :   A context manager yielding a progress reader.

    Return type[:]

    :   ContextManager\[BinaryIO\]

```
<!-- -->
```

[[rich.progress.]][[track]][(]*[[sequence]]*, *[[description]][[=]][[\'Working\...\']]*, *[[total]][[=]][[None]]*, *[[completed]][[=]][[0]]*, *[[auto_refresh]][[=]][[True]]*, *[[console]][[=]][[None]]*, *[[transient]][[=]][[False]]*, *[[get_time]][[=]][[None]]*, *[[refresh_per_second]][[=]][[10]]*, *[[style]][[=]][[\'bar.back\']]*, *[[complete_style]][[=]][[\'bar.complete\']]*, *[[finished_style]][[=]][[\'bar.finished\']]*, *[[pulse_style]][[=]][[\'bar.pulse\']]*, *[[update_period]][[=]][[0.1]]*, *[[disable]][[=]][[False]]*, *[[show_speed]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/progress.html#track)[](#rich.progress.track "Link to this definition")

:   Track progress by iterating over a sequence.

    You can also track progress of an iterable, which might require that you additionally specify [`total`].

    Parameters[:]

    :   -   **sequence** (*Iterable\[ProgressType\]*) -- Values you wish to iterate over and track progress.

        -   **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Description of task show next to progress bar. Defaults to "Working".

        -   **total** (*Optional\[*[*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*\]*) -- (float, optional): Total number of steps. Default is len(sequence).

        -   **completed** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Number of steps completed so far. Defaults to 0.

        -   **auto_refresh** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Automatic refresh, disable to force a refresh after each iteration. Default is True.

        -   **transient** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")) -- (bool, optional): Clear the progress on exit. Defaults to False.

        -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")*,* *optional*) -- Console to write to. Default creates internal Console instance.

        -   **refresh_per_second** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")) -- Number of times per second to refresh the progress information. Defaults to 10.

        -   **style** (*StyleType,* *optional*) -- Style for the bar background. Defaults to "bar.back".

        -   **complete_style** (*StyleType,* *optional*) -- Style for the completed bar. Defaults to "bar.complete".

        -   **finished_style** (*StyleType,* *optional*) -- Style for a finished bar. Defaults to "bar.finished".

        -   **pulse_style** (*StyleType,* *optional*) -- Style for pulsing bars. Defaults to "bar.pulse".

        -   **update_period** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Minimum time (in seconds) between calls to update(). Defaults to 0.1.

        -   **disable** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Disable display of progress.

        -   **show_speed** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show speed if total isn't known. Defaults to True.

        -   **get_time** (*Optional\[Callable\[\[\],* [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*\]\]*)

    Returns[:]

    :   An iterable of the values in the sequence.

    Return type[:]

    :   Iterable\[ProgressType\]

```
<!-- -->
```

[[rich.progress.]][[wrap_file]][(]*[[file]]*, *[[total]]*, *[[\*]]*, *[[description]][[=]][[\'Reading\...\']]*, *[[auto_refresh]][[=]][[True]]*, *[[console]][[=]][[None]]*, *[[transient]][[=]][[False]]*, *[[get_time]][[=]][[None]]*, *[[refresh_per_second]][[=]][[10]]*, *[[style]][[=]][[\'bar.back\']]*, *[[complete_style]][[=]][[\'bar.complete\']]*, *[[finished_style]][[=]][[\'bar.finished\']]*, *[[pulse_style]][[=]][[\'bar.pulse\']]*, *[[disable]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/progress.html#wrap_file)[](#rich.progress.wrap_file "Link to this definition")

:   Read bytes from a file while tracking progress.

    Parameters[:]

    :   -   **file** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *PathLike\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *BinaryIO\]*) -- The path to the file to read, or a file-like object in binary mode.

        -   **total** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Total number of bytes to read.

        -   **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Description of task show next to progress bar. Defaults to "Reading".

        -   **auto_refresh** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Automatic refresh, disable to force a refresh after each iteration. Default is True.

        -   **transient** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")) -- (bool, optional): Clear the progress on exit. Defaults to False.

        -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")*,* *optional*) -- Console to write to. Default creates internal Console instance.

        -   **refresh_per_second** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")) -- Number of times per second to refresh the progress information. Defaults to 10.

        -   **style** (*StyleType,* *optional*) -- Style for the bar background. Defaults to "bar.back".

        -   **complete_style** (*StyleType,* *optional*) -- Style for the completed bar. Defaults to "bar.complete".

        -   **finished_style** (*StyleType,* *optional*) -- Style for a finished bar. Defaults to "bar.finished".

        -   **pulse_style** (*StyleType,* *optional*) -- Style for pulsing bars. Defaults to "bar.pulse".

        -   **disable** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Disable display of progress.

        -   **get_time** (*Optional\[Callable\[\[\],* [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*\]\]*)

    Returns[:]

    :   A context manager yielding a progress reader.

    Return type[:]

    :   ContextManager\[BinaryIO\]

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).