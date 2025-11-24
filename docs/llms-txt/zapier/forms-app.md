# Source: https://docs.zapier.com/platform/reference/forms-app.md

# Zapier integration structure for a forms app

> Form and survey app integrations built on Zapier allow users to connect mobile data collection forms to send the responses into other apps as new contacts, document templates, messages, and more.

To add a form or survey app integration in the Platform UI:

## Prerequisites

* A [Zapier account](https://zapier.com/sign-up).
* If you haven't used Zapier before, you'll want to learn the basics in our [Zapier Getting Started Guide](https://zapier.com/learn/zapier-quick-start-guide/).
* Familiarity with your app's API documentation and available endpoints.
* Review the [Platform UI Tutorial](/platform/quickstart/ui-tutorial).

## 1. Add a new entry/response trigger

* Start a new integration at [https://developer.zapier.com/](https://developer.zapier.com/) for your app
* Create a *New Form Entry/Submission* or *New Survey Response* trigger
* Use the standard *New* naming pattern to show users that this trigger retrieves new entries, not existing ones.
  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d5a605fafa8aaa679f86bca3655ce0d9.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=ab4f5f294a64e2bf0de9d3f138e58015" data-og-width="1215" width="1215" data-og-height="562" height="562" data-path="images/d5a605fafa8aaa679f86bca3655ce0d9.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d5a605fafa8aaa679f86bca3655ce0d9.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=0617b3c032121758da13bfc47a67a347 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d5a605fafa8aaa679f86bca3655ce0d9.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=babb547659c2ec939040faae307811c4 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d5a605fafa8aaa679f86bca3655ce0d9.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=4dd88de20c004d23ab305505d0eaa0c6 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d5a605fafa8aaa679f86bca3655ce0d9.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=6da727033116b3b249dff784a797aa36 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d5a605fafa8aaa679f86bca3655ce0d9.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=a6347ce566cfe387140266dbc3ea1b9d 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d5a605fafa8aaa679f86bca3655ce0d9.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=26f01634bbe2501227159326cfa32472 2500w" />
  </Frame>

## 2. Configure selection of a specific form

* Add a [dynamic dropdown](/platform/build/field-definitions#how-to-add-dynamic-and-custom-fields) to retrieve form names exactly as they are listed in your app.
* If the endpoint the dropdown uses allows for sorting, you can `sort_by` the create date to order the dropdown list by the most recently added form to make it easier for users to select the form they need.
* Make the selection of a form required so the trigger only watches for results from this one form
* If you keep the form field optional, it can be used for responses to any form; and you'll need to add help text to let users know what to expect if they do not select a form.
  <Frame>
    <video controls autoplay muted loop src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/79158aee580d74c8241e1375e73f91db.mp4?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=382e6f66bad0d05792a6a9687c47725d" data-path="images/79158aee580d74c8241e1375e73f91db.mp4" />
  </Frame>

## 3. Format the responses the trigger receives

### Question and answer fields

* Form fields or survey questions must include the same name within Zapier as that form field shown in your app's user interface.

* In a form that asks for contact information, the question/field “What's your email?” might internally use an ID like `1839dod38k01` or a generic label such as `Question 1` in your app's API. The user should also see the field's friendly name within Zapier so they'll recognize which field to use when mapping data to action steps. The raw field ID, the `key`, can still be shown beside the friendly name.

* For example, a common use case is to log responses in spreadsheets, with each answer field mapped to different columns. Showing only the key `q_1_answer` for a question is not intuitive for users. Include the label with the full question.

* Include the question number as a prefix to the label if possible, to help users find specific questions and fields.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/ae9c0c297710e3bce8385f5d5a7b468f.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=e567822a17344d1a8293efb656584521" data-og-width="1098" width="1098" data-og-height="1099" height="1099" data-path="images/ae9c0c297710e3bce8385f5d5a7b468f.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/ae9c0c297710e3bce8385f5d5a7b468f.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=6a7e431ed4826ca66845c7236e5f6cc1 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/ae9c0c297710e3bce8385f5d5a7b468f.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=8e903624a5b802d8981a0be3f1bb602e 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/ae9c0c297710e3bce8385f5d5a7b468f.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=c4fde68d92a114806ee1ef96d9b053dc 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/ae9c0c297710e3bce8385f5d5a7b468f.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=33fbc75047ce8235a08c12777814d4b6 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/ae9c0c297710e3bce8385f5d5a7b468f.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=2ede899c8d75f69761dc621ae579fb09 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/ae9c0c297710e3bce8385f5d5a7b468f.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=eef748be28530b846f697bb92eacfd0f 2500w" />
</Frame>

### Multiple choice fields

* Include the question title, answer and value as separate fields where possible. Use the same label to group these together in the trigger output.

* When a multiple choice question is based on a range of values (e.g., from “not really” to “very”), it is useful to return the choice values (such as `1` to `5`) with the actual answer. This can be especially helpful for users wishing to track responses in a spreadsheet.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/033953ce0537c18a6efbe47f783ddf5a.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=b906a8916b696ecda6e33f09eb93fd62" data-og-width="1398" width="1398" data-og-height="410" height="410" data-path="images/033953ce0537c18a6efbe47f783ddf5a.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/033953ce0537c18a6efbe47f783ddf5a.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=db38078acafef39abbe6ef9a33ca101e 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/033953ce0537c18a6efbe47f783ddf5a.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=fe9d2e03bd2d3e305ab9d712943ff168 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/033953ce0537c18a6efbe47f783ddf5a.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=669022babbc748d6393475a96aa67787 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/033953ce0537c18a6efbe47f783ddf5a.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=3f04ca71d7a68ee18cf6660de13de61a 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/033953ce0537c18a6efbe47f783ddf5a.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=238fc14125702a46e1fc505a8d78d0b9 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/033953ce0537c18a6efbe47f783ddf5a.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=c0f6007e702079ea21f1495136aab5ba 2500w" />
</Frame>

### Multi-select fields

* When users can select multiple responses (like a list of checkboxes) in a form or survey, it can be challenging to use this data within a trigger.

  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e922d705c9f9d61c46f32b31ba03e53f.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=9b5c4371bd039d42a4249a1ac7ce2a2a" data-og-width="1160" width="1160" data-og-height="610" height="610" data-path="images/e922d705c9f9d61c46f32b31ba03e53f.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e922d705c9f9d61c46f32b31ba03e53f.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=64fa3224908c337cdecf7f66772612a5 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e922d705c9f9d61c46f32b31ba03e53f.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=87b58ee43fdcc80ea7ad3f8636b82612 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e922d705c9f9d61c46f32b31ba03e53f.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=88e6b7a4a57e96309a314b192f795147 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e922d705c9f9d61c46f32b31ba03e53f.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=86cd5faf92685fdc2e9a59710ad2a0fd 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e922d705c9f9d61c46f32b31ba03e53f.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=f6e84a43f1a4ee8c6a9d21253b46bd07 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e922d705c9f9d61c46f32b31ba03e53f.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=85b0cf76e0d25ce624df0f73f9a65a54 2500w" />
  </Frame>

* When possible, return these responses individually by splitting each individual response to the question into its own field, with a value if it is selected by the responder and a blank value if not selected. This makes mapping Zap steps simpler because users can map all responses into one field separated by the correct delimiter, or can take action on specific responses when they are present with the user of [Filters](https://help.zapier.com/hc/en-us/articles/8496276332557-Add-conditions-to-Zaps-with-filters) or [Paths](https://zapier.com/features/paths).

  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a71b26a4a333fa9cb6b4a8c77607c426.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=d507fc81bbf5723b33a14a4f8ddf52db" data-og-width="1270" width="1270" data-og-height="422" height="422" data-path="images/a71b26a4a333fa9cb6b4a8c77607c426.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a71b26a4a333fa9cb6b4a8c77607c426.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=4452a7b863562ede0397a239998f7f28 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a71b26a4a333fa9cb6b4a8c77607c426.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=2026b061335759824e12aabb01e1d348 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a71b26a4a333fa9cb6b4a8c77607c426.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=5c9dda4f7403584bab1cffdfcff576b4 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a71b26a4a333fa9cb6b4a8c77607c426.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=fb76ee308f3a04b5352d84f5294a495a 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a71b26a4a333fa9cb6b4a8c77607c426.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=63d4a229e8c123449ead14cc6e677185 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a71b26a4a333fa9cb6b4a8c77607c426.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=c85f85c1bd432bfa7fb3e8d9ac3ce4a0 2500w" />
  </Frame>

* Depending on your app's API response fields, you might instead opt to return the question's selected values in a single, comma separated field. Users can then split the values themselves with Zapier's [Formatter](https://help.zapier.com/hc/en-us/articles/8496030096013-How-to-use-Formatter-Functions#using-split-text-0-3) tool, or could map the all the values together to a later step's field.
  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/02fd5f03f00a7e3c6953c95366013473.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=ea8a558b627fd7e2fdd92e0c6ae25ff8" data-og-width="850" width="850" data-og-height="102" height="102" data-path="images/02fd5f03f00a7e3c6953c95366013473.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/02fd5f03f00a7e3c6953c95366013473.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=995831d9ba8cc68b83ae79dbd07e323f 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/02fd5f03f00a7e3c6953c95366013473.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=82b476ad0cab0adeb63e33d492e93afb 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/02fd5f03f00a7e3c6953c95366013473.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=05845c50f43414e343c60417f780fb40 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/02fd5f03f00a7e3c6953c95366013473.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=70cb5e6c4e6387d0b4552ac389bd604e 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/02fd5f03f00a7e3c6953c95366013473.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=dbfb2c20454e76f6e49cebb60ee99853 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/02fd5f03f00a7e3c6953c95366013473.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=663718a755c89f6bc0d3f2e8613fa51f 2500w" />
  </Frame>

### Date fields

* Return the timestamp when the response was completed in [ISO 8601 format](/platform/publish/branding-guidelines#output-data). Also return any dates users can select in the form or survey in ISO 8601 format.

* When possible, also include a human-friendly date for the response completion and any other selected dates in the response.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/762d2661a3da2d4a689052e316091f42.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=75e5da3721e65a036658fcbfa04ad9cc" data-og-width="806" width="806" data-og-height="219" height="219" data-path="images/762d2661a3da2d4a689052e316091f42.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/762d2661a3da2d4a689052e316091f42.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=600d34db8b8e9ee0f8b8b8fd1c043a7a 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/762d2661a3da2d4a689052e316091f42.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=04502c4f020650e0a97db6fe27fdc35b 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/762d2661a3da2d4a689052e316091f42.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=5156dcfe3083edb96b0a359b2b949843 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/762d2661a3da2d4a689052e316091f42.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=259c617ad28f05b22c09003394a4b533 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/762d2661a3da2d4a689052e316091f42.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=65b4a7057882464e40b44fcb2b1811cd 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/762d2661a3da2d4a689052e316091f42.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=3cc09e5618171e34b2a0c04186213fde 2500w" />
</Frame>

### File attachments

* When users can attach files to form responses, include those in the response data as a publicly accessible URL for the file.

* You could configure Zapier to request the full file via [file dehydration](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#file-dehydration) but you'll need to then work in the [Platform CLI](/platform/quickstart/cli-tutorial).

## 4. Choose trigger type under API Configuration

### REST Hook trigger

* If your app supports webhook subscriptions that can be manipulated through a REST API, use [REST hooks](/platform/build/trigger#rest-hook-trigger) for your trigger to send new form entries to Zapier as soon as the form is filled out.

* Webhook triggers are marked as *Instant* [in the Zap Editor](https://cdn.zappy.app/6b696dfaf34664b181b6df651067cfd3.png).

* When your user has many form entries in a short space of time, webhooks make your integration more robust, preventing the possibility that a high number of new entries will exceed the page size of polling results.

* With REST hooks, Zapier won't need to repeatedly poll your API to check for new responses.

### Polling trigger

* When using a Polling trigger, and for the *Perform List* URL for REST Hook triggers, the Polling URL should return the most recent form entry for the chosen form.

* If there are no entries for the selected form, return an empty array. Zapier will then encourage the user to create a sample then re-test their trigger in the Zap Editor to finish mapping their Zap.

## 5. Handle Sample data

* Zapier requests sample results for every trigger and action when users select *Skip test* if the test API call returns no data.

* Since a form app has dynamic fields unique to each user, it's impossible to define sample data that work for every form.

* Instead, include only the common form fields that would be present for every result, such as form ID and timestamp, for the trigger's static sample data.

## 6. Test your triggers

Make Zaps with the trigger for the following criteria to ensure your app integration works as expected:

* A triggering form that already has completed entries, where you should check that your polling URL is returning the latest form entry first (reverse chronological).
* A brand new triggering form with no entries, to make sure your form sends an appropriate error when no results exists.
* A triggering form that is composed of required and optional questions, to make sure all the questions are mappable into later action steps, regardless of whether the latest response only had a few questions answered.
* A triggering form that has questions with multi select answers, where you should choose one or more options when sending a response in your app, to check that all the values come through.
* Turn on the Zaps and submit new entries to each form to check that the Zap triggers and includes the expected response.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
