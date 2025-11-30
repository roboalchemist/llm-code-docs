# Source: https://docs.ntfy.sh/

# Getting started[¶](#getting-started "Permanent link")

ntfy lets you **send push notifications to your phone or desktop via scripts from any computer**, using simple HTTP PUT or POST requests. I use it to notify myself when scripts fail, or long-running commands complete.

## Step 1: Get the app[¶](#step-1-get-the-app "Permanent link")

[![](static/img/badge-googleplay.png)](https://play.google.com/store/apps/details?id=io.heckel.ntfy) [![](static/img/badge-fdroid.png)](https://f-droid.org/en/packages/io.heckel.ntfy/) [![](static/img/badge-appstore.png)](https://apps.apple.com/us/app/ntfy/id1625396347)

To [receive notifications on your phone](subscribe/phone/), install the app, either via Google Play, App Store or F-Droid. Once installed, open it and subscribe to a topic of your choosing. Topics don\'t have to explicitly be created, so just pick a name and use it later when you [publish a message](publish/). Note that **topic names are public, so it\'s wise to choose something that cannot be guessed easily.**

For this guide, we\'ll just use `mytopic` as our topic name:

<figure>
<p><img src="static/img/getting-started-add.png" width="500" alt="adding a topic" /></p>
<figcaption>Creating/adding your first topic</figcaption>
</figure>

That\'s it. After you tap \"Subscribe\", the app is listening for new messages on that topic.

## Step 2: Send a message[¶](#step-2-send-a-message "Permanent link")

Now let\'s [send a message](publish/) to our topic. It\'s easy in every language, since we\'re just using HTTP PUT/POST, or with the [ntfy CLI](install/). The message is in the request body. Here\'s an example showing how to publish a simple message using a POST request:

Command line (curl)ntfy CLIHTTPJavaScriptGoPythonPHP

    curl -d "Backup successful 😀" ntfy.sh/mytopic

    ntfy publish mytopic "Backup successful 😀"

    POST /mytopic HTTP/1.1
    Host: ntfy.sh

    Backup successful 😀

    fetch('https://ntfy.sh/mytopic', )

    http.Post("https://ntfy.sh/mytopic", "text/plain",
       strings.NewReader("Backup successful 😀"))

    requests.post("https://ntfy.sh/mytopic",
        data="Backup successful 😀".encode(encoding='utf-8'))

    file_get_contents('https://ntfy.sh/mytopic', false, stream_context_create([
        'http' => [
            'method' => 'POST', // PUT also works
            'header' => 'Content-Type: text/plain',
            'content' => 'Backup successful 😀'
        ]
    ]));

This will create a notification that looks like this:

<figure>
<p><img src="static/img/android-screenshot-basic-notification.png" width="500" alt="basic notification" /></p>
<figcaption>Android notification</figcaption>
</figure>

That\'s it. You\'re all set. Go play and read the rest of the docs. I highly recommend reading at least the page on [publishing messages](publish/), as well as the detailed page on the [Android/iOS app](subscribe/phone/).

Here\'s another video showing the entire process:

<figure>

<figcaption>Sending push notifications to your Android phone</figcaption>
</figure>