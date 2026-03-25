# Source: https://doc.keepnetlabs.com/next-generation-product/customer-success/multi-language-features/hyper-personalisation.md

# Hyper-Personalisation

The Hyper-Personalisation feature allows you to send phishing simulation scenarios in each recipient’s preferred language. If a preferred language is not set, the system will default to the company's preferred language.

### **Step 1: Setting Up Preferred Languages for Users**

Before launching a campaign with this feature, you must assign preferred languages to users:

1. Navigate to Company > Target Users.
   1. **Manual Upload**: Assign a preferred language to each user via CSV or manually add for each employee
   2. **Sync with Entra ID / AD:** Populate the Preferred Language property in Entra ID and Keepnet will pull this through automatically

### **Step 2: Enabling Preferred Language in a Campaign**

To launch a campaign using this feature:

1. Navigate to **Phishing Simulator > Campaign Manager**.
2. Click the **+ NEW** button to create a new campaign.
3. In the **Hyper-Personalization** section, select:
   * **"Send in the target users’ preferred language"**\
     → The system will send scenarios in each recipient’s preferred language. If no preferred language is set, the company's default language will be used.
4. Click **Next** to proceed through **scenario** **selection**, **target** **groups**, and **delivery settings**.
5. Click **Launch** to start the campaign.

### **Video Tutorial**

{% embed url="<https://www.loom.com/share/cf8a34e7b79f4122bcfa58c56bf369e8?sid=3959ddda-44fe-4116-9cb6-bf7a247aa1a1>" %}

### **How Scenarios Are Assigned Based on Language**

* If a scenario template is available in the user's preferred language, they will receive that version.
* If a scenario template is not available in the user’s preferred language, the system will send the scenario in the **company’s default language**.
* If no scenario template matches either the user's preferred language or the company’s default language, the system will prompt you to select appropriate language versions before launch.

This ensures that users receive scenarios in the most relevant language for them, improving the effectiveness of phishing simulations.
