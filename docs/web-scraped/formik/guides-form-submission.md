# Formik Documentation
# Source: https://formik.org/docs/guides/form-submission
# Path: /docs/guides/form-submission

#### Documentation

#### API Reference

#### Documentation

#### API Reference

# Form Submission

## Submission Phases

To submit a form in Formik, you need to somehow fire off the providedhandleSubmit(e)orsubmitFormprop. When you call either of these methods, Formik will execute the following(pseudo code)each time:

`handleSubmit(e)`
`submitForm`

### Pre-submit

- Touch all fields.initialValuesare required and should always be specified. See#445
`initialValues`
- SetisSubmittingtotrue
`isSubmitting`
`true`
- IncrementsubmitCount+ 1
`submitCount`

### Validation

- SetisValidatingtotrue
`isValidating`
`true`
- Run all field-level validations,validate, andvalidationSchemaasynchronously and deeply merge results
`validate`
`validationSchema`
- Are there any errors?Yes: Abort submission. SetisValidatingtofalse, seterrors, setisSubmittingtofalseNo: SetisValidatingtofalse, proceed to "Submission"
- Yes: Abort submission. SetisValidatingtofalse, seterrors, setisSubmittingtofalse
`isValidating`
`false`
`errors`
`isSubmitting`
`false`
- No: SetisValidatingtofalse, proceed to "Submission"
`isValidating`
`false`

### Submission

- Proceed with running the submission handler (i.e.onSubmitorhandleSubmit)
`onSubmit`
`handleSubmit`
- Did the submit handler return a promise?Yes: Wait until it is resolved or rejected, then setsetSubmittingtofalseNo:CallsetSubmitting(false)to finish the cycle
- Yes: Wait until it is resolved or rejected, then setsetSubmittingtofalse
`setSubmitting`
`false`
- No:CallsetSubmitting(false)to finish the cycle
`setSubmitting(false)`

## Frequently Asked Questions

IfisValidatingisfalseandisSubmittingistrue.

`isValidating`
`false`
`isSubmitting`
`true`
It is common practice to only show an input's errors in the UI if it has been visited (a.k.a "touched"). Before submitting a form, Formik touches all fields so that all errors that may have been hidden will now be visible.

Disable whatever is triggering submission ifisSubmittingistrue.

`isSubmitting`
`true`
IfisValidatingistrueandisSubmittingistrue.

`isValidating`
`true`
`isSubmitting`
`true`
If the submission handler does not return a promise, make suresetSubmitting(false)is called at the end of the handler.

`setSubmitting(false)`

#### On this page

#### Resources

- Docs
- Learn
- Guides
- API Reference
- Blog

#### Community

- User Showcase
- Funding
- Community Chat
- Project Forum
- Releases
- Star

#### About Formium

- Home
- GitHub
- Twitter
- Contact Sales

#### Subscribe to our newsletter

The latest Formik news, articles, and resources, sent to your inbox.