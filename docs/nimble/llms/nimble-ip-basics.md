# Source: https://docs.nimbleway.io/general/onboarding-guide/nimble-ip-basics.md

# Nimble IP Basics

{% embed url="<https://www.loom.com/share/5a543dd1ec7544e6bcaabb0242a38e0d?sid=8349cb8a-6a9b-4be4-b7a4-16e623336686>" %}

Welcome to Nimble IP - our modern, high-performance proxy network! Nimble IP works using a Backconnect Gateway - a managed, single point of access - that you connect to using a standard proxy syntax. If you've never used proxies before, don't worry! By the end of this guide, you'll have sent your first request.

### Setting Up an IP Pipeline

By default, you account will come with an out-of-the-box IP pipeline. If you prefer to keep things simple, feel free to skip this step and just use that pipeline. However, as your usage expands, pipelines will become more and more useful in organizing, compartmentalizing, and tracking your activity.

To create a new pipeline, follow these steps:

1. Log in to the User Dashboard.
2. Go to the "Pipelines" page.
3. Click "+ Add Pipeline" on the right side of the page.
4. Enter a name for the pipeline, and select "Nimble IP" as the pipeline type in order to use it for proxy requests, then click "Next".
5. Select an Optimization Engine profile. Nimble's AI Optimization Engine will automatically provide IPs that are most suitable to your selected use case.
6. Set your IP Rotation, Sticky session, and geotargeting settings. You can always change any of these settings later, so feel free to leave them as-is for your first pipeline.

That's all! You've created your first pipeline, and you'll be immediately directed to the new Pipeline's overview page. The Pipeline's username, password, server, and port will be displayed at the top of the page.

### Sending Your First Proxy Request

Whether you chose to create a new pipeline or use the default IP pipeline that came from your account, you're now ready to send your first request.

Let’s breakdown a basic cURL request:

<pre class="language-bash" data-overflow="wrap"><code class="lang-bash">curl -x http://<a data-footnote-ref href="#user-content-fn-1">account-accountName-pipeline-pipelineName</a>:<a data-footnote-ref href="#user-content-fn-2">pipelinePassword</a>@<a data-footnote-ref href="#user-content-fn-3">ip.nimbleway.com</a>:<a data-footnote-ref href="#user-content-fn-4">7000</a> https://ipinfo.io
</code></pre>

* **`account-accountName-pipeline-pipelineName`** - the username of an IP pipeline of your choice. You can find the username at the top of the pipeline's overview page.
* **`pipelinePassword`** - the password of an IP pipeline of your choice. You can find the password at the top of the pipeline's overview page.
* **`ip.nimbleway.com`** - Nimble IP Backconnect gateway address.
* **`7000`** Nimble IP port.

That's it! You're now ready to send your first request.

### Next Steps

* [x] **Geolocation Targeting:** Dive deeper into setting up precise geolocation targeting to enhance your data collection accuracy. [Learn More ->](https://docs.nimbleway.com/scraping-infrastructure/backconnect-gateway/country-state-city-geotargeting)
* [x] **Session Management:** Understand how to control and manage sessions effectively for persistent connections. [Explore Sessions ->](https://docs.nimbleway.com/scraping-infrastructure/backconnect-gateway/controlling-ip-rotation)
* [x] **Customize your Pipelines:** Each Pipeline is fully configurable with customized rotation, geolocation, and budget cap settings. [Learn More ->](https://docs.nimbleway.com/management-tools/nimble-dashboard/managing-pipelines)
* [x] **Reporting & Analytics:** Generate custom reports, compare usage over time, and get insight into your activity. [Show me how ->](https://docs.nimbleway.com/management-tools/nimble-dashboard/reporting-and-analytics)




