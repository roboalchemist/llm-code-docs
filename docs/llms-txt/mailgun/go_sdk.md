# Source: https://documentation.mailgun.com/docs/mailgun/sdk/go_sdk.md

# Golang

a
img

    Official Mailgun Go SDK

### Installation

If you are using [golang modules](https://go.dev/wiki/Modules) make sure you
include the `/v5` at the end of your import paths


```bash
$ go get github.com/mailgun/mailgun-go/v5
```

### Usage

Here's a simple example of how to send an email.
As always, please consult the repository readme for full details.


```go
package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"github.com/mailgun/mailgun-go/v5"
)

// Your available domain names can be found here:
// (https://app.mailgun.com/mg/sending/domains)
var yourDomain = "your-domain-name" // e.g. mg.yourcompany.com

// You can find the Private API Key in your Account Menu, under "Account Settings":
// (https://app.mailgun.com/settings/api_security)
var privateAPIKey = "your-private-key"

func main() {
	// Create an instance of the Mailgun Client
	mg := mailgun.NewMailgun(privateAPIKey)
	
	// When you have an EU domain, you must specify the endpoint:
	// mg.SetAPIBase(mailgun.APIBaseEU)

	sender := "sender@mg.yourcompany.com"
	subject := "Fancy subject!"
	body := "Hello from Mailgun Go!"
	recipient := "recipient@example.com"

	// The message object allows you to add attachments and Bcc recipients
	message := mg.NewMessage(yourDomain, sender, subject, body, recipient)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second*10)
	defer cancel()

	// Send the message with a 10-second timeout
	resp, err := mg.Send(ctx, message)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("ID: %s Resp: %s\n", resp.ID, resp.Message)
}
```