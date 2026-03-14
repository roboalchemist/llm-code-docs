# Reference

## Application

*class*prompt_toolkit.application.AppSession(*input: Input | None = None*, *output: Output | None = None*)

An AppSession is an interactive session, usually connected to one terminal.
Within one such session, interaction with many applications can happen, one
after the other.

The input/output device is not supposed to change during one session.

Warning: Always use the create_app_session function to create an
instance, so that it gets activated correctly.

Parameters:

-

**input** – Use this as a default input for all applications
running in this session, unless an input is passed to the Application
explicitly.

-

**output** – Use this as a default output.

*class*prompt_toolkit.application.Application(*layout: Layout | None = None*, *style: BaseStyle | None = None*, *include_default_pygments_style: FilterOrBool = True*, *style_transformation: StyleTransformation | None = None*, *key_bindings: KeyBindingsBase | None = None*, *clipboard: Clipboard | None = None*, *full_screen: bool = False*, *color_depth: ColorDepth | Callable[[], ColorDepth | None] | None = None*, *mouse_support: FilterOrBool = False*, *enable_page_navigation_bindings: None | FilterOrBool = None*, *paste_mode: FilterOrBool = False*, *editing_mode: EditingMode = EditingMode.EMACS*, *erase_when_done: bool = False*, *reverse_vi_search_direction: FilterOrBool = False*, *min_redraw_interval: float | int | None = None*, *max_render_postpone_time: float | int | None = 0.01*, *refresh_interval: float | None = None*, *terminal_size_polling_interval: float | None = 0.5*, *cursor: AnyCursorShapeConfig = None*, *on_reset: ApplicationEventHandler[_AppResult] | None = None*, *on_invalidate: ApplicationEventHandler[_AppResult] | None = None*, *before_render: ApplicationEventHandler[_AppResult] | None = None*, *after_render: ApplicationEventHandler[_AppResult] | None = None*, *input: Input | None = None*, *output: Output | None = None*)

The main Application class!
This glues everything together.

Parameters:

-

**layout** – A `Layout` instance.

-

**key_bindings** – `KeyBindingsBase` instance for
the key bindings.

-

**clipboard** – `Clipboard` to use.

-

**full_screen** – When True, run the application on the alternate screen buffer.

-

**color_depth** – Any `ColorDepth` value, a callable that
returns a `ColorDepth` or None for default.

-

**erase_when_done** – (bool) Clear the application output when it finishes.

-

**reverse_vi_search_direction** – Normally, in Vi mode, a ‘/’ searches
forward and a ‘?’ searches backward. In Readline mode, this is usually
reversed.

-

**min_redraw_interval** –

Number of seconds to wait between redraws. Use
this for applications where invalidate is called a lot. This could cause
a lot of terminal output, which some terminals are not able to process.

None means that every invalidate will be scheduled right away
(which is usually fine).

When one invalidate is called, but a scheduled redraw of a previous
invalidate call has not been executed yet, nothing will happen in any
case.

-

**max_render_postpone_time** – When there is high CPU (a lot of other
scheduled calls), postpone the rendering max x seconds.  ‘0’ means:
don’t postpone. ‘.5’ means: try to draw at least twice a second.

-

**refresh_interval** – Automatically invalidate the UI every so many
seconds. When None (the default), only invalidate when invalidate
has been called.

-

**terminal_size_polling_interval** – Poll the terminal size every so many
seconds. Useful if the applications runs in a thread other then then
main thread where SIGWINCH can’t be handled, or on Windows.

Filters:

Parameters:

-

**mouse_support** – (`Filter` or
boolean). When True, enable mouse support.

-

**paste_mode** – `Filter` or boolean.

-

**editing_mode** – `EditingMode`.

-

**enable_page_navigation_bindings** – When True, enable the page
navigation key bindings. These include both Emacs and Vi bindings like
page-up, page-down and so on to scroll through pages. Mostly useful for
creating an editor or other full screen applications. Probably, you
don’t want this for the implementation of a REPL. By default, this is
enabled if full_screen is set.

Callbacks (all of these should accept an
`Application` object as input.)

Parameters:

-

**on_reset** – Called during reset.

-

**on_invalidate** – Called when the UI has been invalidated.

-

**before_render** – Called right before rendering.

-

**after_render** – Called right after rendering.

I/O:
(Note that the preferred way to change the input/output is by creating an
AppSession with the required input/output objects. If you need multiple
applications running at the same time, you have to create a separate
AppSession using a with create_app_session(): block.

Parameters:

-

**input** – `Input` instance.

-

**output** – `Output` instance. (Probably
Vt100_Output or Win32Output.)

Usage:

app = Application(…)
app.run()

# Or

await app.run_async()
