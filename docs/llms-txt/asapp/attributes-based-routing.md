# Source: https://docs.asapp.com/agent-desk/digital-agent-desk/queues-and-routing/attributes-based-routing.md

# Attributes Based Routing

> Learn how to use Attributes Based Routing (ABR) to route chats to the appropriate Agent Queue.

Attributes Based Routing (ABR) is a rules-based system to determine which Agent Queue an incoming chat should be assigned to.

ASAPP invokes ABR by default after our Machine Learning model classifies a customer's utterances to an Intent and determines that the Intent cannot be serviced by an automated flow.

## Attributes of ABR

Attributes can be any piece of information that customers can pass to ASAPP using the integrated SDKs.

ASAPP natively defines the standard attributes below:

* Intent - This is a code determined by running customer utterances through various different ML models.
  Ex: ACCTINFO, BILLING
* Web URL - This is the webpage that invoked the SDK. You can use any part of the URL as a value to route on.
  Ex: [www.customer.com/consumer/support](http://www.customer.com/consumer/support), [www.customer.com/business/sales](http://www.customer.com/business/sales)
* Channel - This is the channel the chat originated from.
  Ex: Web, iOS

The ASAPP SDK defines additional parameters, which can also be used in ABR. You can define these parameters as part of the ContextProvider.

* Company Subdivision
  Ex: divisionId1, subDivisionId2
* Segments
  Ex: NorthEast, USA, EMEA

You can also define custom customer specific attributes to be used in routing. Customer Information allows definition of any number of attributes as key-value pairs, which can be set per chat and be used for routing to specific agent queues. Please refer to the Customer Information section for more details on how to define custom attributes.

## Configuration

ABR is capable of using any or all of the above attributes to determine which queue to route a chat. The configuration is extremely flexible and can accommodate various complex rules including regular expression matches, as well as multi value matches.

Contact your Implementation Manager to model the routing rules.

## Template for Submitting Rules

Customers can create an Excel document with a sheet for each attribute they would like to define. The sheet name should be the name of the attribute and have two columns, one defining all the possible attribute values and the other column containing the name of the queue to be routed to.

If you are going to use multiple attributes in any different combinations, then you should define these conditions in a separate sheet, dedicating a row for every unique combination.

ASAPP will assume that Excel attribute names that do not follow the ASAPP standard are custom defined and passed in 'Customer Information'.

See the [User Management](/agent-desk/digital-agent-desk/user-management) section for more information.

## Queue Management

You can define Queues based on business or technical needs. You can define any number of queues and can follow any desired naming convention. You can apply Business Hours to queues individually. For more information on other features and functionality, please contact your Implementation Manager.

You can assign Agents to one or more queues based on skills and/or requirements. Please refer to [User Management](/agent-desk/digital-agent-desk/user-management) for more details.
