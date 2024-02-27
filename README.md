# sp24-lab7
Materials for week 7 lab in CS-370, which includes Ch. 8 "Functions & Closures" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 27, 2024_

Organization:
* SDX-ch9: The code files for the _SDX Ch. 8_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
Who will start out as
* DRIVER: Neel Troeger
* NAVIGATOR: Clara
* NAVIGATOR: Sam

You will switch halfway through the _SDX Ch. 9_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 8?

- Mock Objects
- Decorators
- Iterators

The main idea from SDX chapter 8 is to understand the concepts of mock objects, context managers, decorators, and iterators. Mock objects are used to test code that depends on other code. Context managers are used to manage resources. Decorators are used to modify the behavior of functions or methods. Iterators are used to iterate over a sequence of items.

* What questions did you have about the material in the chapters? What did you find confusing?

What's the point of mock objects?
What are some real world examples of how these concepts are used?

Fill in the following table with your definitions and examples for the main concepts of this chapter --- mock objects, context managers, decorators, iterators.

| Concept | Brief Definition | When to use (generally) | Potential uses in audio archive project |
| --- | --- | --- | --- |
| **mock objects** | temporarily replacing the definition of a function | software testing | testing |
| **context managers** | manages mock objects | when we want to use the original function definition after using the mock object | testing |
| **decorators** | wrapping one function with another | when you want to add extra functionality to your function | flask |
| **iterators** | iterate through a newly defined object | polymorphism (provides a uniform interface) | playing many sounds |


Write a short summary of what you did (which exercises) below.

- Timing blocks
  - We made a class called Timer to log the time it takes to run a block of code
- Handling empty strings
  - We made the BetterIterator handle empty strings
- Even better cursor
  - Our previous one solved this in such a way
- Logging to a file (?)
  - We created a decorator that writes to a log file every time a function is run