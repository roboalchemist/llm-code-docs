# Source: https://docs.wiremock.io/recording-stubs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Recording via the Cloud

> Creating new stubs by recording traffic to another API

If the API you're mocking already exists you can speed up the process of stubbing responses using WireMock Cloud's record feature.
This essentially involves telling WireMock Cloud to act as a proxy to the target API then directing some HTTP requests to WireMock Cloud
representing the resources you'd like to stub.

## A simple recording example

Once you have logged into WireMock Cloud and created a mock API, navigate to the Stubs page.

Then hit the Record button, enter `http://ip-api.com` as the target URL and hit Start.

<img src="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/record-dialog-screenshot-3.png?fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=3b9a2b662279462fca1f105fda143e92" title="Record dialog" width="80%" data-og-width="481" data-og-height="405" data-path="images/screenshots/record-dialog-screenshot-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/record-dialog-screenshot-3.png?w=280&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=dbc1a20200377ffa80a07072e3a5877c 280w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/record-dialog-screenshot-3.png?w=560&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=902ded64175fd275715d3fda521e0ec0 560w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/record-dialog-screenshot-3.png?w=840&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=3e098c49c9764535a47e6ea2ccb2a086 840w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/record-dialog-screenshot-3.png?w=1100&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=b957fefb138e309a1e4e7a7d0b3ba9c9 1100w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/record-dialog-screenshot-3.png?w=1650&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=7f1aa93cfef090045f094b551bacffe1 1650w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/record-dialog-screenshot-3.png?w=2500&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=7f2d79dab3652b7a091adbd6ef68ebc9 2500w" />

Now make a request to your mock API (substituting `my-mock-api` for your own sub domain name):

```bash  theme={null}
$ curl -v http://my-mock-api.wiremockapi.cloud/json
```

This request will be proxied through WireMock Cloud, so that a `GET` request will be made to `http://ip-api.com/json` and the result captured.

Now hit Stop, and you should see that an extra stub has been added to the list.

## Request matching rules when recording

When a request with no body is received during recording, the recorder will create a stub matched on HTTP method and URL only.

When a request with a body is received a body pattern is also included. If the request body is a valid JSON document,
then the `equalToJson` operator will be used. If XML, the `equalToXml` operator will be used. Otherwise the operator will be `equalTo` i.e. simple string equality.

## Recording from Private Endpoints

For obvious reasons, WireMock Cloud cannot record by proxying to an endpoint that is not accessible via the internet.
Nor can it record from an endpoint that requires authentication via mutual TLS. However, this can be achieved using
the WireMock CLI. See [Recording using the WireMock CLI](/cli/recording/).
