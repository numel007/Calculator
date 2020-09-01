# This calculator takes a user's input of how much weight they can benchpress for 4-6 reps.
# It then calculates their 1RM, the weight the user can move for a maximum of 1 rep at 100% RPE (Rate of Perceived Exertion).
# After displaying the one rep max, the calculator displays how much weight the user should be able to move for descending levels of RPE.

while True:  # Asks for weight input until a float is entered.
    try: # Convert input into float for later usage.
        input_weight_lb = float(
            input("How much weight can you benchpress for 4-6 reps? "))
        break

    except ValueError: # Reject string inputs.
        print("Enter a valid number.")

while True:
    try: # Determine rep count to pick which calculation to perform.
        input_rep_count = int(input("How many reps were completed at this weight? Must be 4, 5, or 6. "))

        if input_rep_count == 4: # Modifies formula for 4 reps performed.
            one_rep_max_lb = (input_weight_lb * 4 * 0.033) + input_weight_lb
            break

        elif input_rep_count == 5: # Modifies formula for 5 reps performed.
            one_rep_max_lb = (input_weight_lb * 5 * 0.033) + input_weight_lb
            break

        elif input_rep_count == 6: # Modifies formula for 6 reps performed.
            one_rep_max_lb = (input_weight_lb * 6 * 0.033) + input_weight_lb
            break

        else: # Reject incorrect numerical inputs.
            print("Enter 4, 5, of 6.") 

    except ValueError: # Reject string inputs.
        print("Do not enter a string.")
        continue

rpe_95_lb = one_rep_max_lb*0.95  # Calculate 95% rate of perceived effort.
rpe_93_lb = one_rep_max_lb*0.93  # Calculate 93% rate of perceived effort.
rpe_90_lb = one_rep_max_lb*0.9   # Calculate 90% rate of perceived effort.
rpe_87_lb = one_rep_max_lb*0.87  # Calculate 87% rate of perceived effort.
rpe_85_lb = one_rep_max_lb*0.85  # Calculate 85% rate of perceived effort.
rpe_83_lb = one_rep_max_lb*0.83  # Calculate 83% rate of perceived effort.
rpe_80_lb = one_rep_max_lb*0.8   # Calculate 80% rate of perceived effort.
rpe_77_lb = one_rep_max_lb*0.77  # Calculate 77% rate of perceived effort.
rpe_75_lb = one_rep_max_lb*0.75  # Calculate 75% rate of perceived effort.

while True: # Determines which units to display.
    kg_or_lb = str.upper(input("Is this weight in kgs or lbs? "))

    if kg_or_lb == "KGS":  # Selects kgs as unit.
        print("You selected kgs. \n")
        print(
            f"You lifted {input_weight_lb}kgs for {input_rep_count} reps. Your 1RM is {one_rep_max_lb}kgs. \n")
        print(f"RPE 95%: {rpe_95_lb}kgs for 2 reps.")
        print(f"RPE 93%: {rpe_93_lb}kgs for 3 reps.")
        print(f"RPE 90%: {rpe_90_lb}kgs for 4 reps.")
        print(f"RPE 87%: {rpe_87_lb}kgs for 5 reps.")
        print(f"RPE 85%: {rpe_85_lb}kgs for 6 reps.")
        print(f"RPE 83%: {rpe_83_lb}kgs for 7 reps.")
        print(f"RPE 80%: {rpe_80_lb}kgs for 8 reps.")
        print(f"RPE 77%: {rpe_77_lb}kgs for 9 reps.")
        print(f"RPE 75%: {rpe_75_lb}kgs for 10 reps. \n")
        break

    elif kg_or_lb == "LBS":  # Selects lbs as unit.
        print("You selected lbs. \n")
        print(
            f"You lifted {input_weight_lb}lbs for {input_rep_count} reps. Your 1RM is {one_rep_max_lb}lbs. \n")
        print(f"RPE 95%: {rpe_95_lb}lbs for 2 reps.")
        print(f"RPE 93%: {rpe_93_lb}lbs for 3 reps.")
        print(f"RPE 90%: {rpe_90_lb}lbs for 4 reps.")
        print(f"RPE 87%: {rpe_87_lb}lbs for 5 reps.")
        print(f"RPE 85%: {rpe_85_lb}lbs for 6 reps.")
        print(f"RPE 83%: {rpe_83_lb}lbs for 7 reps.")
        print(f"RPE 80%: {rpe_80_lb}lbs for 8 reps.")
        print(f"RPE 77%: {rpe_77_lb}lbs for 9 reps.")
        print(f"RPE 75%: {rpe_75_lb}lbs for 10 reps. \n")
        break

    elif not kg_or_lb.isalpha():  # Reject numerical inputs.
        print("Do not enter numbers.")

    else:  # Reject incorrect string input.
        print("Enter either 'kgs' or 'lbs.'")
