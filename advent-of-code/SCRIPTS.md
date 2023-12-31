# YT-Scripts - Advent of Code 2023

## Day 1 - Trebuchet!?

Hey there! Today, we're diving into the first challenge of Advent of Code 2023. Let's get started!

In part one, the Elves discover that their calibration document has been enhanced by an enthusiastic young Elf. The calibration values are now hidden within lines of text. We need to recover these values by combining the first and last digits in each line.

Let's take a look at my Python solution:

This code reads the document, extracts digits from each line, combines the first and last digits, and calculates the sum of all calibration values. The result? A total calibration sum.


In Part 2, the challenge becomes a bit trickier. Some digits are now spelled out with letters. Our task is to find the real first and last digits on each line. Let's explore the solution:

This code introduces a dictionary mapping word representations to their numerical values. The calc function handles the conversion of digits or words to numerical values. We then iterate through each line, calculate the calibration values, and find the total sum.

And there you have it! We've successfully solved the first challenge. If you enjoyed this video, don't forget to like, share, and subscribe for more content.


