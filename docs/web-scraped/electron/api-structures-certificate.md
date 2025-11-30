# Source: https://www.electronjs.org/docs/latest/api/structures/certificate

# Certificate Object

- `data` string - PEM encoded data
- `issuer` [CertificatePrincipal](/docs/latest/api/structures/certificate-principal) - Issuer principal
- `issuerName` string - Issuer\'s Common Name
- `issuerCert` Certificate - Issuer certificate (if not self-signed)
- `subject` [CertificatePrincipal](/docs/latest/api/structures/certificate-principal) - Subject principal
- `subjectName` string - Subject\'s Common Name
- `serialNumber` string - Hex value represented string
- `validStart` number - Start date of the certificate being valid in seconds
- `validExpiry` number - End date of the certificate being valid in seconds
- `fingerprint` string - Fingerprint of the certificate

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/certificate.md)