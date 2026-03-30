# Source: https://developers.smtp2go.com/docs/adding-attachments.md

# Adding Attachments

Attachments are commonly added to emails and when sending with the [API](https://developers.smtp2go.com/reference/send-standard-email). There are two ways they can be included using the "*attachments*" parameter.

## A fileblob of base64 encoded data

Here’s an example using cURL:

```curl Fileblob
"attachments": [
    {
      "filename": "testfile.pdf",
      "fileblob": "--base64-data--",
      "mimetype": "application/pdf"
   }
]
```

You can encode files using free online services such as [Base64 Encode](https://www.base64encode.org/).

## A URL address where SMTP2GO will fetch the data

You can set a URL pointing to a web address where we will fetch the data rather than having to send it with the POST request. An advantage of using the URL parameter is that it speeds up sending, as you don't need to continually pass data if you send the same attachment in multiple emails. Our system retrieves the attachment data from the URL, and caches it locally for 24 hours, further speeding up sending.

Here’s an example using cURL:

```curl URL
"attachments": [
  {
   "filename": "test.jpg",
   "url": "https://mydomain.com/myimage.jpg,
   "mimetype": "image/jpeg"
  }
]
```

## A full request example - fileblob

A full request example using cURL to send a basic email with a PDF attachment as a fileblob.

```curl cURL - email with attachment
curl --request POST \
     --url https://api.smtp2go.com/v3/email/send \
     --header 'Content-Type: application/json' \
     --header 'X-Smtp2go-Api-Key: api-xxxxxxxxxxxxxxxxxx' \
     --header 'accept: application/json' \
     --data '
{
  "sender": "email@example.com",
  "to": [
    "friend@example.com"
  ],
  "subject": "SMTP2GO attachment",
  "text_body": "Hello - find the email attached",
	"attachments": [
    {
      "filename": "testfile.pdf",
      "fileblob": "--base64-data--",
      "mimetype": "application/pdf"
   	}
	]
  
}
'
```

## Attachment Size

The maximum total email size when sending via the API is 50 MB (this includes content, attachments and headers).