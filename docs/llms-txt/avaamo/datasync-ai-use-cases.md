# Source: https://docs.avaamo.com/user-guide/datasync-ai/datasync-ai-use-cases.md

# DataSync AI Use cases

## Use Case: Accessing Holiday Calendar Information for Employees from the US Region

### Objective:

To enable employees from the United States (US) region to access specific contract policy information tailored to their area using a content management system.

### Actors:

1. Employee from the India region&#x20;
2. Content manager or administrator

### Prerequisites:

1\. The content management system is set up and operational.

2\. Documents detailing contract policies for various regions, including US and others, are available for ingestion.

### Normal Flow:

#### 1. Create a Document for the US Region Holiday calendar:

&#x20;  \- The content manager creates a document outlining the holiday calendar for employees from the US region.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfGTzJASHH_cwiY0LGiO0AaNt1Vw9JQ6Ra9jmgTk8jdx6pr_xIOH79oZ3yq0N6QAhiLVWszOKhD1Q4ej_unndZ7h8L3JSXogNAAQsVSBu1RuIapllTdKqwpal8RAlN8EuvhpU7-dJ847AgR4mt30QyUt8X2?key=6Lx3HhW7ooq4MQ7MG1Zpvg" alt=""><figcaption></figcaption></figure>

#### 2. Ingest Document for US Region:

&#x20;  \- The content manager uses the content connector to ingest the document into the system.

&#x20;  \- Sets the attribute "**Region**" with the value "**US**" (United States).

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdjh2amP4zdHa5NcibUBS3Mhogf3-fRUHNj9HW71X_V4AAlJFZPgYTkc9-IEIu9j1Rk9Qb7Qd9DqIcSHqguDKlWbTJ48LUCW0b0cSLyNSRGp7NzxZ3J7QXdteSN4xACeObVqFLz6jQ-qDHGbugdfu1FrDGV?key=6Lx3HhW7ooq4MQ7MG1Zpvg" alt=""><figcaption></figcaption></figure>

#### 3. Test Scenario - Accessing via Simulator:

&#x20;  \- The content manager tests the scenario by accessing the agent from a simulator.

&#x20;  \- The simulated user asks, "**May I know about the holiday calendar?**"

&#x20;  \- Since the simulated user is from a non-US region (e.g., India), the system checks for documents related to contract policy for non-US region employees.

&#x20;  \- If no document is found for the non-US region, the system does not provide an answer.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcY_O95FB83RaowNwjLOmf_lte-ZuYC6bEO7HklufOuaxVPtCAuyiO0C-bYq1MUBsLgysSyq-B53LcafdHdKMtPQTbxAVP254kFeuLLkji7Ki0ySnYa9wy8AqhecoQOLy8OVoGSeljBv-uwnGWD7VSB70rg?key=6Lx3HhW7ooq4MQ7MG1Zpvg" alt=""><figcaption></figcaption></figure>

#### 4. Ingest Document for Other Regions (e.g., India):

&#x20;  \- Recognizing the need for regional specificity, the content manager then creates and ingests another document specifically for employees from India.

&#x20;  \- Sets the attribute "**Region**" with the value "**India**."

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXedk9r0J3P6OKGHAuuok4t_qBWMhHkrojFEF4bH3ysuuBGwf-X8yT924No30LwhBFggt4Te7fhO71tOOgveatfrgtQaWdeZc6G9UQkz-rB-Cd5UrXdHoZTIfv1qNj2xjz0VrmZO0rV9I5A4ei6JyNQ58Gyp?key=6Lx3HhW7ooq4MQ7MG1Zpvg" alt=""><figcaption></figcaption></figure>

#### 5. Test Scenario - Accessing Updated Information:

&#x20;  \- The simulated user, now from India, asks the same question about the contract policy.

&#x20;  \- The system retrieves and presents information from the document meant for India region employees, acknowledging the updated ingestion.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdzpkxvhdae4l82cIOQv-kk7ZGtymJ9aVqjRPcpiQYTj3Hviu7LQmYxS004cWZeaK4Nmido0hjC_2W1CUpcRtSS32m5_36WN46nDx6dQroCybb9V2U6NFZON4J_qPwBVy8cL0RwQd2rnvpiCv-IcZyA2zU?key=6Lx3HhW7ooq4MQ7MG1Zpvg" alt=""><figcaption></figcaption></figure>

### Postconditions:

\- Employees from the United States region can access relevant contract policy information tailored to their region.

\- The system dynamically retrieves and presents information based on the user's region attribute, ensuring accurate and contextually relevant responses.

### Exceptional Flow:

\- If documents specific to a user's region are not ingested or available, the system should inform the user that no information is currently accessible for their region's contract policy.

### Business Benefits:

**Efficiency:** Provides targeted information to employees based on their region, reducing ambiguity and ensuring compliance.

**Customization:** Allows for customization and refinement of content attributes, supporting continuous adaptation to meet evolving regional needs.

**Accuracy:** Enhances answer accuracy by delivering region-specific information, improving user satisfaction and operational effectiveness.<br>
