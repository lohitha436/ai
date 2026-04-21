state = {
    "monkey": "door",
    "banana": "ceiling",
    "chair": "corner",
    "has_banana": False
}

def solve():
    print("Monkey goes to chair")
    print("Push chair to banana")
    print("Climb chair")
    print("Grab banana")
    state["has_banana"] = True

solve()
print("Monkey has banana:", state["has_banana"])
