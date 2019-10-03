# GAMEY BROMEY
The strangest, most elusive Open Problem ever to spontaneously arise out of a third-grader

## What is it?
John Brode somehow made up a formula for computing numbers from any combination of 
alphanumeric or puntuation characters, in the third grade. It is perfectly internally consistent
(ie, he's not just making it up). He can calculate them extremely quickly, but the
answers do not follow an easily discernable pattern.

## How does it work?
We know that the characters GAMEY make up are worth points, while the rest are not. Other than Y, which is 
worth -1, they are all worth 1. However, when they are grouped, strange patterns appear. To simplify things,
all characters GAME are denoted by an A, while the rest are denoted by a T (and Y by Y, of course).

## What do we know?
We know leading T's are irrelevant. Thus the score can always be computed by starting from the first
group of A's. This means that we can unambigously denote a set of numbers {3, 4, 1, 8} as meaning 
3 A's, 4 T's, 1 A, and 8 T's, or AAATTTTATTTTTTTT. In `knowns.ts` you will see over 10,000 of such combinations,
all with their verified answer. One would think that it would be trivial to solve the problem if that
much data had been collected. One would be wrong.

We know there is something to do with alternation. Patterns that arrise when changing one letter group 
at a time consistently appear as 010101 or 0,2,1,2, etc. Even-odd-ness is important, we think.


## Why the name?
GAMEY as the point-value letters. BROMEY is just mashing GAMEY with the originators last name, Brode
