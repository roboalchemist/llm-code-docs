# Source: https://docs.avaamo.com/user-guide/skills/prompt-skill/functions.md

# Functions

The `Functions` section allows you to define and configure the functions your agent can execute during customer interactions. This feature enables the agent to perform specific tasks dynamically based on user inputs or system triggers.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FnaR6cFsMQxYUMhFN5CLV%2FScreenshot%202025-12-09%20at%202.40.54%E2%80%AFPM.png?alt=media&#x26;token=fcb03aef-0c4c-44c6-b682-cea3ec862558" alt=""><figcaption></figcaption></figure>

### **Key Components**

1. **Function List:**
   * Displays the list of existing functions configured for the agent.
   * Click `Add New` to create a new function.
   * Functions can be deleted using the trash icon.
2. **Name:**
   * Enter a unique name for the function to identify it within the system.
3. **Declaration:**
   * Define the function structure here.
   * This typically includes the function’s name, parameters, and expected behavior.
4. **Definition:**
   * Specifies how the function operates and what output it should generate.
   * Can include logic or conditions for execution.
   * You can also make use of built-in definitions.&#x20;

### **Usage**

* Functions enable the agent to interact with external systems, process data, or execute predefined tasks.
* Well-defined functions enhance automation and improve the efficiency of customer interactions.
* Ensure the function names and instructions are clear to avoid misinterpretation by the model.

After configuring a function, click **Save** to apply changes.

### **Use Case: Enhancing Customer Interaction with Functions in Prompts**

**Scenario: Booking a Doctor's Appointment**

An agent is designed to help users schedule doctor appointments through a conversational interface. To improve automation and efficiency, the assistant needs to integrate with an external appointment scheduling system.

**Prompt:**&#x20;

If the user requests an appointment, call the function `book_appointment` with the provided details. If any detail is missing, ask the user before proceeding.

**Function Definition: `book_appointment`**

The function allows the assistant to process user requests and interact with the scheduling system dynamically.

**Function Declaration:**

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "name": "book_appointment",
  "parameters": {
    "doctor_name": "string",
    "date": "string",
    "time": "string",
    "patient_name": "string"
  },
  "returns": {
    "confirmation_number": "string",
    "status": "string"
  }
}
</code></pre>

**How the Function is Used in a Prompt:**

When a user interacts with the assistant and says:\
\&#xNAN;*"I want to book an appointment with Dr. Smith on April 5 at 10 AM."*

The assistant processes this input and uses the function:

```plaintext
plaintextCopyEditExecuting function: book_appointment
Doctor: Dr. Smith
Date: April 5
Time: 10 AM
Patient: John Doe
```

The function interacts with the external system and returns:

```json
{
  "confirmation_number": "APPT-12345",
  "status": "Confirmed"
}
```

The assistant then responds:\
\&#xNAN;*"Your appointment with Dr. Smith on April 5 at 10 AM is confirmed. Your confirmation number is APPT-12345."*

By using functions in prompts, the assistant enhances customer interactions while ensuring precise and efficient execution of tasks.
