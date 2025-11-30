# Source: https://docs.ntfy.sh/subscribe/cli/

# Subscribe via ntfy CLI[¶](#subscribe-via-ntfy-cli "Permanent link")

In addition to subscribing via the [web UI](../web/), the [phone app](../phone/), or the [API](../api/), you can subscribe to topics via the ntfy CLI. The CLI is included in the same `ntfy` binary that can be used to [self-host a server](../../install/).

Info

The **ntfy CLI is not required to send or receive messages**. You can instead [send messages with curl](../../publish/), and even use it to [subscribe to topics](../api/). It may be a little more convenient to use the ntfy CLI than writing your own script. It all depends on the use case. 😀

## Install + configure[¶](#install-configure "Permanent link")

To install the ntfy CLI, simply **follow the steps outlined on the [install page](../../install/)**. The ntfy server and client are the same binary, so it\'s all very convenient. After installing, you can (optionally) configure the client by creating `~/.config/ntfy/client.yml` (for the non-root user), `~/Library/Application Support/ntfy/client.yml` (for the macOS non-root user), or `/etc/ntfy/client.yml` (for the root user). You can find a [skeleton config](https://github.com/binwiederhier/ntfy/blob/main/client/client.yml) on GitHub.

If you just want to use [ntfy.sh](https://ntfy.sh), you don\'t have to change anything. If you **self-host your own server**, you may want to edit the `default-host` option:

    # Base URL used to expand short topic names in the "ntfy publish" and "ntfy subscribe" commands.
    # If you self-host a ntfy server, you'll likely want to change this.
    #
    default-host: https://ntfy.myhost.com

## Publish messages[¶](#publish-messages "Permanent link")

You can send messages with the ntfy CLI using the `ntfy publish` command (or any of its aliases `pub`, `send` or `trigger`). There are a lot of examples on the page about [publishing messages](../../publish/), but here are a few quick ones:

Simple sendSend with title, priority, and tagsSend at 8:30amTriggering a webhook

    ntfy publish mytopic This is a message
    ntfy publish mytopic "This is a message"
    ntfy pub mytopic "This is a message" 

    ntfy publish \
        --title="Thing sold on eBay" \
        --priority=high \
        --tags=partying_face \
        mytopic \
        "Somebody just bought the thing that you sell"

    ntfy pub --at=8:30am delayed_topic Laterzz

    ntfy trigger mywebhook
    ntfy pub mywebhook

### Attaching a local file[¶](#attaching-a-local-file "Permanent link")

You can easily upload and attach a local file to a notification:

    $ ntfy pub --file README.md mytopic | jq .
    
    }

### Wait for PID/command[¶](#wait-for-pidcommand "Permanent link")

If you have a long-running command and want to **publish a notification when the command completes**, you may wrap it with `ntfy publish --wait-cmd` (aliases: `--cmd`, `--done`). Or, if you forgot to wrap it, and the command is already running, you can wait for the process to complete with `ntfy publish --wait-pid` (alias: `--pid`).

Run a command and wait for it to complete (here: `rsync ...`):

    $ ntfy pub --wait-cmd mytopic rsync -av ./ root@example.com:/backups/ | jq .
    

Or, if you already started the long-running process and want to wait for it using its process ID (PID), you can do this:

Using a PID directlyUsing a `pidof`

    $ ntfy pub --wait-pid 8458 mytopic | jq .
    

    $ ntfy pub --wait-pid $(pidof rsync) mytopic | jq .
    

## Subscribe to topics[¶](#subscribe-to-topics "Permanent link")

You can subscribe to topics using `ntfy subscribe`. Depending on how it is called, this command will either print or execute a command for every arriving message. There are a few different ways in which the command can be run:

### Stream messages as JSON[¶](#stream-messages-as-json "Permanent link")

    ntfy subscribe TOPIC

If you run the command like this, it prints the JSON representation of every incoming message. This is useful when you have a command that wants to stream-read incoming JSON messages. Unless `--poll` is passed, this command stays open forever.

    $ ntfy sub mytopic
    
    
    ...

<figure>

<figcaption>Subscribe in JSON mode</figcaption>
</figure>

### Run command for every message[¶](#run-command-for-every-message "Permanent link")

    ntfy subscribe TOPIC COMMAND

If you run it like this, a COMMAND is executed for every incoming messages. Scroll down to see a list of available environment variables. Here are a few examples:

    ntfy sub mytopic 'notify-send "$m"'
    ntfy sub topic1 /my/script.sh
    ntfy sub topic1 'echo "Message $m was received. Its title was $t and it had priority $p"'

<figure>

<figcaption>Execute command on incoming messages</figcaption>
</figure>

The message fields are passed to the command as environment variables and can be used in scripts. Note that since these are environment variables, you typically don\'t have to worry about quoting too much, as long as you enclose them in double-quotes, you should be fine:

  Variable           Aliases                      Description
  ------------------ ---------------------------- ----------------------------------------
  `$NTFY_ID`         `$id`                        Unique message ID
  `$NTFY_TIME`       `$time`                      Unix timestamp of the message delivery
  `$NTFY_TOPIC`      `$topic`                     Topic name
  `$NTFY_MESSAGE`    `$message`, `$m`             Message body
  `$NTFY_TITLE`      `$title`, `$t`               Message title
  `$NTFY_PRIORITY`   `$priority`, `$prio`, `$p`   Message priority (1=min, 5=max)
  `$NTFY_TAGS`       `$tags`, `$tag`, `$ta`       Message tags (comma separated list)
  `$NTFY_RAW`        `$raw`                       Raw JSON message

### Subscribe to multiple topics[¶](#subscribe-to-multiple-topics "Permanent link")

    ntfy subscribe --from-config

To subscribe to multiple topics at once, and run different commands for each one, you can use `ntfy subscribe --from-config`, which will read the `subscribe` config from the config file. Please also check out the [ntfy-client systemd service](#using-the-systemd-service).

Here\'s an example config file that subscribes to three different topics, executing a different command for each of them:

\~/.config/ntfy/client.yml (Linux)\~/Library/Application Support/ntfy/client.yml (macOS)%AppData%\\ntfy\\client.yml (Windows)

    default-host: https://ntfy.sh
    default-user: phill
    default-password: mypass

    subscribe:
    - topic: echo-this
      command: 'echo "Message received: $message"'
    - topic: alerts
      command: notify-send -i /usr/share/ntfy/logo.png "Important" "$m"
      if:
        priority: high,urgent
    - topic: calc
      command: 'gnome-calculator 2>/dev/null &'
    - topic: print-temp
      command: |
            echo "You can easily run inline scripts, too."
            temp="$(sensors | awk '/Pack/ ')"
            if [ $temp -gt 80 ]; then
              echo "Warning: CPU temperature is $temp. Too high."
            else
              echo "CPU temperature is $temp. That's alright."
            fi

    default-host: https://ntfy.sh
    default-user: phill
    default-password: mypass

    subscribe:
      - topic: echo-this
        command: 'echo "Message received: $message"'
      - topic: alerts
        command: osascript -e "display notification \"$message\""
        if:
          priority: high,urgent
      - topic: calc
        command: open -a Calculator

    default-host: https://ntfy.sh
    default-user: phill
    default-password: mypass

    subscribe:
    - topic: echo-this
      command: 'echo Message received: %message%'
    - topic: alerts
      command: |
        notifu /m "%NTFY_MESSAGE%"
        exit 0
      if:
        priority: high,urgent
    - topic: calc
      command: calc

In this example, when `ntfy subscribe --from-config` is executed:

- Messages to `echo-this` simply echos to standard out
- Messages to `alerts` display as desktop notification for high priority messages using [notify-send](https://manpages.ubuntu.com/manpages/focal/man1/notify-send.1.html) (Linux), [notifu](https://www.paralint.com/projects/notifu/) (Windows) or `osascript` (macOS)
- Messages to `calc` open the calculator 😀 (*because, why not*)
- Messages to `print-temp` execute an inline script and print the CPU temperature (Linux version only)

I hope this shows how powerful this command is. Here\'s a short video that demonstrates the above example:

<figure>

<figcaption>Execute all the things</figcaption>
</figure>

If most (or all) of your subscriptions use the same credentials, you can set defaults in `client.yml`. Use `default-user` and `default-password` or `default-token` (but not both). You can also specify a `default-command` that will run when a message is received. If a subscription does not include credentials to use or does not have a command, the defaults will be used, otherwise, the subscription settings will override the defaults.

Warning

Because the `default-user`, `default-password`, and `default-token` will be sent for each topic that does not have its own username/password (even if the topic does not require authentication), be sure that the servers/topics you subscribe to use HTTPS to prevent leaking the username and password.

### Using the systemd service[¶](#using-the-systemd-service "Permanent link")

You can use the `ntfy-client` systemd services to subscribe to multiple topics just like in the example above.

You have the option of either enabling `ntfy-client` as a **system service** (see [here](https://github.com/binwiederhier/ntfy/blob/main/client/ntfy-client.service)) or **user service** (see [here](https://github.com/binwiederhier/ntfy/blob/main/client/user/ntfy-client.service)). Neither system service nor user service are enabled or started by default, so you have to do that yourself.

**System service:** The `ntfy-client` systemd system service runs as the `ntfy` user. When enabled, it is started at system boot. To configure it as a system service, edit `/etc/ntfy/client.yml` and then enable/start the service (as root), like so:

    sudo systemctl enable ntfy-client
    sudo systemctl restart ntfy-client

The system service runs as user `ntfy`, meaning that typical Linux permission restrictions apply. It also means that the system service cannot run commands in your X session as the primary machine user (unlike the user service).

**User service:** The `ntfy-client` user service is run when the user logs into their desktop environment. To enable/start it, edit `~/.config/ntfy/client.yml` and run the following commands (without sudo!):

    systemctl --user enable ntfy-client
    systemctl --user restart ntfy-client

Unlike the system service, the user service can interact with the user\'s desktop environment, and run commands like `notify-send` to display desktop notifications. It can also run commands that require access to the user\'s home directory, such as `gnome-calculator`.

### Authentication[¶](#authentication "Permanent link")

Depending on whether the server is configured to support [access control](../../config/#access-control), some topics may be read/write protected so that only users with the correct credentials can subscribe or publish to them. To publish/subscribe to protected topics, you can use [Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication) with a valid username/password. For your self-hosted server, **be sure to use HTTPS to avoid eavesdropping** and exposing your password.

You can either add your username and password to the configuration file:

\~/.config/ntfy/client.yml

     - topic: secret
       command: 'notify-send "$m"'
       user: phill
       password: mypass

Or with the `ntfy subscribe` command:

    ntfy subscribe \
      -u phil:mypass \
      ntfy.example.com/mysecrets