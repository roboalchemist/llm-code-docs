# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/events/filter-field.md

# Filter Field

Log Records can be filtered by the following fields:

| Filter | Description |
|  --- | --- |
| event | An event type. For a complete list of all events written to the log see the Event Types table below. |
| list | The email address of a mailing list the message was originally sent to. |
| attachment | A name of an attached file |
| from | An email address mentioned in the from MIME header. |
| message-id | A Mailgun message id returned by the messages API |
| subject | A subject line |
| to | An email address mentioned in the MIME header |
| size | Message size. Mostly intended to be used with a wide ranger filtering expressions (see below) |
| recipient | Specific to stored events, this field tracks all the potential message recipients. |
| tags | User defined tags |
| severity | Temporary or Permanent. Used to filter events based on severity, if exists. (Currently failed events only) |