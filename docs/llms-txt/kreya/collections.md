# Source: https://kreya.app/docs/collections.md

# Collections [Pro / Enterprise](/pricing.md)

Collections allow you to organize your operations into an unit of work. Kreya will execute the operations in the defined order. This is especially useful for testing multiple endpoints, for example creating and later deleting an entity. Kreya aggregates the operation and test results, allowing you to quickly scan the outcome. Find more information about this in the [scripting and tests](/docs/scripting-and-tests.md) documentation.

You can also invoke any directory as a collection, just open the directory in Kreya and open the tab "Run as collection".

Invoking collections via the [Kreya CLI](/docs/cli/commands/collection/invoke.md) makes running your tests in a CI/CD pipeline even easier.

![A Kreya collection with multiple successful and a failed test](/assets/ideal-img/collection.a8c6102.400.png)
