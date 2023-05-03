# Builder

The Builder Pattern is a creational pattern whose intent is to separate the construction of a complex object from its `
representation so that you can use the same construction process to create different representations.

The Builder Pattern tries to solve,

1. How can a class that includes creating a complex object be simplified?
2. How can a class create different representations of a complex object?

The Builder and Factory patterns are very similar in the fact they both instantiate new objects at
runtime. The difference is when the process of creating the object is more complex, so rather than the Factory returning
a new instance of ObjectA, it calls the builders director constructor method ObjectA.construct() that goes through a
more complex construction process involving several steps. Both return an Object/Product.

## Terminology

* Product: The Product being built.
* Builder: Builds the concrete product. Implements the Builder Interface.
* Builder Interface: The Interface that the Concrete builder should implement.
* Director: Has a construct() method that when called creates a customized product.


