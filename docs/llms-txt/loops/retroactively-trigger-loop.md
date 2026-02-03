# Source: https://loops.so/docs/guides/retroactively-trigger-loop.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrigger a Loop

> Backfill contacts into a loop.

<Warning>
  This is a temporary workaround while we build native backfill. The current
  flow is clunky and will get much better. Please still let us know you want
  native backfill so we can prioritize it.
</Warning>

## When to use this

* You have an existing loop that should have run for some contacts but didn’t.
* You’re comfortable exporting and re-importing a contact list.

## What you’ll do (high level)

1. Duplicate the original loop.
2. Create a one-off contact property (e.g., `backfill_welcome_sep2025`).
3. Change the duplicate loop’s trigger to “Contact updated” based on that property.
4. Start the duplicated loop.
5. Export the intended audience.
6. Add the property to the CSV for those contacts.
7. Re-import the CSV to update contacts and trigger the loop.

## Step-by-step

<Steps>
  <Step title="Duplicate the loop">
    Open the loop you want to retroactively trigger.

    Use **Duplicate** to create a copy. Rename it clearly (e.g., “Welcome Backfill (Sep 2025)”).
  </Step>

  <Step title="Create a one-off contact property">
    Add a new contact property to use exclusively for this backfill.

    **Example:**\
    Boolean: `backfill_welcome_sep2025` (true/false)

    Use a name that avoids collisions with any existing logic.
  </Step>

  <Step title="Change the duplicate loop’s trigger">
    Select “Contact updated” as the trigger.

    Set the criteria to:

    * was any
    * is equal to `true`

    <Tip>
      For one-off backfills, set Trigger frequency to <strong>One time</strong> so a
      contact only enters once.
    </Tip>
  </Step>

  <Step title="Export the intended audience from the original loop">
    From the main audience table, [export the contacts](/contacts/export-contacts) who should be backfilled.
  </Step>

  <Step title="Prepare the CSV for re-import">
    Open the CSV and add a new column with the property key you created.

    Populate that column with `true` for every row you want to trigger.

    Ensure the CSV still includes the primary identifier (either `email` or `userId`).
  </Step>

  <Step title="Re-import to update contacts and trigger">
    Import the CSV from the **Import** button on the [Audience page](https://app.loops.so/audience).

    Confirm the column mapping so your backfill property maps 1:1 to the new contact property.

    Set the CSV import to [trigger loops](/add-users/csv-upload#trigger-loops-via-csv) using the **Trigger Loops** toggle.

    Start the import.

    Your backfilled loop will begin triggering immediately.
  </Step>
</Steps>

<Warning>
  After the backfill completes, consider removing or resetting the temporary
  contact property to avoid accidental future triggers.
</Warning>
