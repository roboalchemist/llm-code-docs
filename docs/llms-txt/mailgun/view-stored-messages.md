# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/receive-forward-store/view-stored-messages.md

## Viewing Stored Messages

To access the contents of the stored messages (including raw MIME) you'll need the email's storage URL. This can be found on a Domains Accepted/Delivered/Failed event.

The event can be found through the [Events API](https://mailgun-docs.redoc.ly/docs/mailgun/api-reference/openapi-final/tag/Events/#tag/Events) or through the UI  in the expanded log entry under the Send->Logs section.

### Sample code

Run the following python script with the storage key as a parameter. The script will retrieve the message from Mailgun. In the script the message is saved to "message.eml", which can then be opened in Mozilla Thunderbird for analysis.


```
"""View a message using its Mailgun storage key."""
import os
import sys

import requests

if len(sys.argv) != 2:
  print "Usage: retrieve.py message_key"
  sys.exit(1)

api_key = YOUR_API_KEY

# output filename
filename = "message.eml"

# url for retrieval
domain = "mailgun.com"
key = sys.argv[1]
url = "https://api.mailgun.net/v3/domains/%s/messages/%s"
url = url % (domain, key)

headers = {"Accept": "message/rfc2822"}

# request to API
r = requests.get(url, auth=("api", api_key), headers=headers)

if r.status_code == 200:
  with open(filename, "w") as message:
    message.write(r.json()["body-mime"])
  os.system("thunderbird -file %s" % filename)
else:
  print "Oops! Something went wrong: %s" % r.content
```