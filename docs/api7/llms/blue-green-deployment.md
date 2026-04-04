# Source: https://docs.api7.ai/enterprise/best-practices/blue-green-deployment.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/best-practices/blue-green-deployment.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/best-practices/blue-green-deployment.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/best-practices/blue-green-deployment.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/best-practices/blue-green-deployment.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/best-practices/blue-green-deployment.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/best-practices/blue-green-deployment.md

# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/blue-green-deployment.md

# Source: https://docs.api7.ai/enterprise/3.7.x/best-practices/blue-green-deployment.md

# Source: https://docs.api7.ai/enterprise/3.6.x/best-practices/blue-green-deployment.md

# Source: https://docs.api7.ai/enterprise/3.5.x/best-practices/blue-green-deployment.md

# Source: https://docs.api7.ai/enterprise/3.4.x/best-practices/blue-green-deployment.md

# Source: https://docs.api7.ai/enterprise/3.3.x/best-practices/blue-green-deployment.md

# Configure Blue-Green Deployment

Blue-green deployment is a strategy that minimizes downtime and risk by using two identical environments: Blue (current live) and Green (new version). Traffic is switched from Blue to Green once the new version is verified, allowing seamless updates. If issues occur, you can quickly revert to Blue, ensuring continuous service with minimal disruption.

Below is an interactive demo that provides a hands-on introduction to blue-green deployment using API7 Enterprise.

## Configure Blue/Green Upstreams[â](#configure-bluegreen-upstreams "Direct link to Configure Blue/Green Upstreams")

1. Select **Published Services** of your gateway group from the side navigation bar, then click the service you want to modify, for example, `httpbin`.

2. Under the published service, select **Upstreams** from the side navigation bar.

3. In the **Default Upstream** module, click **Edit**, rename the upstream to `Blue Upstream`, and click **Save**.

4. In the **Canary Rules** module, click **Start Canary**.

5. In the dialog box, do the following:

   <!-- -->

   * In the **Weight** field, enter `100`.
   * In the **Condition** field, keep the button off.
   * Click **Next**.

6. In the **Canary Upstream** field, choose **Create a new upstream**.

   <!-- -->

   * In the **Upstream Name** field, enter `Green Upstream`.
   * Click **Edit** to adjust the host of the node to point to the new backend. For example, use `172.16.1.82` as the host and `80` as the port.
   * Click **Save**.

7. Click **Start**. The canary rules start working immediately.

## Validate[â](#validate "Direct link to Validate")

Validate the Green Upstream by sending a request:

```
curl "http://127.0.0.1:9080/headers" -v
```

You will receive a `200 OK` response with the header `green`.

## Finish Canary Rules[â](#finish-canary-rules "Direct link to Finish Canary Rules")

1. In the **Canary Rules** field, click **Actions** and **Finish**.

2. In the dialog box, do the following:

   <!-- -->

   * In the **Baseline Upstream** field, choose `Canary Upstream: Green Upstream`.
   * In the **Delete Unselected Upstream: Default Upstream** field, turn off the button.
   * Click **Finish**. The Blue Upstream is a history upstream that you can send traffic to when necessary.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)
  * [Upstreams](https://docs.api7.ai/enterprise/3.3.x/key-concepts/upstreams.md)
