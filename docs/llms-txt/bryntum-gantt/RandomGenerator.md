# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/RandomGenerator.md

# [RandomGenerator](https://bryntum.com/docs/gantt/api/Core/helper/util/RandomGenerator)

Generates pseudo random numbers from predefined sequence of 100 numbers

## Functions

Functions are methods available for calling on the class

[nextRandom](https://bryntum.com/docs/gantt/api/Core/helper/util/RandomGenerator#function-nextRandom)
Returns next pseudo random integer number from sequence between 0 and max parameter value (99 is maximum value)

```
const rand = new RandomGenerator();
const randomNumber = rand.nextRandom(50);
```

[reset](https://bryntum.com/docs/gantt/api/Core/helper/util/RandomGenerator#function-reset)
Resets sequence to initial number

[fromArray](https://bryntum.com/docs/gantt/api/Core/helper/util/RandomGenerator#function-fromArray)
Returns pseudo random array element

```
const rand = new RandomGenerator();
const cities = ['New York', 'London', 'Tokyo', 'Paris' ];
const randomCity = rand.fromArray(cities);
```

[randomArray](https://bryntum.com/docs/gantt/api/Core/helper/util/RandomGenerator#function-randomArray)
Creates a random array from a larger array of possibilities.

```
const rand = new RandomGenerator();
const cities = [
'New York', 'London', 'Tokyo', 'Paris', 'Los Angeles',
'Berlin', 'Sydney', 'Singapore', 'Rome', 'Toronto',
'Hong Kong', 'Amsterdam', 'Barcelona', 'Dubai', 'Chicago',
'Mumbai', 'Bangkok', 'Moscow', 'San Francisco', 'Madrid' ];
const randomCities = rand.randomArray(cities, 5);
```
