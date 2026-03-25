# Source: https://scrapfly.io/docs/scrape-api/ssl

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/scrape-api/ssl

Markdown Content:
[SSL](https://scrapfly.io/docs/scrape-api/getting-started#api_param_ssl) feature is very straightforward - it collects information about the SSL certificate of the scraped page. It can be a useful tool for monitoring certificate changes, expiration dates and validity.

SSL details can also be found in the monitoring dashboard logs under the `SSL` tab:

To use SSL feature the [SSL](https://scrapfly.io/docs/scrape-api/getting-started#api_param_ssl) parameter can be enabled on any Scrapfly scrape request. This will include SSL details in the `result.ssl` field:

```
...
"result": {
    ...,
    "ssl": {
        "certs": [
            {
                "validity_period": {
                    "not_valid_before": "2020-01-18 00:00:00 UTC",
                    "not_valid_after": "2021-02-18 12:00:00 UTC"
                },
                "version": "2",
                "serial_number": "15511154429359216763915851913648262204",
                "subject_name_hash": 1513450353,
                "algorithm": "sha256WithRSAEncryption",
                "issuer": {
                    "C": "US",
                    "O": "Amazon",
                    "OU": "Server CA 1B",
                    "CN": "Amazon"
                },
                "subject": {
                    "CN": "httpbin.dev"
                },
                "extensions": {
                    "authorityKeyIdentifier": "keyid:59:A4:66:06:52:A0:7B:95:92:3C:A3:94:07:27:96:74:5B:F9:3D:D0\n",
                    "subjectKeyIdentifier": "4D:47:D7:1B:DA:3A:E5:FB:D0:31:40:CA:CE:35:D6:54:B9:C8:EF:A5",
                    "subjectAltName": "DNS:httpbin.dev, DNS:*.httpbin.dev",
                    "keyUsage": "Digital Signature, Key Encipherment",
                    "extendedKeyUsage": "TLS Web Server Authentication, TLS Web Client Authentication",
                    "crlDistributionPoints": "\nFull Name:\n  URI:http://crl.sca1b.amazontrust.com/sca1b.crl\n",
                    "certificatePolicies": "Policy: 2.16.840.1.114412.1.2\nPolicy: 2.23.140.1.2.1\n",
                    "authorityInfoAccess": "OCSP - URI:http://ocsp.sca1b.amazontrust.com\nCA Issuers - URI:http://crt.sca1b.amazontrust.com/sca1b.crt\n",
                    "basicConstraints": "CA:FALSE",
                    "ct_precert_scts": "Signed Certificate Timestamp:\n    Version   : v1 (0x0)\n    Log ID    : EE:4B:BD:B7:75:CE:60:BA:E1:42:69:1F:AB:E1:9E:66:\n                A3:0F:7E:5F:B0:72:D8:83:00:C4:7B:89:7A:A8:FD:CB\n    Timestamp : Jan 18 01:26:21.019 2020 GMT\n    Extensions: none\n    Signature : ecdsa-with-SHA256\n                30:45:02:21:00:81:00:82:78:B4:00:81:AD:D1:F0:07:\n                86:67:18:81:93:CB:7F:FD:17:1B:99:F4:62:28:1E:07:\n                D7:E5:18:DE:7D:02:20:79:76:3E:C7:BA:16:42:62:12:\n                85:70:AB:05:27:6A:79:36:17:AE:CC:50:71:61:3A:66:\n                90:32:43:17:2C:75:45\nSigned Certificate Timestamp:\n    Version   : v1 (0x0)\n    Log ID    : 87:75:BF:E7:59:7C:F8:8C:43:99:5F:BD:F3:6E:FF:56:\n                8D:47:56:36:FF:4A:B5:60:C1:B4:EA:FF:5E:A0:83:0F\n    Timestamp : Jan 18 01:26:21.098 2020 GMT\n    Extensions: none\n    Signature : ecdsa-with-SHA256\n                30:45:02:20:10:CC:62:29:B6:B0:5F:1E:1E:95:B5:67:\n                BF:F2:43:59:62:4F:06:BC:21:14:A3:89:D0:5D:F5:95:\n                48:C1:EE:A6:02:21:00:EC:33:CE:4D:A4:60:73:F7:07:\n                DC:EC:C8:19:2B:BA:74:B6:9E:7B:91:7F:61:19:26:0B:\n                D4:E2:91:68:96:4C:2F"
                },
                "public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApFxnGvqYGUel320/nRE2\n81GA6WAOVwY+Npl79AIz45bHXcxNu+LeMEuGBvrl2EuccQJGXpCY8+sCzFRmcCZs\nMtTzUdj6R/QbWR7OFjf6Z6w1AiKccc7iKlRUF/tWAuoLr1b6L9+JfAkJAUL35VV7\n/vIs9IZ8uWJDhEB2wU6rRZO+2RBvHGM7oeBNda1/maukjLNYmJ+pxSnrsRTMh3dH\nUCxZ47h2UZhj2SWCPlW+SMsYNM/JkURnzSy0lgq/woVeM5g4nOpWuljO1scJ0ZRb\nR3I+3JveGEd3sQi8e6HkWFtImGklhirXxE/t86GP86s+XbwnABIML12h09M3mTJq\nEwIDAQAB\n-----END PUBLIC KEY-----\n"
            },
            {
                "validity_period": {
                    "not_valid_before": "2015-10-22 00:00:00 UTC",
                    "not_valid_after": "2025-10-19 00:00:00 UTC"
                },
                "version": "2",
                "serial_number": "144918209630989264145272943054026349679957517",
                "subject_name_hash": 604098895,
                "algorithm": "sha256WithRSAEncryption",
                "issuer": {
                    "C": "US",
                    "O": "Amazon",
                    "CN": "Amazon Root CA 1"
                },
                "subject": {
                    "C": "US",
                    "O": "Amazon",
                    "OU": "Server CA 1B",
                    "CN": "Amazon"
                },
                "extensions": {
                    "basicConstraints": "CA:TRUE, pathlen:0",
                    "keyUsage": "Digital Signature, Certificate Sign, CRL Sign",
                    "subjectKeyIdentifier": "59:A4:66:06:52:A0:7B:95:92:3C:A3:94:07:27:96:74:5B:F9:3D:D0",
                    "authorityKeyIdentifier": "keyid:84:18:CC:85:34:EC:BC:0C:94:94:2E:08:59:9C:C7:B2:10:4E:0A:08\n",
                    "authorityInfoAccess": "OCSP - URI:http://ocsp.rootca1.amazontrust.com\nCA Issuers - URI:http://crt.rootca1.amazontrust.com/rootca1.cer\n",
                    "crlDistributionPoints": "\nFull Name:\n  URI:http://crl.rootca1.amazontrust.com/rootca1.crl\n",
                    "certificatePolicies": "Policy: 2.23.140.1.2.1\n"
                },
                "public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwk4WZ93OvGrIN1rsOjCw\nHebREugSKEjM6CnBuW5T1aPrAzkazHeH9gG52XDMz2uN4+MDcYaZbcumlCpOE9an\nvQTsChY8Cus5scS1WKO2x1Yl7D5SeqjjKRYHuW5Qz/tfMfgdugNKYokDrj5H8g8n\nkeMUIIX4+umKNfVfnplN52s376RQPkTs+lqFZgecfhdqVfMXijUe7umsw3VOWFV9\nU2sKa5sUQtflrAGJs+qj/s/AKwyEwthTFctn8NCIyjrRF3P1X5rUxXIefgHxmDBj\nKqryei3F4gIahuUyPg69EbTPPJPvF1AQnkPCBirgDWi+04iLSmWMStTDLkybVfSG\n5QIDAQAB\n-----END PUBLIC KEY-----\n"
            },
            {
                "validity_period": {
                    "not_valid_before": "2015-05-25 12:00:00 UTC",
                    "not_valid_after": "2037-12-31 01:00:00 UTC"
                },
                "version": "2",
                "serial_number": "144918191876577076464031512351042010504348870",
                "subject_name_hash": 3462296815,
                "algorithm": "sha256WithRSAEncryption",
                "issuer": {
                    "C": "US",
                    "ST": "Arizona",
                    "L": "Scottsdale",
                    "O": "Starfield Technologies, Inc.",
                    "CN": "Starfield Services Root Certificate Authority - G2"
                },
                "subject": {
                    "C": "US",
                    "O": "Amazon",
                    "CN": "Amazon Root CA 1"
                },
                "extensions": {
                    "basicConstraints": "CA:TRUE",
                    "keyUsage": "Digital Signature, Certificate Sign, CRL Sign",
                    "subjectKeyIdentifier": "84:18:CC:85:34:EC:BC:0C:94:94:2E:08:59:9C:C7:B2:10:4E:0A:08",
                    "authorityKeyIdentifier": "keyid:9C:5F:00:DF:AA:01:D7:30:2B:38:88:A2:B8:6D:4A:9C:F2:11:91:83\n",
                    "authorityInfoAccess": "OCSP - URI:http://ocsp.rootg2.amazontrust.com\nCA Issuers - URI:http://crt.rootg2.amazontrust.com/rootg2.cer\n",
                    "crlDistributionPoints": "\nFull Name:\n  URI:http://crl.rootg2.amazontrust.com/rootg2.crl\n",
                    "certificatePolicies": "Policy: X509v3 Any Policy\n"
                },
                "public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsniAccp41eNxr0eAUHR9\nbtjXiHb0mWj3WCFg+XSEAS+sAi2G06BDek6ypNA2ugG+jdtIyAcXNkz07ogjxz7r\nN/W1GfhJaLDe17l2OB1hnqT+gjal5UpW5EXh+f20Fvp02pybNTkv+rAgUAZsetCA\nsqb5r+xHGY9QOAfcooc5WPi61an5SGcwlu6UeF5viaNRwDCGZqFFZrpU66PDkflI\n3P/R6DAtfS10cDXXiCT3nsRZbrtzhxfyMkYouEP6tx2qyrTynyQOLUv3cVxeaf/q\nlQLLOIquUDhv2/stYhvFxx5U4XfgZ8gPnIcj1j9AIH8ggMSATD47JCaOBK5smsiq\nDQIDAQAB\n-----END PUBLIC KEY-----\n"
            },
            {
                "validity_period": {
                    "not_valid_before": "2009-09-02 00:00:00 UTC",
                    "not_valid_after": "2034-06-28 17:39:16 UTC"
                },
                "version": "2",
                "serial_number": "12037640545166866303",
                "subject_name_hash": 158896471,
                "algorithm": "sha256WithRSAEncryption",
                "issuer": {
                    "C": "US",
                    "O": "Starfield Technologies, Inc.",
                    "OU": "Starfield Class 2 Certification Authority"
                },
                "subject": {
                    "C": "US",
                    "ST": "Arizona",
                    "L": "Scottsdale",
                    "O": "Starfield Technologies, Inc.",
                    "CN": "Starfield Services Root Certificate Authority - G2"
                },
                "extensions": {
                    "basicConstraints": "CA:TRUE",
                    "keyUsage": "Digital Signature, Certificate Sign, CRL Sign",
                    "subjectKeyIdentifier": "9C:5F:00:DF:AA:01:D7:30:2B:38:88:A2:B8:6D:4A:9C:F2:11:91:83",
                    "authorityKeyIdentifier": "keyid:BF:5F:B7:D1:CE:DD:1F:86:F4:5B:55:AC:DC:D7:10:C2:0E:A9:88:E7\n",
                    "authorityInfoAccess": "OCSP - URI:http://o.ss2.us/\nCA Issuers - URI:http://x.ss2.us/x.cer\n",
                    "crlDistributionPoints": "\nFull Name:\n  URI:http://s.ss2.us/r.crl\n",
                    "certificatePolicies": "Policy: X509v3 Any Policy\n"
                },
                "public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1Qw6xCr5TuL1vhmXX46I\nU7EfP8vPnyATbSk6yA99PPdrdjhj2TZgqJteXACAsi9Zf/aH+SVDhudpG1KakOFx\n49gtDU5v9shJ2bbzGlauK7Z0FOvP+ybjGrodli5qO1iUiUdW/yWgk3BTg9qEdBTD\nZ54EaDrfjkBaHUpOz0ORO+dW1gBwy1Lue32uOue8MflF9sJgzxNZAiuAzDRH37ne\nkGVtAs8skaam596FGEl8Zk6jOm2pte40LroNA7gz30frsWuNJdmbzoHRRUYylnCH\n3gIOSUOFtmxzu2TqYUGsydRU34cvxyKyJsyfWVRon/y+Ki/EVRx1QGAXhQJVOYt/\nBQIDAQAB\n-----END PUBLIC KEY-----\n"
            }
        ],
        "protocol": {
            "cipher": "ECDHE-RSA-AES128-GCM-SHA256"
        },
        "notice": [],
        "metadata": {
            "san": [
                {
                    "type": "DNS",
                    "name": "httpbin.dev"
                },
                {
                    "type": "DNS",
                    "name": "*.httpbin.dev"
                }
            ],
            "usage": [
                "Digital Signature",
                "Key Encipherment",
                "TLS Web Server Authentication",
                "TLS Web Client Authentication"
            ],
            "access": [
                "OCSP - URI:http://ocsp.sca1b.amazontrust.com\nCA Issuers - URI:http://crt.sca1b.amazontrust.com/sca1b.crt"
            ],
            "expire": "2021-02-18 12:00:00 UTC",
            "cn": "httpbin.dev",
            "issuer": "Amazon",
            "validity": true
        }
    },
    ...
}
...
```

No additional fee is applied on usage.
