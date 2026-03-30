# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/understanding-the-preferred-language-setting.md

# Understanding the Preferred Language Setting

The Keepnet platform allows organizations to configure language preferences at different levels:

## Company’s Preferred Language (Mandatory, Default: English)

* The primary language used for phishing campaigns, training, and system notification emails.
* This field cannot be empty; the default is English.
* The system admin can prioritize listing in this language for phishing templates, scenarios, landing pages, and security training.

## User’s Preferred Language (Optional, for Hyper-Personalization)

* If enabled by the system admin, phishing campaigns and training enrollments will prioritize the user’s preferred language.
* If no preferred language is set or content is unavailable, the platform defaults to the Company’s Preferred Language.

## Example Use Cases for Company’s Preferred Language

### Phishing Simulations

* The platform prioritizes the Company’s Preferred Language unless configured differently.
* **How It Works:**
  * Phishing scenarios, email templates, and landing pages are displayed first in the Company’s Preferred Language.
  * If content is available in multiple languages, the default listing prioritizes the Company’s Preferred Language.
  * Admins can manually override the language selection if needed.
* **Example:**
  * **Company’s Preferred Language:** Spanish
  * **Available Email Templates:** Spanish, English
  * The system defaults to Spanish, with other languages available for selection.

### Security Awareness Training Library

* Training materials like learning paths, posters, and screensavers are prioritized in the Company’s Preferred Language unless configured otherwise.
* **How It Works:**
  * The platform displays training materials in the Company’s Preferred Language.
  * Admins can manually search, filter, and select other languages.
  * Admins can override language selection if needed.
* **Example:**
  * **Company’s Preferred Language:** English
  * **Available Training Modules:** English, Spanish, French
  * The system lists English training first, with manual switching available.

### Sending a Phishing Campaign Based on User’s Preferred Language

When launching a phishing campaign, Keepnet automatically assigns training content based on the following rules:

* If hyper-personalization is **not** enabled, the campaign content is assigned in its original language.
* If hyper-personalization is enabled:
  * The system checks if the User’s Preferred Language is set.
  * If phishing content is available in this language, it is assigned accordingly.
  * If unavailable, the system defaults to the Company’s Preferred Language.
  * If neither is available, the default system language (English) is used.
* **Example:**
  * **Company’s Preferred Language:** Italian
  * **User’s Preferred Language:** Dutch
  * **Phishing Scenarios In:** Italian, French, English
  * Since Dutch phishing content is unavailable, the system assigns Italian.

### Enrolling Training Based on User’s Preferred Language

When enrolling users in training, Keepnet prioritizes the best-matching language based on the following rules:

* If hyper-personalization is **not** enabled, training is assigned in its original language.
* If hyper-personalization is enabled:
  * The platform checks if the User’s Preferred Language is set.
  * If training is available in this language, it is assigned accordingly.
  * If unavailable, the Company’s Preferred Language is used.
  * If neither is available, the default system language is applied.
* **Example:**
  * **Company’s Preferred Language:** English
  * **User’s Preferred Language:** Russian
  * **Training Available In:** English, French
  * Since Russian training is unavailable, the system assigns English.

### How the Platform Handles Language Preferences – Priority Order

The Keepnet platform applies the following priority when assigning phishing campaign training and security awareness enrollments:

1. If hyper-personalization is **not** enabled:
   1. The system assigns the content language as selected by the system admin.
2. If hyper-personalization **is** enabled:
   1. **User’s Preferred Language** (if available)
   2. **Company’s Preferred Language** (if User’s Preferred Language is unavailable)
   3. **Default System Language** (English) (if neither is available)

## FAQs

### Q: Where can I set the Company’s Preferred Language?

A: The System Admin can configure this setting in the platform settings.

### Q: How do I set the User’s Preferred Language?

A: The system admin can update the user’s preferred language in user settings. If left empty, the system defaults to the Company’s Preferred Language.

### Q: What happens if the User’s Preferred Language is not available?

A: The system automatically applies the Company’s Preferred Language. If that is also unavailable, the system defaults to English.

### Q: Can admins manually override the Preferred Language setting?

A: Yes, admins can manually select a different language when configuring phishing campaigns or training enrollments.

### Q: Does this apply to all Keepnet modules?

A: The Preferred Language setting affects: ✅ Phishing Simulator (Scenarios, Emails, Landing Pages) ✅ Phishing Campaign Training Assignment (If hyper-personalization is enabled) ✅ Security Awareness Training Enrollment (If hyper-personalization is enabled)

### Summary of Language Selection Behavior in Keepnet

| Scenario                                              | Company’s Preferred Language (Default: English)    | User’s Preferred Language (Optional, for Personalization) | Fallback to Default System Language (English)    |
| ----------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------ |
| Phishing Simulator (Scenarios, Emails, Landing Pages) | ✅ Applied by Default                               | Not Applicable                                            | ✅ If Company’s Preferred Language is Unavailable |
| Security Awareness Training Library Listing           | ✅ Applied by Default                               | Not Applicable                                            | ✅ If Company’s Preferred Language is Unavailable |
| Phishing Campaign Assignment (Hyper-Personalized)     | ✅ Used if User’s Preferred Language is Unavailable | ✅ Used for Personalized Assignments (if set)              | ✅ If Neither is Available                        |
| Training Enrollment (Hyper-Personalized)              | ✅ Used if User’s Preferred Language is Unavailable | ✅ Used for Personalized Assignments (if set)              | ✅ If Neither is Available                        |
