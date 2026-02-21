# Source: https://docs.wiremock.io/samples/exploratory-testing-tutorial.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Exploratory Testing With Spring Boot

> Exploratory testing a Spring Boot app with WireMock Cloud

This tutorial demonstrates how WireMock Cloud can be used to perform a manual exploratory test of an application with an API back-end.

The app is a simple to-do list based on Java and Spring Boot, supporting listing of to-do items and posting new ones. Any version off Spring Boot, such as spring boot 3, will suffice for this tutorial.

## Mock API setup

If you haven't yet created a mock API in WireMock Cloud, start by doing this. See [Getting Started](/overview#getting-started) for how to do this.
Make a note of the base URL from the Settings page (any of them will do).

## App setup

Ensure that you have Java 8+ installed and the `java` executable on your shell's `PATH`.

Clone the WireMock Cloud demo project and change the working directory to the newly checked out project:

```bash  theme={null}
git clone git@github.com:wiremock/wiremock-cloud-demo-app.git
cd wiremock-cloud-demo-app
```

Edit `src/main/resources/application.properties` changing the `todo-api.baseurl` value to your mock API's base URL noted earlier.

Run the app:

```bash  theme={null}
./gradlew bootRun
```

This should start the app locally on port `9000`.

## Step 1 - show a list of to do items

Navigate to the Stubs page and create a new stub with method `GET`, URL `/todo-items`, response `Content-Type` header `application/json` and the following JSON in the response body:

```json  theme={null}
{
  "items": [
    {
      "id": "1",
      "description": "First item"
    },
    {
      "id": "2",
      "description": "Item number two"
    },
    {
      "id": "3",
      "description": "Do that number three thing"
    },
    {
      "id": "4",
      "description": "Don't forget the fourth thing on the list"
    }
  ]
}
```

Your stub should look something like this:

<img title="To do list stub" src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-stub.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=4e4abc5d583227a08a39bb8c25fc3e4c" data-og-width="1950" width="1950" data-og-height="1750" height="1750" data-path="images/screenshots/to-do-stub.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-stub.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=1cf0046a7c57fc4d296396b2e8f749bb 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-stub.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=786a8451044087cb849d7941338cc384 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-stub.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=a7443c30c8d004d09dfe2a6cc6d0e1e8 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-stub.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=28198747ec2d01c9f44ec7ac8a5a516e 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-stub.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=3b69316cbc7a351e8f6edafbacbb5c14 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-stub.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=6c147f1fdf83f49fdbe84d3b6f9caa9d 2500w" />

Once you've saved the stub, point your browser to [http://localhost:9000](http://localhost:9000).
You should see the to-do items in your response body listed in the page:

<img title="To do list" src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-list-app.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=db85e74dbe5bd421dc6e26f0a8fa710d" data-og-width="1358" width="1358" data-og-height="702" height="702" data-path="images/screenshots/to-do-list-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-list-app.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=5a7001d401bc6aac448c9dfca989e801 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-list-app.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=7932cf52f02cba988db1d072d7c077e6 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-list-app.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=8afd7020ac8e1573f4f296794f5aabfb 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-list-app.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=c64ead1e7815f10351cd8dcfcc02656a 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-list-app.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=27dac61f436c77ce4d4231c59e882c7c 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-list-app.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=5272741e25c35f2aa282ea91a8caa19d 2500w" />

What has happened here is that the Spring Boot app has made a REST request to WireMock Cloud, which was matched by the stub you just created.
The stub returned a JSON response which the app parsed and rendered into an HTML page.

Now try modifying one or more of the item descriptions in the stub response and saving it, then refreshing the page. You should
immediately see your new items in the to-to list.

## Step 2 - simulating the posting of a new item

Next we're going to simulate a new item being added to the list via a POST request.

For this you'll need another new stub, this time for `POST` to `/todo-items` , response `Content-Type` header `application/json` and the following JSON in the response body:

```json  theme={null}
{ "message": "Successfully sent new item." }
```

Your stub should look like this:

<img title="To do list POST stub" src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-post-stub.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=290724753b5fda33e9c210e7f0d77307" data-og-width="1958" width="1958" data-og-height="1752" height="1752" data-path="images/screenshots/to-do-post-stub.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-post-stub.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=5e3db8b064dcefbe35e57f326d3a65ff 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-post-stub.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=1b3cf631d6324a4c125608cd82d3e994 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-post-stub.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=53b30e843d047cd4c96f99978caeb9d9 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-post-stub.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=4611efb1f7b33e9f4b4fb321fb3d04ab 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-post-stub.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=b79d5c63cdeec0eea6c7214e03f799d8 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-post-stub.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=afc4564e7220c4b488069b416cb4e26f 2500w" />

Once that's saved, go to the to-do list page and add a new item by typing a description in the field and clicking the button:

<img title="New to-do item" src="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/new-to-do-item-field.png?fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=f84f0c0a864aa52191883c495f9b77af" data-og-width="1226" width="1226" data-og-height="168" height="168" data-path="images/screenshots/new-to-do-item-field.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/new-to-do-item-field.png?w=280&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=2a28451fb5fd03e4857cf598c2a086ac 280w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/new-to-do-item-field.png?w=560&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=c6f800e5040a4f928c2b14a1595135ed 560w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/new-to-do-item-field.png?w=840&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=dc2ec1134b0729df12a00efdb7e7dbb4 840w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/new-to-do-item-field.png?w=1100&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=21762058b8f12ce3e153ba9c11122c96 1100w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/new-to-do-item-field.png?w=1650&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=3fd1d25c233b285a8f513754be0e949e 1650w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/new-to-do-item-field.png?w=2500&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=9a8aee990129e699f3138ae48c205460 2500w" />

You should now see the success message you put in the stub response:

<img title="Success message" src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-list-success-message.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=6b18f47f5977f80cd2633b1998b15907" data-og-width="1312" width="1312" data-og-height="850" height="850" data-path="images/screenshots/to-do-list-success-message.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-list-success-message.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=d39c96e2de02f6df0536b1ae1b890735 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-list-success-message.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=b8fa2bd028719192c0f372c088d3072b 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-list-success-message.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=22817c56dd2736c3b275cbd3d28614d0 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-list-success-message.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=a28337d9c153af59720746dc263a77fa 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-list-success-message.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=e7af3c67a386be9a7132c1ed695283a9 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-list-success-message.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=31239d5fbb3b629d8c0eadaf09dfdfaf 2500w" />

You'll notice that the contents of the list hasn't changed. This is because WireMock Cloud stubs aren't stateful - the app will load whatever is in the `GET /todo-items` stub you created at the start until you change it. However, if you visit the request log in the WireMock Cloud UI you can confirm that the request you expected actually arrived:

<img title="To do post request log" src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-request-log.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=3ccf811dba3d889a45629f2e06d8213e" data-og-width="2464" width="2464" data-og-height="1692" height="1692" data-path="images/screenshots/to-do-request-log.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-request-log.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=f186c3c5ad0c9983642174efad30925f 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-request-log.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=1b9fdc6f4f20e9a0424675ef443a4d29 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-request-log.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=f0b2b5c1e1e234f0c7617a063a02ed75 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-request-log.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=27540387e600fb8e05971384f0232557 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-request-log.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=9c0bef6a9aa58d2e65654ccf1ab65cf8 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-request-log.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=a9dab1c54e2d6ad36a17d16ae6bc7b14 2500w" />

## Step 3 - posting a new item fails

In this step we're going to deliberately return an error from the API in order to test that the app behaves appropriately.

Navigate to the `POST /todo-items` stub you created in the previous step and clone it (using the Clone button at the end of the form).

In the newly cloned stub, expand the Advanced section and give the stub a higher priority - 4 or less will work as the default is 5.
The reason we need to do this is to ensure that this and not the OK posting stub we cloned from is guaranteed to match an incoming `POST /todo-items`.

In the response section change the response code to 502 and the message in the JSON body to something suitable:

<img title="To do list stub" src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-bad-post-stub.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=057de9c083864b43b3b19aad106bfe60" data-og-width="1918" width="1918" data-og-height="1914" height="1914" data-path="images/screenshots/to-do-bad-post-stub.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-bad-post-stub.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=364ee9e0e9495051bcc347505c0728f0 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-bad-post-stub.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=8589b5a4b8f331d96b2403cc591370bf 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-bad-post-stub.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=6ca564e08351390dd2caa2e82f2ea7de 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-bad-post-stub.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=c6a0bbc512b13b5929dc14adf5521253 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-bad-post-stub.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=466f2b9c4260a0e2e80d452ebeff3708 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-bad-post-stub.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=19d3fa179338c69c6358702a45aa3879 2500w" />

Now try adding a new to-do item as you did in Step 2. When after submitting it, you should see an error page like this:

<img title="To do error" src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-error-page.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=e65c44e69f6dbdd6a027bce79ad336c5" data-og-width="694" width="694" data-og-height="358" height="358" data-path="images/screenshots/to-do-error-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-error-page.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=4aa4d37f829fe9c8499922dc28d402a3 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-error-page.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=696bcd5f97465d61fb8c52d9a4bda441 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-error-page.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=da9bb599b59ec7eead69a44527bb50d1 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-error-page.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=9be729658ba8f27caa13af5a8e58ea05 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-error-page.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=dd536580bc48219ed0d0f55cb1a8f036 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/to-do-error-page.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=3c26ab4b3ee76c1d651684c6f65d5a52 2500w" />
