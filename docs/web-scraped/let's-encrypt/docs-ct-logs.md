# Source: https://letsencrypt.org/docs/ct-logs/

Title: Certificate Transparency (CT) Logs

URL Source: https://letsencrypt.org/docs/ct-logs/

Markdown Content:
[Certificate Transparency (CT)](https://www.certificate-transparency.org/what-is-ct) is a system for logging and monitoring the issuance of TLS certificates. CT greatly enhances everyone's ability to monitor and study certificate issuance, and these capabilities have led to numerous improvements to the CA ecosystem and Web security. As a result, CT is rapidly becoming critical infrastructure.

Let's Encrypt submits all certificates we issue to CT logs. We also operate CT logs. All publicly trusted certificate authorities are welcome to submit to our logs. Many certificate authority root certificates have already been included in our CT logs. If you operate a Certificate Authority and your issuer is not in our accepted issuers list, please file an issue [here](https://github.com/letsencrypt/ct-log-metadata).

Sign up for notifications in the [CT announcements category](https://community.letsencrypt.org/t/about-the-ct-announcements-category) of our community forum to see major announcements about our CT logs.

Funding
-------

If your organization would like to help us continue this work, please consider [sponsoring or donating](https://www.abetterinternet.org/sponsor/).

CT Logs
-------

Information about the various lifecycle states that a CT log progresses through can be found [here](https://googlechrome.github.io/CertificateTransparency/log_states.html).

### Sunlight

Let's Encrypt currently operates [static-ct](https://c2sp.org/static-ct-api) logs based on [Sunlight](https://sunlight.dev/).

Information including accepted roots, public keys, log IDs, and shard intervals are available at each log's landing page, linked below.

Sycamore and Willow are our production CT logs, accepting certificates from trusted CAs.

*   **Sycamore**: [log.sycamore.ct.letsencrypt.org](https://log.sycamore.ct.letsencrypt.org/)
*   **Willow**: [log.willow.ct.letsencrypt.org](https://log.willow.ct.letsencrypt.org/)

Twig is a test log, accepting certificates from trusted CAs as well as some additional test CAs, including the Let's Encrypt staging environment.

*   **Twig**: [log.twig.ct.letsencrypt.org](https://log.twig.ct.letsencrypt.org/)

### RFC 6962 Logs EOL

Let's Encrypt formerly ran a log based on Trillian, implementing the RFC 6962 API. It is currently available read-only, and will be shut down in February 2026. For more information, see the [end of life plan for our RFC 6962 Certificate Transparency logs](https://letsencrypt.org/2025/08/14/rfc-6962-logs-eol). URLs and log keys can be found in Google and Apple's CT log lists, if required. The old production log was called Oak.

We also ran test logs called Testflume and Sapling, which are no longer available.

Log Operations
--------------

To enumerate the included roots for a particular CT log, you can run the following command in the terminal of your choice:

$ for i in $(curl -s https://oak.ct.letsencrypt.org/2020/ct/v1/get-roots | jq -r '.certificates[]'); do
    echo '------'; base64 -d <<< "${i}" | openssl x509 -inform der -noout -issuer -serial
done

Submitting certificates to a CT log is typically handled by certificate authorities. If you'd like to experiment with this, begin by retrieving an arbitrary PEM encoded certificate from our favorite website. Copy and paste the following block into your terminal.

$ echo | \
openssl s_client \
    -connect "letsencrypt.org":443 \
    -servername "letsencrypt.org" \
    -verify_hostname "letsencrypt.org" 2>/dev/null | \
sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > example.crt

Before a certificate can be submitted, it must be JSON encoded within a special structure. You can use the JSON generator provided by [https://crt.sh/gen-add-chain](https://crt.sh/gen-add-chain) to perform this task. The crt.sh utility will return a JSON bundle. Download the bundle to your computer, rename the file if you must, and issue the following command to perform the add-chain operation ([RFC 6962 section 4.1](https://tools.ietf.org/html/rfc6962#section-4.1)) to submit the certificate to a CT log. The output will contain a signature which is in fact an [SCT](https://letsencrypt.org/2018/04/04/sct-encoding). More on the signature in a moment.

$ curl \
    -X POST \
   --data @example-json-bundle.json \
    -H "Content-Type: application/json" \
    -H "User-Agent: lets-encrypt-ct-log-example-1.0" \
   https://oak.ct.letsencrypt.org/2020/ct/v1/add-chain
{"sct_version":0,"id":"5xLysDd+GmL7jskMYYTx6ns3y1YdESZb8+DzS/JBVG4=","timestamp":1576689972016,"extensions":"","signature":"BAMARzBFAiEA4OmuTcft9Jq3XLtcdZz9XinXCvYEY1RdSQICXayMJ+0CIHuujkKBLmQz5Cl/VG6C354cP9gxW0dfgMWB+A2yHi+E"}

To confirm that the CT log was signed by the Oak 2020 shard, we use the id field from the command above and run it through the following command. The result of this will output the Log ID of the CT log.

$ base64 -d <<< "5xLysDd+GmL7jskMYYTx6ns3y1YdESZb8+DzS/JBVG4=" | xxd -p -c 64 | sed -e 's/../&:/g' -e 's/:$//' | tr '[:lower:]' '[:upper:]'
E7:12:F2:B0:37:7E:1A:62:FB:8E:C9:0C:61:84:F1:EA:7B:37:CB:56:1D:11:26:5B:F3:E0:F3:4B:F2:41:54:6E

Using the signature field, we can verify that the certificate was submitted to a log. Using our [SCT deep dive guide](https://letsencrypt.org/2018/04/04/sct-encoding), you could further decode this value.

$ base64 -d <<< "BAMARzBFAiEA4OmuTcft9Jq3XLtcdZz9XinXCvYEY1RdSQICXayMJ+0CIHuujkKBLmQz5Cl/VG6C354cP9gxW0dfgMWB+A2yHi+E" | xxd -p -c 16 | sed -e 's/../&:/g' -e 's/:$//' | tr '[:lower:]' '[:upper:]'
04:03:00:47:30:45:02:21:00:E0:E9:AE:4D:C7:ED:F4
9A:B7:5C:BB:5C:75:9C:FD:5E:29:D7:0A:F6:04:63:54
5D:49:02:02:5D:AC:8C:27:ED:02:20:7B:AE:8E:42:81
2E:64:33:E4:29:7F:54:6E:82:DF:9E:1C:3F:D8:31:5B
47:5F:80:C5:81:F8:0D:B2:1E:2F:84
