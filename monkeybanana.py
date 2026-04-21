def monkey_banana(monkey, box, banana):
    steps = []
    
    if monkey != box:
        steps.append("Monkey moves to the box")
        monkey = box

    if box != banana:
        steps.append("Monkey pushes the box under the banana")
        box = banana
        monkey = banana

    steps.append("Monkey climbs the box")

    steps.append("Monkey picks the banana")

    return steps

monkey = input("Enter monkey position (A/B/C): ")
box = input("Enter box position (A/B/C): ")
banana = input("Enter banana position (A/B/C): ")

result = monkey_banana(monkey, box, banana)


print("\nSteps to get the banana:\n")
for step in result:
    print(step)
