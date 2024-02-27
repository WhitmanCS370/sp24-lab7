# sp24-lab7
Materials for week 7 lab in CS-370, which includes Ch. 8 "Functions & Closures" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 27, 2024_

Organization:
* SDX-ch9: The code files for the _SDX Ch. 8_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
Who will start out as
* DRIVER: Driver's name
* NAVIGATOR: Navigator's name

You will switch halfway through the _SDX Ch. 9_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 8?
* What questions did you have about the material in the chapters? What did you find confusing?

Fill in the following table with your definitions and examples for the main concepts of this chapter --- mock objects, context managers, decorators, iterators.

| Concept | Brief Definition | When to use (generally) | Potential uses in audio archive project |
| --- | --- | --- | --- |
| **mock objects** | A temporary fake object that can be used to fake having a real object | testing something that interacts with an object, when the actual
object is not yet implemented | This could be used with our cache and database implementation, as one may be finshed before the other, and but they need eachother
to function |
| **context managers** | objects or classes that allow for having code sandwiched between a constructor and a desctructor| It's useful for making testing functions that can
manage there own creation and destruction| Having a cache that can start and end itself for the sake of testing would be pretty nice |
| **decorators** | The act of passing a function into another function to execute nested functions | When we have a general function that is shared between classes, but certain
implementation details are varied, those details could be passed as its own function| Audio effects might have similar set up and necessary steps per effect, but the actual effect
might be unique, thus we can pass in the unique bit of code through the function |
| **iterators** | The ability to add the functionality to iterate through your object/class | Any case in which a given object would benefit from being able
to traverse to another object in an order | perhaps the cache would have a cell that would be linked to a next cell |


Write a short summary of what you did (which exercises) below.
