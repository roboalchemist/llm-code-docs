# Source: https://infisical.com/docs/documentation/platform/access-controls/access-requests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Access Requests

> Learn how to request access to sensitive resources in Infisical.

In certain situations, developers need to expand their access to a certain new project or a sensitive environment. For those use cases, it is helpful to utilize Infisical's **Access Requests** functionality.

This functionality works in the following way:

1. A project administrator sets up an access policy that assigns access managers (also known as eligible approvers) to a certain sensitive folder or environment.
   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/access-controls/create-access-request-policy.png" alt="Create Access Request Policy Modal" />

   <Note>
     A step policy enables a sequential approval workflow in which approvals
     must follow the designated chain.
   </Note>

   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/access-controls/access-request-policies.png" alt="Access Request Policies" />

2. When a developer requests access to one of such sensitive resources, the request is visible in the dashboard, and the corresponding eligible approvers get an email notification about it.
   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/access-controls/request-access.png" alt="Access Request Create" />
   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/access-controls/access-requests-pending.png" alt="Access Request Dashboard" />

3. An eligible approver can approve or reject the access request.

   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/access-controls/access-request-bypass.png" alt="Access Request Bypass" />

   <Note>
     Optionally, approvers can edit the duration of an access request to reduce how long access will be granted by clicking the **Edit** icon next to the duration.
     <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/access-controls/edit-access-request.png" alt="Edit Access Request" />
   </Note>

<Info>
  If the access request matches with a policy that allows break-glass approval
  bypasses, the requester may bypass the policy and get access to the resource
  without full approval.
</Info>

5. As soon as the request is approved, developer is able to access the sought resources.
