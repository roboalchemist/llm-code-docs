# Source: https://developers.make.com/custom-apps-documentation/best-practices/instant-triggers-scheduled.md

# Instant triggers (scheduled)

An instant trigger is a webhook that starts a scenario whenever new data arrives.

Your app should implement a fully functional instant trigger as a [Watch module](https://developers.make.com/custom-apps-documentation/app-components/modules/instant-trigger), even if an API might have endpoints like Get a webhook, List webhooks, or Update a webhook.

## Connect metadata

Always save the metadata in the connection if

* the endpoint that can obtain authenticated user’s information is available, and
* the information provided is able to distinguish the connection.

When naming your connection, provide as much information as possible. This provides better identification on the connection page. The following information is suggested:

* Name
* Email
* User ID
* Organization / Company / Location / Tenant

{% tabs %}
{% tab title="Good practice" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-92dd28a1ae032b413e2ba76d0f39704c2f27c186%2Finstanttriggers_goodpractice.png?alt=media" alt="" width="344"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Bad practice" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-47484687f7ea21bd0e6383f13c462a703ed8528e%2Finstanttriggers_badpractice.png?alt=media" alt="" width="370"><figcaption></figcaption></figure></div>
{% endtab %}
{% endtabs %}

### Example - Constant Contact

{% tabs %}
{% tab title="Source" %}

```json
{
	"info": {
		"url": "https://api.cc.email/v3/account/summary",
		"method": "GET",
		"headers": {
			"authorization": "Bearer {{connection.accessToken}}"
		},
		"response": {
			"error": {
				"message": "[{{statusCode}}]\n{{parseError(body)}}"
			},
			"uid": "{{body.encoded_account_id}}",
			"metadata": {
				"type": "text",
				"value": "{{body.contact_email}}"
			}
		},
		"log": {
			"sanitize": ["request.headers.authorization"]
		}
	}
}
```

{% endtab %}
{% endtabs %}

## UID

Always save the UID in the connection if the service supports a single webhook URL per app (a shared webhook). The saved UID must match the ID that is included in the incoming webhook payload.

### Example - Highlevel OAuth 2.0

{% tabs %}
{% tab title="Connection" %}

```json
{
	"url": "https://services.leadconnectorhq.com/locations/{{connection.locationId}}",
	"method": "GET",
	"headers": {
		"Authorization": "Bearer {{connection.accessToken}}",
		"Version": "2021-07-28"
	},
	"response": {
		"uid": "{{connection.locationId}}",
		"metadata": {
			"type": "text",
			"value": "Location: {{body.location.name}}"
		}
	},
	"log": {
		"sanitize": [ "request.headers.authorization" ]
	}
}
```

{% endtab %}

{% tab title="Incoming webhook payload" %}

```json
{
    "type": "ContactCreate",
    "locationId": "ve9EPM428h8vShlRW1KT",
    "id": "nmFmQEsNgz6AVpgLVUJ0",
    "address1": "3535 1st St N",
    "city": "ruDolomitebika",
    "state": "AL",
    "companyName": "Loram ipsum",
    "country": "DE",
    "source": "xyz form",
    "dateAdded": "2021-11-26T12:41:02.193Z",
    "dateOfBirth": "2000-01-05T00:00:00.000Z",
    "dnd": true,
    "email": "JohnDeo@gmail.comm",
    "name": "John Deo",
    "firstName": "John",
    "lastName": "Deo",
    "phone": "+919509597501",
    "postalCode": "452001",
    "tags": [
        "id magna sed Lorem",
        "Duis dolor commodo aliqua"
    ],
    "website": "https://www.google.com/",
    "attachments": [],
    "assignedTo": "nmFmQEsNgz6AVpgLVUJ0"
}
```

{% endtab %}
{% endtabs %}
