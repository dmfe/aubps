import uuid

from tns import TNS
from gasnn import GASNN
from scenarios import ScenarioRunner


def main():
  scenario_runners = []

  gasnn_scenario_runner = ScenarioRunner(
    str(uuid.uuid4()),
    "gasnn_scenario_thread",
    GASNN()
  )
  tns_scenario_runner = ScenarioRunner(
    str(uuid.uuid4()),
    "tns_scenario_thread",
    TNS()
  )

  gasnn_scenario_runner.start()
  tns_scenario_runner.start()

  scenario_runners.append(gasnn_scenario_runner)
  scenario_runners.append(tns_scenario_runner)

  for runner in scenario_runners:
    runner.join()

  print("Exiting Main Thread")


if __name__ == "__main__":
  main()

