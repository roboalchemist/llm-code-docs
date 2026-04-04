# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/administration/activities-audited-in-enate.md

# Activities Audited in Enate

## List of Activities Audited in Enate.

An Audit entry of all of the following activities is captured in Enate. Audits of system-generated activity are a time-stamped history of when the event occurred. Audits of user-generated activity contain both a time stamp and a record of the user account involved in the event.

### Packet Status Changes for a Work Item

This is the primary audit trail for process execution in Enate. It records when any work item changes status. Critically it records when users complete actions and tickets as the person accountable for the correct completion of that action.

* Whenever a Work Item status is changed e.g. to In progress, To Do, Completed, Unable to Complete etc. these status changes are recorded in the system, with timestamp.

### Due Date Changes to Work Items (Tickets, Actions & Cases)

* Any manual override to a system generated due date is recorded as a user-generated activity and audited as such.
* Any change the due date is an audit of system-generated activity.

### Allocation of Work Item to Users

* Push Allocations i.e. Manual Assignments where an Agent user allocates a piece of work to a user / clears the allocation, and Configuration-driven automatic assignments of work items to agent users (i.e. a system-generated event).
* Pull Allocations where Agent users request and are auto-allocated a Work Item from Queues they work out of (recorded as a user-generated event), plus the upstream automatic activity where a Configuration-driven Queue assignment was carried out to allocate work into a work Queue.

### Communications/Notes within a Work Item

* The creation of internal Notes and manual sending of Outgoing Emails (with or without attachments) in a Work Item is an audit of user-generated activity.
* The arrival of any inbound email is an audit of system generated activity.

### Time Tracking of Agent Activity in a Work Item

Every time a user opens a work item in Enate regardless of whether the edit it or save it this is audited as user-generated activity.

* The length of time an individual Agent user has spent on a work item is tracked, broken out into each individual session the user works on the Work item. Combined overall length of time spent on a Work Item by all Agent users is also recorded.\
  See Enate Online Help article for details of [when time is tracked / note tracked for a Work Item](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/time-tracker-card#when-is-time-tracked-not-tracked).
* Further, any manual adjustments to the auto-tracked time are recorded, along with timestamp of when the change was made, who made the change, what it ws changed from and to. Note that the originally auto-recorded time is NEVER lost in the Database, this record is persisted and the manual ‘adjustment’ is recoded as a new record.

### Changes to Security and Access Permissions

Any change to security and access permissions is logged as an audit of user-generated activity. This includes a log the change made in the system that caused the user’s access to be changed. The changes that may result in the creation of security and access audit entries include (but are not limited to):

* Creation, deletion, and changes to user accounts.
* Creation, deletion, and changes to user groups.
* Changes to objects accessible by user groups.
* Changes to customer, contracts, services and processes that result in a change to user access.
* Changes to role assigned to users (e.g. team leader)

### Configuration Change Audits

The act of setting a Case or Ticket process Live in Enate is the moment that a change to the operational configuration is made. This restricted to those users with the ‘Release Manager’ role.

* The act of setting a Case or Ticket process live is audited as user-generated activity.

### User sessions

All successful and failed attempts to create a User Session (i.e. log in to Enate) are logged as user-generated activity.

### Universal Timestamp

Every record in Enate is stamped with the date and time that it was last updated. This, in combination with the time tracking of agent activity within a work item, creates an additional interpreted audit for activities that are not directly audited.

For example the Universal Timestamp allows us to understand that a Defect on work item 1234-C-A1 was deleted at 2022/04/12 13:41:32 GMT. From the Agent Activity on a Work Item we can see that John Doe opened work item 1234-C-A1 at 2022/04/12 13:39:00 GMT and closed the work item at 2022/04/12 13:50:00 GMT. Therefore, John Doe deleted the Defect.

### API Access Logs

All updates to Enate are made through the Enate WebAPI. Every call to the Enate WebAPI whether the call is initiated from the Enate web applications (Work Manager or Builder) or a direct access to the Enate API (e.g. by an external system calling it) are logged as user-generated activity.

These logs are not available to End clients directly through the user interface but are managed as part of the Enate SaaS service in our log aggregation platform. They are available for either forensic requirements in response to security incidents or for detailed analysis of functional incidents by the Enate support team.
