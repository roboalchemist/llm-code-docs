# Source: https://docs.xano.com/the-function-stack/functions/data-manipulation/switch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Switch

<Info>
  **Quick Summary**

  Switch Case is similar to a conditional statement, but it's designed to only check a single value for matches. Where a conditional is great for things like "If the user joined before 2020 and is also a subscriber", Switch Case is more efficient and ideal for simple scenarios like "If the color is red, blue, green, brown, yellow, or orange", when you want each of those options to have different paths.
</Info>

## Conditional vs Switch — which one should you use?

When deciding between using an If/Then statement and a Switch statement, it's important to consider the complexity and clarity of the logic you're implementing. An If/Then statement is ideal for situations where you have several conditions that require different actions. It provides straightforward logic for evaluating true or false scenarios.

On the other hand, a Switch statement is better suited for cases with multiple possible values for a single variable. It makes your function stacks cleaner and more organized by avoiding deep nesting of conditions when the logic involves fixed values. Use If/Then for more advanced conditions and Switch for handling multiple specific scenarios with more concise readability.

## Using Switch Case

<Steps>
  <Step title="Add a Switch statement to your function stack.">
    Switch is located under Data Manipulation.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/74525eec-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=a3852682af1bfbcac15ddca1652fd010" width="301" height="74" data-path="images/74525eec-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Set the value that Switch should be checking.">
    You can hard code a value here, or specify a variable or input.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/e0381843-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=2416b91a54e54e22cefeadeef39debdf" width="521" height="238" data-path="images/e0381843-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Set your 'default' functions, if desired.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/906f2cb1-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=3e9360c0350cb3f06510a0291d2a3eb3" width="249" height="171" data-path="images/906f2cb1-image.jpeg" />
    </Frame>

    The **Default** section of Switch will run if:

    1. No matches are found

    2. You chose to not break out of Switch after a match is found

    This is a good spot to insert any "catch-all" situations where you want a standard behavior for unaccounted possibilities.
  </Step>

  <Step title="Click '+ Add Switch Case' to define a behavior based on a specific value.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/47772075-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=80039ad6e9a29bbfe90e8a3c0a2d9294" width="146" height="34" data-path="images/47772075-image.jpeg" />
    </Frame>

    When adding a new **case**, you'll be asked to provide the value that determines if this case will run.

    You can also choose to either stop the Switch Case statement after the match is found, or execute the functions under Default after matching.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/d0b0fc7b-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=165179efc61d4dfb2423d60df1026213" width="516" height="415" data-path="images/d0b0fc7b-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Add functions to your case(s)">
    Click <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/742005fd-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=2b59a6ee80388320c298d02ca5c15263" className="inline m-0" width="93" height="26" data-path="images/742005fd-image.jpeg" /> under your cases to add functions to them, or drag and drop functions inside of them. Now, when your Switch function detects that case in the value you specified in step 2, it will execute those functions.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/de33daf5-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=07fd8c30e5f490b1e118f37a344664d8" width="376" height="285" data-path="images/de33daf5-image.jpeg" />
    </Frame>
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).