# Source: https://documentation.mailgun.com/docs/mailgun/quickstart.md

# Quickstart: Send Your First Email

Send an email in under two minutes using your sandbox domain

## Step 1: Sign up

1. [Sign up for Mailgun](https://signup.mailgun.com/new/signup) (free)


Info
After creating your account, follow the guided setup in your [Mailgun Dashboard](https://app.mailgun.com/welcome-guide) to activate your account and create your first API key. Both of these things will need to be done during this setup in order for you to continue. You can then choose to continue with the dashboards guide to quickly send your first email, or you can grab your API key and continue below.

1. Go to [API Keys](https://app.mailgun.com/settings/api_security) in your dashboard
2. Copy your **Private API key**


## Step 2: Add Authorized Recipient

First, add your email as an authorized recipient. This will send a verification email to that address.

cURL

```bash
curl -X POST \
  "https://api.mailgun.net/v5/sandbox/auth_recipients?email=your-email@example.com" \
  --user 'api:YOUR_API_KEY'
```

Node.js

```javascript
fetch('https://api.mailgun.net/v5/sandbox/auth_recipients?email=your-email@example.com', {
  method: 'POST',
  headers: {
    'Authorization': 'Basic ' + Buffer.from('api:YOUR_API_KEY').toString('base64')
  }
})
.then(res => console.log('Status:', res.status))
.catch(err => console.log('Error:', err.message));
```

Python

```python
import requests

response = requests.post(
    "https://api.mailgun.net/v5/sandbox/auth_recipients?email=your-email@example.com",
    auth=("api", "YOUR_API_KEY")
)
print(f"Status: {response.status_code}")
```

Java

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Base64;

public class Main {
    public static void main(String[] args) throws Exception {
        String auth = Base64.getEncoder().encodeToString("api:YOUR_API_KEY".getBytes());
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://api.mailgun.net/v5/sandbox/auth_recipients?email=your-email@example.com"))
            .header("Authorization", "Basic " + auth)
            .POST(HttpRequest.BodyPublishers.noBody())
            .build();
        
        HttpResponse<String> response = HttpClient.newHttpClient()
            .send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println("Status: " + response.statusCode());
    }
}
```

C#

```csharp
using System;
using System.Net.Http;
using System.Text;

var client = new HttpClient();
var auth = Convert.ToBase64String(Encoding.ASCII.GetBytes("api:YOUR_API_KEY"));
client.DefaultRequestHeaders.Authorization = 
    new System.Net.Http.Headers.AuthenticationHeaderValue("Basic", auth);

var response = await client.PostAsync(
    "https://api.mailgun.net/v5/sandbox/auth_recipients?email=your-email@example.com", 
    new StringContent(""));

Console.WriteLine($"Status: {response.StatusCode}");
```

PHP

```php
<?php
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://api.mailgun.net/v5/sandbox/auth_recipients?email=your-email@example.com");
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_USERPWD, "api:YOUR_API_KEY");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
echo "Status: $status\n";
curl_close($ch);
?>
```

Go

```go
package main

import (
    "fmt"
    "net/http"
)

func main() {
    req, _ := http.NewRequest("POST", 
        "https://api.mailgun.net/v5/sandbox/auth_recipients?email=your-email@example.com", nil)
    req.SetBasicAuth("api", "YOUR_API_KEY")
    
    client := &http.Client{}
    resp, _ := client.Do(req)
    fmt.Println("Status:", resp.Status)
}
```

Rust

```rust
use reqwest;

#[tokio::main]
async fn main() {
    let response = reqwest::Client::new()
        .post("https://api.mailgun.net/v5/sandbox/auth_recipients?email=your-email@example.com")
        .basic_auth("api", Some("YOUR_API_KEY"))
        .send()
        .await
        .unwrap();
    
    println!("Status: {}", response.status());
}
```

Important
Check the authorized recipients email inbox and click the verification link before proceeding to Step 2B. You must verify your email address to receive emails from this sandbox domain.

## Step 3: Send Your First Email

Once you've clicked the verification link in your email, you can now send an email to that recipient.

cURL

```bash
curl --user 'api:YOUR_API_KEY' \
  https://api.mailgun.net/v3/YOUR_SANDBOX_DOMAIN/messages \
  -F from='Test <postmaster@YOUR_SANDBOX_DOMAIN>' \
  -F to='your-email@example.com' \
  -F subject='Hello!' \
  -F text='Test message'
```

Node.js

```javascript
const form = new FormData();
form.append('from', 'Test <postmaster@YOUR_SANDBOX_DOMAIN>');
form.append('to', 'your-email@example.com');
form.append('subject', 'Hello!');
form.append('text', 'Test message');

fetch('https://api.mailgun.net/v3/YOUR_SANDBOX_DOMAIN/messages', {
  method: 'POST',
  headers: {
    'Authorization': 'Basic ' + Buffer.from('api:YOUR_API_KEY').toString('base64')
  },
  body: form
})
.then(res => console.log('Status:', res.status));
```

Python

```python
import requests

response = requests.post(
    "https://api.mailgun.net/v3/YOUR_SANDBOX_DOMAIN/messages",
    auth=("api", "YOUR_API_KEY"),
    data={
        "from": "Test <postmaster@YOUR_SANDBOX_DOMAIN>",
        "to": "your-email@example.com",
        "subject": "Hello!",
        "text": "Test message"
    }
)
print(f"Status: {response.status_code}")
```

Java

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Base64;

public class Main {
    public static void main(String[] args) throws Exception {
        String auth = Base64.getEncoder().encodeToString("api:YOUR_API_KEY".getBytes());
        
        String data = "from=Test <postmaster@YOUR_SANDBOX_DOMAIN>" +
                     "&to=your-email@example.com" +
                     "&subject=Hello!" +
                     "&text=Test message";
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://api.mailgun.net/v3/YOUR_SANDBOX_DOMAIN/messages"))
            .header("Authorization", "Basic " + auth)
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(data))
            .build();
        
        HttpResponse<String> response = HttpClient.newHttpClient()
            .send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println("Status: " + response.statusCode());
    }
}
```

C#

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;

var client = new HttpClient();
var auth = Convert.ToBase64String(Encoding.ASCII.GetBytes("api:YOUR_API_KEY"));
client.DefaultRequestHeaders.Authorization = 
    new System.Net.Http.Headers.AuthenticationHeaderValue("Basic", auth);

var data = new FormUrlEncodedContent(new[] {
    new KeyValuePair<string, string>("from", "Test <postmaster@YOUR_SANDBOX_DOMAIN>"),
    new KeyValuePair<string, string>("to", "your-email@example.com"),
    new KeyValuePair<string, string>("subject", "Hello!"),
    new KeyValuePair<string, string>("text", "Test message")
});

var response = await client.PostAsync(
    "https://api.mailgun.net/v3/YOUR_SANDBOX_DOMAIN/messages", data);

Console.WriteLine($"Status: {response.StatusCode}");
```

PHP

```php
<?php
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://api.mailgun.net/v3/YOUR_SANDBOX_DOMAIN/messages");
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_USERPWD, "api:YOUR_API_KEY");
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query([
    'from' => 'Test <postmaster@YOUR_SANDBOX_DOMAIN>',
    'to' => 'your-email@example.com',
    'subject' => 'Hello!',
    'text' => 'Test message'
]));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
echo "Status: $status\n";
curl_close($ch);
?>
```

Go

```go
package main

import (
    "fmt"
    "net/http"
    "net/url"
    "strings"
)

func main() {
    data := url.Values{
        "from":    {"Test <postmaster@YOUR_SANDBOX_DOMAIN>"},
        "to":      {"your-email@example.com"},
        "subject": {"Hello!"},
        "text":    {"Test message"},
    }

    req, _ := http.NewRequest("POST", 
        "https://api.mailgun.net/v3/YOUR_SANDBOX_DOMAIN/messages",
        strings.NewReader(data.Encode()))
    req.SetBasicAuth("api", "YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/x-www-form-urlencoded")

    client := &http.Client{}
    resp, _ := client.Do(req)
    fmt.Println("Status:", resp.Status)
}
```

Rust

```rust
use reqwest;
use std::collections::HashMap;

#[tokio::main]
async fn main() {
    let mut params = HashMap::new();
    params.insert("from", "Test <postmaster@YOUR_SANDBOX_DOMAIN>");
    params.insert("to", "your-email@example.com");
    params.insert("subject", "Hello!");
    params.insert("text", "Test message");

    let response = reqwest::Client::new()
        .post("https://api.mailgun.net/v3/YOUR_SANDBOX_DOMAIN/messages")
        .basic_auth("api", Some("YOUR_API_KEY"))
        .form(&params)
        .send()
        .await
        .unwrap();
    
    println!("Status: {}", response.status());
}
```

You're response will look like 
 200 ok
{
"id": "[message-id@your-domain.com](mailto:message-id@your-domain.com)",
"message": "Queued. Thank you."
} 

## Step 4: Check Your Inbox

- **Check your inbox** - email should arrive in seconds
- **Didn't get it?** Check spam folder or [view logs](https://app.mailgun.com/mg/reporting/logs)


**ð That's it!** You just sent an email through Mailgun.

## Step 5: Get production ready

Now that you've sent your first email, here's how to level up:

Set up your own domain
Move from sandbox to your custom domain..

Domain verification guide
DNS setup and verification process.

#### Send more email

Send to multiple people
Batch sending with personalization variables.

Use HTML templates
Create beautiful, branded emails.

Track opens & clicks
Monitor engagement with detailed analytics.

#### Go beyond basic sending

Set up webhooks
Get real-time notifications for email events.

Receive emails 
Parse and route incoming emails to your app.

Manage mailing lists
Build and maintain subscriber lists.

Email validation
Verify email addresses before sending.