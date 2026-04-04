# Source: https://docs.intelligems.io/general-features/targeting/mutually-exclusive-experiments.md

# Mutually Exclusive Experiments

{% hint style="info" %}
Note that this feature is not enabled by default. If you would like to use this feature, please contact us [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).
{% endhint %}

## Why make tests mutually exclusive?

* **Reduce interaction effects:** If someone is exposed to several experiments at the same time, it may become harder to ascertain which experience led to a change in their behavior. For example, if a visitor is exposed to one experiment that changes the copy on a button and another that repositions the button, you can’t be sure whether a change in conversion rate was caused by the first change, the second, or a combination of both.
* **Minimize UX risks:** If you’re concerned about bugs or unexpected site behavior resulting from two experiments that affect the same elements or pages in your site, you may consider making them mutually exclusive.
* **Prevent users from being exposed to a test after seeing another:** In case you’re running frequent tests, you may be concerned about a visitor seeing dramatic changes to colors, prices, and layouts in quick succession.

## How to Make Tests Mutually Exclusive

**Intelligems uses Mutually Exclusive Test Groups, or “Exclusion Groups” to ensure that tests are mutually exclusive.**

* An exclusion group holds one or more tests that will not be shown to the same visitor.
* If a user has never been exposed to any of the active tests in the group, Intelligems will randomly place them in one of the active tests. You can also set a test to have higher probability than others of being served to a user.
* If a user has been exposed to one of the active tests in the exclusion group, they will be kept in that test going forward - as long as it remains in the exclusion group.
* Tests of any type and any status can be in an Exclusion Group - though the status of a test will affect the behavior of the group. See below for details.
* A test can be in at most one exclusion group at the same time. This means there is no way for test A to be mutually exclusive with test B and C, but for B and C *not* to be mutually exclusive.

**Follow these steps to place a test in an Exclusion Group:**

* On the Targeting page of an experiment, go to the Mutually Exclusive Tests section. Click to add the test to an existing Exclusion Group or create a new group.
* You may do this regardless of test status, though it’s safest to create a number of tests and activate them only once they’ve been added to the same Exclusion Group.
* When you no longer want a test to be in the group, you can remove it from the group or place it in another.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-63307d01e63e81114d22e71ff34410e5fa4d7b86%2Fimage.png?alt=media" alt=""><figcaption><p>Making a test mutually exclusive</p></figcaption></figure>

## How does Intelligems decide which visitors see which tests?

A new visitor to your site will be exposed to at most one active test in an Exclusion Group. Intelligems uses one of two strategies to decide which test to show to a new visitor. You can set this option manually on each Exclusion Group at any time.

* **Option 1 - Random:** a new visitor has an equal chance of being bucketed into any of the *active* tests. This is the default behavior that should serve well in most situations.
* **Option 2 - Weighted:** a new visitor is more likely to be exposed to some tests than others. You can set the relative ‘weights’ of each test to indicate which tests are more important. This is useful in case you want specific tests to fill up with visitors first - in order to reach statistical significance faster - or if you are unsure about a test’s effects and want to ease users into it.

{% hint style="info" %}
Weighted non-active tests: Note that, since visitors cannot be shown a paused or pending experiment, the weights shown for experiments are approximate and relative. For example, consider a group that contains the following tests:

A (active - 40% weight), B (active - 40%), C (pending - 10%), D (paused - 10%)

C and D cannot be shown to a visitor until activated, so A and B will each have a 50% chance of being shown to a visitor, rather than a 40% chance. This ensures that tests receive as much traffic as possible.
{% endhint %}

## What about pending, ended, or paused experiments?

Aside from active tests, your Exclusion Groups may contain tests that are pending (not yet started), paused, or ended. Intelligems treats these as follows:

### **Ended Tests**

**New Visitors:** If a group contains an Ended test, *new visitors* will be placed in one of the active tests in the group, as usual.

**Returning Visitors:** If a group contains an Ended test, Intelligems uses one of two strategies to decide what should happen to any returning visitors that have previously been exposed to that test. You can set this option manually on each Exclusion Group at any time.

* **Option 1 - Include :** the returning visitor will be placed into one of the active tests (if any). This is the default behavior and helps maximize traffic to your tests.
* **Option 2 - Exclude:** the returning visitor will not be placed into any of the active tests in the group, as long as those tests remain in the group. You may choose this option in order to limit the number of changes visitors see in a short period of time, or to prevent visitors from seeing a certain experience once they’ve been exposed to another in the past.

Note that, if a test ends and it’s in a group that uses relative weights, its weight is automatically set to zero. The weights of all other tests are scaled up proportionally to add up to 100%.

### **Paused & Pending Tests**

* **New Visitors:** If a group contains an Paused or Pending test, *new visitors* will be placed in one of the active tests in the group, as usual.
* **Returning Visitors in Paused tests:** If a group contains a Paused test, *returning visitors* that have been exposed to that test will be excluded from all tests in the group. When the experiment is unpaused, they will once again see it.

## Caveats about Price and Shipping Tests

There are a few things to consider when adding a Price or a Shipping Test to an exclusion group:

* **Price Tests**: when you start a price test, Intelligems will automatically update your product prices in Shopify to the highest price in the test for each product. Therefore, any visitors excluded from the test will see the highest price on those products for the duration of the test.
* **Shipping Tests**: when you start a shipping test, Intelligems will automatically remove the rates that you select to test when you start your test, and replace those with the rates configured in the test. Any visitors excluded from the test will see the rates you've set for the Control Group.

## How Mutual Exclusion Interacts with Test Entry Requirements

When you set up tests to be mutually exclusive, each visitor is assigned to one test within the exclusion group **as soon as they land on your site** — before any entry requirements are evaluated.

This is important because some test types require visitors to take a specific action to actually enter the test:

* **Split URL tests** require visiting the origin URL
* **Template tests** require visiting a page using the control template

If a visitor is assigned to one of these tests but never meets the entry requirement, they won't be included in the test — and because of mutual exclusion, they also can't enter any other test in the group.

**Example:** Say you have 3 mutually exclusive Split URL tests. A visitor lands on your site and is randomly assigned to Split URL Test B. But they never visit the origin URL for that test — maybe they landed on a product page and checked out. Since they didn't meet the entry requirement, they're not counted in Test B. But because they were assigned to Test B exclusively, they also can't enter Test A or Test C, even if they would have met the entry requirements for those.

This can lead to some of your traffic not being included in any test, which may slow down how quickly you gather data.

**Best practice:** Mutually exclusive tests work best when the tests in your group have broad entry criteria — like shipping tests, or onsite edits tests — where visitors enter simply by landing on your site.
