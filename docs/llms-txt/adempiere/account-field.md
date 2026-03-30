# Source: https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons/account-field.md

# Account Field

![An Account field in the Accounting tab of the Product window.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1rGpPpwYvov7eQJR%2Fswing_field_account_example.PNG?generation=1551809346450039\&alt=media)

Icons: ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1rGrkRP99h2vu5U9%2Faccount24.gif?generation=1551809346252294\&alt=media) ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1rGt2NOXql3eaXEU%2Finfoaccount24.webicon.png?generation=1551809346286182\&alt=media)

The Account field displays the details of a selected set of [Accounting Dimensions](https://adempiere.gitbook.io/docs/glossary#accounting-dimension) referred to as a [Combination](https://adempiere.gitbook.io/docs/glossary#combination). It is usually found on Accounting tabs which provide accounting information related to the parent tab.

The field shows a text value with the Accounting Dimensions separated by a hyphen. Dimensions that have not yet been set have an underscore as a place holder. When the Combination is used to post Accounting Facts, the values of the Dimensions will be drawn from the posted document, overwriting the placeholders and other values in the Combination and the final Combination will be used to create the Accounting Fact. The account number dimension is not overwritten.

To set a Combination, you can type in a text value or you can click on the helper button. The text that is entered will be assessed as follows:

* If the text is null, zero length or equals "%" - the wild card - , the [Account Dialog](https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/account-dialog) will be opened.
* If the text does not end with a percent sign "%", one is added as the last character.
* The software then looks for a valid combination where the alias or the combination string match the text
* If there is a single match, the field is filled with the valid combination.
* If there is no match or more than one match, the [Account Dialog](https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/account-dialog) is opened.

The Account Icon ([![Image:Icon\_Account24.png](http://wiki.adempiere.net/images/3/31/Icon_Account24.png)](http://wiki.adempiere.net/File:Icon_Account24.png)) can also be pressed to activate the [Account Dialog](https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/account-dialog). A combination selected in the Account Dialog will be displayed once the dialog is confirmed and closed. If the Account Dialog is canceled, the Account field will be cleared.

The pop-up menu (mouse right-click) will display the following entry:

* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) [Change Log](http://wiki.adempiere.net/Change_Log)
