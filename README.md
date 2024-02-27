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

| Concept | Brief Definition | When to use (generally) | Potential uses in audio archive project | Questions |
| --- | --- | --- | --- |
| **mock objects** | When you change functions at runtime to make testing easier. | Used mainly for testing and to call functions already defined. | Testing complicated functionality when you need to fix/set the inputs. Also for singling out individual functions. | What is the difference between this and monkey patching
| **context managers** | After you use/test your mock object, context managers reset it to the original version. | When you are using/testing mock objects. | Testing complicated functionality when you need to fix/set the inputs. Also for singling out individual functions. After each, we need to reset them |
| **decorators** |They are functions that are like inheritance but with functions | When we want to reuse functions | Having a generalized function which would be able to play a section of a sound or edit that specific section. | How is it different than using just other functions inside a function?
| **iterators** | An abstract method of parsing through a linear set of data that supports iteration, generally a data structure  | So you don't have to redefine a way of parsing for each class | Parsing through sounds of different data types. If we have encapselated iterator functionality, we can reuse an iterator class. |


Write a short summary of what you did (which exercises) below.
