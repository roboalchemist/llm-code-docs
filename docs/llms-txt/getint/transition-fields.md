# Source: https://docs.getint.io/getintio-platform/workflows/transition-fields.md

# Transition Fields

### Correct Usage of Transition Fields in a Jira Integration

When integrating Jira with other applications, it's essential to understand the correct usage of fields to ensure data integrity and seamless workflow transitions. Transition fields in Jira are unique because they cannot be updated directly like other fields. Instead, it must be set during the ticket status transition. This document provides a thorough explanation and step-by-step instructions on properly using these fields in integrations.

#### Why Transition Fields Should Not Be Included in Field Mapping <a href="#why-transition-fields-should-not-be-included-in-field-mapping" id="why-transition-fields-should-not-be-included-in-field-mapping"></a>

1. **Direct Updates Not Allowed:**
   * Transition fields — such as status changes, workflow triggers, or resolution updates — cannot be updated directly like standard fields. Attempting to do so often results in errors, ignored updates, or broken workflows, especially when platform-specific conditions (like required screens or validators) are not met.
2. **Workflow Integrity:**
   * Mapping transition fields as regular fields disrupts the intended workflow logic. These fields are designed to trigger actions, not store static data. Treating them as mappable fields can lead to:
     * Incorrect status changes.
     * Skipped automation rules.
     * Conflicts with validation or post-functions.
3. **Correct Transition Handling:**
   * Transition fields must be handled through the status tab. This ensures:
     * Workflow conditions and validators are respected.
     * Status changes occur in the correct sequence.
     * Related fields (like resolution) are updated consistently.

#### Correct Placement of the Resolution Field in the Integration <a href="#correct-placement-of-the-resolution-field-in-the-integration" id="correct-placement-of-the-resolution-field-in-the-integration"></a>

Instead of including the Resolution field in the **Field Mapping** section, it should be included in the **Status option**. This ensures that the field is updated during the correct status transition of the Jira ticket.

#### How to Set Up Transition Fields in Getint <a href="#how-to-set-up-transition-fields-in-getint" id="how-to-set-up-transition-fields-in-getint"></a>

**Step 1: Access the Status Tab**

* Navigate to your integration settings and open the issue type where you want to add the status transition. Then, switch to the Status tab.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlM5yoilmwZ2cbAy7xqrL%2FOpening%20the%20Status%20Tab.png?alt=media&#x26;token=ef0c5bae-0add-415f-b05e-d50a27b71fae" alt=""><figcaption></figcaption></figure>

**Step 2: Open the Status Configuration**

* Find the status where the transition should take place (i.e., **Done**). Click the gear icon next to it to open its configuration settings.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ft6NVdqbZPOdzwo0iwImC%2FSelect%20the%20status%20option.png?alt=media&#x26;token=b32e4143-1f98-46b0-a98d-c3582ed520c6" alt=""><figcaption></figcaption></figure>

**Step 3: Map the Transition Fields**

* The transition fields tab will appear. Map the transition field (for example, the **Resolution**), and then select the settings icon in the resolution to open the option to match fields to configure the transitions. This ensures that the field will be set during the appropriate status transition of the Jira ticket.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fg9groAUX4G3mrfUp7miC%2Fmapping%20transition%20fields.png?alt=media&#x26;token=70b4a183-33bf-46a3-8610-a219430a1858" alt=""><figcaption></figcaption></figure>

**Step 4: Match the Resolutions**

* Map the options for this field just like you would for any other dropdown field, such as Assignee or Reporter.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fc7mkpfaQNI94KfSoEK6O%2FMapping%20resolution%20options.png?alt=media&#x26;token=34fa0d42-2daf-4904-a49b-c57af2af0938" alt=""><figcaption></figcaption></figure>

**Step 5: Save and Validate the Configuration**

* **Save Settings:**
  * Save the integration settings once all configurations are complete.
* **Validate Integration:**
  * Perform a test to ensure the Resolution field is set correctly during the ticket status transitions. Create a test ticket, transition it through the configured statuses, and verify the Resolution field is updated as expected.

If you require additional assistance, don't hesitate to get in touch with our support team at our [Help Center.](https://getint.io/help-center)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
