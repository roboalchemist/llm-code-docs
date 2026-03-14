# Source: https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/units-of-measure.md

# Units of Measure

Unit of Measure (UOM) are how the quantities of products are defined. For Products, these are non monetary in nature and represent something that can be measured such as time, distance, volume, quantity, weight, etc.... Conversion from one UOM to another is possible, allowing the UOM to be specified on documents and have the quantities dealt with properly.

UOM types can include product specific types such as packaging (box, 6-pack, pallet). The conversion to other UOM such as "each" can be defined so the packaging can be broken down.

Each UOM is also used to set the precision of quantities and costs. The precision value is the number of decimal places the system will maintain when calculating the quantity or cost of the product.

One UOM should be marked as the default. Typically, this is the unit Each.

## Unit of Measure Conversion

The ADempiere system provides some automatic conversions between common units of measures (e.g. minute, hour, day, working day, etc.) but these are only used in resource scheduling operations. All other conversions have to be defined explicitly for each product.

Each product has a base or system UOM. All conversions are from this base UOM. Conversions need to be direct (i.e. if you have only a conversion between UOMs A-B and B-C, the system cannot convert A-C).

The conversion is defined by a multiply rate and divide rate used to convert the quantity from one of the units to the other. The Product UOM has to be the smallest UOM in the set of possible conversions. The divide rate must be > =1. For example, to convert Each to Pair, the multiply rate would be 0.5.

As an example, suppose there are two types of rope in inventory. The rope is stocked and sold in meters (m) but its is purchased by spool. For rope A, the spool contains 1000m of the rope. For rope B, the spool contains 400m. Each rope product would use Meter as its base unit and each would have a UOM conversion from Meter to Spool with different values.

![The Meter Unit of Measure](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G3L68JQlTRhJmOqV%2Fimage%20\(8\).png?generation=1550588336942678\&alt=media)

![The Spool Unit of Measure](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LKSuKcmYEEujXOHKw1P%2Fimage.png?generation=1550287136708456\&alt=media)

![Conversions from Meter to Spool for the two Rope products](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G3L8rOsUngTXcPwT%2Fimage%20\(14\).png?generation=1550588338276928\&alt=media)

![Purchase Order Line for 3 Spools of Rope A](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G3LAUMchhTNKxvBD%2Fimage%20\(11\).png?generation=1550588335900034\&alt=media)

![Purchase Order Line for 3 Spools of Rope B](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-LZ5G3LILf-EXjz9mW06%2Fimage%20\(19\).png?generation=1551809343479838\&alt=media)

![Product Info for the Rope products showing Ordered Quantities in meters](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G3LE65eEIrPJUYRi%2Fimage%20\(12\).png?generation=1550588335569655\&alt=media)

![Material Receipt Lines showing receipt of spools. Not matched to order yet.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G3LGqzMqpJzsGZly%2Fimage%20\(4\).png?generation=1550588335944193\&alt=media)

![After the Material Receipt, On Hand quantity is shown in meters](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1qz6MMH7cxPsSRVD%2Fimage%20\(20\).png?generation=1551809344438190\&alt=media)

![After the Matching of PO with the Receipt, the On Order quantity is now zero. ](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G3LKac2LEcKhanSN%2Fimage%20\(3\).png?generation=1550588335410014\&alt=media)
