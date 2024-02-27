# sp24-lab7
Materials for week 7 lab in CS-370, which includes Ch. 8 "Functions & Closures" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 27, 2024_

Organization:
* SDX-ch9: The code files for the _SDX Ch. 8_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Grant and Marlyn

## Team Roles for Part 1
Who will start out as
* DRIVER: Grant 
* NAVIGATOR: Marlyn

You will switch halfway through the _SDX Ch. 9_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 8?

-Mock objects: how to implement them and how they can be used in testing
-Protocols: we were confused about the context manager and how ...'s are used when passing arguments into with statmeents
-Decorators: how to wrap a function with another function. we were confused on how exactly the built in @wrap works internally
-Iterators: understanding more clearly how iterators that we rely on in python's builtins work and how to design our own in OOP using __iter__ and __next__ . We were slightly confused about whether StopIteratiuon is a builtin and how to use it properly



* What questions did you have about the material in the chapters? What did you find confusing?

Fill in the following table with your definitions and examples for the main concepts of this chapter --- mock objects, context managers, decorators, iterators.

| Concept | Brief Definition | When to use (generally) | Potential uses in audio archive project |
| --- | --- | --- | --- |
| **mock objects** | An object that mimics an objects behavior in a way that's more simple to control and predict. Includes behavior of its constansts and functions. | Simulating behavior that we dont actually want to run for testing | Testing functionality without actually havving to play lots of sounds |
| **context managers** | An object that is used to do some setup and teardown work for entering and leaving a codeblock.| file objects, environment variables, timers, and loggers| Opening an audio file or seting a timer to track the duration of a recording |
| **decorators** | 
Functions that modify or extend behavior of other functions or methods without changing the code.  | Add more functionality to an existing function | Using patch decorator from the unittest library to use mock objects and test for proper command calls without having to actually execute (ex: playing audio file call testing) |
| **iterators** | function or object that allows you to iterate over collections of data | When you need to iterate
 over a large collection and you want to save memory, when you need to create a custom iterable, when you need to safely remove elements from a collection while iterating over it, when you need to work with different collection types | when playing files in sequence or simultaneously (creating iterable object composed of audio objects and iterate playing with or without waiting for stops) |


Write a short summary of what you did (which exercises) below.
