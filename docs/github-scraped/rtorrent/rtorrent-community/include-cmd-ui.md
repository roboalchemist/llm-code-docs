# User Interface Commands

## `ui.*` commands

Commands in this group control aspects of the `curses` UI.

> ui.current_view
> ui.current_view.set

```ini

            ui.column.hide = ‹column index›[, …] ≫ 0
            ui.column.show = ‹column index›[, …] ≫ 0
            ui.column.is_hidden = ‹column index› ≫ bool (0 or 1)
            ui.column.hidden.list = ≫ array of value (column index list)

        Hide or show columns by their index.
        The hide/show commands take any number of arguments, or a list of values.

        The ``ui.column.is_hidden`` command allows to query the visibility of a column,
        and the last command returns a list of index values for all hidden columns.

        The hiddden state is *not* persisted over client restarts.
        Also note that some columns are auto-hidden in case the terminal gets too narrow
        to show all of them.

    ui.column.sacrificed
    ui.column.sacrificed.set
    ui.column.sacrificed.toggle
    ui.column.sacrificial.list

        The ``ui.column.sacrificed`` value is *false* (0) by default,
        and can set set as usual.
        The ``ui.column.sacrificed.toggle`` command changes the state of this value
        and :term:`ui.column.hide`\ s or :term:`ui.column.show`\ s all the columns
        that ``ui.column.sacrificial.list`` returns (as a list of values).

    ui.focus.end
    ui.focus.home
    ui.focus.pgdn
    ui.focus.pgup
    ui.focus.page_size
    ui.focus.page_size.set

        These commands support quick paging through the download list,
        and jumping to the start or end of it.
        See `bind-navigation-keys.rc`_ on how to use them in a `rTorrent-PS` configuration.

        With the ``ui.focus.page_size.set`` command, the amount of items to skip
        can be changed from the default value of 50, e.g. in the ``_rtlocal.rc`` file.

    ui.find.term
    ui.find.term.set

        This string variable holds the current search term,
        and is normally set by entering a value into the :kbd:`Ctrl-F` prompt.

        When you hit :kbd:`Enter` in the ``find>`` prompt, the entered text
        is saved here and then :term:`ui.find.next` is called.

    ui.find.next

        This command is bound to :kbd:`Shift-F` and :kbd:`F3` and jumps to the next hit
        for a non-empty :term:`ui.find.term`. The search is ignoring case (for :abbr:`ASCII` names).

        A console message is shown if nothing is found in the current view, or if the view is empty.

    ui.style.progress
    ui.style.progress.set
    ui.style.ratio
    ui.style.ratio.set

## `view.*` commands

> view.add
> view.list
> view.size
> view.persistent

### TODO (view add/list/size/persistent)

> view.event_added
> view.event_removed

### TODO (view events)

> view.filter
> view.filter_all
> view.filter_download
> view.filter_on

### TODO (view filter)

> view.set
> view.set_visible
> view.set_not_visible
> view.size_not_visible

### TODO (view set)

> view.sort
> view.sort_current
> view.sort_new

### TODO (view sort)

> view.collapsed.toggle

```ini

            schedule = bind_collapse,0,0,"ui.bind_key=download_list,*,view.collapsed.toggle="

```
