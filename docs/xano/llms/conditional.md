# Source: https://docs.xano.com/the-function-stack/functions/data-manipulation/conditional.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Conditional

Conditional statements are used to determine what functions to run based on the outcome of an expression, or a set of expressions.

<Tip>
  **Hint**

  For simple comparisons with multiple options, consider using [Switch](/the-function-stack/functions/data-manipulation/switch) instead.
</Tip>

## Conditional vs Switch — which one should you use?

When deciding between using an If/Then statement and a Switch statement, it's important to consider the complexity and clarity of the logic you're implementing. An If/Then statement is ideal for situations where you have several conditions that require different actions. It provides straightforward logic for evaluating true or false scenarios.

On the other hand, a Switch statement is better suited for cases with multiple possible values for a single variable. It makes your function stacks cleaner and more organized by avoiding deep nesting of conditions when the logic involves fixed values. Use If/Then for more advanced conditions and Switch for handling multiple specific scenarios with more concise readability.

<Frame>
  <iframe src="https://demo.arcade.software/FhWQsqxH5UlL7y89PGzV?embed" title="https://demo.arcade.software/FhWQsqxH5UlL7y89PGzV?embed" allowFullScreen allow="clipboard-write" class="contentkit-webframe" width="1000" height="500" />
</Frame>

<Steps>
  <Step title="Add a Conditional step to your function stack.">
    &#x9;
  </Step>

  <Step title="Click Add Condition to add a condition.">
    You can add multiple conditions to a single function stack if you want to check multiple values.

    ### Using the Expression Builder

    Each conditional has four different components.

    **Conditional Type**

    The conditional type determines how this condition is weighted in the final return. You can choose between **AND** and **OR. AND** conditionals require the present conditional and any others before it to be satisfied, such as "where the date is before today **AND** the user is an admin". **OR** conditionals do not require any other conditionals to be satisfied, such as "if the user is an admin **OR** if the user is a manager".

    **Left Value**

    This is the first value you're using in the conditional. In a database query, this is usually going to be a column that you want to check against.

    **Operators**

    <Info>
      Please note that operators may differ based on where you are building the expression. Database queries will have different operators available than regular conditional statements. Learn More
    </Info>

    * **Equals (==)** - an exact match

    * **Not Equals (!=)** - does not equal

    * **Equals with type matching (===)** - an exact value match and an exact type match

      * Ex. Variable **var\_1** has a value of 123, with a type of text. You set up a conditional statement to check if **var\_1 === 123**, but your value in the conditional statement is of type integer. This would return false, because the types do not match.

    * **Not equals with type matching (!==)** - does not equal value or type, similar to ===

    * **Greater than (>)** - the value on the left is greater than the value on the right

    * **Greater than or equals (≥)** - the value on the left is greater than or equals to the value on the right.

    * **Less than (\<)** - the value on the left is less than the value on the right.

    * **Less than or equals (≤)** - the value on the left is less than or equals to the value on the right.

    * **LIKE** - Used for comparing text. Like is case-insensitive and compares if a text string is like another text string. It can be thought of as equals for text but upper case and lower case does not matter.

    * **NOT LIKE** - Used for comparing text. Not Like is case-insensitive and compares if a text string is not like another. It is like not equals for text but upper case and lower case does not matter.

    * **INCLUDES** - Used for comparing text. Includes is a flexible operator and is case-insensitive. It is able to determine if there is a partial match in a text string.

    * **DOES NOT INCLUDE** - Used for comparing text. Does not include determines if a text string is not included in another text string.

    * **IN** - If a single value is found in an array (list). Start with the single value on the left side and the right side should contain the array.

    * **NOT IN** - If a single value is not found in an array (list). The single value should be on the left side and the array on the right side.

    * **REGEX MATCHES** - [Regular Expression](https://regex101.com/) used for finding patterns in text.

    * **REGEX DOES NOT MATCH** - [Regular Expression](https://regex101.com/) used for finding a pattern that does not match in text.

    * **OVERLAPS** - Used for comparing two arrays. Overlaps determines if any values in one array are present in the second array.

    * **DOES NOT OVERLAP** - Used for comparing two arrays. Does not overlaps determines if no values in the first array are present in the second array.

    * **CONTAINS** - Contains is an advanced filter used for JSON and arrays. It looks for an exact schema match.

    * **DOES NOT CONTAIN** - Does not contain is the opposite of contains. It determines if there is not an exact schema match.

    #### Right Value

    The right value is whatever you are checking against the left value. This could be a hardcoded value, a variable, or even a database field from the same record.
  </Step>

  <Step title="Once you have your conditions defined, add additional functions into your Then and Else blocks.">
    If the condition(s) evaluate as **true**, it will run the steps in the Then block.

    If the condition(s) evaluate as **false**, it will run the steps in the Else block.

    You can also leave either of these blocks empty if you only want to utilize one of them.
  </Step>

  <Step title="You can Use Else If to define multiple paths in the same conditional statement.">
    Click <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2b4bce28-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=948f0a009f3f946b4f54494a54880f21" className="inline m-0" width="169" height="38" data-path="images/2b4bce28-image.jpeg" /> to add an Else If path to your conditional statement. The process for defining the condition(s) it checks is exactly the same as before.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).