# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/forward-call-c-ivr-channel.md

# Forward call (C-IVR channel)

You can use `SmartCall.forward` method to forward the call to another number such as a help center number or a call center number, in case the user requires any further assistance in the C-IVR flow.

{% hint style="info" %}
**Note**: This option works if you have deployed your agent in the C-IVR channel. See the [C-IVR channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone), for more information.
{% endhint %}

```javascript
return SmartCall.forward(<<message>>,<<phoneno>>);
```

* **message**: Specify any message that you wish to be read out to the user before forwarding the call to the number.
* **phoneno**: Provide the complete phone number with a country code.

Consider that you have an "Order Status" skill in your pizza agent that checks for the order status using the order number provided by the user.&#x20;

* You have deployed your agent in the C-IVR channel.&#x20;
* You have designed a flow, where you wish to transfer the call to an agent if requested by the user.&#x20;
* You can use the following JS method to forward the call or use can use the [Call forward](https://docs.avaamo.com/user-guide/how-to/build-skills/using-dialog-designer/create-new-skill/build-skill-responses/add-skill-messages-responses#call-forward) response from the UI.

```javascript
return SmartCall.forward("Forwarding to an agent. Please wait.","+918887651234");
```

### For "**refer"** transfer mode

You can use `SmartCall.forward` method to forward the call to a SIP number when you have deployed your agents on [Genesys](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/genesys), [SIP](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/sip), [Nice InContact](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/nice-incontact) channels.

```javascript
return SmartCall.forward("<<message>>", "<<SIP number>>?call_type=sip", {<<Header>>});
```

{% hint style="info" %}
**Note:**&#x20;

* You must get the <\<SIP number>> from the customer call stack. This is the number where Avaamo Platform forwards the call.
* You must also get the details of the specific headers that must be passed in the call forward request.
  {% endhint %}

**Example**: The following example illustrates a Nice InContact SIP call forward request:

```javascript
return SmartCall.forward("Please hold on! Let me transfer your call to a care specialist", 
"+14003460060?call_type=sip", 
{"X-NICE-CXONE-CONTACT-ID": context.x_in_contact_contact_id });
```
