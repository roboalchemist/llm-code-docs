# Source: https://loops.so/docs/transactional/attachments.md

# Attachments

> How to send attachments with your transactional email.

<Note>
  Need to send attachments with your transactional email? Just [reach out to
  us](mailto:help@loops.so) and we can enable the feature on your account.
</Note>

## Sending attachments

Check out [the transactional API documentation](/api-reference/send-transactional-email) for a refresher on the transactional API email payload.

To attach a file to a transactional message, you'll need to add a `attachments` key to the standard transaction API email payload. The `attachments` key should be an array of objects, each with the following keys:

* `filename` - the name of the file
* `contentType` - the MIME type of the file
* `data` - the base64 encoded content of the file

Here's an example of a transactional email payload with [this ICS file](https://gist.github.com/phil-loops/c0cb5d84d502a3949651934252d306af) attached:

```json  theme={"dark"}
{
  "transactionalId": "*********",
  "email": "phil+attachments@loops.so",
  "attachments": [
    {
      "filename": "oil-change-invite.ics",
      "contentType": "text/calendar",
      "data": "QkVHSU46VkNBTEVOREFSClZFUlNJT046Mi4wClBST0RJRDotLy9pY2FsLm1hcnVkb3QuY29tLy9pQ2FsIEV2ZW50IE1ha2VyCkNBTFNDQUxFOkdSRUdPUklBTgpCRUdJTjpWVElNRVpPTkUKVFpJRDpBbWVyaWNhL0xvc19BbmdlbGVzCkxBU1QtTU9ESUZJRUQ6MjAyMzA0MDdUMDUwNzUwWgpUWlVSTDpodHRwczovL3d3dy50enVybC5vcmcvem9uZWluZm8tb3V0bG9vay9BbWVyaWNhL0xvc19BbmdlbGVzClgtTElDLUxPQ0FUSU9OOkFtZXJpY2EvTG9zX0FuZ2VsZXMKQkVHSU46REFZTElHSFQKVFpOQU1FOlBEVApUWk9GRlNFVEZST006LTA4MDAKVFpPRkZTRVRUTzotMDcwMApEVFNUQVJUOjE5NzAwMzA4VDAyMDAwMApSUlVMRTpGUkVRPVlFQVJMWTtCWU1PTlRIPTM7QllEQVk9MlNVCkVORDpEQVlMSUdIVApCRUdJTjpTVEFOREFSRApUWk5BTUU6UFNUClRaT0ZGU0VURlJPTTotMDcwMApUWk9GRlNFVFRPOi0wODAwCkRUU1RBUlQ6MTk3MDExMDFUMDIwMDAwClJSVUxFOkZSRVE9WUVBUkxZO0JZTU9OVEg9MTE7QllEQVk9MVNVCkVORDpTVEFOREFSRApFTkQ6VlRJTUVaT05FCkJFR0lOOlZFVkVOVApEVFNUQU1QOjIwMjMwOTExVDE4NTY0M1oKVUlEOjE2OTQ0NTg1ODM0MzgtOTkyMjJAaWNhbC5tYXJ1ZG90LmNvbQpEVFNUQVJUO1RaSUQ9QW1lcmljYS9Mb3NfQW5nZWxlczoyMDI1MDUwMVQxMjAwMDAKRFRFTkQ7VFpJRD1BbWVyaWNhL0xvc19BbmdlbGVzOjIwMjUwNTAxVDEyMDAwMApTVU1NQVJZOkNoYW5nZSBPaWwKVVJMOmd1bWRyb3AuZXhhbXBsZS5jb20KREVTQ1JJUFRJT046WW91ciBjYXIgaXMgcmVhZHkgZm9yIGFuIG9pbCBjaGFuZ2UhCkxPQ0FUSU9OOkd1bWRyb3AgVmlsbGFnZQpFTkQ6VkVWRU5UCkVORDpWQ0FMRU5EQVI="
    }
  ]
}
```

When you send this payload, the recipient will receive an email with the ICS file attached:

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/transactional-attachment-send.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=fbe99c3fd0d1a1d15fda1bdf78755c51" alt="An email with an ICS file attached" data-og-width="1748" width="1748" data-og-height="516" height="516" data-path="images/transactional-attachment-send.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/transactional-attachment-send.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=f2a9ba5bc0faa966709c8f1e38d1a346 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/transactional-attachment-send.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=74943762dba4c02e4e688da6f705fdcb 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/transactional-attachment-send.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=e46a8de2a0670344ab4a43b4f90c1f00 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/transactional-attachment-send.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=57f933f5e88b00ee817092bae88c7609 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/transactional-attachment-send.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=7b6e0b335bfd4a246b9dcb9dab9406fd 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/transactional-attachment-send.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=f5a8ee3b23f37828cbbae62031f9f691 2500w" />

<Info>
  All the usual [transactional API email
  payload](/api-reference/send-transactional-email) keys are still required. The
  `attachments` key is in addition to the standard payload.
</Info>

## Limitations

* The total size of the payload must be less than 4MB
* Attachments are not generally available. Please [contact us](mailto:help@loops.so) if you need this feature enabled on your account.
