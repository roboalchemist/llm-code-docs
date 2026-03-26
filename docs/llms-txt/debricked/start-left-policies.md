# Source: https://docs.debricked.com/product/open-source-select/start-left-policies.md

# Start left policies

{% hint style="info" %}
*The Start Left feature is only available for* [*Select Enterprise*](https://debricked.com/pricing/) *users. Already have an account?* [*Click here to upgrade.*](https://debricked.com/app/en/repositories?billingModal=free,enterprise)
{% endhint %}

You can use your automation policies to evaluate new packages in Open Source Select. If you are looking for a new package in Select, you can check whether or not it will trigger an automation rule using Start Left Policies.&#x20;

### **Evaluate license issues using start left policies (example)**

1. Create an automation rule to evaluate the licenses family. For example, “If there is a dependency which is licensed under a strong copyleft license then fail pipeline”.
2. Go to **Open Source Select** and search for a desired package.
3. After searching for the \`node-forge\` package, you can see that the pipeline would fail if this package is included, as it is licensed under \`GLP-2.0-only\` which belongs to the "strong copyleft" licenses family.

### **Evaluate security risk packages using start left policies (example)**

1. Create an automation rule to evaluate the check the CVSS. For example, "If a dependency contains a vulnerability which has not been marked as unaffected where CVSS is at least medium (4.0-6.9)”
2. Go to **Open Source Select** and search for a desired package.
3. After searching for the \`angularjs\` package, you can see that our pipeline would trigger a warning if we included this package, due to CVE-2017-16009.

### Choose open source components with OpenText Core SCA's open source select and start left - video guide

{% embed url="<https://www.youtube.com/watch?t=1s&v=JCgA1DjAq8A>" %}
