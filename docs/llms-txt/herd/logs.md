# Source: https://herd.laravel.com/docs/macos/debugging/logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Log Viewer

# Inspect local log files

If you don't want to run a terminal command like `tail` or tail the logs with [Laravel Pail](https://laravel.com/docs/11.x/logging#tailing-log-messages-using-pail), you can use Herd's integrated log viewer. It allows you to inspect your log files in great detail and makes searching through logs a breeze.

If you are only interested in the logs of the latest request, you man use the [log view](/macos/debugging/dumps#logs) of the [Dumps](/macos/debugging/dumps) feature to get the most recent logs automatically.

<Note>
  This feature requires PHP 8.0 or later
</Note>

Herd automatically polls for new logs every few seconds as long as the Logs window is open.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/log-viewer.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=722a74dd322c7ae6e4f814297dc11a7e" data-og-width="2454" width="2454" data-og-height="1512" height="1512" data-path="images/docs/log-viewer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/log-viewer.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a1b672928847ec2027725de8dedc06c5 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/log-viewer.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=99932afca188d8f00c32d07a6e926a52 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/log-viewer.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=98b86757352ea0696509ce3b84a2fa03 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/log-viewer.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=6d7279117c4554c96b032ad969de144a 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/log-viewer.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=28886826d371c2614ec0bba2b6b6aca5 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/log-viewer.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=6c72789e4efdce24c3853bb04956bfc1 2500w" />
</Frame>

## Selecting a Project and Log File

By default, the log window shows the latest log file of the last project that you visited in your browser. This allows you to quickly find the latest log file, but you can also switch between all projects that Herd knows and serves.

If your project includes more than one log file, for example when using daily log rotation, you can select the log file on the left.

## Searching in Log Files

The search bar at the top searches through all logs and allows you to pinpoint all log entries that match your search query. You can hit Cmd+F in the text area that shows the details of the entry and search within this single entry.

## Custom log paths

Herd looks for logs in the framework-specific standard directory, such as `storage/logs` for Laravel. You can change that directory and even add multiple log directories by using a [custom driver](/macos/extending-herd/custom-drivers#customize-herds-behaviour) for that application.
