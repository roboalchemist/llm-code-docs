Source: https://docs.slack.dev/legacy/legacy-messaging

# Legacy messaging

Messages are the basic building block of all conversations on Slack.

Messages notify, communicate, and motivate. They invite response. To have their buttons pressed. Their wit awarded. Sometimes messages even inspire people to do the best work of their lives.

![A gorgeous message](data:image/png;base64,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)

Slack messages are part message, part medium. Posting messages means sending not only a bundle of words, but also a series of attributes both describing and containing content.

We have a lot to say about messages. This particular document is a primer, a jumping off point for further adventures in messaging.

## Composing messages {#composing_messages}

A local comic book store uses Slack to keep its staff informed and engaged in their collective hobby turned vocation. The owner set up an incoming webhook to notify employees when new issues hit the shelves.

![A short message from a comic book shop](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAegAAAAvCAMAAAAfFKmGAAACfFBMVEX////29ve4ubowMTQsLTD+/v7x8fH39/c9PEDy8/O/v8D5+fnWE17eoR1CQ0bZ2do0NTgysYqqq6yur7A/P0Kzs7ZcXV/09PR/f4Hp6er8/P3u7u5UVVdHSEo0s41vb3H7+/ulpqdxcnTU1NV4eHpMTVBra204OTzy8fKDg4Wam5y2trexsbNlZmjQ0NFXWFrh4eJfX2Le399FRUnv7+9ow9R6e33w8/IuLzLj4+Q6Oz5hYmRQUVNKS07l5ebIyMnKysvn5+ienqDs7OyGhojS0tPioBxaW11mw9POztCVlJf19fZkZGdPT1LYFGDGxsfCwsOkpKW8vL3y8fVoaGvb29yMjI5SUlXMzc7W1tfiniHv9veYmJp1dniSk5SgoKKioqTbEl/FxcaoqKnTFFr6+vvCwsfc3N2Qj5KIiYuFhodrwdOWlpg3rIjs9PRnxM7IDA1uwM2mpq25uL6qqrHl9vhlxMgWjnitrbTaohv0+/v58PpgfhgnDTC85eHZpTmJzdn78OD87fXY8fD77+7coCfO7OvQG2T7+fBbvqBrv6eZ18baTYVLsZTmw3fcZZXz3a3zvNP63+7x8ubVoSeFxchApZLIGF7d3d1+y7TYLnDk9PGh097KCy9Zgh2/FQE4BjHmsErrzpPngq3abl341eHdt2H558p1wMkqo4LGNG+amjMvkop4fw5joXHmncDPE0nv7dLGPBGg2uRyuKCy3+aXrW6t39HddXJXt7ffcCJAfHjLoyLohzG4myFwxb7hqFcsT1WVuaacHVyKsIvRN0KtvojL2bXvtLKrZYl8aIBUiT/yrYCPFFMeKzx5DUm+HWhWCTqqHWLq6OvgeZELAAAACXBIWXMAAAsTAAALEwEAmpwYAAARZElEQVR42u2be1DTZ7rHPwm5kHAJEAIkCISEi4JcBRW1KOANraK2Wt1tu5122nXP9syZqTM7nZ7Zc9npdDtzZvePs+5ZZ50624utra3VonVbvIEoioiIIHILIndCuIVbCEnOHwmSULptbc+ZTiffGYb393u/7/P8fu/ze5/3fZ/3CXjhhRdeeOGFF1544YUXXnjhhRdeeOEBgefl7xR2W+Are1k++thHf5r+oZVJF75t8Zrh/9nQ/237LcBeQL/xTuu2f6mYx841Y6uFlz8S9n6txPy6yMl7XkP/2ODjNpqff+UiAHVLOZa7OMJyTZdUa/Ngt+8syWgi/UtLdN/XCXyxv21genLhOtHCt21eM/zfQzhnZ/mvHpaP7a6w2wFVisSTfkN1bi0WgmpB+qJnlcbpHI7eWMYS160CDQDayIfarNatm0OA7T5xm9eQaLVarVZfdykKPQCZB+QFUCA/kAmQfuDAjky0B2QAkQe8Vvs+I/qotCS2DSC/jTqSJ6cihobYmbc34aI7vVtk9UluRzKWqhkwqGJ799clGOU+O+7GCUkK7gOIMvflVvhZeKFho+5y6DJDnHCPrWXzuBlApF0zGkD7uM/K9rCwoPJM++JwUWZsq9uIVj8XeRPIbT2fm3FTVCR6fyarHfwi/xxcoL6tvWsFXjLVeM323THrTV+/2H8hfzcmuEA+Si4U8vu/Thv6kb/2hjvfV/QgtfKpt3PH24Pk3ba5GX7MP9gXIK8i+Z6VTR8BlU+GHdeJGTOZlpzb/pGLN1A+vaOj605YC/iaWkih3H2Z4DdzbjkaR09onPG8bRFVl4jLLgMaHRXaMwKVn6KHXEK8Vnt01/16Xk7Yv2ICpTI/n7Dly49MDRyuf+GVN998XfGax5BO4nTox8TWB/YaigZkcxXpxeeci7uu8WEqpIDo0HuUroGrd6O5OuuZk5O3D91ZN9UGqBPWz3+aTUv64It9JNSAau1SFdSIXVUBa0E0g3iw1Gu072HorOM8XnHhgglMF8Jylk9FWM2/PjcJmHkz2KPBpbWsH6eLNXCDfXP3nctwcRPhCWMYrQA4VESAmkuEz9LCE0oU0/UbAfS0znsYvaQMSPkjM/nQKgpvhfxpgOwDr763CHrGM3esqvIa7dENffTv3EHJbi74FB5JXjzpU3X3ep6vrchsBt447NGin1KIpByyMU2Q61G5ekASlZCQSJTz8zHSDGClw1U/cuFTW0ua8PI0MFjaNu9hiu4kK/3XAmerQdnRoYTqLwBG770zcRhwbNR3eW32PeZoB2Bit0/h0w/8e3yqagZu6WDdME+/B2D/arMHye0R8lOhZ+Oo39LVOHf/HpGnIZ2+HIhPamX3u3GInzs34DdHie1NqLbm+p9b0/eVbdUfQT1WKg7r6nzqr9pl76rXN9/fZq4HGl3+evKmodVrs0cf0a9XARQlLPbvkdzr77tX05lqMCgumbVOzquvfaXZRWvi8Gh4qGU89UZ5WvbD25IJiRioCWcE2pr7wruBrtOj2x2zc3R8vCiymgR9hV9Nx9TCjxT6FH4zqr1/6ar6y17VjOeUXOK18/eJjF07lgZKSaNg2HKvWAcG0Bl8di3O+OIUZuCff7dQmOvZwwAC+fiCgl84GiTscUBcZ1zbzw5/NTIWNPy1kTFNt/OPh/+8+GFcd0uaEl8fxfX/GQ0cwgA6aN/WqRxtAAiAyIVaWpzWc4x/rexZI40fXqBymH/YrttThBc/zBwd6fNW8baXEkZTa0EHQAxgMWvNziXUIwi+HxnWC+AfOeQNav9YImNFn9wqpkmtyJXN9OLaTYWVz8jChdq2aSlkn/vugtuGOp3briGzt5d/LIuxezHF27ahEkWzImO24vMttYwKMAcAf/b200/EdR/cBnQZg79MnvXSBupjWgjWOi3txU9jRLc7y6qQfWlzNQZqT6j8n8bsdb0/GUPHbwM4iCjh4amlDh2ptkvRSwB+7e2nn4ahdcXFkMNIo3uwyqDAh1vmpwlwG9Jbn1EDrH32u2nxWz137k1M/oIc31TPa9Wm+Rt3MfByEUCqTqfT6XTPybd5UnJ0Op1Ot2F+pGA+bTa8o9vhKhXFf6tEq4URkqEEXsxPWJ6KdtUvPep2PAXAJqH7Ta3rJH9DnFP++l2uiiV7vklXji5ztpj6zDeRI/c8/kyqh6FNUFxMTr3EjgGDwWAAAxkrsJ0YCuLp/zo09759H9i0QN3fv5uhZyaWzF0EahbkWOft1u1B8wjRYcD9ywCikRF1wMhI9Z5OT0p4u9lsNnuEbOXhMJ/mwnpxnasUuvAGMivuW7zbruS4KaC0c+lYoDa68h3PL6XJudf0sGDhSef/srBggNRLBldFwOA36EptfjAzW657/xvIAnm1SFH/S3dDu763gdKIBNdoNmQAK/a/yOgaeXV1inv/L38Ev2G5Vf+9fY/GMFeuNpk6VSZTrWze+uH2KqPRaDzvfusX60G24DJDNmxUuIriTQuqvJv4LZ6rxnR8HBT9XSfult8X6j2zqCLEALJWj8yr4ixXr6RFAfhu/raZFDss4Y5v32GCzPaTB1dOue+j110GMiaoSLBt1tl6gYy45EvaYNVq46qpbpjLMdL0Fpza2YBcOE6OT1xYzr2d+Tc4JIhq45kWK+T4OFTR/eIYfyKSOjWKfGmEf1BAWoCRx5c0snOMPcYxCI/rTLSJLORIbCrluN3FRqhvUccvvg+CPdMzT91Grqt36dBskYbaxX7m6KBd1Qkdrp4MSLsNxsc6to9N2lAq05Y2Axs7+wF5rAm1ejJsy2BEROGpGGv6dXfaBuEmrbod2FvXF61rR5oXvLp1UcCKZhvC7K7CcEKHNavGcnx+VqnKLYtZ0+EUlifcpFUP7JxOymrIlSYp9J3gtzMkOqvhV+P9EVIzm+tW3Qf8U+tJ9092iCdR+Wfm1g5m3s6LlFjShNIQTT97tb1RY/ZnrqnUzjM4e91TdchG6hxrQ2YSE9uJlBpUT9RCWnhf3PATysnlMxTVI1gfKU1vA/DVXFthnf1mBAIHmct6k9bVycPjZen3NyW0sDRwkCL5xDbfHsAxPoh4RY3RbUS/+p+z86Id6Qr+wLZFMZrX9IkK88jJflC6fyddivp0AEH9Y3dXXkhvfd+Pzy5rKXg/GKTThdaoPp6dMSdbpqX0XutXTq+x67ok9PjwwgOppToe4P1EQWqgRjq9Zarb9OxDNmTptZeA7WPR2s+K3HTwSWf39uB0FqX9zc2RmwHbhYhGezyxi+KbWnOAqlG9Xi9dmQDpxsnEdkeKb/PMhbQGD1qN383r48BWQ4KjcxD29PmVOD66eFaEZrVGf8VsU4ckjsRcfaxKkjr487QvXcJq/G5eHw8vaxGdwzZ0WXATKKxuaTiV+9ldhX83fLbKsj8P0m+h9zG0RucSEp0vuiIOOJPXWdFqbentM1k1hSd9kkf16qMOjSuRunpFDUSIohW3G6Wp5QqANf3AVCyjKQafEGtU5ifPE9ssUNQtBagpmTdoHYbRuLMCS0htihmzGrJG2VfaGHLCeRx1n52LTUMe+2gzUJxTwcjqkWZTxoH90kCrzqK8zl1E+nY8Mw8GQxIbgKTW4mcJjj0t23DSp6iSmpVXwNreM1kBZeMjFQKjAyZH7KaOrmMzybVAf/pbOB349veQ2P3immut/Kxrjv3FhviDAKeAlGbmdPQzYD9CNLVdcEftnMdklTFA9EwlKTapJKlMqawGArpyQJt4AqpUw76XF3+KzPrYcVa502Jk8iYjMCkoYfsJ9MUT0zTtOBK2/lCw/GTKrg+sYwLfy9srL3T6nV/UZGSxU5hKJm/Kuj+ZEdU5OrWlpBYoOu2wEGoatIZdBBxNheeNG0rOLW0TTtm7fcKlE2lHgEa5v8ROeId1xC+49+aqU4SENsiVx2f7siJw65nl0neWZL078XaY0mOhoPuUtIyDZFwrKJVsZmLhPa59UHIcWVrTc3OnCTVRq+AD16rKEnNnSbd74sG//xmogPqLbWHa3N8GJdrMTS2Xp6clEs5nR89L92ztSgPCJZqyMnmw9WlNpvzjAIl/N7BO2A1gSAGHeh1AH2IsASEAlwfcP0XHEw69Fd75fI69+3q5c8KUL1/drGVOB8wFbcaSXCtmpkBQ2Qha4crWwZCIyXGgS1BcXHz+3JOwyZcHQTkgcTTOow32VAAIrk4sWVIRT6JimsjhGoaui4MjtX6mpCfjRqrUJ1ATT3QBuIQN9lQgUMaZ/j5DwwX1DsCqsYCsTeJwHsf3/c26Ip6syCc6hpBESnN93wUEM8p745CtG8FeFau7CZo2NkXPuSVRRWp7ByIT8ETyfDP634VxrTArpqzMIVz4QEFvi8md1CjLfvXwwD9ZU1ZWFunqpc9P+6g9kwO7D778MhwcSLan1MdalNenacCkTBQDAZ/O9xcThuRmLukbgAbutq5lXH9vRAbccWbuau6Cdrh/XrMU96Nk+bhZ6A9ozR0P2aOPj0SeAXbaS/ycC3OXDvdVusk1Gqz+XfDSW6NwOe2G/AvXtDX85DFg4gO07UYcIYfBqumYR1Nlvg3w7NRxCBpVVwdD2pf1JFQ6/I7IOpfW3AJVUgdS/ypZpfShMFXm28Q03QYjE9asKkCrNJB7Jfe6ZjZ75r4wnpHPg4s+ZE1ZtUhkBV56qzNLd5+qxU34Bxn7UqsZgIi5n0Xc31/RF9iErBooNwKE3PjKqK1ae/7r1lsjV/K62jnBvtMbP21yLunqh2Z/WxGy7gRkCTxzxl7tefUg/P43OVHBivqmPzRUVppMzuMmS+nR+eKrR6+DdCgEjVBNk7FhDeOxK3oAiVzJ1mTyNDKpPMl3XqvYYQnrMgEqtVmJT5wcsiWjCMlzY39Y2wAgKB0ROLOQZ3UAcC1rTAK/KHRtpB4D+kQOJGMjaUnPk7keyKAPIH2fVNYbgsMH8I3RyDxpU+8CSM8ct9vtg0EhW1MFRT1BFio0kZFMqlO1kn8qcJRDvYpEzJJZYVPvwsfDuch35hRYHaFA2Vm1tDfhYng0wO4MheZ5cbn4asHkx3mpQ/rptKRUCl/ok08KT+UR4E9udGuXOkK8VhdLya6tGvV+pwFuyxRJIFMcEu/oSARo6T0kTvaYK8/vMGtJdQ8yzDaGQs1FUa62kA+CQohaqo28DeIpPVuVWsCnbB/6z25pthxyT+B/dekrBRvCR4ZuD7SLUaJUosR0tdEyLnljgalhF0xmyEO1cdAd1LefM2MRAF0R8sDaBD5RZWj1ivlJfB/OxEZZpQDRKS2WZmuXIjhUkPqJG9s6lZ0PlMSHiZwxj1kdAEzfF8RsFX/o8uLZUkCZCDKyK9QnQuNDgWinG/28JDtx2kiyGkisGtR50owFAFtyIgAC7YaLiuvRywBr0hHQn9SkHDufvB5UvtQnm3NnhRkLQBx0JXDR8PUbaZMCYFA3KS2YJNsKcCMnou9yRE2uwP7z9WVT0elUJD4IvHlTmUNpQjttoVEzKXZWl2dH+FVgeL82Ym3NZuckvWiiEkqNv/EpF5YClGr/lrpM4dFxQ8Oa0MFIAJmvb5XFN2+2MWKTz6LRO5bebfGjx7AZpKFpULvIGHh+D4Bx79kgka5O8MUNz9jPm3rhLdAFBZ+1NDqjKMsr2Tr9xj/akX816WDrGQDxzEL7Pe2G2TWDwFktEFkXYkuFkwvqEDhAoF4oF0Ez5LF9fdEt00FrHP862qw6j2Ny2YwVD43uwqRYQCxySfFTdIMuzTm1iTee8Xw5D2V+iu65Kqmym+U3HAv0Gyz4htrkMx7Xc42dSqRYAHGIa+clC3ZJEAumHyp1C/KFf/o56FL6zk+3OqNl8B9X3vBGif8xkkYeJS81vWni0VU+UmOPaO6f9Fd1BF2ephVM8G/HjnoNyU/z99HhJ4cCzxkrlStZdmfMO5q98MILL7zwwgsvvPDih8D/AofXtGdjzNz8AAAAAElFTkSuQmCC)

To send this formatted text as an [incoming webhook](/messaging/sending-messages-using-incoming-webhooks), the owner followed these very docs you're reading now to construct a JSON hash that formatted the important notification with distinctive italics.

```json
{  "text": "New comic book alert! _The Further Adventures of Slackbot_, Volume 1, Issue 3."}
```text

As effective as that notification is, Slack messages are capable of more unobtrusive ornamentation and interaction opportunities.

If you're wondering how to compose truly great messages — check out our [message guidelines](/surfaces/app-design#messaging).

## Formatting messages {#formatting_messages}

Get your point across with bold, italics, and other markup-fu. If you're familiar with similar markup formats like Markdown, you'll be sending beautiful messages in no time.

### Basic formatting {#simple-formatting}

Make text bold by wrapping it in asterisks (\*) like this:

```text
*Well, this is a bold statement.*
```text

Italics adds emphasis without the gaudiness of being bold. Wrap your text in underscores to italicize.

```text
My _spidey sense_ tells me I'll have to skip lunch today.
```text

Some times you want a line break to appear in your text. Perhaps you're writing poetry about your business' bottom line. Use the special control character `\n` to denote a new line. Yes, that's technically two characters.

```text
The spent cents are tails\nI'll never see wag again
```text

### Code blocks {#code-blocks}

If there's a short bit of code you want to appear inline, wrap a grave accent around it.

Slack will render this kind of text in a readable monotype font.

```text
We should be concerned if the variable value for `radioactive` is `true`.
```text

Finally, if you want to share a larger code block, you'll want to wrap it in multiple grave accents, which sounds like a bad accident waiting to happen but it's not.

Use three accents `\`\`\``before and after your code block, which likely will contain new line characters represented as`\\n\` as suggested above.

````
```\n{\n  "text":"A short self-referential message we're sending in `JSON`."\n}\n```
````

* * *

There's even more to learn about message formatting — more ways to express yourself.

Continue on in **[message formatting](/messaging/formatting-message-text)**.

## Simplify complex interactions with buttons {#simplify_complex_interactions_with_buttons}

Users already can read, respond, and react to messages. There are so many interactive possibilities within those capabilities alone.

But if you really want to solicit specific answers from users, [buttons](/legacy/legacy-messaging/legacy-message-buttons) are the way to go.

Messages containing buttons become even more interactive, as each clicked button sends a request to your servers where you get to decide what happens next:

* Respond with additional messages, even more buttons.
* Using [`chat.update`](/reference/methods/chat.update), your messages can evolve as the consequences of users pressing buttons emerge.
* Each button press sends an identifiable request to your servers where you decide what happens next.

You'll need a Slack app to use message buttons, as they are not supported when sending messages with custom integrations.

Be sure and read all about [message buttons](/legacy/legacy-messaging/legacy-message-buttons) and how actions are invoked.

### Meanwhile, back at work {#meanwhile-back-at-work}

Back at the comic shop, the manager has been busy developing a deeper Slack integration with their inventory management software.

Now when a comic book that's sold out comes back into stock, it's announced to employees and even gives them the opportunity to recommend it.

![Looks like a great comic book is back in stock and it&#39;s time to ask employees what they think](/assets/images/messages-full-featured-405ab9385c8b3926111ede4edce865c6.png)

This message highlights a number of message features. It includes a `text` field with a brief message and an emoji reference. It also contains four message attachments. The final attachment has been assigned a blue bar and contains two buttons, encouraging comic shop employees to click and share their opinion.

Here's the JSON message definition used to create a message like this:

```json
{    "text": "Now back in stock!:tada:",    "attachments": [        {            "title": "The Further Adventures of Slackbot",            "fields": [                {                    "title": "Volume",                    "value": "1",                    "short": true                },                {                    "title": "Issue",                    "value": "3",            "short": true                }            ],            "author_name": "Stanford S. Strickland",            "author_icon": "http://a.slack-edge.com/7f18/img/api/homepage_custom_integrations-2x.png",            "image_url": "http://i.imgur.com/OJkaVOI.jpg?1"        },        {            "title": "Synopsis",            "text": "After @episod pushed exciting changes to a devious new branch back in Issue 1, Slackbot notifies @don about an unexpected deploy..."        },        {            "fallback": "Would you recommend it to customers?",            "title": "Would you recommend it to customers?",            "callback_id": "comic_1234_xyz",            "color": "#3AA3E3",            "attachment_type": "default",            "actions": [                {                    "name": "recommend",                    "text": "Recommend",                    "type": "button",                    "value": "recommend"                },                {                    "name": "no",                    "text": "No",                    "type": "button",                    "value": "bad"                }            ]        }    ]}
```text

[Read all about how to simplify workflows with action-invoking buttons](/legacy/legacy-messaging/legacy-message-buttons).

## Take action! Visual app interactions {#actions}

[Buttons](/legacy/legacy-messaging/legacy-message-buttons) are excellent ways to let users interact with messages _posted by your app_, but what about all those other many, many, many (many) messages that weren't?

Here's where [actions](/interactivity/implementing-shortcuts) come in - once you create a custom action and associate it with your app it'll be available to use with practically any message.

These custom actions provide a visual way for people to interact with your app from Slack - perfect for users who aren't comfortable with the verbose nature of slash commands.

Read our comprehensive [custom actions](/interactivity/implementing-shortcuts) docs to find out how to set them up and start using them with your app.

## How to send messages {#how_to_send_messages}

All this talk about writing a Slack message but so few words on how slipping missives into the system.

Messages enter Slack by way of many avenues, some with differing capabilities and approaches.

### Users typing in a Slack app {#users-typing}

It's worth reminding that users type messages in Slack. They even follow some of the conventions documented here. But applications are capable of quite a few more messaging tricks.

Maybe users add some light formatting or an @mention. After pressing enter, their profound message is delivered to Slack and sent along to all the right members and bot users listening in from afar.

Typically when users post messages, they're sending them [via the Real Time Messaging API](#using_the_real_time_messaging_api).

### Using incoming webhooks {#incoming-webhooks}

An effective way to send messages is with [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks).

Incoming webhooks are capable of handling the most richly formatted messages with parades of interactive buttons.

Sending a message could be as easy as:

```bash
curl -X POST -H 'Content-type: application/json' \--data '{"text":"This is a line of text.\nAnd this is another one."}' \ https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX</code></pre>
```text

Incoming webhooks are ideal for sending notifications.

Find out more in the [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks) and preview your messages with the message builder.

### Using the Web API {#web-api}

Use [`chat.postMessage`](/reference/methods/chat.postMessage) to send messages or [`chat.postEphemeral`](/reference/methods/chat.postEphemeral) to send ephemeral messages using the web API. The token you use will need the `chat:write:bot` or `chat:write:user` [token scope](/legacy/legacy-authentication/legacy-oauth-scopes) applied to it.

[Read more about posting messages with the Web API](/reference/methods/chat.postMessage).

### Using the Real Time Messaging API {#rtm}

To send messages on behalf of the user owning a specific token, post message JSON directly into an open websocket connection in the [Real Time Messaging API](/legacy/legacy-rtm-api).

You cannot provide attachments nor buttons to messages posted over the RTM API. If your bot user needs to send more complex messages, use the web API's [`chat.postMessage`](/reference/methods/chat.postMessage) or [`chat.postEphemeral`](/reference/methods/chat.postEphemeral).

### Responding to slash commands {#slash-commands}

[Slash commands](/interactivity/implementing-slash-commands) are powerful way for users to demonstrate intent. When your command URL is invoked, you can respond with your message in JSON, including attachments or interactive buttons. You can even wait until later to respond by following up with posting more JSON to the invocation's `response_url`. Implementation is very similar to incoming webhooks.

[Message buttons](/legacy/legacy-messaging/legacy-message-buttons) complement the slash command workflow well, especially when using ephemeral messages.

### Responding to message button actions {#message-button-actions}

Each time a [message button](/legacy/legacy-messaging/legacy-message-buttons) is clicked, we send a request to your server and you can take that opportunity to add additional messages or replace the original. As with slash commands, you can also delay your response and perform follow up transformations and new messages.

### Threading messages {#threading}

Our documentation on [message threads](/messaging#threading) describes how messages knit together.

### Message permalinks {#message-permalinks}

Easily generate a permalink URL for any message using [`chat.getPermalink`](/reference/methods/chat.getPermalink).
