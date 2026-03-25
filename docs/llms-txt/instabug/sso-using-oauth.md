# Source: https://docs.instabug.com/organization-settings/user-management/sso-using-oauth.md

# SSO Using OAuth

### Configuration Steps:

To configure Luciq with your OAuth SSO service provider, you’ll need to follow these steps:

1. Create an account on [Auth0](https://auth0.com/).

2. From the left navigation bar, click on Applications > Applications.

   <figure><img src="https://downloads.intercomcdn.com/i/o/ih9pma6x/1736831997/f2a0ced78c135ace19871f6e87d9/image.png?expires=1764258300&#x26;signature=077907c9e53de0e54318e7ac8b6ee9798c041ee414d450609b5d312614dfe2f0&#x26;req=dSckEMF9nIhWXvMW1HO4zS2FxAvZKnzSkFYvUmgIQyXybX71Bz8mWLf%2F0BJO%0AExGL%0A" alt=""><figcaption></figcaption></figure>

3. Open the default app.

4. Configure OAuth using the data found in the default app page
   1. On the Luciq Dashboard, navigate to Identity Access Management Settings, then navigate to [SSO](https://dashboard.instabug.com/company/sso) and click on Configure OAuth.

      <figure><img src="https://downloads.intercomcdn.com/i/o/ih9pma6x/1736824710/73246dd82f4ddbab177fbc38c628/image.png?expires=1764258300&#x26;signature=f40717325d779d490bad2f22bc13df34792fbf31e01d4ec4f948032a27850036&#x26;req=dSckEMF8mYZeWfMW1HO4zetmf6OfnHRVHr7vdGLsnYpQ%2F2rsNolzRS0fc%2Fc2%0A6oQi%0A" alt=""><figcaption></figcaption></figure>

      Fill in the fields with the following data:

      1. Client ID:

         <figure><img src="https://downloads.intercomcdn.com/i/o/ih9pma6x/1401654343/296cfe9abe04e751ebf37fed280e/image.png?expires=1764258300&#x26;signature=f62280ac4d1b218e343199c089364caaf73c9b34e2943158f23be109958dcdae&#x26;req=dSQnF897mYJbWvMW1HO4zdN6o2KJSC0Hfc%2BqjYQD63KfhU4TvWh62E5VMPsj%0ANjpZ%0A" alt=""><figcaption></figcaption></figure>

      2. Client Secret:

         <figure><img src="https://downloads.intercomcdn.com/i/o/ih9pma6x/1401654752/0514af0f906470774db17e0607c1/image.png?expires=1764258300&#x26;signature=f5bf2213b71bfc14a2f7bfe33c335ac8246249fe801139f056214ef9fdaa19a5&#x26;req=dSQnF897mYZaW%2FMW1HO4zf6oiqJWpa2vqHZG39rpAQD7%2FpyzEUpz688mX%2BrB%0ATxXX%0A" alt=""><figcaption></figcaption></figure>

      3. Authorization & Token URLs:\
         Scroll all the way down to the “Advanced Settings” section and open the “Endpoints” tab.”

         <figure><img src="https://downloads.intercomcdn.com/i/o/ih9pma6x/1401655449/2b9287fb903f4e9f29d761b694dc/image.png?expires=1764258300&#x26;signature=82a36df9b98f2ed76a3a03916327548f94c11f72b7dc4162b3972cadc0879593&#x26;req=dSQnF897mIVbUPMW1HO4zV8fZL%2FbVyWCfy4eTMacEB43I39cqFYubZtFqvGg%0Ae8Nw%0A" alt=""><figcaption></figcaption></figure>

   2. On the default app settings page, add your Luciq company’s callback URL
      1. *Note: You can add multiple callback URLs by separating them with a comma.*

         <figure><img src="https://downloads.intercomcdn.com/i/o/ih9pma6x/1736833129/6ac026f24da40f9ca0c1ad11bd6a/Screenshot+2025-09-22+at+12_16_44%E2%80%AFAM.png?expires=1764258300&#x26;signature=ea573c9ee74135ed8d3a96cf1c313b23b03e7424554f08499193f27ac70443d0&#x26;req=dSckEMF9noBdUPMW1HO4zXmuzw2YBRw8ABLr2rvuIgSNfQEj0Z82FKRfTvz%2B%0AyTwL%0A" alt=""><figcaption></figcaption></figure>

   3. Save changes on both the dashboard and the default app settings page

{% hint style="info" %}
To activate your integration, you will need to log in at least once via [SSO](https://dashboard.instabug.com/sso_login)
{% endhint %}
