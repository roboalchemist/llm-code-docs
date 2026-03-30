# Source: https://rich.readthedocs.io/en/latest/progress.html

[]

# Progress Display[](#progress-display "Link to this heading")

Rich can display continuously updated information regarding the progress of long running tasks / file copies etc. The information displayed is configurable, the default will display a description of the 'task', a progress bar, percentage complete, and estimated time remaining.

Rich progress display supports multiple tasks, each with a bar and progress information. You can use this to track concurrent tasks where the work is happening in threads or processes.

To see how the progress display looks, try this from the command line:

    python -m rich.progress

Note

Progress works with Jupyter notebooks, with the caveat that auto-refresh is disabled. You will need to explicitly call [[`refresh()`]](reference/progress.html#rich.progress.Progress.refresh "rich.progress.Progress.refresh") or set [`refresh=True`] when calling [[`update()`]](reference/progress.html#rich.progress.Progress.update "rich.progress.Progress.update"). Or use the [[`track()`]](reference/progress.html#rich.progress.track "rich.progress.track") function which does a refresh automatically on each loop.

## Basic Usage[](#basic-usage "Link to this heading")

For basic usage call the [[`track()`]](reference/progress.html#rich.progress.track "rich.progress.track") function, which accepts a sequence (such as a list or range object) and an optional description of the job you are working on. The track function will yield values from the sequence and update the progress information on each iteration. Here's an example:

    import time
    from rich.progress import track

    for i in track(range(20), description="Processing..."):
        time.sleep(1)  # Simulate work being done