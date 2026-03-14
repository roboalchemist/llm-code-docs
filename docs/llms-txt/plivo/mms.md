# Source: https://plivo.com/docs/faq/messaging/mms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MMS

> MMS support, media types, file size limits, and delivery troubleshooting

Frequently asked questions about MMS messaging, supported media types, size limits, and delivery.

***

## What is MMS?

MMS (Multimedia Messaging Service) allows sending images, videos, and audio in addition to text.

**Availability:** US and Canada only

***

## Is MMS supported by all carriers in the US and Canada?

### Major Carriers

* AT\&T, Verizon, T-Mobile (US)
* Rogers, Bell, Fido, Telus, Wind Canada

### Minor Carriers

365 Wireless, Alaska Communication System (ACS), Alltel Wireless, Bluegrass Cellular, Boost Mobile, and others.

***

## How much does it cost to send and receive MMS messages?

| Direction | Cost per Message |
| --------- | ---------------- |
| Outbound  | \$0.0160         |
| Inbound   | \$0.0080         |

Volume discounts available—contact [Plivo Sales](https://www.plivo.com/contact/sales/).

***

## What types of multimedia content does Plivo accept?

| Category  | Formats        |
| --------- | -------------- |
| **Image** | JPEG, PNG, GIF |
| **Video** | MP4, 3GP, MOV  |
| **Audio** | MP3, WAV, AMR  |

See [full list](https://www.plivo.com/docs/messaging/concepts/mms/) of accepted content types.

***

## What are the size limitations for sending messages with text and images?

| Limit                  | Value                       |
| ---------------------- | --------------------------- |
| Total message size     | 5 MB                        |
| Maximum attachments    | 10 files                    |
| Text content           | 1,600 characters (\~4.8 KB) |
| Recommended image size | \< 600 KB                   |

**Note:** Plivo does not resize images. Messages exceeding 5 MB fail with error code 120.

***

## Will Plivo automatically resize my images for MMS messaging?

No. Plivo does not resize images. You must ensure total message size is under 5 MB before sending.

***

## What MMS content types does Plivo support?

Media URLs must return valid `Content-Type` and `Content-Length` headers. URLs without these headers are rejected.

***

## How do I send MMS via API?

```bash  theme={null}
curl -X POST "https://api.plivo.com/v1/Account/{auth_id}/Message/" \
  -u "{auth_id}:{auth_token}" \
  -H "Content-Type: application/json" \
  -d '{
    "src": "14151234567",
    "dst": "14157654321",
    "type": "mms",
    "text": "Check out this image!",
    "media_urls": ["https://example.com/image.jpg"]
  }'
```

***

## How do I send MMS via Powerpack?

Replace `src` with `powerpack_uuid`:

```json  theme={null}
{
  "powerpack_uuid": "your-powerpack-uuid",
  "dst": "14157654321",
  "type": "mms",
  "media_urls": ["https://example.com/image.jpg"]
}
```

***

## How does Plivo manage delivery order of multiple media files via one MMS message?

Send up to 10 files in one message:

```json  theme={null}
{
  "media_urls": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpg"
  ]
}
```

**Note:** Media file order is not guaranteed at delivery.

***

## How can I upload media to an MMS message?

### Via Console

1. Navigate to **Messaging > MMS Media Upload**
2. Upload files
3. Use returned `media_id` in API requests

### Via API

Use the [Media API](https://www.plivo.com/docs/messaging/api/media/) to upload and manage files.

### Hosted Media

Host media on any cloud storage (S3, GCS, etc.) and provide the URL in `media_urls`.

***

## How long does Plivo store MMS media files?

| Feature          | Details             |
| ---------------- | ------------------- |
| Storage duration | Up to 1 year        |
| URL type         | Publicly accessible |
| Extension        | Case-by-case basis  |

Media files sent or received are stored in your account with unique URLs.

***

## How can I retrieve Plivo MMS media files?

**Via SDK:** Use the list media method

**Via API:** Use the [Media API](https://www.plivo.com/docs/messaging/api/media/)

***

## How do I receive MMS messages?

1. Set `message_url` on your Plivo application
2. Assign MMS-enabled number to application
3. Plivo POSTs inbound MMS to your URL

### Inbound Parameters

In addition to standard SMS parameters:

| Parameter               | Description                   |
| ----------------------- | ----------------------------- |
| `Type`                  | "mms" for multimedia messages |
| `Media0`, `Media1`, ... | URLs of attached media files  |

***

## What do the different MMS delivery statuses mean?

| Status          | Meaning                           |
| --------------- | --------------------------------- |
| **queued**      | Message accepted, waiting to send |
| **sent**        | Sent to carrier                   |
| **delivered**   | Confirmed delivery to recipient   |
| **undelivered** | Failed to deliver                 |
| **failed**      | Error occurred                    |

View status in Message Detail Records or via delivery callbacks.

***

## Can I send and receive MMS on my toll-free phone number?

Yes. Toll-free numbers support MMS in the US and Canada.

**Features:**

* Videos up to 40 seconds
* Audio files
* Animated GIFs
* Images and slideshows
* Automatic message queuing

***

## What are the MMS rate limits?

### Account Level

| Limit           | Value                     |
| --------------- | ------------------------- |
| Default MMS MPS | 0.25                      |
| API concurrency | 100 simultaneous requests |

### Per Number

Long code numbers have individual throughput limits.

***

## What happens to MMS messages sent to unsupported destinations?

MMS to countries or devices without MMS support returns HTTP 400 error.

***

## What happens to MMS messages sent from unsupported phone numbers?

HTTP 400 error is returned. Use an MMS-enabled number.

***

## Does Plivo do anything with the metadata associated with digital pictures?

* Metadata (date, time, location) is usually stripped by sending carrier
* If carrier preserves metadata, Plivo passes it through
* No modification of received metadata

***

## Related Resources

* [Messaging API Overview](/docs/messaging/messaging-api)
* [SMS](/docs/messaging/sms)
* [MMS API Reference](https://www.plivo.com/docs/messaging/api/message/)
* [Media API Reference](https://www.plivo.com/docs/messaging/api/media/)
