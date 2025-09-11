from experta import *

class AgeFacts(Fact):
    """Info about the person's age"""
    pass

class AgeDecisionEngine(KnowledgeEngine):

    @Rule(AgeFacts(age=P(lambda x: x >= 18)))
    def can_vote_and_drive(self):
        print("You are eligible to vote and drive.")

    @Rule(AgeFacts(age=P(lambda x: 16 <= x < 18)))
    def can_drive_only(self):
        print("You are eligible to drive but not vote.")

    @Rule(AgeFacts(age=P(lambda x: x < 16)))
    def too_young(self):
        print("You are too young to vote or drive.")

# Main code to run
if __name__ == "__main__":
    age = int(input("Enter your age: "))
    engine = AgeDecisionEngine()
    engine.reset()
    engine.declare(AgeFacts(age=age))
    engine.run()

