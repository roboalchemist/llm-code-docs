# Source: https://adempiere.gitbook.io/docs/introduction/warehouse-management-system.md

# Warehouse Management System

Usually the sales department creates Sales Orders *SO* using alternative Delivery Rules:

| **Delivery Rule**   |
| ------------------- |
| Full Line Delivery  |
| Full Order Delivery |

## Distribution Plan

This report comes out of executing a standard process, basically shows current status of items to be delivered, it allows to consolidate commitments from previous orders in order to generate a delivery plan, this in turn allows to create Outbound Orders based on the items to be delivered.

![Input Parameters for Delivery Plan Report](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MSaiA3SNKjv_RdQn6Iu%2F-MSajZPlqO3kOrZSsQ_D%2Fimage.png?alt=media\&token=eacccdd3-0a1f-491e-8d1b-335bce5a2472)

![Delivery Plan Report](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MSak6tmlZvAQ7_kSgDn%2F-MSakN_ySqZbRr2FhyVr%2Fimage.png?alt=media\&token=57fd72e9-40ba-4ae4-8d9b-6e71d3ff9f9a)

Important data is obtained from this report, such as delivery date, source warehouse, customer, quantity, among others.

## Generate Outbound Order

The user generates a picking list through an Outbound Order *OO* using several criteria based on demand or open sales orders. It is important to mention the key parameters chosen here refer to common criteria that makes delivery possible, for example: Promised Date range, Document Type, Sales Region.

![Generate Outbound Order Selection Criteria](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MSc9b8DcJuSaAVQE6hW%2F-MScE4Mk_DcsWHENbeKZ%2Fimage.png?alt=media\&token=ba473864-96ce-4e05-a6b6-aaa26195faa5)

![Record Selection Preview from Order Lines](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MSc9b8DcJuSaAVQE6hW%2F-MScGVZjbdPOPqzrQNFn%2Fimage.png?alt=media\&token=99d43aee-e9b5-44d0-8e5f-dc4a700198b5)

![Generated Outbound Order Example](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MScHlj47ygiX_QVbc-6%2F-MScJ3xHqMuTAW0zzzoE%2Fimage.png?alt=media\&token=6f65a106-283c-487f-b408-40799fa8f53d)

![Outbound Order Line Detail](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MTy4cV_R2R_GyDumy1H%2F-MTySmE55uFkenVme6fz%2Fimage.png?alt=media\&token=81368ec3-a9c9-473d-b66e-e65e2f1b792a)

You may notice there are different sales order lines reference in an outbound order, This is because their focus is to ease deliveries across several criteria, for example a distribution route and/or fulfilling truck capacity.

![Release Outbound Order to Pick](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MTy4cV_R2R_GyDumy1H%2F-MTy_KzEXJh4xQ6gi6qb%2Fimage.png?alt=media\&token=5b909548-d2f2-4853-8418-fd9c569d9fcd)

As we reach one of the critical steps in this process, this is the Release Outbound Order to Pick that generates the pick tickets and indicates the picking list and the location of the items.

## Distribution Order

The pick tickets that were created on the previous steps will now show up as distribution orders

![Distribution Order from Pick Ticket](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MTy4cV_R2R_GyDumy1H%2F-MTyayLeqQAnKh2WlgUz%2Fimage.png?alt=media\&token=15b8ccd7-a493-49d4-9062-64c5055c29d4)

There are a number of different business scenarios that leverage the distribution order document so from here we can manage picking tickets and inventory movement transactions which also include an In-Transit Warehouse.

The final step involves Generate Shipments from Outbound Order

![Generate Shipments from Outbound Order](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MUCY7_SkHWF1iUv1QVd%2F-MUCdBPCfRpYSNf4ly8D%2Fimage.png?alt=media\&token=ca4d83cd-065c-4d8d-a1fd-c351ce069e97)

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MUCY7_SkHWF1iUv1QVd%2F-MUCe3jbDGyYrZDmtgn-%2Fimage.png?alt=media\&token=360bad26-51a2-45f8-bce2-b8dc63cc4415)
