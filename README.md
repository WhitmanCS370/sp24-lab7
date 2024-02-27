# sp24-lab7
Materials for week 7 lab in CS-370, which includes Ch. 8 "Functions & Closures" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 27, 2024_

Organization:
* SDX-ch9: The code files for the _SDX Ch. 8_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Gabe and Jacob

## Team Roles for Part 1
Who will start out as
* DRIVER: Gabe
* NAVIGATOR: Jacob

You will switch halfway through the _SDX Ch. 9_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 8?
the main ideas from the chapter were first mock objects, second is protocols including context manager, decorators and finally iterators,
* What questions did you have about the material in the chapters? What did you find confusing?
I was still not entirely sure about the ideas behind mock objects. I have an understanding but i am not sure if it matches the actuall definition.

Fill in the following table with your definitions and examples for the main concepts of this chapter --- mock objects, context managers, decorators, iterators.

| Concept | Brief Definition | When to use (generally) | Potential uses in audio archive project |
| --- | --- | --- | --- |
| **mock objects** | a mock object is an easy to control replacment for part of a program, it removes some of the coplexity that is not needed. | when you want to test the functionallyity of a program than you can have the mock function return one thing so you dont have to rely on the other functions functionality. | If there is a part of the project that hasnt been done yet. You can also set an object to a specific file instead of giving to option to choose so that you know whats in it every time |
| **context managers** | They are the thing that decided whether to replace the mock objects as well as they are the thing that puts it back at the end. | When you need to control dependencies you use mock objects and the context managers are the things you use to manipulate it. | It seems that every time you are using a mock object it is smart to use a context manager becuse it seems to be the thing that is doing the controlling and making sure everything is doing the correct things. |
| **decorators** | decorators are the functions that are inside of other functions. | They are used to enhance the functionality of a function | we may use this in a function to add accesability when you play something so that every time you play a sound it lets you know it is playing.
| **iterators** | Iterators are a thing that does a certain task over and over again for different values  | The use case of this is when you have a very repetative task that you need to do ever and over again with different values and so you use an iterator | adding a tag to a bunch of different files |


Write a short summary of what you did (which exercises) below.
