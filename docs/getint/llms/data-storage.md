# Source: https://docs.getint.io/getintio-platform/settings/data-storage.md

# Data Storage

#### **A Closer Look at Getint's Data Storage Capabilities**

Managing integration records and logs is a critical part of modern project workflows. As organizations scale, the ability to store, access, and control data becomes essential for efficiency, compliance, and troubleshooting. Getint addresses these needs by offering flexible data storage capacities designed to support diverse business requirements.

This feature is available under the settings page:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9eHKv3k6wCB7lreOQmAV%2FChanging%20the%20logs%20minimum%20level.png?alt=media&#x26;token=9300e5aa-3784-4462-bc11-4123985eca3d" alt=""><figcaption></figcaption></figure>

#### **Navigating the User Interface**

Getint's user interface now includes specific options for streamlined data storage management:

**Enable Logs Storage:**&#x20;

This toggle feature allows users to activate or deactivate log storage and define the log retention duration. By default, logs surpassing this duration are automatically deleted.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaIv2EnWFIFvajFuYuxUH%2FEnable%20logs%20storage.png?alt=media&#x26;token=82d99149-4b8b-4077-b7eb-2ef257405521" alt=""><figcaption></figcaption></figure>

**Logs Retention Period:**

Set the number of days during which the logs will be available. After this time, older logs get deleted automatically.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVpr6qAgvHosXAiKdHr23%2FEnable%20logs%20storage.png?alt=media&#x26;token=fad9eaca-faec-4409-9305-8a89f0aebbfb" alt=""><figcaption></figcaption></figure>

**Logs Minimum Level and Log HTTP Requests:**

These settings ensure that essential details and HTTP requests are trackable for in-depth debugging and troubleshooting.

* **Access the Setting**: Navigate to the "Logs minimum level" dropdown menu in your system settings.
* **Select New Level**: Click on the dropdown, and you'll see two options for the severity level of the logs that can be recorded. These levels typically range from less to more severe as follows:
  * `DEBUG`: Provides detailed information, typically of interest only when diagnosing problems, necessary for support and troubleshooting
  * `INFO`: Confirmation that things are working as expected, basic information about the runs.
* **Choose a Level**: To determine the level of logs you want to be recorded, consider your specific needs. If you want to capture both typical and unexpected events, you might choose the INFO level. On the other hand, if you're only interested in errors and more severe issues, you might want to choose the DEBUG level.
* **Log HTTP Requests:** This option enriches logs with detailed request/response data, giving developers and support teams the visibility they need to quickly diagnose issues, validate fixes, and ensure integrations work as expected.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLNcrFjIj2sK0Qd1RQDaJ%2FEnable%20logs%20storage.png?alt=media&#x26;token=00b16033-c92e-4f80-b000-6a0419dadf67" alt=""><figcaption></figcaption></figure>

**Encryption of Log Files:**

When enabled, information in the logs is protected through encryption. Users can secure sensitive log data through encryption, enhancing the protection against unauthorized data breaches.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCc5pYCasi48QkhieuHTM%2FEnable%20logs%20storage.png?alt=media&#x26;token=20bd5714-f43d-4e6c-a4eb-cc5695e43f10" alt=""><figcaption></figcaption></figure>

After choosing the desired level, make sure to save the changes by clicking the "Save" button located at the bottom of the settings page.

#### **Considerations and Limitations**

**Risk of Losing Important Logs**

While this provides custom retention periods, there's a danger of setting some values too low and subsequently losing critical logs. The user has to make sure in their settings not to land into added complications on future troubleshooting.

**Irretrievability of Older Logs**

After retaining logs over the stipulated period, it is impossible to retrieve the discarded logs. Users have to be very strategic in how to keep their logs, perhaps with routine checks and backup logs to circumvent such restrictions.

#### **Conclusion**

Getint's data storage capabilities provide users with greater flexibility and stronger security in managing their information. By understanding the advantages and limitations of these options and navigating the interface effectively, businesses can optimize their integration processes. With strategic use, Getint users can keep operations efficient, safeguard data, and remain compliant with evolving governance policies.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
