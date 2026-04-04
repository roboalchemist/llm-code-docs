# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/smartcall-c-ivr.md

# SmartCall (C-IVR)

You can use the following function in your C-IVR flow to either forward a call or to hang up the call with a message:

* [SmartCall.forward](#smartcall.forward):&#x20;
  * Forward the call to another number such as a help center number or a call center number, in case the user requires any further assistance in the C-IVR flow.&#x20;
  * This is also used to forward the call to a SIP number when you have deployed your agents on [Genesys](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/genesys), [SIP](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/sip), [Nice InContact](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/nice-incontact) channels.
* [SmartCall.hangup](#smartcall.forward-sip): Hangs up the call in the C-IVR flow with a message.

{% hint style="info" %}
**Note**: This option works if you have deployed your agent in the C-IVR channel. See the [C-IVR channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone), for more information.
{% endhint %}

### SmartCall.forward

The following is the syntax to forward the call to a number with a message in the C-IVR flow:

```javascript
return SmartCall.forward(<<message>>,<<phoneno>>);
```

#### **Example**&#x20;

```javascript
return SmartCall.forward("Forwarding to an agent. Please wait.","+918887651234");
```

See [Forward call (C-IVR channel)](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/forward-call-c-ivr-channel), for a sample scenario.

### SmartCall.forward (SIP)

The following is the syntax to forward the call to a number with a message in SIP:

```javascript
return SmartCall.forward("<<message>>", "<<SIP number>>?call_type=sip", {<<Header>>});
```

#### **Example**&#x20;

```javascript
return SmartCall.forward("Please hold on! Let me transfer your call to a care specialist", 
"+14003460060?call_type=sip", 
{"X-NICE-CXONE-CONTACT-ID": context.x_in_contact_contact_id);
```

See [Forward call (C-IVR channel)](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/how-to/forward-call-c-ivr-channel#for-refer-transfer-mode), for a sample scenario.

### SmartCall.hangup

The following is the syntax to hang up the call in the C-IVR flow with a message:

```javascript
return [<<message>>, SmartCall.hangup()];
```

#### **Example**&#x20;

```javascript
return ['You order is on its way and will be delivered in 20 minutes. Hanging up the call now. Have a good day.',SmartCall.hangup()];
```

See [Hangup call (C-IVR channel)](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/hangup-call-c-ivr-channel), for a sample scenario.
