# One Rep Max and RPE Calculator
This calculator is used to calculate a user's one rep maximum on the bench press. It will also output expected rep ranges at each level of perceived exertion from 95% to 80%. 

- 1RM & RPE Calculator
    - [Terminology](#Terminology)
    - [Usage](#Usage)
    - [Sources](#Sources)

## Terminology
In bench pressing, a person lifts a bar with a certain amount of weight. A one rep max (1RM) is the weight that a person can move through the eccentric and concentric motion for a maximum of one repetition. Since the lifter can only complete the movement once, they are at 100% rate of perceived effort, known as 100% RPE. As weight on the bar is reduced the lifter should be able to complete multiple repetitions. At 95% RPE the lifter is able to complete the movement for 2 repetitions. At 93% RPE, 3 repetitions should be completed. 

The 1RM calculator uses the amount of weight lifted for 4-6 reps at 85% RPE in order to predict the 1RM. The formula in use is (weight_lifted * 1.1307) + 0.6998.
The same formula is used for inputs of both pounds and kilograms.

Percentages of RPE are then calculated based off the 1RM and are presented along with their corresponding rep ranges.

## Usage
Input weight lifted for the 4-6 rep range

Input desired unit of measurement

Output provides a summary of the entered data, 1RM, and descending RPE ranges from 100% to 80%.

## Sources
- [Men's Health](https://www.menshealth.com/uk/building-muscle/a748257/how-to-calculate-one-rep-max)
- [Bodybuilding.com](https://www.bodybuilding.com/fun/other7.htm)
- [CDC](https://www.cdc.gov/physicalactivity/basics/measuring/exertion.htm)
