# Source: https://developers.make.com/custom-apps-documentation/create-your-first-app/test-your-app.md

# Test your app

To test your app in Make, create a new scenario.

{% stepper %}
{% step %}
In the Scenario Builder, add the **Geocodify > Search geolocation** module that you have just created.

Note that is has the **Private** tag.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-f975d0aad750bca3a4d9478d23c1ee5605d1b135%2Faddgeocodifyappmodule.png?alt=media" alt="" width="493"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click **Create a connection**.
{% endstep %}

{% step %}
Enter your API Key from the Geocodify API.
{% endstep %}

{% step %}
Click **Save**.
{% endstep %}

{% step %}
Insert the address you want to geolocate, for example: Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France.

This is the Location parameter you set up in the Mappable parameters tab.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-68e16ec4a963df8180263aa35947e8c0a4537b69%2Faddressforgeocodify.png?alt=media" alt="" width="520"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click **Save** to save the module.
{% endstep %}

{% step %}
Save the scenario. A pop-up appears appears asking for confirmation to install the app in your organization.

* Click **Yes** on the pop-up to install the app in your organization.
* Click **Run once** to run the scenario.
  {% endstep %}

{% step %}
Open the output to retrieve the coordinates. They are under **Output> Bundle 1>** **response> features> 1> geometry> coordinates**.

The coordinates are output this way because you chose to return the response as is, without filtering or customization.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-13f202bc38bcf1e4f011a8a447fe4fa63f570a8f%2Fgeocodify_output.png?alt=media" alt="" width="320"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

Your app works. Congratulations!

At this point, your module is hidden by default. Even if the app is installed in the organization, it won't appear in the scenario editor for other users until you make it visible.

To let other users see your module, go to the module in the app setup and slide the toggle from hidden to visible.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-2cda5e70e1d8e8e6651677826be8e0fa81494346%2Fmodulevisible.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

To learn more about app and module visibility, see the [App visibility article](https://developers.make.com/custom-apps-documentation/create-your-first-app/app-visibility).
