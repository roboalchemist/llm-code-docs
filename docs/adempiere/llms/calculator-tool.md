# Source: https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/calculator-tool.md

# Calculator Tool

The Calculator Tool is a small and simple calculator that provides simple math support to data entry for number fields. It is most commonly accessed in Number fields as the helper function.

![A Number field with the Calculator Tool as the helper function.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1rHBNfvDfHE3OeUT%2Fswing_field_amountexample.PNG?generation=1551809346134604\&alt=media)

| Accessed through ... | In ...                      |
| -------------------- | --------------------------- |
| Helper Function      | Number Fields               |
| Java Client Menu:    | **Tools > Calculator** menu |
| Short Cut Key:       | (none)                      |
| Menu Tree            | (none)                      |

## Restrictions

None.

## Description

![Java Client version of the Calculator Tool](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1rHEaQr7HYC-7K9U%2Fswing_calculatorttool.PNG?generation=1551809346030786\&alt=media)

![Web Application version of the Calculator Tool](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1rHGfjts3eFmu2ab%2Fwebui_calculatortoo.PNG?generation=1551809346136985\&alt=media)

The calculator tool is a simple calculator that provides support for the following operators: + - \* / %. Is also can be used to perform currency conversions by clicking the '$' button. (Bottom, left. It is hard to see in yellow.)

{% hint style="info" %}
The Web Application version of the calculator is simpler and only performs basic calculations. There is no currency conversion.
{% endhint %}

In the Java Client, the calculator can be activated from the **Tools > Calculator** menu entry or by clicking on the calculator icon[![Image:Icon\_Calculator24.png](http://wiki.adempiere.net/images/d/db/Icon_Calculator24.png)](http://wiki.adempiere.net/File:Icon_Calculator24.png) in any number field.

The calculator can be operated by the mouse but it is most effective with a number pad and keyboard. The behavior between the Java Client and the Web Application is slightly different.

For the Java Client, the following keys are accepted:

* 0-9 - standard digits are added to the end of the display
* In the Java Client, '.' and ',' are both treated as decimals and replaced by '.' in the display.&#x20;
* / \* - + operands are added to the end of the display. If there is already an operand in the last position, it is replaced by the one just typed. If there is an operand between two numbers, the calculation is completed before the new operand is added.
* % operand will divide the displayed number by 100.
* \= or \<Enter> will complete the calculation. If the calculator was opened from a number field, the equal sign will close the calculator tool and the result will appear in the number field.
* 'A' or \<Delete> will clear the display.
* 'C' or \<Backspace> will remove the last character typed.
* \<Esc> or clicking the red Cancel button will abort the calculation and close the Calculator Tool.
* '$' or clicking the $ button will display the currency conversion buttons. Selecting and double clicking either currency will convert the currently displayed number.

![Java Client calculator showing the currency conversion.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1rHI_vjDd8qAZpBD%2Fswing_calculatortoolcurrency.PNG?generation=1551809346442409\&alt=media)

For the Web Application, the calculator is simpler.

* The 0-9 - standard digits are added to the end of the display
* / \* - + operands are added to the end of the display.&#x20;
* % operand, if clicked, will divide the displayed number by 100.   If typed into the box, nothing will happen.
* \= will complete the calculation. If the calculator was opened from a number field, the equal sign will close the calculator tool and the result will appear in the number field.
* 'A' will clear the display.
* 'C' will remove the last character typed.
* Clicking outside the calculator will abort the calculation and close the Calculator Tool.
* The $ button is disabled.

## See Also

* [Number Field](https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons/number-field)
