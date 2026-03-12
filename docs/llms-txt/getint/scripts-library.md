# Source: https://docs.getint.io/getintio-platform/scripts-library.md

# Scripts Library

### Getint Scripts Overview <a href="#getint-scripts-overview" id="getint-scripts-overview"></a>

The scripts library is a repository of user-defined scripts that can be used to modify or enrich data during synchronization. These scripts are written in JavaScript and executed at runtime, allowing for dynamic transformations, conditional logic, and custom field mappings.

By storing scripts in a shared library, they can be written once and used across multiple syncs, reducing setup time, minimizing errors, and allowing users to revert changes if needed. Updates to a script in the library automatically apply to all syncs that reference it, making it easier to manage changes and ensure alignment.

#### How to Use the Scripts Library <a href="#how-to-use-the-scripts-library" id="how-to-use-the-scripts-library"></a>

To access the scripts library, navigate to **Workflows**, then click on the **Scripts Library** section in the Getint dashboard.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLMisdom6YXqH2LW7xEwC%2FWhere%20to%20access%20the%20scripst%20library.png?alt=media&#x26;token=62ae5a43-897f-42b5-a577-5854feb06ed7" alt=""><figcaption></figcaption></figure>

From there, you can:

* Create new scripts using the built-in editor.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FL4xiIBml2meQcKGHRH8Q%2FCreate%20a%20script.png?alt=media&#x26;token=e1ab0d90-482f-470d-9601-7430dc581c9e" alt=""><figcaption></figcaption></figure>

* Disable, edit, or delete scripts as needed.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FC6TEGYYPbmXPDYt3DY3z%2FScripts%20Library.png?alt=media&#x26;token=b12ffbec-7e3c-4b87-a7e6-9ad081721ef7" alt=""><figcaption></figcaption></figure>

* Test scripts before applying them to live syncs.

Each script can be labeled and described for clarity, making it easier to identify its purpose and usage.

#### How to Avoid Creating Duplicate Scripts <a href="#how-to-avoid-creating-duplicate-scripts" id="how-to-avoid-creating-duplicate-scripts"></a>

When working with the scripts library, it’s important to ensure that each function you create is unique. Duplicate functions can cause conflicts and make it harder to maintain your codebase. To avoid this, follow these steps:

* **Create a new script**: Inside the script, define a function. The script's filename is not critical, but the function name is. Always choose a name that hasn’t been used in other scripts to prevent duplication.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMvh7CGlWzQvxaqlPDLw0%2FExample%20function%20name.png?alt=media&#x26;token=e8ed8814-7d3f-479b-b79f-50c9397ae365" alt=""><figcaption></figcaption></figure>

* **Save and verify**: After saving the script, check the list of scripts. You should see your function name displayed in the second column, which helps confirm that it's distinct and properly registered.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDTtU3QH1yj3xqVMdKnJH%2FHow%20to%20check%20the%20function%20name%20after%20creation.png?alt=media&#x26;token=85841b9f-523e-4a7d-b702-ed7d30870f04" alt=""><figcaption></figcaption></figure>

* **Use the function consistently**: After saving, the script is enabled for use. Call it from any hook using `utils.{nameOfFunction}()`.
* **Amend functions when needed**: If anything needs to change inside the function, simply update it directly within the script.
* **Handle special cases in hooks**: For scenarios where you need to do specific things beyond invoking the function, manage those directly in the relevant hooks.

#### Best Practices <a href="#best-practices" id="best-practices"></a>

* Keep scripts modular and focused on specific tasks.
* Use clear naming conventions to improve readability.
* Test scripts thoroughly before deployment.
* Regularly review and clean up unused or outdated scripts.
* Review the logs if the scripts are failing.

#### Support <a href="#support" id="support"></a>

If you have any questions about the scripts library or need assistance with your integration setup, our team is here to help. Whether you're troubleshooting a specific issue or looking for guidance on best practices, feel free to reach out.

You can contact us through the following channels:

* **Email**: <support@getint.io>.
* **Live Chat**: Available directly within the Getint dashboard.
* **Help Center**: Visit our [Help Center](https://getintio.atlassian.net/servicedesk/customer/portals) to open a support ticket, and [Docs](https://docs.getint.io/) for detailed articles and FAQs.

We aim to respond promptly and ensure you have the support you need to make the most of your Getint experience.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTYNTk9Bg1Oswglnttfwz%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=6516710b-7309-4c9c-b4dc-5fc46980e37f" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
