class VolleyballPosition:
    def __init__(self, name, role, specialization, on_court):
        self.name = name
        self.role = role
        self.specialization = specialization
        self.on_court = on_court

    def enter_court(self):
        self.on_court = True
        print(f"{self.name} enters the court.")

    def leave_court(self):
        self.on_court = False
        print(f"{self.name} leaves the court.")

    def __del__(self):
        print(f"The {self.name} has left the game.")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")
        print(f"On Court: {self.on_court}\n")

setter = VolleyballPosition(name="Setter", role="Setter", specialization="Setting", on_court=False)
outside_hitter = VolleyballPosition(name="Outside Hitter", role="Hitter", specialization="Attacking", on_court=False)

print("Initial Info:")
setter.display_info()
outside_hitter.display_info()

setter.enter_court()
outside_hitter.leave_court()

print("Updated Info:")
setter.display_info()
outside_hitter.display_info()

outside_hitter.on_court = True

print("Final Info:")
outside_hitter.display_info()

