def water_jug_problem():
    jug_a = 4  # Capacity of Jug A
    jug_b = 3  # Capacity of Jug B
    target = 2  # Target amount
    current_a = 0  # Current amount of water in Jug A
    current_b = 0  # Current amount of water in Jug B
    actions = []  # List to store actions

    # Check if the state is valid (within the capacity limits)
    def is_valid_state(a, b):
        return 0 <= a <= jug_a and 0 <= b <= jug_b

    # Perform an action (fill, empty, pour)
    def perform_action(action):
        nonlocal current_a, current_b
        actions.append(action)
        if action == "fill_a":
            current_a = jug_a
        elif action == "fill_b":
            current_b = jug_b
        elif action == "empty_a":
            current_a = 0
        elif action == "empty_b":
            current_b = 0
        elif action == "pour_a_to_b":
            pour_amount = min(current_a, jug_b - current_b)
            current_a -= pour_amount
            current_b += pour_amount
        elif action == "pour_b_to_a":
            pour_amount = min(current_b, jug_a - current_a)
            current_b -= pour_amount
            current_a += pour_amount

    # Start solving the problem
    while current_b != target:
        if current_b == jug_b:
            perform_action("empty_b")  # Empty Jug B if it's full
        elif current_a == 0:
            perform_action("fill_a")  # Fill Jug A if it's empty
        else:
            perform_action("pour_a_to_b")  # Pour water from Jug A to Jug B
    
    # Output the sequence of actions
    print("Sequence of actions:")
    for action in actions:
        print(action)

# Call the water jug problem function
water_jug_problem()
