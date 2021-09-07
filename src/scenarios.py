import threading


class ScenarioRunner (threading.Thread):
  def __init__(self, thread_id, name, scenario):
    threading.Thread.__init__(self)
    self.thread_id = thread_id
    self.name = name
    self.scenario = scenario

  def run(self):
    print("Starting thread " + self.name)

    self.scenario.execute()

    print("Exiting thread " + self.name)
