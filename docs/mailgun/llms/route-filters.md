# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/receive-forward-store/route-filters.md

# Route Filters

Route filters are expressions that decide when an action is triggered. A filter is created based on the recipient of the incoming email, the headers in the incoming email or use a catch-all filter. Filters support regular expressions in the pattern to give you a lot of flexibility when creating them.

### Match Recipient(pattern)

Matches the SMTP recipient of the incoming message against the regular expression pattern. For example, this filter will match messages going to foo@bar.com:


```JSON
match_recipient("foo@bar.com")
```

You can use Python-style regular expressions in your filter. For example, this will match all messages coming to any recipient at @bar.com:


```JSON
match_recipient(".*@bar.com")
```

Another example, handling plus addressing for a specific recipient:


```JSON
match_recipient("^chris\+(.*)@example.com$")
```

Mailgun supports regexp captures in filters, which allows you to use captured values inside of your actions. The example below captures the local name (the part of email before @) and passes it as a mailbox parameter to an application URL:


```JSON
route filter : match_recipient("(.*)@bar.com")
route action : forward("http://myhost.com/post/?mailbox=\1")
```

You can use named captures as well:


```JSON
route filter : match_recipient("(?P<user>.*?)@(?P<domain>.*)")
route action : forward("http://mycallback.com/domains/\g<domain>/users/\g<user>")
```

### Match Header(header,pattern)

This is similar to match-recipient, only instead of looking at a message recipient, it applies the pattern to an arbitrary MIME header for the message.

The example below matches any message with a word "support" in its subject:


```JSON
match_header("subject", ".*support")
```

The example below matches any message against several keywords:


```JSON
match_header('subject', '(.*)(urgent|help|asap)(.*)')
```

The example below will match any messages deemed spam (if spam filtering is enabled):


```JSON
match_header('X-Mailgun-Sflag', 'Yes')
```

### match_recipient(pattern) AND match_header(header, pattern)

The example below will match any recipient for a domain, then match if the message is in English:


```JSON
match_recipient('^(.*)@example.com$') and match_header("Content-Language", "^(.*)en-US(.*)$")
```

### catch_all()

Will create matches if no proceeding routes matched. Usually, you need to use it in a route with a lowest priority, to make sure it evaluates last.