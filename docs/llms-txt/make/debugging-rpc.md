# Source: https://developers.make.com/custom-apps-documentation/debug-your-app/debugging-rpc.md

# Remote Procedure Calls

To find the RPC debug tool:

{% stepper %}
{% step %}
Navigate to the Custom apps area.
{% endstep %}

{% step %}
Select your custom app from the list.
{% endstep %}

{% step %}
Click the **Remote Procedures** tab.
{% endstep %}

{% step %}
Select the RPC you want to debug.
{% endstep %}

{% step %}
Click **Test RPC**.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-392e813b6a574f56a4e259b4ac88075294a682c7%2Ftestrpc.png?alt=media" alt="" width="563"><figcaption><p><br></p></figcaption></figure></div>
{% endstep %}
{% endstepper %}

## RPC page

Compare the tabs below to learn how to access information about your RPCs in Make.

### Communication tab

After creating a new RPC, you can modify the default template in the Communications tab for your needs.

{% tabs %}
{% tab title="Default Communication" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-e4b42ed0bcd526e6c015389b4abe1c72a33b8c7b%2FdefaultRPCcommunication.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Inside RPC, you can use the relative path and the full form of the URL.

However, we advise using the relative path across all your RPCs and modules.

A relative path is added to the `"baseUrl"` that you need to specify inside the app Base.
{% endhint %}
{% endtab %}

{% tab title="Customized Communication" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-90ec2af7604ded25d9ed806195f05dc00cb3a3bb%2FcustomizedRPCcommunication.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}
{% endtabs %}

### Parameters tab

By default, the Parameters tab is empty. Here you can add any parameter you need. You can also add mappable parameters from a module. [Learn more about using RPC parameters](https://developers.make.com/custom-apps-documentation/app-components/rpcs/dynamic-options-rpc#select-parameter-with-rpc-options).

{% tabs %}
{% tab title="Default parameters" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-325b6cd89042f6259ff00ca8bf95847abc155eab%2FdefaultRPCparameters.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Any parameter created inside an RPC will be available only for RPC debugging. It will not be visible inside your modules or inside scenarios.

To preview and test parameters, click on the **Test RPC** button.
{% endhint %}
{% endtab %}

{% tab title="Customized parameters" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-d9b8ac757d280a22397fad4027fdc68848710706%2FcustomizedRPCparameters.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Default preview" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-edc34ef12a0d25ea58b657f065defb7f62cb4efb%2FRPCdefaultpreview.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Customized preview with parameters" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-c0c5d0af3885a4168e1c55e9fc13a7f95b752190%2FRPCpreviewwithparameters.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}
{% endtabs %}

## RPC debug tool

The RPC debug tool works the same way modules do.

1. Specify the connection and other fields (parameters) if needed.
2. Click the **Test** button.
3. The call, which you specified before in the RPC communication, will be executed.

You will see the `output` that you specified in the RPC communication.

If you specified output as "`label"` and `"value"` (with the purpose of using it inside a Select parameter), do not expect to see the full server response there.

{% hint style="info" %}
Sometimes you might get an empty array as a response. If that's not the response that you expected, check that you correctly specified the path to the object, which you use inside `iterate`.
{% endhint %}

{% tabs %}
{% tab title="Input" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-c6343f9105493e939724abc521ab176bda5871b3%2FRPCinput.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Output" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-0154393af2e9b6857c5acfae97e5e3b79d9fc7f6%2FRPCoutput.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Communication code" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-90ec2af7604ded25d9ed806195f05dc00cb3a3bb%2FcustomizedRPCcommunication.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}
{% endtabs %}

## Debug RPCs in the dev console

Sometimes you may need to look into the request you're sending and the response from the API.

You can see more details about the RPC you're testing by opening your browser's dev console: Network tab.

The `debug` values show the request being sent and the response received by the API.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-4263004f8e645a7fad6766e3b3c7a17659605426%2Fdebugrpc.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
