def monkey_banana(monkey, box, banana):
    steps = []

    # Step 1: Move monkey to box
    if monkey != box:
        steps.append("Monkey moves to the box")
        monkey = box

    # Step 2: Push box to banana
    if box != banana:
        steps.append("Monkey pushes the box under the banana")
        box = banana
        monkey = banana

    # Step 3: Climb box
    steps.append("Monkey climbs the box")

    # Step 4: Pick banana
    steps.append("Monkey picks the banana")

    return steps


# ---- User Input ----
monkey = input("Enter monkey position (A/B/C): ")
box = input("Enter box position (A/B/C): ")
banana = input("Enter banana position (A/B/C): ")

result = monkey_banana(monkey, box, banana)

# ---- Output ----
print("\nSteps to get the banana:\n")
for step in result:
    print(step)
