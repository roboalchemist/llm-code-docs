# Source: https://docs.getint.io/support-legal-and-others/platform-releases/getint-version-1.92.md

# Getint Version 1.92

### Release date: October 28, 2025 <a href="#release-date-february-24-2025" id="release-date-february-24-2025"></a>

### Overview <a href="#overview" id="overview"></a>

This update brings faster quick builds, improved requester handling in Freshservice, and key fixes for Jira and GitLab integrations.

#### New Features and Improvements

* **Freshservice Integration**: Improved performance by implementing paginated fetching of requesters. This allows efficient handling of large requester lists (e.g., 5000+ users) and prevents API timeouts during field mapping.
* **Quick Build Optimization**: Reduced processing time for quick builds, resolving 504 Gateway Timeout errors. Both "Match fields" and "Quick build" features now execute reliably within the expected timeout window.

#### **App Changes and Bug Fixes**

* **GitLab**: Enhanced assignee synchronization by supporting multiple assignees per work item. All assigned users are now fetched and synced to a custom text field in Jira, ensuring complete assignment visibility for GitLab Premium users.
* **Jira**: Resolved issues with cascading fields by refining string splitting and field lookup logic. This ensures accurate creation and updating of cascading field values. Also, restored correct behavior for transition screen meta fields in Many to Many project integrations, improving field visibility and mapping accuracy.

#### Contact Us <a href="#contact-us" id="contact-us"></a>

If you have any questions, encounter issues, or need further assistance regarding this release, please feel free to reach out to us:

* **Support Email:** <support@getint.io>
* **Help Center:** <https://getint.io/help-center>

Our team is here to ensure an *effortless* experience for you. Don't hesitate to get in touch!

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
