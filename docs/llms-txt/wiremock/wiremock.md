# Source: https://docs.wiremock.io/import-export/wiremock.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Import & Export - WireMock

> Importing and exporting mock APIs between WireMock and WireMock Cloud.

WireMock Cloud and WireMock OSS share the same native JSON format for stubs, so mock APIs
can be imported and exported between the two.

JSON exports can also be stored in source control, and used to clone or move stubs
between WireMock Cloud APIs.

## Importing a mock API into WireMock Cloud from WireMock

Assuming you're running a WireMock instance on port 8080, you can export all the
stubs currently defined via the admin API:

```
curl --output example-stubs.json http://localhost:8080/__admin/mappings
```

Then to import into WireMock Cloud, open the Import dialog and drop or upload the `example-stubs.json`:

<img alt="Import file" src="https://mintcdn.com/wiremockinc/I2C6ZJ3TgEtYucxf/images/screenshots/import-file.png?fit=max&auto=format&n=I2C6ZJ3TgEtYucxf&q=85&s=82e86f4f522f03d99c2337691460ad90" width="80%" data-og-width="767" data-og-height="495" data-path="images/screenshots/import-file.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/I2C6ZJ3TgEtYucxf/images/screenshots/import-file.png?w=280&fit=max&auto=format&n=I2C6ZJ3TgEtYucxf&q=85&s=0d1594ce921bd3b218d898284815409c 280w, https://mintcdn.com/wiremockinc/I2C6ZJ3TgEtYucxf/images/screenshots/import-file.png?w=560&fit=max&auto=format&n=I2C6ZJ3TgEtYucxf&q=85&s=4a158a8818ae03f5ada39b250c46b113 560w, https://mintcdn.com/wiremockinc/I2C6ZJ3TgEtYucxf/images/screenshots/import-file.png?w=840&fit=max&auto=format&n=I2C6ZJ3TgEtYucxf&q=85&s=01515450fb8f7524dc203c4617655069 840w, https://mintcdn.com/wiremockinc/I2C6ZJ3TgEtYucxf/images/screenshots/import-file.png?w=1100&fit=max&auto=format&n=I2C6ZJ3TgEtYucxf&q=85&s=ea23380233fcbeebd320851a83f89e82 1100w, https://mintcdn.com/wiremockinc/I2C6ZJ3TgEtYucxf/images/screenshots/import-file.png?w=1650&fit=max&auto=format&n=I2C6ZJ3TgEtYucxf&q=85&s=a6d45387d563826151ef70b55415bcaf 1650w, https://mintcdn.com/wiremockinc/I2C6ZJ3TgEtYucxf/images/screenshots/import-file.png?w=2500&fit=max&auto=format&n=I2C6ZJ3TgEtYucxf&q=85&s=4f4fc4eeba5abf33dbe37988d0a0d5bf 2500w" />

<Note>A current limitation of this approach is that response bodies represented as files under the `__files` directory will not be imported. See how this can be worked around by [uploading a WireMock project folder](#uploading-a-wiremock-folder) and via the [WireMock Java API](#pushing-stubs-to-wiremock-cloud-using-wiremocks-java-api).</Note>

## Importing a mock API into WireMock from WireMock Cloud

First, export the stubs via the Export dialog in the Stubs page:

<img alt="Export dialog" src="https://mintcdn.com/wiremockinc/I2C6ZJ3TgEtYucxf/images/screenshots/export-stubs.png?fit=max&auto=format&n=I2C6ZJ3TgEtYucxf&q=85&s=5a866e2cdee0b23b3df73c2cc93824f5" width="60%" data-og-width="688" data-og-height="213" data-path="images/screenshots/export-stubs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/I2C6ZJ3TgEtYucxf/images/screenshots/export-stubs.png?w=280&fit=max&auto=format&n=I2C6ZJ3TgEtYucxf&q=85&s=b837a7688d1ad414125dc82338948a19 280w, https://mintcdn.com/wiremockinc/I2C6ZJ3TgEtYucxf/images/screenshots/export-stubs.png?w=560&fit=max&auto=format&n=I2C6ZJ3TgEtYucxf&q=85&s=72b41cccdf5c2f6307072285527ad518 560w, https://mintcdn.com/wiremockinc/I2C6ZJ3TgEtYucxf/images/screenshots/export-stubs.png?w=840&fit=max&auto=format&n=I2C6ZJ3TgEtYucxf&q=85&s=25775b8bf00465896fe7e2f974a29bf4 840w, https://mintcdn.com/wiremockinc/I2C6ZJ3TgEtYucxf/images/screenshots/export-stubs.png?w=1100&fit=max&auto=format&n=I2C6ZJ3TgEtYucxf&q=85&s=8bcfca5eadc524611adb5fda5e451e37 1100w, https://mintcdn.com/wiremockinc/I2C6ZJ3TgEtYucxf/images/screenshots/export-stubs.png?w=1650&fit=max&auto=format&n=I2C6ZJ3TgEtYucxf&q=85&s=e310759e77b47b16f0c0b30c13a8cc5f 1650w, https://mintcdn.com/wiremockinc/I2C6ZJ3TgEtYucxf/images/screenshots/export-stubs.png?w=2500&fit=max&auto=format&n=I2C6ZJ3TgEtYucxf&q=85&s=a6682fecf0dc56b146c36cf8435d8e8f 2500w" />

Then call the WireMock import API with the file you downloaded:

```
curl -v -d @example-stubs.json http://localhost:8080/__admin/mappings/import
```

Alternatively you can copy `example-stubs.json` into the `mappings` directory
under your WireMock root and either restart WireMock or make a `POST` request to the
reset API:

```
curl -v -X POST http://localhost:8080/__admin/mappings/reset
```

<Note>If any of your stubs make use of **response templating** then you'll need to ensure WireMock is started with the `--local-response-templating` CLI parameter or [Java equivalent](https://wiremock.org/docs/response-templating/).</Note>

<Note>It is not currently possible to import stubs that use the JWT and JWKS template helpers into WireMock.</Note>

## Uploading a WireMock folder

If you have a WireMock project that consists of individual JSON stub mapping
files under the `mappings` directory that refer to response body files under `__files`
you can import this by dragging and dropping the project folder into the dialog.
Unlike the method involving a single JSON file described above, this will cause the
response bodies under `__files` to be inlined.

<img alt="Import file" src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/wiremock-folder-drop.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=df2ac36f652412bfdda2f2040095e5ee" width="80%" data-og-width="2166" data-og-height="1508" data-path="images/screenshots/wiremock-folder-drop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/wiremock-folder-drop.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=74e7a0b813c6c9ae70120943692f82dd 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/wiremock-folder-drop.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=5e7f9d09fdfcff5732187d95f2e09b21 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/wiremock-folder-drop.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=7fd30dbf2e11b129a05b8ae84942703b 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/wiremock-folder-drop.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=719693ca6fa2000575889943d7d95323 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/wiremock-folder-drop.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=a58eafa4e8b1c1316ffc1e061c2bf2b4 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/wiremock-folder-drop.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=49748c8092bc3a84121ce442080af5dd 2500w" />

## Pushing stubs to WireMock Cloud using WireMock's Java API

Another way to import a WireMock project that has a `__files` directory is to push it using WireMock's Java API.
This method also inlines response bodies before sending them to WireMock Cloud:

```java  theme={null}
WireMock wireMock = WireMock.create()
    .scheme("https")
    // The domain name of the mock API you wish to import into
    .host("my-api.wiremockapi.cloud")
    .port(443)
    // API token from https://app.wiremock.cloud/account/security
    .authenticator(new ClientTokenAuthenticator("mytokenabc123"))
    .build();

// The root directory of the WireMock project, under which the mappings and __files directories should be found
wireMock.loadMappingsFrom("/wiremock");
```
