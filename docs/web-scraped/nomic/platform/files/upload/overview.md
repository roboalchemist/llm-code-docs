# Nomic Documentation

Source: https://docs.nomic.ai/platform/files/upload/overview/

File upload allows you to send documents directly to Nomic without relying on external storage like S3 or public URLs.
Once uploaded, you'll receive a unique nomic:// URL that can be used with the /parse or /extract endpoints. The file
will be available at this URL for at most 24 hours.

```
nomic://
```

## Example​

```
import requestsfrom nomic import NomicClientresp = requests.get("https://assets.nomicatlas.com/department-of-labor-data.pdf")with open("department-of-labor-data.pdf", "wb") as f:    f.write(resp.content)client = NomicClient()file = client.upload_file("department-of-labor-data.pdf")
```

In the above example, we download a PDF and then upload it to the Nomic platform. This is just for demonstration. If
you have a public HTTPS url for your document, you should typically pass it to parse or extract directly.

## Security​

All uploaded files are:

- Encrypted in transit using TLS
- Encrypted at rest using AES-256
- Stored in secure, compliant infrastructure
- Accessible only to authorized users in your organization
## Next Steps​

After uploading files, you can:

- Parse files into a structured representation
- Extract data from files using a specific schema
- Example
- Security
- Next Steps
