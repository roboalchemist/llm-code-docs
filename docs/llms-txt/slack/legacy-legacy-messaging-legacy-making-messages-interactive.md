Source: https://docs.slack.dev/legacy/legacy-messaging/legacy-making-messages-interactive

# Legacy making messages interactive

Conversation is central to the chat experience, but messages do more than just communicate. Made interactive, messages inspire decisive, calculated action all from the comfort of Slack.

Provide users with direct paths to goals with [message buttons](/legacy/legacy-messaging/legacy-message-buttons):

Give them the ability to do something with a message via a [message shortcut](/interactivity/implementing-shortcuts#message):

![Once installed, your app&#39;s message shortcuts appear in the More actions section of each Slack message&#39;s context menu, beside the default actions.](/assets/images/actions_ui_preview-62d6f93c2463603270f2cc09c5a1106e.png)

Or let users navigate through more nuanced options with [message menus](/legacy/legacy-messaging/legacy-adding-menus-to-messages):

![Triforce Project PM](data:image/png;base64,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)

## The interactive message framework {#framework}

Interactive messages are much like other messages, only they contain [buttons](/legacy/legacy-messaging/legacy-message-buttons), a variety of [menus types](/legacy/legacy-messaging/legacy-adding-menus-to-messages), or they have some custom [message shortcuts](/interactivity/implementing-shortcuts) available. Rather than remaining mostly static, interactive messages evolve over time.

Message buttons and menus may travel almost anywhere a message goes.

Attach them:

* in response to [slash command](/interactivity/implementing-slash-commands) invocations
* as link attachments in [app unfurls](/messaging/unfurling-links-in-messages)
* in notifications sent by [incoming webhook](/messaging/sending-messages-using-incoming-webhooks)
* as part of messages attached to [message threads](/messaging#threading)
* messages your bot sends out of the honest blue or in response to conversational antics using [`chat.postMessage`](/reference/methods/chat.postMessage)
* or sending messages visible only to a specific user by [`chat.postEphemeral`](/reference/methods/chat.postEphemeral).

Message shortcuts are available on any message, except for those spooky, ghostly [ephemeral messages](/reference/methods/chat.postEphemeral) and the best thing is they haunt appear without needing any initial action, unlike buttons or menus.

Yes, interactive messages work on [Enterprise organizations](/enterprise) and on [Single workspace apps](/app-management/distribution)built for your workspace. a Slack app is required.

### Lifecycle of a typical interactive message flow {#lifecycle}

Whether using buttons, message shortcuts, or menus, interactive messages flow like so:

1. **A message exists, ready for action**. If your app created it, it might have buttons, or it might have menus, and if it's not ephemeral it might have custom message shortcuts available. Now all the users who can read it can interact with it.

2. **Users encounter your message and, inspired by its call to action, clicks or makes a selection**. This triggers an invocation of your application's associated Request URL.

3. **Slack sends a request to your Request URL**, sending all the context needed to identify the originating message, the user executing the action, and the specific values you've associated with the action. This request also contains a `response_url` you can use to continue interacting with the user or channel.

4. **Your app responds to the action**. If responding directly to the incoming invocation request, your provided message will replace the existing message. Or respond with an ephemeral message, visible only to the invoking user. Or respond with just HTTP 200 OK and delay continuing the interaction until later using the provided `response_url`. There are many ways for your app to respond.

5. _Meanwhile_: **Your application does whatever it does** as a result of the intended action to be taken: enqueue a process, save a database row or some prince or princess captured in a castle. All the while your app may continue interacting with users through additional messages and evolving shortcuts.

6. **By using the `response_url`**, your app can continue interacting with users up to 5 times within 30 minutes of the action invocation. Use this to continue through a workflow until it is complete.

7. **Messages can evolve**. By using [`chat.update`](/reference/methods/chat.update) and your created message's `message_ts` field, you can modify the original interactive message (including all of its attachments) to add or remove buttons or menus based on user interactions.

With many users interacting with many messages, this lifecycle repeats itself with all its various decisions and destinations.

Messages are truly a garden of forking paths.

## Interaction types {#interaction_types}

While this document covers common aspects of working with both message menus and message buttons, you'll find even more nuance and detail in each action type's dedicated documentation:

* [Message buttons](/legacy/legacy-messaging/legacy-message-buttons) are brief, decisive, and compelling decision-making aids. We recommend starting with buttons if you're new to interactive messages.
* [Message menus](/legacy/legacy-messaging/legacy-adding-menus-to-messages) allow more studied conclusions to be drawn with dynamic, purpose-driven drop downs.
* [Message shortcuts](/interactivity/implementing-shortcuts#message) are visual ways of interacting with and acting on messages - they're always available once created, no matter whether your app created the initial message or not.

## Readying your application for interactive messages {#readying_app}

Posting messages with buttons requires creating a Slack app.

[Create an app](https://api.slack.com/apps?new_app=1)

### Preparing your Request URL {#preparing-request-url}

Navigate to your [application management tool](https://api.slack.com/apps) and find your app's _Interactive Components_ section.

![A screenshot of the sidebar where you find this dialog](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOcAAAG3CAMAAAB407JRAAAAtFBMVEX39/dHRktlZGjAwMDi4uJ5eXxMS1D///8rj99DQkfX1teCgoVfXmJUU1iIiIuop6mhoKLs7Ozx8fHd3d309fZZWFyQkJOYmJtycnWvrrBram7l5eXT0tOzs7Xo6Om5uLlQT1TPzs/Ix8ZaqOH4+/3Ly8zd7vlzYlHP5vZiUEBRPy4qi9gohdCs1PCDvulEnN+YyeqHd2dwtea6rZ+/3vSYinupnI0ngMc7j840HxkxhcgmfsSeuW5rAAAACXBIWXMAAAsTAAALEwEAmpwYAAAgAElEQVR42u2daXfbRtLv/0BjJ3aCpMTVcrxkcpNzn3sm3/8bPHPm3DyZGSd2bG22KHEniH25LwhQFEUptq+1UOnfC5tCNxosdqPRqOqqAigUCoVyHzCXHy3t45MSrTkfb5HTUeZj8UnJGVqaNyj/4MoPius9LTEheox6rT8teE/wrlRQDl22+F8bP8XZZ6xt9idHnuQ0myYb/fnUoXL+NeTUGo5aayV7PyakET4BObnrEub5DNAt4J+Ag78Dp0r1+Kms+y7nW7XL/3cvEpyYHQOpQ5CDeWsfP7n5Nv+/ae/sLOqzAwAnQA7EL4ZP7/6U/+utBTQGpGEB7eWxqd55cnJ67Jy1GzDinFipAyABUI92XM7ytmRLgTuSsEfCVDUJEk4GAbIMcYj52klWxGVf8f7A3P9DLM9u6s8PDsemZxinKZATIE+85Tr/ksYUafPLr1lPH9O4bcUMICMigDfLSQ7AW+tuAAjBY/gtHmEPOW6fu4RjDVVlmSQGYZEgRgyGvbg8R/CVPIw4dCDbgufoC2S2MYfQngI10TdSOYbMxFZO+ARQcq7Oc5HjzqQoa3iSn1rGAk3GihPbMIPUIZEiqz4QWzOuJnuGXJt9+3F77UdOWA8KgMwDCyCBx+Lqzdg9yedG0jkH3HScVMcESKcN0SNvTa/5QRKmhISiGLbBjZFwlTirLdxARm2MPcCcVbSx2/zIuANVmFpnSbdPoF2oADjXyc5jjkz5r+mv8g0sqB1/1mDiA5Sv3BnrKcvP7Hq9j2ieCUgBgOyf5lzS/Aj4MZ9IOQ4l0de5qekDwZkoRbUx5ycfXrDQB2CDIdBwxGM5HAKozMXq2B5/KJpaPr8EPhlXLr5mXbcaA9Hn3Z//UK+UeWAZsMD55bowDg5xwY0dAOkp5hkCAHNgD4tQBIs5AwlAIMKAhAGa4vEQ/eIB3D8/hgoFgCoiRQ7RwcHlUEEsK4uvuv/Kry32P0/O5A+wxLZtm7UZYDl4waz95jzpVThOQrmiqpTD+iNqVXALYFrWPkIfXSQASaXyZ97LhNMrV12/KT6yJJwYXyOnJyxHnOZ/5nwrVmAaAGAiB8CCARhI3tqKuJ9lmbv6fkHZRhsXGdwQCMvZuIsGBlCACsFR0fx5Sm4RJKnymO99jaADIQXATj97PTTXpxMAk+kEYAsxwdurlfE4lX3f9zm3u1xXiCAAbGCAisdJL4EqikEUI0COGTAFEYtBrz731c1LHmFQwXIiuQh1TL9qanVbKZL9z1/3jQdiNplMshQAmOX7TP4/q0msCn4hiqIo4yNALMl1rQsAoSxmKQsTb0VrnpoAPNMcQkEYzDIxQxWwJFE0g0Fcv/Y+K4aSZAYEaPJSUkHt654hHzWzd/z5corvRywysIRhGAZADhifxNU63guWS6E0jUcIhlHfCABgMo0Jt8C548R9i+sDsOWZ6JyCtMIkdupnQF+NRV/HOZGuCWqR8bjCAn09EgTh6Csflu7o+AveP9EZPlv7IuncRDqoHG1RYndOUyaECCAWmeakWAFr5jEAcyb6lWLmDJ2iqLIAOsOtiuKyrpZ6d/L+eW09BMz23lQZIGUYGCGGnoE/SNLaskYx5jnDcQCQccyknFCjGQBIIZfE5W9YFsUAZvHWL1QejeJ7WscDON6TcqTB8N/GFDkJvH9bNrt1RCTlyqWWbD6dhWT+yPUmACRhSmAwqYNcPeNxppjYdb3JlnELhPthRdHYiQH8Uk1m9YvZbDfFvBy3N9gdwhfHUKxRqkjJAE/B7kDtK6B2Byrno5ezGT5F6cLmNf2QHD9BOfUo2OjPsVZ5emJWLncjrO5PT1We2NANFdX7y+2TolAoFAqFQqFQKBQKhUKhUCgUCgWPYJ/xFRyL928+5cB+GnpuwjIys/f8puKOLDewy37oBb1iq619enmsyvIfAU6CCzRmSOInYM9mAN5kwZ6ub4hyZwD2UwbAUOUaT8CPrtqH9XGGNru+rTkp/BwAILnA/AmMWyVHaI6Kz7FZCbiT6owhAQNwpBC1c2gmipB9qljHQDVgQztjIB714kHzIvd2Q057LEGN3QQAySQAwQucbNQRpvU5AglAlLZmxRadeH8AAGGGnXiu+PUIUUpENbArGRdoarI42xtzqqYocdaQFCVLQcJKhLTJRsgzNkZdFMKAD9WAswymNtkRP9dMHxMgk8dTAQqX8Ui7RwL8C6DmDudApzDv9947KTEvpChYDBrgPcwQfkqxM/PtoK/WDWD8UgNmQXB+w1oCwMBAAB2Sb8rIAQVE0Exnd/ZJjQ7PeMDNAStJkoS9tZN+F5CF/bAOxCyQhP6u+GcT0QOkGOcQlguC+FbHGYeLNKL+fgqMwake8ZzBTvRnW8j1jjlB0Go1oBBH0XtAEw7Xgg+3eu130aYYLKaGAii9ZMKDH+zGfMumyLyUhXI+1bwFiZGprC+FCxKpSc7Fhih4y/lWnaASsZGuLbgsSqEq4tgyfYjhbtyfk30jAEh9ChxHIRAk5yPMCKAzYQgMN8Xghg1dSwKkbKS641TnsDM43Mr7yC4/dm0A6FrXfyhZB8DLKoBud4feV76QSoaw7qaoH+7Ye9kXYqVzCQiZFE8dh1NsqpihUCgUCoVCoVAoFAqF8tfFuVVh2fpszUnVfiT7TXSW59uKl28c1hJj3XTSiZuX4ZAUU/KDP7/WS/jgMiZ8HPYVEBHHrLD3/urRip/f2Ig+/6wQbYc1QOeM2SOR03OB1vGm+f2PWxqR+M+J0da9ADBaixz3sONWjHKApExo6wzY/TlIBY3amFQioOPy+cEYAAyvMtXrMtsUF63AH3OtWVuJZEv2wLZSpqfCloOWE4M1AnRcsM8mL/1QCAkh342wqvoiZOza9IHk5DSlfV7LfHPY0cIgbs0a2qdp3h4CnZM9LsyCUs5sIStTL59+d17ziHJeSbgoC8FPzQozmzOVfDjpjtrZQhkzTY9Vci/VZnmeqtPqqmqgafNB62G2r+iyIMjay+UfhoYDmQOADgOo9bVdYV3wPJbHhH1AZwHsyxyEyvI8tGSjOAy05SoO5BYAprdW1QBaMnkge3YYRZL91gDAPRddTEO2vgxrbKcbUVIFAGFxa6oOgAg5oBelp4EOsFUA3QNmdfRKVQU4/ZoQs98qvsn4UJmj2swGY2BkNtihCQD5bQ2dBQCkbSVWxT8PP6/q/cdxIUCYZrMMwOj4TE8AYMxpNzckZwA4mNdLUi1dSJ9X9V6fK4oI2Z3qUyeE5WZocYfIl/1BTOu9om0P1GkNGyL3gWyJ/+unC2cG4Jg/q+ajW6veq5yph3my9wnhmSrP+CgQnw05fQgArDdhyA0j4IRkF6lc3RJjsJ0rvpUAiRJozOjWqg+DXZin7TUr9m0W65tWrk53lczmz6pSKBQKhUKhUCgUCuUvhX3l/VBpAy8vX8ifc3gS/ryOwEWJJF+qroRZhvhyf//CcW9pUMmz3fDTsQWP26uS7CvVqnELu+Gnw3+yhxPA+Uotubgr4zauDgDAA7qJJPL7UwhpBnHN3gKDNaozoDfn8+4USmobkWFnUlOQrcybcQ3X0RjUzBk6aMXO3OSbCzZ7ZOOWI3J5n440w/ZHK8c4cbTfFicALOJ4gzZ6Ry3OOerAFvmgMZpU0nzC+wFqWYQoq7eGp1XMxEDr90wjc4TH1sEv5TItU4/pAlW5hwoPaEZpb4FgAI5Qh9oAUFHRlsssNnwFYHoAJxMAmg5DVgBTtR/hPPT+MvERcwQMuTVDNfdcdAEowMAe2+kAgJ7aZSothVS1UvmpA8hUgPMAEhGTe3RyJmkZBSJXACBfWVUKe0tJjjYAobS6EFWvlibcQygAyNnyr+FenKQvH91zxZq3l45WJG0BrXQ1U5X2FgCw+/aYGwNY/gu0hPrZeXkrm+AAZOWNfjRxG/1H91yJmXNTHRljNuDOFZxLq3Fb2FuAvJvGSMBahquSwh17jDNUPRWoBNZ8yB8/T8JZscXhAO/tc/3R9efItPih31en47Tm+7XVMEZ4psoZD8D3Rzk7BD8hAZlwZXbURJ0RANp4UsO+fHKRRcVOjiNX0+XHmV/Bcratc+3upnlk3X3Qsq6cc6WImlMoFAqFQqFQKBQKhfKF2MSC0sbux53Urx9y1oKKMkIIpn+5yfz5E8oXKd3ki2EHav8JyXmjSanSVLwudjKO6FL67z7GhnIIK6oN5UQ85nho8oStetnVKGdpmPXGAHRjljpeNlAClmGS5smu9Cd3pte9oxZ440SIMFXFLGOXBpQr1ZSxMPDmAHwiZfkkhi3WM45Md0LtpbNYOZbsLdWupoqVAaUqK6gU4tZVQJHbWHqy6CzacvvePFK+yf1ZOJbwcXP/snMuDSjFLKRUWi2LzLD0ZKlwAHzgtKHuyv1ZcqwkStJdbtgnspqd19dLC8+HyF6Gyy3dJp2P8s7Nt955NmWuG1CWhIbv+34tLjLBSkUgXI24uyZnj8NHsNCirrI0oFwZClMRAI64FGDbttFvAeDstk+sXZNz2q61lfdwkwtWLA0oK6rccgtDNlagZWPLOAbg60NW3MFU8d1LQ4p1czfxlaXJpS1Xn7RrCl/com25+qTzoTtFJ549xezUFAqFQqFQKBQK5UnB3RBgrK3gBq3bA9hXhOJbKkz9i2STZVmu8QQA4fdXAdJWJifCV9FntlluOnnvId4/SeGaEX9pSBmBYUZ2pgMMu4oR5a6igVX4/AbLzSftFA+hp5bbAHDAqF/YnwQAXsqd9aN1fZveYUVPfbj4YIThXQAKU8kXRWwvFKHAUPqwKDW3xhmNcSuTDE30AYAlaQ5gJAZRS0KsVCO56tZ9KXYWuk0EK6hEIEThRVP2jCwDzDTb/5izhBDSnl46w7RUl5Xj+9CbhP3nAPmkAVBOmRZxHfh9GOMZWfmwVJKmNkdiTyMjI1eNLlxq990G2GzP9GAsSFaB35dVvrkAEEsmuYghpQDEdGm5yRQuXXOG+dh/sRfcx7itoM7CURvYq6+UW6tQYAAMDZzMAXsmOkwXePlsfdyiJ1c5+QDMcvju6QD4mr0MMMbzAHgVDRZAgy0sNwdya80ZRgF6snUvejCJ6/BOVCg2l7G9VqHAuOeii6Sxj246R8gnzea7/pVvNVl6emgn/OU94Y3WIopVtgT7W3OGkYEU7L3IeaQEyWQMXI/tVfqwHA9qLJuCcRiG2a9dyXvqkREAzFgh47dfc8tTZMMZ5r70mmwQsFtje5U+LLW67PYBQfBPT0+vBIZ6zhUq3HRxwG31kZQihJvz7lVnmHuTc2QYhQ1sPnLW42E6LCwWAOsNWbOKxSKxHFIGNFMVhTTe84cA4OzbSNMQnmqvq67Ztm30CeykYxMPgBZ1l4sh1u5YHZvct576pDC9t2u1QFu7euHDYl3EHCONqqNMmQzl0lM0ynN7xC5/lnSm17x0gGp8JZKqnIwt4xh/8IMxqwJwkwvWAnDVGeYBcLrbYoYZewAgvNwIHrb1TGtrEDH7ugvMI7SyvRTM54RvPtKcifh2+a7a0VjQwxF9M6NQKBQKhUKhUCgUCoVCoVAoFAq+sZ56r9hDkcR44jt9bqHK8h+fjpw8gzLI4gZJRJ5Qf1qHN1VPdnXcXu8eNURleYtaOoOGPQUsw4cmKUE1yVifZUgdtgtFFJTA5Ph6JeqNV1VbjO6zuubt0P3JcXOQMcxJ15+JSKDA9gAJUBbpAmicQYEQIp+Sy6r2NI0lRO5u+F15qqryEF2YsYYpd+SpQmRhevB7NYBarV7dLDFWw6NVVTOFrjh6uhv3pwsgtQIYgTbipfrhYgHwQIATAf4FcMV7mb+AsaqaAq55vDPz0AVQU84wBXhgCnTzKLx0TN541Mxgrqq6qZSN+MbJboxbPo7jfgyQJEkStobG8WB2W5bOy6oJywHcqbJDfpEe4MVxHC9+359J/N7641RC9YaqSMXIgCTs0HpotDcVBVZJ0J8B5L0RAUCz7wSNU4I+0RfbqqLzKY1xd9u67uK5MgukCAFwMA4Rs8v+DNDnpzYDCEGwrWowSJtzpNwu+fN6thEAYfSeMZBW6zwAzAigM7EWgHOMLVWnCcZJ2BsCO5YcfLl5ybrcqNe1AcBpOTdUtTka1JdCoVAoFAqFQqFQKBQKhULZOawvCkxdRvywyE3qwPtOh6t/pg84q209XOMBQGEIANS1z49MKezjUcad1LbvVGASG4AmSQDgM9j5+JrTydbDhjQFsEhiG2gnCzza/QlilIN9ETJ2bQq0lUiWQ7SVSLZkD+yLeVcQ+dyuTdEg4apeN2l5kqW7AFg7DaFkaRLlYCPdbyuR3JitIn7o/qIR5XKMMrXtqm2iuDCqXHA3WW63y8kHmjYftObVc4W3M1E5ryRclIXg4c0YmUuSQXdK/GxVLzG8jBVnMQAvlj3Y0owXY9iLRfW84nUG7THJtEoy4kPdF6YH4iQHR2ytP6361bJtorgdZTjvyQKk+9ijtR5XvZiTdBbAvsxB2Ad0YRnjQ+cv69U6gLmHIu6HAnUfHcHuyp3lqSa/ivhRxvVYpbZda/u58PLOstzeHlddXVqLVAdAVFg1WQNIguaVepMpnEVW2ggFJWXBxNMcDNxKs9lM0rWIH8u4HqvUtpdt90+qv99Zltvb56Gz5Xx5FgC4LepSPdBCFGNt3FAE6xRHjcrIOgJkhmEM41rEj1Vq28u2nbxv31mW29t/Onkpp5wB4GDeaNZMJMLMy5gd/ozJATD2cAGo7OmViB8lprdMbbu4bJuocQLgCNjr37OczZOOr4RiNmyI3Adyi/U2yOVG5Y/l54WEBQC2DwVIpvshROEQbNtL+5f5aVapba3LtsdK1Dm+oyy3t4/b353J8Cz3TqLs4kS+bb0iKaz7vgiYlYRhAuDUIkPAi+bjcX6xivixokxtu962t99XHirLbde5kql2+6wlOAB484aFsI3tTVjYWnAnWW6/ycKsO2YWvYXnJ7u0X/NrloCZHgS5OQaFQqFQKPhr+SN9H58+OeFa/H825fz+w5Psxmf/2VjHx09zuMab/Sk90fsy+KZ5g/A08mJSOVcz2+7J+SxvfYkAr18D+PHkh63S5+qq0VePuj9f/alnEc8DSDo3uPHMvwcA/PD+kY/bP3dEmQFA0rhpvnZflw5reIT+Kz+GvJvJv+PHCZ7hA37wEi4+xY+hR8TfX0UJq/4L+MFLOCXlf+k8A5Kh+CpQ/wX86H7A915mxm+WDf30y98AvHrz0y8AWtaElX7D6+yTLbJvfnAzTvkXiuZe8xOYIflPeXZResf96f7mKtxv3yOaQJLw6ldVV09acH0G5Ic3vDr69TVe/QqFd5GAlSQpew/mkAVav0j48d+iPitd7qKf3NdA0BsDaJ3MFOXNK2S/taXYff0rq0sxyubCiaJMfLY8uyi9+3HrJCYCZDaSBF4viISOAhzrVhL+PU+6yOFpdpZbiQQ9SRIRSH765TU05K1fXuVReljOS/FxhleHKgBYsLPkpwBhR8oMiUCIkhxlc+/lLDMnUXl2UXr3eup/4LtOhrddvMXr/2gORhABhP8C0DIysK//89M/AOA18BZ4Cbz7ATlODpIKQhZk5cidvPqt/bEXAsAHTIAPc0b5N+TB6evOmwPhN7xbNoeDMMXZs/95VZzNLEvvYx56t/aoieM4j5fHXndPvAAAwo36oRa15so7Dkocp6sEJO9YTOfqOwCwtTiOjTaS/8X9dtJKnFfJmx9XzZnZyckzDuXZRem9rhPedGaSJJVZafns/xgx8KazKee79nurE2KKVJIkab4yvbyaHyyr6nNVkiQJbyOjDe3dPK8f/FI2h8Xk7/9F5quzi9J7k1PE96+gHMoiiYtsJe7xxYAHoB7++MP3XbzpfXj1Q/kM+kV+B+mn33iRj1f3w7vK38zl0BjDF8WUxUt2UAHbkv1+1ls1h/n5eMq+Ls8uSu8vD3Hv3xGy1x9+9cTCtzzWTojSA5K/TX49kQAVb4p5MTmAB7zjXrm/usqbVRP/TIq+ldr49Vd4IN6J97cQ7skJK6+aw4Gi4Ldsdfay9C7nIePnCYyf/xtoJEeQVCfF2xev83SRLI9KDkkX1gJvX1Tr6QKIviMz5D9PgHf/++cJgH++aNTT5f4L6ecpgLfFp3ffqQ5SF0m1zkzffaf+HalbNtf6rc1l9vvV2dKy9NvrTR74/fP1KfYRjlpv7ur985F43iYvvBzSq+md68EeWp/wHVOM8Dvqz1LO756etg8AWu825lv+aaoR+L+a/pZCoVAoFArlS3AsAHi5+SrDbe6Ktb4+31X1JR5635tFZpAV1YvFDQ2QNl+PndXNdW/erH3lXjdxFuGB7Q4R8yI2lT9zOKiORan6Ism6Oztqi8Sd0IyNAmPdAam53K7/tSPXVB983D6bLMeryIRlllpSQaM2lvKU4dn2FADao9ADAA9bfVs6sOWg5cRgjWAz9S1eTviaz0RFqw/np+Nne3wAiExoDjtaGMStWUP7NM2lOO+qur8AAMMrwwFXt/m2MHOmkg8n3VE7WyhjpumxipctZGXq5Xn1lGtIPqKi1YcbuB1WFvZX49bQcCBzAGA8w8rLzmSuuN1t+rYYGtCSjVX19dS39WfLcVu0+nD2z+NMySeF3YB7LrqYhmy9DWAIgFm6+2lSaei+0bflNNABtnot9S1XvM+XrT6gnXeoBcZaltqR2WCH5ob9t+yMP/Vt2Ux9e1Zsi9/S6r3KuXxSnGMtS+3o+ExPrlQ6sTxrqRYt/U9uvMJm6ltSTj3XW8U92rPJmcH5cycdAXBCWG6GFneIfGPRMKkvOkM7HrfxZ74tfrq4kvp274QY0xRbW73H/kyrqedXF6O1LLVB/EzjNlxnvNib5OdM6+RPfVs2U9/6tcyVbGxt9X65dCCxi+XO9uS0XeDPfVuup75d5ay1H2GmWgqFQqFQKBQKhUKh3Cf27a+Um5aWLzO0cP9fgcbwzeIKOAIXJZKiegDAifX5ldKX8DcsLe1s7pvlvqtOzPOyXb9F/UyE2tUNilEaPYQezBY8bm+P8wQbAFR1fDVw2eG13aJhJZe956s/q4o9/HSLOYxhp58VaAx37NfBf7KHE6D6qQ4AfBRe0eF0Lzbrdy8UeMql4m4xHtr6LUnrkk0d3xQPMm5j5wIA/Ma54+H5yGAi3YNT2RvDVvccPxTCnr9macG0DRdx+WUNjwvgL0zX1pV6XJ+DbaVML7UVNjdEoSku0JIQK9VIrrpYhgJrkBDdRBL5/emlEeZbRwm71p9Vr1C2SlIO9JPT7rEHwB0BcEd7PvgsRcK2M6bMxTbxlI20bJbhIZkwAskB7qNDEj+QnTDDbByRtM/vvWezvWyOHpNkzjTxfTgjjSPHI2fgB5YxjkhaFN1hB7+UD5YfDuTn6DK9pQeZIxPAlgkO5NZVSwvIs6ZWhc0v59yO3OkZ6rMWJxPAFhQIlSJKYU9uA7UGOPmgsD0WocB0Hj2mC1Tl3soI882jhF2bh96jGC0ZjjDl3VbL4a51+pqlpZrlUcByhjQoygKvomSnORrNphSHgL660hlAlo5K2glP1kOBBcwRMOSClRHmm0cJuyZnkvqlHj1BSrzRaILbjLKpejjQiHS+MqAlFx/PjwCcMwzTvEFDO2OFjF8LBZYrAJBfGgm/eZSw688V5UIp/ztI93zf9zUeg6B+UwsSMIr0bEOzbqJzenp6Orjp11kccC0cTdxGHwBI2gJa6dqkuCq6MznZ/cR8+dJM9lkMyXsAENzn2Ge4VgLgGGfVK7eOOmjYLVEg2dWuGyaHVSj17XeZs28jTcODA9jnLAAE3LminHOXKbQui+5MzlGkJCcniRKNrIAUxrE+2JiPLAIkfHZ148IJm/kX+TkP+apMqjpn6tFoe2/O9JqXDi5DgY3Tmu/X0stV1D1FCdu2vrU2/r9uZ/nc45c2l7VQYPZ9RAmjUCgUCoVCoVAoFMpu0r3Vv2WNlr0lEv/DosuyLMs3x6JwViYG85ks6N3t/hAbvwdT2WigI/fwwHGzCMMwzM3xuaXz4sO+l8dt5bN05l4t2Gjgk3b60HGzvOzzLBW5dIg/Pu8qg2sNJOd4BPlXAPTmlg/UK4tWJhma6CtpS3VZOd7/mLPE9AGEpBIAQKUSALweSHlbDtn2tHRMWeZuUVLbiAxLdZWUEC5vzfY/5iwhhLSn6M35vDtF2TQKs8s9yanZuq7P2KA+hTVqMF5UjXlm0Ygmi+/ESZ5JJMoVD8CzmSQkGVBjFsAes5Dmrq1wg6xwTClyt+iREth9KQwakeMKeaouJBLleSWX5r2jdmh+6szKpiFyprgI73UeclDhgf0aOkwXePlslThlzWXqgGdk3UGzDqBZh/HMAQy5WzimrFxX9gHUTLTl9jJZi6kCOJBbUBsAKpc5WVYuX/czD4W+7/sDNLkW+jFCPmk23/WtMnHKWsX3cUeP14KyDQeAjaxwTFFLY/7KWu0Dp41LG4adDgDoqb1qeml2uec4hb+ThSK6YByGYfZv8AM76hvJ5rw2KhxTzrZN2c7HdR+YNgBhLRbi0uxy3/EYuURNEgiCf3p6enTTIoGtIFtPanURiIVjisxsTQZ2Oc2MufHqX6ybXe7pubJ8JHrQj5kMWJDEImNtcvlV+92BB6B7XHdlblxFXrO89FMNcHuLMa+NC8eUMnfL2rVsxSfWoGwArGW4Krls2eHDUZqG99WfaZ7neQ4ccbCAUaZMhvLanhM3uWAtAEcvON9bRCcQg6EuaQAa41nmkdIxpcjdstawrw9ZcbBqAPyEBGTCbZpdHmwluOlnYm0WWBtGkvJ4d31fUVuulp4u1vWmbnB12UFuziz4tOI2n2kV+oJHoVAoFAqFQqFQKPhz/a3O8nxb8dYCAzl7hQqnUZsAwH6q+7sm5xb9EBFxzAp7769bVHaYbfYVF2gde984F+qjzL8Clw+AdjISKulg/3FBpYoAAAE6SURBVJjjoW3sGDbT6mmeoHPKOewJ9IqXKf3i2I7cnyKnKe3zWrbKPH9pUVH5CQBoAV9fZqHv9Gsq4fRpNjdFzrqvzPTfqD/TOTyp8hEx0wf2J5xnJik2tI3TRBgBCKxPwB4DVKMRzOWxnZEzzGDpb42pKp1fRv5alqxU58STTTexXNIE5jLgLcpj2KX8ZeNDZb4l8pdGLADIuNHSv4RBlWGYMvjVHWWmv9t8OmRbVnsPGQA7C4os9LPadLJ2zt1kpr/LeajKzvSwsahWq0dwUZu1luY/X5mb+3Pz3PQPrIk9lALeqo1aSh4TEgPFsZ2RM4lj198bYJZLk6lYn4L4pYleE9JZrKUzzAmxIt4PIUznuRgQEqM8totPV/u6GaT0xS79S9ZtKNTnhEKhUCgUCoVCoVAolL8E/w+KqKK5ssbODgAAAABJRU5ErkJggg==)

Here you'll find a interface for setting your Request URL.

![A screenshot of the message actions configuration dialog&quot; class=&quot;padding_top padding_bottom](/assets/images/messages-config-action-url-51504b382e055f5d612091b65776b1db.png)

You can only configure one Request URL for your application. It will receive actions from all clicks happening throughout messages with buttons your app has produced, across all channels and workspaces. It's a master dispatch station of interactivity. If you're familiar with [slash commands](/interactivity/implementing-slash-commands), you'll find it behaves very similarly.

In some ways, you're building a guided API on your servers for responding to interactive messages.

See [Responding to message actions](#responding_to_message_actions) later in this doc for more detail on how to process these requests.

#### Request URL SSL certificate requirements {#request-url-ssl}

Request URLs _must_ point to a TLS-enabled HTTPS URL located on a publicly accessible server with a valid SSL certificate

This [testing tool](https://www.ssllabs.com/ssltest/index.html) can help you understand whether your HTTPS implementation is valid and publicly accessible.

Don't have a SSL certificate yet? Consider using these low-cost providers:

* [Let's Encrypt](https://letsencrypt.org/)
* [CloudFlare](https://www.cloudflare.com/ssl/)

Many find a HTTP proxying tool like ngrok useful while developing their app.

### Asking for the appropriate scopes {#appropriate-scopes}

To post messages with buttons and process their interactions, your app just needs to be capable of posting messages. If you have a [bot user](/legacy/legacy-bot-users) integration, your bot user already has permission to create messages.

Otherwise, you'll need to request [OAuth permission scopes](/legacy/legacy-authentication/legacy-oauth-scopes) involved with posting messages:

* `incoming-webhook` (if you're sending messages via [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks))
* `commands` (if you're using [message shortcuts](/interactivity/implementing-shortcuts#message) or [slash commands](/interactivity/implementing-slash-commands))
* `chat:write:user` (if you're sending interactive messages on behalf of users)
* `chat:write:bot` (if you're sending interactive messages on behalf of a bot identity)

## Building workflows {#building_workflows}

Work may be a four letter word but workflow is eight. They make work great.

Interactive messages simplify multi-step processes requiring guided user input. Straightforward _yes/no/maybe so_, _either/or/or/or_ decisions? Throw them a button or two. Do users need to choose from a litany of refined choices? Let them order from a message menu.

Each interaction moves a workflow toward completion.

### Posting interactive messages {#posting-interactive-messages}

There are many ways to post messages on Slack. Most of them support interactive messages like little attached riders in the conversation storm.

Most interactive messages begin their lives posted using [`chat.postMessage`](/reference/methods/chat.postMessage), [`chat.postEphemeral`](/reference/methods/chat.postEphemeral), or [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks). Perhaps they are notifications, or messages from a readily helpful [bot user](/legacy/legacy-bot-users).

Some messages are _made_ interactive, such as when elements are attached to messages mentioning watched link domains with [app unfurl's](/messaging/unfurling-links-in-messages) [chat.unfurl](/reference/methods/chat.unfurl) method.

Many interactive messages initiate through interaction itself — in response to a user-executed [slash command](/interactivity/implementing-slash-commands) or yet another interaction with a different or even the same (!!) interactive message.

The commonality is that _your_ interactive messages must be posted from a Slack app.

#### Using chat.postMessage, chat.postEphemeral, chat.update, and chat.unfurl {#using-chat}

There's a quirk when posting message attachments, including buttons and menus, to our [Web API](/apis/web-api/) methods. Whether you're posting a message with [`chat.postMessage`](/reference/methods/chat.postMessage) or [`chat.postEphemeral`](/reference/methods/chat.postEphemeral), adding attachments to a link-bearing message with [`chat.unfurl`](/reference/methods/chat.unfurl), or replacing them with [`chat.update`](/reference/methods/chat.update) — they all only understand `application/x-www-form-urlencoded` parameters. But if you're sending messages with `response_url` or in direct response to an invocation or with an incoming webhook, messages are posted purely as `application/json`.

The way out is somewhat confusing but fully functional: `chat.update`, `chat.postMessage`, and `chat.postEphemeral` support an `attachments` parameter that actually expects a URL-encoded string representation of a JSON array of attachments. Say that five times fast, blur your eyes, and apply the same philosophy to the `unfurls` parameter in `chat.unfurl`.

To send an array with a single attachment with a single action like this:

```json
[    {        "callback_id": "tender_button",        "attachment_type": "default",        "actions": [            {                "name": "press",                "text": "Press",                "type": "button",                "value": "pressed"            }        ]    }]
```text

You'll need to stringify (and optionally minify) and URL-encode it into a POST or URL parameter more like:

```text
%5B%7B%22callback_id%22%3A%22tender_button%22%2C%22attachment_type%22%3A%22default%22%2C%22actions%22%3A%5B%7B%22name%22%3A%22press%22%2C%22text%22%3A%22Press%22%2C%22type%22%3A%22button%22%2C%22value%22%3A%22pressed%22%7D%5D%7D%5D
```text

Check out the `callback_id` that identifies the button in this example. **All interactive messages with buttons** require a `callback_id`. Slack uses them to show your app which button a user interacted with.

If working with a well-supported [client library or framework](https://slackcommunity.com), these details are likely blissfully hidden from you.

### Receiving action invocations {#receiving-action-invocations}

When users interact with buttons or menus provided by your app or click on an action associated with your app, you'll receive an action invocation at the Request URL you registered when configuring your Slack app.

There are many ways to respond to this action, but before you do anything you'll want to verify the request in fact came from Slack.

#### Validating Slack requests {#validating-slack-requests}

**Important!** Your Slack application panel contains a `Signing Secret` used for interactive messages and slash commands. You'll find it in the _App Credentials_ section of your app's _Basic Information_ page.

![Admin page with signing secret and verification token](/assets/images/signing_secrets_admin_page-f7bedc42883405cc5d03c586b4905b25.png)

When your Request URL is pinged, [validate the `x-slack-signature` header value you receive](/authentication/verifying-requests-from-slack). If it does not match the signature you compute, do not respond to the request with a 200 OK or other message.

#### Checking the action type {#checking-action-type}

Action payloads include a `type` field, allowing you to determine whether the invoked action originates from an `interactive_message` or other interactive component, like [dialogs](/legacy/legacy-dialogs).

Here's an example of a parsed `payload` dispatched when users select an item from message menus:

```json
{  "type": "interactive_message",  "actions": [    {      "name": "channel_list",      "type": "select",      "selected_options":[        {          "value": "C24BTKDQW"        }      ]    }  ],  "callback_id": "pick_channel_for_fun",  "team": {    "id": "T1ABCD2E12",    "domain": "hooli-hq"  },  "channel": {    "id": "C123ABC456",    "name": "triage-random"  },  "user": {    "id": "U123ABC456",    "name": "sbutterfield"  },  "action_ts": "1520966872.245369",  "message_ts": "1520965348.000538",  "attachment_id": "1",  "token": "lbAZE0ckwoSNJcsGWE7sqX5j",  "is_app_unfurl": false,  "original_message": {    "text": "",    "username": "Belson Bot",    "bot_id": "B9DKHFZ1E",    "attachments":[      {        "callback_id": "pick_channel_for_fun",        "text": "Choose a channel",        "id": 1,        "color": "2b72cb",        "actions": [          {            "id": "1",            "name": "channel_list",            "text": "Public channels",            "type": "select",            "data_source": "channels"          }        ],        "fallback":"Choose a channel"      }    ],    "type": "message",    "subtype": "bot_message",    "ts": "1520965348.000538"  },  "response_url": "https://hooks.slack.com/actions/T1ABCD2E12/330361579271/0dAEyLY19ofpLwxqozy3firz",  "trigger_id": "328654886736.72393107734.9a0f78bccc3c64093f4b12fe82ccd51e"}
```text

Now that that's out of the way, it's time to respond to the action.

### Responding to message actions {#responding}

There are several different ways to respond and each may be used in combination together for richer interactions.

When creating new messages or modifying old ones, consult the [message field guide](/legacy/legacy-messaging/legacy-interactive-message-field-guide) to understand how to construct all the available options.

#### Responding immediately {#responding-immediately}

Respond to the request we send to your Request URL with a JSON message body directly.

You must respond within **3 seconds.** If it takes your application longer to process the request, we recommend responding with a HTTP 200 OK immediately, then use the `response_url` to respond five times within thirty minutes.

Responding immediately with a JSON message body will replace the current message in its entirety by default. If you explicitly indicate that you want to create a new message instead, specify a literal `false` in the `replace_original` field.

#### Responding incrementally with response_url {#responding-response-url}

Use the response URL provided in the post to:

* Replace the current message
* Respond with a public message in the channel
* Respond with an ephemeral message in the channel that only the acting user will see

You'll be able to use a `response_url` _five times_ within _30 minutes_. After that, it's best to move on to new messages and new interactions.

#### Using chat.update to modify the original message {#using-chat-update}

If you created your message using `chat.postMessage`, you can modify the original message with [`chat.update`](/reference/methods/chat.update) by providing the `message_ts` value from the original message.

We helpfully provide the original message in the `original_message` field of your Request URL invocation. The `original_message` is not provided for ephemeral messages. Bot users can modify their messages too!

Interactive messages produced by apps using `chat.update` can continue updating messages beyond any time window restrictions imposed on human members.

#### Responding with an error message {#responding-with-error}

If you would like to let a user know when something goes wrong, return an ephemeral response containing a helpful error message. To do this, either respond directly to the action request, or use the provided `response_url`.

You'll want to send a JSON payload that looks something like this:

```json
{  "response_type": "ephemeral",  "replace_original": false,  "text": "Sorry, that didn't work. Please try again."}
```text

This sets your response as `ephemeral`, neglects to replace the original (since you don't want to spill the beans on your sidebar dialog to everyone else in the channel), and sets the text to display to the user.

### Replacing the original message {#replacing}

By replacing the original message, you can incrementally change that message's content to reflect the actions taken by members. By adding additional interactive messages, you can refine dialog options with users, either by broadcasting to the whole channel or focusing on particular users who've invoked actions via ephemeral messages.

As you replace messages using [`chat.update`](/reference/methods/chat.update) or the `replace_original` option, you cannot change a message's type from `ephemeral` to `in_channel`. Once a message has been issued, it will retain its visibility quality for life.

Since your interactive messages can respond or evolve with additional content and message buttons, this cycle between creating messages, processing responses, and replacing and generating new messages is potentially endless.

Be sure and review those [interactive message guidelines](/surfaces/app-design#messaging).

### Determining user identity against your service {#user-identity}

If your service or application needs to associate a Slack member with a specific account within your product, you'll want to unobtrusively link their account to complete the action.

When your Request URL is triggered, you'll receive the user ID and team ID for the invoker. If they do not yet exist in your system, send them an ephemeral message containing a link they can follow to link accounts on your website.

This is a great opportunity to identify users with [**Sign in with Slack**](/authentication/sign-in-with-slack/).

## Field guide {#field_guide}

While interactive messages are built on top of typical messages, the workflow may involve many stages, with evolving request and response structures.

If you use [`chat.postMessage`](/reference/methods/chat.postMessage) or [`chat.postEphemeral`](/reference/methods/chat.postEphemeral) to send interactive messages, you'll need to handle presenting your message attachments as a JSON string placed within an `application/x-www-form-urlencoded` request parameter while also balancing using straight-forward `application/json` when working with response URLs.

For a comprehensive accounting of all the fields related to interactive messages, please consult the dedicated [field guide](/legacy/legacy-messaging/legacy-interactive-message-field-guide).

## Guidelines and best practices {#guidelines}

Crafting the ideal message is never easy. Adding interactive flows and additional content while maintaining a productive flow of conversation is even harder!

We've put together a collection of [best practices and guidelines](/surfaces/app-design#messaging) to help you build the most effective and unobtrusive messages.

Here are some quick highlights:

* Though messages may contain up to 20 attachments, messages containing buttons or menus shouldn't have more than one or two attachments.
* Each attachment can contain up to 5 message actions, but it's best to keep options limited and decisive.
* Use confirmation dialogs, colors, and differentiated button types (`primary` and `danger`) sparingly.
* Message action buttons, menus, and confirmation dialogs may not contain Slack's formatting markup.

## Glossary {#glossary}

* **Message Button**: A user interface for invoking Attachment Actions. Buttons can be added, removed, changed, and clicked. Clicking a button triggers its associated Attachment Action.
* **Message Action**: A user interface for invoking an app's custom Actions. Actions are added to all non-ephemeral messages posted in channels that the app is installed in.
* **Message Menu**: Another user interface for invoking Attachment Actions. With message menus, a single action may hold many different values for the user to select from. The selection can be pre-populated, dynamically-driven, or you can use a custom type letting you easily utilize user and channel pickers.
* **Interactive Message**: Mutable messages appearing in Slack, providing users with message buttons that applications may respond to and modify.
* **Attachments**: [_Message Attachments_](/messaging/formatting-message-text#attachments) are contained within messages, and typically offer a means to include rich formatting in messages, such as images, color, and lightweight key/value pairs. They may also contain _Attachment Actions_.
* **Attachment Actions**: Objectives a member may interact with within a Message Attachment, executing an _Request URL_. The user will see a message button. The result of an invocation may change something in the calculus universe, and if desired, within the parent interactive message.
* **Request URL**: URLs associated with your application to complete specific attachment actions. Slack will use this URL when members click buttons that trigger Attachment Actions.
* **External Suggestions URL**: URLs associated with your app for dynamically populating message menus with customized options.
