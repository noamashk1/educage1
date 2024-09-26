import json
from typing import List, Dict, Any
import reward_and_punishment_system
import trial
import level
import data_analysis

class Experiment:
    def __init__(self, mice: List[Mouse], levels: Dict[int, Level]):
        self.mice = mice
        self.levels = levels
        self.results = []

    def run_trial(self, mouse: Mouse):
        parameters = mouse.level.get_parameters()

        # Example stimulus interaction (simply mocked for demonstration)
        stimulus = Stimulus(stimulus_id=1, stimulus_type='light', duration=2.0)
        stimulus.play()

        # Simulated response (In a real scenario, this would come from the user's input)
        response = 'correct'  # Replace this with actual response capturing.

        reward_system = RewardAndPunishmentSystem()
        reward_type = reward_system.evaluate_response(response)

        # Record the result
        trial_data = {
            'mouse_id': mouse.id,
            'level': mouse.level.level_id,
            'response': response,
            'outcome': reward_type
        }
        mouse.record_performance(trial_data)
        self.results.append(trial_data)

        # Deliver reward or punishment
        if reward_type == 'reward':
            reward_system.deliver_reward()
        else:
            reward_system.impose_punishment()

    def change_mouse_level(self, mouse: Mouse, new_level: Level):
        mouse.update_level(new_level)

    def save_results(self, filename: str):
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=4)

# class Mouse:
#     def __init__(self, mouse_id: int, level: 'Level'):
#         self.id = mouse_id
#         self.level = level
#         self.performance_data = []
#
#     def update_level(self, new_level: 'Level'):
#         self.level = new_level
#
#     def record_performance(self, trial_data: Dict[str, Any]):
#         self.performance_data.append(trial_data)
#
#
#
#
# class Stimulus:
#     def __init__(self, stimulus_id: int, stimulus_type: str, duration: float):
#         self.stimulus_id = stimulus_id
#         self.type = stimulus_type
#         self.duration = duration
#
#     def play(self):
#         print(f"Playing stimulus: {self.type} for {self.duration} seconds.")

# Example usage:
if __name__ == "__main__":
    # Create levels
    level_1 = Level(level_id=1, parameters={'stimuli': ['light', 'sound'], 'reaction_time': '2s'})
    level_2 = Level(level_id=2, parameters={'stimuli': ['noise', 'visual'], 'reaction_time': '1s'})

    # Create mice
    mouse_1 = Mouse(mouse_id=1, level=level_1)
    mouse_2 = Mouse(mouse_id=2, level=level_1)

    # Create an experiment
    experiment = Experiment(mice=[mouse_1, mouse_2], levels={1: level_1, 2: level_2})

    # Run trials
    experiment.run_trial(mouse_1)
    experiment.run_trial(mouse_2)

    # Save results to a file
    experiment.save_results('experiment_results.json')

    print("Experiment completed and results saved.")
