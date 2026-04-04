# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps.md

# Android

You can deploy the agents built on the Avaamo Platform into your Android channel to facilitate easy communication with Android mobile users. This helps to clearly distinguish and monitor the user interactions from the Android channel separately. See [Channels in Analytics](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics), for more information.

{% hint style="info" %}
**Note**: You can connect to a channel only if it is enabled for your account or company. If you wish to enable a channel, then contact Avaamo Support for further assistance. Note that only the web channel is enabled by default.&#x20;
{% endhint %}

### Channel settings

{% hint style="success" %}
**Key points**:&#x20;

* All the properties, parameters, and callback functions as applicable for the web channel are also available for the Android channel. See [Web channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel), for more information.
* After you configure the channel settings, you can view, edit, disconnect and delete the channel settings as per your requirements. See [Manage channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/manage-channel-settings), for more information.
* You can also deploy your agent on multiple instances of the Android channel similar to the web channel. See [Deploy in multiple web channel instances](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/deploy-and-test-web-channel), for more information.
  {% endhint %}

The following lists a few properties that distinguish a Web channel from an Android channel:

* **Advanced -> Android page URL:** Indicates the page where the agent is deployed for Android mobile users. See [Suggested steps to deploy](#suggested-steps-to-deploy), for more information on this feature can be useful.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbeRBtUYsGNvDyuPmZN%2F-MbeRvWn5J31DgJNqgsU%2F5.7-android-channel-page-url.png?alt=media\&token=0d3968f3-0a21-4253-a49c-7b51fb096e4e)

<table><thead><tr><th width="150">Properties</th><th>Description</th></tr></thead><tbody><tr><td>Android page URL</td><td>Indicates the page where the agent is deployed for Android mobile users.</td></tr><tr><td>Embed code</td><td>Script that must be embedded in the Android apps to render the agent. Note that this URL is different from the web channel URL. </td></tr></tbody></table>

* **Deployment -> Copy your embed code**: Script that must be embedded in the Android channel to render the agent. Note that this URL is different from the web channel URL. See [Suggested steps to deploy](#suggested-steps-to-deploy), for more information on this feature can be useful.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbeZkydx3380Zztkbzm%2F-Mbe_N5Rs9MM4imyyCrz%2F5.7-android-channel-embed-code.png?alt=media\&token=56fc877e-f454-4431-8c97-3932a8ab7849)

### Suggested steps to deploy

Consider that you have a website where you are required to deploy your agent. You wish to monitor the user interactions from the web channel and Android Apps channel separately for analytics. You can deploy your agent in both the channels with the same user experience as follows:

Consider that you have a website where you are required to deploy your agent. You wish to monitor the user interactions from the web channel and Android channel separately for analytics. You can deploy your agent in both the channels as follows:

* Create a blank page that has the same base URL as the website. **Example**: If your website is <http://www.macpizza.com/>, then you can create a blank page with <http://www.macpizza.com/android.php>.
* In the Android channel page, specify the URL <http://www.macpizza.com/android.php> in the **Android page URL**.
* Deploy your agent in the page <http://www.macpizza.com/android.php> using the **Embed code** in the Android channel.
* Test your agent from any Android device to verify the implementation.
* In the main website <http://www.macpizza.com/> source, include the script tag with the following code:

```javascript
<script type="text/javascript">
  if(<<androidDevice>>){
    <<Android Channel URL>>
  }
  else{
    <<Web Channel URL>>
  }
</script>
```

The following is a detailed script that checks if the device is android and launches the agent URL accordingly:

```javascript
if(navigator.userAgent.toLowerCase().indexOf("android") != -1){
    var AvaamoChatBot = function(t) {
    function o(t, o) {
        var n = document.createElement("script");
        n.setAttribute("src", t), n.onload = o, document.body.appendChild(n)
    }
    return this.options = t || {}, this.load = function(t) {
        o(this.options.url, function() {
            window.Avaamo.addFrame(), t && "function" == typeof(t) && t(window.Avaamo)
        })
        }, this
    };
    var bot_url = <<android channel URL>>;
    var custom_property = '';
    var url = bot_url + "&custom_properties[userdata]=usernotlogged";
    var chatBox = new AvaamoChatBot({
        url: url
    });
    chatBox.load(function (avaamo) {
      avaamo.onChatBoxClose = function () {
        window.Avaamo.sendMessage("#clear");
      }
    });
  }
  else{
    var AvaamoChatBot = function(t) {
      function o(t, o) {
          var n = document.createElement("script");
          n.setAttribute("src", t), n.onload = o, document.body.appendChild(n)
      }
      return this.options = t || {}, this.load = function(t) {
          o(this.options.url, function() {
              window.Avaamo.addFrame(), t && "function" == typeof(t) && t(window.Avaamo)
          })
      }, this
    };
    var bot_url = <<Web channel URL>>;
    var custom_property = '';
    var url = bot_url + "&custom_properties[userdata]=usernotlogged";
    var chatBox = new AvaamoChatBot({
        url: url
    });
    chatBox.load(function (avaamo) {
      avaamo.onChatBoxClose = function () {
        window.Avaamo.sendMessage("#clear");
      }
    });
  }
```
