# Source: https://docs.intelligems.io/content-testing/ending-a-theme-test.md

# Ending a Theme Test

{% hint style="danger" %}
After ending a theme test, we recommend you not delete any theme that was in the test for at least two months
{% endhint %}

During the experiment, visitors are sent to draft themes, and their browser will "remember" which theme to open the next time they visit your store via a session cookie. Once the test is over, if a visitor who was in one of the test groups re-visits your store and the cookie is still active, Shopify will load the draft theme, and Intelligems will then immediately reset them back to the live theme.

However, if the draft theme that was in the test has since been deleted, Intelligems won't be loaded and won't have the opportunity to reset the visitor's theme. Instead, the visitor see an error from Shopify, since they're trying to load a theme that does not exist.\
\
So, it's important to leave any themes that were tested in draft mode (rather than deleting them) for a while after the experiment, to ensure any returning visitors are reset back to the live theme.
