# Source: https://developers.make.com/api-documentation/troubleshooting/common-issues.md

# Troubleshooting

This section describes most common mistakes that result in API-related problems, such as receiving `Access denied` or `Not found` errors. You can also refer to the [HTTP status error codes](https://developers.make.com/api-documentation/troubleshooting/http-status-codes) for more details.

* **Using HTTP instead of HTTPS in the URL**

  Use HTTPS at the beginning of the URL in your request. This is required for security reasons.
* **Using an incorrect environment**

  If you have access to more than one Make environment, ensure that you use the correct environment in the URL and that you use a valid authentication token generated for this specific environment.
* **Using an incorrect endpoint**

  Ensure there are no empty or white spaces in the endpoint URL and that there are no backslash symbols at the end of the URL after the endpoint name.
* **Missing authentication details or using incorrect authentication details**

  Ensure that you are using the correct authentication details. To make a successful request, you need to have the correct [authentication token](https://developers.make.com/api-documentation/authentication/authentication-managing) with the correct scopes assigned to it.

  <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p>Note that you need a separate token for each Make environment.</p></div>
* **Missing access to the requested resource**

  Ensure that scopes assigned to your authentication token correspond to the requested resource.

{% hint style="warning" %}
Note that you cannot access administrator resources if you are a regular Make user.
{% endhint %}

* **Missing required parameters or using invalid or improperly formatted parameters**

  Many endpoints require at least one mandatory parameter. Often it is the **teamId** or an ID of the specific resource. Do not forget to add the required parameters to the request. Also, note that query, path, and pagination parameters need to be properly formatted. The first query parameter should start with a question mark. Separate parameters with the ampersand symbol. Some special characters, for example, in the [pagination](https://developers.make.com/api-documentation/pagination-sorting-filtering/pagination-and-sorting) parameters, need to be encoded when used in URLs.
* **Sending an invalid or improperly formatted request body**

  The structure of the API request body must conform to the JSON schema standard. You can use JSON validators available on the internet to validate your request body before sending it.

{% hint style="warning" %}
If your issue is not mentioned in the table above and the [error code message](https://developers.make.com/api-documentation/troubleshooting/http-status-codes) do not indicate how to resolve the issue, please contact us via the help form at [Make Help center](https://www.make.com/en/help). Include a detailed description of the problem, the full request, and the error code and error message that you received.
{% endhint %}
