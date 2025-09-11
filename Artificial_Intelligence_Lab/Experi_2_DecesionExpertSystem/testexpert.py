from experta import *

class TestEngine(KnowledgeEngine):
    @Rule(Fact(test='ok'))
    def test_rule(self):
        print("Experta is working!")

engine = TestEngine()
engine.reset()
engine.declare(Fact(test='ok'))
engine.run()

