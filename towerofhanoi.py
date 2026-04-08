def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, source, destination)


# ---- User Input ----
n = int(input("Enter number of disks: "))

print("\nSteps to solve Tower of Hanoi:\n")
tower_of_hanoi(n, 'A', 'B', 'C')
