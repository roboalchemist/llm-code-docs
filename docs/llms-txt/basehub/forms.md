# Forms

> The powerful Event block lets you build a form schema from the dashboard, and consume it in code to build complex forms.

This article goes over how to build and manage Forms via BaseHub. Take a look at our video guides:

*   [Feedback Form](https://docs.basehub.com/templates-and-examples/examples-and-guides/create-a-feedback-form)
    
*   [Newsletter](https://docs.basehub.com/templates-and-examples/examples-and-guides/create-a-newsletter)
    
*   [Form Builder](https://docs.basehub.com/templates-and-examples/examples-and-guides/create-a-form-builder)
    

## Create an event block and customize your fields

First things first, you’ll need an Event block to start building your form and to have a space where to display users’ submissions. You can create a new block using the slash command in the dashboard.

## Handle the incoming schema in code

BaseHub SDK lets you fetch the event block schema and handle each field as you want. Completely headless experience.

Easily set up a dynamic form builder using <Pump />

## Start receiving events

Last but not least, you should set up a form action to link users’ submissions to your Event block in BaseHub’s dashboard.

page.tsx

```
import { Pump } from "basehub/react-pump"
import { RichText } from "basehub/react-rich-text"
import { parseFormData, sendEvent } from "basehub/events"

export default function Home() {
  return (
    <Pump
      queries={[
        {
          homepage: {
            title: true,
            subtitle: {
              json: {
                content: true,
              },
            },
            submissions: { 
              ingestKey: true,
              schema: true,
            },
          },
        },
      ]}
    >
      {async ([{ homepage }]) => {
        "use server"

        const ingestKey = homepage.submissions.ingestKey 

        return (
          <div className="...">
            <main className="flex flex-col gap-8 row-start-2 items-center">
              <h1 className="text-3xl sm:text-4xl text-center sm:text-left">
                {homepage.title}
              </h1>
              <div className="text-center sm:text-left">
                <RichText
                  content={homepage.subtitle.json.content}
                />
              </div>
              <form
                className="w-1/2 sm:w-full border rounded-lg p-4 space-y-3"
                action={async (formData) => { 
                  "use server"
                  const parsedSubmission = parseFormData(
                    ingestKey,
                    homepage.submissions.schema,
                    formData,
                  )

                  if (!parsedSubmission.success) {
                    // The `parseFormData` return type lets you
                    // handle parsing errors. Since this is a simple
                    // example, we're just throwing an error.
                    throw new Error(
                      JSON.stringify(parsedSubmission.errors),
                    )
                  }

                  sendEvent(ingestKey, parsedSubmission.data)
                }}
              >
                {homepage.submissions.schema.map((field) => (
                  <label
                    key={field.id}
                    className="flex gap-x-2"
                  >
                    <span>{field.label}</span>
                    <input
                      {...field}
                      className="border rounded-sm"
                    />
                  </label>
                ))}
                <button type="submit">Submit</button>
              </form>
            </main>
          </div>
        )
      }}
    </Pump>
  )
}
```

Once this is set up, events will be loaded in real-time in your dashboard.

Safely parse user inputs, send typed form data, and read submissions in real-time

## Extend your forms

Once you have the initial setup, building more complete forms has the same or even less complexity. Here’s how:

Fully customizable forms, in a way you've never seen before.