#packages
import time
import random

class Simulation:
    def __init__(self):
        self.running = True
        self.success_counter = 0
        self.num_of_results = 0
        self.goal_inarow = 0
        self.seconds_per_trial = 0
        self.goal_number = 0

    def choose_object(self):
        print("An object is something with an equal chance to land on each side."
              "\nSome Examples:"
              "\n1.) 2 sides: coin"
              "\n2.) 6 sides: dice")
        while True:
            try:
                self.num_of_results = int(input("Enter how many sides your chance object has: "))
                return self.num_of_results
            except:
                print("Invalid input. Please try again.")


    def simulate(self):
        trials = 1
        current_inarow = 0
        initial_time = time.time()
        while self.running:
            number = random.randint(1,self.num_of_results)
            if number == self.goal_number:
                current_inarow +=1
                trials += 1

            else:
                current_inarow = 0
                trials += 1

            if current_inarow == self.goal_inarow:
                print("Goal Reached! There were '" +str(trials)+ "' trials.")
                self.taken_time(trials)

                self.running = False
                break
            if trials % 1000000*(trials*60) == 0:
                print("This much time has passed:")
                print(time.time()-initial_time)

        return trials

    def taken_time(self,trials):
        if trials * self.seconds_per_trial > 259200:
            print("Let's say that it took you " + str(self.seconds_per_trial) + " seconds per trial"
            "\nThis trial would've taken " + str((trials * self.seconds_per_trial) / 86400) + " days!")
        elif trials * self.seconds_per_trial > 1051200:
            print("Let's say that it took you " + str(self.seconds_per_trial) + " seconds per trial"
            "\nThis trial would've taken " + str((trials * self.seconds_per_trial) / 8760) + " years!")
        elif trials * self.seconds_per_trial > 86500000:
            print("Let's say that it took you " + str(self.seconds_per_trial) + " seconds per trial"
                "\nThis trial would've taken " + str((trials * self.seconds_per_trial) / 1440000) + " millennia !")
        else:
            print("Let's say that it took you " + str(self.seconds_per_trial) + " seconds per trial"
            "\nThis trial would've taken " + str((trials * self.seconds_per_trial) / 3600) + " hours!")



    def single_trial(self):
        self.goal_inarow = int(input("Enter how many lands 'in-a-row' you want to get on your object"))
        print("Enter the number you want to land on. (Ex: for a dice you might want it to land on 3)")
        self.goal_number = int(input("Enter that number here: "))
        self.seconds_per_trial = int(input("Enter how many seconds each trial would take in real life: "))
        print("Flipping Coins, Rolling Dice, and Simulating......This might take awhile.")
        self.simulate()

    def average_trials(self):
        self.goal_inarow = int(input("Enter how many lands 'in-a-row' you want to get on your object"))
        print("Enter the number you want to land on. (Ex: for a dice you might want it to land on 3)")
        self.goal_number = int(input("Enter that number here: "))
        self.seconds_per_trial = int(input("Enter how many seconds each trial would take in real life: "))
        simulation_trials = int(input("Enter how many times you want to simulate this (to average out the final value): "))
        print("Flipping Coins, Rolling Dice, and Simulating......This might take awhile.")
        trial_sum = 0
        simulation_attempts = 1
        while True:
            if simulation_attempts <= simulation_trials:
                trial_sum += self.simulate()
                print(trial_sum)
                print("trial sum above")
                simulation_attempts += 1
            else:
                print("There were "+ str(simulation_attempts) + " total simulations run.")
                print("The average trial value was: " + str(trial_sum/simulation_attempts))
                self.taken_time(trial_sum)
                break
simulation = Simulation()
simulation.num_of_results = simulation.choose_object()
simulation.single_trial()

