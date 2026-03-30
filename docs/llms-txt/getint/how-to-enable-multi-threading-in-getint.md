# Source: https://docs.getint.io/getting-started-with-the-platform/deployment-options/on-premise-deployment/how-to-enable-multi-threading-in-getint.md

# How to Enable Multi-Threading in Getint

### Enabling Multi-Threading in Getint

Getint supports a multi-threading configuration, allowing integrations to run in parallel. In an **on-premise deployment**, multiple threads can be assigned per tenant based on a predefined setting.

#### Configuring Multi-Threading for On-Premise Deployments

To enable multi-threading, define a **custom property** specifying the number of threads allocated to each tenant. Follow these steps:

1. Navigate to **Custom Properties** (<https://docs.getint.io/getintio-platform/settings/how-to-override-getint-behavior-using-custom-properties> ).
2. Add a property named SYNC\_THREADS\_NUMBER and set its value to a number greater than 1 (e.g., 3 to create three threads).
3. Restart the Getint service for changes to take effect:

   ```
   ./manager.sh restart 
   ```

#### Verifying Multi-Threading Setup

After restarting, go to **Reporting → Sync Jobs** in the Getint UI. The configured number of integration threads should be visible. For example, if SYNC\_THREADS\_NUMBER=3, the UI should display **Thread #0, Thread #1, and Thread #2**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTENrLBQWpIweJfSDgfVu%2FChecking%20multi-threading%20for%20Onpremise.png?alt=media&#x26;token=f11264b8-166e-4847-b593-c36faec73f78" alt=""><figcaption></figcaption></figure>

#### Assigning Integrations to Threads

By default, all integrations run on **Thread #0**. To distribute integrations across multiple threads:

1. Open the integration details page.
2. Navigate to **Settings**.
3. Specify the **Thread ID** to execute that integration.

For example, if **3 threads** were created, valid Thread IDs are: 0, 1, 2.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6GQMbbRhI5x2tZZIolV7%2FAssigning%20threads%20to%20Integrations.png?alt=media&#x26;token=d66d481a-9ac8-41f6-bb80-47adc4d3c7c1" alt=""><figcaption></figcaption></figure>

#### Managing Thread Reductions

If the number of threads is reduced in the future, integrations assigned to non-existing threads must be manually reassigned. For example:

* If **Thread #4** was previously assigned to an integration but the number of threads is reduced to **3**, then **Thread #4 no longer exists**.
* In such cases, update the integration’s settings to use a valid Thread ID (0, 1, or 2).

#### Conclusion

Setting up multi-threading in your on-premise Getint environment can help improve performance and keep integrations running more efficiently. By adjusting a few settings and defining the number of threads, you can allow multiple jobs to run in parallel and support each tenant's setup.

Just remember to keep an eye on thread assignments if you ever decide to change the number of threads. If integrations are still linked to old thread IDs that no longer exist, they’ll need to be updated to make sure everything keeps running smoothly.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
