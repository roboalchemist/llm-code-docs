# Source: https://docs.getint.io/getintio-platform/hiding-work-items-from-users-with-security-schemes-automation.md

# Hiding Work Items from Users with Security Schemes Automation

### Use Case: <a href="#use-case" id="use-case"></a>

When working on Jira projects where multiple outside of the company users have access to them, such as customer-facing projects, you may want to limit the visibility of these users to some work items (i.e., limit companies to only visualize work items related to them).\
In this scenario, you can build an automation within Jira that, once a specific trigger is met, will hide the work items of the project from certain users, or simply only display the work items that are related to these users.

### 1. Creating your Security Scheme <a href="#id-1.-creating-your-security-scheme" id="id-1.-creating-your-security-scheme"></a>

* Click the Settings/Gear Icon at the right upper corner, and click on "Work Items."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FZFXmGdnNa4kbO4dA0Mui%2FAccessing%20the%20work%20Items.png?alt=media&#x26;token=80b0086a-73fa-4215-baa4-cca03a457743" alt=""><figcaption></figcaption></figure>

* Under "Work Item Attributes," select "Work item security schemes."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4r6vpOOSxCKhuksRc6Ed%2FWork%20item%20attributes.png?alt=media&#x26;token=8319bc3c-b9d4-4b45-9e4e-4712b51ed91a" alt=""><figcaption></figcaption></figure>

* Click "Add work item security scheme."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPPNo8F2PvbNtw2x5zCYl%2FSecurity%20scheme%20from%20Work%20Items.png?alt=media&#x26;token=17c8e329-1532-4115-9193-df911a6b15bd" alt=""><figcaption></figcaption></figure>

* Add a name to your new security scheme, and feel free to add a description to it, then click "Add."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F5ZloHewelYjX1r6d0y2i%2Fadd%20a%20work%20item%20security%20scheme.png?alt=media&#x26;token=f4d88be4-29c4-4240-a40f-723f3461c3c2" alt=""><figcaption></figcaption></figure>

### 2. Setting Up the Security Levels <a href="#id-2.-setting-up-the-security-levels" id="id-2.-setting-up-the-security-levels"></a>

* After creating your new security scheme, click "Security Levels."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxMlX7mcv7phHVeXRm09W%2FLooking%20for%20the%20new%20security%20scheme.png?alt=media&#x26;token=e1977ef9-fa41-431e-af58-52ff5e62e4ee" alt=""><figcaption></figcaption></figure>

* Each security level can be configured so that users within it can only visualize the work items related to them. Add a name for that security level, a description, and click "Add security level."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fb9FwPPSzNxc8p8ofgNxO%2FEdit%20work%20item%20security%20level.png?alt=media&#x26;token=5b83dca3-1000-4bed-b9c0-dee6da058485" alt=""><figcaption></figcaption></figure>

* After creating your new security level, you can add users or groups of users to it, then click add to start adding users to that security level.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIsUaWalcyx272RIaqwpm%2FAdd%20users%20or%20groups%20to%20the%20security%20level.png?alt=media&#x26;token=d54040c9-5174-41d5-a641-5bf21ac19065" alt=""><figcaption></figcaption></figure>

* From this screen, you can define how you’d like to add users to this security level. In this example, we will be adding a single user who was recently invited to the organization. However, you can also bulk-add users based on their roles, groups, or utilize a custom field to define which users should be added. Click "Add" to finish editing.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOaTopPyHlUTUOB28hDLj%2FDefine%20how%20would%20you%20add%20those%20users.png?alt=media&#x26;token=0705c7c1-ce71-4e1a-812c-d0ddf45637b0" alt=""><figcaption></figcaption></figure>

* You can then see the users added to this security level. You can remove previously added users, and/or add more users to it if you need to.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBZ7O63RO3KEYGiRtxTuC%2FSee%20security%20levels%20added%20for%20the%20users.png?alt=media&#x26;token=966ab646-62e1-416f-bbe8-d01ba4e47d09" alt=""><figcaption></figcaption></figure>

### 3. Enable Security Schemes for Your Company Managed Project <a href="#id-3.-enable-security-schemes-for-your-company-managed-project" id="id-3.-enable-security-schemes-for-your-company-managed-project"></a>

Be aware that only **Company Managed Projects** can utilize Security Schemes. If you are using a different type of project (such as Team Managed), you may need to migrate the work items to the proper type of project.

* Go to your Project settings:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXtqaqZtP8U2XqcRGFaSa%2Fgoing%20to%20your%20project%20settings.png?alt=media&#x26;token=2e69d744-6174-4e88-9da6-d3fc1a0b56f4" alt=""><figcaption></figcaption></figure>

* Under Work Items, click "Security."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEFWIL2gF4kDZfE74X9Nq%2FSelect%20security%20under%20work%20items.png?alt=media&#x26;token=f8e64287-fc1b-4a8c-b309-fd8dc50a86b1" alt=""><figcaption></figcaption></figure>

* Click "Actions," and then click "Select a scheme."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQcMzT4tuWCe7d9TyVnYZ%2FSelect%20a%20Scheme.png?alt=media&#x26;token=f3e19a8a-8b39-41e3-8170-f1495d53ea6c" alt=""><figcaption></figcaption></figure>

* Select the created scheme for your project, and click "Next."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FiQ2RPMqcNGbcyUwKtVXU%2Fselect%20the%20created%20scheme%20and%20click%20next.png?alt=media&#x26;token=3acf995e-d44c-4b24-b308-cb82af082ca7" alt=""><figcaption></figcaption></figure>

* Click "Associate."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdqdWRUqYNQYdLC9ExiJ8%2Fclick%20associate%20to%20pair%20a%20security%20scheme%20to%20a%20project.png?alt=media&#x26;token=0b509228-8a05-4f7c-9639-02baa2fa51cd" alt=""><figcaption></figcaption></figure>

* The security scheme is now set for your project.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUdcZgXpvrtHrlmuan7y9%2Fsecurity%20scheme%20is%20now%20set%20for%20your%20project.png?alt=media&#x26;token=f4195087-70e0-4e10-a458-8551a874bd4c" alt=""><figcaption></figcaption></figure>

### 4. Set Up the Automations <a href="#id-4.-set-up-the-automations" id="id-4.-set-up-the-automations"></a>

You can now set an automation to define when a work item should be available for a specific user or group of users, based on a trigger.

* Create an automation from scratch, and the first operator can be "When: Work item created." Meaning we would like to trigger the automation as soon as the item is created.
* The second operator would be "IF: Company name contains Company X." This means the automation should kick in when a work item is created, and the field "Company name" has a string value "Company X."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0NLqNn3huLMP1AsVTDC5%2FSetting%20up%20conditions.png?alt=media&#x26;token=fda1ffd3-5019-424b-9c84-ecc6745d2048" alt=""><figcaption></figcaption></figure>

* The third operator should be "THEN: Set work item security level." As a result, we will be changing the security level of that work item to the desired security level, as long as it has the field "Company name" with the value "Company X."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F3AyEcrpoXhOlix2h9EHn%2Fset%20work%20item%20security%20level.png?alt=media&#x26;token=7439f0e2-73d9-4b00-b29a-086d2f319f94" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVlai7MJUSSVfniRRQ9jt%2Fselect%20the%20work%20item%20security%20level.png?alt=media&#x26;token=055764af-4924-4b73-8dff-a1018cbbdb98" alt=""><figcaption></figcaption></figure>

* This is how our rule looks. We can then turn it on for it to take effect.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxY2S8BKN5PWCXrcJe20I%2FTurn%20on%20the%20rule.png?alt=media&#x26;token=99db2375-c45e-4fe3-a415-d9bf103e8206" alt=""><figcaption></figcaption></figure>

### 5. Test your New Automation to Validate its Functionality <a href="#id-5.-test-your-new-automation-to-validate-its-functionality" id="id-5.-test-your-new-automation-to-validate-its-functionality"></a>

We can now test the automation to verify if it’s working as expected. Please be aware that you might have to build multiple automations or edit your existing automation to cover all the possible scenarios when dealing with multiple companies or users within a single project.

If you require additional assistance, don't hesitate to get in touch with our support team at our [Help Center.](https://getint.io/help-center)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
