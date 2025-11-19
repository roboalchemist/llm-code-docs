# Source: https://docs.frigade.com/component/survey/nps.md

# NPS Survey

> Collect structured and freeform feedback from your users

<Frame className="h-96 items-center px-4">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/components/nps.svg" />
</Frame>

## About this component

The `Survey` component is a fantastic way to engage users right when it matters and gather valuable feedback or data. Whether you’re looking to measure satisfaction or collect insights, targeted in-app surveys can help you connect with users at key moments in their journey.

**When to Use Surveys:**

* **User Research:** Deploy surveys like NPS (Net Promoter Score) right after users complete specific actions. This is a great way to capture their feelings while the experience is fresh in their minds.
* **Data Collection:** Use surveys to collect additional data after user signups, helping you enrich your CRM and tailor your communications.

**Best Practices for Surveys:**

* **Flexible Display Options:** By default, NPS surveys typically float on the screen, ensuring they don’t take over the entire user experience. This keeps the process smooth and non-intrusive.
* **Full-Screen Takeovers:** For the highest engagement rates, for custom surveys or other input forms, they can be displayed inline within the page or as a full page modal. Just be sure to use these methods thoughtfully to avoid annoying users.

**Custom Surveys:**

* **Built on Forms:** Custom surveys utilize the same underlying components as Forms, which means you can refer to the Forms documentation for more details on how to create and implement them effectively.

## Resources

* Launch surveys with no-code using [Collections](/platform/collections#announcements-surveys-and-dialogs)
* Target your survey to specific users with [Targeting](/platform/targeting)
* See [industry examples](https://www.productonboarding.com/?type=survey) of surveys

## Demo

* See surveys in action in our [live demo](https://demo.frigade.com/modals)

## Alternative scales

The component comes with a default NPS scale of 0-10. You can also use a custom scale by passing the `options` property either directly in the React component or in the YAML config via the `props` property. For instance, in the example below, we're using an emoji scale:

<Tabs>
  <Tab title="Emoji Survey">
    <Frame style={{ paddingTop: "64px", paddingBottom: "64px" }}>
      <img
        src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/components/surveys/emoji.png"
        style={{
        width: "340px",
        height: "auto",
      }}
      />
    </Frame>
  </Tab>

  <Tab title="Code">
    <CodeGroup>
      ```Typescript App.tsx
        import * as Frigade from '@frigade/react';
        
        const App = () => {
          return (
            <Frigade.Survey.NPS
             flowId="my-flow-id"
             dismissible={true}
             alignSelf="flex-end"
             justifySelf="flex-end"
             positiveLabel="Very good"
             negativeLabel="Very bad"
             options={[
              { label: "😞", value: "0" },
              { label: "😕", value: "1" },
              { label: "😐", value: "2" },
              { label: "🙂", value: "3" },
              { label: "😍", value: "4" },
              ]}
            />
          );
        };
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.Survey.NPS flowId="my-flow-id" dismissible={true} />
      );
    };
    ```
  </Tab>

  <Tab title="No-code">
    NPS Surveys can be be deployed with no-code using [Collections](/platform/collections).
  </Tab>
</Tabs>

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
      import { Form, FormFieldProps } from "@frigade/react";

      function CalendarField({ field, submit }: FormFieldProps) {
        return (
          <div>
            <input type="date" onChange={field.onChange} value={field.value} />
          </div>
        );
      }

      // ...

      <Form flowId="my-flow-id" fieldTypes={{ calendar: CalendarField }} />;
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

    <ParamField body="negativeLabel" type="string">
      The label to display for the negative end of the NPS scale.
      If not provided, the default label "Not likely at all" will be used.
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

    <ParamField body="options" type="NPSOptions">
      The options to display in the NPS field.
      If not provided, the default NPS numbers from 0 to 10 will be used.
    </ParamField>

    <ParamField body="positiveLabel" type="string">
      The label to display for the positive end of the NPS scale.
      If not provided, the default label "Extremely likely" will be used.
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
