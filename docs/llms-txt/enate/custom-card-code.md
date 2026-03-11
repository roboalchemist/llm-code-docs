# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/custom-card-content/custom-card-code.md

# Custom Card Validation

In the Typescript section of a Custom Card you can add your logical calculation or validation code related to work items and data fields.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWjeNA-Y8yYwPqdj4lc%2F-MWjeUCuWC9_z6mEtvcN%2Fimage.png?alt=media\&token=32a50154-b660-474c-86a0-38c77d058764)

In many circumstances you will also need to add validation. The best way to add validation is by using the **ngOnInit** method. Once you submit a work item it will be checked for any validation errors. If there is a validation error, the work item submission will be paused until the error is resolved.

If you look at your Typescript you will see that there are few lines of code which have been created by default, as well as a few properties such as **Option**, **Packet** and **IsExpanded**.

1. **Option** - The Option property contains two properties: Packet and Card.

   **Card** - This property contains the information about the card including which fields are attached to this card.

   **Packet** - The Packet property contains all the information related to the work item. Use your Swagger UI, available for your instance at (**https\://*****\<your-work-manager-url>*****/webapi/**) and look for the following APIs to see further details: \
   **Case/GetCase** \
   **Ticket/GetTicket**\
   **Action/GetAction**&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWjeNA-Y8yYwPqdj4lc%2F-MWjeaHNGb5WHtHisl6n%2Fimage.png?alt=media\&token=edacf093-d68b-4101-80ab-a86eebf4cef7)

In your Typescript section there will be generated/auto- code and it will also contain following **ngOnInit** method:

```
ngOnInit() {
        //YOUR CUSTOM CODE BEGINS
        
        //YOUR CUSTOM CODE ENDS
}
```

Now let us take a few examples to understand how we can add runtime validation.

1\. Required Validation

```
ngOnInit() {
        //YOUR CUSTOM CODE BEGINS

        this.Option.Card.Validators.push(function (packet, card) {
            // YOUR VALIDATION
            const errors = [];
            if (
                packet.DataFields.Policy === null ||
                packet.DataFields.Policy === ""
            ) {
                errors.push('Please enter a policy number');
            }
            return WorkItemValidator.ERRORS(card, errors);
        });

        //YOUR CUSTOM CODE ENDS
    }

```

2\. Range Validation

```
ngOnInit() {
        //YOUR CUSTOM CODE BEGINS

        this.Option.Card.Validators.push(function (packet, card) {
            // YOUR VALIDATION
            const errors = [];
            if (
                packet.DataFields.Policy > 0 ||
                packet.DataFields.Policy < 9999
            ) {
                errors.push('Policy number must be between 1 - 9999.');
            }
            return WorkItemValidator.ERRORS(card, errors);
        });

        //YOUR CUSTOM CODE ENDS
    }

```

3\. Complex Validation

```
ngOnInit() {
        //YOUR CUSTOM CODE BEGINS

        this.Option.Card.Validators.push(function (packet, card) {
            // YOUR VALIDATION
            const errors = [];
            if (packet.ProcessType === 1) { //for case type work item
                if (
                    packet.DataFields.Policy > 0 ||
                    packet.DataFields.Policy < 99
                ) {
                    errors.push('Policy number must be between 1 - 99.');
                }
            } else if (packet.ProcessType === 2) { //for ticket type work item
                if (
                    packet.DataFields.Policy > 100 ||
                    packet.DataFields.Policy < 199
                ) {
                    errors.push('Policy number must be between 100 - 199.');
                }
            } else { //for action type work item
                if (
                    packet.DataFields.Policy > 200 ||
                    packet.DataFields.Policy < 299
                ) {
                    errors.push('Policy number must be between 200 - 299.');
                }
            }

            return WorkItemValidator.ERRORS(card, errors);
        });

        //YOUR CUSTOM CODE ENDS
    }

```
