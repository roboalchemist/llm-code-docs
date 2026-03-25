# Source: https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/servicenow-oauth-authentication.md

# ServiceNow OAuth Authentication

To set up OAuth authentication, begin by creating credentials in the Application Registry. Once set up, these credentials allow you to connect a ServiceNow instance to Getint, enabling seamless data synchronization.

### Creating Application Registry for OAuth Authentication <a href="#creating-application-registry-for-oauth-athentication" id="creating-application-registry-for-oauth-athentication"></a>

#### 1. Find Application Registry in All tab

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmxNbrvZHnObLcGNajXs4%2FCreator%20studio%20main%20screen.png?alt=media&#x26;token=79f28c1d-9acf-4608-90e4-f0851b74e8a2" alt=""><figcaption></figcaption></figure>

#### 2. Create a New Application Registry <a href="#id-2.-create-new-application-registry" id="id-2.-create-new-application-registry"></a>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCYl42wUpdSXMGqaQnADJ%2FCreate%20a%20new%20application%20registry.png?alt=media&#x26;token=2b1107c9-613a-40bd-a207-1bb8bc8a5da0" alt=""><figcaption></figcaption></figure>

#### 3. Click Create an OAuth API endpoint for external clients <a href="#id-3.-click-create-an-oauth-api-endpoint-for-external-clients" id="id-3.-click-create-an-oauth-api-endpoint-for-external-clients"></a>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVM9cQQe99UExoJnQa6aO%2FAPI%20endpoint.png?alt=media&#x26;token=bbc289ed-337a-4de8-9a8b-29790a382341" alt=""><figcaption></figcaption></figure>

#### 4. Fill in the Name input and Submit <a href="#id-4.-fill-the-name-input-and-submit" id="id-4.-fill-the-name-input-and-submit"></a>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIcn8QYvfP3thqEkAUHt7%2Ffilling%20in%20name%20input.png?alt=media&#x26;token=2cc8c551-47d1-4cec-af83-4811df6e9422" alt=""><figcaption></figcaption></figure>

#### 5. Enter the newly created Application Registry <a href="#id-5.-enter-newly-created-application-registry" id="id-5.-enter-newly-created-application-registry"></a>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQjmbND50aVZe2Gpn4lZq%2FEnter%20application%20registry.png?alt=media&#x26;token=6207fffc-7632-45a6-ab19-86b009ad1f77" alt=""><figcaption></figcaption></figure>

#### 6. Click the padlock to show the Client Secret <a href="#id-6.-click-padlock-to-show-client-secret" id="id-6.-click-padlock-to-show-client-secret"></a>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F98GJmJcfWGon4IeQsp4e%2FClient%20secret.png?alt=media&#x26;token=5d2cc427-edf4-496e-ab48-4e66dd951300" alt=""><figcaption><p>Generated client ID and client secret can be now used during connection setup in Getint.</p></figcaption></figure>

### **Generating Access & Refresh tokens manually via POSTMAN** <a href="#generating-access-and-refresh-tokens-manually-via-postman" id="generating-access-and-refresh-tokens-manually-via-postman"></a>

#### 1. Create POST request: <a href="#id-1.-create-post-request" id="id-1.-create-post-request"></a>

* Set **URL** to https\://**instance**.service-now\.co&#x6D;**/oauth\_token.do**
* Select **x-www-form-urlencoded** in the **Body** tab and add the following properties:
  * **client\_id** - client\_id from Application Registry
  * **client\_secret** - client\_secret from Application Registry
  * **username** - ServiceNow User name
  * **password** - ServiceNow User password
  * **grant\_type** - must be named **password**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaIYyxIaP17ONvu7nBWwX%2FPostman%20configuration.png?alt=media&#x26;token=08dbd0b2-9b03-415d-81ef-6c5faca80d08" alt=""><figcaption></figcaption></figure>

#### 2. You will get the following response <a href="#id-2.-you-will-get-the-following-response" id="id-2.-you-will-get-the-following-response"></a>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrjzeLJXrAoLZyaLzpSmv%2FPostman%20response.png?alt=media&#x26;token=29cf7f45-d286-4fe9-b442-911644b3d62b" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
At Getint we take feedback seriously. Our company aims to bring solutions to many different use cases. Therefore, we highly advise you to contact our [Support Team](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team), if you require further assistance.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
