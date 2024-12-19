class VacuumCleaner:
    def __init__(self, environment, start_location):
        # Initialize the vacuum cleaner with an environment and a starting location
        self.environment = environment
        self.location = start_location

    def move(self, direction):
        # Move the vacuum cleaner based on the direction
        if direction == "right" and self.location == 'A':
            self.location = 'B'
        elif direction == "left" and self.location == 'B':
            self.location = 'A'

    def clean(self):
        # Clean the location if it's dirty
        if self.environment[self.location] == "dirty":
            print(f"Cleaning location {self.location}")
            self.environment[self.location] = "clean"
        else:
            print(f"Location {self.location} is already clean")

    def decide_action(self):
        # Decide whether to clean or move
        if self.environment[self.location] == "dirty":
            self.clean()
        else:
            # If location is clean, move to the other location
            if self.location == 'A':
                self.move("right")
            else:
                self.move("left")

    def run(self, steps):
        # Run the vacuum cleaner for a given number of steps
        for step in range(steps):
            print(f"Step {step + 1}, Location: {self.location}, Status: {self.environment}")
            self.decide_action()

            # If all locations are clean, stop the vacuum
            if all(status == "clean" for status in self.environment.values()):
                print("All locations are clean. Stopping...")
                break

# Define the environment and create the vacuum cleaner
environment = {'A': 'dirty', 'B': 'dirty'}
vacuum = VacuumCleaner(environment, 'A')

# Run the vacuum cleaner for 4 steps
vacuum.run(4)