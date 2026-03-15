# Source: https://docs.firehydrant.com/docs/template-variables.md

# Template Variables

FireHydrant uses the [Liquid templating language](https://shopify.github.io/liquid/basics/introduction/). A templating language allows you to set variables/placeholders that are replaced with actual data at execution time.

You can use template variables to reference many types of incident data, such as name and description, milestones, roles, user assignments, and more.

In FireHydrant, you can use template variables to dynamically interpolate FireHydrant incident data into multiple places, including:

* [Runbook steps](https://docs.firehydrant.com/docs/introduction-to-runbooks)
* [Jira field mappings](https://docs.firehydrant.com/docs/jira-cloud-integration)
* [Command Extensions](https://docs.firehydrant.com/docs/command-extensions)
* ...and more!

As an example, in a Runbook step, you can use an incident's name and description with `{{ incident.name }}` and `{{ incident.description }}` in the fields. When the Runbook step executes on a real incident, those placeholders will be filled with the actual name and description of the incident.

To minimize impact to your instance through repeated test incidents, **we recommend testing these template variables using the[Liquid playground](https://liquidjs.com/playground.html#I0ZpcmVIeWRyYW50IExpcXVpZCBFeGFtcGxlcwpEb2NzOiBodHRwczovL3Nob3BpZnkuZGV2L2FwaS9saXF1aWQKRm9yIG1vcmUgZXhhbXBsZXM6IGh0dHBzOi8vZ2l0aHViLmNvbS9maXJlaHlkcmFudC9saXF1aWQtdGVtcGxhdGUtZXhhbXBsZXMKCiMjQmFzaWMgRXhhbXBsZXMKSW5jaWRlbnQgbmFtZToge3tpbmNpZGVudC5uYW1lfX0KQ2hhbm5lbCBuYW1lOiB7e2luY2lkZW50LmNoYW5uZWxfbmFtZX19ClRhZ3MKICB7JS0gZm9yIHRhZyBpbiBpbmNpZGVudC50YWdfbGlzdCAlfQogICAgKiB7eyB0YWcgfX0KICB7JS0gZW5kZm9yICV9CkppcmEgVGlja2V0CiAgeyUtIGZvciB0aWNrZXQgaW4gaW5jaWRlbnQuaW5jaWRlbnRfdGlja2V0c1swXS5hdHRhY2htZW50cyAlfQogICAgKiB7eyB0aWNrZXQuZGlzcGxheV90ZXh0IH19IHwge3sgdGlja2V0LmhyZWZfdXJsIH19CiAgeyUtIGVuZGZvciAlfQpOb3RlOiBUaGUgJ3JldHJvJyBvYmplY3QgaXMgb25seSBhdmFpYWxibGUgYWZ0ZXIgYSByZXRyb3NwZWN0aXZlIGhhcyBiZWVuIHN0YXJ0ZWQgYW5kIGluIHRoZSBjb250ZXh0IG9mIGEgJ3JldHJvIGV4cG9ydCcgcnVuYm9vayBzdGVwLgoqIFJldHJvIHB1Ymxpc2hlZCBhdDoge3tyZXRyby5wdWJsaXNoZWRfYXR9fQ==,ewoJImluY2lkZW50IjogewoJCSJpZCI6ICJpbmNpZGVudF9pZCIsCgkJIm5hbWUiOiAiVGVzdCBJbmNpZGVudCIsCgkJImNyZWF0ZWRfYXQiOiAiMjAyMi0wNS0yMFQxNTo0Mjo0NC42MjlaIiwKCQkic3RhcnRlZF9hdCI6ICIyMDIyLTA1LTIwVDE1OjQyOjQ0LjcxOFoiLAoJCSJzdW1tYXJ5IjogIlN1bW1hcnkiLAoJCSJjdXN0b21lcl9pbXBhY3Rfc3VtbWFyeSI6IG51bGwsCgkJImRlc2NyaXB0aW9uIjogIkRlc2NyaXB0aW9uIiwKCQkiY3VycmVudF9taWxlc3RvbmUiOiAicmVzb2x2ZWQiLAoJCSJudW1iZXIiOiAxNjYsCgkJInByaW9yaXR5IjogIlA0IiwKCQkic2V2ZXJpdHkiOiAiU0VWMyIsCgkJInNldmVyaXR5X2ltcGFjdCI6IG51bGwsCgkJInNldmVyaXR5X2NvbmRpdGlvbiI6IG51bGwsCgkJInRhZ19saXN0IjogWwoJCQkidGFnMSIsICJ0YWcyIgoJCV0sCgkJInByaXZhdGVfaWQiOiAieHh4eHh4eCIsCgkJIm9yZ2FuaXphdGlvbl9pZCI6ICJvcmdfaWQiLAoJCSJpbmNpZGVudF9yb2xlcyI6IFtdLAoibWlsZXN0b25lcyI6IFsKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTA6MTkuNDQwWiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMDQ3WiIsCiJ0eXBlIjogInN0YXJ0ZWQiLAoib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQxMzoxMDoxOS4wMDBaIiwKImR1cmF0aW9uIjogbnVsbAp9LAp7CiJpZCI6ICJ1bmlxdWVfbWlsZXN0b25lX2lkIiwKImNyZWF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNDowNy4wNTJaIiwKInVwZGF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNDowNy4wODZaIiwKInR5cGUiOiAiZGV0ZWN0ZWQiLAoib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQxNDoxMzo1NS4wMDBaIiwKImR1cmF0aW9uIjogIlBUMUgzTTM2UyIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTA6MTkuNjg5WiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMDkyWiIsCiJ0eXBlIjogImFja25vd2xlZGdlZCIsCiJvY2N1cnJlZF9hdCI6ICIyMDIyLTA2LTA0VDE1OjEzOjU2LjAwMFoiLAoiZHVyYXRpb24iOiAiUFQxSDFTIgp9LAp7CiJpZCI6ICJ1bmlxdWVfbWlsZXN0b25lX2lkIiwKImNyZWF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNDowNy4wNjVaIiwKInVwZGF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNDowNy4wOThaIiwKInR5cGUiOiAiaW52ZXN0aWdhdGluZyIsCiJvY2N1cnJlZF9hdCI6ICIyMDIyLTA2LTA0VDE2OjEzOjU2LjAwMFoiLAoiZHVyYXRpb24iOiAiUFQxSCIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMDcwWiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMTA0WiIsCiJ0eXBlIjogImlkZW50aWZpZWQiLAoib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQxNzoxMzo1Ny4wMDBaIiwKImR1cmF0aW9uIjogIlBUMUgxUyIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMDc1WiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMTEwWiIsCiJ0eXBlIjogIm1pdGlnYXRlZCIsCiJvY2N1cnJlZF9hdCI6ICIyMDIyLTA2LTA0VDE4OjEzOjU4LjAwMFoiLAoiZHVyYXRpb24iOiAiUFQxSDFTIgp9LAp7CiJpZCI6ICJ1bmlxdWVfbWlsZXN0b25lX2lkIiwKImNyZWF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNzoxMi4zNTZaIiwKInVwZGF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNzoxMi4zODNaIiwKInR5cGUiOiAicmVzb2x2ZWQiLAoib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNzoxMi4zNDdaIiwKImR1cmF0aW9uIjogIlBUNEgzTTE0UyIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTg6NDAuMzQwWiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTg6NDAuMzcwWiIsCiJ0eXBlIjogInBvc3Rtb3J0ZW1fc3RhcnRlZCIsCiJvY2N1cnJlZF9hdCI6ICIyMDIyLTA2LTA0VDIyOjE4OjQwLjMzM1oiLAoiZHVyYXRpb24iOiAiUFQxTTI3UyIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MzI6NTMuNTIwWiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MzI6NTMuNTY0WiIsCiJ0eXBlIjogInBvc3Rtb3J0ZW1fY29tcGxldGVkIiwKIm9jY3VycmVkX2F0IjogIjIwMjItMDYtMDRUMjI6MzI6NTMuNTA5WiIsCiJkdXJhdGlvbiI6ICJQVDE0TTEzUyIKfQpdLAoJCSJhY3RpdmUiOiB0cnVlLAoJCSJsYWJlbHMiOiB7fSwKCQkicm9sZV9hc3NpZ25tZW50cyI6IFtdLAoJCSJzdGF0dXNfcGFnZXMiOiBbXSwKCQkiaW5jaWRlbnRfdXJsIjogImh0dHBzOi8vYXBwLmZpcmVoeWRyYW50LmlvL2luY2lkZW50cy9pbmNpZGVudF9pZC9pbmNpZGVudC9vdmVydmlldyIsCgkJInByaXZhdGVfc3RhdHVzX3BhZ2VfdXJsIjogImh0dHBzOi8vYXBwLmZpcmVoeWRyYW50LmlvL2luY2lkZW50cy9pbnRlcm5hbC9zdGF0dXNfcGFnZS8zMTk3MDgyNi14eHh4LXh4eHgteHh4eC04ZTU5ZTJiNzI5MzUveHh4eHgiLAoJCSJvcmdhbml6YXRpb24iOiB7CgkJCSJuYW1lIjogIlRlc3QgQWNjb3VudCIsCgkJCSJpZCI6ICJvcmdfaWQiCgkJfSwKCQkiY3VzdG9tZXJzX2ltcGFjdGVkIjogMCwKCQkibW9uZXRhcnlfaW1wYWN0IjogbnVsbCwKCQkibW9uZXRhcnlfaW1wYWN0X2NlbnRzIjogbnVsbCwKCQkibGFzdF91cGRhdGUiOiBudWxsLAoJCSJsYXN0X25vdGUiOiBudWxsLAoJCSJyZXBvcnRfaWQiOiBudWxsLAoJCSJzZXJ2aWNlcyI6IFt7CgkJCSJuYW1lIjogImZpc2giLAoJCQkiaWQiOiAic3R1ZmYiCgkJfV0sCgkJImVudmlyb25tZW50cyI6IFtdLAoJCSJmdW5jdGlvbmFsaXRpZXMiOiBbXSwKCQkiY2hhbm5lbF9uYW1lIjogImluY2lkZW50LTE2NiIsCgkJImNoYW5uZWxfcmVmZXJlbmNlIjogIjwjQzAzR0M1U0tENUh8aW5jaWRlbnQtMTY2PiIsCgkJImNoYW5uZWxfaWQiOiAiQzAzR0M1U0tENUgiLAoJCSJjaGFubmVsX3N0YXR1cyI6ICJvcGVyYXRpb25hbCIsCgkJImluY2lkZW50X3RpY2tldHMiOiBbewoJCQkiaWQiOiAidGlja2V0X2lkIiwKCQkJInN1bW1hcnkiOiAiVGVzdCBjcmVhdGVkIGluIHVpIiwKCQkJImRlc2NyaXB0aW9uIjogIkRlc2NyaXB0aW9uIiwKCQkJInN0YXRlIjogImluX3Byb2dyZXNzIiwKCQkJInR5cGUiOiAiaW5jaWRlbnQiLAoJCQkiYXNzaWduZWVzIjogW10sCgkJCSJjcmVhdGVkX2J5IjogewoJCQkJImlkIjogInVzZXJfaWQiLAoJCQkJIm5hbWUiOiAiSm9obiBTbWl0aCIsCgkJCQkic291cmNlIjogImZpcmVoeWRyYW50X3VzZXIiLAoJCQkJImVtYWlsIjogImpzbWl0aEBnbWFpbC5jb20iCgkJCX0sCgkJCSJhdHRhY2htZW50cyI6IFt7CgkJCQkidHlwZSI6ICJsaW5rIiwKCQkJCSJkaXNwbGF5X3RleHQiOiAiWFhYLTEwMjIiLAoJCQkJImhyZWZfdXJsIjogImh0dHBzOi8vY29tcGFueS5hdGxhc3NpYW4ubmV0L2Jyb3dzZS9YWFgtMTAyMiIsCgkJCQkiaWNvbl91cmwiOiAiaHR0cHM6Ly9hcHAuY29tcGFueS5pby8vaW50ZWdyYXRpb25zLWFzc2V0cy9qaXJhX2Nsb3VkL2Zhdmljb24ucG5nIgoJCQl9XQoJCX1dLAoJCSJpbXBhY3RzIjogW10sCgkJImNvbmZlcmVuY2VfYnJpZGdlcyI6IFtdLAoJCSJpbmNpZGVudF9jaGFubmVscyI6IFt7CgkJCSJpZCI6ICJDMDNHQzVTS0Q1SCIsCgkJCSJuYW1lIjogImluY2lkZW50LTE2NiIsCgkJCSJzb3VyY2UiOiAic2xhY2siLAoJCQkic291cmNlX25hbWUiOiAiU2xhY2siLAoJCQkic291cmNlX2lkIjogInNvdXJjZV9pZCIsCgkJCSJ1cmwiOiAiaHR0cHM6Ly9maHRlc3RhY2NvdW50LnNsYWNrLmNvbS9tZXNzYWdlcy9DMDNHQzVTS0Q1SCIsCgkJCSJpY29uX3VybCI6ICJodHRwczovL2FwcC5maXJlaHlkcmFudC5pby8vaW50ZWdyYXRpb25zLWFzc2V0cy9zbGFjay9mYXZpY29uLnBuZyIsCgkJCSJzdGF0dXMiOiAib3BlcmF0aW9uYWwiCgkJfV0sCgkJInJldHJvX2V4cG9ydHMiOiBbXSwKCQkiY3JlYXRlZF9ieSI6IHsKCQkJImlkIjogInVzZXJfaWQiLAoJCQkibmFtZSI6ICJKb2UgU21pdGgiLAoJCQkic291cmNlIjogImZpcmVoeWRyYW50X3VzZXIiLAoJCQkiZW1haWwiOiAiam9lX3NtaXRoQGdtYWlsLmNvbSIKCQl9LAoJCSJjb250ZXh0X29iamVjdCI6IG51bGwsCgkJInJlc3RyaWN0ZWQiOiBmYWxzZSwKCQkiZXhwbGljaXRfb3JnYW5pemF0aW9uX3VzZXJfaWRzIjogW10KCX0sCgoKCSJyZXRybyI6IHsKICAgICJuYW1lIjogIlRlc3QgSW5jaWRlbnQiLAogICAgInB1Ymxpc2hlZF9hdCI6ICIyMDIyLTA2LTA0VDE5OjE1OjU2LjAwOFoiLAoJCSJxdWVzdGlvbnMiOiBbewoJCQkidGl0bGUiOiAidGl0bGUiLAoJCQkiYm9keSI6ICJib2R5IiwKCQkJInVwZGF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQxOToxNTo1Ni4wMDhaIgoJCX1dLAoJCSJjb250cmlidXRpbmdfZmFjdG9ycyI6IFt7CgkJCSJzdW1tYXJ5IjogInN1bW1hcnkiLAoJCQkicG9zaXRpb24iOiAicG9zaXRpb24iLAoJCQkiY3JlYXRlZF9ieSI6ICJKYW5lIFNtaXRoIDxKYW5lU21pdGhAZ21haWwuY29tPiIKCQl9XSwKCQkiaW5jaWRlbnRfcm9sZXMiOiBbewoJCQkibmFtZSI6ICJyb2xlIG5hbWUiLAoJCQkiZGVzY3JpcHRpb24iOiAiUm9sZSBEZXNjcmlwdGlvbiIsCgkJCSJ1c2VyIjogIkphbmUgU21pdGggPEphbmVTbWl0aEBnbWFpbC5jb20+IiwKCQkJInN0YXR1cyI6ICJzdGF0dXMiCgkJfV0sCgkJImluY2lkZW50X2FjdGl2ZV9kdXJhdGlvbiI6ICIyMDIyLTA2LTA0VDE5OjE1OjU2LjAwOFoiLAoJCSJpbXBhY3RzIjogW3sKCQkJInR5cGUiOiAiaW1wYWN0IHR5cGUiLAoJCQkibmFtZSI6ICJpbXBhY3QgbmFtZSIsCgkJCSJzZXZlcml0eSI6ICJTRVYzIiwKCQkJImNvbmRpdGlvbiI6ICJjb25kaXRpb24gbmFtZSIKCQl9XSwKCgkJInN0YXJyZWRfZXZlbnRzIjogW3sKCQkJIm9jY3VycmVkX2F0IjogIjIwMjItMDYtMDRUMTk6MTU6NTYuMDA4WiIsCgkJCSJjcmVhdGVkX2J5IjogIkphbmUgU21pdGggPEphbmVTbWl0aEBnbWFpbC5jb20+IiwKCQkJImJvZHkiOiAiU3RhcnRlZCBFdmVudCBUZXh0IgoJCX1dLAoJCSJtaWxlc3RvbmVzIjogW3sKCQkJInR5cGUiOiAic3RhcnRlZCIsCgkJCSJkdXJhdGlvbiI6ICIyMDIyLTA2LTA0VDE5OjE1OjU2LjAwOFoiLAoJCQkib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQxOToxNTo1Ni4wMDhaIgoJCX1dCgl9Cn0=).** Additionally, you can check out our liquid template examples in [this GitHub repo](https://github.com/firehydrant/liquid-template-examples).

Runbook steps now also feature an output preview, where you can select previous incidents as example data to preview how your templating would have looked:

<Image alt="Liquid/JSON preview on a Runbook step" align="center" width="650px" src="https://files.readme.io/1e60834-image.png">
  Liquid/JSON preview on a Runbook step
</Image>

## Incident Fields and Variables

This list includes the properties in the FireHydrant API that are most often used as template variables. To see **all available FireHydrant incident properties** refer to the [IncidentEntity](https://developers.firehydrant.com/#/schemas/IncidentEntity) model (for incident data) and [PostmortemReportEntity](https://developers.firehydrant.com/#/schemas/PostMortems_PostMortemReportEntity) model (for retrospective data).

All left-most fields are accessible under the main `incident` object with `{{ incident.VAR }}`, where `VAR` is the name of the field. Visit the sections in the table of contents to the right to see each section's available variables.

### General Incident Fields

| Key                       | Type       | Description                                                                                                                         |
| :------------------------ | :--------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| `active`                  | `boolean`  | Whether the incident is still ongoing (`true` when in any milestone prior to resolved or post-incident phase)                       |
| `ai_incident_summary`     | `string`   | AI-generated summary of the incident (requires [AI features enabled](https://docs.firehydrant.com/docs/ai-powered-incident-summaries) )                           |
| `created_at`              | `datetime` | UTC time when the incident was created in ISO 8601 format                                                                           |
| `created_by`              | `object`   | Object representing the user who declared the incident. For additional                                                              |
| ↳ `email`                 | `string`   | Email address of the user who declared                                                                                              |
| ↳ `id`                    | `string`   | UUID representing the user who declared the incident                                                                                |
| ↳ `name`                  | `string`   | Name of the user who declared the incident                                                                                          |
| ↳ `source`                | `string`   | Where the user declared the incident, for example `firehydrant_user` (web interface) or `slack`                                     |
| `customer_impact_summary` | `string`   | A description or summary of the customer impact                                                                                     |
| `description`             | `string`   | A more detailed description of the incident                                                                                         |
| `id`                      | `string`   | UUID representing the incident                                                                                                      |
| `incident_url`            | `string`   | URL for the incident page in the web UI                                                                                             |
| `last_note`               | `object`   | Object representing the very latest update and the time it was posted                                                               |
| ↳ `body`                  | `string`   | Most recent incident update note                                                                                                    |
| ↳ `created_at`            | `datetime` | UTC timestamp of when the latest note was posted                                                                                    |
| `last_update`             | `string`   | The same as `last_note.body`                                                                                                        |
| `links`                   | `object`   | Array of links on the incident                                                                                                      |
| ↳ `text`                  | `string`   | The label/title for the link                                                                                                        |
| ↳ `url`                   | `string`   | URL of the link                                                                                                                     |
| `name`                    | `string`   | Name of the incident                                                                                                                |
| `number`                  | `integer`  | Incident number auto-assigned by FireHydrant. This number automatically increments with each incident created and cannot be changed |
| `organization`            | `object`   | Object representing the organization this incident was opened in                                                                    |
| ↳ `id`                    | `string`   | UUID representing the organization                                                                                                  |
| ↳ `name`                  | `string`   | Name of the organization                                                                                                            |
| `organization_id`         | `string`   | The same as `organization.id`                                                                                                       |
| `private_id`              | `string`   | Private ID of the incident's [internal status page](https://docs.firehydrant.com/docs/internal-status-pages)                                                      |
| `recent_updates`          | `object[]` | Array of recent update objects                                                                                                      |
| ↳ `body`                  | `string`   | Most recent incident update note                                                                                                    |
| ↳ `timestamp`             | `string`   | ISO 8601 timestamp of when the note was made                                                                                        |
| `report_id`               | `string`   | UUID for the retrospective report. This value is only populated if the incident is `resolved`.                                      |
| `retro_exports`           | `object[]` | Array of objects representing all of the retrospective exports (e.g., Confluence, Google Docs, etc.)                                |
| ↳ `created_at`            | `datetime` | UTC time of when the export was created in ISO 8601 format                                                                          |
| ↳ `display_text`          | `string`   | Title of the exported document                                                                                                      |
| ↳ `href_url`              | `string`   | URL of the exported document                                                                                                        |
| ↳ `icon_url`              | `string`   | URL of the destination application's icon                                                                                           |
| ↳ `id`                    | `string`   | UUID for the export                                                                                                                 |
| `severity`                | `string`   | Current [severity](https://docs.firehydrant.com/docs/severities-and-priorities) of the incident                                                                   |
| `started_at`              | `datetime` | UTC time of when an incident was started/declared in ISO 8601 format                                                                |
| `tag_list`                | `string[]` | Array of tags attached to the incident                                                                                              |

### Milestone and Lifecycle Fields

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `current_lifecycle`
      </td>

      <td>
        `string`
      </td>

      <td>
        The current lifecycle phase of the incident. See [Incident Milestones & Lifecycle Phases](https://docs.firehydrant.com/docs/incident-milestones-lifecycle-phases).
      </td>
    </tr>

    <tr>
      <td>
        `current_lifecycle_milestone`
      </td>

      <td>
        `object`
      </td>

      <td>
        The current milestone. See [Incident Milestones & Lifecycle Phases](https://docs.firehydrant.com/docs/incident-milestones-lifecycle-phases).

        * \*Note\*\*: This is preferred over `current_milestone`, as it contains other pertinent details.
      </td>
    </tr>

    <tr>
      <td>
        ↳ `id`
      </td>

      <td>
        `string`
      </td>

      <td>
        UUID of the milestone
      </td>
    </tr>

    <tr>
      <td>
        ↳ `name`
      </td>

      <td>
        `string`
      </td>

      <td>
        The name of the milestone
      </td>
    </tr>

    <tr>
      <td>
        ↳ `description`
      </td>

      <td>
        `string`
      </td>

      <td>
        The description of the milestone
      </td>
    </tr>

    <tr>
      <td>
        ↳ `slug`
      </td>

      <td>
        `string`
      </td>

      <td>
        The slug of the milestone (equivalent to `current_milestone` today)
      </td>
    </tr>

    <tr>
      <td>
        ↳ `position`
      </td>

      <td>
        `integer`
      </td>

      <td>
        The milestone's order number in the list (0-based)
      </td>
    </tr>

    <tr>
      <td>
        ↳ `created_by`
      </td>

      <td>
        `object`
      </td>

      <td>
        The user who created the milestone. See `created_by` above for the same keys/values.
      </td>
    </tr>

    <tr>
      <td>
        ↳ `updated_by`
      </td>

      <td>
        `object`
      </td>

      <td>
        The user who created the milestone. See `created_by` above for the same keys/values.
      </td>
    </tr>

    <tr>
      <td>
        `current_milestone`
      </td>

      <td>
        `string`
      </td>

      <td>
        The slug of the current <Glossary>Milestone</Glossary> that the incident is in. See [Incident Milestones & Lifecycle Phases](https://docs.firehydrant.com/docs/incident-milestones-lifecycle-phases).

        * \*Note\*\*: It is recommend to use `current_lifecycle_milestone` instead.
      </td>
    </tr>

    <tr>
      <td>
        `milestones`
      </td>

      <td>
        `object[]`
      </td>

      <td>
        Array of objects representing each time the incident transitioned milestones
      </td>
    </tr>

    <tr>
      <td>
        ↳ `created_at`
      </td>

      <td>
        `datetime`
      </td>

      <td>
        UTC timestamp of when the milestone was set
      </td>
    </tr>

    <tr>
      <td>
        ↳ `duration`
      </td>

      <td>
        `string`
      </td>

      <td>
        Measure of the milestone's duration in seconds, printed in the format of `P[months]M[days]DT[hours]H[minutes]M[seconds]S`
      </td>
    </tr>

    <tr>
      <td>
        ↳ `id`
      </td>

      <td>
        `string`
      </td>

      <td>
        UUID of the milestone transition
      </td>
    </tr>

    <tr>
      <td>
        ↳ `occurred_at`
      </td>

      <td>
        `datetime`
      </td>

      <td>
        UTC timestamp of the milestone
      </td>
    </tr>

    <tr>
      <td>
        ↳ `type`
      </td>

      <td>
        `string`
      </td>

      <td>
        The milestone, represented by its slug
      </td>
    </tr>

    <tr>
      <td>
        ↳ `updated_at`
      </td>

      <td>
        `datetime`
      </td>

      <td>
        UTC timestamp of when the milestone was last updated
      </td>
    </tr>
  </tbody>
</Table>

### Role and User Assignment Fields

| Key                | Type       | Description                                                                                                                                                                                               |
| :----------------- | :--------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `role_assignments` | `object[]` | Array of objects containing the assigned users and their roles                                                                                                                                            |
| ↳ `created_at`     | `datetime` | UTC timestamp for when the role was assigned                                                                                                                                                              |
| ↳ `id`             | `string`   | UUID for the assignment                                                                                                                                                                                   |
| ↳ `incident_role`  | `object`   | Object representing the incident role that the user was assigned to. For the full list of available parameters, see [IncidentRoleEntity](https://developers.firehydrant.com/#/schemas/IncidentRoleEntity) |
| ↳ `status`         | `string`   | Current status of this role assignment (`active` or `inactive`)                                                                                                                                           |
| ↳`updated_at`      | `datetime` | UTC timestamp for when the role assignment was updated                                                                                                                                                    |
| ↳ `user`           | `object`   | Object representing the user for this assignment. For the full list of available parameters, see [UserEntity](https://developers.firehydrant.com/#/schemas/UserEntity)                                    |
| `team_assignments` | `object[]` | Array of objects containing the assigned teams                                                                                                                                                            |
| ↳ `created_at`     | `datetime` | UTC timestamp of when the team assignment occurred                                                                                                                                                        |
| ↳ `id`             | `string`   | UUID for the assignment (not the team's ID)                                                                                                                                                               |
| ↳ `status`         | `string`   | Current status of the team assignment (`active` or `inactive`)                                                                                                                                            |
| ↳ `team`           | `object`   | Object representing the team that was assigned. For the full list of available parameters, see [TeamEntity](https://developers.firehydrant.com/#/schemas/TeamEntity)                                      |
| ↳ `updated_at`     | `datetime` | UTC timestamp for when the team assignment was last updated                                                                                                                                               |

### Custom Fields

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `custom_fields`
      </td>

      <td>
        `object{}`
      </td>

      <td>
        Object containing custom field objects keyed by their slugs (for example, `incident.custom_fields.deployment_silo`)
      </td>
    </tr>

    <tr>
      <td>
        ↳ `display_name`
      </td>

      <td>
        `string`
      </td>

      <td>
        The human-friendly display name for the custom field
      </td>
    </tr>

    <tr>
      <td>
        ↳ `field_id`
      </td>

      <td>
        `string`
      </td>

      <td>
        UUID representing the field
      </td>
    </tr>

    <tr>
      <td>
        ↳ `slug`
      </td>

      <td>
        `string`
      </td>

      <td>
        Unique, humanized identifier for the field
      </td>
    </tr>

    <tr>
      <td>
        ↳ `value`
      </td>

      <td>
        `string`
      </td>

      <td>
        String value for the field that varies in content.

        * If `value_type` = `array`, this field will be a string with all array values joined by a comma
        * If `value_type` = `string`, this will just be the specified string or chosen value
        * If `value_type` = `datetime`, this will be an ISO 8601 string of the date and time
      </td>
    </tr>

    <tr>
      <td>
        ↳ `value_array`
      </td>

      <td>
        `string[]`
      </td>

      <td>
        Array of chosen values. Only exists if `value_type` = `array`
      </td>
    </tr>

    <tr>
      <td>
        ↳ `value_string`
      </td>

      <td>
        `string`
      </td>

      <td>
        Value of the custom field. Only exists if `value_type` = `string`
      </td>
    </tr>

    <tr>
      <td>
        ↳ `value_type`
      </td>

      <td>
        `string`
      </td>

      <td>
        Type of the custom field (`string`, `array`, `datetime`)
      </td>
    </tr>
  </tbody>
</Table>

Custom field attributes (e.g., *display\_name*, *value*) can be accessed directly by slug name or can be iterated using Liquid's *for* loop, which will return each custom field as an object.

```jsx Custom Fields Liquid Example
## Accessing the value of custom field by slug
{{ incident.custom_fields.slug.value }}

## Iterating over all custom fields to display the name and the value
{% for field in incident.custom_fields %}
  {{ field.name }}
  {{ field.value }}
{% endfor %}
```

### Audiences

| Key         | Type       | Description                                                                                                                     |
| :---------- | :--------- | :------------------------------------------------------------------------------------------------------------------------------ |
| `audiences` | `object{}` | Object containing audience objects keyed by their slugs (for example, `incident.audiences.executive-team`)                      |
| ↳ `content` | `string`   | The content of the given summary for that audience                                                                              |
| ↳ `details` | `object{}` | Object containing detail objects keyed by their slugs (for example, `incident.audiences.executive-team.details.current-impact`) |
| ↳ `content` | `string`   | The content of the given detail for the specified audience                                                                      |

### Service Catalog Fields

| Key               | Type       | Description                                                                                                                                                                                                                                |
| :---------------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `services`        | `object[]` | Array of Service objects containing key parameters                                                                                                                                                                                         |
| ↳ `id`            | `string`   | UUID of the service                                                                                                                                                                                                                        |
| ↳ `name`          | `string`   | Name of the service                                                                                                                                                                                                                        |
| ↳ `labels`        | `object{}` | Object containing the key:value pairs of all the labels for the service.                                                                                                                                                                   |
| ↳ ↳ `{KEY}`       | `string`   | Whatever labels you've configured for a service. For example, if you have a label called `region` with value `us-east-1`, then you would access this via `*.labels.region` or `*.labels['region']` and these will return `us-east-1`       |
| `functionalities` | `object[]` | Array of Functionality objects containing key parameters                                                                                                                                                                                   |
| ↳ `id`            | `string`   | UUID of the functionality                                                                                                                                                                                                                  |
| ↳ `name`          | `string`   | Name of the functionality                                                                                                                                                                                                                  |
| ↳ `labels`        | `object{}` | Object containing the key:value pairs of all the labels for the functionality                                                                                                                                                              |
| ↳ ↳ `{KEY}`       | `string`   | Whatever labels you've configured for a functionality. For example, if you have a label called `region` with value `us-east-1`, then you would access this via `*.labels.region` or `*.labels['region']` and these will return `us-east-1` |
| `environments`    | `object[]` | Array of Environment objects containing key parameters                                                                                                                                                                                     |
| ↳ `id`            | `string`   | UUID of the environment                                                                                                                                                                                                                    |
| ↳ `name`          | `string`   | Name of the environment                                                                                                                                                                                                                    |
| `impacts`         | `object[]` | Array of impact objects                                                                                                                                                                                                                    |
| ↳ `id`            | `string`   | UUID of the noted impact/instance. **Note**: This is ***not*** the UUID of the component itself (e.g., a service or functionality). For that, see below under `impact`                                                                     |
| ↳ `type`          | `string`   | One of `service`, `functionality`, or `environment`                                                                                                                                                                                        |
| ↳ `impact`        | `object{}` | Object containing the impacted component                                                                                                                                                                                                   |
| ↳ ↳ `id`          | `string`   | UUID of the impacted component                                                                                                                                                                                                             |
| ↳ ↳ `name`        | `string`   | Name of the impacted component                                                                                                                                                                                                             |
| ↳ `condition`     | `object{}` | Object containing the impacted component's condition                                                                                                                                                                                       |
| ↳ ↳ `id`          | `string`   | UUID of the condition                                                                                                                                                                                                                      |
| ↳ ↳ `name`        | `string`   | Name of the condition (e.g., `unavailable`, `degraded`, etc.). This is customizable.                                                                                                                                                       |
| `change_events`   | `object[]` | Array of change event objects                                                                                                                                                                                                              |
| ↳ `id`            | `string`   | UUID of the change event                                                                                                                                                                                                                   |
| ↳ `summary`       | `string`   | Summary or title of the change event                                                                                                                                                                                                       |
| ↳ `services`      | `object[]` | Array of objects detailing the services impacted by this change event                                                                                                                                                                      |
| ↳ ↳ `id`          | `string`   | UUID of the modified service                                                                                                                                                                                                               |
| ↳ ↳ `name`        | `string`   | Name of the modified service                                                                                                                                                                                                               |
| ↳ `environments`  | `object[]` | Array of objects detailing the environments impacted by this change event                                                                                                                                                                  |
| ↳ ↳ `id`          | `string`   | UUID of the modified environment                                                                                                                                                                                                           |
| ↳ ↳ `name`        | `string`   | Name of the modified environment                                                                                                                                                                                                           |
| ↳ `started_at`    | `string`   | Datetime of when the change event occurred                                                                                                                                                                                                 |
| ↳ `impact`        | `string`   | One of `suspect`, `caused`, `fixed`, `dismissed`                                                                                                                                                                                           |

### Tasks/Follow-Ups

* `tasks` or `follow_ups` *(array of objects)*: List of tasks or follow-ups created on the incident. Tasks and follow-ups use the same data model, but some parameters will not be relevant depending on the type. See below.
  * `id`: FireHydrant UUID for this task/follow-up
  * `summary`: Title/summary
  * `description`: The description. Always `null` for Tasks.
  * `state`: The current state of the task/follow-up. Possible values are `open`, `in_progress`, `cancelled`, and `done`
  * `type`: `task` or `follow_up`
  * `assignees` *(array of objects)*: Who's assigned to the task/follow-up
    * `id`: FireHydrant UUID for the user
    * `name`: User's name
    * `source`: `firehydrant_user`, `bot_user`, or `patchy`. For Follow-Ups, will basically always be `firehydrant_user`
    * `email`: User's email address
  * `priority`: The priority, defined in **Settings** > **Ticketing settings**. Always `null` for Tasks.
  * `created_by` *(object)*: Who created the task/follow-up
    * `id`: FireHydrant UUID for the user
    * `name`: User's name
    * `source`: `firehydrant_user`, `bot_user`, or `patchy`. For Follow-Ups, will basically always be `firehydrant_user`
    * `email`: User's email address
  * `attachments` *(object)*: Any links or other attachments. Always an empty array for Tasks.
    * `id`: UUID for the link attachment. Generally not used/needed for anything
    * `type`: Usually `link`
    * `display_text`: External link's display text/title
    * `href_url`: The URL for the external link
    * `icon_url`: Link to the icon FireHydrant uses for the integration
    * `editable`:  Always `false`
    * `deletable`: Always `false`
  * `created_at`: ISO 8601 datetime representing when the ticket was created
  * `updated_at`: ISO 8601 datetime representing when the ticket was last updated
  * `tag_list` *(array of strings)*: List of ticketing tags (not to be confused with incident tags). Always empty for Tasks.
  * `incident_id`: FireHydrant UUID of the incident this task/follow-up was created for
  * `due_at`: ISO 8601 format datetime of when the Task is due. Currently not supported for follow-ups.
  * `link`: Linked external resource, usually a project ticket for follow-ups. Always empty for Tasks.
    * `id`: FireHydrant UUID for the attachment
    * `type`: Always `link`
    * `display_text`: The ticket's code (e.g., "ABC-123")
    * `href_url`: The URL to the external ticket
    * `icon_url`: Link to the icon FireHydrant uses for the integration
    * `editable`:  Always `false`
    * `deletable`: Always `false`

### Integrations-Related Fields

* `channel_name`: The name of the Slack channel for the incident.

* `channel_reference`: The Slack-formatted encoded link for the Slack channel. You can use this reference number in a Slack message to create a link to the incident channel.

* `channel_id`: The Slack ID for the channel (not formatted for creating links).

* `channel_status`: Indicates whether the Slack channel is operational.

* `private_status_page_url`: The url of the private status page for the incident.

* `incident_tickets`\*\* *(array of objects)*:

  * `id`: The incident ticket ID.

  * `summary`: Summary of information in the ticket.

  * `Description`: Description of the incident as provided in the ticket.

  * `state`: State of the ticket: **open** , **in\_progress** , **done** , etc.

  * `type`: Ticket type: **Incident** , **follow\_up** , or **task**.

  * `assignees`: The incident ticket ID.

  * `created_by` *(object)*: 

    * `id`: ID of the user who created the ticket.

    * `name`: Name of the user who created the ticket.

    * `source`: Ticketing source: **Slack** , **PagerDuty** , **FireHydrant** , etc.

    * `email`: Email address for the user who created the ticket.

  * `attachments` *(array of objects)*:

    * `display_text`: The text displayed that links to the ticket.

    * `href_url`: The URL for the ticket.

    * `icon_url`: The URL for the icon of the ticketing provider.

    * `type`: The type of ticket.

> 📘 Note:
>
> At this time, only the incident ticket is included in this array of objects, not Tasks or Follow-Ups.

Alternatively, you may  use `ticket`, which is the only ticket of type: **Incident**, and also supports any of the attributes above. This `ticket` object has the following attributes:

* `ticket` *(object)*: Singular object containing the incident ticket

  * `link`: The reference to a corresponding external integration ticket or issue

    * `display_text`: The text displayed that links to the ticket.

    * `href_url`: The URL for the ticket.

    * `icon_url`: The URL for the icon of the ticketing provider.

    * `type`: The type of ticket; in this case, it's always *"link"*

* `conference_bridges` *(array of objects)*:

  * `id`: UUID of the conference object as stored on FireHydrant (not the Zoom/Google Meet ID)

  * `attachments` *(array of objects)*:

    * `type`: Attachment type: image, alert, etc.

    * `display_text`: The text displayed describes the conference bridge.

    * `href_url`: The URL for the conference bridge (for example, `https://us02web.zoom.us/j/1234567890`)

    * `icon_url`: The URL for the icon of the conference bridge provider.

* `incident_channels` *(array of objects)*: List of channels attached to the incident
  * `id`: Slack ID for the channel
  * `name`: The name of the channel
  * `source`: The originating source of the channel (e.g. `slack`)
  * `url`: The URL for the channel
  * `icon_url`: URL for the source/channel's icon

### Retrospective Fields

The `retro` data object is only available after an incident has moved to the 'retrospective started' milestone. This object can be directly referenced like an incident, for example,`{{ retro.name }}`.

* `retro` *(object)*:

  * `name`: The name of the report

  * `published_at`: When the retro was completed

  * `questions` *(array of objects)*: An array of custom questions set from the Retrospective Configuration tab

    * `title`: The title of the question

    * `body`: The answer to the question

    * `updated_at`: When the question was last updated

  * `contributing_factors` *(array of objects)*: An array of the Five Whys section in contributing factors

    * `summary`: The content of the contributing factor

    * `position`: The position in the list of Five Whys

  * `incident_active_duration`: The duration that the incident was in an active state. Active is defined as the Started through Mitigated milestone

  * `starred_events` *(array of objects)*: An array of the starred events from the incident

    * `occurred_at`: When the event occurred

    * `created_by`: Who created the event

    * `summary`: The content of the contributing factor

    * `body`: The content of the event

## Special FireHydrant Liquid Variables and Filters

Liquid templating is a general templating system, but it does allow for the creation of custom filters, functions, and more. The following is a list of custom FireHydrant Liquid variables/functions that you can use:

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Value
      </th>

      <th>
        Type
      </th>

      <th>
        Usage
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `toJSON`
      </td>

      <td>
        **Function**
      </td>

      <td>
        `{{ some_variable \| toJSON }}`
      </td>

      <td>
        Prints the specified variable/object in JSON. Useful for debugging
      </td>
    </tr>

    <tr>
      <td>
        `date_pt`\
        `date_mt`\
        `date_ct`\
        `date_et`\
        `date_utc`
      </td>

      <td>
        **Variable**
      </td>

      <td>
        `incident-my_inc-{{ date_pt }}`
      </td>

      <td>
        Convenient variables for getting the current date (YYYY-MM-DD) according to US timezones.

        * \*Note\*\*: Only available in [Create or rename Incident Slack channel](https://docs.firehydrant.com/docs/runbook-step-create-or-rename-incident-slack-channel) Runbook step
      </td>
    </tr>
  </tbody>
</Table>

## Cookbook

The following section contains examples of using Liquid templating to interpolate incident data.

### Slack Channel URL

* **Summary**: Get the URL to the Slack channel and display the link using markdown.
* **Usage**: Any external comms step, like **Notify with Custom Message** or **Email**, etc., where you want to link to the incident Slack channel.

```jsx Liquid
[Incident Channel]({{ incident.incident_channels[0].url }})
```

### Confluence Retro Additions

* **Summary**: Display Tags, Labels, and Jira tickets in Confluence export
* **Usage**: Add to the **Export to Confluence** runbook step

```jsx Liquid
### Tags

| Tags      |
|-----------|
{%- for tag in incident.tag_list %}
| {{ tag }} |
{%- endfor %}

### Labels

| Key | Value |
|-----|-------|
{%- for label in incident.labels %}
| {{ label[0] }} | {{ label[1] }} |
{%- endfor %}

### Jira

| Ticket Name | Link |
|-------------|------|
{%- for ticket in incident.incident_tickets[0].attachments %}
| {{ ticket.display_text }} | {{ ticket.href_url }} |
{%- endfor %}
```

### Print Duration of Incident

* **Summary**: Return the current or total duration of the incident. Calculates from **Resolved** milestone or `now` if the incident is still open.
* **Usage**: Custom message to channel or email runbook steps

```jsx Liquid
{% assign started = incident.milestones | where: "type", "started" | first %}
{% assign started_at = started.occurred_at | date: "%s" %}

{% assign resolved = incident.milestones | where: "type", "resolved" | first %}
{% if resolved %}
  {% assign resolved_at_or_now = resolved.occurred_at | date: "%s" %}
{% else %}
  {% assign resolved_at_or_now = "now" | date: "%s" %}
{% endif %}

{% assign SECONDS_PER_MINUTE = 60 %}
{% assign SECONDS_PER_HOUR = SECONDS_PER_MINUTE | times: 60 %}
{% assign SECONDS_PER_DAY = SECONDS_PER_HOUR | times: 24 %}

{% assign remainder = resolved_at_or_now | minus: started_at | modulo: SECONDS_PER_DAY %}
{% assign days = resolved_at_or_now | minus: started_at | divided_by: SECONDS_PER_DAY | floor %}

{% assign hours = remainder | divided_by: SECONDS_PER_HOUR | floor %}
{% assign remainder = remainder | modulo: SECONDS_PER_HOUR %}

{% assign minutes = remainder | divided_by: SECONDS_PER_MINUTE | floor %}
{% assign seconds = remainder | modulo: SECONDS_PER_MINUTE %}

This incident has been active for {{ days }}d {{ hours }}h {{ minutes }}m {{ seconds }}s
```

### Print all responders' names, emails, and roles

* **Summary**: Return all responders' information. This information is available in other places today like the Command Center or any Notify messages in Slack, but could be useful in e.g. an email.
* **Usage**: The **Send an email notification** runbook step, in Jira/Confluence step descriptions, etc.

```jsx Liquid
{% for role in incident.role_assignments -%}
  **{{ role.incident_role.name }}**: {{ role.user.name }} \<{{ role.user.email }}\>
{% endfor %}
```

### Print overview message of current information and next update ETA

* **Summary**: Using Liquid's built in time mechanics, we do time conversions using simple math and then display with formatting.
* **Usage**: Anywhere, but likely **Email** or **Custom Message** steps

```jsx Liquid
{% assign started = incident.milestones | where: "type", "started" | first %}

**CURRENT STATUS**: {{ incident.current_milestone }}
**SEVERITY**: {{ incident.severity }}
**DESCRIPTION**: {{ incident.description }}
**START TIME**: {{ started.occurred_at | date: "%s" | minus: 28800 | date: "%Y-%m-%d %H:%M" }}

**LAST UPDATE**:
  - At: {{ incident.last_note.created_at | date: "$s" | minus: 28800 | date: "%Y-%m-%d %H:%M" }}
  - Note: {{ incident.last_note.body }}

**NEXT UPDATE**: {{ incident.last_note.created_at | date: "%s" | minus: 27000 | date: "%Y-%m-%d %H:%M" }}
```

In the example above, updates are posted in 30-minute intervals and in PST. Dates are stored in UTC, so we first convert them to a date object that Liquid can work with using `date`, and then we subtract seconds from the time to convert from UTC to PST with `minus` before formatting the output to print.

## Limitations

Currently, the use of `where:` in Liquid templating can only be used to filter on a top-level parameter. For example, given the following JSON object:

```json JSON
[
  {
    "id": "3ebfb4da-e2a4-4ae7-9e44-e34df78589e0",
    "status": "active",
    "created_at": "2025-01-08T00:47:43.587Z",
    "updated_at": "2025-01-08T00:47:43.587Z",
    "incident_role": {
      "id": "a75e35b4-b228-4f1a-b455-6de2aec46a1b",
      "name": "Incident Commander",
      "summary": "The Incident Commander is responsible for overall management, communication, and task delegation during incidents.",
      "description": "The Incident Commander holds the high-level state of an incident and is responsible for overall management, communicating with stakeholders, triaging and delegating work, and most importantly, motivating and driving the team through the situation.",
      "created_at": "2022-02-09T17:18:05.678Z",
      "updated_at": "2023-05-09T16:48:44.554Z",
      "discarded_at": null
    },
    "user": {
      "id": "a561dd61-5ff6-480b-aaaf-87bba4ed6d74",
      "name": "John Doe",
      "email": "vthanh+demo@firehydrant.io",
      "slack_user_id": "U032E92MN6S",
      "slack_linked?": true,
      "created_at": "2022-02-09T17:18:06.577Z",
      "updated_at": "2023-10-13T21:25:28.643Z",
      "signals_enabled_notification_types": [
        "sms",
        "apns"
      ]
    }
  }
]
```

...you can filter on top-level parameters like `status = "active"`, but you would not be able to do checks against any nested parameters (e.g., `incident_role.name = "Incident Commander"`). This is due to a limitation in the Liquid templating Ruby gem we use underneath the hood.

The recommended workaround is to use more primitive filters like `for` and `if` statements. For example:

```jsx Liquid
// DOES NOT WORK
{% assign incidentManagers = incident.role_assignments | where: "incident_role.name", "Incident Mnaager" %}

// DOES WORK
{% for role in incident.role_assignments %}
  {% if role_assignment.incident_role.name == "Incident Manager" %}
    // etc...
  {% endif %}
{% endfor %}
```

## Other Resources

* [FireHydrant Liquid playground](https://liquidjs.com/playground.html#I0ZpcmVIeWRyYW50IExpcXVpZCBFeGFtcGxlcwpEb2NzOiBodHRwczovL3Nob3BpZnkuZGV2L2FwaS9saXF1aWQKRm9yIG1vcmUgZXhhbXBsZXM6IGh0dHBzOi8vZ2l0aHViLmNvbS9maXJlaHlkcmFudC9saXF1aWQtdGVtcGxhdGUtZXhhbXBsZXMKCiMjQmFzaWMgRXhhbXBsZXMKSW5jaWRlbnQgbmFtZToge3tpbmNpZGVudC5uYW1lfX0KQ2hhbm5lbCBuYW1lOiB7e2luY2lkZW50LmNoYW5uZWxfbmFtZX19ClRhZ3MKICB7JS0gZm9yIHRhZyBpbiBpbmNpZGVudC50YWdfbGlzdCAlfQogICAgKiB7eyB0YWcgfX0KICB7JS0gZW5kZm9yICV9CkppcmEgVGlja2V0CiAgeyUtIGZvciB0aWNrZXQgaW4gaW5jaWRlbnQuaW5jaWRlbnRfdGlja2V0c1swXS5hdHRhY2htZW50cyAlfQogICAgKiB7eyB0aWNrZXQuZGlzcGxheV90ZXh0IH19IHwge3sgdGlja2V0LmhyZWZfdXJsIH19CiAgeyUtIGVuZGZvciAlfQpOb3RlOiBUaGUgJ3JldHJvJyBvYmplY3QgaXMgb25seSBhdmFpYWxibGUgYWZ0ZXIgYSByZXRyb3NwZWN0aXZlIGhhcyBiZWVuIHN0YXJ0ZWQgYW5kIGluIHRoZSBjb250ZXh0IG9mIGEgJ3JldHJvIGV4cG9ydCcgcnVuYm9vayBzdGVwLgoqIFJldHJvIHB1Ymxpc2hlZCBhdDoge3tyZXRyby5wdWJsaXNoZWRfYXR9fQ==,ewoJImluY2lkZW50IjogewoJCSJpZCI6ICJpbmNpZGVudF9pZCIsCgkJIm5hbWUiOiAiVGVzdCBJbmNpZGVudCIsCgkJImNyZWF0ZWRfYXQiOiAiMjAyMi0wNS0yMFQxNTo0Mjo0NC42MjlaIiwKCQkic3RhcnRlZF9hdCI6ICIyMDIyLTA1LTIwVDE1OjQyOjQ0LjcxOFoiLAoJCSJzdW1tYXJ5IjogIlN1bW1hcnkiLAoJCSJjdXN0b21lcl9pbXBhY3Rfc3VtbWFyeSI6IG51bGwsCgkJImRlc2NyaXB0aW9uIjogIkRlc2NyaXB0aW9uIiwKCQkiY3VycmVudF9taWxlc3RvbmUiOiAicmVzb2x2ZWQiLAoJCSJudW1iZXIiOiAxNjYsCgkJInByaW9yaXR5IjogIlA0IiwKCQkic2V2ZXJpdHkiOiAiU0VWMyIsCgkJInNldmVyaXR5X2ltcGFjdCI6IG51bGwsCgkJInNldmVyaXR5X2NvbmRpdGlvbiI6IG51bGwsCgkJInRhZ19saXN0IjogWwoJCQkidGFnMSIsICJ0YWcyIgoJCV0sCgkJInByaXZhdGVfaWQiOiAieHh4eHh4eCIsCgkJIm9yZ2FuaXphdGlvbl9pZCI6ICJvcmdfaWQiLAoJCSJpbmNpZGVudF9yb2xlcyI6IFtdLAoibWlsZXN0b25lcyI6IFsKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTA6MTkuNDQwWiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMDQ3WiIsCiJ0eXBlIjogInN0YXJ0ZWQiLAoib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQxMzoxMDoxOS4wMDBaIiwKImR1cmF0aW9uIjogbnVsbAp9LAp7CiJpZCI6ICJ1bmlxdWVfbWlsZXN0b25lX2lkIiwKImNyZWF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNDowNy4wNTJaIiwKInVwZGF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNDowNy4wODZaIiwKInR5cGUiOiAiZGV0ZWN0ZWQiLAoib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQxNDoxMzo1NS4wMDBaIiwKImR1cmF0aW9uIjogIlBUMUgzTTM2UyIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTA6MTkuNjg5WiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMDkyWiIsCiJ0eXBlIjogImFja25vd2xlZGdlZCIsCiJvY2N1cnJlZF9hdCI6ICIyMDIyLTA2LTA0VDE1OjEzOjU2LjAwMFoiLAoiZHVyYXRpb24iOiAiUFQxSDFTIgp9LAp7CiJpZCI6ICJ1bmlxdWVfbWlsZXN0b25lX2lkIiwKImNyZWF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNDowNy4wNjVaIiwKInVwZGF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNDowNy4wOThaIiwKInR5cGUiOiAiaW52ZXN0aWdhdGluZyIsCiJvY2N1cnJlZF9hdCI6ICIyMDIyLTA2LTA0VDE2OjEzOjU2LjAwMFoiLAoiZHVyYXRpb24iOiAiUFQxSCIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMDcwWiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMTA0WiIsCiJ0eXBlIjogImlkZW50aWZpZWQiLAoib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQxNzoxMzo1Ny4wMDBaIiwKImR1cmF0aW9uIjogIlBUMUgxUyIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMDc1WiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMTEwWiIsCiJ0eXBlIjogIm1pdGlnYXRlZCIsCiJvY2N1cnJlZF9hdCI6ICIyMDIyLTA2LTA0VDE4OjEzOjU4LjAwMFoiLAoiZHVyYXRpb24iOiAiUFQxSDFTIgp9LAp7CiJpZCI6ICJ1bmlxdWVfbWlsZXN0b25lX2lkIiwKImNyZWF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNzoxMi4zNTZaIiwKInVwZGF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNzoxMi4zODNaIiwKInR5cGUiOiAicmVzb2x2ZWQiLAoib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNzoxMi4zNDdaIiwKImR1cmF0aW9uIjogIlBUNEgzTTE0UyIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTg6NDAuMzQwWiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTg6NDAuMzcwWiIsCiJ0eXBlIjogInBvc3Rtb3J0ZW1fc3RhcnRlZCIsCiJvY2N1cnJlZF9hdCI6ICIyMDIyLTA2LTA0VDIyOjE4OjQwLjMzM1oiLAoiZHVyYXRpb24iOiAiUFQxTTI3UyIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MzI6NTMuNTIwWiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MzI6NTMuNTY0WiIsCiJ0eXBlIjogInBvc3Rtb3J0ZW1fY29tcGxldGVkIiwKIm9jY3VycmVkX2F0IjogIjIwMjItMDYtMDRUMjI6MzI6NTMuNTA5WiIsCiJkdXJhdGlvbiI6ICJQVDE0TTEzUyIKfQpdLAoJCSJhY3RpdmUiOiB0cnVlLAoJCSJsYWJlbHMiOiB7fSwKCQkicm9sZV9hc3NpZ25tZW50cyI6IFtdLAoJCSJzdGF0dXNfcGFnZXMiOiBbXSwKCQkiaW5jaWRlbnRfdXJsIjogImh0dHBzOi8vYXBwLmZpcmVoeWRyYW50LmlvL2luY2lkZW50cy9pbmNpZGVudF9pZC9pbmNpZGVudC9vdmVydmlldyIsCgkJInByaXZhdGVfc3RhdHVzX3BhZ2VfdXJsIjogImh0dHBzOi8vYXBwLmZpcmVoeWRyYW50LmlvL2luY2lkZW50cy9pbnRlcm5hbC9zdGF0dXNfcGFnZS8zMTk3MDgyNi14eHh4LXh4eHgteHh4eC04ZTU5ZTJiNzI5MzUveHh4eHgiLAoJCSJvcmdhbml6YXRpb24iOiB7CgkJCSJuYW1lIjogIlRlc3QgQWNjb3VudCIsCgkJCSJpZCI6ICJvcmdfaWQiCgkJfSwKCQkiY3VzdG9tZXJzX2ltcGFjdGVkIjogMCwKCQkibW9uZXRhcnlfaW1wYWN0IjogbnVsbCwKCQkibW9uZXRhcnlfaW1wYWN0X2NlbnRzIjogbnVsbCwKCQkibGFzdF91cGRhdGUiOiBudWxsLAoJCSJsYXN0X25vdGUiOiBudWxsLAoJCSJyZXBvcnRfaWQiOiBudWxsLAoJCSJzZXJ2aWNlcyI6IFt7CgkJCSJuYW1lIjogImZpc2giLAoJCQkiaWQiOiAic3R1ZmYiCgkJfV0sCgkJImVudmlyb25tZW50cyI6IFtdLAoJCSJmdW5jdGlvbmFsaXRpZXMiOiBbXSwKCQkiY2hhbm5lbF9uYW1lIjogImluY2lkZW50LTE2NiIsCgkJImNoYW5uZWxfcmVmZXJlbmNlIjogIjwjQzAzR0M1U0tENUh8aW5jaWRlbnQtMTY2PiIsCgkJImNoYW5uZWxfaWQiOiAiQzAzR0M1U0tENUgiLAoJCSJjaGFubmVsX3N0YXR1cyI6ICJvcGVyYXRpb25hbCIsCgkJImluY2lkZW50X3RpY2tldHMiOiBbewoJCQkiaWQiOiAidGlja2V0X2lkIiwKCQkJInN1bW1hcnkiOiAiVGVzdCBjcmVhdGVkIGluIHVpIiwKCQkJImRlc2NyaXB0aW9uIjogIkRlc2NyaXB0aW9uIiwKCQkJInN0YXRlIjogImluX3Byb2dyZXNzIiwKCQkJInR5cGUiOiAiaW5jaWRlbnQiLAoJCQkiYXNzaWduZWVzIjogW10sCgkJCSJjcmVhdGVkX2J5IjogewoJCQkJImlkIjogInVzZXJfaWQiLAoJCQkJIm5hbWUiOiAiSm9obiBTbWl0aCIsCgkJCQkic291cmNlIjogImZpcmVoeWRyYW50X3VzZXIiLAoJCQkJImVtYWlsIjogImpzbWl0aEBnbWFpbC5jb20iCgkJCX0sCgkJCSJhdHRhY2htZW50cyI6IFt7CgkJCQkidHlwZSI6ICJsaW5rIiwKCQkJCSJkaXNwbGF5X3RleHQiOiAiWFhYLTEwMjIiLAoJCQkJImhyZWZfdXJsIjogImh0dHBzOi8vY29tcGFueS5hdGxhc3NpYW4ubmV0L2Jyb3dzZS9YWFgtMTAyMiIsCgkJCQkiaWNvbl91cmwiOiAiaHR0cHM6Ly9hcHAuY29tcGFueS5pby8vaW50ZWdyYXRpb25zLWFzc2V0cy9qaXJhX2Nsb3VkL2Zhdmljb24ucG5nIgoJCQl9XQoJCX1dLAoJCSJpbXBhY3RzIjogW10sCgkJImNvbmZlcmVuY2VfYnJpZGdlcyI6IFtdLAoJCSJpbmNpZGVudF9jaGFubmVscyI6IFt7CgkJCSJpZCI6ICJDMDNHQzVTS0Q1SCIsCgkJCSJuYW1lIjogImluY2lkZW50LTE2NiIsCgkJCSJzb3VyY2UiOiAic2xhY2siLAoJCQkic291cmNlX25hbWUiOiAiU2xhY2siLAoJCQkic291cmNlX2lkIjogInNvdXJjZV9pZCIsCgkJCSJ1cmwiOiAiaHR0cHM6Ly9maHRlc3RhY2NvdW50LnNsYWNrLmNvbS9tZXNzYWdlcy9DMDNHQzVTS0Q1SCIsCgkJCSJpY29uX3VybCI6ICJodHRwczovL2FwcC5maXJlaHlkcmFudC5pby8vaW50ZWdyYXRpb25zLWFzc2V0cy9zbGFjay9mYXZpY29uLnBuZyIsCgkJCSJzdGF0dXMiOiAib3BlcmF0aW9uYWwiCgkJfV0sCgkJInJldHJvX2V4cG9ydHMiOiBbXSwKCQkiY3JlYXRlZF9ieSI6IHsKCQkJImlkIjogInVzZXJfaWQiLAoJCQkibmFtZSI6ICJKb2UgU21pdGgiLAoJCQkic291cmNlIjogImZpcmVoeWRyYW50X3VzZXIiLAoJCQkiZW1haWwiOiAiam9lX3NtaXRoQGdtYWlsLmNvbSIKCQl9LAoJCSJjb250ZXh0X29iamVjdCI6IG51bGwsCgkJInJlc3RyaWN0ZWQiOiBmYWxzZSwKCQkiZXhwbGljaXRfb3JnYW5pemF0aW9uX3VzZXJfaWRzIjogW10KCX0sCgoKCSJyZXRybyI6IHsKICAgICJuYW1lIjogIlRlc3QgSW5jaWRlbnQiLAogICAgInB1Ymxpc2hlZF9hdCI6ICIyMDIyLTA2LTA0VDE5OjE1OjU2LjAwOFoiLAoJCSJxdWVzdGlvbnMiOiBbewoJCQkidGl0bGUiOiAidGl0bGUiLAoJCQkiYm9keSI6ICJib2R5IiwKCQkJInVwZGF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQxOToxNTo1Ni4wMDhaIgoJCX1dLAoJCSJjb250cmlidXRpbmdfZmFjdG9ycyI6IFt7CgkJCSJzdW1tYXJ5IjogInN1bW1hcnkiLAoJCQkicG9zaXRpb24iOiAicG9zaXRpb24iLAoJCQkiY3JlYXRlZF9ieSI6ICJKYW5lIFNtaXRoIDxKYW5lU21pdGhAZ21haWwuY29tPiIKCQl9XSwKCQkiaW5jaWRlbnRfcm9sZXMiOiBbewoJCQkibmFtZSI6ICJyb2xlIG5hbWUiLAoJCQkiZGVzY3JpcHRpb24iOiAiUm9sZSBEZXNjcmlwdGlvbiIsCgkJCSJ1c2VyIjogIkphbmUgU21pdGggPEphbmVTbWl0aEBnbWFpbC5jb20+IiwKCQkJInN0YXR1cyI6ICJzdGF0dXMiCgkJfV0sCgkJImluY2lkZW50X2FjdGl2ZV9kdXJhdGlvbiI6ICIyMDIyLTA2LTA0VDE5OjE1OjU2LjAwOFoiLAoJCSJpbXBhY3RzIjogW3sKCQkJInR5cGUiOiAiaW1wYWN0IHR5cGUiLAoJCQkibmFtZSI6ICJpbXBhY3QgbmFtZSIsCgkJCSJzZXZlcml0eSI6ICJTRVYzIiwKCQkJImNvbmRpdGlvbiI6ICJjb25kaXRpb24gbmFtZSIKCQl9XSwKCgkJInN0YXJyZWRfZXZlbnRzIjogW3sKCQkJIm9jY3VycmVkX2F0IjogIjIwMjItMDYtMDRUMTk6MTU6NTYuMDA4WiIsCgkJCSJjcmVhdGVkX2J5IjogIkphbmUgU21pdGggPEphbmVTbWl0aEBnbWFpbC5jb20+IiwKCQkJImJvZHkiOiAiU3RhcnRlZCBFdmVudCBUZXh0IgoJCX1dLAoJCSJtaWxlc3RvbmVzIjogW3sKCQkJInR5cGUiOiAic3RhcnRlZCIsCgkJCSJkdXJhdGlvbiI6ICIyMDIyLTA2LTA0VDE5OjE1OjU2LjAwOFoiLAoJCQkib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQxOToxNTo1Ni4wMDhaIgoJCX1dCgl9Cn0=)
* [LiquidJS Documentation](https://shopify.github.io/liquid/basics/introduction/)