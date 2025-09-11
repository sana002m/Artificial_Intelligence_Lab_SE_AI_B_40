class ExpertSystem:
    def __init__(self):
        self.knowledge_base = []
        self.facts = set()

    def ask(self, question):
        answer = input(question + " (yes/no): ").strip().lower()
        return answer == "yes"

    def add_rule(self, condition, conclusion):
        self.knowledge_base.append((condition, conclusion))

    def evaluate(self):
        applied = True
        while applied:
            applied = False
            for condition, conclusion in self.knowledge_base:
                if condition(self.facts) and conclusion not in self.facts:
                    print(f"Inferred: {conclusion}")
                    self.facts.add(conclusion)
                    applied = True

    def run(self):
        print("🌿 Welcome to the Plant Doctor Expert System!")
        # Initial user facts
        if self.ask("Are the leaves yellow?"):
            self.facts.add("yellow_leaves")
        if self.ask("Is the soil wet?"):
            self.facts.add("wet_soil")
        if self.ask("Is the plant in direct sunlight?"):
            self.facts.add("direct_sunlight")

        self.evaluate()

        print("\n✅ Final conclusions:")
        for fact in self.facts:
            if fact.startswith("diagnosis:"):
                print("-", fact.replace("diagnosis:", ""))


# Define the system
system = ExpertSystem()

# Add rules (condition, conclusion)
system.add_rule(lambda facts: "yellow_leaves" in facts and "wet_soil" in facts,
                "diagnosis:Overwatering")
system.add_rule(lambda facts: "yellow_leaves" in facts and "direct_sunlight" in facts,
                "diagnosis:Sunburn")
system.add_rule(lambda facts: "yellow_leaves" in facts and "wet_soil" not in facts,
                "diagnosis:Underwatering")
system.add_rule(lambda facts: "yellow_leaves" not in facts and "direct_sunlight" in facts,
                "diagnosis:Too much light")

# Run the system
if __name__ == "__main__":
    system.run()




