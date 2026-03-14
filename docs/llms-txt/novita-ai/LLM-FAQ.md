# Source: https://novita.ai/docs/guides/LLM-FAQ.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM FAQs

## Voucher Usage Guide

### What types of voucher does Novita provide?

Novita currently offers the following types of vouchers to help users experience the platform's services:

* **New User Voucher**: Available to first-time registered users for trying out services of various types of models.
* **Referral Voucher**: Earned by inviting others to register and complete tasks on the platform.

## Rate Limits for Model Usage

### What are the RPM limits for different users?

RPM (Requests Per Minute) limits vary based on a user's verification level and account status. For detailed limits, please refer to the official documentation:

<Tip>
  👉 For further assistance, please [book a call with our sales team](https://meet.brevo.com/novita-ai/contact-sales)
</Tip>

## RPM Adjustment and Upgrade Policy

### Can users apply for increased RPM limits?

Yes. Novita allows flexible RPM upgrades based on usage needs. Rules are listed as below:

* **DeepSeek models**: The platform will strive to accommodate reasonable scaling needs.
* **Other models**: RPM increases are evaluated based on model cost and actual user behavior, subject to capacity availability.

### **Application process:**

User → Customer Manager / Tech Support → Product Team Review & Approval

### **What happens if actual usage falls short of the committed RPM?**

If the user's actual RPM remains below the committed level for one consecutive week, the platform will adjust the rate limits policy as:

* Reduce the limit to the peak RPM in the past week, or
* Revert to the model's default rate limit (whichever is lower).

### **Is self-service RPM upgrade supported?**

Yes. Novita plans to launch an **RPM Upgrade Package**, allowing users to manage and increase RPM limits independently, without manual approval.

For further assistance, please [book a call with our sales team](https://meet.brevo.com/novita-ai/contact-sales).

### How to control thinking function of Zai-org/GLM-4.5 when calling its API?

When calling API zai-org/glm-4.5, there always exists some situations where thinking function is not needed. In these cases, if you want to turn thinking function off, you can simply add one fixed sentence called:

```python  theme={"system"}
"enable_thinking": false 
```

at the bottom, for example:

```python  theme={"system"}
{
  "model": "zai-org/glm-4.5",
  "messages": [
  {
   "role": "user",
   "content": "How is the weather in New York?"
  }
 ],
 "temperature": 0.7,
 "stream": false,
 "max_tokens": 500,
 "tool_choice": "auto",
 "enable_thinking": false
}
```


Built with [Mintlify](https://mintlify.com).