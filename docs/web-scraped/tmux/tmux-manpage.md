# tmux(1) - Terminal Multiplexer

**Source**: https://man.openbsd.org/OpenBSD-current/man1/tmux.1

**OpenBSD Manual Page - Current Version**

---
## NAME

`tmux` --- [terminal multiplexer]

## SYNOPSIS

## DESCRIPTION

`tmux` is a terminal multiplexer: it enables a number of terminals to be created, accessed, and controlled from a single screen. `tmux` may be detached from a screen and continue running in the background, then later reattached.

Each session is persistent and will survive accidental disconnection (such as [ssh(1)](/ssh.1) connection timeout) or intentional detaching (with the '`C-b d`' key strokes). `tmux` may be reattached using:

`$ tmux attach`

The options are as follows:

[`-2`](#2)
: Force `tmux` to assume the terminal supports 256 colours. This is equivalent to `-T` `256`.

[`-C`](#C)
: Start in control mode (see the [CONTROL MODE](#CONTROL_MODE) section). Given twice (`-CC`) disables echo.

[`-D`](#D)

[`-f`](#f) `file`

: Specify an alternative configuration file. By default, `tmux` loads the system configuration file from [/etc/tmux.conf], if present, then looks for a user configuration file at [\~/.tmux.conf].

[`-h`](#h)
: Print usage information and exit.

[`-L`](#L) `socket-name`

: `tmux` stores the server socket in a directory under `TMUX_TMPDIR` or [/tmp] if it is unset. The default socket is named [*default*](#default). This option allows a different socket name to be specified, allowing several independent `tmux` servers to be run. Unlike `-S` a full path is not necessary: the sockets are all created in a directory [tmux-UID] under the directory given by `TMUX_TMPDIR` or in [/tmp]. The [tmux-UID] directory is created by `tmux` and must not be world readable, writable or executable.

 If the socket is accidentally removed, the `SIGUSR1` signal may be sent to the `tmux` server process to recreate it (note that this will fail if any parent directories are missing).

[`-l`](#l)
: Behave as a login shell. This flag currently has no effect and is for compatibility with other shells when using tmux as a login shell.

[`-N`](#N)

[`-S`](#S) `socket-path`
: Specify a full alternative path to the server socket. If `-S` is specified, the default socket directory is not used and any `-L` flag is ignored.

[`-T`](#T) `features`
: Set terminal features for the client. This is a comma-separated list of features. See the `terminal-features` option.

[`-u`](#u)
: Write UTF-8 output to the terminal even if the first environment variable of `LC_ALL`, `LC_CTYPE`, or `LANG` that is set does not contain \"UTF-8\" or \"UTF8\".

[`-V`](#V)
: Report the `tmux` version.

[`-v`](#v)

: Request verbose logging. Log messages will be saved into [tmux-client-PID.log] and [tmux-server-PID.log] files in the current directory, where [*PID*](#PID) is the PID of the server or client process. If `-v` is specified twice, an additional [tmux-out-PID.log] file is generated with a copy of everything `tmux` writes to the terminal.

 The `SIGUSR2` signal may be sent to the `tmux` server process to toggle logging between on (as if `-v` was given) and off.

## DEFAULT KEY BINDINGS

C-b
: Send the prefix key (C-b) through to the application.

C-o
: Rotate the panes in the current window forwards.

C-z
: Suspend the `tmux` client.

!
: Break the current pane out of the window.

\"
: Split the current pane into two, top and bottom.

\#
: List all paste buffers.

\$
: Rename the current session.

\%
: Split the current pane into two, left and right.

&
: Kill the current window.

'
: Prompt for a window index to select.

(
: Switch the attached client to the previous session.

)
: Switch the attached client to the next session.

,
: Rename the current window.

\-
: Delete the most recently copied buffer of text.

.
: Prompt for an index to move the current window.

0 to 9
: Select windows 0 to 9.

:

;
: Move to the previously active pane.

=
: Choose which buffer to paste interactively from a list.

?
: List all key bindings.

D
: Choose a client to detach.

L
: Switch the attached client back to the last session.

[
: Enter copy mode to copy text or view the history.

]
: Paste the most recently copied buffer of text.

c
: Create a new window.

d
: Detach the current client.

f
: Prompt to search for text in open windows.

i
: Display some information about the current window.

l
: Move to the previously selected window.

m
: Mark the current pane (see `select-pane` `-m`).

M
: Clear the marked pane.

n
: Change to the next window.

o
: Select the next pane in the current window.

p
: Change to the previous window.

q
: Briefly display pane indexes.

r
: Force redraw of the attached client.

s
: Select a new session for the attached client interactively.

t
: Show the time.

w
: Choose the current window interactively.

x
: Kill the current pane.

z
: Toggle zoom state of the current pane.

: Swap the current pane with the next pane.

\~
: Show previous messages from `tmux`, if any.

Page Up
: Enter copy mode and scroll one page up.

Up, Down
:  

Left, Right
: Change to the pane above, below, to the left, or to the right of the current pane.

M-1 to M-7
: Arrange panes in one of the seven preset layouts: even-horizontal, even-vertical, main-horizontal, main-horizontal-mirrored, main-vertical, main-vertical-mirrored, or tiled.

Space
: Arrange the current window in the next preset layout.

M-n
: Move to the next window with a bell or activity marker.

M-o
: Rotate the panes in the current window backwards.

M-p
: Move to the previous window with a bell or activity marker.

C-Up, C-Down
:  

C-Left, C-Right
: Resize the current pane in steps of one cell.

M-Up, M-Down
:  

M-Left, M-Right
: Resize the current pane in steps of five cells.

## COMMAND PARSING AND EXECUTION

 $ tmux set-option -g status-style bg=cyan

 set-option -g status-style bg=cyan

 bind-key C set-option -g status-style bg=cyan

- in a configuration file;
- given to `bind-key`;
- passed as arguments to `if-shell` or `confirm-before`.

 new-session; new-window
 if-shell "true" "split-window"
 kill-session

## PARSING SYNTAX

 $ tmux neww \; splitw

Or:

 $ tmux neww ';' splitw

 neww ; splitw

 $ tmux neww\; splitw

Or:

 $ tmux 'neww;' splitw

As in these examples, when running tmux from the shell extra care must be taken to properly quote semicolons:

2. Individual semicolons or trailing semicolons that should be interpreted as arguments should be escaped twice: once according to the shell conventions and a second time for `tmux`; for example:

 ::: 
 $ tmux neww 'foo\;' bar
 $ tmux neww foo\\\; bar
 :::
3. Semicolons that are not individual tokens or trailing another token should only be escaped once according to shell conventions; for example:

 ::: 
 $ tmux neww 'foo-;-bar'
 $ tmux neww foo-\;-bar
 :::

Comments are marked by the unquoted \# character - any remaining text after a comment is ignored until the end of the line.

If the last character of a line is \\, the line is joined with the following line (the \\ and the newline are completely removed). This is called line continuation and applies both inside and outside quoted strings and in comments, but not inside braces.

Outside of quotes and inside double quotes, these replacements are performed:

- Environment variables preceded by \$ are replaced with their value from the global environment (see the [GLOBAL AND SESSION ENVIRONMENT](#GLOBAL_AND_SESSION_ENVIRONMENT) section).
- A leading \~ or \~user is expanded to the home directory of the current or specified user.
- \\uXXXX or \\uXXXXXXXX is replaced by the Unicode codepoint corresponding to the given four or eight digit hexadecimal number.
- When preceded (escaped) by a \\, the following characters are replaced: \\e by the escape character; \\r by a carriage return; \\n by a newline; and \\t by a tab.
- \\ooo is replaced by a character of the octal value ooo. Three octal digits are required, for example \\001. The largest valid character is \\377.

 if-shell true $foo'
 }

 if-shell true "display -p 'brace-dollar-foo: }\$foo'"

Braces may be enclosed inside braces, for example:

 bind x if-shell "true" 
 }

Environment variables may be set by using the syntax '`name=value`', for example '`HOME=/home/user`'. Variables set during parsing are added to the global environment. A hidden variable may be set with '`%hidden`', for example:

 %hidden MYVAR=42

Hidden variables are not passed to the environment of processes created by tmux. See the [GLOBAL AND SESSION ENVIRONMENT](#GLOBAL_AND_SESSION_ENVIRONMENT) section.

 %if "#,myhost}"
 set -g status-style bg=red
 %elif "#,myotherhost}"
 set -g status-style bg=green
 %else
 set -g status-style bg=blue
 %endif

Will change the status line to red if running on '`myhost`', green if running on '`myotherhost`', or blue if running on another host. Conditionals may be given on one line, for example:

 %if #,myhost} set -g status-style bg=red %endif

## COMMANDS

`target-session` is tried as, in order:

1. A session ID prefixed with a \$.
3. The start of a session name, for example '`mysess`' would match a session named '`mysession`'.
4. A [glob(7)](/glob.7) pattern which is matched against the session name.

If the session name is prefixed with an '`=`', only an exact match is accepted (so '`=mysess`' will only match exactly '`mysess`', not '`mysession`').

If a single session is found, it is used as the target session; multiple matches produce an error. If a session is omitted, the current session is used if available; if no current session is available, the most recently used is chosen.

`target-window` (or `src-window` or `dst-window`) specifies a window in the form *session*:*window*. *session* follows the same rules as for `target-session`, and *window* is looked for in order as:

1. A special token, listed below.
2. A window index, for example '`mysession:1`' is window 1 in session '`mysession`'.
3. A window ID, such as \@1.
4. An exact window name, such as '`mysession:mywindow`'.
5. The start of a window name, such as '`mysession:mywin`'.
6. As a [glob(7)](/glob.7) pattern matched against the window name.

The following special tokens are available to indicate particular windows. Each has a single-character alternative form.

 [**Token**](#Token) [**Meaning**](#Meaning)
 [``](#_start_) \^ The lowest-numbered window
 [``](#_end_) \$ The highest-numbered window
 [``](#_last_) ! The last (previously current) window
 [``](#_next_) \+ The next window by number
 [``](#_previous_) \- The previous window by number
 [``](#_current_) @ The current window

`target-pane` (or `src-pane` or `dst-pane`) may be a pane ID or takes a similar form to `target-window` but with the optional addition of a period followed by a pane index or pane ID, for example: '`mysession:mywindow.1`'. If the pane index is omitted, the currently active pane in the specified window is used. The following special tokens are available for the pane index:

 [**Token**](#Token~2) [**Meaning**](#Meaning~2)
 [``](#_last_~2) ! The last (previously active) pane
 [``](#_next_~2) \+ The next pane by number
 [``](#_previous_~2) \- The previous pane by number
 [``](#_top_) The top pane
 [``](#_bottom_) The bottom pane
 [``](#_left_) The leftmost pane
 [``](#_right_) The rightmost pane
 [``](#_top-left_) The top-left pane
 [``](#_top-right_) The top-right pane
 [``](#_bottom-left_) The bottom-left pane
 [``](#_bottom-right_) The bottom-right pane
 [``](#_up-of_) The pane above the active pane
 [``](#_down-of_) The pane below the active pane
 [``](#_left-of_) The pane to the left of the active pane
 [``](#_right-of_) The pane to the right of the active pane
 [``](#_active_) @ The active pane

The tokens '`+`' and '`-`' may be followed by an offset, for example:

 select-window -t:+2

In addition, [*target-session*](#target-session), [*target-window*](#target-window) or [*target-pane*](#target-pane) may consist entirely of the token '``' (alternative form '`=`') to specify the session, window or pane where the most recent mouse event occurred (see the [MOUSE SUPPORT](#MOUSE_SUPPORT) section) or '``' (alternative form '`~`') to specify the marked pane (see `select-pane` `-m`).

 new-window 'vi ~/.tmux.conf'

Will run:

 /bin/sh -c 'vi ~/.tmux.conf'

 $ tmux new-window vi ~/.tmux.conf

Will run [vi(1)](/vi.1) directly without invoking the shell.

 bind-key F1 set-option status off

Or passed as a single string argument in [.tmux.conf], for example:

 bind-key F1 

 refresh-client -t/dev/ttyp2

 rename-session -tfirst newname

 set-option -wt:0 monitor-activity on

 new-window ; split-window -d

 bind-key R source-file ~/.tmux.conf \; \
 display-message "source-file done"

Or from [sh(1)](/sh.1):

 $ tmux kill-window -t :1

 $ tmux new-window \; split-window -d

 $ tmux new-session -d 'vi ~/.tmux.conf' \; split-window -d \; attach

## CLIENTS AND SESSIONS

[`attach-session`](#attach-session) [`-dErx`] [`-c` `working-directory`] [`-f` `flags`] [`-t` `target-session`]

: ::: 
 (alias: `attach`)
 :::

 active-pane
 : the client has an independent active pane

 ignore-size
 : the client does not affect the size of other clients

 no-detach-on-destroy
 : do not detach the client when the session it is attached to is destroyed if there are any other sessions

 no-output
 : the client does not receive pane output in control mode

 pause-after=seconds
 : output is paused once the pane is `seconds` behind in control mode

 read-only
 : the client is read-only

 wait-exit
 : wait for an empty line input before exiting in control mode

 If no server is started, `attach-session` will attempt to start it; this will fail unless sessions are created in the configuration file.

 The `target-session` rules for `attach-session` are slightly adjusted: if `tmux` needs to select the most recently used session, it will prefer the most recently used [*unattached*](#unattached) session.

 `-c` will set the session working directory (used for new windows) to `working-directory`.

 If `-E` is used, the `update-environment` option will not be applied.

: ::: 
 (alias: `detach`)
 :::

[`has-session`](#has-session) [`-t` `target-session`]

: ::: 
 (alias: `has`)
 :::

 Report an error and exit with 1 if the specified session does not exist. If it does exist, exit with 0.

[`kill-server`](#kill-server)
: Kill the `tmux` server and clients and destroy all sessions.

[`kill-session`](#kill-session) [`-aC`] [`-t` `target-session`]
: Destroy the given session, closing any windows linked to it and no other sessions, and detaching all clients attached to it. If `-a` is given, all sessions but the specified one is killed. The `-C` flag clears alerts (bell, activity, or silence) in all windows linked to the session.

[`list-clients`](#list-clients) [`-F` `format`] [`-f` `filter`] [`-t` `target-session`]

: ::: 
 (alias: `lsc`)
 :::

 List all clients attached to the server. `-F` specifies the format of each line and `-f` a filter. Only clients for which the filter is true are shown. See the [FORMATS](#FORMATS) section. If `target-session` is specified, list only clients connected to that session.

: ::: 
 (alias: `lscm`)
 :::

[`list-sessions`](#list-sessions) [`-F` `format`] [`-f` `filter`]

: ::: 
 (alias: `ls`)
 :::

[`lock-client`](#lock-client) [`-t` `target-client`]

: ::: 
 (alias: `lockc`)
 :::

[`lock-session`](#lock-session) [`-t` `target-session`]

: ::: 
 (alias: `locks`)
 :::

 Lock all clients attached to `target-session`.

: ::: 
 (alias: `new`)
 :::

 Create a new session with name `session-name`.

 If run from a terminal, any [termios(4)](/termios.4) special characters are saved and used for new windows in the new session.

 The `-A` flag makes `new-session` behave like `attach-session` if `session-name` already exists; if `-A` is given, `-D` behaves like `-d` to `attach-session`, and `-X` behaves like `-x` to `attach-session`.

 If `-t` is given, it specifies a `session group`. Sessions in the same group share the same set of windows - new windows are linked to all sessions in the group and any windows closed removed from all sessions. The current and previous window and any session options remain independent and any session in a group may be killed without affecting the others. The `group-name` argument may be:

 1. the name of an existing group, in which case the new session is added to that group;
 2. the name of an existing session - the new session is added to the same group as that session, creating a new group if necessary;
 3. the name for a new group containing only the new session.

 The `-P` option prints information about the new session after it has been created. By default, it uses the format '`#:`' but a different format may be specified with `-F`.

 If `-E` is used, the `update-environment` option will not be applied. `-e` takes the form '`VARIABLE=value`' and sets an environment variable for the newly created session; it may be specified multiple times.

[`refresh-client`](#refresh-client) [`-cDlLRSU`] [`-A` `pane:state`] [`-B` `name:what:format`] [`-C` `size`] [`-f` `flags`] [`-r` `pane:report`] [`-t` `target-client`] [`adjustment`]

: ::: 
 (alias: `refresh`)
 :::

 Refresh the current client if bound to a key, or a single client if one is given with `-t`. If `-S` is specified, only update the client's status line.

 The `-U`, `-D`, `-L` `-R`, and `-c` flags allow the visible portion of a window which is larger than the client to be changed. `-U` moves the visible part up by `adjustment` rows and `-D` down, `-L` left by `adjustment` columns and `-R` right. `-c` returns to tracking the cursor automatically. If `adjustment` is omitted, 1 is used. Note that the visible position is a property of the client not of the window, changing the current window in the attached session will reset it.

 `-B` sets a subscription to a format for a control mode client. The argument is split into three items by colons: `name` is a name for the subscription; `what` is a type of item to subscribe to; `format` is the format. After a subscription is added, changes to the format are reported with the `%subscription-changed` notification, at most once a second. If only the name is given, the subscription is removed. `what` may be empty to check the format only for the attached session, or one of: a pane ID such as '`%0`'; '`%*`' for all panes in the attached session; a window ID such as '`@0`'; or '`@*`' for all windows in the attached session.

 `-f` sets a comma-separated list of client flags, see `attach-session`. `-r` allows a control mode client to provide information about a pane via a report (such as the response to OSC 10). The argument is a pane ID (with a leading '`%`'), a colon, then a report escape sequence.

 `-l` requests the clipboard from the client using the [xterm(1)](/xterm.1) escape sequence and stores it in a new paste buffer.

 `-L`, `-R`, `-U` and `-D` move the visible portion of the window left, right, up or down by `adjustment`, if the window is larger than the client. `-c` resets so that the position follows the cursor. See the `window-size` option.

[`rename-session`](#rename-session) [`-t` `target-session`] `new-name`

: ::: 
 (alias: `rename`)
 :::

 Rename the session to `new-name`.

[`server-access`](#server-access) [`-adlrw`] [`user`]

: Change the access or read/write permission of `user`. The user running the `tmux` server (its owner) and the root user cannot be changed and are always permitted access.

 `-a` and `-d` are used to give or revoke access for the specified user. If the user is already attached, the `-d` flag causes their clients to be detached.

 `-r` and `-w` change the permissions for `user`: `-r` makes their clients read-only and `-w` writable. `-l` lists current access permissions.

[`show-messages`](#show-messages) [`-JT`] [`-t` `target-client`]

: ::: 
 (alias: `showmsgs`)
 :::

 Show server messages or information. Messages are stored, up to a maximum of the limit set by the `message-limit` server option. `-J` and `-T` show debugging information about jobs and terminals.

[`source-file`](#source-file) [`-Fnqv`] [`-t` `target-pane`] `path ...`

: ::: 
 (alias: `source`)
 :::

[`start-server`](#start-server)

: ::: 
 (alias: `start`)
 :::

 Start the `tmux` server, if not already running, without creating any sessions.

 ::: 
 $ tmux start \; show -g
 :::

[`suspend-client`](#suspend-client) [`-t` `target-client`]

: ::: 
 (alias: `suspendc`)
 :::

 Suspend a client by sending `SIGTSTP` (tty stop).

[`switch-client`](#switch-client) [`-ElnprZ`] [`-c` `target-client`] [`-t` `target-session`] [`-T` `key-table`]

: ::: 
 (alias: `switchc`)
 :::

 If `-E` is used, `update-environment` option will not be applied.

 ::: 
 bind-key -Ttable2 c list-keys
 bind-key -Ttable1 b switch-client -Ttable2
 bind-key -Troot a switch-client -Ttable1
 :::

## WINDOWS AND PANES

By default, a `tmux` pane permits direct access to the terminal contained in the pane. A pane may also be put into one of several modes:

In copy mode an indicator is displayed in the top-right corner of the pane with the current position and the number of lines in the history.

[`append-selection`](#append-selection)
: Append the selection to the top paste buffer.

[`append-selection-and-cancel`](#append-selection-and-cancel) (vi: A)
: Append the selection to the top paste buffer and exit copy mode.

[`back-to-indentation`](#back-to-indentation) (vi: \^) (emacs: M-m)
: Move the cursor back to the indentation.

[`begin-selection`](#begin-selection) (vi: Space) (emacs: C-Space)
: Begin selection.

[`bottom-line`](#bottom-line) (vi: L)
: Move to the bottom line.

[`cancel`](#cancel) (vi: q) (emacs: Escape)
: Exit copy mode.

[`clear-selection`](#clear-selection) (vi: Escape) (emacs: C-g)
: Clear the current selection.

[`copy-end-of-line`](#copy-end-of-line) [`-CP`] [`prefix`]
: Copy from the cursor position to the end of the line. `prefix` is used to name the new paste buffer.

[`copy-end-of-line-and-cancel`](#copy-end-of-line-and-cancel) [`-CP`] [`prefix`]
: Copy from the cursor position and exit copy mode.

: Same as `copy-pipe-end-of-line` but also exit copy mode.

[`copy-line`](#copy-line) [`-CP`] [`prefix`]
: Copy the entire line.

[`copy-line-and-cancel`](#copy-line-and-cancel) [`-CP`] [`prefix`]
: Copy the entire line and exit copy mode.

: Same as `copy-pipe-line` but also exit copy mode.

: Same as `copy-pipe` but do not clear the selection.

: Same as `copy-pipe` but also exit copy mode.

[`copy-selection`](#copy-selection) [`-CP`] [`prefix`]
: Copies the current selection.

[`copy-selection-no-clear`](#copy-selection-no-clear) [`-CP`] [`prefix`]
: Same as `copy-selection` but do not clear the selection.

[`copy-selection-and-cancel`](#copy-selection-and-cancel) [`-CP`] [`prefix`] (vi: Enter) (emacs: M-w)
: Copy the current selection and exit copy mode.

[`cursor-down`](#cursor-down) (vi: j) (emacs: Down)
: Move the cursor down.

[`cursor-down-and-cancel`](#cursor-down-and-cancel)
: Same as `cursor-down` but also exit copy mode if reaching the bottom.

[`cursor-left`](#cursor-left) (vi: h) (emacs: Left)
: Move the cursor left.

[`cursor-right`](#cursor-right) (vi: l) (emacs: Right)
: Move the cursor right.

[`cursor-up`](#cursor-up) (vi: k) (emacs: Up)
: Move the cursor up.

[`cursor-centre-vertical`](#cursor-centre-vertical) (emacs: C-l)
: Moves the cursor to the vertical centre of the pane.

[`cursor-centre-horizontal`](#cursor-centre-horizontal) (emacs: M-l)
: Moves the cursor to the horizontal centre of the pane.

[`end-of-line`](#end-of-line) (vi: \$) (emacs: C-e)
: Move the cursor to the end of the line.

[`goto-line`](#goto-line) `line` (vi: :) (emacs: g)
: Move the cursor to a specific line.

[`halfpage-down`](#halfpage-down) (vi: C-d) (emacs: M-Down)
: Scroll down by half a page.

[`halfpage-down-and-cancel`](#halfpage-down-and-cancel)
: Same as `halfpage-down` but also exit copy mode if reaching the bottom.

[`halfpage-up`](#halfpage-up) (vi: C-u) (emacs: M-Up)
: Scroll up by half a page.

[`history-bottom`](#history-bottom) (vi: G) (emacs: M-\>)
: Scroll to the bottom of the history.

[`history-top`](#history-top) (vi: g) (emacs: M-\<)
: Scroll to the top of the history.

[`jump-again`](#jump-again) (vi: ;) (emacs: ;)
: Repeat the last jump.

[`jump-backward`](#jump-backward) `to` (vi: F) (emacs: F)
: Jump backwards to the specified text.

[`jump-forward`](#jump-forward) `to` (vi: f) (emacs: f)
: Jump forward to the specified text.

[`jump-reverse`](#jump-reverse) (vi: ,) (emacs: ,)
: Repeat the last jump in the reverse direction (forward becomes backward and backward becomes forward).

[`jump-to-backward`](#jump-to-backward) `to` (vi: T)
: Jump backwards, but one character less, placing the cursor on the character after the target.

[`jump-to-forward`](#jump-to-forward) `to` (vi: t)
: Jump forward, but one character less, placing the cursor on the character before the target.

[`jump-to-mark`](#jump-to-mark) (vi: M-x) (emacs: M-x)
: Jump to the last mark.

[`middle-line`](#middle-line) (vi: M) (emacs: M-r)
: Move to the middle line.

[`next-matching-bracket`](#next-matching-bracket) (vi: %) (emacs: M-C-f)
: Move to the next matching bracket.

[`next-paragraph`](#next-paragraph) (vi: }) (emacs: M-})
: Move to the next paragraph.

[`next-prompt`](#next-prompt) [`-o`]
: Move to the next prompt.

[`next-word`](#next-word) (vi: w)
: Move to the next word.

[`next-word-end`](#next-word-end) (vi: e) (emacs: M-f)
: Move to the end of the next word.

[`next-space`](#next-space) (vi: W)
: Same as `next-word` but use a space alone as the word separator.

[`next-space-end`](#next-space-end) (vi: E)
: Same as `next-word-end` but use a space alone as the word separator.

[`other-end`](#other-end) (vi: o)
: Switch at which end of the selection the cursor sits.

[`page-down`](#page-down) (vi: C-f) (emacs: PageDown)
: Scroll down by one page.

[`page-down-and-cancel`](#page-down-and-cancel)
: Same as `page-down` but also exit copy mode if reaching the bottom.

[`page-up`](#page-up) (vi: C-b) (emacs: PageUp)
: Scroll up by one page.

: Same as `pipe` but do not clear the selection.

: Same as `pipe` but also exit copy mode.

[`previous-matching-bracket`](#previous-matching-bracket) (emacs: M-C-b)
: Move to the previous matching bracket.

[`previous-paragraph`](#previous-paragraph) (vi: ](#previous-prompt) [`-o`]
: Move to the previous prompt.

[`previous-word`](#previous-word) (vi: b) (emacs: M-b)
: Move to the previous word.

[`previous-space`](#previous-space) (vi: B)
: Same as `previous-word` but use a space alone as the word separator.

[`rectangle-on`](#rectangle-on)
: Turn on rectangle selection mode.

[`rectangle-off`](#rectangle-off)
: Turn off rectangle selection mode.

[`rectangle-toggle`](#rectangle-toggle) (vi: v) (emacs: R)
: Toggle rectangle selection mode.

[`refresh-from-pane`](#refresh-from-pane) (vi: r) (emacs: r)
: Refresh the content from the pane.

[`scroll-bottom`](#scroll-bottom)
: Scroll up until the current line is at the bottom while keeping the cursor on that line.

[`scroll-down`](#scroll-down) (vi: C-e) (emacs: C-Down)
: Scroll down.

[`scroll-down-and-cancel`](#scroll-down-and-cancel)
: Same as `scroll-down` but also exit copy mode if the cursor reaches the bottom.

[`scroll-middle`](#scroll-middle) (vi: z)
: Scroll so that the current line becomes the middle one while keeping the cursor on that line.

[`scroll-to-mouse`](#scroll-to-mouse)
: Scroll pane in copy-mode when bound to a mouse drag event. `-e` causes copy mode to exit when at the bottom.

[`scroll-top`](#scroll-top)
: Scroll down until the current line is at the top while keeping the cursor on that line.

[`scroll-up`](#scroll-up) (vi: C-y) (emacs: C-Up)
: Scroll up.

[`search-again`](#search-again) (vi: n) (emacs: n)
: Repeat the last search.

[`search-backward`](#search-backward) `text` (vi: ?)
: Search backwards for the specified text.

[`search-backward-incremental`](#search-backward-incremental) `text` (emacs: C-r)

[`search-backward-text`](#search-backward-text) `text`
: Search backwards for the specified plain text.

[`search-forward`](#search-forward) `text` (vi: /)
: Search forward for the specified text.

[`search-forward-incremental`](#search-forward-incremental) `text` (emacs: C-s)

[`search-forward-text`](#search-forward-text) `text`
: Search forward for the specified plain text.

[`search-reverse`](#search-reverse) (vi: N) (emacs: N)
: Repeat the last search in the reverse direction (forward becomes backward and backward becomes forward).

[`select-line`](#select-line) (vi: V)
: Select the current line.

[`select-word`](#select-word)
: Select the current word.

[`selection-mode`](#selection-mode) [`char` \| `word` \| `line`]
: Change the selection mode.

[`set-mark`](#set-mark) (vi: X) (emacs: X)
: Mark the current line.

[`start-of-line`](#start-of-line) (vi: 0) (emacs: C-a)
: Move the cursor to the start of the line.

[`stop-selection`](#stop-selection)
: Stop selecting without clearing the current selection.

[`toggle-position`](#toggle-position) (vi: P) (emacs: P)
: Toggle the visibility of the position indicator in the top right.

[`top-line`](#top-line) (vi: H) (emacs: M-R)
: Move to the top line.

The default incremental search key bindings, '`C-r`' and '`C-s`', are designed to emulate [emacs(1)](/emacs.1). When first pressed they allow a new search term to be entered; if pressed with an empty search term they repeat the previously used search term.

The next and previous word keys skip over whitespace and treat consecutive runs of either word separators or other letters as words. Word separators can be customized with the *word-separators* session option. Next word moves to the start of the next word, next word end to the end of the next word and previous word to the start of the previous word. The three next and previous space keys work similarly but use a space alone as the word separator. Setting *word-separators* to the empty string makes next/previous word equivalent to next/previous space.

[`copy-mode`](#copy-mode) [`-deHMqSu`] [`-s` `src-pane`] [`-t` `target-pane`]

: Enter copy mode.

 `-u` enters copy mode and scrolls one page up and `-d` one page down. `-H` hides the position indicator in the top right. `-q` cancels copy mode and any other modes.

 `-M` begins a mouse drag (only valid if bound to a mouse key binding, see [MOUSE SUPPORT](#MOUSE_SUPPORT)).

 `-S` enters copy-mode and scrolls when bound to a mouse drag event; See `scroll-to-mouse`.

 `-s` copies from `src-pane` instead of `target-pane`.

 `-e` specifies that scrolling to the bottom of the history (to the visible screen) should exit copy mode. While in copy mode, pressing a key other than those used for scrolling will disable this behaviour. This is intended to allow fast scrolling through a pane's history, for example with:

 ::: 
 bind PageUp copy-mode -eu
 bind PageDown copy-mode -ed
 :::

The following layouts are supported:

[`even-horizontal`](#even-horizontal)
: Panes are spread out evenly from left to right across the window.

[`even-vertical`](#even-vertical)
: Panes are spread evenly from top to bottom.

[`main-horizontal`](#main-horizontal)
: A large (main) pane is shown at the top of the window and the remaining panes are spread from left to right in the leftover space at the bottom. Use the *main-pane-height* window option to specify the height of the top pane.

[`main-horizontal-mirrored`](#main-horizontal-mirrored)
: The same as `main-horizontal` but mirrored so the main pane is at the bottom of the window.

[`main-vertical`](#main-vertical)
: A large (main) pane is shown on the left of the window and the remaining panes are spread from top to bottom in the leftover space on the right. Use the *main-pane-width* window option to specify the width of the left pane.

[`main-vertical-mirrored`](#main-vertical-mirrored)
: The same as `main-vertical` but mirrored so the main pane is on the right of the window.

[`tiled`](#tiled)
: Panes are spread out as evenly as possible over the window in both rows and columns.

 $ tmux list-windows
 0: ksh [159x48]
 layout: bb62,159x48,0,0
 $ tmux select-layout 'bb62,159x48,0,0'

`tmux` automatically adjusts the size of the layout for the current window size. Note that a layout cannot be applied to a window with more panes than that from which the layout was originally defined.

[`break-pane`](#break-pane) [`-abdP`] [`-F` `format`] [`-n` `window-name`] [`-s` `src-pane`] [`-t` `dst-window`]

: ::: 
 (alias: `breakp`)
 :::

 Break `src-pane` off from its containing window to make it the only pane in `dst-window`. With `-a` or `-b`, the window is moved to the next index after or before (existing windows are moved if necessary). If `-d` is given, the new window does not become the current window. The `-P` option prints information about the new window after it has been created. By default, it uses the format '`#:#.#`' but a different format may be specified with `-F`.

[`capture-pane`](#capture-pane) [`-aepPqCJMN`] [`-b` `buffer-name`] [`-E` `end-line`] [`-S` `start-line`] [`-t` `target-pane`]

: ::: 
 (alias: `capturep`)
 :::

 Capture the contents of a pane. If `-p` is given, the output goes to stdout, otherwise to the buffer specified with `-b` or a new buffer if omitted. If `-a` is given, the alternate screen is used, and the history is not accessible. If no alternate screen exists, an error will be returned unless `-q` is given. Similarly, if the pane is in a mode, `-M` uses the screen for the mode. If `-e` is given, the output includes escape sequences for text and background attributes. `-C` also escapes non-printable characters as octal \\xxx. `-T` ignores trailing positions that do not contain a character. `-N` preserves trailing spaces at each line's end and `-J` preserves trailing spaces and joins any wrapped lines; `-J` implies `-T`. `-P` captures only any output that the pane has received that is the beginning of an as-yet incomplete escape sequence.

 `-S` and `-E` specify the starting and ending line numbers, zero is the first line of the visible pane and negative numbers are lines in the history. '`-`' to `-S` is the start of the history and to `-E` the end of the visible pane. The default is to capture only the visible contents of the pane.

[`choose-client`](#choose-client) [`-NryZ`] [`-F` `format`] [`-f` `filter`] [`-K` `key-format`] [`-O` `sort-order`] [`-t` `target-pane`] [`template`]

 [**Key**](#Key) [**Function**](#Function)
 [`Enter`](#Enter) Choose selected client
 [`Up`](#Up) Select previous client
 [`Down`](#Down) Select next client
 [`C-s`](#C-s) Search by name
 [`n`](#n) Repeat last search forwards
 [`N`](#N~2) Repeat last search backwards
 [`t`](#t) Toggle if client is tagged
 [`T`](#T~2) Tag no clients
 [`C-t`](#C-t) Tag all clients
 [`d`](#d) Detach selected client
 [`D`](#D~2) Detach tagged clients
 [`x`](#x) Detach and HUP selected client
 [`X`](#X) Detach and HUP tagged clients
 [`z`](#z) Suspend selected client
 [`Z`](#Z) Suspend tagged clients
 [`f`](#f~2) Enter a format to filter items
 [`O`](#O) Change sort field
 [`r`](#r) Reverse sort order
 [`v`](#v~2) Toggle preview
 [`q`](#q) Exit mode

[`choose-tree`](#choose-tree) [`-GNrswyZ`] [`-F` `format`] [`-f` `filter`] [`-K` `key-format`] [`-O` `sort-order`] [`-t` `target-pane`] [`template`]

 [**Key**](#Key~2) [**Function**](#Function~2)
 [`Enter`](#Enter~2) Choose selected item
 [`Up`](#Up~2) Select previous item
 [`Down`](#Down~2) Select next item
 [`S-Up`](#S-Up) Swap the current window with the previous one
 [`S-Down`](#S-Down) Swap the current window with the next one
 [`+`](#+) Expand selected item
 `-` Collapse selected item
 [`M-+`](#M-+) Expand all items
 [`M--`](#M--) Collapse all items
 [`x`](#x~2) Kill selected item
 [`X`](#X~2) Kill tagged items
 [`<`](#_) Scroll list of previews left
 [`>`](#_~2) Scroll list of previews right
 [`C-s`](#C-s~2) Search by name
 [`m`](#m) Set the marked pane
 [`M`](#M) Clear the marked pane
 [`n`](#n~2) Repeat last search forwards
 [`N`](#N~3) Repeat last search backwards
 [`t`](#t~2) Toggle if item is tagged
 [`T`](#T~3) Tag no items
 [`C-t`](#C-t~2) Tag all items
 [`f`](#f~3) Enter a format to filter items
 [`H`](#H) Jump to the starting pane
 [`O`](#O~2) Change sort field
 [`r`](#r~2) Reverse sort order
 [`v`](#v~3) Toggle preview
 [`q`](#q~2) Exit mode

[`customize-mode`](#customize-mode) [`-NZ`] [`-F` `format`] [`-f` `filter`] [`-t` `target-pane`] [`template`]

: Put a pane into customize mode, where options and key bindings may be browsed and modified from a list. Option values in the list are shown for the active pane in the current window. `-Z` zooms the pane. The following keys may be used in customize mode:

 [**Key**](#Key~3) [**Function**](#Function~3)
 [`Enter`](#Enter~3) Set pane, window, session or global option value
 [`Up`](#Up~3) Select previous item
 [`Down`](#Down~3) Select next item
 [`+`](#+~2) Expand selected item
 `-` Collapse selected item
 [`M-+`](#M-+~2) Expand all items
 [`M--`](#M--~2) Collapse all items
 [`s`](#s) Set option value or key attribute
 [`S`](#S~2) Set global option value
 [`w`](#w) Set window option value, if option is for pane and window
 [`d`](#d~2) Set an option or key to the default
 [`D`](#D~3) Set tagged options and tagged keys to the default
 [`u`](#u~2) Unset an option (set to default value if global) or unbind a key
 [`U`](#U) Unset tagged options and unbind tagged keys
 [`C-s`](#C-s~3) Search by name
 [`n`](#n~3) Repeat last search forwards
 [`N`](#N~4) Repeat last search backwards
 [`t`](#t~3) Toggle if item is tagged
 [`T`](#T~4) Tag no items
 [`C-t`](#C-t~3) Tag all items
 [`f`](#f~4) Enter a format to filter items
 [`v`](#v~4) Toggle option information
 [`q`](#q~3) Exit mode

[`display-panes`](#displayp) [`-bN`] [`-d` `duration`] [`-t` `target-client`] [`template`]

: ::: 
 (alias: `displayp`)
 :::

[`find-window`](#find-window) [`-iCNrTZ`] [`-t` `target-pane`] `match-string`

: ::: 
 (alias: `findw`)
 :::

 Search for a [glob(7)](/glob.7) pattern or, with `-r`, regular expression `match-string` in window names, titles, and visible content (but not history). The flags control matching behavior: `-C` matches only visible window contents, `-N` matches only the window name and `-T` matches only the window title. `-i` makes the search ignore case. The default is `-CNT`. `-Z` zooms the pane.

[`join-pane`](#join-pane) [`-bdfhv`] [`-l` `size`] [`-s` `src-pane`] [`-t` `dst-pane`]

: ::: 
 (alias: `joinp`)
 :::

 Like `split-window`, but instead of splitting `dst-pane` and creating a new pane, split it and move `src-pane` into the space. This can be used to reverse `break-pane`. The `-b` option causes `src-pane` to be joined to left of or above `dst-pane`.

 If `-s` is omitted and a marked pane is present (see `select-pane` `-m`), the marked pane is used rather than the current pane.

[`kill-pane`](#kill-pane) [`-a`] [`-t` `target-pane`]

: ::: 
 (alias: `killp`)
 :::

 Destroy the given pane. If no panes remain in the containing window, it is also destroyed. The `-a` option kills all but the pane given with `-t`.

[`kill-window`](#kill-window) [`-a`] [`-t` `target-window`]

: ::: 
 (alias: `killw`)
 :::

 Kill the current window or the window at `target-window`, removing it from any sessions to which it is linked. The `-a` option kills all but the window given with `-t`.

[`last-pane`](#last-pane) [`-deZ`] [`-t` `target-window`]

: ::: 
 (alias: `lastp`)
 :::

 Select the last (previously selected) pane. `-Z` keeps the window zoomed if it was zoomed. `-e` enables or `-d` disables input to the pane.

[`last-window`](#last-window) [`-t` `target-session`]

: ::: 
 (alias: `last`)
 :::

 Select the last (previously selected) window. If no `target-session` is specified, select the last window of the current session.

[`link-window`](#link-window) [`-abdk`] [`-s` `src-window`] [`-t` `dst-window`]

: ::: 
 (alias: `linkw`)
 :::

 Link the window at `src-window` to the specified `dst-window`. If `dst-window` is specified and no such window exists, the `src-window` is linked there. With `-a` or `-b` the window is moved to the next index after or before `dst-window` (existing windows are moved if necessary). If `-k` is given and `dst-window` exists, it is killed, otherwise an error is generated. If `-d` is given, the newly linked window is not selected.

[`list-panes`](#list-panes) [`-as`] [`-F` `format`] [`-f` `filter`] [`-t` `target`]

: ::: 
 (alias: `lsp`)
 :::

 If `-a` is given, `target` is ignored and all panes on the server are listed. If `-s` is given, `target` is a session (or the current session). If neither is given, `target` is a window (or the current window). `-F` specifies the format of each line and `-f` a filter. Only panes for which the filter is true are shown. See the [FORMATS](#FORMATS) section.

[`list-windows`](#list-windows) [`-a`] [`-F` `format`] [`-f` `filter`] [`-t` `target-session`]

: ::: 
 (alias: `lsw`)
 :::

 If `-a` is given, list all windows on the server. Otherwise, list windows in the current session or in `target-session`. `-F` specifies the format of each line and `-f` a filter. Only windows for which the filter is true are shown. See the [FORMATS](#FORMATS) section.

[`move-pane`](#move-pane) [`-bdfhv`] [`-l` `size`] [`-s` `src-pane`] [`-t` `dst-pane`]

: ::: 
 (alias: `movep`)
 :::

 Does the same as `join-pane`.

[`move-window`](#move-window) [`-abrdk`] [`-s` `src-window`] [`-t` `dst-window`]

: ::: 
 (alias: `movew`)
 :::

 This is similar to `link-window`, except the window at `src-window` is moved to `dst-window`. With `-r`, all windows in the session are renumbered in sequential order, respecting the `base-index` option.

: ::: 
 (alias: `neww`)
 :::

 Create a new window. With `-a` or `-b`, the new window is inserted at the next index after or before the specified `target-window`, moving windows up if necessary; otherwise `target-window` is the new window location.

 `-e` takes the form '`VARIABLE=value`' and sets an environment variable for the newly created window; it may be specified multiple times.

 The `TERM` environment variable must be set to '`screen`' or '`tmux`' for all programs running [*inside*](#inside) `tmux`. New windows will automatically have '`TERM=screen`' added to their environment, but care must be taken not to reset this in shell start-up files or by the `-e` option.

 The `-P` option prints information about the new window after it has been created. By default, it uses the format '`#:#`' but a different format may be specified with `-F`.

[`next-layout`](#next-layout) [`-t` `target-window`]

: ::: 
 (alias: `nextl`)
 :::

 Move a window to the next layout and rearrange the panes to fit.

[`next-window`](#next-window) [`-a`] [`-t` `target-session`]

: ::: 
 (alias: `next`)
 :::

 Move to the next window in the session. If `-a` is used, move to the next window with an alert.

: ::: 
 (alias: `pipep`)
 :::

 The `-o` option only opens a new pipe if no previous pipe exists, allowing a pipe to be toggled with a single key, for example:

 ::: 
 bind-key C-p pipe-pane -o 'cat >>~/output.#I-#P'
 :::

[`previous-layout`](#previous-layout) [`-t` `target-window`]

: ::: 
 (alias: `prevl`)
 :::

 Move to the previous layout in the session.

[`previous-window`](#previous-window) [`-a`] [`-t` `target-session`]

: ::: 
 (alias: `prev`)
 :::

 Move to the previous window in the session. With `-a`, move to the previous window with an alert.

[`rename-window`](#rename-window) [`-t` `target-window`] `new-name`

: ::: 
 (alias: `renamew`)
 :::

 Rename the current window, or the window at `target-window` if specified, to `new-name`.

[`resize-pane`](#resize-pane) [`-DLMRTUZ`] [`-t` `target-pane`] [`-x` `width`] [`-y` `height`] [`adjustment`]

: ::: 
 (alias: `resizep`)
 :::

 Resize a pane, up, down, left or right by `adjustment` with `-U`, `-D`, `-L` or `-R`, or to an absolute size with `-x` or `-y`. The `adjustment` is given in lines or columns (the default is 1); `-x` and `-y` may be a given as a number of lines or columns or followed by '`%`' for a percentage of the window size (for example '`-x 10%`'). With `-Z`, the active pane is toggled between zoomed (occupying the whole of the window) and unzoomed (its normal position in the layout).

 `-M` begins mouse resizing (only valid if bound to a mouse key binding, see [MOUSE SUPPORT](#MOUSE_SUPPORT)).

 `-T` trims all lines below the current cursor position and moves lines out of the history to replace them.

[`resize-window`](#resize-window) [`-aADLRU`] [`-t` `target-window`] [`-x` `width`] [`-y` `height`] [`adjustment`]

: ::: 
 (alias: `resizew`)
 :::

: ::: 
 (alias: `respawnp`)
 :::

: ::: 
 (alias: `respawnw`)
 :::

[`rotate-window`](#rotate-window) [`-DUZ`] [`-t` `target-window`]

: ::: 
 (alias: `rotatew`)
 :::

 Rotate the positions of the panes within a window, either upward (numerically lower) with `-U` or downward (numerically higher). `-Z` keeps the window zoomed if it was zoomed.

[`select-layout`](#select-layout) [`-Enop`] [`-t` `target-pane`] [`layout-name`]

: ::: 
 (alias: `selectl`)
 :::

[`select-pane`](#select-pane) [`-DdeLlMmRUZ`] [`-T` `title`] [`-t` `target-pane`]

: ::: 
 (alias: `selectp`)
 :::

 `-m` and `-M` are used to set and clear the [*marked pane*](#marked). There is one marked pane at a time, setting a new marked pane clears the last. The marked pane is the default target for `-s` to `join-pane`, `move-pane`, `swap-pane` and `swap-window`.

[`select-window`](#select-window) [`-lnpT`] [`-t` `target-window`]

: ::: 
 (alias: `selectw`)
 :::

: ::: 
 (alias: `splitw`)
 :::

 Create a new pane by splitting `target-pane`: `-h` does a horizontal split and `-v` a vertical split; if neither is specified, `-v` is assumed. The `-l` option specifies the size of the new pane in lines (for vertical split) or in columns (for horizontal split); `size` may be followed by '`%`' to specify a percentage of the available space. The `-b` option causes the new pane to be created to the left of or above `target-pane`. The `-f` option creates a new pane spanning the full window height (with `-h`) or full window width (with `-v`), instead of splitting the active pane. `-Z` zooms if the window is not zoomed, or keeps it zoomed if already zoomed.

 ::: 
 $ make 2>&1|tmux splitw -dI &
 :::

[`swap-pane`](#swap-pane) [`-dDUZ`] [`-s` `src-pane`] [`-t` `dst-pane`]

: ::: 
 (alias: `swapp`)
 :::

 Swap two panes. If `-U` is used and no source pane is specified with `-s`, `dst-pane` is swapped with the previous pane (before it numerically); `-D` swaps with the next pane (after it numerically). `-d` instructs `tmux` not to change the active pane and `-Z` keeps the window zoomed if it was zoomed.

 If `-s` is omitted and a marked pane is present (see `select-pane` `-m`), the marked pane is used rather than the current pane.

[`swap-window`](#swap-window) [`-d`] [`-s` `src-window`] [`-t` `dst-window`]

: ::: 
 (alias: `swapw`)
 :::

 This is similar to `link-window`, except the source and destination windows are swapped. It is an error if no window exists at `src-window`. If `-d` is given, the new window does not become the current window.

 If `-s` is omitted and a marked pane is present (see `select-pane` `-m`), the window containing the marked pane is used rather than the current window.

[`unlink-window`](#unlink-window) [`-k`] [`-t` `target-window`]

: ::: 
 (alias: `unlinkw`)
 :::

 Unlink `target-window`. Unless `-k` is given, a window may be unlinked only if it is linked to multiple sessions - windows may not be linked to no sessions; if `-k` is specified and the window is linked to only one session, it is unlinked and destroyed.

## KEY BINDINGS

 bind-key '"' split-window
 bind-key "'" new-window

: ::: 
 (alias: `bind`)
 :::

[`list-keys`](#list-keys) [`-1aN`] [`-P` `prefix-string`] [`-T` `key-table`] [`key`]

: ::: 
 (alias: `lsk`)
 :::

 With the default form, all key tables are listed by default. `-T` lists only keys in `key-table`.

[`send-keys`](#send-keys) [`-FHKlMRX`] [`-c` `target-client`] [`-N` `repeat-count`] [`-t` `target-pane`] [`key ...`]

: ::: 
 (alias: `send`)
 :::

 The `-l` flag disables key name lookup and processes the keys as literal UTF-8 characters. The `-H` flag expects each key to be a hexadecimal number for an ASCII character.

 The `-R` flag causes the terminal state to be reset.

 `-M` passes through a mouse event (only valid if bound to a mouse key binding, see [MOUSE SUPPORT](#MOUSE_SUPPORT)).

[`send-prefix`](#send-prefix) [`-2`] [`-t` `target-pane`]
: Send the prefix key, or with `-2` the secondary prefix key, to a window as if it was pressed.

[`unbind-key`](#unbind-key) [`-anq`] [`-T` `key-table`] `key`

: ::: 
 (alias: `unbind`)
 :::

## OPTIONS

 set -w window-style bg=red
 set -pt:.0 window-style bg=blue

`tmux` also supports user options which are prefixed with a '`@`'. User options may have any name, so long as they are prefixed with '`@`', and be set to any string. For example:

 $ tmux set -wq @foo "abc123"
 $ tmux show -wv @foo
 abc123

[`set-option`](#set-option) [`-aFgopqsuUw`] [`-t` `target-pane`] `option` [`value`]

: ::: 
 (alias: `set`)
 :::

 Set a pane option with `-p`, a window option with `-w`, a server option with `-s`, otherwise a session option. If the option is not a user option, `-w` or `-s` may be unnecessary - `tmux` will infer the scope from the option name, assuming `-w` for pane options. If `-g` is given, the global session or window option is set.

 `-F` expands formats in the option value. The `-u` flag unsets an option, so a session inherits the option from the global options (or with `-g`, restores a global option to the default). `-U` unsets an option (like `-u`) but if the option is a pane option also unsets the option on any panes in the window. `value` depends on the option and its type and can be omitted for flag and choice options to toggle its value (choice options toggle between the first two choices).

 The `-o` flag prevents setting an option that is already set and the `-q` flag suppresses errors about unknown or ambiguous options.

 With `-a`, and if the option expects a string or a style, `value` is appended to the existing setting. For example:

 ::: 
 set -g status-left "foo"
 set -ag status-left "bar"
 :::

 Will result in '`foobar`'. And:

 ::: 
 set -g status-style "bg=red"
 set -ag status-style "fg=blue"
 :::

 Will result in a red background [*and*](#and) blue foreground. Without `-a`, the result would be the default background and a blue foreground.

[`show-options`](#show-options) [`-AgHpqsvw`] [`-t` `target-pane`] [`option`]

: ::: 
 (alias: `show`)
 :::

 Show the pane options (or a single option if `option` is provided) with `-p`, the window options with `-w`, the server options with `-s`, otherwise the session options. If the option is not a user option, `-w` or `-s` may be unnecessary - `tmux` will infer the scope from the option name, assuming `-w` for pane options. Global session or window options are listed if `-g` is used. `-v` shows only the option value, not the name. If `-q` is set, no error will be returned if `option` is unset. `-H` includes hooks (omitted by default). `-A` includes options inherited from a parent set of options, such options are marked with an asterisk.

Available server options are:

[`backspace`](#backspace) `key`
: Set the key sent by `tmux` for backspace.

[`buffer-limit`](#buffer-limit) `number`
: Set the number of buffers; as new buffers are added to the top of the stack, old ones are removed from the bottom if necessary to maintain this maximum length.

 ::: 
 :::

 Using:

 ::: 
 `zoom -t:.1`
 :::

 Is equivalent to:

 ::: 
 `resize-pane -Z -t:.1`
 :::

[`codepoint-widths[]`](#codepoint-widths__) `string`
: An array option allowing widths of Unicode codepoints to be overridden. Note the new width applies to all clients. Each entry is of the form [*codepoint=width*](#codepoint=width), where codepoint may be a UTF-8 character or an identifier of the form '`U+number`' where the number is a hexadecimal number.

[`default-terminal`](#default-terminal) `terminal`
: Set the default terminal for new windows created in this session - the default value of the `TERM` environment variable. For `tmux` to work correctly, this [*must*](#must) be set to '`screen`', '`tmux`' or a derivative of them.

[`escape-time`](#escape-time) `time`
: Set the time in milliseconds for which `tmux` waits after an escape is input to determine if it is part of a function or meta key sequences.

[`exit-empty`](#exit-empty) [`on` \| `off`]
: If enabled (the default), the server will exit when there are no active sessions.

[`exit-unattached`](#exit-unattached) [`on` \| `off`]
: If enabled, the server will exit when there are no attached clients.

[`extended-keys`](#extended-keys) [`on` \| `off` \| `always`]

: Controls how modified keys (keys pressed together with Control, Meta, or Shift) are reported. This is the equivalent of the `modifyOtherKeys` [xterm(1)](/xterm.1) resource.

 When set to `on`, the program inside the pane can request one of two modes: mode 1 which changes the sequence for only keys which lack an existing well-known representation; or mode 2 which changes the sequence for all keys. When set to `always`, modes 1 and 2 can still be requested by applications, but mode 1 will be forced instead of the standard mode. When set to `off`, this feature is disabled and only standard keys are reported.

 `tmux` will always request extended keys itself if the terminal supports them. See also the `extkeys` feature for the `terminal-features` option, the `extended-keys-format` option and the `pane_key_mode` variable.

[`extended-keys-format`](#extended-keys-format) [`csi-u` \| `xterm`]
: Selects one of the two possible formats for reporting modified keys to applications. This is the equivalent of the `formatOtherKeys` [xterm(1)](/xterm.1) resource. For example, C-S-a will be reported as '`^[[27;6;65~`' when set to `xterm`, and as '`^[[65;6u`' when set to `csi-u`.

[`focus-events`](#focus-events) [`on` \| `off`]
: When enabled, focus events are requested from the terminal if supported and passed through to applications running in `tmux`. Attached clients should be detached and attached again after changing this option.

[`focus-follows-mouse`](#focus-follows-mouse) [`on` \| `off`]
: When enabled and `mouse` is on, moving the mouse into a pane selects it.

[`get-clipboard`](#get-clipboard) [`both` \| `request` \| `buffer` \| `off`]

: Controls the behaviour when an application requests the clipboard from `tmux`.

 If `off`, the request is ignored; if `buffer`, `tmux` responds with the newest paste buffer; `request` causes `tmux` to request the clipboard from the most recently used client (if possible) and send the reply (if any) back to the application; `buffer` is the same as `request` but also creates a paste buffer.

 See also the `set-clipboard` option.

[`history-file`](#history-file) `path`

[`input-buffer-size`](#input-buffer-size) `bytes`
: Maximum of bytes allowed to read in escape and control sequences. Once reached, the sequence will be discarded.

[`message-limit`](#message-limit) `number`
: Set the number of error or information messages to save in the message log for each client.

[`prompt-history-limit`](#prompt-history-limit) `number`

[`set-clipboard`](#set-clipboard) [`on` \| `external` \| `off`]

: Attempt to set the terminal clipboard content using the [xterm(1)](/xterm.1) escape sequence, if there is an *Ms* entry in the [terminfo(5)](/terminfo.5) description (see the [TERMINFO EXTENSIONS](#TERMINFO_EXTENSIONS) section).

 If set to `on`, `tmux` will both accept the escape sequence to create a buffer and attempt to set the terminal clipboard. If set to `external`, `tmux` will attempt to set the terminal clipboard but ignore attempts by applications to set `tmux` buffers. If `off`, `tmux` will neither accept the clipboard escape sequence nor attempt to set the clipboard.

 Note that this feature needs to be enabled in [xterm(1)](/xterm.1) by setting the resource:

 ::: 
 disallowedWindowOps: 20,21,SetXprop
 :::

 Or changing this property from the [xterm(1)](/xterm.1) interactive menu when required.

[`terminal-features[]`](#terminal-features__) `string`

: Set terminal features for terminal types read from [terminfo(5)](/terminfo.5). `tmux` has a set of named terminal features. Each will apply appropriate changes to the [terminfo(5)](/terminfo.5) entry in use.

 `tmux` can detect features for a few common terminals; this option can be used to easily tell tmux about features supported by terminals it cannot detect. The `terminal-overrides` option allows individual [terminfo(5)](/terminfo.5) capabilities to be set instead, `terminal-features` is intended for classes of functionality supported in a standard way but not reported by [terminfo(5)](/terminfo.5). Care must be taken to configure this only with features the terminal actually supports.

 This is an array option where each entry is a colon-separated string made up of a terminal type pattern (matched using [glob(7)](/glob.7) patterns) followed by a list of terminal features. The available features are:

 256
 : Supports 256 colours with the SGR escape sequences.

 clipboard
 : Allows setting the system clipboard.

 ccolour
 : Allows setting the cursor colour.

 cstyle
 : Allows setting the cursor style.

 extkeys
 : Supports extended keys.

 focus
 : Supports focus reporting.

 hyperlinks
 : Supports OSC 8 hyperlinks.

 ignorefkeys
 : Ignore function keys from [terminfo(5)](/terminfo.5) and use the `tmux` internal set only.

 margins
 : Supports DECSLRM margins.

 mouse
 : Supports [xterm(1)](/xterm.1) mouse sequences.

 osc7
 : Supports the OSC 7 working directory extension.

 overline
 : Supports the overline SGR attribute.

 rectfill
 : Supports the DECFRA rectangle fill escape sequence.

 RGB
 : Supports RGB colour with the SGR escape sequences.

 sixel
 : Supports SIXEL graphics.

 strikethrough
 : Supports the strikethrough SGR escape sequence.

 sync
 : Supports synchronized updates.

 title
 : Supports [xterm(1)](/xterm.1) title setting.

 usstyle
 : Allows underscore style and colour to be set.

[`terminal-overrides[]`](#terminal-overrides__) `string`

: Allow terminal descriptions read using [terminfo(5)](/terminfo.5) to be overridden. Each entry is a colon-separated string made up of a terminal type pattern (matched using [glob(7)](/glob.7) patterns) and a set of [*name=value*](#name=value) entries.

 For example, to set the '`clear`' [terminfo(5)](/terminfo.5) entry to '`\e[H\e[2J`' for all terminal types matching '`rxvt*`':

 ::: 
 `rxvt*:clear=\e[H\e[2J`
 :::

 The terminal entry value is passed through [strunvis(3)](/strunvis.3) before interpretation.

[`user-keys[]`](#user-keys__) `key`

: Set list of user-defined key escape sequences. Each item is associated with a key named '`User0`', '`User1`', and so on.

 For example:

 ::: 
 set -s user-keys[0] "\e[5;30012~"
 bind User0 resize-pane -L 3
 :::

[`variation-selector-always-wide`](#variation-selector-always-wide) [`on` \| `off`]
: Always treat Unicode variation selector 16 as marking a wide character. This is a feature of some terminals as part of their Unicode 14 support.

Available session options are:

[`activity-action`](#activity-action) [`any` \| `none` \| `current` \| `other`]
: Set action on window activity when `monitor-activity` is on. `any` means activity in any window linked to a session causes a bell or message (depending on `visual-activity`) in the current window of that session, `none` means all activity is ignored (equivalent to `monitor-activity` being off), `current` means only activity in windows other than the current window are ignored and `other` means activity in the current window is ignored but not those in other windows.

[`assume-paste-time`](#assume-paste-time) `milliseconds`
: If keys are entered faster than one in `milliseconds`, they are assumed to have been pasted rather than typed and `tmux` key bindings are not processed. The default is one millisecond and zero disables.

[`base-index`](#base-index) `index`
: Set the base index from which an unused index should be searched when a new window is created. The default is zero.

[`bell-action`](#bell-action) [`any` \| `none` \| `current` \| `other`]
: Set action on a bell in a window when `monitor-bell` is on. The values are the same as those for `activity-action`.

[`default-shell`](#default-shell) `path`

[`default-size`](#default-size) `XxY`

[`destroy-unattached`](#destroy-unattached) [`off` \| `on` \| `keep-last` \| `keep-group`]
: If `on`, destroy the session after the last client has detached. If `off` (the default), leave the session orphaned. If `keep-last`, destroy the session only if it is in a group and has other sessions in that group. If `keep-group`, destroy the session unless it is in a group and is the only session in that group.

[`detach-on-destroy`](#detach-on-destroy) [`off` \| `on` \| `no-detached` \| `previous` \| `next`]
: If `on` (the default), the client is detached when the session it is attached to is destroyed. If `off`, the client is switched to the most recently active of the remaining sessions. If `no-detached`, the client is detached only if there are no detached sessions; if detached sessions exist, the client is switched to the most recently active. If `previous` or `next`, the client is switched to the previous or next session in alphabetical order.

[`display-panes-active-colour`](#display-panes-active-colour) `colour`

[`display-panes-colour`](#display-panes-colour) `colour`

[`display-panes-time`](#display-panes-time) `time`

[`display-time`](#display-time) `time`
: Set the amount of time for which status line messages and other on-screen indicators are displayed. If set to 0, messages and indicators are displayed until a key is pressed. `time` is in milliseconds.

[`history-limit`](#history-limit) `lines`
: Set the maximum number of lines held in window history. This setting applies only to new windows - existing window histories are not resized and retain the limit at the point they were created.

[`initial-repeat-time`](#initial-repeat-time) `time`

[`key-table`](#key-table) `key-table`
: Set the default key table to `key-table` instead of *root*.

[`lock-after-time`](#lock-after-time) `number`

[`menu-style`](#menu-style) `style`
: Set the menu style. See the [STYLES](#STYLES) section on how to specify `style`.

[`menu-selected-style`](#menu-selected-style) `style`
: Set the selected menu item style. See the [STYLES](#STYLES) section on how to specify `style`.

[`menu-border-style`](#menu-border-style) `style`
: Set the menu border style. See the [STYLES](#STYLES) section on how to specify `style`.

[`menu-border-lines`](#menu-border-lines) `type`
: Set the type of characters used for drawing menu borders. See `popup-border-lines` for possible values for `border-lines`.

[`message-line`](#message-line) [`0` \| `1` \| `2` \| `3` \| `4`]

[`message-style`](#message-style) `style`

[`mouse`](#mouse) [`on` \| `off`]
: If on, `tmux` captures the mouse and allows mouse events to be bound as key bindings. See the [MOUSE SUPPORT](#MOUSE_SUPPORT) section for details.

[`prefix`](#prefix) `key`
: Set the key accepted as a prefix key. In addition to the standard keys described under [KEY BINDINGS](#KEY_BINDINGS), `prefix` can be set to the special key '`None`' to set no prefix.

[`prefix2`](#prefix2) `key`
: Set a secondary key accepted as a prefix key. Like `prefix`, `prefix2` can be set to '`None`'.

[`prefix-timeout`](#prefix-timeout) `time`
: Set the time in milliseconds for which `tmux` waits after `prefix` is input before dismissing it. Can be set to zero to disable any timeout.

[`prompt-cursor-colour`](#prompt-cursor-colour) `colour`

[`prompt-cursor-style`](#prompt-cursor-style) `style`

[`renumber-windows`](#renumber-windows) [`on` \| `off`]
: If on, when a window is closed in a session, automatically renumber the other windows in numerical order. This respects the `base-index` option if it has been set. If off, do not renumber the windows.

[`repeat-time`](#repeat-time) `time`

[`set-titles`](#set-titles) [`on` \| `off`]
: Attempt to set the client terminal title using the [*tsl*](#tsl) and *fsl* [terminfo(5)](/terminfo.5) entries if they exist. `tmux` automatically sets these to the \\e]0;\...\\007 sequence if the terminal appears to be [xterm(1)](/xterm.1). This option is off by default.

[`set-titles-string`](#set-titles-string) `string`
: String used to set the client terminal title if `set-titles` is on. Formats are expanded, see the [FORMATS](#FORMATS) section.

[`silence-action`](#silence-action) [`any` \| `none` \| `current` \| `other`]
: Set action on window silence when `monitor-silence` is on. The values are the same as those for `activity-action`.

[`status`](#status) [`off` \| `on` \| `2` \| `3` \| `4` \| `5`]
: Show or hide the status line or specify its size. Using `on` gives a status line one row in height; `2`, `3`, `4` or `5` more rows.

[`status-format[]`](#status-format__) `format`
: Specify the format to be used for each line of the status line. The default builds the top status line from the various individual status options below.

[`status-interval`](#status-interval) `interval`
: Update the status line every `interval` seconds. By default, updates will occur every 15 seconds. A setting of zero disables redrawing at interval.

[`status-justify`](#status-justify) [`left` \| `centre` \| `right` \| `absolute-centre`]
: Set the position of the window list in the status line: left, centre or right. centre puts the window list in the relative centre of the available free space; absolute-centre uses the centre of the entire horizontal space.

[`status-keys`](#status-keys) [`vi` \| `emacs`]

[`status-left`](#status-left) `string`

: Display `string` (by default the session name) to the left of the status line. `string` will be passed through [strftime(3)](/strftime.3). Also see the [FORMATS](#FORMATS) and [STYLES](#STYLES) sections.

 For details on how the names and titles can be set see the [NAMES AND TITLES](#NAMES_AND_TITLES) section.

 Examples are:

 ::: 
 #(sysctl vm.loadavg)
 #[fg=yellow,bold]#(apm -l)%%#[default] [#S]
 :::

 The default is '`[#S] `'.

[`status-left-length`](#status-left-length) `length`
: Set the maximum `length` of the left component of the status line. The default is 10.

[`status-left-style`](#status-left-style) `style`
: Set the style of the left part of the status line. For how to specify `style`, see the [STYLES](#STYLES) section.

[`status-position`](#status-position) [`top` \| `bottom`]
: Set the position of the status line.

[`status-right`](#status-right) `string`
: Display `string` to the right of the status line. By default, the current pane title in double quotes, the date and the time are shown. As with `status-left`, `string` will be passed to [strftime(3)](/strftime.3) and character pairs are replaced.

[`status-right-length`](#status-right-length) `length`
: Set the maximum `length` of the right component of the status line. The default is 40.

[`status-right-style`](#status-right-style) `style`
: Set the style of the right part of the status line. For how to specify `style`, see the [STYLES](#STYLES) section.

[`status-style`](#status-style) `style`
: Set status line style. For how to specify `style`, see the [STYLES](#STYLES) section.

[`update-environment[]`](#update-environment__) `variable`

[`visual-activity`](#visual-activity) [`on` \| `off` \| `both`]
: If on, display a message instead of sending a bell when activity occurs in a window for which the `monitor-activity` window option is enabled. If set to both, a bell and a message are produced.

[`visual-bell`](#visual-bell) [`on` \| `off` \| `both`]
: If on, a message is shown on a bell in a window for which the `monitor-bell` window option is enabled instead of it being passed through to the terminal (which normally makes a sound). If set to both, a bell and a message are produced. Also see the `bell-action` option.

[`visual-silence`](#visual-silence) [`on` \| `off` \| `both`]
: If `monitor-silence` is enabled, prints a message after the interval has expired on a given window instead of sending a bell. If set to both, a bell and a message are produced.

[`word-separators`](#word-separators) `string`

Available window options are:

[`aggressive-resize`](#aggressive-resize) [`on` \| `off`]
: Aggressively resize the chosen window. This means that `tmux` will resize the window to the size of the smallest or largest session (see the `window-size` option) for which it is the current window, rather than the session to which it is attached. The window may resize when the current window is changed on another session; this option is good for full-screen programs which support `SIGWINCH` and poor for interactive programs such as shells.

[`automatic-rename`](#automatic-rename) [`on` \| `off`]
: Control automatic window renaming. When this setting is enabled, `tmux` will rename the window automatically using the format specified by `automatic-rename-format`. This flag is automatically disabled for an individual window when a name is specified at creation with `new-window` or `new-session`, or later with `rename-window`, or with a terminal escape sequence. It may be switched off globally with:
 ::: 
 set-option -wg automatic-rename off
 :::

[`automatic-rename-format`](#automatic-rename-format) `format`
: The format (see [FORMATS](#FORMATS)) used when the `automatic-rename` option is enabled.

[`clock-mode-colour`](#clock-mode-colour) `colour`
: Set clock colour.

[`clock-mode-style`](#clock-mode-style) [`12` \| `24` \| `12-with-seconds` \| `24-with-seconds`]
: Set clock hour format.

[`fill-character`](#fill-character) `character`
: Set the character used to fill areas of the terminal unused by a window.

[`main-pane-height`](#main-pane-height) `height`
:  

[`main-pane-width`](#main-pane-width) `width`
: Set the width or height of the main (left or top) pane in the `main-horizontal`, `main-horizontal-mirrored`, `main-vertical`, or `main-vertical-mirrored` layouts. If suffixed by '`%`', this is a percentage of the window size.

[`copy-mode-match-style`](#copy-mode-match-style) `style`
: Set the style of search matches in copy mode. For how to specify `style`, see the [STYLES](#STYLES) section.

[`copy-mode-mark-style`](#copy-mode-mark-style) `style`
: Set the style of the line containing the mark in copy mode. For how to specify `style`, see the [STYLES](#STYLES) section.

[`copy-mode-current-match-style`](#copy-mode-current-match-style) `style`
: Set the style of the current search match in copy mode. For how to specify `style`, see the [STYLES](#STYLES) section.

[`copy-mode-position-format`](#copy-mode-position-format) `format`
: Format of the position indicator in copy mode.

[`mode-keys`](#mode-keys) [`vi` \| `emacs`]
: Use vi or emacs-style key bindings in copy mode. The default is emacs, unless `VISUAL` or `EDITOR` contains '`vi`'.

[`copy-mode-position-style`](#copy-mode-position-style) `style`
: Set the style of the position indicator in copy mode. For how to specify `style`, see the [STYLES](#STYLES) section.

[`copy-mode-selection-style`](#copy-mode-selection-style) `style`
: Set the style of the selection in copy mode. For how to specify `style`, see the [STYLES](#STYLES) section.

[`mode-style`](#mode-style) `style`
: Set window modes style. For how to specify `style`, see the [STYLES](#STYLES) section.

[`monitor-activity`](#monitor-activity) [`on` \| `off`]
: Monitor for activity in the window. Windows with activity are highlighted in the status line.

[`monitor-bell`](#monitor-bell) [`on` \| `off`]
: Monitor for a bell in the window. Windows with a bell are highlighted in the status line.

[`monitor-silence`](#monitor-silence) [`interval`]
: Monitor for silence (no activity) in the window within `interval` seconds. Windows that have been silent for the interval are highlighted in the status line. An interval of zero disables the monitoring.

[`other-pane-height`](#other-pane-height) `height`
: Set the height of the other panes (not the main pane) in the `main-horizontal` and `main-horizontal-mirrored` layouts. If this option is set to 0 (the default), it will have no effect. If both the `main-pane-height` and `other-pane-height` options are set, the main pane will grow taller to make the other panes the specified height, but will never shrink to do so. If suffixed by '`%`', this is a percentage of the window size.

[`other-pane-width`](#other-pane-width) `width`
: Like `other-pane-height`, but set the width of other panes in the `main-vertical` and `main-vertical-mirrored` layouts.

[`pane-active-border-style`](#pane-active-border-style) `style`
: Set the pane border style for the currently active pane. For how to specify `style`, see the [STYLES](#STYLES) section. Attributes are ignored.

[`pane-base-index`](#pane-base-index) `index`
: Like `base-index`, but set the starting index for pane numbers.

[`pane-border-format`](#pane-border-format) `format`
: Set the text shown in pane border status lines.

[`pane-border-indicators`](#pane-border-indicators) [`off` \| `colour` \| `arrows` \| `both`]
: Indicate active pane by colouring only half of the border in windows with exactly two panes, by displaying arrow markers, by drawing both or neither.

[`pane-border-lines`](#pane-border-lines) `type`

: Set the type of characters used for drawing pane borders. `type` may be one of:

 single
 : single lines using ACS or UTF-8 characters

 double
 : double lines using UTF-8 characters

 heavy
 : heavy lines using UTF-8 characters

 simple
 : simple ASCII characters

 number
 : the pane number

 spaces
 : space characters

 '`double`' and '`heavy`' will fall back to standard ACS line drawing when UTF-8 is not supported.

[`pane-border-status`](#pane-border-status) [`off` \| `top` \| `bottom`]
: Turn pane border status lines off or set their position.

[`pane-border-style`](#pane-border-style) `style`
: Set the pane border style for panes aside from the active pane. For how to specify `style`, see the [STYLES](#STYLES) section. Attributes are ignored.

[`popup-style`](#popup-style) `style`
: Set the popup style. See the [STYLES](#STYLES) section on how to specify `style`. Attributes are ignored.

[`popup-border-style`](#popup-border-style) `style`
: Set the popup border style. See the [STYLES](#STYLES) section on how to specify `style`. Attributes are ignored.

[`popup-border-lines`](#popup-border-lines) `type`

: Set the type of characters used for drawing popup borders. `type` may be one of:

 single
 : single lines using ACS or UTF-8 characters (default)

 rounded
 : variation of single with rounded corners using UTF-8 characters

 double
 : double lines using UTF-8 characters

 heavy
 : heavy lines using UTF-8 characters

 simple
 : simple ASCII characters

 padded
 : simple ASCII space character

 none
 : no border

 '`double`' and '`heavy`' will fall back to standard ACS line drawing when UTF-8 is not supported.

[`pane-scrollbars`](#pane-scrollbars) [`off` \| `modal` \| `on`]

: When enabled, a character based scrollbar appears on the left or right of each pane. A filled section of the scrollbar, known as the '`slider`', represents the position and size of the visible part of the pane content.

 If set to `on` the scrollbar is visible all the time. If set to `modal` the scrollbar only appears when the pane is in copy mode or view mode. When the scrollbar is visible, the pane is narrowed by the width of the scrollbar and the text in the pane is reflowed. If set to `modal`, the pane is narrowed only when the scrollbar is visible.

 See also `pane-scrollbars-style`.

[`pane-scrollbars-style`](#pane-scrollbars-style) `style`
: Set the scrollbars style. For how to specify `style`, see the [STYLES](#STYLES) section. The foreground colour is used for the slider, the background for the rest of the scrollbar. The `width` attribute sets the width of the scrollbar and the `pad` attribute the padding between the scrollbar and the pane. Other attributes are ignored.

[`pane-scrollbars-position`](#pane-scrollbars-position) [`left` \| `right`]
: Sets which side of the pane to display pane scrollbars on.

[`pane-status-current-style`](#pane-status-current-style) `style`
: Set status line style for the currently active pane. For how to specify `style`, see the [STYLES](#STYLES) section.

[`pane-status-style`](#pane-status-style) `style`
: Set status line style for a single pane. For how to specify `style`, see the [STYLES](#STYLES) section.

[`session-status-current-style`](#session-status-current-style) `style`
: Set status line style for the currently active session. For how to specify `style`, see the [STYLES](#STYLES) section.

[`session-status-style`](#session-status-style) `style`
: Set status line style for a single session. For how to specify `style`, see the [STYLES](#STYLES) section.

[`tiled-layout-max-columns`](#tiled-layout-max-columns) `number`
: Set the maximum number of columns in the `tiled` layout. A value of 0 (the default) means no limit. When a limit is set, panes are arranged to not exceed this number of columns, with additional panes stacked in extra rows.

[`window-status-activity-style`](#window-status-activity-style) `style`
: Set status line style for windows with an activity alert. For how to specify `style`, see the [STYLES](#STYLES) section.

[`window-status-bell-style`](#window-status-bell-style) `style`
: Set status line style for windows with a bell alert. For how to specify `style`, see the [STYLES](#STYLES) section.

[`window-status-current-format`](#window-status-current-format) `string`
: Like `window-status-format`, but is the format used when the window is the current window.

[`window-status-current-style`](#window-status-current-style) `style`
: Set status line style for the currently active window. For how to specify `style`, see the [STYLES](#STYLES) section.

[`window-status-format`](#window-status-format) `string`
: Set the format in which the window is displayed in the status line window list. See the [FORMATS](#FORMATS) and [STYLES](#STYLES) sections.

[`window-status-last-style`](#window-status-last-style) `style`
: Set status line style for the last active window. For how to specify `style`, see the [STYLES](#STYLES) section.

[`window-status-separator`](#window-status-separator) `string`
: Sets the separator drawn between windows in the status line. The default is a single space character.

[`window-status-style`](#window-status-style) `style`
: Set status line style for a single window. For how to specify `style`, see the [STYLES](#STYLES) section.

[`wrap-search`](#wrap-search) [`on` \| `off`]
: If this option is set, searches will wrap around the end of the pane contents. The default is on.

Available pane options are:

[`allow-passthrough`](#allow-passthrough) [`on` \| `off` \| `all`]
: Allow programs in the pane to bypass `tmux` using a terminal escape sequence (\\ePtmux;\...\\e\\\\). If set to `on`, passthrough sequences will be allowed only if the pane is visible. If set to `all`, they will be allowed even if the pane is invisible.

[`allow-rename`](#allow-rename) [`on` \| `off`]
: Allow programs in the pane to change the window name using a terminal escape sequence (\\ek\...\\e\\\\).

[`allow-set-title`](#allow-set-title) [`on` \| `off`]
: Allow programs in the pane to change the title using the terminal escape sequences (\\e]2;\...\\e\\\\ or \\e]0;\...\\e\\\\).

[`alternate-screen`](#alternate-screen) [`on` \| `off`]
: This option configures whether programs running inside the pane may use the terminal alternate screen feature, which allows the [*smcup*](#smcup) and [*rmcup*](#rmcup) [terminfo(5)](/terminfo.5) capabilities. The alternate screen feature preserves the contents of the window when an interactive application starts and restores it on exit, so that any output visible before the application starts reappears unchanged after it exits.

[`cursor-colour`](#cursor-colour) `colour`
: Set the colour of the cursor.

[`cursor-style`](#cursor-style) `style`
: Set the style of the cursor. Available styles are: `default`, `blinking-block`, `block`, `blinking-underline`, `underline`, `blinking-bar`, `bar`.

[`pane-colours[]`](#pane-colours__) `colour`
: The default colour palette. Each entry in the array defines the colour `tmux` uses when the colour with that index is requested. The index may be from zero to 255.

[`remain-on-exit`](#remain-on-exit) [`on` \| `off` \| `failed`]

[`remain-on-exit-format`](#remain-on-exit-format) `string`
: Set the text shown at the bottom of exited panes when `remain-on-exit` is enabled.

[`scroll-on-clear`](#scroll-on-clear) [`on` \| `off`]
: When the entire screen is cleared and this option is on, scroll the contents of the screen into history before clearing it.

[`synchronize-panes`](#synchronize-panes) [`on` \| `off`]
: Duplicate input to all other panes in the same window where this option is also on (only for panes that are not in any mode).

[`window-active-style`](#window-active-style) `style`
: Set the pane style when it is the active pane. For how to specify `style`, see the [STYLES](#STYLES) section.

[`window-style`](#window-style) `style`
: Set the pane style. For how to specify `style`, see the [STYLES](#STYLES) section.

## HOOKS

 set-hook -g pane-mode-changed[42] 'set -g status-left-style bg=red'
 set-option -g pane-mode-changed[42] 'set -g status-left-style bg=red'

Setting a hook without specifying an array index clears the hook and sets the first member of the array.

 set-hook -g after-split-window "selectl even-vertical"

All the notifications listed in the [CONTROL MODE](#CONTROL_MODE) section are hooks (without any arguments), except `%exit`. The following additional hooks are available:

alert-activity
: Run when a window has activity. See `monitor-activity`.

alert-bell
: Run when a window has received a bell. See `monitor-bell`.

alert-silence
: Run when a window has been silent. See `monitor-silence`.

client-active
: Run when a client becomes the latest active client of its session.

client-attached
: Run when a client is attached.

client-detached
: Run when a client is detached

client-focus-in
: Run when focus enters a client

client-focus-out
: Run when focus exits a client

client-resized
: Run when a client is resized.

client-session-changed
: Run when a client's attached session is changed.

client-light-theme
: Run when a client switches to a light theme.

client-dark-theme
: Run when a client switches to a dark theme.

pane-died
: Run when the program running in a pane exits, but `remain-on-exit` is on so the pane has not closed.

pane-exited
: Run when the program running in a pane exits.

pane-focus-in
: Run when the focus enters a pane, if the `focus-events` option is on.

pane-focus-out
: Run when the focus exits a pane, if the `focus-events` option is on.

pane-set-clipboard
: Run when the terminal clipboard is set using the [xterm(1)](/xterm.1) escape sequence.

session-created
: Run when a new session created.

session-closed
: Run when a session closed.

session-renamed
: Run when a session is renamed.

window-layout-changed
: Run when a window layout is changed.

window-linked
: Run when a window is linked into a session.

window-renamed
: Run when a window is renamed.

window-resized
: Run when a window is resized. This may be after the `client-resized` hook is run.

window-unlinked
: Run when a window is unlinked from a session.

 With `-R`, run `hook-name` immediately.

[`show-hooks`](#show-hooks) [`-gpw`] [`-t` `target-pane`] [`hook`]
: Shows hooks. The flags are the same as for `show-options`.

## MOUSE SUPPORT

If the `mouse` option is on (the default is off), `tmux` allows mouse events to be bound as keys. The name of each key is made up of a mouse event (such as '`MouseUp1`') and a location suffix, one of the following:

 [`Pane`](#Pane) the contents of a pane
 [`Border`](#Border) a pane border
 [`Status`](#Status) the status line window list
 [`StatusLeft`](#StatusLeft) the left part of the status line
 [`StatusRight`](#StatusRight) the right part of the status line
 [`StatusDefault`](#StatusDefault) any other part of the status line
 [`ScrollbarSlider`](#ScrollbarSlider) the scrollbar slider
 [`ScrollbarUp`](#ScrollbarUp) above the scrollbar slider
 [`ScrollbarDown`](#ScrollbarDown) below the scrollbar slider

The following mouse events are available:

 [`WheelUp`](#WheelUp) WheelDown 
 [`MouseDown1`](#MouseDown1) MouseUp1 MouseDrag1 MouseDragEnd1
 [`MouseDown2`](#MouseDown2) MouseUp2 MouseDrag2 MouseDragEnd2
 [`MouseDown3`](#MouseDown3) MouseUp3 MouseDrag3 MouseDragEnd3
 [`SecondClick1`](#SecondClick1) SecondClick2 SecondClick3 
 [`DoubleClick1`](#DoubleClick1) DoubleClick2 DoubleClick3 
 [`TripleClick1`](#TripleClick1) TripleClick2 TripleClick3 

The '`SecondClick`' events are fired for the second click of a double click, even if there may be a third click which will fire '`TripleClick`' instead of '`DoubleClick`'.

Each should be suffixed with a location, for example '`MouseDown1Status`'.

The `send-keys` `-M` flag may be used to forward a mouse event to a pane.

The default key bindings allow the mouse to be used to select and resize panes, to copy text and to change window using the status line. These take effect if the `mouse` option is turned on.

## FORMATS

Conditionals are available by prefixing with '`?`'. For each pair of two arguments, if the variable in the first of the pair exists and is not zero, the second of the pair is chosen, otherwise it continues. If no condition from paired arguments matches, the default value is chosen. If there's an unpaired final argument, that is the default. If not, the default is the empty string. For example '`#`' will include the string '`attached`' if the session is attached and the string '`not attached`' if it is unattached, or '`#`' will include '`yes`' if `automatic-rename` is enabled, or '`no`' if not. '`#,# - }`' will include the window name with a dash separator if there is a window name, or the empty string if the window name is empty. '`#`' will include format1 for a session format, format2 for a window format, or format3 for neither a session nor a window format. Conditionals can be nested arbitrarily. Inside a conditional, '`,`' and '`}`' must be escaped as '`#,`' and '`#}`', unless they are part of a '`#`' replacement. For example:

 ##W

String comparisons may be expressed by prefixing two comma-separated alternatives by '`==`', '`!=`', '`<`', '`>`', '`<=`' or '`>=`' and a colon. For example '`#,myhost}`' will be replaced by '`1`' if running on '`myhost`', otherwise by '`0`'. '`||`' and '`&&`' evaluate to true if any or all of the comma-separated alternatives are true, for example '`#,#}`'. '`!`' evaluates to true if the value is false and vice versa, for example '`#}`'. '`!!`' converts a value to a canonical boolean form, 1 for true and 0 for false, for example '`#`' evaluates to 1.

An '`m`' specifies a [glob(7)](/glob.7) pattern or regular expression comparison. The first argument is the pattern and the second the string to compare. An optional argument specifies flags: '`r`' means the pattern is a regular expression instead of the default [glob(7)](/glob.7) pattern, and '`i`' means to ignore case. For example: '`#}`' or '`#`'. A '`C`' performs a search for a [glob(7)](/glob.7) pattern or regular expression in the pane content and evaluates to zero if not found, or a line number if found. Like '`m`', an '`r`' flag means search for a regular expression and '`i`' ignores case. For example: '`#`'

Numeric operators may be performed by prefixing two comma-separated alternatives with an '`e`' and an operator. An optional '`f`' flag may be given after the operator to use floating point numbers, otherwise integers are used. This may be followed by a number giving the number of decimal places to use for the result. The available operators are: addition '`+`', subtraction '`-`', multiplication '`*`', division '`/`', modulus '`m`' or '`%`' (note that '`%`' must be escaped as '`%%`' in formats which are also expanded by [strftime(3)](/strftime.3)) and numeric comparison operators '`==`', '`!=`', '`<`', '`<=`', '`>`' and '`>=`'. For example, '`#`' multiplies 5.5 by 3 for a result with four decimal places and '`#`' returns the modulus of 7 and 3. '`a`' replaces a numeric argument by its ASCII equivalent, so '`#`' results in '`b`'. '`c`' replaces a `tmux` colour by its six-digit hexadecimal RGB value.

A limit may be placed on the length of the resultant string by prefixing it by an '`=`', a number and a colon. Positive numbers count from the start of the string and negative from the end, so '`#`' will include at most the first five characters of the pane title, or '`#`' the last five characters. A suffix or prefix may be given as a second argument - if provided then it is appended or prepended to the string if the length has been trimmed, for example '`#`' will append '`...`' if the pane title is more than five characters. Similarly, '`p`' pads the string to a given width, for example '`#`' will result in a width of at least 10 characters. A positive width pads on the left, a negative on the right. '`n`' expands to the length of the variable and '`w`' to its width when displayed, for example '`#`'. '`R`' repeats the first argument by a number of times given by the second argument, so '`#`' will result in '`aaa`'.

Prefixing a time variable with '`t:`' will convert it to a string, so if '`#`' gives '`1445765102`', '`#`' gives '`Sun Oct 25 09:25:02 2015`'. Adding '`p (`' '`` `t/p` ``') will use shorter but less accurate time format for times in the past. A custom format may be given using an '`f`' suffix (note that '`%`' must be escaped as '`%%`' if the format is separately being passed through [strftime(3)](/strftime.3), for example in the `status-left` option): '`#`', see [strftime(3)](/strftime.3).

The '`b:`' and '`d:`' prefixes are [basename(3)](/basename.3) and [dirname(3)](/dirname.3) of the variable respectively. '`q:`' will escape [sh(1)](/sh.1) special characters or with a '`h`' suffix, escape hash characters (so '`#`' becomes '`##`'). '`E:`' will expand the format twice, for example '`#`' is the result of expanding the content of the `status-left` option rather than the option itself. '`T:`' is like '`E:`' but also expands [strftime(3)](/strftime.3) specifiers. '`S:`', '`W:`', '`P:`' or '`L:`' will loop over each session, window, pane or client and insert the format once for each. '`L:`', '`S:`' and '`W:`' can take an optional sort argument '`/i`', '`/n`', '`/t`' to sort by index, name, or last activity time; additionally '`/r`' to sort in reverse order. '`/r`' can also be used with '`P:`' to reverse the sort order by pane index. For example, '`S/nr:`' to sort sessions by name in reverse order. For each, two comma-separated formats may be given: the second is used for the current window, active pane, or active session. For example, to get a list of windows formatted like the status line:

 # ,# }

'`N:`' checks if a window (without any suffix or with the '`w`' suffix) or a session (with the '`s`' suffix) name exists, for example '`` `N/w:foo` ``' is replaced with 1 if a window named '`foo`' exists.

A prefix of the form '`s/foo/bar/:`' will substitute '`foo`' with '`bar`' throughout. The first argument may be an extended regular expression and a final argument may be '`i`' to ignore case, for example '`s/a(.)/\1x/i:`' would change '`abABab`' into '`bxBxbx`'. A different delimiter character may also be used, to avoid collisions with literal slashes in the pattern. For example, '`s|foo/|bar/|:`' will substitute '`foo/`' with '`bar/`' throughout.

Multiple modifiers may be separated with a semicolon (;) as in '`#`', which limits the resulting [strftime(3)](/strftime.3) -expanded string to at most 10 characters.

An '`l`' specifies that a string should be interpreted literally and not expanded. For example '`#}`' will be replaced by '`#`'.

The following variables are available, where appropriate:

 [**Variable name**](#Variable) [**Alias**](#Alias) [**Replaced with**](#Replaced)
 [`active_window_index`](#active_window_index) Index of active window in session
 [`alternate_on`](#alternate_on) 1 if pane is in alternate screen
 [`alternate_saved_x`](#alternate_saved_x) Saved cursor X in alternate screen
 [`alternate_saved_y`](#alternate_saved_y) Saved cursor Y in alternate screen
 [`buffer_created`](#buffer_created) Time buffer created
 [`buffer_full`](#buffer_full) Full buffer content
 [`buffer_name`](#buffer_name) Name of buffer
 [`buffer_sample`](#buffer_sample) Sample of start of buffer
 [`buffer_size`](#buffer_size) Size of the specified buffer in bytes
 [`client_activity`](#client_activity) Time client last had activity
 [`client_cell_height`](#client_cell_height) Height of each client cell in pixels
 [`client_cell_width`](#client_cell_width) Width of each client cell in pixels
 [`client_control_mode`](#client_control_mode) 1 if client is in control mode
 [`client_created`](#client_created) Time client created
 [`client_discarded`](#client_discarded) Bytes discarded when client behind
 [`client_flags`](#client_flags) List of client flags
 [`client_height`](#client_height) Height of client
 [`client_key_table`](#client_key_table) Current key table
 [`client_last_session`](#client_last_session) Name of the client's last session
 [`client_name`](#client_name) Name of client
 [`client_pid`](#client_pid) PID of client process
 [`client_prefix`](#client_prefix) 1 if prefix key has been pressed
 [`client_readonly`](#client_readonly) 1 if client is read-only
 [`client_session`](#client_session) Name of the client's session
 [`client_termfeatures`](#client_termfeatures) Terminal features of client, if any
 [`client_termname`](#client_termname) Terminal name of client
 [`client_termtype`](#client_termtype) Terminal type of client, if available
 [`client_tty`](#client_tty) Pseudo terminal of client
 [`client_uid`](#client_uid) UID of client process
 [`client_user`](#client_user) User of client process
 [`client_utf8`](#client_utf8) 1 if client supports UTF-8
 [`client_width`](#client_width) Width of client
 [`client_written`](#client_written) Bytes written to client
 [`config_files`](#config_files) List of configuration files loaded
 [`cursor_blinking`](#cursor_blinking) 1 if the cursor is blinking
 [`copy_cursor_hyperlink`](#copy_cursor_hyperlink) Hyperlink under cursor in copy mode
 [`copy_cursor_line`](#copy_cursor_line) Line the cursor is on in copy mode
 [`copy_cursor_word`](#copy_cursor_word) Word under cursor in copy mode
 [`copy_cursor_x`](#copy_cursor_x) Cursor X position in copy mode
 [`copy_cursor_y`](#copy_cursor_y) Cursor Y position in copy mode
 [`current_file`](#current_file) Current configuration file
 [`cursor_character`](#cursor_character) Character at cursor in pane
 [`cursor_colour`](#cursor_colour) Cursor colour in pane
 [`cursor_flag`](#cursor_flag) Pane cursor flag
 [`cursor_shape`](#cursor_shape) Cursor shape in pane
 [`cursor_very_visible`](#cursor_very_visible) 1 if the cursor is in very visible mode
 [`cursor_x`](#cursor_x) Cursor X position in pane
 [`cursor_y`](#cursor_y) Cursor Y position in pane
 [`history_bytes`](#history_bytes) Number of bytes in window history
 [`history_limit`](#history_limit) Maximum window history lines
 [`history_size`](#history_size) Size of history in lines
 [`hook`](#hook) Name of running hook, if any
 [`hook_client`](#hook_client) Name of client where hook was run, if any
 [`hook_pane`](#hook_pane) ID of pane where hook was run, if any
 [`hook_session`](#hook_session) ID of session where hook was run, if any
 [`hook_session_name`](#hook_session_name) Name of session where hook was run, if any
 [`hook_window`](#hook_window) ID of window where hook was run, if any
 [`hook_window_name`](#hook_window_name) Name of window where hook was run, if any
 [`host`](#host) #H Hostname of local host
 [`host_short`](#host_short) #h Hostname of local host (no domain name)
 [`insert_flag`](#insert_flag) Pane insert flag
 [`keypad_cursor_flag`](#keypad_cursor_flag) Pane keypad cursor flag
 [`keypad_flag`](#keypad_flag) Pane keypad flag
 [`last_window_index`](#last_window_index) Index of last window in session
 [`line`](#line) Line number in the list
 [`loop_last_flag`](#loop_last_flag) 1 if last window, pane, session, client in the W:, P:, S:, or L: loop
 [`mouse_all_flag`](#mouse_all_flag) Pane mouse all flag
 [`mouse_any_flag`](#mouse_any_flag) Pane mouse any flag
 [`mouse_button_flag`](#mouse_button_flag) Pane mouse button flag
 [`mouse_hyperlink`](#mouse_hyperlink) Hyperlink under mouse, if any
 [`mouse_line`](#mouse_line) Line under mouse, if any
 [`mouse_sgr_flag`](#mouse_sgr_flag) Pane mouse SGR flag
 [`mouse_standard_flag`](#mouse_standard_flag) Pane mouse standard flag
 [`mouse_status_line`](#mouse_status_line) Status line on which mouse event took place
 [`mouse_status_range`](#mouse_status_range) Range type or argument of mouse event on status line
 [`mouse_utf8_flag`](#mouse_utf8_flag) Pane mouse UTF-8 flag
 [`mouse_word`](#mouse_word) Word under mouse, if any
 [`mouse_x`](#mouse_x) Mouse X position, if any
 [`mouse_y`](#mouse_y) Mouse Y position, if any
 [`next_session_id`](#next_session_id) Unique session ID for next new session
 [`origin_flag`](#origin_flag) Pane origin flag
 [`pane_active`](#pane_active) 1 if active pane
 [`pane_at_bottom`](#pane_at_bottom) 1 if pane is at the bottom of window
 [`pane_at_left`](#pane_at_left) 1 if pane is at the left of window
 [`pane_at_right`](#pane_at_right) 1 if pane is at the right of window
 [`pane_at_top`](#pane_at_top) 1 if pane is at the top of window
 [`pane_bg`](#pane_bg) Pane background colour
 [`pane_bottom`](#pane_bottom) Bottom of pane
 [`pane_current_path`](#pane_current_path) Current path if available
 [`pane_dead`](#pane_dead) 1 if pane is dead
 [`pane_dead_signal`](#pane_dead_signal) Exit signal of process in dead pane
 [`pane_dead_status`](#pane_dead_status) Exit status of process in dead pane
 [`pane_dead_time`](#pane_dead_time) Exit time of process in dead pane
 [`pane_fg`](#pane_fg) Pane foreground colour
 [`pane_format`](#pane_format) 1 if format is for a pane
 [`pane_height`](#pane_height) Height of pane
 [`pane_id`](#pane_id) #D Unique pane ID
 [`pane_in_mode`](#pane_in_mode) Number of modes pane is in
 [`pane_index`](#pane_index) #P Index of pane
 [`pane_input_off`](#pane_input_off) 1 if input to pane is disabled
 [`pane_key_mode`](#pane_key_mode) Extended key reporting mode in this pane
 [`pane_last`](#pane_last) 1 if last pane
 [`pane_left`](#pane_left) Left of pane
 [`pane_marked`](#pane_marked) 1 if this is the marked pane
 [`pane_marked_set`](#pane_marked_set) 1 if a marked pane is set
 [`pane_mode`](#pane_mode) Name of pane mode, if any
 [`pane_path`](#pane_path) Path of pane (can be set by application)
 [`pane_pid`](#pane_pid) PID of first process in pane
 [`pane_pipe`](#pane_pipe) 1 if pane is being piped
 [`pane_right`](#pane_right) Right of pane
 [`pane_search_string`](#pane_search_string) Last search string in copy mode
 [`pane_start_path`](#pane_start_path) Path pane started with
 [`pane_synchronized`](#pane_synchronized) 1 if pane is synchronized
 [`pane_tabs`](#pane_tabs) Pane tab positions
 [`pane_title`](#pane_title) #T Title of pane (can be set by application)
 [`pane_top`](#pane_top) Top of pane
 [`pane_tty`](#pane_tty) Pseudo terminal of pane
 [`pane_unseen_changes`](#pane_unseen_changes) 1 if there were changes in pane while in mode
 [`pane_width`](#pane_width) Width of pane
 [`pid`](#pid) Server PID
 [`rectangle_toggle`](#rectangle_toggle) 1 if rectangle selection is activated
 [`scroll_position`](#scroll_position) Scroll position in copy mode
 [`scroll_region_lower`](#scroll_region_lower) Bottom of scroll region in pane
 [`scroll_region_upper`](#scroll_region_upper) Top of scroll region in pane
 [`search_count`](#search_count) Count of search results
 [`search_count_partial`](#search_count_partial) 1 if search count is partial count
 [`search_match`](#search_match) Search match if any
 [`search_present`](#search_present) 1 if search started in copy mode
 [`selection_active`](#selection_active) 1 if selection started and changes with the cursor in copy mode
 [`selection_end_x`](#selection_end_x) X position of the end of the selection
 [`selection_end_y`](#selection_end_y) Y position of the end of the selection
 [`selection_mode`](#selection_mode) Selection mode
 [`selection_present`](#selection_present) 1 if selection started in copy mode
 [`selection_start_x`](#selection_start_x) X position of the start of the selection
 [`selection_start_y`](#selection_start_y) Y position of the start of the selection
 [`server_sessions`](#server_sessions) Number of sessions
 [`session_active`](#session_active) 1 if session active
 [`session_activity`](#session_activity) Time of session last activity
 [`session_activity_flag`](#session_activity_flag) 1 if any window in session has activity
 [`session_alerts`](#session_alerts) List of window indexes with alerts
 [`session_attached`](#session_attached) Number of clients session is attached to
 [`session_attached_list`](#session_attached_list) List of clients session is attached to
 [`session_bell_flag`](#session_bell_flag) 1 if any window in session has bell
 [`session_created`](#session_created) Time session created
 [`session_format`](#session_format) 1 if format is for a session
 [`session_group`](#session_group) Name of session group
 [`session_group_attached`](#session_group_attached) Number of clients sessions in group are attached to
 [`session_group_attached_list`](#session_group_attached_list) List of clients sessions in group are attached to
 [`session_group_list`](#session_group_list) List of sessions in group
 [`session_group_size`](#session_group_size) Size of session group
 [`session_grouped`](#session_grouped) 1 if session in a group
 [`session_id`](#session_id) Unique session ID
 [`session_last_attached`](#session_last_attached) Time session last attached
 [`session_marked`](#session_marked) 1 if this session contains the marked pane
 [`session_name`](#session_name) #S Name of session
 [`session_path`](#session_path) Working directory of session
 [`session_silence_flag`](#session_silence_flag) 1 if any window in session has silence alert
 [`session_stack`](#session_stack) Window indexes in most recent order
 [`session_windows`](#session_windows) Number of windows in session
 [`socket_path`](#socket_path) Server socket path
 [`sixel_support`](#sixel_support) 1 if server has support for SIXEL
 [`start_time`](#start_time) Server start time
 [`synchronized_output_flag`](#synchronized_output_flag) 1 if pane has synchronized output enabled
 [`uid`](#uid) Server UID
 [`user`](#user) Server user
 [`version`](#version) Server version
 [`window_active`](#window_active) 1 if window active
 [`window_active_clients`](#window_active_clients) Number of clients viewing this window
 [`window_active_clients_list`](#window_active_clients_list) List of clients viewing this window
 [`window_active_sessions`](#window_active_sessions) Number of sessions on which this window is active
 [`window_active_sessions_list`](#window_active_sessions_list) List of sessions on which this window is active
 [`window_activity`](#window_activity) Time of window last activity
 [`window_activity_flag`](#window_activity_flag) 1 if window has activity
 [`window_bell_flag`](#window_bell_flag) 1 if window has bell
 [`window_bigger`](#window_bigger) 1 if window is larger than client
 [`window_cell_height`](#window_cell_height) Height of each cell in pixels
 [`window_cell_width`](#window_cell_width) Width of each cell in pixels
 [`window_end_flag`](#window_end_flag) 1 if window has the highest index
 [`window_flags`](#window_flags) #F Window flags with \# escaped as \##
 [`window_format`](#window_format) 1 if format is for a window
 [`window_height`](#window_height) Height of window
 [`window_id`](#window_id) Unique window ID
 [`window_index`](#window_index) #I Index of window
 [`window_last_flag`](#window_last_flag) 1 if window is the last used
 [`window_layout`](#window_layout) Window layout description, ignoring zoomed window panes
 [`window_linked`](#window_linked) 1 if window is linked across sessions
 [`window_linked_sessions`](#window_linked_sessions) Number of sessions this window is linked to
 [`window_linked_sessions_list`](#window_linked_sessions_list) List of sessions this window is linked to
 [`window_marked_flag`](#window_marked_flag) 1 if window contains the marked pane
 [`window_name`](#window_name) #W Name of window
 [`window_offset_x`](#window_offset_x) X offset into window if larger than client
 [`window_offset_y`](#window_offset_y) Y offset into window if larger than client
 [`window_panes`](#window_panes) Number of panes in window
 [`window_raw_flags`](#window_raw_flags) Window flags with nothing escaped
 [`window_silence_flag`](#window_silence_flag) 1 if window has silence alert
 [`window_stack_index`](#window_stack_index) Index in session most recent stack
 [`window_start_flag`](#window_start_flag) 1 if window has the lowest index
 [`window_visible_layout`](#window_visible_layout) Window layout description, respecting zoomed window panes
 [`window_width`](#window_width) Width of window
 [`window_zoomed_flag`](#window_zoomed_flag) 1 if window is zoomed
 [`wrap_flag`](#wrap_flag) Pane wrap flag

## STYLES

`tmux` offers various options to specify the colour and attributes of aspects of the interface, for example `status-style` for the status line. In addition, embedded styles may be specified in format options, such as `status-left`, by enclosing them in '`#[`' and '`]`'.

A style may be the single term '`default`' to specify the default style (which may come from an option, for example `status-style` in the status line) or a space or comma separated list of the following:

[`fg=colour`](#fg=colour)
: Set the foreground colour. The colour is one of: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`; if supported the bright variants `brightblack`, `brightred`, \...; `colour0` to `colour255` from the 256-colour set; `default` for the default colour; `terminal` for the terminal default colour; or a hexadecimal RGB string such as '`#ffffff`'.

[`bg=colour`](#bg=colour)
: Set the background colour.

[`us=colour`](#us=colour)
: Set the underscore colour.

[`none`](#none)
: Set no attributes (turn off any active attributes).

[`acs`](#acs), `bright` (or `bold`), `dim`, `underscore`, `blink`, `reverse`, `hidden`, `italics`, `overline`, `strikethrough`, `double-underscore`, `curly-underscore`, `dotted-underscore`, `dashed-underscore`
: Set an attribute. Any of the attributes may be prefixed with '`no`' to unset. `acs` is the terminal alternate character set.

[`align=left`](#align=left) (or `noalign`), `align=centre`, `align=right`
: Align text to the left, centre or right of the available space if appropriate.

[`fill=colour`](#fill=colour)
: Fill the available space with a background colour if appropriate.

[`list=on`](#list=on), `list=focus`, `list=left-marker`, `list=right-marker`, `nolist`
: Mark the position of the various window list components in the `status-format` option: `list=on` marks the start of the list; `list=focus` is the part of the list that should be kept in focus if the entire list won't fit in the available space (typically the current window); `list=left-marker` and `list=right-marker` mark the text to be used to mark that text has been trimmed from the left or right of the list if there is not enough space.

[`noattr`](#noattr)
: Do not copy attributes from the default style.

[`push-default`](#push-default), `pop-default`
: Store the current colours and attributes as the default or reset to the previous default. A `push-default` affects any subsequent use of the `default` term until a `pop-default`. Only one default may be pushed (each `push-default` replaces the previous saved default).

[`range=left`](#range=left), `range=right`, `range=session|X`, `range=window|X`, `range=pane|X`, `range=user|X`, `norange`

: Mark a range for mouse events in the `status-format` option. When a mouse event occurs in the `range=left` or `range=right` range, the '`StatusLeft`' and '`StatusRight`' key bindings are triggered.

 `range=session|X`, `range=window|X` and `range=pane|X` are ranges for a session, window or pane. These trigger the '`Status`' mouse key with the target session, window or pane given by the '`X`' argument. '`X`' is a session ID, window index in the current session or a pane ID. For these, the `mouse_status_range` format variable will be set to '`session`', '`window`' or '`pane`'.

 `range=user|X` is a user-defined range; it triggers the '`Status`' mouse key. The argument '`X`' will be available in the `mouse_status_range` format variable. '`X`' must be at most 15 bytes in length.

[`set-default`](#set-default)
: Set the current colours and attributes as the default, overwriting any previous default. The previous default cannot be restored.

Examples are:

 fg=yellow bold underscore blink
 bg=black,fg=default,noreverse

## NAMES AND TITLES

`tmux` distinguishes between names and titles. Windows and sessions have names, which may be used to specify them in targets and are displayed in the status line and various lists: the name is the `tmux` identifier for a window or session. Only panes have titles. A pane's title is typically set by the program running inside the pane using an escape sequence (like it would set the [xterm(1)](/xterm.1) window title in [X(7)](/X.7)). Windows themselves do not have titles - a window's title is the title of its active pane. `tmux` itself may set the title of the terminal in which the client is running, see the `set-titles` option.

2. An escape sequence (if the `allow-rename` option is turned on):

 ::: 
 $ printf '\033kWINDOW_NAME\033\'
 :::

When a pane is first created, its title is the hostname. A pane's title can be set via the title setting escape sequence, for example:

 $ printf '\033]2;My Title\033\'

## GLOBAL AND SESSION ENVIRONMENT

When the server is started, `tmux` copies the environment into the [*global environment*](#global); in addition, each session has a *session environment*. When a window is created, the session and global environments are merged. If a variable exists in both, the value from the session environment is used. The result is the initial environment passed to the new process.

Variables in both session and global environments may be marked as hidden. Hidden variables are not passed into the environment of new processes and instead can only be used by tmux itself (for example in formats, see the [FORMATS](#FORMATS) section).

[`set-environment`](#set-environment) [`-Fhgru`] [`-t` `target-session`] `variable` [`value`]

: ::: 
 (alias: `setenv`)
 :::

 Set or unset an environment variable. If `-g` is used, the change is made in the global environment; otherwise, it is applied to the session environment for `target-session`. If `-F` is present, then `value` is expanded as a format. The `-u` flag unsets a variable. `-r` indicates the variable is to be removed from the environment before starting a new process. `-h` marks the variable as hidden.

[`show-environment`](#show-environment) [`-hgs`] [`-t` `target-session`] [`variable`]

: ::: 
 (alias: `showenv`)
 :::

## STATUS LINE

`tmux` includes an optional status line which is displayed in the bottom line of each terminal.

By default, the status line is enabled and one line in height (it may be disabled or made multiple lines with the `status` session option) and contains, from left-to-right: the name of the current session in square brackets; the window list; the title of the active pane in double quotes; and the time and date.

 [**Symbol**](#Symbol) [**Meaning**](#Meaning~3)
 [`*`](#*) Denotes the current window.
 `-` Marks the last window (previously selected).
 [`#`](#_~3) Window activity is monitored and activity has been detected.
 [`!`](#!) Window bells are monitored and a bell has occurred in the window.
 `~` The window has been silent for the monitor-silence interval.
 [`M`](#M~2) The window contains the marked pane.
 [`Z`](#Z~2) The window's active pane is zoomed.

The \# symbol relates to the `monitor-activity` window option. The window name is printed in inverted colours if an alert (bell, activity or silence) is present.

The colour and attributes of the status line may be configured, the entire status line using the `status-style` session option and individual windows using the `window-status-style` window option.

The status line is automatically refreshed at interval if it has changed, the interval may be controlled with the `status-interval` session option.

[`clear-prompt-history`](#clear-prompt-history) [`-T` `prompt-type`]

: ::: 
 (alias: `clearphist`)
 :::

 If `-I` is present, `inputs` is a comma-separated list of the initial text for each prompt. If `-p` is given, `prompts` is a comma-separated list of prompts which are displayed in order; otherwise a single prompt is displayed, constructed from `template` if it is present, or '`:`' if not. `-l` disables splitting of `inputs` and `prompts` at commas and treats them literally.

 [**Function**](#Function~4) [**vi**](#vi) [**emacs**](#emacs)
 [`Delete from cursor to start of word`](#Delete) C-w
 [`Delete from cursor to end`](#Delete~3) D C-k
 [`Insert top paste buffer`](#Insert) p C-y
 [`Look for completions`](#Look) Tab Tab
 [`Move cursor left`](#Move) h Left
 [`Move cursor right`](#Move~2) l Right
 [`Move cursor to end`](#Move~3) \$ C-e
 [`Move cursor to next word`](#Move~4) w M-f
 [`Move cursor to previous word`](#Move~5) b M-b
 [`Move cursor to start`](#Move~6) 0 C-a
 [`Transpose characters`](#Transpose) C-t

 With `-b`, the prompt is shown in the background and the invoking client does not exit until it is dismissed.

: ::: 
 (alias: `confirm`)
 :::

: ::: 
 (alias: `menu`)
 :::

 `-b` sets the type of characters used for drawing menu borders. See `popup-border-lines` for possible values for `border-lines`.

 `-H` sets the style for the selected menu item (see [STYLES](#STYLES)).

 `-s` sets the style for the menu and `-S` sets the style for the menu border (see [STYLES](#STYLES)).

 `-T` is a format for the menu title (see [FORMATS](#FORMATS)).

 `-C` sets the menu item selected by default, if the menu is not bound to a mouse key binding.

 `-x` and `-y` give the position of the menu. Both may be a row or column number, or one of the following special values:

 [**Value**](#Value) [**Flag**](#Flag) [**Meaning**](#Meaning~4)
 [`C`](#C~2) Both The centre of the terminal
 [`R`](#R) [`-x`](#x~3) The right side of the terminal
 [`P`](#P) Both The bottom left of the pane
 [`M`](#M~3) Both The mouse position
 [`W`](#W) Both The window position on the status line
 [`S`](#S~3) [`-y`](#y) The line above or below the status line

 Or a format, which is expanded including the following additional variables:

 [**Variable name**](#Variable~2) [**Replaced with**](#Replaced~2)
 [`popup_centre_x`](#popup_centre_x) Centered in the client
 [`popup_centre_y`](#popup_centre_y) Centered in the client
 [`popup_height`](#popup_height) Height of menu or popup
 [`popup_mouse_bottom`](#popup_mouse_bottom) Bottom of at the mouse
 [`popup_mouse_centre_x`](#popup_mouse_centre_x) Horizontal centre at the mouse
 [`popup_mouse_centre_y`](#popup_mouse_centre_y) Vertical centre at the mouse
 [`popup_mouse_top`](#popup_mouse_top) Top at the mouse
 [`popup_mouse_x`](#popup_mouse_x) Mouse X position
 [`popup_mouse_y`](#popup_mouse_y) Mouse Y position
 [`popup_pane_bottom`](#popup_pane_bottom) Bottom of the pane
 [`popup_pane_left`](#popup_pane_left) Left of the pane
 [`popup_pane_right`](#popup_pane_right) Right of the pane
 [`popup_pane_top`](#popup_pane_top) Top of the pane
 [`popup_status_line_y`](#popup_status_line_y) Above or below the status line
 [`popup_width`](#popup_width) Width of menu or popup
 [`popup_window_status_line_x`](#popup_window_status_line_x) At the window position in status line
 [`popup_window_status_line_y`](#popup_window_status_line_y) At the status line showing the window

 Each menu consists of items followed by a key shortcut shown in brackets. If the menu is too large to fit on the terminal, it is not displayed. Pressing the key shortcut chooses the corresponding item. If the mouse is enabled and the menu is opened from a mouse key binding, releasing the mouse button with an item selected chooses that item and releasing the mouse button without an item selected closes the menu. `-O` changes this behaviour so that the menu does not close when the mouse button is released without an item selected the menu is not closed and a mouse button must be clicked to choose an item.

 `-M` tells `tmux` the menu should handle mouse events; by default only menus opened from mouse key bindings do so.

 The following keys are available in menus:

 [**Key**](#Key~4) [**Function**](#Function~5)
 [`Enter`](#Enter~4) Choose selected item
 [`Up`](#Up~4) Select previous item
 [`Down`](#Down~4) Select next item
 [`q`](#q~4) Exit menu

[`display-message`](#display-message) [`-aCIlNpv`] [`-c` `target-client`] [`-d` `delay`] [`-t` `target-pane`] [`message`]

: ::: 
 (alias: `display`)
 :::

 Display a message. If `-p` is given, the output is printed to stdout, otherwise it is displayed in the `target-client` status line for up to `delay` milliseconds. If `delay` is not given, the `display-time` option is used; a delay of zero waits for a key press. '`N`' ignores key presses and closes only after the delay expires. If `-C` is given, the pane will continue to be updated while the message is displayed. If `-l` is given, `message` is printed unchanged. Otherwise, the format of `message` is described in the [FORMATS](#FORMATS) section; information is taken from `target-pane` if `-t` is given, otherwise the active pane.

 `-v` prints verbose logging as the format is parsed and `-a` lists the format variables and their values.

 `-I` forwards any input read from stdin to the empty pane given by `target-pane`.

: ::: 
 (alias: `popup`)
 :::

 `-B` does not surround the popup by a border.

 `-b` sets the type of characters used for drawing popup borders. When `-B` is specified, the `-b` option is ignored. See `popup-border-lines` for possible values for `border-lines`.

 `-s` sets the style for the popup and `-S` sets the style for the popup border (see [STYLES](#STYLES)).

 `-e` takes the form '`VARIABLE=value`' and sets an environment variable for the popup; it may be specified multiple times.

 `-T` is a format for the popup title (see [FORMATS](#FORMATS)).

 The `-C` flag closes any popup on the client.

 `-N` disables any previously specified -E, -EE, or -k option.

[`show-prompt-history`](#show-prompt-history) [`-T` `prompt-type`]

: ::: 
 (alias: `showphist`)
 :::

## BUFFERS

[`choose-buffer`](#choose-buffer) [`-NryZ`] [`-F` `format`] [`-f` `filter`] [`-K` `key-format`] [`-O` `sort-order`] [`-t` `target-pane`] [`template`]

 [**Key**](#Key~5) [**Function**](#Function~6)
 [`Enter`](#Enter~5) Paste selected buffer
 [`Up`](#Up~5) Select previous buffer
 [`Down`](#Down~5) Select next buffer
 [`C-s`](#C-s~4) Search by name or content
 [`n`](#n~4) Repeat last search forwards
 [`N`](#N~5) Repeat last search backwards
 [`t`](#t~4) Toggle if buffer is tagged
 [`T`](#T~5) Tag no buffers
 [`C-t`](#C-t~4) Tag all buffers
 [`p`](#p) Paste selected buffer
 [`P`](#P~2) Paste tagged buffers
 [`d`](#d~3) Delete selected buffer
 [`D`](#D~4) Delete tagged buffers
 [`e`](#e) Open the buffer in an editor
 [`f`](#f~5) Enter a format to filter items
 [`O`](#O~3) Change sort field
 [`r`](#r~3) Reverse sort order
 [`v`](#v~5) Toggle preview
 [`q`](#q~5) Exit mode

[`clear-history`](#clear-history) [`-H`] [`-t` `target-pane`]

: ::: 
 (alias: `clearhist`)
 :::

 Remove and free the history for the specified pane. `-H` also removes all hyperlinks.

[`delete-buffer`](#delete-buffer) [`-b` `buffer-name`]

: ::: 
 (alias: `deleteb`)
 :::

 Delete the buffer named `buffer-name`, or the most recently added automatically named buffer if not specified.

[`list-buffers`](#list-buffers) [`-F` `format`] [`-f` `filter`]

: ::: 
 (alias: `lsb`)
 :::

 List the global buffers. `-F` specifies the format of each line and `-f` a filter. Only buffers for which the filter is true are shown. See the [FORMATS](#FORMATS) section.

[`load-buffer`](#load-buffer) [`-w`] [`-b` `buffer-name`] [`-t` `target-client`] `path`

: ::: 
 (alias: `loadb`)
 :::

 Load the contents of the specified paste buffer from `path`. If `-w` is given, the buffer is also sent to the clipboard for `target-client` using the [xterm(1)](/xterm.1) escape sequence, if possible. If `path` is '`-`', the contents are read from stdin.

[`paste-buffer`](#paste-buffer) [`-dpr`] [`-b` `buffer-name`] [`-s` `separator`] [`-t` `target-pane`]

: ::: 
 (alias: `pasteb`)
 :::

 Insert the contents of a paste buffer into the specified pane. If not specified, paste into the current one. With `-d`, also delete the paste buffer. When output, any linefeed (LF) characters in the paste buffer are replaced with a separator, by default carriage return (CR). A custom separator may be specified using the `-s` flag. The `-r` flag means to do no replacement (equivalent to a separator of LF). If `-p` is specified, paste bracket control codes are inserted around the buffer if the application has requested bracketed paste mode.

[`save-buffer`](#save-buffer) [`-a`] [`-b` `buffer-name`] `path`

: ::: 
 (alias: `saveb`)
 :::

 Save the contents of the specified paste buffer to `path`. The `-a` option appends to rather than overwriting the file. If `path` is '`-`', the contents are written to stdout.

[`set-buffer`](#set-buffer) [`-aw`] [`-b` `buffer-name`] [`-t` `target-client`] [][`-n` `new-buffer-name`] `data`

: ::: 
 (alias: `setb`)
 :::

 Set the contents of the specified buffer to `data`. If `-w` is given, the buffer is also sent to the clipboard for `target-client` using the [xterm(1)](/xterm.1) escape sequence, if possible. The `-a` option appends to rather than overwriting the buffer. The `-n` option renames the buffer to `new-buffer-name`.

[`show-buffer`](#show-buffer) [`-b` `buffer-name`]

: ::: 
 (alias: `showb`)
 :::

 Display the contents of the specified buffer.

## MISCELLANEOUS

[`clock-mode`](#clock-mode) [`-t` `target-pane`]
: Display a large clock.

: ::: 
 (alias: `if`)
 :::

[`lock-server`](#lock-server)

: ::: 
 (alias: `lock`)
 :::

: ::: 
 (alias: `run`)
 :::

[`wait-for`](#wait-for) [`-L` \| `-S` \| `-U`] `channel`

: ::: 
 (alias: `wait`)
 :::

 When used without options, prevents the client from exiting until woken using `wait-for` `-S` with the same channel. When `-L` is used, the channel is locked and any clients that try to lock the same channel are made to wait until the channel is unlocked with `wait-for` `-U`.

## EXIT MESSAGES

When a `tmux` client detaches, it prints a message. This may be one of:

detached (from session \...)
: The client was detached normally.

detached and SIGHUP
: The client was detached and its parent sent the `SIGHUP` signal (for example with `detach-client` `-P`).

lost tty
: The client's [tty(4)](/tty.4) or [pty(4)](/pty.4) was unexpectedly destroyed.

terminated
: The client was killed with `SIGTERM`.

too far behind
: The client is in control mode and became unable to keep up with the data from `tmux`.

exited
: The server exited when it had no sessions.

server exited
: The server exited when it received `SIGTERM`.

server exited unexpectedly
: The server crashed or otherwise exited without telling the client the reason.

## TERMINFO EXTENSIONS

[*AX*](#AX)
: An existing extension that tells `tmux` the terminal supports default colours.

[*Bidi*](#Bidi)
: Tell `tmux` that the terminal supports the VTE bidirectional text extensions.

[*Cs*](#Cs), [*Cr*](#Cr)

: Set the cursor colour. The first takes a single string argument and is used to set the colour; the second takes no arguments and restores the default cursor colour. If set, a sequence such as this may be used to change the cursor colour from inside `tmux`:

 ::: 
 $ printf '\033]12;red\033\'
 :::

 The colour is an [X(7)](/X.7) colour, see [XParseColor(3)](/XParseColor.3).

[*Cmg, Clmg, Dsmg*](#Cmg,), [*Enmg*](#Enmg)
: Set, clear, disable or enable DECSLRM margins. These are set automatically if the terminal reports it is [*VT420*](#VT420) compatible.

[*Dsbp*](#Dsbp), [*Enbp*](#Enbp)
: Disable and enable bracketed paste. These are set automatically if the *XT* capability is present.

[*Dseks*](#Dseks), [*Eneks*](#Eneks)
: Disable and enable extended keys.

[*Dsfcs*](#Dsfcs), [*Enfcs*](#Enfcs)
: Disable and enable focus reporting. These are set automatically if the *XT* capability is present.

[*Hls*](#Hls)
: Set or clear a hyperlink annotation.

[*Nobr*](#Nobr)
: Tell `tmux` that the terminal does not use bright colors for bold display.

[*Rect*](#Rect)
: Tell `tmux` that the terminal supports rectangle operations.

[*Smol*](#Smol)
: Enable the overline attribute.

[*Smulx*](#Smulx)
: Set a styled underscore. The single parameter is one of: 0 for no underscore, 1 for normal underscore, 2 for double underscore, 3 for curly underscore, 4 for dotted underscore and 5 for dashed underscore.

[*Setulc*](#Setulc), [*Setulc1, ol*](#Setulc1,)
: Set the underscore colour or reset to the default. *Setulc* is for RGB colours and [*Setulc1*](#Setulc1) for ANSI or 256 colours. The *Setulc* argument is (red \* 65536) + (green \* 256) + blue where each is between 0 and 255.

[*Ss*](#Ss), *Se*

: Set or reset the cursor style. If set, a sequence such as this may be used to change the cursor to an underline:

 ::: 
 $ printf '\033[4 q'
 :::

 If *Se* is not set, Ss with argument 0 will be used to reset the cursor style instead.

[*Swd*](#Swd)
: Set the opening sequence for the working directory notification. The sequence is terminated using the standard *fsl* capability.

[*Sxl*](#Sxl)
: Indicates that the terminal supports SIXEL.

[*Sync*](#Sync)
: Start (parameter is 1) or end (parameter is 2) a synchronized update.

[*Tc*](#Tc)

: Indicate that the terminal supports the '`direct colour`' RGB escape sequence (for example, \\e[38;2;255;255;255m).

 If supported, this is used for the initialize colour escape sequence (which may be enabled by adding the '`initc`' and '`ccc`' capabilities to the `tmux` [terminfo(5)](/terminfo.5) entry).

 This is equivalent to the [*RGB*](#RGB) [terminfo(5)](/terminfo.5) capability.

[*Ms*](#Ms)

[*XT*](#XT)
: This is an existing extension capability that tmux uses to mean that the terminal supports the [xterm(1)](/xterm.1) title set sequences and to automatically set some of the capabilities above.

## CONTROL MODE

`tmux` offers a textual interface called [*control mode*](#control). This allows applications to communicate with `tmux` using a simple text-only protocol.

 %begin 1363006971 2 1
 0: ksh* (1 panes) [80x24] [layout b25f,80x24,0,0,2] @2 (active)
 %end 1363006971 2 1

In control mode, `tmux` outputs notifications. A notification will never occur inside an output block.

The following notifications are defined:

[`%client-detached`](#_client-detached) `client`
: The client has detached.

[`%client-session-changed`](#_client-session-changed) `client session-id name`
: The client is now attached to the session with ID `session-id`, which is named `name`.

[`%config-error`](#_config-error) `error`
: An error has happened in a configuration file.

[`%continue`](#_continue) `pane-id`
: The pane has been continued after being paused (if the `pause-after` flag is set, see `refresh-client` `-A`).

[`%exit`](#_exit) [`reason`]
: The `tmux` client is exiting immediately, either because it is not attached to any session or an error occurred. If present, `reason` describes why the client exited.

[`%extended-output`](#_extended-output) `pane-id` `age` `... `: `value`
: New form of `%output` sent when the `pause-after` flag is set. `age` is the time in milliseconds for which tmux had buffered the output before it was sent. Any subsequent arguments up until a single '`:`' are for future use and should be ignored.

[`%layout-change`](#_layout-change) `window-id` `window-layout` `window-visible-layout` `window-flags`
: The layout of a window with ID `window-id` changed. The new layout is `window-layout`. The window's visible layout is `window-visible-layout` and the window flags are `window-flags`.

[`%message`](#_message) `message`

[`%output`](#_output) `pane-id` `value`
: A window pane produced output. `value` escapes non-printable characters and backslash as octal \\xxx.

[`%pane-mode-changed`](#_pane-mode-changed) `pane-id`
: The pane with ID `pane-id` has changed mode.

[`%paste-buffer-changed`](#_paste-buffer-changed) `name`
: Paste buffer `name` has been changed.

[`%paste-buffer-deleted`](#_paste-buffer-deleted) `name`
: Paste buffer `name` has been deleted.

[`%pause`](#_pause) `pane-id`
: The pane has been paused (if the `pause-after` flag is set).

[`%session-changed`](#_session-changed) `session-id` `name`
: The client is now attached to the session with ID `session-id`, which is named `name`.

[`%session-renamed`](#_session-renamed) `name`
: The current session was renamed to `name`.

[`%session-window-changed`](#_session-window-changed) `session-id` `window-id`
: The session with ID `session-id` changed its active window to the window with ID `window-id`.

[`%sessions-changed`](#_sessions-changed)
: A session was created or destroyed.

[`%subscription-changed`](#_subscription-changed) `name` `session-id` `window-id` `window-index` `pane-id ... `: `value`
: The value of the format associated with subscription `name` has changed to `value`. See `refresh-client` `-B`. Any arguments after `pane-id` up until a single '`:`' are for future use and should be ignored.

[`%unlinked-window-add`](#_unlinked-window-add) `window-id`
: The window with ID `window-id` was created but is not linked to the current session.

[`%unlinked-window-close`](#_unlinked-window-close) `window-id`
: The window with ID `window-id`, which is not linked to the current session, was closed.

[`%unlinked-window-renamed`](#_unlinked-window-renamed) `window-id`
: The window with ID `window-id`, which is not linked to the current session, was renamed.

[`%window-add`](#_window-add) `window-id`
: The window with ID `window-id` was linked to the current session.

[`%window-close`](#_window-close) `window-id`
: The window with ID `window-id` closed.

[`%window-pane-changed`](#_window-pane-changed) `window-id` `pane-id`
: The active pane in the window with ID `window-id` changed to the pane with ID `pane-id`.

[`%window-renamed`](#_window-renamed) `window-id` `name`
: The window with ID `window-id` was renamed to `name`.

## ENVIRONMENT

When `tmux` is started, it inspects the following environment variables:

[`EDITOR`](#EDITOR)

[`HOME`](#HOME)
: The user's login directory. If unset, the [passwd(5)](/passwd.5) database is consulted.

[`LC_CTYPE`](#LC_CTYPE)
: The character encoding [locale(1)](/locale.1). It is used for two separate purposes. For output to the terminal, UTF-8 is used if the `-u` option is given or if `LC_CTYPE` contains \"UTF-8\" or \"UTF8\". Otherwise, only ASCII characters are written and non-ASCII characters are replaced with underscores ('`_`'). For input, `tmux` always runs with a UTF-8 locale. If en_US.UTF-8 is provided by the operating system, it is used and `LC_CTYPE` is ignored for input. Otherwise, `LC_CTYPE` tells `tmux` what the UTF-8 locale is called on the current system. If the locale specified by `LC_CTYPE` is not available or is not a UTF-8 locale, `tmux` exits with an error message.

[`LC_TIME`](#LC_TIME)
: The date and time format [locale(1)](/locale.1). It is used for locale-dependent [strftime(3)](/strftime.3) format specifiers.

[`PWD`](#PWD)
: The current working directory to be set in the global environment. This may be useful if it contains symbolic links. If the value of the variable does not match the current working directory, the variable is ignored and the result of [getcwd(3)](/getcwd.3) is used instead.

[`SHELL`](#SHELL)
: The absolute path to the default shell for new windows. See the `default-shell` option for details.

[`TMUX_TMPDIR`](#TMUX_TMPDIR)
: The parent directory of the directory containing the server sockets. See the `-L` option for details.

[`VISUAL`](#VISUAL)

## FILES

[\~/.tmux.conf]
: Default `tmux` configuration file.

[/etc/tmux.conf]
: System-wide configuration file.

## EXAMPLES

To create a new `tmux` session running [vi(1)](/vi.1):

`$ tmux new-session vi`

`$ tmux new vi`

 $ tmux n

Within an active session, a new window may be created by typing '`C-b c`' (Ctrl followed by the '`b`' key followed by the '`c`' key).

Windows may be navigated with: '`C-b 0`' (to select window 0), '`C-b 1`' (to select window 1), and so on; '`C-b n`' to select the next window; and '`C-b p`' to select the previous window.

A session may be detached using '`C-b d`' (or by an external event such as [ssh(1)](/ssh.1) disconnection) and reattached with:

`$ tmux attach-session`

Typing '`C-b ?`' lists the current key bindings in the current window; up and down may be used to navigate the list or '`q`' to exit from it.

Changing the default prefix key:

 set-option -g prefix C-a
 unbind-key C-b
 bind-key C-a send-prefix

Turning the status line off, or changing its colour:

 set-option -g status off
 set-option -g status-style bg=blue

 set-option -g lock-after-time 1800

Creating new key bindings:

 bind-key b set-option status

## SEE ALSO

[pty(4)](/pty.4)

## AUTHORS

[Nicholas Marriott] \<[nicholas.marriott@gmail.com](mailto:nicholas.marriott@gmail.com)\>

 line"}