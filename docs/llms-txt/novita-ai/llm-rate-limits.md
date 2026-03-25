# Source: https://novita.ai/docs/guides/llm-rate-limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate limits

export const DynamicRPMList = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    let attempts = 0;
    const maxAttempts = 50;
    const formatAmount = num => {
      if (typeof num === "number") {
        return num.toLocaleString();
      }
      return num || "-";
    };
    const interval = setInterval(() => {
      const clientComponent = document.getElementById("dynamic-rpm-list");
      if (clientComponent && window.novitaRemoteData.llmModels.status === 'loaded') {
        const modelList = window.novitaRemoteData.llmModels.data.filter(model => {
          return Boolean(model.rpm);
        });
        const allModels = modelList.map(model => {
          const t1 = (model.quota_items || []).find(item => item.tier === "T1") || ({});
          const t2 = (model.quota_items || []).find(item => item.tier === "T2") || ({});
          const t3 = (model.quota_items || []).find(item => item.tier === "T3") || ({});
          const t4 = (model.quota_items || []).find(item => item.tier === "T4") || ({});
          const t5 = (model.quota_items || []).find(item => item.tier === "T5") || ({});
          return `
            <tr>
              <td rowspan="2" style="vertical-align: middle; max-width: 230px">${model.id}</td>
              <td>RPM</td>
              <td>${formatAmount(t1.rpm)}</td>
              <td>${formatAmount(t2.rpm)}</td>
              <td>${formatAmount(t3.rpm)}</td>
              <td>${formatAmount(t4.rpm)}</td>
              <td>${formatAmount(t5.rpm)}</td>
            </tr>
            <tr>
              <td>TPM</td>
              <td>${formatAmount(t1.tpm)}</td>
              <td>${formatAmount(t2.tpm)}</td>
              <td>${formatAmount(t3.tpm)}</td>
              <td>${formatAmount(t4.tpm)}</td>
              <td>${formatAmount(t5.tpm)}</td>
            </tr>
          `;
        }).join('');
        clientComponent.innerHTML = `
          <table class="table table-big">
            <thead>
              <tr>
                <th>Model</th>
                <th></th>
                <th>T1</th>
                <th>T2</th>
                <th>T3</th>
                <th>T4</th>
                <th>T5</th>
              </tr>
            </thead>
            <tbody>
              ${allModels}
            </tbody>
          </table>
        `;
        clearInterval(interval);
      }
      attempts++;
      if (attempts >= maxAttempts) {
        clearInterval(interval);
      }
    }, 200);
    return <div id="dynamic-rpm-list"></div>;
  }
};

Rate limits control how frequently users can make requests to our LLM API within specific time periods. Understanding and working within these limits is essential for optimal API usage.

## 1. Understanding Rate Limits

### What are Rate Limits?

Rate limits restrict the number of API requests that can be made within defined time periods. They help:

* Prevent API abuse and misuse;
* Ensure fair resource distribution among users;
* Maintain consistent API performance and reliability;
* Protect the stability of our services.

### Default Rate Limits

Each account has a default rate limit for model calls, measured in RPM (requests per model per minute) and TPM (tokens per model per minute). Rate limits vary by account tier, as outlined in the tables below.

<table class="table table-big">
  <thead>
    <tr>
      <th class="min-w-10">Tier</th>
      <th>How to reach</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>T1</td>
      <td>Monthly top-ups did not exceed \$50 in any of the last 3 calendar months.</td>
    </tr>

    <tr>
      <td>T2</td>
      <td>Monthly top-ups were at least \$50 but did not exceed \$500 in any of the last 3 calendar months.</td>
    </tr>

    <tr>
      <td>T3</td>
      <td>Monthly top-ups were at least \$500 but did not exceed \$3,000 in any of the last 3 calendar months.</td>
    </tr>

    <tr>
      <td>T4</td>
      <td>Monthly top-ups were at least \$3,000 but did not exceed \$10,000 in any of the last 3 calendar months.</td>
    </tr>

    <tr>
      <td>T5</td>
      <td>Monthly top-ups were at least \$10,000 in at least one of the last 3 calendar months.</td>
    </tr>
  </tbody>
</table>

<Tip>The last 3 calendar months refers to the current month and the two months before it.</Tip>

Default Rate Limit by Tier (RPM / TPM):

<DynamicRPMList />

## 2. Handling Rate Limits

### How to Monitor Rate Limits?

When you exceed the rate limit, the API will return:

* HTTP Status Code: 429 (Too Many Requests);
* A rate limit exceeded message in the response body.

### Best Practices

To avoid hitting rate limits:

1. Implement request throttling in your application;
2. Add exponential backoff for retries;
3. Monitor your API usage patterns.

### When You Hit Rate Limits

If you receive a 429 error, you can:

1. **Retry Later**: Wait a short period before retrying your request;
2. **Optimize Requests**: Reduce request frequency;
3. **Rate Limits Increase**: For higher rate limits, you can:
   * <a href="https://discord.gg/YyPRAzwp7P" target="_blank">Contact us through Discord</a>
   * or <a href="https://meet.brevo.com/novita-ai/contact-sales" target="_blank">Book a call with our sales team</a>

***

**If you have any questions, [please reach out to us on Discord](https://discord.gg/YyPRAzwp7P).**


Built with [Mintlify](https://mintlify.com).