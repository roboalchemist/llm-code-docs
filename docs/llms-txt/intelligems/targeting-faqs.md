# Source: https://docs.intelligems.io/general-features/targeting/targeting-faqs.md

# Targeting FAQs

<details>

<summary>When running a price test, what prices do visitors see when they do not match audience targeting or are excluded from the test?</summary>

When a visitor is **excluded from a price test**, they are shown **control group pricing** by default.

At the start of a test, Intelligems updates product prices in Shopify to reflect the **highest test price**. For those not included in the test, Intelligems assigns them to the control group so they see the same pricing experience they would have if the test weren’t running — maintaining a seamless and accurate user experience. This includes any other changes that have been set up in the control group, such as onsite edits, CSS or JS injections.

</details>

<details>

<summary>How is audience or page targeting taken into account when it comes to Mutually Exclusive Experiments?</summary>

When you set up tests to be **mutually exclusive**, each visitor is assigned to one test within the exclusion group as soon as they land on your site — **before** any targeting conditions are evaluated. They are not assigned to a test group until they meet all targeting conditions.

This means a visitor might be assigned to a test they never actually qualify for. If they don’t meet that test’s targeting rules, they won’t be included in a test group — and they also won’t be eligible for any other mutually exclusive tests. As a result, some of your traffic may not be included in any testing, which can lead to **lower traffic utilization** and **slower learnings**.

This approach helps ensure clean, unbiased test results by preventing targeting rules from influencing which test a visitor is assigned to. However, it’s important to keep in mind that mutually exclusive tests are best used when targeting is broad, or when avoiding test overlap is critical.

</details>
