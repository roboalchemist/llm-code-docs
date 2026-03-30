# Source: https://www.hammerdb.com/docs4.0/ch03s05.html

Title: 5. Understanding the TPROC-C workload derived from TPC-C

URL Source: https://www.hammerdb.com/docs4.0/ch03s05.html

Markdown Content:
The TPC-C specification on which TPROC-C is based implements a computer system to fulfil orders from customers to supply products from a company. The company sells 100,000 items and keeps its stock in warehouses. Each warehouse has 10 sales districts and each district serves 3000 customers. The customers call the company whose operators take the order, each order containing a number of items. Orders are usually satisfied from the local warehouse however a small number of items are not in stock at a particular point in time and are supplied by an alternative warehouse. It is important to note that the size of the company is not fixed and can add Warehouses and sales districts as the company grows. For this reason your test schema can be as small or large as you wish with a larger schema requiring a more powerful computer system to process the increased level of transactions. The TPROC-C schema is shown below, in particular note how the number of rows in all of the tables apart from the ITEM table which is fixed is dependent upon the number of warehouses you choose to create your schema.

**Figure 3.2.TPROC-C Schema**

![Image 1: TPROC-C Schema](https://www.hammerdb.com/docs4.0/resources/ch3-2.png)

For additional clarity please note that the term Warehouse in the context of TPROC-C bears no relation to a Data Warehousing workload, as you have seen TPROC-C defines a transactional based system and not a decision support (DSS) one. In addition to the computer system being used to place orders it also enables payment and delivery of orders and the ability to query the stock levels of warehouses. Consequently the workload is defined by a mix of 5 transactions selected at random according to the balance of the percentage value shown as follows:

*   New-order: receive a new order from a customer: 45%

*   Payment: update the customers balance to record a payment: 43%

*   Delivery: deliver orders asynchronously: 4%

*   Order-status: retrieve the status of customers most recent order: 4%

*   Stock-level: return the status of the warehouses inventory: 4%
