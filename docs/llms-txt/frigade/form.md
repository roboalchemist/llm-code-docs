# Source: https://docs.frigade.com/component/form.md

# Form

> Collect user information via forms in modals or embedded in your UI

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/forms-modal.png" style={{ width: "350px" }} />
</Frame>

## About this component

The `Form` component is a super versatile tool that can fit right into your product UI or pop up in a modal for things like surveys. They can be used for wide range of use cases including registration flows, surveys, feedback forms, and more. The component supports form validation (client and server-side), conditional fields, branching logic, and multi-step Flows.

**When to Use Forms:**

* **Embedded in UI:** Forms work great for tasks like product registration, helping users get started smoothly without leaving the page.
* **Modal Surveys:** Use forms in modals for surveys or feedback, making it easy for users to share their thoughts without disrupting their experience.

**Why Forms Are Powerful:**

* **Conditional and Branching Logic:** Forms can adapt based on user responses, guiding them through a tailored experience that feels intuitive.
* **Custom React Steps:** You can embed custom React components to invite teammates or perform API lookups, adding a personal touch to your forms.
* **Customizable Input Types:** With a variety of built-in input types—like text fields, multiple-choice options, and dropdowns—you can design forms that suit your specific needs.

**Best Practices for Forms:**

* **Provide Progress Indicators:** Adding progress bars or step indicators (like "Step X of Y") can help users see how far they've come and what's left to do. This makes the process feel less daunting and more manageable.
* **Streamlined Data Collection:** Frigade makes it easy to create new forms quickly, allowing you to gather user data and send it wherever you need it in your system.

## Resources

* Create a form and [send events to Slack](/guides/form-video-demo)
* Launch pop-up forms and surveys with no-code using [Collections](/platform/collections#announcements-surveys-and-dialogs)
* Target your form to specific users with [Targeting](/platform/targeting)
* See [industry examples](https://www.productonboarding.com/?type=form) of forms

## Demo

* See forms in action in our [live demo](https://demo.frigade.com/forms)

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## Examples

The following section includes ready-made examples and code for various form use cases.

### Simple Modal Form

<Tabs>
  <Tab title="Component">
    <Frame>
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/components/forms/simple-modal.png" style={{ width: "350px" }} />
    </Frame>
  </Tab>

  <Tab title="Configuration and Code">
    <CodeGroup>
      ```Typescript App.tsx
      import * as Frigade from '@frigade/react';

      const App = () => {
      return (

      <Frigade.Form
        flowId="my-flow-id"
        // Remove the line below to render the Form inline
        as={Frigade.Dialog}
        dismissible
      />
      ) }

      ```

      ```yaml Configuration
      steps:
        - id: waitlist-page
          title: Join the waitlist
          subtitle: Get pumped! We are launching soon.
          primaryButton:
            title: Join the waitlist
          fields:
            - id: company-size
              type: radio
              label: Company size
              options:
                - label: 1-10
                  value: 1-10
                - label: 20-100
                  value: 20-100
                - label: 100+
                  value: 100
            - id: industry
              type: select
              label: Industry
              options:
                - label: Icecream making
                  value: icecream
                - label: Guitar riffing
                  value: guitar-riffing
            - id: name
              type: text
              label: Your name
              placeholder: John Doe
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Churn Survey

<Tabs>
  <Tab title="Component">
    <Frame>
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/components/forms/churn-survey.png" style={{ width: "350px" }} />
    </Frame>
  </Tab>

  <Tab title="Configuration and Code">
    <CodeGroup>
      ```Typescript App.tsx
      import * as Frigade from '@frigade/react';

      const App = () => {
      return (

      <Frigade.Form flowId="my-flow-id" as={Frigade.Dialog} dismissible />) }

      ```

      ```yaml Configuration
      steps:
        - id: collect-intend
          title: We are sorry to see you go
          subtitle: We are sorry to see you go. Please help us improve by answering a few questions.
          primaryButton:
            title: Cancel my plan
          fields:
            - id: rating
              type: select
              multiple: true
              label: Why would you like to cancel your plan?
              options:
                - label: Too expensive
                  value: too-expensive
                - label: Not enough features
                  value: not-enough-features
                - label: Found a better alternative
                  value: better-alternative
                - label: Too many bugs
                  value: too-many-bugs
                - label: Other
                  value: other
            - id: feedback
              type: textarea
              label: What can we do better?
              placeholder: Your feedback here
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Dynamic Fields

<Tabs>
  <Tab title="Component">
    <Frame>
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/components/forms/dynamic-fields.png" style={{ width: "350px" }} />
    </Frame>

    Sometimes you may want to conditionally render a dynamic field based on the value of another field. The example above dynamically changes the second dropdown based on the value of the first dropdown.
  </Tab>

  <Tab title="Configuration and Code">
    This component requires a custom form field for dynamically changing the input. You can achieve this by using the `formContext` provided by react-hook-forms.
    In this case, we define a [custom field](/component/form#custom-field-types) type called `DynamicFollowUpBasedOnField` that renders a `SelectField` component.
    The options of the `follow-up` dropdown depends on the value of `food`. If the user selects `pizza`, the `follow-up` dropdown will show options for pizza toppings. If the user selects `pasta`, the `follow-up` dropdown will show options for pasta sauces.

    <CodeGroup>
      ```Typescript App.tsx
      import { Form, type FormFieldProps, SelectField } from "@frigade/react";

      const App = () => {
      return (

      <Form
      flowId="my-flow-id"
      fieldTypes={{
      DynamicFollowUpBasedOnField: (props: FormFieldProps) => {
      const categoryValue = props.formContext.watch("food");
      const field = props.fieldData.props.mappings[categoryValue];

                if (!field) {
                  return null;
                }

                return (
                  <SelectField
                    {...props}
                    fieldData={{
                      ...props.fieldData,
                      ...field,
                    }}
                  />
                );
              },
            }}
          />

      )
      }

      ```

      ```yaml Configuration
      steps:
        - id: collect-intend
          title: Tell us about your favorites
          subtitle: Help us understand your preferences and taste.
          fields:
            - id: food
              label: What is your favorite food?
              type: select
              required: true
              options:
                - value: pizza
                  label: Pizza
                - value: pasta
                  label: Pasta
            - id: follow-up
              type: DynamicFollowUpBasedOnField
              required: true
              props:
                mappings:
                  pizza:
                    label: What is your favorite topping?
                    required: true
                    options:
                      - value: pepperoni
                        label: Pepperoni
                      - value: mushrooms
                        label: Mushrooms
                  pasta:
                    label: What is your favorite sauce?
                    required: true
                    options:
                      - value: tomato
                        label: Tomato
                      - value: alfredo
                        label: Alfredo
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Branching Forms

<Tabs>
  <Tab title="Component">
    <Frame>
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/components/forms/branching.png" style={{ width: "350px" }} />
    </Frame>

    This example shows how to implement branching in a form based on the user's choice in the first step.
  </Tab>

  <Tab title="Configuration and Code">
    If you want a form to conditionally skip a step based on the result of a previous step, you can use the `visibilityCriteria` property in the step configuration.
    For instance, the example below will jump directly to page 3 if the user picks a specific option on the first page/step:

    <CodeGroup>
      ```Typescript App.tsx
      import * as Frigade from '@frigade/react';

      const App = () => {
      return (

      <Frigade.Form flowId="my-flow-id" as={Frigade.Dialog} dismissible />
      ); }

      ```

      ```yaml Configuration
      steps:
        - id: page-1
          title: This is page 1
          primaryButtonTitle: Next
          fields:
            - id: test-radio-1
              type: radio
              label: Which page do you want to go to?
              options:
                - label: Go to page 3
                  value: x
                - label: Continue to page 2
                  value: y
        - id: page-2
          title: This is page 2
          primaryButtonTitle: Next
          # Replace the flow ID below with your own
          visibilityCriteria: user.flowStepData("my-flow-id", "page-1", "test-radio-1") != "x"
          fields:
            - id: test-text
              type: text
              label: Text field
        - id: page-3
          title: This is page 3
          primaryButtonTitle: Finish
          fields:
            - id: test-radio-3
              type: radio
              label: Radio group
              options:
                - label: Radio 1
                  value: 1
                - label: Radio 2
                  value: 2
                - label: Radio 3
                  value: 3
      ```
    </CodeGroup>

    `visibilityCriteria` will work with both form data or any other [Targeting](/platform/targeting#examples) condition.
  </Tab>
</Tabs>

## Supported Field Types

The component supports the following builtin field types that correspond to their respective HTML input types:

* `select`

* `radio`

* `text`

* `textarea`

* `checkbox`

### Overriding Field Attributes

You can override or add any attribute for a field by using the `props` property in the field configuration.
For instance, this is useful if you want to use the `text` field type, but override the `type` to `email` or `tel`. It can also be used to add any attribute such as a css class, data, or styling.

```yaml
steps:
  - id: step-1
    title: This is page 1
    fields:
      - id: email
        type: text
        props:
          type: email
          className: "my-custom-class"
          data-attr: "my-custom-data-attr"
          style:
            color: "red"
```

### Custom Field Types

The Form SDK is built on top of [react-hook-form](https://react-hook-form.com/), which means you can use the majority of its features in your forms. You can define your own custom field types using the `fieldTypes` [prop](#fieldtypes).
For instance, you can implement a simple calendar datepicker field type as such:

```tsx
import { FormFieldProps } from "@frigade/react";
import * as Frigade from "@frigade/react";

function CalendarField({ field, submit }: FormFieldProps) {
  return (
    <div>
      <input type="date" onChange={field.onChange} value={field.value} />
    </div>
  );
}

// ...

<Frigade.Form flowId="my-flow-id" fieldTypes={{ calendar: CalendarField }} />;
```

It is also possible to conditionally render a field based on the value of another field by using the [formContext](https://react-hook-form.com/docs/useformcontext) provided by react-hook-form.
For instance, if you want a custom field called `company-size` to show up when a user selects `company` in the `customer-type` field:

```tsx
import { type FormFieldProps, SelectField } from "@frigade/react";
import * as Frigade from "@frigade/react";

<Frigade.Form
  flowId="myflowid"
  fieldTypes={{
    "company-size": (props: FormFieldProps) => {
      const customerTypeValue = props.formContext.watch("customer-type");

      if (customerTypeValue !== "company") {
        return null;
      }

      return <div>My custom conditional field</div>;
    },
  }}
/>;
```

## Form Validation

The component supports client-side and server-side validation out of the box. You can define validation rules for each field in the form configuration using the `pattern` property with a regular expression. The example below shows how to validate an email field:

```yaml
steps:
  - id: collect-intend
    fields:
      - id: email
        type: text
        required: true
        pattern:
          message: Please provide a valid email
          value: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

### Server-side Validation

You can perform server-side validation by returning a Promise from the `onPrimary` event handler. If the promise resolves to `false`, the current step in the form will not be marked as completed. The `onPrimary` event handler also contains all form data collected in the session, which allows you to send the data to your server for validation or storage.

```tsx
import { StepHandlerProp } from "@frigade/react";
import * as Frigade from "@frigade/react";

const App = () => {
  const handlePrimary: StepHandlerProp = async (step, event, properties) => {
    const response = await fetch("https://my-server.com/validate", {
      method: "POST",
      body: JSON.stringify(properties),
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (response.ok) {
      return true;
    }

    // The current step in the form will be marked as completed
    return false;
  };

  return <Frigade.Form flowId="my-flow-id" onPrimary={handlePrimary} />;
};
```

## Browser Navigation

You can implement browser navigation (back/forward) with your Frigade forms using the [useFlow](/sdk/hooks/flow) hook. This allows users to navigate through form steps using their browser's back and forward buttons.

Here's an example of how to implement this:

```jsx
import { useFlow } from '@frigade/react';
import { useEffect, useRef } from 'react';

export function FormWithBrowserNavigation() {
  const flowId = 'your-flow-id';
  const { flow } = useFlow(flowId);
  const flowRef = useRef(flow);

  // Update ref when flow changes
  useEffect(() => {
    flowRef.current = flow;
  }, [flow]);

  useEffect(() => {
    if (!flowRef.current) return;

    // Handle browser navigation events
    const handlePopState = () => {
      const currentStepIndex = flowRef.current.getCurrentStepIndex();
      const newStepIndex = parseInt(window.location.hash.replace('#step-', '')) || 0;
      
      if (newStepIndex < currentStepIndex) {
        // User clicked back - go to previous step
        flowRef.current.back();
      } else if (newStepIndex > currentStepIndex) {
        // User clicked forward - go to next step
        flowRef.current.forward();
      }
    };

    // Add event listener for browser navigation
    window.addEventListener('popstate', handlePopState);

    // Cleanup
    return () => {
      window.removeEventListener('popstate', handlePopState);
    };
  }, []); 

  return (
    <Frigade.Form 
      flowId={flowId}
    />
  );
}
```

This example:

1. Uses the `useFlow` hook to get access to the flow instance
2. Uses a ref to store the flow instance and prevent re-renders
3. Sets up an event listener for browser navigation (`popstate`)
4. Handles browser back/forward navigation by moving to the appropriate step using `flow.back()` or `flow.forward()`
5. Cleans up the event listener when the component unmounts

When users click the browser's back button, they'll be taken to the previous step in the form. Similarly, clicking forward will take them to the next step.

## Prefilling a form

Forms can be prefilled by using [Dynamic Variables](/platform/dynamic-variables) by linking the `value` of a `field` to the `variables` prop of the Form component. The example below shows how to prefill a form with the user's name:

<CodeGroup>
  ```Typescript App.tsx
  import * as Frigade from '@frigade/react';

  const App = () => {
  return (

  <Frigade.Form
  flowId="my-flow-id"
  variables={{
    name: "John Doe",
  }}
  />
  ) }

  ```

  ```yaml Configuration
  steps:
    - id: collect-intend
      fields:
        - id: name
          type: text
          label: Your name
          value: ${name}
  ```
</CodeGroup>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties

<Tabs>
  <Tab title="React Props">
    <ParamField body="as" type="ElementType<any, keyof IntrinsicElements>">
      Optional component to wrap the child components in, e.g. `as={Dialog}` will render the Flow in a modal Dialog. Defaults to `Box`.
    </ParamField>

    <ParamField body="autoStart" type="boolean">
      Whether to automatically mark the Flow started (i.e. in progress) when the Flow is eligible to be shown.
      You will need to call `flow.start()` or `step.start()` from the parent component if you set this to `false`. Most components should not need to override this behavior.

      Defaults to `true`.
    </ParamField>

    <ParamField body="css" type="Interpolation<Theme>">
      Emotion CSS prop to apply to the component. See [Theming documentation](https://docs.frigade.com/v2/sdk/styling/css-overrides) for more information.

      Example usage:

      ```
      <Frigade.Checklist css={{ backgroundColor: "pink", ".fr-button-primary": { backgroundColor: "fuchsia" } }} />
      ```
    </ParamField>

    <ParamField body="dismissible" type="boolean">
      Whether the Flow is dismissible or not
    </ParamField>

    <ParamField body="fieldTypes" type="FieldTypes">
      Custom field types to be used in the Form.
      You can use this to build your own custom form fields in a `Form`.

      For example, if you want to use a custom field type called `calendar`:

      ```tsx
      import { Form, FormFieldProps } from '@frigade/react'

      function CalendarField({ field, submit }: FormFieldProps) {
        return (
         <div>
           <input type="date" onChange={field.onChange} value={field.value} />
         </div>
        )
      }

       // ...

       <Form flowId="my-flow-id" fieldTypes={{ calendar: CalendarField }} />

      ```
    </ParamField>

    <ParamField body="flowId" type="string">
      The Flow ID to render. You can find the Flow ID in the Frigade dashboard.
    </ParamField>

    <ParamField body="forceMount" type="boolean">
      If true, the Flow will be mounted even if it has already been completed or dismissed.
      However, if the user does not match the Flow's targeting, the Flow will not be mounted.
    </ParamField>

    <ParamField body="modal" type="boolean">
      Register the Flow as a modal to prevent popup collisions (only one modal Flow will render at a time).
    </ParamField>

    <ParamField body="onComplete" type="FlowHandlerProp">
      Handler for when the Flow is completed. This is event is fired immediately after the user completes the Flow.
    </ParamField>

    <ParamField body="onDismiss" type="FlowHandlerProp">
      Handler for when the Flow is dismissed (skipped). This is event is fired immediately after the user dismisses the Flow.
    </ParamField>

    <ParamField body="onPrimary" type="StepHandlerProp">
      Handler for when primary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="onSecondary" type="StepHandlerProp">
      Handler for when secondary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="variables" type="Record<string, unknown>">
      Variables to pass to the Flow. You can use variables in the Flow configuration to customize copy.
      For instance, you can use `title: Hello, ${name}!` in the Flow configuration and pass `variables={{name: 'John'}}` to customize the copy.
    </ParamField>
  </Tab>

  <Tab title="Flow Configuration (Advanced Editor)">
    <ParamField body="steps" type="array">
      The individual steps/pages of the form
    </ParamField>

    <ParamField body="steps[].id" type="string">
      Unique identifier for the step. Do not change this once the step has been created.
    </ParamField>

    <ParamField body="steps[].title" type="string">
      The title of the step
    </ParamField>

    <ParamField body="steps[].subtitle" type="string">
      The description of the step
    </ParamField>

    <ParamField body="steps[].imageUri" type="string">
      Url to an image to display in the step
    </ParamField>

    <ParamField body="steps[].iconUri" type="string">
      Url to an icon to display in the step. This is only supported by the carousel checklist component.
    </ParamField>

    <ParamField body="steps[].videoUri" type="string">
      Url to a video to display in the step such as YouTube, Vimeo, or a direct link to an mp4 file
    </ParamField>

    <ParamField body="steps[].primaryButton" type="object">
      Config for the primary button in this step.
    </ParamField>

    <ParamField body="steps[].primaryButton.action" type="boolean,string">
      Primary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].primaryButton.target" type="string">
      Primary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].primaryButton.title" type="string">
      Primary button title. If omitted, the primary button will not be shown.
    </ParamField>

    <ParamField body="steps[].primaryButton.uri" type="string">
      Primary button URI.
    </ParamField>

    <ParamField body="steps[].primaryButtonTitle" type="string">
      **Deprecated**: use `primaryButton.title` instead. The title of the primary button
    </ParamField>

    <ParamField body="steps[].primaryButtonUri" type="string">
      **Deprecated**: use `primaryButton.uri` instead. The url to open when the primary button is clicked
    </ParamField>

    <ParamField body="steps[].primaryButtonUriTarget" type="string">
      **Deprecated**: use `primaryButton.target` instead. The target of the primary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].secondaryButton" type="object">
      Config for the secondary button in this step.
    </ParamField>

    <ParamField body="steps[].secondaryButton.action" type="boolean,string">
      Secondary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].secondaryButton.target" type="string">
      Secondary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].secondaryButton.title" type="string">
      Secondary button title. If omitted, the secondary button will not be shown.
    </ParamField>

    <ParamField body="steps[].secondaryButton.uri" type="string">
      Secondary button URI.
    </ParamField>

    <ParamField body="steps[].secondaryButtonTitle" type="string">
      **Deprecated**: use `secondaryButton.title` instead. The title of the secondary button
    </ParamField>

    <ParamField body="steps[].secondaryButtonUri" type="string">
      **Deprecated**: use `secondaryButton.uri` instead. The url to open when the secondary button is clicked
    </ParamField>

    <ParamField body="steps[].secondaryButtonUriTarget" type="string">
      **Deprecated**: use `secondaryButton.target` instead. The target of the secondary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].completionCriteria" type="string">
      Targeting that automatically completes the step. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].startCriteria" type="string">
      Targeting that automatically blocks the step from starting until it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].visibilityCriteria" type="string">
      Targeting that automatically shows the step when it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].props" type="object">
      Override the default UI props for the corresponding component
    </ParamField>

    <ParamField body="steps[].fields" type="array">
      The data contained on the form step, typically text input boxes, multiple choice questions, etc.
    </ParamField>

    <ParamField body="steps[].fields[].id" type="string">
      Unique identifier for the step. Do not change this once the step has been created.
    </ParamField>

    <ParamField body="steps[].fields[].label" type="string">
      The label of the field
    </ParamField>

    <ParamField body="steps[].fields[].value" type="string">
      The default value of the field (used for prefilling). For checkboxes, use 'true' or 'false'.
    </ParamField>

    <ParamField body="steps[].fields[].multiple" type="boolean">
      Whether the field can accept multiple values. Only used for the `select` type field.
    </ParamField>

    <ParamField body="steps[].fields[].type" type="string">
      The type of the field. The built-in supported types are: `text`, `textarea`, `select`, `checkbox`, and `radio`. If you are using custom form field types, the name here should match it.
    </ParamField>

    <ParamField body="steps[].fields[].placeholder" type="string">
      The placeholder of the field
    </ParamField>

    <ParamField body="steps[].fields[].maxLength" type="integer">
      The maximum length of the field
    </ParamField>

    <ParamField body="steps[].fields[].required" type="any">
      Whether the field is required or not. Use a string here to show a custom error message.
    </ParamField>

    <ParamField body="steps[].fields[].options" type="array">
      The options for the field. Only used for select fields.
    </ParamField>

    <ParamField body="steps[].fields[].options[].label" type="string">
      The label of the option
    </ParamField>

    <ParamField body="steps[].fields[].options[].value" type="any">
      The value of the option
    </ParamField>

    <ParamField body="steps[].fields[].pattern" type="object">
      The validation rules for the field. See documentation for more information.
    </ParamField>

    <ParamField body="steps[].fields[].pattern.value" type="string">
      Regex pattern to match the field against
    </ParamField>

    <ParamField body="steps[].fields[].pattern.message" type="string">
      The error message to display if the pattern does not match
    </ParamField>

    <ParamField body="steps[].fields[].props" type="object">
      Optional additional properties for the field. These will be passed to the frontend component as HTML attributes and merged with the default props for the given field type.
    </ParamField>
  </Tab>
</Tabs>

```
```
