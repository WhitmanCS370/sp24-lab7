# sp24-lab7
Materials for week 7 lab in CS-370, which includes Ch. 8 "Functions & Closures" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 27, 2024_

Organization:
* SDX-ch9: The code files for the _SDX Ch. 8_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
Who will start out as
* DRIVER: John Leeds
* NAVIGATOR: Oliver Baltzer

You will switch halfway through the _SDX Ch. 9_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 9?
* What questions did you have about the material in the chapters? What did you find confusing?

Main ideas:
* Mock Objects: An object that replaces real functions with a simpler function, typically with a fixed return value
* Protocols: A rule that tells Python what to do at specific moments.
* Decorators: Wrap a function with another function
* Iterators: An object with an __next__ method that stops with StopIteration


Fill in the following table with your definitions and examples for the main concepts of this chapter --- mock objects, context managers, decorators, iterators.

| Concept | Brief Definition | When to use (generally) | Potential uses in audio archive project |
| --- | --- | --- | --- |
| **mock objects** | An object that replaces real functions with a simpler function, typically with a fixed return value | Testing | Testing |
| **context managers** | A protocol that automatically calls __enter__ and __exit__ | If you have a series of actions that you know will proceed and / or follow another action | Opening sound files |
| **decorators** | Wrap a function with another function | When there is a repeated pattern you want to apply to multiple functions | Logging |
| **iterators** | An object with an __next__ method that stops with StopIteration |  When you have a class that contains items you want to iterate through | Making an AudioArchive class that contains a list of songs you want to iterate through |


Write a short summary of what you did (which exercises) below.
