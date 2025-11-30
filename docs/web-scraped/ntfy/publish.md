# Source: https://docs.ntfy.sh/publish/

# Publishing[¶](#publishing "Permanent link")

Publishing messages can be done via HTTP PUT/POST or via the [ntfy CLI](../install/). Topics are created on the fly by subscribing or publishing to them. Because there is no sign-up, **the topic is essentially a password**, so pick something that\'s not easily guessable.

Here\'s an example showing how to publish a simple message using a POST request:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl -d "Backup successful 😀" ntfy.sh/mytopic

    ntfy publish mytopic "Backup successful 😀"

    POST /mytopic HTTP/1.1
    Host: ntfy.sh

    Backup successful 😀

    fetch('https://ntfy.sh/mytopic', )

    http.Post("https://ntfy.sh/mytopic", "text/plain",
        strings.NewReader("Backup successful 😀"))

    $Request = @
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/mytopic", 
        data="Backup successful 😀".encode(encoding='utf-8'))

    file_get_contents('https://ntfy.sh/mytopic', false, stream_context_create([
        'http' => [
            'method' => 'POST', // PUT also works
            'header' => 'Content-Type: text/plain',
            'content' => 'Backup successful 😀'
        ]
    ]));

If you have the [Android app](../subscribe/phone/) installed on your phone, this will create a notification that looks like this:

<figure>
<p><img src="../static/img/android-screenshot-basic-notification.png" width="500" alt="basic notification" /></p>
<figcaption>Android notification</figcaption>
</figure>

There are more features related to publishing messages: You can set a [notification priority](#message-priority), a [title](#message-title), and [tag messages](#tags-emojis) 🥳 🎉. Here\'s an example that uses some of them at together:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl \
      -H "Title: Unauthorized access detected" \
      -H "Priority: urgent" \
      -H "Tags: warning,skull" \
      -d "Remote access to phils-laptop detected. Act right away." \
      ntfy.sh/phil_alerts

    ntfy publish \
        --title "Unauthorized access detected" \
        --tags warning,skull \
        --priority urgent \
        mytopic \
        "Remote access to phils-laptop detected. Act right away."

    POST /phil_alerts HTTP/1.1
    Host: ntfy.sh
    Title: Unauthorized access detected
    Priority: urgent
    Tags: warning,skull

    Remote access to phils-laptop detected. Act right away.

    fetch('https://ntfy.sh/phil_alerts', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/phil_alerts",
        strings.NewReader("Remote access to phils-laptop detected. Act right away."))
    req.Header.Set("Title", "Unauthorized access detected")
    req.Header.Set("Priority", "urgent")
    req.Header.Set("Tags", "warning,skull")
    http.DefaultClient.Do(req)

    $Request = @
      Body = "Remote access to phils-laptop detected. Act right away."
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/phil_alerts",
        data="Remote access to phils-laptop detected. Act right away.",
        headers=)

    file_get_contents('https://ntfy.sh/phil_alerts', false, stream_context_create([
        'http' => [
            'method' => 'POST', // PUT also works
            'header' =>
                "Content-Type: text/plain\r\n" .
                "Title: Unauthorized access detected\r\n" .
                "Priority: urgent\r\n" .
                "Tags: warning,skull",
            'content' => 'Remote access to phils-laptop detected. Act right away.'
        ]
    ]));

<figure>
<p><img src="../static/img/priority-notification.png" width="500" alt="priority notification" /></p>
<figcaption>Urgent notification with tags and title</figcaption>
</figure>

You can also do multi-line messages. Here\'s an example using a [click action](#click-action), an [action button](#action-buttons), an [external image attachment](#attach-file-from-a-url) and [email publishing](#e-mail-publishing):

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl \
      -H "Click: https://home.nest.com/" \
      -H "Attach: https://nest.com/view/yAxkasd.jpg" \
      -H "Actions: http, Open door, https://api.nest.com/open/yAxkasd, clear=true" \
      -H "Email: phil@example.com" \
      -d "There's someone at the door. 🐶

    Please check if it's a good boy or a hooman. 
    Doggies have been known to ring the doorbell." \
      ntfy.sh/mydoorbell

    ntfy publish \
        --click="https://home.nest.com/" \
        --attach="https://nest.com/view/yAxkasd.jpg" \
        --actions="http, Open door, https://api.nest.com/open/yAxkasd, clear=true" \
        --email="phil@example.com" \
        mydoorbell \
        "There's someone at the door. 🐶

    Please check if it's a good boy or a hooman. 
    Doggies have been known to ring the doorbell."

    POST /mydoorbell HTTP/1.1
    Host: ntfy.sh
    Click: https://home.nest.com/
    Attach: https://nest.com/view/yAxkasd.jpg
    Actions: http, Open door, https://api.nest.com/open/yAxkasd, clear=true
    Email: phil@example.com

    There's someone at the door. 🐶

    Please check if it's a good boy or a hooman. 
    Doggies have been known to ring the doorbell.

    fetch('https://ntfy.sh/mydoorbell', ,
        body: `There's someone at the door. 🐶

    Please check if it's a good boy or a hooman. 
    Doggies have been known to ring the doorbell.`,
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/mydoorbell",
        strings.NewReader(`There's someone at the door. 🐶

    Please check if it's a good boy or a hooman. 
    Doggies have been known to ring the doorbell.`))
    req.Header.Set("Click", "https://home.nest.com/")
    req.Header.Set("Attach", "https://nest.com/view/yAxkasd.jpg")
    req.Header.Set("Actions", "http, Open door, https://api.nest.com/open/yAxkasd, clear=true")
    req.Header.Set("Email", "phil@example.com")
    http.DefaultClient.Do(req)

    $Request = @
      Body = "There's someone at the door. 🐶`n
      `n
      Please check if it's a good boy or a hooman.`n
      Doggies have been known to ring the doorbell.`n"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/mydoorbell",
        data="""There's someone at the door. 🐶

    Please check if it's a good boy or a hooman.
    Doggies have been known to ring the doorbell.""".encode('utf-8'),
        headers=)

    file_get_contents('https://ntfy.sh/mydoorbell', false, stream_context_create([
        'http' => [
            'method' => 'POST', // PUT also works
            'header' =>
                "Content-Type: text/plain\r\n" .
                "Click: https://home.nest.com/\r\n" .
                "Attach: https://nest.com/view/yAxkasd.jpg\r\n" .
                "Actions": "http, Open door, https://api.nest.com/open/yAxkasd, clear=true\r\n" .
                "Email": "phil@example.com\r\n",
            'content' => 'There\'s someone at the door. 🐶

    Please check if it\'s a good boy or a hooman.
    Doggies have been known to ring the doorbell.'
        ]
    ]));

<figure>
<p><img src="../static/img/android-screenshot-notification-multiline.jpg" width="500" alt="priority notification" /></p>
<figcaption>Notification using a click action, a user action, with an external image attachment and forwarded via email</figcaption>
</figure>

## Message title[¶](#message-title "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

The notification title is typically set to the topic short URL (e.g. `ntfy.sh/mytopic`). To override the title, you can set the `X-Title` header (or any of its aliases: `Title`, `ti`, or `t`).

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl -H "X-Title: Dogs are better than cats" -d "Oh my ..." ntfy.sh/controversial
    curl -H "Title: Dogs are better than cats" -d "Oh my ..." ntfy.sh/controversial
    curl -H "t: Dogs are better than cats" -d "Oh my ..." ntfy.sh/controversial

    ntfy publish \
        -t "Dogs are better than cats" \
        controversial "Oh my ..."

    POST /controversial HTTP/1.1
    Host: ntfy.sh
    Title: Dogs are better than cats

    Oh my ...

    fetch('https://ntfy.sh/controversial', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/controversial", strings.NewReader("Oh my ..."))
    req.Header.Set("Title", "Dogs are better than cats")
    http.DefaultClient.Do(req)

    $Request = @
      Body = "Oh my ..."
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/controversial",
        data="Oh my ...",
        headers=)

    file_get_contents('https://ntfy.sh/controversial', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' =>
                "Content-Type: text/plain\r\n" .
                "Title: Dogs are better than cats",
            'content' => 'Oh my ...'
        ]
    ]));

<figure>
<p><img src="../static/img/notification-with-title.png" width="500" alt="notification with title" /></p>
<figcaption>Detail view of notification with title</figcaption>
</figure>

Info

ntfy supports UTF-8 in HTTP headers, but [not every library or programming language does](https://www.jmix.io/blog/utf-8-in-http-headers/). If non-ASCII characters are causing issues for you in the title (i.e. you\'re seeing `?` symbols), you may also encode any header (including the title) as [RFC 2047](https://datatracker.ietf.org/doc/html/rfc2047#section-2), e.g. `=?UTF-8?B?8J+HqfCfh6o=?=` ([base64](https://en.wikipedia.org/wiki/Base64)), or `=?UTF-8?Q?=C3=84pfel?=` ([quoted-printable](https://en.wikipedia.org/wiki/Quoted-printable)).

## Message priority[¶](#message-priority "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

All messages have a priority, which defines how urgently your phone notifies you. On Android, you can set custom notification sounds and vibration patterns on your phone to map to these priorities (see [Android config](../subscribe/phone/)).

The following priorities exist:

  Priority               Icon                                            ID    Name             Description
  ---------------------- ----------------------------------------------- ----- ---------------- --------------------------------------------------------------------------------------------------------
  Max priority           ![min priority](../static/img/priority-5.svg)   `5`   `max`/`urgent`   Really long vibration bursts, default notification sound with a pop-over notification.
  High priority          ![min priority](../static/img/priority-4.svg)   `4`   `high`           Long vibration burst, default notification sound with a pop-over notification.
  **Default priority**   *(none)*                                        `3`   `default`        Short default vibration and sound. Default notification behavior.
  Low priority           ![min priority](../static/img/priority-2.svg)   `2`   `low`            No vibration or sound. Notification will not visibly show up until notification drawer is pulled down.
  Min priority           ![min priority](../static/img/priority-1.svg)   `1`   `min`            No vibration or sound. The notification will be under the fold in \"Other notifications\".

You can set the priority with the header `X-Priority` (or any of its aliases: `Priority`, `prio`, or `p`).

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl -H "X-Priority: 5" -d "An urgent message" ntfy.sh/phil_alerts
    curl -H "Priority: low" -d "Low priority message" ntfy.sh/phil_alerts
    curl -H p:4 -d "A high priority message" ntfy.sh/phil_alerts

    ntfy publish \ 
        -p 5 \
        phil_alerts An urgent message

    POST /phil_alerts HTTP/1.1
    Host: ntfy.sh
    Priority: 5

    An urgent message

    fetch('https://ntfy.sh/phil_alerts', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/phil_alerts", strings.NewReader("An urgent message"))
    req.Header.Set("Priority", "5")
    http.DefaultClient.Do(req)

    $Request = @
      Body = "An urgent message"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/phil_alerts",
        data="An urgent message",
        headers=)

    file_get_contents('https://ntfy.sh/phil_alerts', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' =>
                "Content-Type: text/plain\r\n" .
                "Priority: 5",
            'content' => 'An urgent message'
        ]
    ]));

<figure>
<p><img src="../static/img/priority-detail-overview.png" width="500" alt="priority notification" /></p>
<figcaption>Detail view of priority notifications</figcaption>
</figure>

## Tags & emojis 🥳 🎉[¶](#tags-emojis "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

You can tag messages with emojis and other relevant strings:

- **Emojis**: If a tag matches an [emoji short code](../emojis/), it\'ll be converted to an emoji and prepended to title or message.
- **Other tags:** If a tag doesn\'t match, it will be listed below the notification.

This feature is useful for things like warnings (⚠️, ️🚨, or 🚩), but also to simply tag messages otherwise (e.g. script names, hostnames, etc.). Use [the emoji short code list](../emojis/) to figure out what tags can be converted to emojis. Here\'s an **excerpt of emojis** I\'ve found very useful in alert messages:

+--------------------------------+---------------------------------------+-----------------------------+
|   Tag                  Emoji   |   Tag                         Emoji   |   Tag               Emoji   |
|   -------------------- ------- |   --------------------------- ------- |   ----------------- ------- |
|   `+1`                 👍      |   `-1`                        👎️      |   `facepalm`        🤦      |
|   `partying_face`      🥳      |   `warning`                   ⚠️      |   `no_entry`        ⛔      |
|   `tada`               🎉      |   `rotating_light`            ️🚨      |   `no_entry_sign`   🚫      |
|   `heavy_check_mark`   ✔️      |   `triangular_flag_on_post`   🚩      |   `cd`              💿      |
|   `loudspeaker`        📢      |   `skull`                     💀      |   `computer`        💻      |
|   \...                 \...    |   \...                        \...    |   \...              \...    |
+--------------------------------+---------------------------------------+-----------------------------+

You can set tags with the `X-Tags` header (or any of its aliases: `Tags`, `tag`, or `ta`). Specify multiple tags by separating them with a comma, e.g. `tag1,tag2,tag3`.

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl -H "X-Tags: warning,mailsrv13,daily-backup" -d "Backup of mailsrv13 failed" ntfy.sh/backups
    curl -H "Tags: horse,unicorn" -d "Unicorns are just horses with unique horns" ntfy.sh/backups
    curl -H ta:dog -d "Dogs are awesome" ntfy.sh/backups

    ntfy publish \
        --tags=warning,mailsrv13,daily-backup \
        backups "Backup of mailsrv13 failed"

    POST /backups HTTP/1.1
    Host: ntfy.sh
    Tags: warning,mailsrv13,daily-backup

    Backup of mailsrv13 failed

    fetch('https://ntfy.sh/backups', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/backups", strings.NewReader("Backup of mailsrv13 failed"))
    req.Header.Set("Tags", "warning,mailsrv13,daily-backup")
    http.DefaultClient.Do(req)

    $Request = @
      Body = "Backup of mailsrv13 failed"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/backups",
        data="Backup of mailsrv13 failed",
        headers=)

    file_get_contents('https://ntfy.sh/backups', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' =>
                "Content-Type: text/plain\r\n" .
                "Tags: warning,mailsrv13,daily-backup",
            'content' => 'Backup of mailsrv13 failed'
        ]
    ]));

<figure>
<p><img src="../static/img/notification-with-tags.png" width="500" alt="priority notification" /></p>
<figcaption>Detail view of notifications with tags</figcaption>
</figure>

Info

ntfy supports UTF-8 in HTTP headers, but [not every library or programming language does](https://www.jmix.io/blog/utf-8-in-http-headers/). If non-ASCII characters are causing issues for you in the title (i.e. you\'re seeing `?` symbols), you may also encode the tags header or individual tags as [RFC 2047](https://datatracker.ietf.org/doc/html/rfc2047#section-2), e.g. `tag1,=?UTF-8?B?8J+HqfCfh6o=?=` ([base64](https://en.wikipedia.org/wiki/Base64)), or `=?UTF-8?Q?=C3=84pfel?=,tag2` ([quoted-printable](https://en.wikipedia.org/wiki/Quoted-printable)).

## Markdown formatting[¶](#markdown-formatting "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

You can format messages using [Markdown](https://www.markdownguide.org/basic-syntax/) 🤩. That means you can use **bold text**, *italicized text*, links, images, and more. Supported Markdown features (web app only for now):

- [Emphasis](https://www.markdownguide.org/basic-syntax/#emphasis) such as **bold** (`**bold**`), *italics* (`*italics*`)
- [Links](https://www.markdownguide.org/basic-syntax/#links) (`[some tool](https://ntfy.sh)`)
- [Images](https://www.markdownguide.org/basic-syntax/#images) (`![some image](https://bing.com/logo.png)`)
- [Code blocks](https://www.markdownguide.org/basic-syntax/#code-blocks) (```` ```code blocks``` ````) and [inline code](https://www.markdownguide.org/basic-syntax/#inline-code) (`` `inline code` ``)
- [Headings](https://www.markdownguide.org/basic-syntax/#headings) (`# headings`, `## headings`, etc.)
- [Lists](https://www.markdownguide.org/basic-syntax/#lists) (`- lists`, `1. lists`, etc.)
- [Blockquotes](https://www.markdownguide.org/basic-syntax/#blockquotes) (`> blockquotes`)
- [Horizontal rules](https://www.markdownguide.org/basic-syntax/#horizontal-rules) (`---`)

By default, messages sent to ntfy are rendered as plain text. To enable Markdown, set the `X-Markdown` header (or any of its aliases: `Markdown`, or `md`) to `true` (or `1` or `yes`), or set the `Content-Type` header to `text/markdown`. As of today, **Markdown is only supported in the web app.** Here\'s an example of how to enable Markdown formatting:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl \
        -d "Look ma, **bold text**, *italics*, ..." \
        -H "Markdown: yes" \
        ntfy.sh/mytopic

    ntfy publish \
        --markdown \
        mytopic \
        "Look ma, **bold text**, *italics*, ..."

    POST /mytopic HTTP/1.1
    Host: ntfy.sh
    Markdown: yes

    Look ma, **bold text**, *italics*, ...

    fetch('https://ntfy.sh/mytopic', 
    })

    http.Post("https://ntfy.sh/mytopic", "text/markdown",
        strings.NewReader("Look ma, **bold text**, *italics*, ..."))

    // or
    req, _ := http.NewRequest("POST", "https://ntfy.sh/mytopic", 
        strings.NewReader("Look ma, **bold text**, *italics*, ..."))
    req.Header.Set("Markdown", "yes")
    http.DefaultClient.Do(req)

    $Request = @
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/mytopic", 
        data="Look ma, **bold text**, *italics*, ..."
        headers=))

    file_get_contents('https://ntfy.sh/mytopic', false, stream_context_create([
        'http' => [
            'method' => 'POST', // PUT also works
            'header' => 'Content-Type: text/markdown', // !
            'content' => 'Look ma, **bold text**, *italics*, ...'
        ]
    ]));

Here\'s what that looks like in the web app:

<figure>
<p><img src="../static/img/web-markdown.png" width="500" alt="markdown" /></p>
<figcaption>Markdown formatting in the web app</figcaption>
</figure>

## Scheduled delivery[¶](#scheduled-delivery "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

You can delay the delivery of messages and let ntfy send them at a later date. This can be used to send yourself reminders or even to execute commands at a later date (if your subscriber acts on messages).

Usage is pretty straight forward. You can set the delivery time using the `X-Delay` header (or any of its aliases: `Delay`, `X-At`, `At`, `X-In` or `In`), either by specifying a Unix timestamp (e.g. `1639194738`), a duration (e.g. `30m`, `3h`, `2 days`), or a natural language time string (e.g. `10am`, `8:30pm`, `tomorrow, 3pm`, `Tuesday, 7am`, [and more](https://github.com/olebedev/when)).

As of today, the minimum delay you can set is **10 seconds** and the maximum delay is **3 days**. This can be configured with the `message-delay-limit` option).

For the purposes of [message caching](../config/#message-cache), scheduled messages are kept in the cache until 12 hours after they were delivered (or whatever the server-side cache duration is set to). For instance, if a message is scheduled to be delivered in 3 days, it\'ll remain in the cache for 3 days and 12 hours. Also note that naturally, [turning off server-side caching](#message-caching) is not possible in combination with this feature.

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl -H "At: tomorrow, 10am" -d "Good morning" ntfy.sh/hello
    curl -H "In: 30min" -d "It's 30 minutes later now" ntfy.sh/reminder
    curl -H "Delay: 1639194738" -d "Unix timestamps are awesome" ntfy.sh/itsaunixsystem

    ntfy publish \
        --at="tomorrow, 10am" \
        hello "Good morning"

    POST /hello HTTP/1.1
    Host: ntfy.sh
    At: tomorrow, 10am

    Good morning

    fetch('https://ntfy.sh/hello', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/hello", strings.NewReader("Good morning"))
    req.Header.Set("At", "tomorrow, 10am")
    http.DefaultClient.Do(req)

    $Request = @
      Body = "Good morning"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/hello",
        data="Good morning",
        headers=)

    file_get_contents('https://ntfy.sh/backups', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' =>
                "Content-Type: text/plain\r\n" .
                "At: tomorrow, 10am",
            'content' => 'Good morning'
        ]
    ]));

Here are a few examples (assuming today\'s date is **12/10/2021, 9am, Eastern Time Zone**):

+------------------------------------------------------------------------------------------------------------+
|   `Delay/At/In` header   Message will be delivered at   Explanation                                        |
|   ---------------------- ------------------------------ -------------------------------------------------- |
|   `30m`                  12/10/2021, 9:**30**am         30 minutes from now                                |
|   `2 hours`              12/10/2021, **11:30**am        2 hours from now                                   |
|   `1 day`                12/**11**/2021, 9am            24 hours from now                                  |
|   `10am`                 12/10/2021, **10am**           Today at 10am (same day, because it\'s only 9am)   |
|   `8am`                  12/**11**/2021, **8am**        Tomorrow at 8am (because it\'s 9am already)        |
|   `1639152000`           12/10/2021, 11am (EST)         Today at 11am (EST)                                |
+------------------------------------------------------------------------------------------------------------+

## Webhooks (publish via GET)[¶](#webhooks-publish-via-get "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

In addition to using PUT/POST, you can also send to topics via simple HTTP GET requests. This makes it easy to use a ntfy topic as a [webhook](https://en.wikipedia.org/wiki/Webhook), or if your client has limited HTTP support.

To send messages via HTTP GET, simply call the `/publish` endpoint (or its aliases `/send` and `/trigger`). Without any arguments, this will send the message `triggered` to the topic. However, you can provide all arguments that are also supported as HTTP headers as URL-encoded arguments. Be sure to check the list of all [supported parameters and headers](#list-of-all-parameters) for details.

For instance, assuming your topic is `mywebhook`, you can simply call `/mywebhook/trigger` to send a message (aka trigger the webhook):

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl ntfy.sh/mywebhook/trigger

    ntfy trigger mywebhook

    GET /mywebhook/trigger HTTP/1.1
    Host: ntfy.sh

    fetch('https://ntfy.sh/mywebhook/trigger')

    http.Get("https://ntfy.sh/mywebhook/trigger")

    Invoke-RestMethod "ntfy.sh/mywebhook/trigger"

    requests.get("https://ntfy.sh/mywebhook/trigger")

    file_get_contents('https://ntfy.sh/mywebhook/trigger');

To add a custom message, simply append the `message=` URL parameter. And of course you can set the [message priority](#message-priority), the [message title](#message-title), and [tags](#tags-emojis) as well. For a full list of possible parameters, check the list of [supported parameters and headers](#list-of-all-parameters).

Here\'s an example with a custom message, tags and a priority:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl "ntfy.sh/mywebhook/publish?message=Webhook+triggered&priority=high&tags=warning,skull"

    ntfy publish \
        -p 5 --tags=warning,skull \
        mywebhook "Webhook triggered"

    GET /mywebhook/publish?message=Webhook+triggered&priority=high&tags=warning,skull HTTP/1.1
    Host: ntfy.sh

    fetch('https://ntfy.sh/mywebhook/publish?message=Webhook+triggered&priority=high&tags=warning,skull')

    http.Get("https://ntfy.sh/mywebhook/publish?message=Webhook+triggered&priority=high&tags=warning,skull")

    Invoke-RestMethod "ntfy.sh/mywebhook/publish?message=Webhook+triggered&priority=high&tags=warning,skull"

    requests.get("https://ntfy.sh/mywebhook/publish?message=Webhook+triggered&priority=high&tags=warning,skull")

    file_get_contents('https://ntfy.sh/mywebhook/publish?message=Webhook+triggered&priority=high&tags=warning,skull');

## Message templating[¶](#message-templating "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

Templating lets you **format a JSON message body into human-friendly message and title text** using [Go templates](https://pkg.go.dev/text/template) (see tutorials [here](https://blog.gopheracademy.com/advent-2017/using-go-templates/), [here](https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-go), and [here](https://developer.hashicorp.com/nomad/tutorials/templates/go-template-syntax)). This is specifically useful when **combined with webhooks** from services such as [GitHub](https://docs.github.com/en/webhooks/about-webhooks), [Grafana](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/manage-contact-points/integrations/webhook-notifier/), [Alertmanager](https://prometheus.io/docs/alerting/latest/configuration/#webhook_config), or other services that emit JSON webhooks.

Instead of using a separate bridge program to parse the webhook body into the format ntfy expects, you can include a templated message and/or a templated title which will be populated based on the fields of the webhook body (so long as the webhook body is valid JSON).

You can enable templating by setting the `X-Template` header (or its aliases `Template` or `tpl`, or the query parameter `?template=...`):

- **Pre-defined template files**: Setting the `X-Template` header or query parameter to a pre-defined template name (one of `github`, `grafana`, or `alertmanager`, such as `?template=github`) will use the built-in template with that name. See [pre-defined templates](#pre-defined-templates) for more details.
- **Custom template files**: Setting the `X-Template` header or query parameter to a custom template name (e.g. `?template=myapp`) will use a custom template file from the template directory (defaults to `/etc/ntfy/templates`, can be overridden with `template-dir`). See [custom templates](#custom-templates) for more details.
- **Inline templating**: Setting the `X-Template` header or query parameter to `yes` or `1` (e.g. `?template=yes`) will enable inline templating, which means that the `message` and/or `title` will be parsed as a Go template. See [inline templating](#inline-templating) for more details.

To learn the basics of Go\'s templating language, please see [template syntax](#template-syntax).

### Pre-defined templates[¶](#pre-defined-templates "Permanent link")

When `X-Template: <name>` (aliases: `Template: <name>`, `Tpl: <name>`) or `?template=<name>` is set, ntfy will transform the message and/or title based on one of the built-in pre-defined templates.

The following **pre-defined templates** are available:

- `github`: Formats a subset of [GitHub webhook](https://docs.github.com/en/webhooks/about-webhooks) payloads (PRs, issues, new star, new watcher, new comment). See [github.yml](https://github.com/binwiederhier/ntfy/blob/main/server/templates/github.yml).
- `grafana`: Formats [Grafana webhook](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/manage-contact-points/integrations/webhook-notifier/) payloads (firing/resolved alerts). See [grafana.yml](https://github.com/binwiederhier/ntfy/blob/main/server/templates/grafana.yml).
- `alertmanager`: Formats [Alertmanager webhook](https://prometheus.io/docs/alerting/latest/configuration/#webhook_config) payloads (firing/resolved alerts). See [alertmanager.yml](https://github.com/binwiederhier/ntfy/blob/main/server/templates/alertmanager.yml).

To override the pre-defined templates, you can place a file with the same name in the template directory (defaults to `/etc/ntfy/templates`, can be overridden with `template-dir`). See [custom templates](#custom-templates) for more details.

Here\'s an example of how to use the **pre-defined `github` template**:

First, configure the webhook in GitHub to send a webhook to your ntfy topic, e.g. `https://ntfy.sh/mytopic?template=github`.

<figure>
<p><img src="../static/img/screenshot-github-webhook-config.png" width="600" alt="GitHub webhook config" /></p>
<figcaption>GitHub webhook configuration</figcaption>
</figure>

After that, when GitHub publishes a JSON webhook to the topic, ntfy will transform it according to the template rules and you\'ll receive notifications in the ntfy app. Here\'s an example for when somebody stars your repository:

<figure>
<p><img src="../static/img/android-screenshot-template-predefined.png" width="500" alt="pre-defined template" /></p>
<figcaption>Receiving a webhook, formatted using the pre-defined "github" template</figcaption>
</figure>

### Custom templates[¶](#custom-templates "Permanent link")

To define **your own custom templates**, place a template file in the template directory (defaults to `/etc/ntfy/templates`, can be overridden with `template-dir`) and set the `X-Template` header or query parameter to the name of the template file (without the `.yml` extension).

For example, if you have a template file `/etc/ntfy/templates/myapp.yml`, you can set the header `X-Template: myapp` or the query parameter `?template=myapp` to use it.

Template files must have the `.yml` (not: `.yaml`!) extension and must be formatted as YAML. They may contain `title` and `message` keys, which are interpreted as Go templates.

Here\'s an **example custom template**:

Custom template (/etc/ntfy/templates/myapp.yml)

    title: |
      }
        }🚨 Critical alert
        }⚠️ Alert}
      }
      ✅ Alert resolved
      }
    message: |
      Status: }
      Type: } (}%)
      Server: }

Once you have the template file in place, you can send the payload to your topic using the `X-Template` header or query parameter:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    echo '' | \
      curl -sT- "https://ntfy.example.com/mytopic?template=myapp"

    echo '' | \
      ntfy publish --template=myapp https://ntfy.example.com/mytopic 

    POST /mytopic?template=myapp HTTP/1.1
    Host: ntfy.example.com

    

    fetch('https://ntfy.example.com/mytopic?template=myapp', '
    })

    payload := ``
    req, _ := http.NewRequest("POST", "https://ntfy.example.com/mytopic?template=myapp", strings.NewReader(payload))
    http.DefaultClient.Do(req)

    $Request = @'
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.example.com/mytopic?template=myapp",
      json=)

    file_get_contents('https://ntfy.example.com/mytopic?template=myapp', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' => "Content-Type: application/json",
            'content' => ''
        ]
    ]));

Which will result in a notification that looks like this:

<figure>
<p><img src="../static/img/android-screenshot-template-custom.png" width="500" alt="notification from custom JSON webhook template" /></p>
<figcaption>JSON webhook, transformed using a custom template</figcaption>
</figure>

### Inline templating[¶](#inline-templating "Permanent link")

When `X-Template: yes` (aliases: `Template: yes`, `Tpl: yes`) or `?template=yes` is set, you can use Go templates in the `message` and `title` fields of your webhook payload.

Inline templates are most useful for templated one-off messages, or if you do not control the ntfy server (e.g., if you\'re using ntfy.sh). Consider using [pre-defined templates](#pre-defined-templates) or [custom templates](#custom-templates) instead, if you control the ntfy server, as templates are much easier to maintain.

Here\'s an **example for a Grafana alert**:

<figure>
<p><img src="../static/img/android-screenshot-template.jpg" width="500" alt="notification with actions" /></p>
<figcaption>Grafana webhook, formatted using templates</figcaption>
</figure>

This was sent using the following templates and payloads

Message templateTitle templateEncoded webhook URLGrafana-sent payload

    }
      }

      Values:
      }
        - }=}
      }
    }

    }

    # Additional URL encoding (see https://www.urlencoder.org/) is necessary for Grafana, 
    # and may be required for other tools too

    https://ntfy.sh/mytopic?tpl=1&t=%7B%7B.title%7D%7D&m=%7B%7Brange%20.alerts%7D%7D%7B%7B.annotations.summary%7D%7D%5Cn%5CnValues%3A%5Cn%7B%7Brange%20%24k%2C%24v%20%3A%3D%20.values%7D%7D-%20%7B%7B%24k%7D%7D%3D%7B%7B%24v%7D%7D%5Cn%7B%7Bend%7D%7D%7B%7Bend%7D%7D

    ,"annotations":,"startsAt":"2024-03-15T02:28:00Z","endsAt":"2024-03-15T02:42:00Z","generatorURL":"localhost:3000/alerting/grafana/NW9oDw-4z/view","fingerprint":"becbfb94bd81ef48","silenceURL":"localhost:3000/alerting/silence/new?alertmanager=grafana&matcher=alertname%3DLoad+avg+15m+too+high&matcher=grafana_folder%3DNode+alerts&matcher=instance%3D10.108.0.2%3A9100&matcher=job%3Dnode-exporter","dashboardURL":"","panelURL":"","values":,"valueString":"[ var='B' labels= value=18.98211314475876 ], [ var='C' labels= value=0 ]"}],"groupLabels":,"commonLabels":,"commonAnnotations":,"externalURL":"localhost:3000/","version":"1","groupKey":":","truncatedAlerts":0,"orgId":1,"title":"[RESOLVED] Load avg 15m too high Node alerts (10.108.0.2:9100 node-exporter)","state":"ok","message":"**Resolved**\n\nValue: B=18.98211314475876, C=0\nLabels:\n - alertname = Load avg 15m too high\n - grafana_folder = Node alerts\n - instance = 10.108.0.2:9100\n - job = node-exporter\nAnnotations:\n - summary = 15m load average too high\nSource: localhost:3000/alerting/grafana/NW9oDw-4z/view\nSilence: localhost:3000/alerting/silence/new?alertmanager=grafana&matcher=alertname%3DLoad+avg+15m+too+high&matcher=grafana_folder%3DNode+alerts&matcher=instance%3D10.108.0.2%3A9100&matcher=job%3Dnode-exporter\n"}

Here\'s an **easier example with a shorter JSON payload**:

Command line (curl)HTTPJavaScriptGoPowerShellPythonPHP

    # To use  in the URL without encoding, we need to turn off
    # curl's globbing using --globoff

    curl \
        --globoff \
        -d '}' \
        'ntfy.sh/mytopic?tpl=yes&t=}:+A+}+error+has+occurred&m=Error+message:+}'

    POST /mytopic?tpl=yes&t=}:+A+}+error+has+occurred&m=Error+message:+} HTTP/1.1
    Host: ntfy.sh

    }

    fetch('https://ntfy.sh/mytopic?tpl=yes&t=}:+A+}+error+has+occurred&m=Error+message:+}', }'
    })

    body := `}`
    uri := "https://ntfy.sh/mytopic?tpl=yes&t=}:+A+}+error+has+occurred&m=Error+message:+}"
    req, _ := http.NewRequest("POST", uri, strings.NewReader(body))
    http.DefaultClient.Do(req)

    $Request = @}:+A+}+error+has+occurred&m=Error+message:+}"
        Body = '}'
        ContentType = "application/json"
    }
    Invoke-RestMethod @Request

    requests.post(
        "https://ntfy.sh/mytopic?tpl=yes&t=}:+A+}+error+has+occurred&m=Error+message:+}",
        data='}'
    )

    file_get_contents("https://ntfy.sh/mytopic?tpl=yes&t=}:+A+}+error+has+occurred&m=Error+message:+}", false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' => "Content-Type: application/json",
            'content' => '}'
        ]
    ]));

This example uses the `message`/`m` and `title`/`t` query parameters, but obviously this also works with the corresponding `Message`/`Title` headers. It will send a notification with a title `phil-pc: A severe error has occurred` and a message `Error message: Disk has run out of space`.

### Template syntax[¶](#template-syntax "Permanent link")

ntfy uses [Go templates](https://pkg.go.dev/text/template) for its templates, which is arguably one of the most powerful, yet also one of the worst templating languages out there.

You can use the following features in your templates:

- Variables, e.g. `}` or `An error occurred: }`
- Conditionals (if/else, e.g. `}..}..}`, see [example](https://repeatit.io/#/share/eyJ0ZW1wbGF0ZSI6Ilt7ey5wdWxsX3JlcXVlc3QuaGVhZC5yZXBvLmZ1bGxfbmFtZX19XSBQdWxsIHJlcXVlc3Qge3tpZiBlcSAuYWN0aW9uIFwib3BlbmVkXCJ9fU9QRU5FRHt7ZWxzZX19Q0xPU0VEe3tlbmR9fToge3sucHVsbF9yZXF1ZXN0LnRpdGxlfX0iLCJpbnB1dCI6IntcbiAgXCJhY3Rpb25cIjogXCJvcGVuZWRcIixcbiAgXCJudW1iZXJcIjogMSxcbiAgXCJwdWxsX3JlcXVlc3RcIjoge1xuICAgIFwidXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9wdWxscy8xXCIsXG4gICAgXCJpZFwiOiAxNzgzNDIwOTcyLFxuICAgIFwibm9kZV9pZFwiOiBcIlBSX2t3RE9IQWJkbzg1cVROZ3NcIixcbiAgICBcImh0bWxfdXJsXCI6IFwiaHR0cHM6Ly9naXRodWIuY29tL2JpbndpZWRlcmhpZXIvZGFiYmxlL3B1bGwvMVwiLFxuICAgIFwiZGlmZl91cmxcIjogXCJodHRwczovL2dpdGh1Yi5jb20vYmlud2llZGVyaGllci9kYWJibGUvcHVsbC8xLmRpZmZcIixcbiAgICBcInBhdGNoX3VybFwiOiBcImh0dHBzOi8vZ2l0aHViLmNvbS9iaW53aWVkZXJoaWVyL2RhYmJsZS9wdWxsLzEucGF0Y2hcIixcbiAgICBcImlzc3VlX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvaXNzdWVzLzFcIixcbiAgICBcIm51bWJlclwiOiAxLFxuICAgIFwic3RhdGVcIjogXCJvcGVuXCIsXG4gICAgXCJsb2NrZWRcIjogZmFsc2UsXG4gICAgXCJ0aXRsZVwiOiBcIkEgc2FtcGxlIFBSIGZyb20gUGhpbFwiLFxuICAgIFwidXNlclwiOiB7XG4gICAgICBcImxvZ2luXCI6IFwiYmlud2llZGVyaGllclwiLFxuICAgICAgXCJpZFwiOiA2NjQ1OTcsXG4gICAgICBcIm5vZGVfaWRcIjogXCJNRFE2VlhObGNqWTJORFU1Tnc9PVwiLFxuICAgICAgXCJhdmF0YXJfdXJsXCI6IFwiaHR0cHM6Ly9hdmF0YXJzLmdpdGh1YnVzZXJjb250ZW50LmNvbS91LzY2NDU5Nz92PTRcIixcbiAgICAgIFwiZ3JhdmF0YXJfaWRcIjogXCJcIixcbiAgICAgIFwidXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyXCIsXG4gICAgICBcImh0bWxfdXJsXCI6IFwiaHR0cHM6Ly9naXRodWIuY29tL2JpbndpZWRlcmhpZXJcIixcbiAgICAgIFwiZm9sbG93ZXJzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9mb2xsb3dlcnNcIixcbiAgICAgIFwiZm9sbG93aW5nX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9mb2xsb3dpbmd7L290aGVyX3VzZXJ9XCIsXG4gICAgICBcImdpc3RzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9naXN0c3svZ2lzdF9pZH1cIixcbiAgICAgIFwic3RhcnJlZF91cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvc3RhcnJlZHsvb3duZXJ9ey9yZXBvfVwiLFxuICAgICAgXCJzdWJzY3JpcHRpb25zX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9zdWJzY3JpcHRpb25zXCIsXG4gICAgICBcIm9yZ2FuaXphdGlvbnNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL29yZ3NcIixcbiAgICAgIFwicmVwb3NfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL3JlcG9zXCIsXG4gICAgICBcImV2ZW50c191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvZXZlbnRzey9wcml2YWN5fVwiLFxuICAgICAgXCJyZWNlaXZlZF9ldmVudHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL3JlY2VpdmVkX2V2ZW50c1wiLFxuICAgICAgXCJ0eXBlXCI6IFwiVXNlclwiLFxuICAgICAgXCJzaXRlX2FkbWluXCI6IGZhbHNlXG4gICAgfSxcbiAgICBcImJvZHlcIjogbnVsbCxcbiAgICBcImNyZWF0ZWRfYXRcIjogXCIyMDI0LTAzLTIxVDAyOjUyOjA5WlwiLFxuICAgIFwidXBkYXRlZF9hdFwiOiBcIjIwMjQtMDMtMjFUMDI6NTI6MDlaXCIsXG4gICAgXCJjbG9zZWRfYXRcIjogbnVsbCxcbiAgICBcIm1lcmdlZF9hdFwiOiBudWxsLFxuICAgIFwibWVyZ2VfY29tbWl0X3NoYVwiOiBudWxsLFxuICAgIFwiYXNzaWduZWVcIjogbnVsbCxcbiAgICBcImFzc2lnbmVlc1wiOiBbXSxcbiAgICBcInJlcXVlc3RlZF9yZXZpZXdlcnNcIjogW10sXG4gICAgXCJyZXF1ZXN0ZWRfdGVhbXNcIjogW10sXG4gICAgXCJsYWJlbHNcIjogW10sXG4gICAgXCJtaWxlc3RvbmVcIjogbnVsbCxcbiAgICBcImRyYWZ0XCI6IGZhbHNlLFxuICAgIFwiY29tbWl0c191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL3B1bGxzLzEvY29tbWl0c1wiLFxuICAgIFwicmV2aWV3X2NvbW1lbnRzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvcHVsbHMvMS9jb21tZW50c1wiLFxuICAgIFwicmV2aWV3X2NvbW1lbnRfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9wdWxscy9jb21tZW50c3svbnVtYmVyfVwiLFxuICAgIFwiY29tbWVudHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9pc3N1ZXMvMS9jb21tZW50c1wiLFxuICAgIFwic3RhdHVzZXNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9zdGF0dXNlcy81NzAzODQyY2M1NzE1ZWQxZTM1OGQyM2ViYjY5M2RiMDk3NDdhZTliXCIsXG4gICAgXCJoZWFkXCI6IHtcbiAgICAgIFwibGFiZWxcIjogXCJiaW53aWVkZXJoaWVyOmFhXCIsXG4gICAgICBcInJlZlwiOiBcImFhXCIsXG4gICAgICBcInNoYVwiOiBcIjU3MDM4NDJjYzU3MTVlZDFlMzU4ZDIzZWJiNjkzZGIwOTc0N2FlOWJcIixcbiAgICAgIFwidXNlclwiOiB7XG4gICAgICAgIFwibG9naW5cIjogXCJiaW53aWVkZXJoaWVyXCIsXG4gICAgICAgIFwiaWRcIjogNjY0NTk3LFxuICAgICAgICBcIm5vZGVfaWRcIjogXCJNRFE2VlhObGNqWTJORFU1Tnc9PVwiLFxuICAgICAgICBcImF2YXRhcl91cmxcIjogXCJodHRwczovL2F2YXRhcnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3UvNjY0NTk3P3Y9NFwiLFxuICAgICAgICBcImdyYXZhdGFyX2lkXCI6IFwiXCIsXG4gICAgICAgIFwidXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyXCIsXG4gICAgICAgIFwiaHRtbF91cmxcIjogXCJodHRwczovL2dpdGh1Yi5jb20vYmlud2llZGVyaGllclwiLFxuICAgICAgICBcImZvbGxvd2Vyc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvZm9sbG93ZXJzXCIsXG4gICAgICAgIFwiZm9sbG93aW5nX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9mb2xsb3dpbmd7L290aGVyX3VzZXJ9XCIsXG4gICAgICAgIFwiZ2lzdHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL2dpc3Rzey9naXN0X2lkfVwiLFxuICAgICAgICBcInN0YXJyZWRfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL3N0YXJyZWR7L293bmVyfXsvcmVwb31cIixcbiAgICAgICAgXCJzdWJzY3JpcHRpb25zX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9zdWJzY3JpcHRpb25zXCIsXG4gICAgICAgIFwib3JnYW5pemF0aW9uc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvb3Jnc1wiLFxuICAgICAgICBcInJlcG9zX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9yZXBvc1wiLFxuICAgICAgICBcImV2ZW50c191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvZXZlbnRzey9wcml2YWN5fVwiLFxuICAgICAgICBcInJlY2VpdmVkX2V2ZW50c191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvcmVjZWl2ZWRfZXZlbnRzXCIsXG4gICAgICAgIFwidHlwZVwiOiBcIlVzZXJcIixcbiAgICAgICAgXCJzaXRlX2FkbWluXCI6IGZhbHNlXG4gICAgICB9LFxuICAgICAgXCJyZXBvXCI6IHtcbiAgICAgICAgXCJpZFwiOiA0NzAyMTIwMDMsXG4gICAgICAgIFwibm9kZV9pZFwiOiBcIlJfa2dET0hBYmRvd1wiLFxuICAgICAgICBcIm5hbWVcIjogXCJkYWJibGVcIixcbiAgICAgICAgXCJmdWxsX25hbWVcIjogXCJiaW53aWVkZXJoaWVyL2RhYmJsZVwiLFxuICAgICAgICBcInByaXZhdGVcIjogZmFsc2UsXG4gICAgICAgIFwib3duZXJcIjoge1xuICAgICAgICAgIFwibG9naW5cIjogXCJiaW53aWVkZXJoaWVyXCIsXG4gICAgICAgICAgXCJpZFwiOiA2NjQ1OTcsXG4gICAgICAgICAgXCJub2RlX2lkXCI6IFwiTURRNlZYTmxjalkyTkRVNU53PT1cIixcbiAgICAgICAgICBcImF2YXRhcl91cmxcIjogXCJodHRwczovL2F2YXRhcnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3UvNjY0NTk3P3Y9NFwiLFxuICAgICAgICAgIFwiZ3JhdmF0YXJfaWRcIjogXCJcIixcbiAgICAgICAgICBcInVybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllclwiLFxuICAgICAgICAgIFwiaHRtbF91cmxcIjogXCJodHRwczovL2dpdGh1Yi5jb20vYmlud2llZGVyaGllclwiLFxuICAgICAgICAgIFwiZm9sbG93ZXJzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9mb2xsb3dlcnNcIixcbiAgICAgICAgICBcImZvbGxvd2luZ191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvZm9sbG93aW5ney9vdGhlcl91c2VyfVwiLFxuICAgICAgICAgIFwiZ2lzdHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL2dpc3Rzey9naXN0X2lkfVwiLFxuICAgICAgICAgIFwic3RhcnJlZF91cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvc3RhcnJlZHsvb3duZXJ9ey9yZXBvfVwiLFxuICAgICAgICAgIFwic3Vic2NyaXB0aW9uc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvc3Vic2NyaXB0aW9uc1wiLFxuICAgICAgICAgIFwib3JnYW5pemF0aW9uc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvb3Jnc1wiLFxuICAgICAgICAgIFwicmVwb3NfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL3JlcG9zXCIsXG4gICAgICAgICAgXCJldmVudHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL2V2ZW50c3svcHJpdmFjeX1cIixcbiAgICAgICAgICBcInJlY2VpdmVkX2V2ZW50c191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvcmVjZWl2ZWRfZXZlbnRzXCIsXG4gICAgICAgICAgXCJ0eXBlXCI6IFwiVXNlclwiLFxuICAgICAgICAgIFwic2l0ZV9hZG1pblwiOiBmYWxzZVxuICAgICAgICB9LFxuICAgICAgICBcImh0bWxfdXJsXCI6IFwiaHR0cHM6Ly9naXRodWIuY29tL2JpbndpZWRlcmhpZXIvZGFiYmxlXCIsXG4gICAgICAgIFwiZGVzY3JpcHRpb25cIjogXCJBIHJlcG8gZm9yIGRhYmJsaW5nXCIsXG4gICAgICAgIFwiZm9ya1wiOiBmYWxzZSxcbiAgICAgICAgXCJ1cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlXCIsXG4gICAgICAgIFwiZm9ya3NfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9mb3Jrc1wiLFxuICAgICAgICBcImtleXNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9rZXlzey9rZXlfaWR9XCIsXG4gICAgICAgIFwiY29sbGFib3JhdG9yc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2NvbGxhYm9yYXRvcnN7L2NvbGxhYm9yYXRvcn1cIixcbiAgICAgICAgXCJ0ZWFtc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL3RlYW1zXCIsXG4gICAgICAgIFwiaG9va3NfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9ob29rc1wiLFxuICAgICAgICBcImlzc3VlX2V2ZW50c191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2lzc3Vlcy9ldmVudHN7L251bWJlcn1cIixcbiAgICAgICAgXCJldmVudHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9ldmVudHNcIixcbiAgICAgICAgXCJhc3NpZ25lZXNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9hc3NpZ25lZXN7L3VzZXJ9XCIsXG4gICAgICAgIFwiYnJhbmNoZXNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9icmFuY2hlc3svYnJhbmNofVwiLFxuICAgICAgICBcInRhZ3NfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS90YWdzXCIsXG4gICAgICAgIFwiYmxvYnNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9naXQvYmxvYnN7L3NoYX1cIixcbiAgICAgICAgXCJnaXRfdGFnc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2dpdC90YWdzey9zaGF9XCIsXG4gICAgICAgIFwiZ2l0X3JlZnNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9naXQvcmVmc3svc2hhfVwiLFxuICAgICAgICBcInRyZWVzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvZ2l0L3RyZWVzey9zaGF9XCIsXG4gICAgICAgIFwic3RhdHVzZXNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9zdGF0dXNlcy97c2hhfVwiLFxuICAgICAgICBcImxhbmd1YWdlc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2xhbmd1YWdlc1wiLFxuICAgICAgICBcInN0YXJnYXplcnNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9zdGFyZ2F6ZXJzXCIsXG4gICAgICAgIFwiY29udHJpYnV0b3JzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvY29udHJpYnV0b3JzXCIsXG4gICAgICAgIFwic3Vic2NyaWJlcnNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9zdWJzY3JpYmVyc1wiLFxuICAgICAgICBcInN1YnNjcmlwdGlvbl91cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL3N1YnNjcmlwdGlvblwiLFxuICAgICAgICBcImNvbW1pdHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9jb21taXRzey9zaGF9XCIsXG4gICAgICAgIFwiZ2l0X2NvbW1pdHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9naXQvY29tbWl0c3svc2hhfVwiLFxuICAgICAgICBcImNvbW1lbnRzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvY29tbWVudHN7L251bWJlcn1cIixcbiAgICAgICAgXCJpc3N1ZV9jb21tZW50X3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvaXNzdWVzL2NvbW1lbnRzey9udW1iZXJ9XCIsXG4gICAgICAgIFwiY29udGVudHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9jb250ZW50cy97K3BhdGh9XCIsXG4gICAgICAgIFwiY29tcGFyZV91cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2NvbXBhcmUve2Jhc2V9Li4ue2hlYWR9XCIsXG4gICAgICAgIFwibWVyZ2VzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvbWVyZ2VzXCIsXG4gICAgICAgIFwiYXJjaGl2ZV91cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL3thcmNoaXZlX2Zvcm1hdH17L3JlZn1cIixcbiAgICAgICAgXCJkb3dubG9hZHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9kb3dubG9hZHNcIixcbiAgICAgICAgXCJpc3N1ZXNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9pc3N1ZXN7L251bWJlcn1cIixcbiAgICAgICAgXCJwdWxsc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL3B1bGxzey9udW1iZXJ9XCIsXG4gICAgICAgIFwibWlsZXN0b25lc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL21pbGVzdG9uZXN7L251bWJlcn1cIixcbiAgICAgICAgXCJub3RpZmljYXRpb25zX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvbm90aWZpY2F0aW9uc3s/c2luY2UsYWxsLHBhcnRpY2lwYXRpbmd9XCIsXG4gICAgICAgIFwibGFiZWxzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvbGFiZWxzey9uYW1lfVwiLFxuICAgICAgICBcInJlbGVhc2VzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvcmVsZWFzZXN7L2lkfVwiLFxuICAgICAgICBcImRlcGxveW1lbnRzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvZGVwbG95bWVudHNcIixcbiAgICAgICAgXCJjcmVhdGVkX2F0XCI6IFwiMjAyMi0wMy0xNVQxNTowNjoxN1pcIixcbiAgICAgICAgXCJ1cGRhdGVkX2F0XCI6IFwiMjAyMi0wMy0xNVQxNTowNjoxN1pcIixcbiAgICAgICAgXCJwdXNoZWRfYXRcIjogXCIyMDI0LTAzLTIxVDAyOjUyOjEwWlwiLFxuICAgICAgICBcImdpdF91cmxcIjogXCJnaXQ6Ly9naXRodWIuY29tL2JpbndpZWRlcmhpZXIvZGFiYmxlLmdpdFwiLFxuICAgICAgICBcInNzaF91cmxcIjogXCJnaXRAZ2l0aHViLmNvbTpiaW53aWVkZXJoaWVyL2RhYmJsZS5naXRcIixcbiAgICAgICAgXCJjbG9uZV91cmxcIjogXCJodHRwczovL2dpdGh1Yi5jb20vYmlud2llZGVyaGllci9kYWJibGUuZ2l0XCIsXG4gICAgICAgIFwic3ZuX3VybFwiOiBcImh0dHBzOi8vZ2l0aHViLmNvbS9iaW53aWVkZXJoaWVyL2RhYmJsZVwiLFxuICAgICAgICBcImhvbWVwYWdlXCI6IG51bGwsXG4gICAgICAgIFwic2l6ZVwiOiAxLFxuICAgICAgICBcInN0YXJnYXplcnNfY291bnRcIjogMCxcbiAgICAgICAgXCJ3YXRjaGVyc19jb3VudFwiOiAwLFxuICAgICAgICBcImxhbmd1YWdlXCI6IG51bGwsXG4gICAgICAgIFwiaGFzX2lzc3Vlc1wiOiB0cnVlLFxuICAgICAgICBcImhhc19wcm9qZWN0c1wiOiB0cnVlLFxuICAgICAgICBcImhhc19kb3dubG9hZHNcIjogdHJ1ZSxcbiAgICAgICAgXCJoYXNfd2lraVwiOiB0cnVlLFxuICAgICAgICBcImhhc19wYWdlc1wiOiBmYWxzZSxcbiAgICAgICAgXCJoYXNfZGlzY3Vzc2lvbnNcIjogZmFsc2UsXG4gICAgICAgIFwiZm9ya3NfY291bnRcIjogMCxcbiAgICAgICAgXCJtaXJyb3JfdXJsXCI6IG51bGwsXG4gICAgICAgIFwiYXJjaGl2ZWRcIjogZmFsc2UsXG4gICAgICAgIFwiZGlzYWJsZWRcIjogZmFsc2UsXG4gICAgICAgIFwib3Blbl9pc3N1ZXNfY291bnRcIjogMSxcbiAgICAgICAgXCJsaWNlbnNlXCI6IG51bGwsXG4gICAgICAgIFwiYWxsb3dfZm9ya2luZ1wiOiB0cnVlLFxuICAgICAgICBcImlzX3RlbXBsYXRlXCI6IGZhbHNlLFxuICAgICAgICBcIndlYl9jb21taXRfc2lnbm9mZl9yZXF1aXJlZFwiOiBmYWxzZSxcbiAgICAgICAgXCJ0b3BpY3NcIjogW10sXG4gICAgICAgIFwidmlzaWJpbGl0eVwiOiBcInB1YmxpY1wiLFxuICAgICAgICBcImZvcmtzXCI6IDAsXG4gICAgICAgIFwib3Blbl9pc3N1ZXNcIjogMSxcbiAgICAgICAgXCJ3YXRjaGVyc1wiOiAwLFxuICAgICAgICBcImRlZmF1bHRfYnJhbmNoXCI6IFwibWFpblwiLFxuICAgICAgICBcImFsbG93X3NxdWFzaF9tZXJnZVwiOiB0cnVlLFxuICAgICAgICBcImFsbG93X21lcmdlX2NvbW1pdFwiOiB0cnVlLFxuICAgICAgICBcImFsbG93X3JlYmFzZV9tZXJnZVwiOiB0cnVlLFxuICAgICAgICBcImFsbG93X2F1dG9fbWVyZ2VcIjogZmFsc2UsXG4gICAgICAgIFwiZGVsZXRlX2JyYW5jaF9vbl9tZXJnZVwiOiBmYWxzZSxcbiAgICAgICAgXCJhbGxvd191cGRhdGVfYnJhbmNoXCI6IGZhbHNlLFxuICAgICAgICBcInVzZV9zcXVhc2hfcHJfdGl0bGVfYXNfZGVmYXVsdFwiOiBmYWxzZSxcbiAgICAgICAgXCJzcXVhc2hfbWVyZ2VfY29tbWl0X21lc3NhZ2VcIjogXCJDT01NSVRfTUVTU0FHRVNcIixcbiAgICAgICAgXCJzcXVhc2hfbWVyZ2VfY29tbWl0X3RpdGxlXCI6IFwiQ09NTUlUX09SX1BSX1RJVExFXCIsXG4gICAgICAgIFwibWVyZ2VfY29tbWl0X21lc3NhZ2VcIjogXCJQUl9USVRMRVwiLFxuICAgICAgICBcIm1lcmdlX2NvbW1pdF90aXRsZVwiOiBcIk1FUkdFX01FU1NBR0VcIlxuICAgICAgfVxuICAgIH0sXG4gICAgXCJiYXNlXCI6IHtcbiAgICAgIFwibGFiZWxcIjogXCJiaW53aWVkZXJoaWVyOm1haW5cIixcbiAgICAgIFwicmVmXCI6IFwibWFpblwiLFxuICAgICAgXCJzaGFcIjogXCI3MmQ5MzFhMjBiYjgzZDEyM2FiNDVhY2NhZjc2MTE1MGM4YjAxMjExXCIsXG4gICAgICBcInVzZXJcIjoge1xuICAgICAgICBcImxvZ2luXCI6IFwiYmlud2llZGVyaGllclwiLFxuICAgICAgICBcImlkXCI6IDY2NDU5NyxcbiAgICAgICAgXCJub2RlX2lkXCI6IFwiTURRNlZYTmxjalkyTkRVNU53PT1cIixcbiAgICAgICAgXCJhdmF0YXJfdXJsXCI6IFwiaHR0cHM6Ly9hdmF0YXJzLmdpdGh1YnVzZXJjb250ZW50LmNvbS91LzY2NDU5Nz92PTRcIixcbiAgICAgICAgXCJncmF2YXRhcl9pZFwiOiBcIlwiLFxuICAgICAgICBcInVybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllclwiLFxuICAgICAgICBcImh0bWxfdXJsXCI6IFwiaHR0cHM6Ly9naXRodWIuY29tL2JpbndpZWRlcmhpZXJcIixcbiAgICAgICAgXCJmb2xsb3dlcnNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL2ZvbGxvd2Vyc1wiLFxuICAgICAgICBcImZvbGxvd2luZ191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvZm9sbG93aW5ney9vdGhlcl91c2VyfVwiLFxuICAgICAgICBcImdpc3RzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9naXN0c3svZ2lzdF9pZH1cIixcbiAgICAgICAgXCJzdGFycmVkX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9zdGFycmVkey9vd25lcn17L3JlcG99XCIsXG4gICAgICAgIFwic3Vic2NyaXB0aW9uc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvc3Vic2NyaXB0aW9uc1wiLFxuICAgICAgICBcIm9yZ2FuaXphdGlvbnNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL29yZ3NcIixcbiAgICAgICAgXCJyZXBvc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvcmVwb3NcIixcbiAgICAgICAgXCJldmVudHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL2V2ZW50c3svcHJpdmFjeX1cIixcbiAgICAgICAgXCJyZWNlaXZlZF9ldmVudHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL3JlY2VpdmVkX2V2ZW50c1wiLFxuICAgICAgICBcInR5cGVcIjogXCJVc2VyXCIsXG4gICAgICAgIFwic2l0ZV9hZG1pblwiOiBmYWxzZVxuICAgICAgfSxcbiAgICAgIFwicmVwb1wiOiB7XG4gICAgICAgIFwiaWRcIjogNDcwMjEyMDAzLFxuICAgICAgICBcIm5vZGVfaWRcIjogXCJSX2tnRE9IQWJkb3dcIixcbiAgICAgICAgXCJuYW1lXCI6IFwiZGFiYmxlXCIsXG4gICAgICAgIFwiZnVsbF9uYW1lXCI6IFwiYmlud2llZGVyaGllci9kYWJibGVcIixcbiAgICAgICAgXCJwcml2YXRlXCI6IGZhbHNlLFxuICAgICAgICBcIm93bmVyXCI6IHtcbiAgICAgICAgICBcImxvZ2luXCI6IFwiYmlud2llZGVyaGllclwiLFxuICAgICAgICAgIFwiaWRcIjogNjY0NTk3LFxuICAgICAgICAgIFwibm9kZV9pZFwiOiBcIk1EUTZWWE5sY2pZMk5EVTVOdz09XCIsXG4gICAgICAgICAgXCJhdmF0YXJfdXJsXCI6IFwiaHR0cHM6Ly9hdmF0YXJzLmdpdGh1YnVzZXJjb250ZW50LmNvbS91LzY2NDU5Nz92PTRcIixcbiAgICAgICAgICBcImdyYXZhdGFyX2lkXCI6IFwiXCIsXG4gICAgICAgICAgXCJ1cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXJcIixcbiAgICAgICAgICBcImh0bWxfdXJsXCI6IFwiaHR0cHM6Ly9naXRodWIuY29tL2JpbndpZWRlcmhpZXJcIixcbiAgICAgICAgICBcImZvbGxvd2Vyc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvZm9sbG93ZXJzXCIsXG4gICAgICAgICAgXCJmb2xsb3dpbmdfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL2ZvbGxvd2luZ3svb3RoZXJfdXNlcn1cIixcbiAgICAgICAgICBcImdpc3RzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9naXN0c3svZ2lzdF9pZH1cIixcbiAgICAgICAgICBcInN0YXJyZWRfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL3N0YXJyZWR7L293bmVyfXsvcmVwb31cIixcbiAgICAgICAgICBcInN1YnNjcmlwdGlvbnNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL3N1YnNjcmlwdGlvbnNcIixcbiAgICAgICAgICBcIm9yZ2FuaXphdGlvbnNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL29yZ3NcIixcbiAgICAgICAgICBcInJlcG9zX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9yZXBvc1wiLFxuICAgICAgICAgIFwiZXZlbnRzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9ldmVudHN7L3ByaXZhY3l9XCIsXG4gICAgICAgICAgXCJyZWNlaXZlZF9ldmVudHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL3JlY2VpdmVkX2V2ZW50c1wiLFxuICAgICAgICAgIFwidHlwZVwiOiBcIlVzZXJcIixcbiAgICAgICAgICBcInNpdGVfYWRtaW5cIjogZmFsc2VcbiAgICAgICAgfSxcbiAgICAgICAgXCJodG1sX3VybFwiOiBcImh0dHBzOi8vZ2l0aHViLmNvbS9iaW53aWVkZXJoaWVyL2RhYmJsZVwiLFxuICAgICAgICBcImRlc2NyaXB0aW9uXCI6IFwiQSByZXBvIGZvciBkYWJibGluZ1wiLFxuICAgICAgICBcImZvcmtcIjogZmFsc2UsXG4gICAgICAgIFwidXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZVwiLFxuICAgICAgICBcImZvcmtzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvZm9ya3NcIixcbiAgICAgICAgXCJrZXlzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUva2V5c3sva2V5X2lkfVwiLFxuICAgICAgICBcImNvbGxhYm9yYXRvcnNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9jb2xsYWJvcmF0b3Jzey9jb2xsYWJvcmF0b3J9XCIsXG4gICAgICAgIFwidGVhbXNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS90ZWFtc1wiLFxuICAgICAgICBcImhvb2tzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvaG9va3NcIixcbiAgICAgICAgXCJpc3N1ZV9ldmVudHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9pc3N1ZXMvZXZlbnRzey9udW1iZXJ9XCIsXG4gICAgICAgIFwiZXZlbnRzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvZXZlbnRzXCIsXG4gICAgICAgIFwiYXNzaWduZWVzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvYXNzaWduZWVzey91c2VyfVwiLFxuICAgICAgICBcImJyYW5jaGVzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvYnJhbmNoZXN7L2JyYW5jaH1cIixcbiAgICAgICAgXCJ0YWdzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvdGFnc1wiLFxuICAgICAgICBcImJsb2JzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvZ2l0L2Jsb2Jzey9zaGF9XCIsXG4gICAgICAgIFwiZ2l0X3RhZ3NfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9naXQvdGFnc3svc2hhfVwiLFxuICAgICAgICBcImdpdF9yZWZzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvZ2l0L3JlZnN7L3NoYX1cIixcbiAgICAgICAgXCJ0cmVlc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2dpdC90cmVlc3svc2hhfVwiLFxuICAgICAgICBcInN0YXR1c2VzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvc3RhdHVzZXMve3NoYX1cIixcbiAgICAgICAgXCJsYW5ndWFnZXNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9sYW5ndWFnZXNcIixcbiAgICAgICAgXCJzdGFyZ2F6ZXJzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvc3RhcmdhemVyc1wiLFxuICAgICAgICBcImNvbnRyaWJ1dG9yc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2NvbnRyaWJ1dG9yc1wiLFxuICAgICAgICBcInN1YnNjcmliZXJzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvc3Vic2NyaWJlcnNcIixcbiAgICAgICAgXCJzdWJzY3JpcHRpb25fdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9zdWJzY3JpcHRpb25cIixcbiAgICAgICAgXCJjb21taXRzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvY29tbWl0c3svc2hhfVwiLFxuICAgICAgICBcImdpdF9jb21taXRzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvZ2l0L2NvbW1pdHN7L3NoYX1cIixcbiAgICAgICAgXCJjb21tZW50c191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2NvbW1lbnRzey9udW1iZXJ9XCIsXG4gICAgICAgIFwiaXNzdWVfY29tbWVudF91cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2lzc3Vlcy9jb21tZW50c3svbnVtYmVyfVwiLFxuICAgICAgICBcImNvbnRlbnRzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvY29udGVudHMveytwYXRofVwiLFxuICAgICAgICBcImNvbXBhcmVfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9jb21wYXJlL3tiYXNlfS4uLntoZWFkfVwiLFxuICAgICAgICBcIm1lcmdlc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL21lcmdlc1wiLFxuICAgICAgICBcImFyY2hpdmVfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS97YXJjaGl2ZV9mb3JtYXR9ey9yZWZ9XCIsXG4gICAgICAgIFwiZG93bmxvYWRzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvZG93bmxvYWRzXCIsXG4gICAgICAgIFwiaXNzdWVzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvaXNzdWVzey9udW1iZXJ9XCIsXG4gICAgICAgIFwicHVsbHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9wdWxsc3svbnVtYmVyfVwiLFxuICAgICAgICBcIm1pbGVzdG9uZXNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9taWxlc3RvbmVzey9udW1iZXJ9XCIsXG4gICAgICAgIFwibm90aWZpY2F0aW9uc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL25vdGlmaWNhdGlvbnN7P3NpbmNlLGFsbCxwYXJ0aWNpcGF0aW5nfVwiLFxuICAgICAgICBcImxhYmVsc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2xhYmVsc3svbmFtZX1cIixcbiAgICAgICAgXCJyZWxlYXNlc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL3JlbGVhc2Vzey9pZH1cIixcbiAgICAgICAgXCJkZXBsb3ltZW50c191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2RlcGxveW1lbnRzXCIsXG4gICAgICAgIFwiY3JlYXRlZF9hdFwiOiBcIjIwMjItMDMtMTVUMTU6MDY6MTdaXCIsXG4gICAgICAgIFwidXBkYXRlZF9hdFwiOiBcIjIwMjItMDMtMTVUMTU6MDY6MTdaXCIsXG4gICAgICAgIFwicHVzaGVkX2F0XCI6IFwiMjAyNC0wMy0yMVQwMjo1MjoxMFpcIixcbiAgICAgICAgXCJnaXRfdXJsXCI6IFwiZ2l0Oi8vZ2l0aHViLmNvbS9iaW53aWVkZXJoaWVyL2RhYmJsZS5naXRcIixcbiAgICAgICAgXCJzc2hfdXJsXCI6IFwiZ2l0QGdpdGh1Yi5jb206Ymlud2llZGVyaGllci9kYWJibGUuZ2l0XCIsXG4gICAgICAgIFwiY2xvbmVfdXJsXCI6IFwiaHR0cHM6Ly9naXRodWIuY29tL2JpbndpZWRlcmhpZXIvZGFiYmxlLmdpdFwiLFxuICAgICAgICBcInN2bl91cmxcIjogXCJodHRwczovL2dpdGh1Yi5jb20vYmlud2llZGVyaGllci9kYWJibGVcIixcbiAgICAgICAgXCJob21lcGFnZVwiOiBudWxsLFxuICAgICAgICBcInNpemVcIjogMSxcbiAgICAgICAgXCJzdGFyZ2F6ZXJzX2NvdW50XCI6IDAsXG4gICAgICAgIFwid2F0Y2hlcnNfY291bnRcIjogMCxcbiAgICAgICAgXCJsYW5ndWFnZVwiOiBudWxsLFxuICAgICAgICBcImhhc19pc3N1ZXNcIjogdHJ1ZSxcbiAgICAgICAgXCJoYXNfcHJvamVjdHNcIjogdHJ1ZSxcbiAgICAgICAgXCJoYXNfZG93bmxvYWRzXCI6IHRydWUsXG4gICAgICAgIFwiaGFzX3dpa2lcIjogdHJ1ZSxcbiAgICAgICAgXCJoYXNfcGFnZXNcIjogZmFsc2UsXG4gICAgICAgIFwiaGFzX2Rpc2N1c3Npb25zXCI6IGZhbHNlLFxuICAgICAgICBcImZvcmtzX2NvdW50XCI6IDAsXG4gICAgICAgIFwibWlycm9yX3VybFwiOiBudWxsLFxuICAgICAgICBcImFyY2hpdmVkXCI6IGZhbHNlLFxuICAgICAgICBcImRpc2FibGVkXCI6IGZhbHNlLFxuICAgICAgICBcIm9wZW5faXNzdWVzX2NvdW50XCI6IDEsXG4gICAgICAgIFwibGljZW5zZVwiOiBudWxsLFxuICAgICAgICBcImFsbG93X2ZvcmtpbmdcIjogdHJ1ZSxcbiAgICAgICAgXCJpc190ZW1wbGF0ZVwiOiBmYWxzZSxcbiAgICAgICAgXCJ3ZWJfY29tbWl0X3NpZ25vZmZfcmVxdWlyZWRcIjogZmFsc2UsXG4gICAgICAgIFwidG9waWNzXCI6IFtdLFxuICAgICAgICBcInZpc2liaWxpdHlcIjogXCJwdWJsaWNcIixcbiAgICAgICAgXCJmb3Jrc1wiOiAwLFxuICAgICAgICBcIm9wZW5faXNzdWVzXCI6IDEsXG4gICAgICAgIFwid2F0Y2hlcnNcIjogMCxcbiAgICAgICAgXCJkZWZhdWx0X2JyYW5jaFwiOiBcIm1haW5cIixcbiAgICAgICAgXCJhbGxvd19zcXVhc2hfbWVyZ2VcIjogdHJ1ZSxcbiAgICAgICAgXCJhbGxvd19tZXJnZV9jb21taXRcIjogdHJ1ZSxcbiAgICAgICAgXCJhbGxvd19yZWJhc2VfbWVyZ2VcIjogdHJ1ZSxcbiAgICAgICAgXCJhbGxvd19hdXRvX21lcmdlXCI6IGZhbHNlLFxuICAgICAgICBcImRlbGV0ZV9icmFuY2hfb25fbWVyZ2VcIjogZmFsc2UsXG4gICAgICAgIFwiYWxsb3dfdXBkYXRlX2JyYW5jaFwiOiBmYWxzZSxcbiAgICAgICAgXCJ1c2Vfc3F1YXNoX3ByX3RpdGxlX2FzX2RlZmF1bHRcIjogZmFsc2UsXG4gICAgICAgIFwic3F1YXNoX21lcmdlX2NvbW1pdF9tZXNzYWdlXCI6IFwiQ09NTUlUX01FU1NBR0VTXCIsXG4gICAgICAgIFwic3F1YXNoX21lcmdlX2NvbW1pdF90aXRsZVwiOiBcIkNPTU1JVF9PUl9QUl9USVRMRVwiLFxuICAgICAgICBcIm1lcmdlX2NvbW1pdF9tZXNzYWdlXCI6IFwiUFJfVElUTEVcIixcbiAgICAgICAgXCJtZXJnZV9jb21taXRfdGl0bGVcIjogXCJNRVJHRV9NRVNTQUdFXCJcbiAgICAgIH1cbiAgICB9LFxuICAgIFwiX2xpbmtzXCI6IHtcbiAgICAgIFwic2VsZlwiOiB7XG4gICAgICAgIFwiaHJlZlwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvcHVsbHMvMVwiXG4gICAgICB9LFxuICAgICAgXCJodG1sXCI6IHtcbiAgICAgICAgXCJocmVmXCI6IFwiaHR0cHM6Ly9naXRodWIuY29tL2JpbndpZWRlcmhpZXIvZGFiYmxlL3B1bGwvMVwiXG4gICAgICB9LFxuICAgICAgXCJpc3N1ZVwiOiB7XG4gICAgICAgIFwiaHJlZlwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvaXNzdWVzLzFcIlxuICAgICAgfSxcbiAgICAgIFwiY29tbWVudHNcIjoge1xuICAgICAgICBcImhyZWZcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2lzc3Vlcy8xL2NvbW1lbnRzXCJcbiAgICAgIH0sXG4gICAgICBcInJldmlld19jb21tZW50c1wiOiB7XG4gICAgICAgIFwiaHJlZlwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvcHVsbHMvMS9jb21tZW50c1wiXG4gICAgICB9LFxuICAgICAgXCJyZXZpZXdfY29tbWVudFwiOiB7XG4gICAgICAgIFwiaHJlZlwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvcHVsbHMvY29tbWVudHN7L251bWJlcn1cIlxuICAgICAgfSxcbiAgICAgIFwiY29tbWl0c1wiOiB7XG4gICAgICAgIFwiaHJlZlwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvcHVsbHMvMS9jb21taXRzXCJcbiAgICAgIH0sXG4gICAgICBcInN0YXR1c2VzXCI6IHtcbiAgICAgICAgXCJocmVmXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9zdGF0dXNlcy81NzAzODQyY2M1NzE1ZWQxZTM1OGQyM2ViYjY5M2RiMDk3NDdhZTliXCJcbiAgICAgIH1cbiAgICB9LFxuICAgIFwiYXV0aG9yX2Fzc29jaWF0aW9uXCI6IFwiT1dORVJcIixcbiAgICBcImF1dG9fbWVyZ2VcIjogbnVsbCxcbiAgICBcImFjdGl2ZV9sb2NrX3JlYXNvblwiOiBudWxsLFxuICAgIFwibWVyZ2VkXCI6IGZhbHNlLFxuICAgIFwibWVyZ2VhYmxlXCI6IG51bGwsXG4gICAgXCJyZWJhc2VhYmxlXCI6IG51bGwsXG4gICAgXCJtZXJnZWFibGVfc3RhdGVcIjogXCJ1bmtub3duXCIsXG4gICAgXCJtZXJnZWRfYnlcIjogbnVsbCxcbiAgICBcImNvbW1lbnRzXCI6IDAsXG4gICAgXCJyZXZpZXdfY29tbWVudHNcIjogMCxcbiAgICBcIm1haW50YWluZXJfY2FuX21vZGlmeVwiOiBmYWxzZSxcbiAgICBcImNvbW1pdHNcIjogMSxcbiAgICBcImFkZGl0aW9uc1wiOiAxLFxuICAgIFwiZGVsZXRpb25zXCI6IDEsXG4gICAgXCJjaGFuZ2VkX2ZpbGVzXCI6IDFcbiAgfSxcbiAgXCJyZXBvc2l0b3J5XCI6IHtcbiAgICBcImlkXCI6IDQ3MDIxMjAwMyxcbiAgICBcIm5vZGVfaWRcIjogXCJSX2tnRE9IQWJkb3dcIixcbiAgICBcIm5hbWVcIjogXCJkYWJibGVcIixcbiAgICBcImZ1bGxfbmFtZVwiOiBcImJpbndpZWRlcmhpZXIvZGFiYmxlXCIsXG4gICAgXCJwcml2YXRlXCI6IGZhbHNlLFxuICAgIFwib3duZXJcIjoge1xuICAgICAgXCJsb2dpblwiOiBcImJpbndpZWRlcmhpZXJcIixcbiAgICAgIFwiaWRcIjogNjY0NTk3LFxuICAgICAgXCJub2RlX2lkXCI6IFwiTURRNlZYTmxjalkyTkRVNU53PT1cIixcbiAgICAgIFwiYXZhdGFyX3VybFwiOiBcImh0dHBzOi8vYXZhdGFycy5naXRodWJ1c2VyY29udGVudC5jb20vdS82NjQ1OTc/dj00XCIsXG4gICAgICBcImdyYXZhdGFyX2lkXCI6IFwiXCIsXG4gICAgICBcInVybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllclwiLFxuICAgICAgXCJodG1sX3VybFwiOiBcImh0dHBzOi8vZ2l0aHViLmNvbS9iaW53aWVkZXJoaWVyXCIsXG4gICAgICBcImZvbGxvd2Vyc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvZm9sbG93ZXJzXCIsXG4gICAgICBcImZvbGxvd2luZ191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvZm9sbG93aW5ney9vdGhlcl91c2VyfVwiLFxuICAgICAgXCJnaXN0c191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvZ2lzdHN7L2dpc3RfaWR9XCIsXG4gICAgICBcInN0YXJyZWRfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL3N0YXJyZWR7L293bmVyfXsvcmVwb31cIixcbiAgICAgIFwic3Vic2NyaXB0aW9uc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvc3Vic2NyaXB0aW9uc1wiLFxuICAgICAgXCJvcmdhbml6YXRpb25zX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9vcmdzXCIsXG4gICAgICBcInJlcG9zX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9yZXBvc1wiLFxuICAgICAgXCJldmVudHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL2V2ZW50c3svcHJpdmFjeX1cIixcbiAgICAgIFwicmVjZWl2ZWRfZXZlbnRzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9yZWNlaXZlZF9ldmVudHNcIixcbiAgICAgIFwidHlwZVwiOiBcIlVzZXJcIixcbiAgICAgIFwic2l0ZV9hZG1pblwiOiBmYWxzZVxuICAgIH0sXG4gICAgXCJodG1sX3VybFwiOiBcImh0dHBzOi8vZ2l0aHViLmNvbS9iaW53aWVkZXJoaWVyL2RhYmJsZVwiLFxuICAgIFwiZGVzY3JpcHRpb25cIjogXCJBIHJlcG8gZm9yIGRhYmJsaW5nXCIsXG4gICAgXCJmb3JrXCI6IGZhbHNlLFxuICAgIFwidXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZVwiLFxuICAgIFwiZm9ya3NfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9mb3Jrc1wiLFxuICAgIFwia2V5c191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2tleXN7L2tleV9pZH1cIixcbiAgICBcImNvbGxhYm9yYXRvcnNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9jb2xsYWJvcmF0b3Jzey9jb2xsYWJvcmF0b3J9XCIsXG4gICAgXCJ0ZWFtc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL3RlYW1zXCIsXG4gICAgXCJob29rc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2hvb2tzXCIsXG4gICAgXCJpc3N1ZV9ldmVudHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9pc3N1ZXMvZXZlbnRzey9udW1iZXJ9XCIsXG4gICAgXCJldmVudHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9ldmVudHNcIixcbiAgICBcImFzc2lnbmVlc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2Fzc2lnbmVlc3svdXNlcn1cIixcbiAgICBcImJyYW5jaGVzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvYnJhbmNoZXN7L2JyYW5jaH1cIixcbiAgICBcInRhZ3NfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS90YWdzXCIsXG4gICAgXCJibG9ic191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2dpdC9ibG9ic3svc2hhfVwiLFxuICAgIFwiZ2l0X3RhZ3NfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9naXQvdGFnc3svc2hhfVwiLFxuICAgIFwiZ2l0X3JlZnNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9naXQvcmVmc3svc2hhfVwiLFxuICAgIFwidHJlZXNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9naXQvdHJlZXN7L3NoYX1cIixcbiAgICBcInN0YXR1c2VzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvc3RhdHVzZXMve3NoYX1cIixcbiAgICBcImxhbmd1YWdlc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2xhbmd1YWdlc1wiLFxuICAgIFwic3RhcmdhemVyc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL3N0YXJnYXplcnNcIixcbiAgICBcImNvbnRyaWJ1dG9yc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2NvbnRyaWJ1dG9yc1wiLFxuICAgIFwic3Vic2NyaWJlcnNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9zdWJzY3JpYmVyc1wiLFxuICAgIFwic3Vic2NyaXB0aW9uX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvc3Vic2NyaXB0aW9uXCIsXG4gICAgXCJjb21taXRzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvY29tbWl0c3svc2hhfVwiLFxuICAgIFwiZ2l0X2NvbW1pdHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9naXQvY29tbWl0c3svc2hhfVwiLFxuICAgIFwiY29tbWVudHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9jb21tZW50c3svbnVtYmVyfVwiLFxuICAgIFwiaXNzdWVfY29tbWVudF91cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2lzc3Vlcy9jb21tZW50c3svbnVtYmVyfVwiLFxuICAgIFwiY29udGVudHNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9jb250ZW50cy97K3BhdGh9XCIsXG4gICAgXCJjb21wYXJlX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvY29tcGFyZS97YmFzZX0uLi57aGVhZH1cIixcbiAgICBcIm1lcmdlc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL21lcmdlc1wiLFxuICAgIFwiYXJjaGl2ZV91cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL3thcmNoaXZlX2Zvcm1hdH17L3JlZn1cIixcbiAgICBcImRvd25sb2Fkc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2Rvd25sb2Fkc1wiLFxuICAgIFwiaXNzdWVzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvaXNzdWVzey9udW1iZXJ9XCIsXG4gICAgXCJwdWxsc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL3B1bGxzey9udW1iZXJ9XCIsXG4gICAgXCJtaWxlc3RvbmVzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvbWlsZXN0b25lc3svbnVtYmVyfVwiLFxuICAgIFwibm90aWZpY2F0aW9uc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL25vdGlmaWNhdGlvbnN7P3NpbmNlLGFsbCxwYXJ0aWNpcGF0aW5nfVwiLFxuICAgIFwibGFiZWxzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vcmVwb3MvYmlud2llZGVyaGllci9kYWJibGUvbGFiZWxzey9uYW1lfVwiLFxuICAgIFwicmVsZWFzZXNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9iaW53aWVkZXJoaWVyL2RhYmJsZS9yZWxlYXNlc3svaWR9XCIsXG4gICAgXCJkZXBsb3ltZW50c191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2JpbndpZWRlcmhpZXIvZGFiYmxlL2RlcGxveW1lbnRzXCIsXG4gICAgXCJjcmVhdGVkX2F0XCI6IFwiMjAyMi0wMy0xNVQxNTowNjoxN1pcIixcbiAgICBcInVwZGF0ZWRfYXRcIjogXCIyMDIyLTAzLTE1VDE1OjA2OjE3WlwiLFxuICAgIFwicHVzaGVkX2F0XCI6IFwiMjAyNC0wMy0yMVQwMjo1MjoxMFpcIixcbiAgICBcImdpdF91cmxcIjogXCJnaXQ6Ly9naXRodWIuY29tL2JpbndpZWRlcmhpZXIvZGFiYmxlLmdpdFwiLFxuICAgIFwic3NoX3VybFwiOiBcImdpdEBnaXRodWIuY29tOmJpbndpZWRlcmhpZXIvZGFiYmxlLmdpdFwiLFxuICAgIFwiY2xvbmVfdXJsXCI6IFwiaHR0cHM6Ly9naXRodWIuY29tL2JpbndpZWRlcmhpZXIvZGFiYmxlLmdpdFwiLFxuICAgIFwic3ZuX3VybFwiOiBcImh0dHBzOi8vZ2l0aHViLmNvbS9iaW53aWVkZXJoaWVyL2RhYmJsZVwiLFxuICAgIFwiaG9tZXBhZ2VcIjogbnVsbCxcbiAgICBcInNpemVcIjogMSxcbiAgICBcInN0YXJnYXplcnNfY291bnRcIjogMCxcbiAgICBcIndhdGNoZXJzX2NvdW50XCI6IDAsXG4gICAgXCJsYW5ndWFnZVwiOiBudWxsLFxuICAgIFwiaGFzX2lzc3Vlc1wiOiB0cnVlLFxuICAgIFwiaGFzX3Byb2plY3RzXCI6IHRydWUsXG4gICAgXCJoYXNfZG93bmxvYWRzXCI6IHRydWUsXG4gICAgXCJoYXNfd2lraVwiOiB0cnVlLFxuICAgIFwiaGFzX3BhZ2VzXCI6IGZhbHNlLFxuICAgIFwiaGFzX2Rpc2N1c3Npb25zXCI6IGZhbHNlLFxuICAgIFwiZm9ya3NfY291bnRcIjogMCxcbiAgICBcIm1pcnJvcl91cmxcIjogbnVsbCxcbiAgICBcImFyY2hpdmVkXCI6IGZhbHNlLFxuICAgIFwiZGlzYWJsZWRcIjogZmFsc2UsXG4gICAgXCJvcGVuX2lzc3Vlc19jb3VudFwiOiAxLFxuICAgIFwibGljZW5zZVwiOiBudWxsLFxuICAgIFwiYWxsb3dfZm9ya2luZ1wiOiB0cnVlLFxuICAgIFwiaXNfdGVtcGxhdGVcIjogZmFsc2UsXG4gICAgXCJ3ZWJfY29tbWl0X3NpZ25vZmZfcmVxdWlyZWRcIjogZmFsc2UsXG4gICAgXCJ0b3BpY3NcIjogW10sXG4gICAgXCJ2aXNpYmlsaXR5XCI6IFwicHVibGljXCIsXG4gICAgXCJmb3Jrc1wiOiAwLFxuICAgIFwib3Blbl9pc3N1ZXNcIjogMSxcbiAgICBcIndhdGNoZXJzXCI6IDAsXG4gICAgXCJkZWZhdWx0X2JyYW5jaFwiOiBcIm1haW5cIlxuICB9LFxuICBcInNlbmRlclwiOiB7XG4gICAgXCJsb2dpblwiOiBcImJpbndpZWRlcmhpZXJcIixcbiAgICBcImlkXCI6IDY2NDU5NyxcbiAgICBcIm5vZGVfaWRcIjogXCJNRFE2VlhObGNqWTJORFU1Tnc9PVwiLFxuICAgIFwiYXZhdGFyX3VybFwiOiBcImh0dHBzOi8vYXZhdGFycy5naXRodWJ1c2VyY29udGVudC5jb20vdS82NjQ1OTc/dj00XCIsXG4gICAgXCJncmF2YXRhcl9pZFwiOiBcIlwiLFxuICAgIFwidXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyXCIsXG4gICAgXCJodG1sX3VybFwiOiBcImh0dHBzOi8vZ2l0aHViLmNvbS9iaW53aWVkZXJoaWVyXCIsXG4gICAgXCJmb2xsb3dlcnNfdXJsXCI6IFwiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy9iaW53aWVkZXJoaWVyL2ZvbGxvd2Vyc1wiLFxuICAgIFwiZm9sbG93aW5nX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9mb2xsb3dpbmd7L290aGVyX3VzZXJ9XCIsXG4gICAgXCJnaXN0c191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvZ2lzdHN7L2dpc3RfaWR9XCIsXG4gICAgXCJzdGFycmVkX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9zdGFycmVkey9vd25lcn17L3JlcG99XCIsXG4gICAgXCJzdWJzY3JpcHRpb25zX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9zdWJzY3JpcHRpb25zXCIsXG4gICAgXCJvcmdhbml6YXRpb25zX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9vcmdzXCIsXG4gICAgXCJyZXBvc191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvcmVwb3NcIixcbiAgICBcImV2ZW50c191cmxcIjogXCJodHRwczovL2FwaS5naXRodWIuY29tL3VzZXJzL2JpbndpZWRlcmhpZXIvZXZlbnRzey9wcml2YWN5fVwiLFxuICAgIFwicmVjZWl2ZWRfZXZlbnRzX3VybFwiOiBcImh0dHBzOi8vYXBpLmdpdGh1Yi5jb20vdXNlcnMvYmlud2llZGVyaGllci9yZWNlaXZlZF9ldmVudHNcIixcbiAgICBcInR5cGVcIjogXCJVc2VyXCIsXG4gICAgXCJzaXRlX2FkbWluXCI6IGZhbHNlXG4gIH1cbn1cbiIsImNvbmZpZyI6eyJ0ZW1wbGF0ZSI6InRleHQiLCJmdWxsU2NyZWVuSFRNTCI6ZmFsc2UsImZ1bmN0aW9ucyI6WyJzcHJpZyJdLCJvcHRpb25zIjpbImxpdmUiXSwiaW5wdXRUeXBlIjoieWFtbCJ9fQ==))
- Loops (e.g. `}..}`, see [example](https://repeatit.io/#/share/eyJ0ZW1wbGF0ZSI6IlNldmVyZSBVUkxzOlxue3tyYW5nZSAuZXJyb3JzfX17e2lmIGVxIC5sZXZlbCBcInNldmVyZVwifX0tIHt7LnVybH19XG57e2VuZH19e3tlbmR9fSIsImlucHV0Ijoie1wiZm9vXCI6IFwiYmFyXCIsIFwiZXJyb3JzXCI6IFt7XCJsZXZlbFwiOiBcInNldmVyZVwiLCBcInVybFwiOiBcImh0dHBzOi8vc2V2ZXJlMS5jb21cIn0se1wibGV2ZWxcIjogXCJ3YXJuaW5nXCIsIFwidXJsXCI6IFwiaHR0cHM6Ly93YXJuaW5nLmNvbVwifSx7XCJsZXZlbFwiOiBcInNldmVyZVwiLCBcInVybFwiOiBcImh0dHBzOi8vc2V2ZXJlMi5jb21cIn1dfSIsImNvbmZpZyI6eyJ0ZW1wbGF0ZSI6InRleHQiLCJmdWxsU2NyZWVuSFRNTCI6ZmFsc2UsImZ1bmN0aW9ucyI6WyJzcHJpZyJdLCJvcHRpb25zIjpbImxpdmUiXSwiaW5wdXRUeXBlIjoieWFtbCJ9fQ==))

A good way to experiment with Go templates is the **[Go Template Playground](https://repeatit.io)**. It is *highly recommended* to test your templates there first ([example for Grafana alert](https://repeatit.io/#/share/eyJ0ZW1wbGF0ZSI6InRpdGxlPUdyYWZhbmErYWxlcnQ6K3t7LnRpdGxlfX0mbWVzc2FnZT17ey5tZXNzYWdlfX0iLCJpbnB1dCI6IntcbiAgXCJyZWNlaXZlclwiOiBcIm50ZnlcXFxcLmV4YW1wbGVcXFxcLmNvbS9hbGVydHNcIixcbiAgXCJzdGF0dXNcIjogXCJyZXNvbHZlZFwiLFxuICBcImFsZXJ0c1wiOiBbXG4gICAge1xuICAgICAgXCJzdGF0dXNcIjogXCJyZXNvbHZlZFwiLFxuICAgICAgXCJsYWJlbHNcIjoge1xuICAgICAgICBcImFsZXJ0bmFtZVwiOiBcIkxvYWQgYXZnIDE1bSB0b28gaGlnaFwiLFxuICAgICAgICBcImdyYWZhbmFfZm9sZGVyXCI6IFwiTm9kZSBhbGVydHNcIixcbiAgICAgICAgXCJpbnN0YW5jZVwiOiBcIjEwLjEwOC4wLjI6OTEwMFwiLFxuICAgICAgICBcImpvYlwiOiBcIm5vZGUtZXhwb3J0ZXJcIlxuICAgICAgfSxcbiAgICAgIFwiYW5ub3RhdGlvbnNcIjoge1xuICAgICAgICBcInN1bW1hcnlcIjogXCIxNW0gbG9hZCBhdmVyYWdlIHRvbyBoaWdoXCJcbiAgICAgIH0sXG4gICAgICBcInN0YXJ0c0F0XCI6IFwiMjAyNC0wMy0xNVQwMjoyODowMFpcIixcbiAgICAgIFwiZW5kc0F0XCI6IFwiMjAyNC0wMy0xNVQwMjo0MjowMFpcIixcbiAgICAgIFwiZ2VuZXJhdG9yVVJMXCI6IFwibG9jYWxob3N0OjMwMDAvYWxlcnRpbmcvZ3JhZmFuYS9OVzlvRHctNHovdmlld1wiLFxuICAgICAgXCJmaW5nZXJwcmludFwiOiBcImJlY2JmYjk0YmQ4MWVmNDhcIixcbiAgICAgIFwic2lsZW5jZVVSTFwiOiBcImxvY2FsaG9zdDozMDAwL2FsZXJ0aW5nL3NpbGVuY2UvbmV3P2FsZXJ0bWFuYWdlcj1ncmFmYW5hJm1hdGNoZXI9YWxlcnRuYW1lJTNETG9hZCthdmcrMTVtK3RvbytoaWdoJm1hdGNoZXI9Z3JhZmFuYV9mb2xkZXIlM0ROb2RlK2FsZXJ0cyZtYXRjaGVyPWluc3RhbmNlJTNEMTAuMTA4LjAuMiUzQTkxMDAmbWF0Y2hlcj1qb2IlM0Rub2RlLWV4cG9ydGVyXCIsXG4gICAgICBcImRhc2hib2FyZFVSTFwiOiBcIlwiLFxuICAgICAgXCJwYW5lbFVSTFwiOiBcIlwiLFxuICAgICAgXCJ2YWx1ZXNcIjoge1xuICAgICAgICBcIkJcIjogMTguOTgyMTEzMTQ0NzU4NzYsXG4gICAgICAgIFwiQ1wiOiAwXG4gICAgICB9LFxuICAgICAgXCJ2YWx1ZVN0cmluZ1wiOiBcIlsgdmFyPSdCJyBsYWJlbHM9e19fbmFtZV9fPW5vZGVfbG9hZDE1LCBpbnN0YW5jZT0xMC4xMDguMC4yOjkxMDAsIGpvYj1ub2RlLWV4cG9ydGVyfSB2YWx1ZT0xOC45ODIxMTMxNDQ3NTg3NiBdLCBbIHZhcj0nQycgbGFiZWxzPXtfX25hbWVfXz1ub2RlX2xvYWQxNSwgaW5zdGFuY2U9MTAuMTA4LjAuMjo5MTAwLCBqb2I9bm9kZS1leHBvcnRlcn0gdmFsdWU9MCBdXCJcbiAgICB9XG4gIF0sXG4gIFwiZ3JvdXBMYWJlbHNcIjoge1xuICAgIFwiYWxlcnRuYW1lXCI6IFwiTG9hZCBhdmcgMTVtIHRvbyBoaWdoXCIsXG4gICAgXCJncmFmYW5hX2ZvbGRlclwiOiBcIk5vZGUgYWxlcnRzXCJcbiAgfSxcbiAgXCJjb21tb25MYWJlbHNcIjoge1xuICAgIFwiYWxlcnRuYW1lXCI6IFwiTG9hZCBhdmcgMTVtIHRvbyBoaWdoXCIsXG4gICAgXCJncmFmYW5hX2ZvbGRlclwiOiBcIk5vZGUgYWxlcnRzXCIsXG4gICAgXCJpbnN0YW5jZVwiOiBcIjEwLjEwOC4wLjI6OTEwMFwiLFxuICAgIFwiam9iXCI6IFwibm9kZS1leHBvcnRlclwiXG4gIH0sXG4gIFwiY29tbW9uQW5ub3RhdGlvbnNcIjoge1xuICAgIFwic3VtbWFyeVwiOiBcIjE1bSBsb2FkIGF2ZXJhZ2UgdG9vIGhpZ2hcIlxuICB9LFxuICBcImV4dGVybmFsVVJMXCI6IFwibG9jYWxob3N0OjMwMDAvXCIsXG4gIFwidmVyc2lvblwiOiBcIjFcIixcbiAgXCJncm91cEtleVwiOiBcInt9OnthbGVydG5hbWU9XFxcIkxvYWQgYXZnIDE1bSB0b28gaGlnaFxcXCIsIGdyYWZhbmFfZm9sZGVyPVxcXCJOb2RlIGFsZXJ0c1xcXCJ9XCIsXG4gIFwidHJ1bmNhdGVkQWxlcnRzXCI6IDAsXG4gIFwib3JnSWRcIjogMSxcbiAgXCJ0aXRsZVwiOiBcIltSRVNPTFZFRF0gTG9hZCBhdmcgMTVtIHRvbyBoaWdoIE5vZGUgYWxlcnRzICgxMC4xMDguMC4yOjkxMDAgbm9kZS1leHBvcnRlcilcIixcbiAgXCJzdGF0ZVwiOiBcIm9rXCIsXG4gIFwibWVzc2FnZVwiOiBcIioqUmVzb2x2ZWQqKlxcblxcblZhbHVlOiBCPTE4Ljk4MjExMzE0NDc1ODc2LCBDPTBcXG5MYWJlbHM6XFxuIC0gYWxlcnRuYW1lID0gTG9hZCBhdmcgMTVtIHRvbyBoaWdoXFxuIC0gZ3JhZmFuYV9mb2xkZXIgPSBOb2RlIGFsZXJ0c1xcbiAtIGluc3RhbmNlID0gMTAuMTA4LjAuMjo5MTAwXFxuIC0gam9iID0gbm9kZS1leHBvcnRlclxcbkFubm90YXRpb25zOlxcbiAtIHN1bW1hcnkgPSAxNW0gbG9hZCBhdmVyYWdlIHRvbyBoaWdoXFxuU291cmNlOiBsb2NhbGhvc3Q6MzAwMC9hbGVydGluZy9ncmFmYW5hL05XOW9Edy00ei92aWV3XFxuU2lsZW5jZTogbG9jYWxob3N0OjMwMDAvYWxlcnRpbmcvc2lsZW5jZS9uZXc/YWxlcnRtYW5hZ2VyPWdyYWZhbmEmbWF0Y2hlcj1hbGVydG5hbWUlM0RMb2FkK2F2ZysxNW0rdG9vK2hpZ2gmbWF0Y2hlcj1ncmFmYW5hX2ZvbGRlciUzRE5vZGUrYWxlcnRzJm1hdGNoZXI9aW5zdGFuY2UlM0QxMC4xMDguMC4yJTNBOTEwMCZtYXRjaGVyPWpvYiUzRG5vZGUtZXhwb3J0ZXJcXG5cIlxufVxuIiwiY29uZmlnIjp7InRlbXBsYXRlIjoidGV4dCIsImZ1bGxTY3JlZW5IVE1MIjpmYWxzZSwiZnVuY3Rpb25zIjpbInNwcmlnIl0sIm9wdGlvbnMiOlsibGl2ZSJdLCJpbnB1dFR5cGUiOiJ5YW1sIn19)).

### Template functions[¶](#template-functions "Permanent link")

ntfy supports a subset of the **[Sprig template functions](template-functions/)** (originally copied from [Sprig](https://github.com/Masterminds/sprig), thank you to the Sprig developers 🙏). This is useful for advanced message templating and for transforming the data provided through the JSON payload.

Below are the functions that are available to use inside your message/title templates.

- [String Functions](template-functions/#string-functions): `trim`, `trunc`, `substr`, `plural`, etc.
- [String List Functions](template-functions/#string-list-functions): `splitList`, `sortAlpha`, etc.
- [Integer Math Functions](template-functions/#integer-math-functions): `add`, `max`, `mul`, etc.
- [Integer List Functions](template-functions/#integer-list-functions): `until`, `untilStep`
- [Float Math Functions](template-functions/#float-math-functions): `maxf`, `minf`
- [Date Functions](template-functions/#date-functions): `now`, `date`, etc.
- [Defaults Functions](template-functions/#default-functions): `default`, `empty`, `coalesce`, `fromJSON`, `toJSON`, `toPrettyJSON`, `toRawJSON`, `ternary`
- [Encoding Functions](template-functions/#encoding-functions): `b64enc`, `b64dec`, etc.
- [Lists and List Functions](template-functions/#lists-and-list-functions): `list`, `first`, `uniq`, etc.
- [Dictionaries and Dict Functions](template-functions/#dictionaries-and-dict-functions): `get`, `set`, `dict`, `hasKey`, `pluck`, `dig`, etc.
- [Type Conversion Functions](template-functions/#type-conversion-functions): `atoi`, `int64`, `toString`, etc.
- [Path and Filepath Functions](template-functions/#path-and-filepath-functions): `base`, `dir`, `ext`, `clean`, `isAbs`, `osBase`, `osDir`, `osExt`, `osClean`, `osIsAbs`
- [Flow Control Functions](template-functions/#flow-control-functions): `fail`
- Advanced Functions
  - [Reflection](template-functions/#reflection-functions): `typeOf`, `kindIs`, `typeIsLike`, etc.
  - [Cryptographic and Security Functions](template-functions/#cryptographic-and-security-functions): `sha256sum`, etc.
  - [URL](template-functions/#url-functions): `urlParse`, `urlJoin`

## Publish as JSON[¶](#publish-as-json "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

For some integrations with other tools (e.g. [Jellyfin](https://jellyfin.org/), [overseerr](https://overseerr.dev/)), adding custom headers to HTTP requests may be tricky or impossible, so ntfy also allows publishing the entire message as JSON in the request body.

To publish as JSON, simple PUT/POST the JSON object directly to the ntfy root URL. The message format is described below the example.

Info

To publish as JSON, you must **PUT/POST to the ntfy root URL**, not to the topic URL. Be sure to check that you\'re POST-ing to `https://ntfy.sh/` (correct), and not to `https://ntfy.sh/mytopic` (incorrect).

Here\'s an example using most supported parameters. Check the table below for a complete list. The `topic` parameter is the only required one:

Command line (curl)HTTPJavaScriptGoPowerShellPythonPHP

    curl ntfy.sh \
      -d ']
      }'

    POST / HTTP/1.1
    Host: ntfy.sh

    ]
    }

    fetch('https://ntfy.sh', ]
        })
    })

    // You should probably use json.Marshal() instead and make a proper struct,
    // or even just use req.Header.Set() like in the other examples, but for the 
    // sake of the example, this is easier.

    body := `]
    }`
    req, _ := http.NewRequest("POST", "https://ntfy.sh/", strings.NewReader(body))
    http.DefaultClient.Do(req)

    $Request = @
        )
      }
      ContentType = "application/json"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/",
        data=json.dumps(]
        })
    )

    file_get_contents('https://ntfy.sh/', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' => "Content-Type: application/json",
            'content' => json_encode([
                "topic": "mytopic",
                "message": "Disk space is low at 5.1 GB",
                "title": "Low disk space alert",
                "tags": ["warning","cd"],
                "priority": 4,
                "attach": "https://filesrv.lan/space.jpg",
                "filename": "diskspace.jpg",
                "click": "https://homecamera.lan/xasds1h2xsSsa/",
                "actions": [["action": "view", "label": "Admin panel", "url": "https://filesrv.lan/admin" ]]
            ])
        ]
    ]));

The JSON message format closely mirrors the format of the message you can consume when you [subscribe via the API](../subscribe/api/) (see [JSON message format](../subscribe/api/#json-message-format) for details), but is not exactly identical. Here\'s an overview of all the supported fields:

  Field        Required   Type                               Example                                     Description
  ------------ ---------- ---------------------------------- ------------------------------------------- -----------------------------------------------------------------------
  `topic`      ✔️         *string*                           `topic1`                                    Target topic name
  `message`    \-         *string*                           `Some message`                              Message body; set to `triggered` if empty or not passed
  `title`      \-         *string*                           `Some title`                                Message [title](#message-title)
  `tags`       \-         *string array*                     `["tag1","tag2"]`                           List of [tags](#tags-emojis) that may or not map to emojis
  `priority`   \-         *int (one of: 1, 2, 3, 4, or 5)*   `4`                                         Message [priority](#message-priority) with 1=min, 3=default and 5=max
  `actions`    \-         *JSON array*                       *(see [action buttons](#action-buttons))*   Custom [user action buttons](#action-buttons) for notifications
  `click`      \-         *URL*                              `https://example.com`                       Website opened when notification is [clicked](#click-action)
  `attach`     \-         *URL*                              `https://example.com/file.jpg`              URL of an attachment, see [attach via URL](#attach-file-from-a-url)
  `markdown`   \-         *bool*                             `true`                                      Set to true if the `message` is Markdown-formatted
  `icon`       \-         *string*                           `https://example.com/icon.png`              URL to use as notification [icon](#icons)
  `filename`   \-         *string*                           `file.jpg`                                  File name of the attachment
  `delay`      \-         *string*                           `30min`, `9am`                              Timestamp or duration for delayed delivery
  `email`      \-         *e-mail address*                   `phil@example.com`                          E-mail address for e-mail notifications
  `call`       \-         *phone number or \'yes\'*          `+1222334444` or `yes`                      Phone number to use for [voice call](#phone-calls)

## Action buttons[¶](#action-buttons "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

You can add action buttons to notifications to allow yourself to react to a notification directly. This is incredibly useful and has countless applications.

You can control your home appliances (open/close garage door, change temperature on thermostat, \...), react to common monitoring alerts (clear logs when disk is full, \...), and many other things. The sky is the limit.

As of today, the following actions are supported:

- [`view`](#open-websiteapp): Opens a website or app when the action button is tapped
- [`broadcast`](#send-android-broadcast): Sends an [Android broadcast](https://developer.android.com/guide/components/broadcasts) intent when the action button is tapped (only supported on Android)
- [`http`](#send-http-request): Sends HTTP POST/GET/PUT request when the action button is tapped

Here\'s an example of what a notification with actions can look like:

<figure>
<p><img src="../static/img/android-screenshot-notification-actions.png" width="500" alt="notification with actions" /></p>
<figcaption>Notification with two user actions</figcaption>
</figure>

### Defining actions[¶](#defining-actions "Permanent link")

You can define **up to three user actions** in your notifications, using either of the following methods:

- In the [`X-Actions` header](#using-a-header), using a simple comma-separated format
- As a [JSON array](#using-a-json-array) in the `actions` key, when [publishing as JSON](#publish-as-json)

#### Using a header[¶](#using-a-header "Permanent link")

To define actions using the `X-Actions` header (or any of its aliases: `Actions`, `Action`), use the following format:

Header format (long)Header format (short)

    action=<action1>, label=<label1>, paramN=... [; action=<action2>, label=<label2>, ...]

    <action1>, <label1>, paramN=... [; <action2>, <label2>, ...]

Multiple actions are separated by a semicolon (`;`), and key/value pairs are separated by commas (`,`). Values may be quoted with double quotes (`"`) or single quotes (`'`) if the value itself contains commas or semicolons.

The `action=` and `label=` prefix are optional in all actions, and the `url=` prefix is optional in the `view` and `http` action. The only limitation of this format is that depending on your language/library, UTF-8 characters may not work. If they don\'t, use the [JSON array format](#using-a-json-array) instead.

As an example, here\'s how you can create the above notification using this format. Refer to the [`view` action](#open-websiteapp) and [`http` action](#send-http-request) section for details on the specific actions:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    body=''
    curl \
        -d "You left the house. Turn down the A/C?" \
        -H "Actions: view, Open portal, https://home.nest.com/, clear=true; \
                     http, Turn down, https://api.nest.com/, body='$body'" \
        ntfy.sh/myhome

    body=''
    ntfy publish \
        --actions="view, Open portal, https://home.nest.com/, clear=true; \
                   http, Turn down, https://api.nest.com/, body='$body'" \
        myhome \
        "You left the house. Turn down the A/C?"

    POST /myhome HTTP/1.1
    Host: ntfy.sh
    Actions: view, Open portal, https://home.nest.com/, clear=true; http, Turn down, https://api.nest.com/, body=''

    You left the house. Turn down the A/C?

    fetch('https://ntfy.sh/myhome', \'' 
        }
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/myhome", strings.NewReader("You left the house. Turn down the A/C?"))
    req.Header.Set("Actions", "view, Open portal, https://home.nest.com/, clear=true; http, Turn down, https://api.nest.com/, body=''")
    http.DefaultClient.Do(req)

    $Request = @'"
      }
      Body = "You left the house. Turn down the A/C?"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/myhome",
        data="You left the house. Turn down the A/C?",
        headers='" })

    file_get_contents('https://ntfy.sh/reddit_alerts', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' =>
                "Content-Type: text/plain\r\n" .
                "Actions: view, Open portal, https://home.nest.com/, clear=true; http, Turn down, https://api.nest.com/, body=''",
            'content' => 'You left the house. Turn down the A/C?'
        ]
    ]));

Info

ntfy supports UTF-8 in HTTP headers, but [not every library or programming language does](https://www.jmix.io/blog/utf-8-in-http-headers/). If non-ASCII characters are causing issues for you in the title (i.e. you\'re seeing `?` symbols), you may also encode any header (including actions) as [RFC 2047](https://datatracker.ietf.org/doc/html/rfc2047#section-2), e.g. `=?UTF-8?B?8J+HqfCfh6o=?=` ([base64](https://en.wikipedia.org/wiki/Base64)), or `=?UTF-8?Q?=C3=84pfel?=` ([quoted-printable](https://en.wikipedia.org/wiki/Quoted-printable)).

#### Using a JSON array[¶](#using-a-json-array "Permanent link")

Alternatively, the same actions can be defined as **JSON array**, if the notification is defined as part of the JSON body (see [publish as JSON](#publish-as-json)):

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl ntfy.sh \
      -d ',
          "
          }
        ]
      }'

    ntfy publish \
        --actions '[
            ,
            "
            }
        ]' \
        myhome \
        "You left the house. Turn down the A/C?"

    POST / HTTP/1.1
    Host: ntfy.sh

    ,
          "
          }
        ]
    }

    fetch('https://ntfy.sh', ,
                "
                }
            ]
        })
    })

    // You should probably use json.Marshal() instead and make a proper struct,
    // but for the sake of the example, this is easier.

    body := `,
          "
          }
        ]
    }`
    req, _ := http.NewRequest("POST", "https://ntfy.sh/", strings.NewReader(body))
    http.DefaultClient.Do(req)

    $Request = @,
          @'
          }
        )
      }
      ContentType = "application/json"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/",
        data=json.dumps(,
                "
                }
            ]
        })
    )

    file_get_contents('https://ntfy.sh/', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' => "Content-Type: application/json",
            'content' => json_encode([
                "topic": "myhome",
                "message": "You left the house. Turn down the A/C?",
                "actions": [
                    [
                        "action": "view",
                        "label": "Open portal",
                        "url": "https://home.nest.com/",
                        "clear": true
                    ],
                    [
                        "action": "http",
                        "label": "Turn down",
                        "url": "https://api.nest.com/",
                        "headers": [
                            "Authorization": "Bearer ..."
                        ],
                        "body": ""
                    ]
                ]
            ])
        ]
    ]));

The required/optional fields for each action depend on the type of the action itself. Please refer to [`view` action](#open-websiteapp), [`broadcast` action](#send-android-broadcast), and [`http` action](#send-http-request) for details.

### Open website/app[¶](#open-websiteapp "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

The `view` action **opens a website or app when the action button is tapped**, e.g. a browser, a Google Maps location, or even a deep link into Twitter or a show ntfy topic. How exactly the action is handled depends on how Android and your desktop browser treat the links. Normally it\'ll just open a link in the browser.

Examples:

- `http://` or `https://` will open your browser (or an app if it registered for a URL)
- `mailto:` links will open your mail app, e.g. `mailto:phil@example.com`
- `geo:` links will open Google Maps, e.g. `geo:0,0?q=1600+Amphitheatre+Parkway,+Mountain+View,+CA`
- `ntfy://` links will open ntfy (see [ntfy:// links](../subscribe/phone/#ntfy-links)), e.g. `ntfy://ntfy.sh/stats`
- `twitter://` links will open Twitter, e.g. `twitter://user?screen_name=..`
- \...

Here\'s an example using the [`X-Actions` header](#using-a-header):

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl \
        -d "Somebody retweeted your tweet." \
        -H "Actions: view, Open Twitter, https://twitter.com/binwiederhier/status/1467633927951163392" \
    ntfy.sh/myhome

    ntfy publish \
        --actions="view, Open Twitter, https://twitter.com/binwiederhier/status/1467633927951163392" \
        myhome \
        "Somebody retweeted your tweet."

    POST /myhome HTTP/1.1
    Host: ntfy.sh
    Actions: view, Open Twitter, https://twitter.com/binwiederhier/status/1467633927951163392

    Somebody retweeted your tweet.

    fetch('https://ntfy.sh/myhome', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/myhome", strings.NewReader("Somebody retweeted your tweet."))
    req.Header.Set("Actions", "view, Open Twitter, https://twitter.com/binwiederhier/status/1467633927951163392")
    http.DefaultClient.Do(req)

    $Request = @
      Body = "Somebody retweeted your tweet."
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/myhome",
        data="Somebody retweeted your tweet.",
        headers=)

    file_get_contents('https://ntfy.sh/reddit_alerts', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' =>
                "Content-Type: text/plain\r\n" .
                "Actions: view, Open Twitter, https://twitter.com/binwiederhier/status/1467633927951163392",
            'content' => 'Somebody retweeted your tweet.'
        ]
    ]));

And the same example using [JSON publishing](#publish-as-json):

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl ntfy.sh \
      -d '
        ]
      }'

    ntfy publish \
        --actions '[
            
        ]' \
        myhome \
        "Somebody retweeted your tweet."

    POST / HTTP/1.1
    Host: ntfy.sh

    
        ]
    }

    fetch('https://ntfy.sh', 
            ]
        })
    })

    // You should probably use json.Marshal() instead and make a proper struct,
    // but for the sake of the example, this is easier.

    body := `
        ]
    }`
    req, _ := http.NewRequest("POST", "https://ntfy.sh/", strings.NewReader(body))
    http.DefaultClient.Do(req)

    $Request = @
        )
      }
      ContentType = "application/json"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/",
        data=json.dumps(
            ]
        })
    )

    file_get_contents('https://ntfy.sh/', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' => "Content-Type: application/json",
            'content' => json_encode([
                "topic": "myhome",
                "message": "Somebody retweeted your tweet.",
                "actions": [
                    [
                        "action": "view",
                        "label": "Open Twitter",
                        "url": "https://twitter.com/binwiederhier/status/1467633927951163392"
                    ]
                ]
            ])
        ]
    ]));

The `view` action supports the following fields:

  Field      Required   Type        Default   Example                 Description
  ---------- ---------- ----------- --------- ----------------------- --------------------------------------------------
  `action`   ✔️         *string*    \-        `view`                  Action type (**must be `view`**)
  `label`    ✔️         *string*    \-        `Turn on light`         Label of the action button in the notification
  `url`      ✔️         *URL*       \-        `https://example.com`   URL to open when action is tapped
  `clear`    -️          *boolean*   `false`   `true`                  Clear notification after action button is tapped

### Send Android broadcast[¶](#send-android-broadcast "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)]

The `broadcast` action **sends an [Android broadcast](https://developer.android.com/guide/components/broadcasts) intent when the action button is tapped**. This allows integration into automation apps such as [MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) or [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm), which basically means you can do everything your phone is capable of. Examples include taking pictures, launching/killing apps, change device settings, write/read files, etc.

By default, the intent action **`io.heckel.ntfy.USER_ACTION`** is broadcast, though this can be changed with the `intent` parameter (see below). To send extras, use the `extras` parameter. Currently, **only string extras are supported**.

Info

If you have no idea what this is, check out the [automation apps](../subscribe/phone/#automation-apps) section, which shows how to integrate Tasker and MacroDroid **with screenshots**. The action button integration is identical, except that you have to use **the intent action `io.heckel.ntfy.USER_ACTION`** instead.

Here\'s an example using the [`X-Actions` header](#using-a-header):

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl \
        -d "Your wife requested you send a picture of yourself." \
        -H "Actions: broadcast, Take picture, extras.cmd=pic, extras.camera=front" \
    ntfy.sh/wifey

    ntfy publish \
        --actions="broadcast, Take picture, extras.cmd=pic, extras.camera=front" \
        wifey \
        "Your wife requested you send a picture of yourself."

    POST /wifey HTTP/1.1
    Host: ntfy.sh
    Actions: broadcast, Take picture, extras.cmd=pic, extras.camera=front

    Your wife requested you send a picture of yourself.

    fetch('https://ntfy.sh/wifey', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/wifey", strings.NewReader("Your wife requested you send a picture of yourself."))
    req.Header.Set("Actions", "broadcast, Take picture, extras.cmd=pic, extras.camera=front")
    http.DefaultClient.Do(req)

    $Request = @
      Body = "Your wife requested you send a picture of yourself."
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/wifey",
        data="Your wife requested you send a picture of yourself.",
        headers=)

    file_get_contents('https://ntfy.sh/wifey', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' =>
                "Content-Type: text/plain\r\n" .
                "Actions: broadcast, Take picture, extras.cmd=pic, extras.camera=front",
            'content' => 'Your wife requested you send a picture of yourself.'
        ]
    ]));

And the same example using [JSON publishing](#publish-as-json):

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl ntfy.sh \
      -d '
          }
        ]
      }'

    ntfy publish \
        --actions '[
            
            }
        ]' \
        wifey \
        "Your wife requested you send a picture of yourself."

    POST / HTTP/1.1
    Host: ntfy.sh

    
          }
        ]
    }

    fetch('https://ntfy.sh', 
                }
            ]
        })
    })

    // You should probably use json.Marshal() instead and make a proper struct,
    // but for the sake of the example, this is easier.

    body := `
          }
        ]
    }`
    req, _ := http.NewRequest("POST", "https://ntfy.sh/", strings.NewReader(body))
    http.DefaultClient.Do(req)

    # Powershell requires the 'Depth' argument to equal 3 here to expand 'Extras',
    # otherwise it will read System.Collections.Hashtable in the returned JSON
    $Request = @
          }
        )
      }
      ContentType = "application/json"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/",
        data=json.dumps(
                }
            ]
        })
    )

    file_get_contents('https://ntfy.sh/', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' => "Content-Type: application/json",
            'content' => json_encode([
                "topic": "wifey",
                "message": "Your wife requested you send a picture of yourself.",
                "actions": [
                    [
                    "action": "broadcast",
                    "label": "Take picture",
                    "extras": [
                        "cmd": "pic",
                        "camera": "front"
                    ]
                ]
            ])
        ]
    ]));

The `broadcast` action supports the following fields:

  Field      Required   Type               Default                        Example                   Description
  ---------- ---------- ------------------ ------------------------------ ------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `action`   ✔️         *string*           \-                             `broadcast`               Action type (**must be `broadcast`**)
  `label`    ✔️         *string*           \-                             `Turn on light`           Label of the action button in the notification
  `intent`   -️          *string*           `io.heckel.ntfy.USER_ACTION`   `com.example.AN_INTENT`   Android intent name, **default is `io.heckel.ntfy.USER_ACTION`**
  `extras`   -️          *map of strings*   \-                             *see above*               Android intent extras. Currently, only string extras are supported. When publishing as JSON, extras are passed as a map. When the simple format is used, use `extras.<param>=<value>`.
  `clear`    -️          *boolean*          `false`                        `true`                    Clear notification after action button is tapped

### Send HTTP request[¶](#send-http-request "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

The `http` action **sends a HTTP request when the action button is tapped**. You can use this to trigger REST APIs for whatever systems you have, e.g. opening the garage door, or turning on/off lights.

By default, this action sends a **POST request** (not GET!), though this can be changed with the `method` parameter. The only required parameter is `url`. Headers can be passed along using the `headers` parameter.

Here\'s an example using the [`X-Actions` header](#using-a-header):

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl \
        -d "Garage door has been open for 15 minutes. Close it?" \
        -H "Actions: http, Close door, https://api.mygarage.lan/, method=PUT, headers.Authorization=Bearer zAzsx1sk.., body=" \
        ntfy.sh/myhome

    ntfy publish \
        --actions="http, Close door, https://api.mygarage.lan/, method=PUT, headers.Authorization=Bearer zAzsx1sk.., body=" \
        myhome \
        "Garage door has been open for 15 minutes. Close it?"

    POST /myhome HTTP/1.1
    Host: ntfy.sh
    Actions: http, Close door, https://api.mygarage.lan/, method=PUT, headers.Authorization=Bearer zAzsx1sk.., body=

    Garage door has been open for 15 minutes. Close it?

    fetch('https://ntfy.sh/myhome', ' 
        }
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/myhome", strings.NewReader("Garage door has been open for 15 minutes. Close it?"))
    req.Header.Set("Actions", "http, Close door, https://api.mygarage.lan/, method=PUT, headers.Authorization=Bearer zAzsx1sk.., body=")
    http.DefaultClient.Do(req)

    $Request = @"
      }
      Body = "Garage door has been open for 15 minutes. Close it?"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/myhome",
        data="Garage door has been open for 15 minutes. Close it?",
        headers=" })

    file_get_contents('https://ntfy.sh/reddit_alerts', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' =>
                "Content-Type: text/plain\r\n" .
                'Actions: http, Close door, https://api.mygarage.lan/, method=PUT, headers.Authorization=Bearer zAzsx1sk.., body=',
            'content' => 'Garage door has been open for 15 minutes. Close it?'
        ]
    ]));

And the same example using [JSON publishing](#publish-as-json):

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl ntfy.sh \
      -d ',
            "body": ""
          }
        ]
      }'

    ntfy publish \
        --actions '[
            ,
              "body": ""
            }
        ]' \
        myhome \
        "Garage door has been open for 15 minutes. Close it?"

    POST / HTTP/1.1
    Host: ntfy.sh

    ,
            "body": ""
          }
        ]
    }

    fetch('https://ntfy.sh', ,
                "body": ""
              }
            ]
        })
    })

    // You should probably use json.Marshal() instead and make a proper struct,
    // but for the sake of the example, this is easier.

    body := `,
            "body": ""
          }
        ]
    }`
    req, _ := http.NewRequest("POST", "https://ntfy.sh/", strings.NewReader(body))
    http.DefaultClient.Do(req)

    # Powershell requires the 'Depth' argument to equal 3 here to expand 'headers', 
    # otherwise it will read System.Collections.Hashtable in the returned JSON

    $Request = @
            Body    = ConvertTo-JSON @
          }
        )
      }
      ContentType = "application/json"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/",
        data=json.dumps(,
                  "body": ""
                }
            ]
        })
    )

    file_get_contents('https://ntfy.sh/', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' => "Content-Type: application/json",
            'content' => json_encode([
                "topic": "myhome",
                "message": "Garage door has been open for 15 minutes. Close it?",
                "actions": [
                    [
                        "action": "http",
                        "label": "Close door",
                        "url": "https://api.mygarage.lan/",
                        "method": "PUT",
                        "headers": [
                            "Authorization": "Bearer zAzsx1sk.."
                         ],
                        "body": ""
                    ]
                ]
            ])
        ]
    ]));

The `http` action supports the following fields:

  Field       Required   Type                  Default     Example                     Description
  ----------- ---------- --------------------- ----------- --------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------
  `action`    ✔️         *string*              \-          `http`                      Action type (**must be `http`**)
  `label`     ✔️         *string*              \-          `Open garage door`          Label of the action button in the notification
  `url`       ✔️         *string*              \-          `https://ntfy.sh/mytopic`   URL to which the HTTP request will be sent
  `method`    -️          *GET/POST/PUT/\...*   `POST` ⚠️   `GET`                       HTTP method to use for request, **default is POST** ⚠️
  `headers`   -️          *map of strings*      \-          *see above*                 HTTP headers to pass in request. When publishing as JSON, headers are passed as a map. When the simple format is used, use `headers.<header1>=<value>`.
  `body`      -️          *string*              *empty*     `some body, somebody?`      HTTP body
  `clear`     -️          *boolean*             `false`     `true`                      Clear notification after HTTP request succeeds. If the request fails, the notification is not cleared.

## Click action[¶](#click-action "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

You can define which URL to open when a notification is clicked. This may be useful if your notification is related to a Zabbix alert or a transaction that you\'d like to provide the deep-link for. Tapping the notification will open the web browser (or the app) and open the website.

To define a click action for the notification, pass a URL as the value of the `X-Click` header (or its alias `Click`). If you pass a website URL (`http://` or `https://`) the web browser will open. If you pass another URI that can be handled by another app, the responsible app may open.

Examples:

- `http://` or `https://` will open your browser (or an app if it registered for a URL)
- `mailto:` links will open your mail app, e.g. `mailto:phil@example.com`
- `geo:` links will open Google Maps, e.g. `geo:0,0?q=1600+Amphitheatre+Parkway,+Mountain+View,+CA`
- `ntfy://` links will open ntfy (see [ntfy:// links](../subscribe/phone/#ntfy-links)), e.g. `ntfy://ntfy.sh/stats`
- `twitter://` links will open Twitter, e.g. `twitter://user?screen_name=..`
- \...

Here\'s an example that will open Reddit when the notification is clicked:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl \
        -d "New messages on Reddit" \
        -H "Click: https://www.reddit.com/message/messages" \
        ntfy.sh/reddit_alerts

    ntfy publish \
        --click="https://www.reddit.com/message/messages" \
        reddit_alerts "New messages on Reddit"

    POST /reddit_alerts HTTP/1.1
    Host: ntfy.sh
    Click: https://www.reddit.com/message/messages 

    New messages on Reddit

    fetch('https://ntfy.sh/reddit_alerts', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/reddit_alerts", strings.NewReader("New messages on Reddit"))
    req.Header.Set("Click", "https://www.reddit.com/message/messages")
    http.DefaultClient.Do(req)

    $Request = @
      Body = "New messages on Reddit"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/reddit_alerts",
        data="New messages on Reddit",
        headers=)

    file_get_contents('https://ntfy.sh/reddit_alerts', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' =>
                "Content-Type: text/plain\r\n" .
                "Click: https://www.reddit.com/message/messages",
            'content' => 'New messages on Reddit'
        ]
    ]));

## Attachments[¶](#attachments "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

You can **send images and other files to your phone** as attachments to a notification. The attachments are then downloaded onto your phone (depending on size and setting automatically), and can be used from the Downloads folder.

There are two different ways to send attachments:

- sending [a local file](#attach-local-file) via PUT, e.g. from `~/Flowers/flower.jpg` or `ringtone.mp3`
- or by [passing an external URL](#attach-file-from-a-url) as an attachment, e.g. `https://f-droid.org/F-Droid.apk`

### Attach local file[¶](#attach-local-file "Permanent link")

To **send a file from your computer** as an attachment, you can send it as the PUT request body. If a message is greater than the maximum message size (4,096 bytes) or consists of non UTF-8 characters, the ntfy server will automatically detect the mime type and size, and send the message as an attachment file. To send smaller text-only messages or files as attachments, you must pass a filename by passing the `X-Filename` header or query parameter (or any of its aliases `Filename`, `File` or `f`).

By default, and how ntfy.sh is configured, the **max attachment size is 15 MB** (with 100 MB total per visitor). Attachments **expire after 3 hours**, which typically is plenty of time for the user to download it, or for the Android app to auto-download it. Please also check out the [other limits below](#limitations).

Here\'s an example showing how to upload an image:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl \
        -T flower.jpg \
        -H "Filename: flower.jpg" \
        ntfy.sh/flowers

    ntfy publish \
        --file=flower.jpg \
        flowers

    PUT /flowers HTTP/1.1
    Host: ntfy.sh
    Filename: flower.jpg
    Content-Type: 52312

    (binary JPEG data)

    fetch('https://ntfy.sh/flowers', 
    })

    file, _ := os.Open("flower.jpg")
    req, _ := http.NewRequest("PUT", "https://ntfy.sh/flowers", file)
    req.Header.Set("Filename", "flower.jpg")
    http.DefaultClient.Do(req)

    $Request = @
    }
    Invoke-RestMethod @Request

    requests.put("https://ntfy.sh/flowers",
        data=open("flower.jpg", 'rb'),
        headers=)

    file_get_contents('https://ntfy.sh/flowers', false, stream_context_create([
        'http' => [
            'method' => 'PUT',
            'header' =>
                "Content-Type: application/octet-stream\r\n" . // Does not matter
                "Filename: flower.jpg",
            'content' => file_get_contents('flower.jpg') // Dangerous for large files 
        ]
    ]));

Here\'s what that looks like on Android:

<figure>
<p><img src="../static/img/android-screenshot-attachment-image.png" width="500" alt="image attachment" /></p>
<figcaption>Image attachment sent from a local file</figcaption>
</figure>

### Attach file from a URL[¶](#attach-file-from-a-url "Permanent link")

Instead of sending a local file to your phone, you can use **an external URL** to specify where the attachment is hosted. This could be a Dropbox link, a file from social media, or any other publicly available URL. Since the files are externally hosted, the expiration or size limits from above do not apply here.

To attach an external file, simple pass the `X-Attach` header or query parameter (or any of its aliases `Attach` or `a`) to specify the attachment URL. It can be any type of file.

ntfy will automatically try to derive the file name from the URL (e.g `https://example.com/flower.jpg` will yield a filename `flower.jpg`). To override this filename, you may send the `X-Filename` header or query parameter (or any of its aliases `Filename`, `File` or `f`).

Here\'s an example showing how to attach an APK file:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl \
        -X POST \
        -H "Attach: https://f-droid.org/F-Droid.apk" \
        ntfy.sh/mydownloads

    ntfy publish \
        --attach="https://f-droid.org/F-Droid.apk" \
        mydownloads

    POST /mydownloads HTTP/1.1
    Host: ntfy.sh
    Attach: https://f-droid.org/F-Droid.apk

    fetch('https://ntfy.sh/mydownloads', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/mydownloads", file)
    req.Header.Set("Attach", "https://f-droid.org/F-Droid.apk")
    http.DefaultClient.Do(req)

    $Request = @
    }
    Invoke-RestMethod @Request

    requests.put("https://ntfy.sh/mydownloads",
        headers=)

    file_get_contents('https://ntfy.sh/mydownloads', false, stream_context_create([
        'http' => [
        'method' => 'PUT',
        'header' =>
            "Content-Type: text/plain\r\n" . // Does not matter
            "Attach: https://f-droid.org/F-Droid.apk",
        ]
    ]));

<figure>
<p><img src="../static/img/android-screenshot-attachment-file.png" width="500" alt="file attachment" /></p>
<figcaption>File attachment sent from an external URL</figcaption>
</figure>

## Icons[¶](#icons "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)]

You can include an icon that will appear next to the text of the notification. Simply pass the `X-Icon` header or query parameter (or its alias `Icon`) to specify the URL that the icon is located at. The client will automatically download the icon (unless it is already cached locally, and less than 24 hours old), and show it in the notification. Icons are cached locally in the client until the notification is deleted. **Only JPEG and PNG images are supported at this time**.

Here\'s an example showing how to include an icon:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl \
        -H "Icon: https://styles.redditmedia.com/t5_32uhe/styles/communityIcon_xnt6chtnr2j21.png" \
        -H "Title: Kodi: Resuming Playback" \
        -H "Tags: arrow_forward" \
        -d "The Wire, S01E01" \
        ntfy.sh/tvshows

    ntfy publish \
        --icon="https://styles.redditmedia.com/t5_32uhe/styles/communityIcon_xnt6chtnr2j21.png" \
        --title="Kodi: Resuming Playback" \
        --tags="arrow_forward" \
        tvshows \
        "The Wire, S01E01"

    POST /tvshows HTTP/1.1
    Host: ntfy.sh
    Icon: https://styles.redditmedia.com/t5_32uhe/styles/communityIcon_xnt6chtnr2j21.png
    Tags: arrow_forward
    Title: Kodi: Resuming Playback

    The Wire, S01E01

    fetch('https://ntfy.sh/tvshows', ,
        body: "The Wire, S01E01"
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/tvshows", strings.NewReader("The Wire, S01E01"))
    req.Header.Set("Icon", "https://styles.redditmedia.com/t5_32uhe/styles/communityIcon_xnt6chtnr2j21.png")
    req.Header.Set("Tags", "arrow_forward")
    req.Header.Set("Title", "Kodi: Resuming Playback")
    http.DefaultClient.Do(req)

    $Request = @
      Body = "The Wire, S01E01"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/tvshows",
        data="The Wire, S01E01",
        headers=)

    file_get_contents('https://ntfy.sh/tvshows', false, stream_context_create([
        'http' => [
        'method' => 'PUT',
        'header' =>
            "Content-Type: text/plain\r\n" . // Does not matter
            "Title: Kodi: Resuming Playback\r\n" .
            "Tags: arrow_forward\r\n" .
            "Icon: https://styles.redditmedia.com/t5_32uhe/styles/communityIcon_xnt6chtnr2j21.png",
        ],
        'content' => "The Wire, S01E01"
    ]));

Here\'s an example of how it will look on Android:

<figure>
<p><img src="../static/img/android-screenshot-icon.png" width="500" alt="file attachment" /></p>
<figcaption>Custom icon from an external URL</figcaption>
</figure>

## E-mail notifications[¶](#e-mail-notifications "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

You can forward messages to e-mail by specifying an address in the header. This can be useful for messages that you\'d like to persist longer, or to blast-notify yourself on all possible channels.

Usage is easy: Simply pass the `X-Email` header (or any of its aliases: `X-E-mail`, `Email`, `E-mail`, `Mail`, or `e`). Only one e-mail address is supported.

Since ntfy does not provide auth (yet), the rate limiting is pretty strict (see [limitations](#limitations)). In the default configuration, you get **16 e-mails per visitor** (IP address) and then after that one per hour. On top of that, your IP address appears in the e-mail body. This is to prevent abuse.

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl \
        -H "Email: phil@example.com" \
        -H "Tags: warning,skull,backup-host,ssh-login" \
        -H "Priority: high" \
        -d "Unknown login from 5.31.23.83 to backups.example.com" \
        ntfy.sh/alerts
    curl -H "Email: phil@example.com" -d "You've Got Mail" 
    curl -d "You've Got Mail" "ntfy.sh/alerts?email=phil@example.com"

    ntfy publish \
        --email=phil@example.com \
        --tags=warning,skull,backup-host,ssh-login \
        --priority=high \
        alerts "Unknown login from 5.31.23.83 to backups.example.com"

    POST /alerts HTTP/1.1
    Host: ntfy.sh
    Email: phil@example.com
    Tags: warning,skull,backup-host,ssh-login
    Priority: high

    Unknown login from 5.31.23.83 to backups.example.com

    fetch('https://ntfy.sh/alerts', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/alerts", 
        strings.NewReader("Unknown login from 5.31.23.83 to backups.example.com"))
    req.Header.Set("Email", "phil@example.com")
    req.Header.Set("Tags", "warning,skull,backup-host,ssh-login")
    req.Header.Set("Priority", "high")
    http.DefaultClient.Do(req)

    $Request = @
      Body = "Unknown login from 5.31.23.83 to backups.example.com"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/alerts",
        data="Unknown login from 5.31.23.83 to backups.example.com",
        headers=)

    file_get_contents('https://ntfy.sh/alerts', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' =>
                "Content-Type: text/plain\r\n" .
                "Email: phil@example.com\r\n" .
                "Tags: warning,skull,backup-host,ssh-login\r\n" .
                "Priority: high",
            'content' => 'Unknown login from 5.31.23.83 to backups.example.com'
        ]
    ]));

Here\'s what that looks like in Google Mail:

<figure>
<p><img src="../static/img/screenshot-email.png" width="600" alt="e-mail notification" /></p>
<figcaption>E-mail notification</figcaption>
</figure>

## E-mail publishing[¶](#e-mail-publishing "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

You can publish messages to a topic via e-mail, i.e. by sending an email to a specific address. For instance, you can publish a message to the topic `sometopic` by sending an e-mail to `ntfy-sometopic@ntfy.sh`. This is useful for e-mail based integrations such as for statuspage.io (though these days most services also support webhooks and HTTP calls).

Depending on the [server configuration](../config/#e-mail-publishing), the e-mail address format can have a prefix to prevent spam on topics. For ntfy.sh, the prefix is configured to `ntfy-`, meaning that the general e-mail address format is:

    ntfy-$topic@ntfy.sh

If [access control](../config/#access-control) is enabled, and the target topic does not support anonymous writes, e-mail publishing won\'t work without providing an authorized access token or using SMTP AUTH PLAIN.

If you use [access tokens](#access-tokens), that will change the format of the e-mail\'s recipient address to

    ntfy-$topic+$token@ntfy.sh

To use [username/password](https://docs.ntfy.sh/publish/#username-password), you can use SMTP PLAIN auth when authenticating to the ntfy server.

As of today, e-mail publishing only supports adding a [message title](#message-title) (the e-mail subject). Tags, priority, delay and other features are not supported (yet). Here\'s an example that will publish a message with the title `You've Got Mail` to topic `sometopic` (see [ntfy.sh/sometopic](https://ntfy.sh/sometopic)):

<figure>
<p><img src="../static/img/screenshot-email-publishing-gmail.png" width="500" alt="e-mail publishing" /></p>
<figcaption>Publishing a message via e-mail</figcaption>
</figure>

## Phone calls[¶](#phone-calls "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYuODUgNi43NHEuMDE1IDAgMCAwTTIxLjI4IDguNmMtLjQzLTEuMDUtMS4zMi0yLjE4LTIuMDEtMi41NC41NiAxLjExLjg5IDIuMjIgMS4wMiAzLjA0di4wMmMtMS4xMy0yLjgyLTMuMDUtMy45Ni00LjYyLTYuNDQtLjA4LS4xMi0uMTctLjI1LS4yNC0uMzgtLjA0LS4wNy0uMDctLjE0LS4xMS0uMjEtLjA2LS4xMy0uMTItLjI2LS4xNS0uNCAwLS4wMS0uMDEtLjAyLS4wMi0uMDJoLS4wM2MtMi4yMiAxLjMtMy4xNSAzLjU5LTMuMzggNS4wNC0uNjkuMDQtMS4zNy4yMS0xLjk5LjUxLS4xMi4wNS0uMTcuMTktLjEzLjMxLjA1LjE0LjIxLjIxLjM0LjE1LjU0LS4yNiAxLjE0LS40MSAxLjc0LS40NWguMDVjLjA4LS4wMS4xNy0uMDEuMjUtLjAxLjUtLjAxLjk3LjA2IDEuNDQuMmwuMDYuMDJjLjEuMDIuMTcuMDYuMjUuMDYuMDUuMDQuMTEuMDYuMTYuMDhsLjE0LjA2Yy4wNy4wMy4xNC4wNi4yLjA5LjAzLjAyLjA2LjAzLjA5LjA1LjA3LjA0LjE2LjA3LjIuMTEuMDQuMDIuMDguMDUuMTIuMDcuNzMuNDUgMS4zNCAxLjA3IDEuNzUgMS44MS0uNTMtLjM3LTEuNDktLjc0LTIuNDEtLjU4IDMuNiAxLjgxIDIuNjMgOC0yLjM2IDcuNzYtLjQ0LS4wMS0uODgtLjEtMS4zLS4yNS0uMS0uMDMtLjItLjA3LS4yOS0uMTItLjA1LS4wMi0uMTItLjA1LS4xNy0uMDgtMS4yMy0uNjMtMi4yNC0xLjgyLTIuMzgtMy4yNyAwIDAgLjUtMS43MyAzLjMzLTEuNzMuMzEgMCAxLjE3LS44NiAxLjItMS4xIDAtLjA5LTEuNzQtLjc4LTIuNDItMS40NS0uMzctLjM2LS41NC0uNTMtLjY5LS42Ni0uMDgtLjA3LS4xNy0uMTMtLjI2LS4xOWE0LjYzIDQuNjMgMCAwIDEtLjAzLTIuNDVDNy42IDYuMTIgNi44IDYuODYgNi4yMiA3LjVjLS40LS41LS4zNy0yLjE1LS4zNS0yLjUtLjAxIDAtLjMuMTYtLjMzLjE4LS4zNS4yNS0uNjguNTMtLjk4LjgyLS4zNS4zNy0uNjYuNzQtLjk0IDEuMTQtLjYyLjkxLTEuMTIgMS45NS0xLjM0IDMuMDQgMCAuMDEtLjEuNDEtLjE3LjkybC0uMDMuMjNjLS4wMi4xNy0uMDQuMzItLjA4LjU4di40MWMwIDUuNTMgNC41IDEwLjAxIDEwIDEwLjAxIDQuOTcgMCA5LjA4LTMuNTkgOS44OC04LjMzLjAyLS4xMS4wMy0uMjQuMDUtLjM3LjItMS43Mi0uMDItMy41Mi0uNjUtNS4wMyIgLz48L3N2Zz4=)]

You can use ntfy to call a phone and **read the message out loud using text-to-speech**. Similar to email notifications, this can be useful to blast-notify yourself on all possible channels, or to notify people that do not have the ntfy app installed on their phone.

**Phone numbers have to be previously verified** (via the [web app](https://ntfy.sh/account)), so this feature is **only available to authenticated users** (no anonymous phone calls). To forward a message as a voice call, pass a phone number in the `X-Call` header (or its alias: `Call`), prefixed with a plus sign and the country code, e.g. `+12223334444`. You may also simply pass `yes` as a value to pick the first of your verified phone numbers. On ntfy.sh, this feature is only supported to [ntfy Pro](https://ntfy.sh/app) plans.

<figure>
<p><img src="../static/img/web-phone-verify.png" alt="phone number verification" /></p>
<figcaption>Phone number verification in the <a href="https://ntfy.sh/account">web app</a></figcaption>
</figure>

As of today, the text-to-speed voice used will only support English. If there is demand for other languages, we\'ll be happy to add support for that. Please [open an issue on GitHub](https://github.com/binwiederhier/ntfy/issues).

Info

You are responsible for the message content, and **you must abide by the [Twilio Acceptable Use Policy](https://www.twilio.com/en-us/legal/aup)**. This particularly means that you must not use this feature to send unsolicited messages, or messages that are illegal or violate the rights of others. Please read the policy for details. Failure to do so may result in your account being suspended or terminated.

Here\'s how you use it:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl \
        -u :tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2 \
        -H "Call: +12223334444" \
        -d "Your garage seems to be on fire. You should probably check that out." \
        ntfy.sh/alerts

    ntfy publish \
        --token=tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2 \
        --call=+12223334444 \
        alerts "Your garage seems to be on fire. You should probably check that out."

    POST /alerts HTTP/1.1
    Host: ntfy.sh
    Authorization: Bearer tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2
    Call: +12223334444

    Your garage seems to be on fire. You should probably check that out.

    fetch('https://ntfy.sh/alerts', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/alerts", 
        strings.NewReader("Your garage seems to be on fire. You should probably check that out."))
    req.Header.Set("Call", "+12223334444")
    req.Header.Set("Authorization", "Bearer tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2")
    http.DefaultClient.Do(req)

    $Request = @
      Body = "Your garage seems to be on fire. You should probably check that out."
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/alerts",
        data="Your garage seems to be on fire. You should probably check that out.",
        headers=)

    file_get_contents('https://ntfy.sh/alerts', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' =>
                "Content-Type: text/plain\r\n" .
                "Authorization: Bearer tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2\r\n" .
                "Call: +12223334444",
            'content' => 'Your garage seems to be on fire. You should probably check that out.'
        ]
    ]));

Here\'s what a phone call from ntfy sounds like:

Audio transcript:

> You have a notification from ntfy on topic alerts.\
> Message: Your garage seems to be on fire. You should probably check that out. End message.\
> This message was sent by user phil. It will be repeated up to three times.

## Authentication[¶](#authentication "Permanent link")

Depending on whether the server is configured to support [access control](../config/#access-control), some topics may be read/write protected so that only users with the correct credentials can subscribe or publish to them. To publish/subscribe to protected topics, you can:

- Use [username & password](#username-password) via Basic auth, e.g. `Authorization: Basic dGVzdHVzZXI6ZmFrZXBhc3N3b3Jk`
- Use [access tokens](#access-tokens) via Bearer/Basic auth, e.g. `Authorization: Bearer tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2`
- or use either with the [`auth` query parameter](#query-param), e.g. `?auth=QmFzaWMgZEdWemRIVnpaWEk2Wm1GclpYQmhjM04zYjNKaw`

Warning

When using Basic auth, base64 only encodes username and password. It **is not encrypting it**. For your self-hosted server, **be sure to use HTTPS to avoid eavesdropping** and exposing your password.

### Username + password[¶](#username-password "Permanent link")

The simplest way to authenticate against a ntfy server is to use [Basic auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Here\'s an example with a user `testuser` and password `fakepassword`:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShell 7+PowerShell 5 and earlierPythonPHP

    curl \
      -u testuser:fakepassword \
      -d "Look ma, with auth" \
      https://ntfy.example.com/mysecrets

    ntfy publish \
      -u testuser:fakepassword \
      ntfy.example.com/mysecrets \
      "Look ma, with auth"

    POST /mysecrets HTTP/1.1
    Host: ntfy.example.com
    Authorization: Basic dGVzdHVzZXI6ZmFrZXBhc3N3b3Jk

    Look ma, with auth

    fetch('https://ntfy.example.com/mysecrets', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.example.com/mysecrets",
    strings.NewReader("Look ma, with auth"))
    req.Header.Set("Authorization", "Basic dGVzdHVzZXI6ZmFrZXBhc3N3b3Jk")
    http.DefaultClient.Do(req)

    # Get the credentials from the user
    $Credential = Get-Credential testuser

    # Alternatively, create a PSCredential object with the password from scratch
    $Credential = [PSCredential]::new("testuser", (ConvertTo-SecureString "password" -AsPlainText -Force))

    # Note that the Authentication parameter requires PowerShell 7 or later
    $Request = @
    Invoke-RestMethod @Request

    # With PowerShell 5 or earlier, we need to create the base64 username:password string ourselves
    $CredentialString = "$($Credential.Username):$($Credential.GetNetworkCredential().Password)"
    $EncodedCredential = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($CredentialString))
    $Request = @
      Body = "Look ma, with auth"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.example.com/mysecrets",
    data="Look ma, with auth",
    headers=)

    file_get_contents('https://ntfy.example.com/mysecrets', false, stream_context_create([
        'http' => [
            'method' => 'POST', // PUT also works
            'header' =>
                'Content-Type: text/plain\r\n' .
                'Authorization: Basic dGVzdHVzZXI6ZmFrZXBhc3N3b3Jk',
            'content' => 'Look ma, with auth'
        ]
    ]));

To generate the `Authorization` header, use **standard base64** to encode the colon-separated `<username>:<password>` and prepend the word `Basic`, i.e. `Authorization: Basic base64(<username>:<password>)`. Here\'s some pseudo-code that hopefully explains it better:

    username   = "testuser"
    password   = "fakepassword"
    authHeader = "Basic " + base64(username + ":" + password) // -> Basic dGVzdHVzZXI6ZmFrZXBhc3N3b3Jk

The following command will generate the appropriate value for you on \*nix systems:

    echo "Basic $(echo -n 'testuser:fakepassword' | base64)"

### Access tokens[¶](#access-tokens "Permanent link")

In addition to username/password auth, ntfy also provides authentication via access tokens. Access tokens are useful to avoid having to configure your password across multiple publishing/subscribing applications. For instance, you may want to use a dedicated token to publish from your backup host, and one from your home automation system.

You can create access tokens using the `ntfy token` command, or in the web app in the \"Account\" section (when logged in). See [access tokens](../config/#access-tokens) for details.

Once an access token is created, you can use it to authenticate against the ntfy server, e.g. when you publish or subscribe to topics. Here\'s an example using [Bearer auth](https://swagger.io/docs/specification/authentication/bearer-authentication/), with the token `tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2`:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShell 7+PowerShell 5 and earlierPythonPHP

    curl \
      -H "Authorization: Bearer tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2" \
      -d "Look ma, with auth" \
      https://ntfy.example.com/mysecrets

    ntfy publish \
      --token tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2 \
      ntfy.example.com/mysecrets \
      "Look ma, with auth"

    POST /mysecrets HTTP/1.1
    Host: ntfy.example.com
    Authorization: Bearer tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2

    Look ma, with auth

    fetch('https://ntfy.example.com/mysecrets', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.example.com/mysecrets",
    strings.NewReader("Look ma, with auth"))
    req.Header.Set("Authorization", "Bearer tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2")
    http.DefaultClient.Do(req)

    # With PowerShell 7 or greater, we can use the Authentication and Token parameters
    # The Token parameter must be in the form of a System.Security.SecureString

    $Request = @
    Invoke-RestMethod @Request

    # In PowerShell 5 and below, we can only send the Bearer token as a string in the Headers
    $Request = @
      Body = "Look ma, with auth"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.example.com/mysecrets",
    data="Look ma, with auth",
    headers=)

    file_get_contents('https://ntfy.example.com/mysecrets', false, stream_context_create([
        'http' => [
            'method' => 'POST', // PUT also works
            'header' =>
                'Content-Type: text/plain\r\n' .
                'Authorization: Bearer tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2',
            'content' => 'Look ma, with auth'
        ]
    ]));

Alternatively, you can use [Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication) to send the access token. When sending an empty username, the basic auth password is treated by the ntfy server as an access token. This is primarily useful to make `curl` calls easier, e.g. `curl -u:tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2 ...`:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl \
      -u :tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2 \
      -d "Look ma, with auth" \
      https://ntfy.example.com/mysecrets

    ntfy publish \
      --token tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2 \
      ntfy.example.com/mysecrets \
      "Look ma, with auth"

    POST /mysecrets HTTP/1.1
    Host: ntfy.example.com
    Authorization: Basic OnRrX0FnUWRxN21WQm9GRDM3elFWTjI5Umh1TXpOSXoy

    Look ma, with auth

    fetch('https://ntfy.example.com/mysecrets', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.example.com/mysecrets",
    strings.NewReader("Look ma, with auth"))
    req.Header.Set("Authorization", "Basic OnRrX0FnUWRxN21WQm9GRDM3elFWTjI5Umh1TXpOSXoy")
    http.DefaultClient.Do(req)

    # Note that PSCredentials *must* have a username, so we fall back to placing the authorization in the Headers as with PowerShell 5
    $Request = @
      Body = "Look ma, with auth"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.example.com/mysecrets",
    data="Look ma, with auth",
    headers=)

    file_get_contents('https://ntfy.example.com/mysecrets', false, stream_context_create([
        'http' => [
            'method' => 'POST', // PUT also works
            'header' =>
                'Content-Type: text/plain\r\n' .
                'Authorization: Basic OnRrX0FnUWRxN21WQm9GRDM3elFWTjI5Umh1TXpOSXoy',
            'content' => 'Look ma, with auth'
        ]
    ]));

### Query param[¶](#query-param "Permanent link")

Here\'s an example using the `auth` query parameter:

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl \
      -d "Look ma, with auth" \
      "https://ntfy.example.com/mysecrets?auth=QmFzaWMgZEdWemRIVnpaWEk2Wm1GclpYQmhjM04zYjNKaw"

    ntfy publish \
      -u testuser:fakepassword \
      ntfy.example.com/mysecrets \
      "Look ma, with auth"

    POST /mysecrets?auth=QmFzaWMgZEdWemRIVnpaWEk2Wm1GclpYQmhjM04zYjNKaw HTTP/1.1
    Host: ntfy.example.com

    Look ma, with auth

    fetch('https://ntfy.example.com/mysecrets?auth=QmFzaWMgZEdWemRIVnpaWEk2Wm1GclpYQmhjM04zYjNKaw', )

    req, _ := http.NewRequest("POST", "https://ntfy.example.com/mysecrets?auth=QmFzaWMgZEdWemRIVnpaWEk2Wm1GclpYQmhjM04zYjNKaw",
        strings.NewReader("Look ma, with auth"))
    http.DefaultClient.Do(req)

    $Request = @
    Invoke-RestMethod @Request

    requests.post("https://ntfy.example.com/mysecrets?auth=QmFzaWMgZEdWemRIVnpaWEk2Wm1GclpYQmhjM04zYjNKaw",
    data="Look ma, with auth"

    file_get_contents('https://ntfy.example.com/mysecrets?auth=QmFzaWMgZEdWemRIVnpaWEk2Wm1GclpYQmhjM04zYjNKaw', false, stream_context_create([
        'http' => [
            'method' => 'POST', // PUT also works
            'header' => 'Content-Type: text/plain',
            'content' => 'Look ma, with auth'
        ]
    ]));

To generate the value of the `auth` parameter, encode the value of the `Authorization` header (see above) using **raw base64 encoding** (like base64, but strip any trailing `=`). Here\'s some pseudo-code that hopefully explains it better:

    username   = "testuser"
    password   = "fakepassword"
    authHeader = "Basic " + base64(username + ":" + password) // -> Basic dGVzdHVzZXI6ZmFrZXBhc3N3b3Jk
    authParam  = base64_raw(authHeader) // -> QmFzaWMgZEdWemRIVnpaWEk2Wm1GclpYQmhjM04zYjNKaw (no trailing =)

    // If your language does not have a function to encode raw base64, simply use normal base64
    // and REMOVE TRAILING "=" characters. 

The following command will generate the appropriate value for you on \*nix systems:

    echo -n "Basic `echo -n 'testuser:fakepassword' | base64 -w0`" | base64 -w0 | tr -d '='

For access tokens, you can use this instead:

    echo -n "Bearer faketoken" | base64 -w0 | tr -d '='

## Advanced features[¶](#advanced-features "Permanent link")

### Message caching[¶](#message-caching "Permanent link")

Info

If `Cache: no` is used, messages will only be delivered to connected subscribers, and won\'t be re-delivered if a client re-connects. If a subscriber has (temporary) network issues or is reconnecting momentarily, **messages might be missed**.

By default, the ntfy server caches messages on disk for 12 hours (see [message caching](../config/#message-cache)), so all messages you publish are stored server-side for a little while. The reason for this is to overcome temporary client-side network disruptions, but arguably this feature also may raise privacy concerns.

To avoid messages being cached server-side entirely, you can set `X-Cache` header (or its alias: `Cache`) to `no`. This will make sure that your message is not cached on the server, even if server-side caching is enabled. Messages are still delivered to connected subscribers, but [`since=`](../subscribe/api/#fetch-cached-messages) and [`poll=1`](../subscribe/api/#poll-for-messages) won\'t return the message anymore.

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl -H "X-Cache: no" -d "This message won't be stored server-side" ntfy.sh/mytopic
    curl -H "Cache: no" -d "This message won't be stored server-side" ntfy.sh/mytopic

    ntfy publish \
        --no-cache \
        mytopic "This message won't be stored server-side"

    POST /mytopic HTTP/1.1
    Host: ntfy.sh
    Cache: no

    This message won't be stored server-side

    fetch('https://ntfy.sh/mytopic', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/mytopic", strings.NewReader("This message won't be stored server-side"))
    req.Header.Set("Cache", "no")
    http.DefaultClient.Do(req)

    $Request = @
      Body = "This message won't be stored server-side"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/mytopic",
        data="This message won't be stored server-side",
        headers=)

    file_get_contents('https://ntfy.sh/mytopic', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' =>
                "Content-Type: text/plain\r\n" .
                "Cache: no",
            'content' => 'This message won't be stored server-side'
        ]
    ]));

### Disable Firebase[¶](#disable-firebase "Permanent link")

Info

If `Firebase: no` is used and [instant delivery](../subscribe/phone/#instant-delivery) isn\'t enabled in the Android app (Google Play variant only), **message delivery will be significantly delayed (up to 15 minutes)**. To overcome this delay, simply enable instant delivery.

The ntfy server can be configured to use [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging) (see [Firebase config](../config/#firebase-fcm)) for message delivery on Android (to minimize the app\'s battery footprint). The ntfy.sh server is configured this way, meaning that all messages published to ntfy.sh are also published to corresponding FCM topics.

If you\'d like to avoid forwarding messages to Firebase, you can set the `X-Firebase` header (or its alias: `Firebase`) to `no`. This will instruct the server not to forward messages to Firebase.

Command line (curl)ntfy CLIHTTPJavaScriptGoPowerShellPythonPHP

    curl -H "X-Firebase: no" -d "This message won't be forwarded to FCM" ntfy.sh/mytopic
    curl -H "Firebase: no" -d "This message won't be forwarded to FCM" ntfy.sh/mytopic

    ntfy publish \
        --no-firebase \
        mytopic "This message won't be forwarded to FCM"

    POST /mytopic HTTP/1.1
    Host: ntfy.sh
    Firebase: no

    This message won't be forwarded to FCM

    fetch('https://ntfy.sh/mytopic', 
    })

    req, _ := http.NewRequest("POST", "https://ntfy.sh/mytopic", strings.NewReader("This message won't be forwarded to FCM"))
    req.Header.Set("Firebase", "no")
    http.DefaultClient.Do(req)

    $Request = @
      Body = "This message won't be forwarded to FCM"
    }
    Invoke-RestMethod @Request

    requests.post("https://ntfy.sh/mytopic",
        data="This message won't be forwarded to FCM",
        headers=)

    file_get_contents('https://ntfy.sh/mytopic', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' =>
                "Content-Type: text/plain\r\n" .
                "Firebase: no",
            'content' => 'This message won't be stored server-side'
        ]
    ]));

### UnifiedPush[¶](#unifiedpush "Permanent link")

Info

This setting is not relevant to users, only to app developers and people interested in [UnifiedPush](https://unifiedpush.org).

[UnifiedPush](https://unifiedpush.org) is a standard for receiving push notifications without using the Google-owned [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging) service. It puts push notifications in the control of the user. ntfy can act as a **UnifiedPush distributor**, forwarding messages to apps that support it.

When publishing messages to a topic, apps using ntfy as a UnifiedPush distributor can set the `X-UnifiedPush` header or query parameter (or any of its aliases `unifiedpush` or `up`) to `1` to [disable Firebase](#disable-firebase). As of today, this option is mostly equivalent to `Firebase: no`, but was introduced to allow future flexibility. The flag additionally enables auto-detection of the message encoding. If the message is binary, it\'ll be encoded as base64.

### Matrix Gateway[¶](#matrix-gateway "Permanent link")

The ntfy server implements a [Matrix Push Gateway](https://spec.matrix.org/v1.2/push-gateway-api/) (in combination with [UnifiedPush](https://unifiedpush.org) as the [Provider Push Protocol](https://unifiedpush.org/developers/gateway/)). This makes it easier to integrate with self-hosted [Matrix](https://matrix.org/) servers (such as [synapse](https://github.com/matrix-org/synapse)), since you don\'t have to set up a separate push proxy (such as [common-proxies](https://github.com/UnifiedPush/common-proxies)).

In short, ntfy accepts Matrix messages on the `/_matrix/push/v1/notify` endpoint (see [Push Gateway API](https://spec.matrix.org/v1.2/push-gateway-api/)), and forwards them to the ntfy topic defined in the `pushkey` of the message. The message will then be forwarded to the ntfy Android app, and passed on to the Matrix client there.

There is a nice diagram in the [Push Gateway docs](https://spec.matrix.org/v1.2/push-gateway-api/). In this diagram, the ntfy server plays the role of the Push Gateway, as well as the Push Provider. UnifiedPush is the Provider Push Protocol.

Info

This is not a generic Matrix Push Gateway. It only works in combination with UnifiedPush and ntfy.

## Public topics[¶](#public-topics "Permanent link")

Obviously all topics on ntfy.sh are public, but there are a few designated topics that are used in examples, and topics that you can use to try out what [authentication and access control](#authentication) looks like.

  Topic                                            User                    Permissions              Description
  ------------------------------------------------ ----------------------- ------------------------ --------------------------------------
  [announcements](https://ntfy.sh/announcements)   `*` (unauthenticated)   Read-only for everyone   Release announcements and such
  [stats](https://ntfy.sh/stats)                   `*` (unauthenticated)   Read-only for everyone   Daily statistics about ntfy.sh usage

## Limitations[¶](#limitations "Permanent link")

There are a few limitations to the API to prevent abuse and to keep the server healthy. Almost all of these settings are configurable via the server side [rate limiting settings](../config/#rate-limiting). Most of these limits you won\'t run into, but just in case, let\'s list them all:

  Limit                        Description
  ---------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Message length**           Each message can be up to 4,096 bytes long. Longer messages are treated as [attachments](#attachments).
  **Requests**                 By default, the server is configured to allow 60 requests per visitor at once, and then refills the your allowed requests bucket at a rate of one request per 5 seconds.
  **Daily messages**           By default, the number of messages is governed by the request limits. This can be overridden. On ntfy.sh, the daily message limit is 250.
  **E-mails**                  By default, the server is configured to allow sending 16 e-mails per visitor at once, and then refills the your allowed e-mail bucket at a rate of one per hour. On ntfy.sh, the daily limit is 5.
  **Phone calls**              By default, the server does not allow any phone calls, except for users with a tier that has a call limit.
  **Subscription limit**       By default, the server allows each visitor to keep 30 connections to the server open.
  **Attachment size limit**    By default, the server allows attachments up to 15 MB in size, up to 100 MB in total per visitor and up to 5 GB across all visitors. On ntfy.sh, the attachment size limit is 2 MB, and the per-visitor total is 20 MB.
  **Attachment expiry**        By default, the server deletes attachments after 3 hours and thereby frees up space from the total visitor attachment limit.
  **Attachment bandwidth**     By default, the server allows 500 MB of GET/PUT/POST traffic for attachments per visitor in a 24 hour period. Traffic exceeding that is rejected. On ntfy.sh, the daily bandwidth limit is 200 MB.
  **Total number of topics**   By default, the server is configured to allow 15,000 topics. The ntfy.sh server has higher limits though.

These limits can be changed on a per-user basis using [tiers](../config/#tiers). If [payments](../config/#payments) are enabled, a user tier can be changed by purchasing a higher tier. ntfy.sh offers multiple paid tiers, which allows for much hier limits than the ones listed above.

## List of all parameters[¶](#list-of-all-parameters "Permanent link")

The following is a list of all parameters that can be passed when publishing a message. Parameter names are **case-insensitive** when used in **HTTP headers**, and must be **lowercase** when used as **query parameters in the URL**. They are listed in the table in their canonical form.

Info

ntfy supports UTF-8 in HTTP headers, but [not every library or programming language does](https://www.jmix.io/blog/utf-8-in-http-headers/). If non-ASCII characters are causing issues for you in the title (i.e. you\'re seeing `?` symbols), you may also encode any header as [RFC 2047](https://datatracker.ietf.org/doc/html/rfc2047#section-2), e.g. `=?UTF-8?B?8J+HqfCfh6o=?=` ([base64](https://en.wikipedia.org/wiki/Base64)), or `=?UTF-8?Q?=C3=84pfel?=` ([quoted-printable](https://en.wikipedia.org/wiki/Quoted-printable)).

  Parameter         Aliases                                      Description
  ----------------- -------------------------------------------- -----------------------------------------------------------------------------------------------
  `X-Message`       `Message`, `m`                               Main body of the message as shown in the notification
  `X-Title`         `Title`, `t`                                 [Message title](#message-title)
  `X-Priority`      `Priority`, `prio`, `p`                      [Message priority](#message-priority)
  `X-Tags`          `Tags`, `Tag`, `ta`                          [Tags and emojis](#tags-emojis)
  `X-Delay`         `Delay`, `X-At`, `At`, `X-In`, `In`          Timestamp or duration for [delayed delivery](#scheduled-delivery)
  `X-Actions`       `Actions`, `Action`                          JSON array or short format of [user actions](#action-buttons)
  `X-Click`         `Click`                                      URL to open when [notification is clicked](#click-action)
  `X-Attach`        `Attach`, `a`                                URL to send as an [attachment](#attachments), as an alternative to PUT/POST-ing an attachment
  `X-Markdown`      `Markdown`, `md`                             Enable [Markdown formatting](#markdown-formatting) in the notification body
  `X-Icon`          `Icon`                                       URL to use as notification [icon](#icons)
  `X-Filename`      `Filename`, `file`, `f`                      Optional [attachment](#attachments) filename, as it appears in the client
  `X-Email`         `X-E-Mail`, `Email`, `E-Mail`, `mail`, `e`   E-mail address for [e-mail notifications](#e-mail-notifications)
  `X-Call`          `Call`                                       Phone number for [phone calls](#phone-calls)
  `X-Cache`         `Cache`                                      Allows disabling [message caching](#message-caching)
  `X-Firebase`      `Firebase`                                   Allows disabling [sending to Firebase](#disable-firebase)
  `X-UnifiedPush`   `UnifiedPush`, `up`                          [UnifiedPush](#unifiedpush) publish option, only to be used by UnifiedPush apps
  `X-Poll-ID`       `Poll-ID`                                    Internal parameter, used for [iOS push notifications](../config/#ios-instant-notifications)
  `Authorization`   \-                                           If supported by the server, you can [login to access](#authentication) protected topics
  `Content-Type`    \-                                           If set to `text/markdown`, [Markdown formatting](#markdown-formatting) is enabled