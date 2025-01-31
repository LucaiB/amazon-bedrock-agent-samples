import numpy as np
import matplotlib.pyplot as plt
from termcolor import colored

without_history = "green"
with_history = "blue"

def last_message_analytics(approach_one_data, approach_two_data):
    def get_data(data):
        latencies = list()
        input_tokens = list()
        
        for experiment in data:
            latencies.append(experiment[-1]["latency"])
            input_tokens.append(experiment[-1]["inputTokens"])

        return latencies, input_tokens

    approach_one_latencies, approach_one_tokens = get_data(approach_one_data)
    approach_two_latencies, approach_two_tokens = get_data(approach_two_data)

    print(colored(f"Avg InputTokens without Conversation History: {np.mean(approach_one_tokens)}", without_history))
    print(colored(f"Avg Latency without Conversation History: {np.mean(approach_one_latencies)}s", without_history))
    print(colored(f"Avg InputTokens with Conversation History: {np.mean(approach_two_tokens)}", with_history))
    print(colored(f"Avg Latency with Conversation History: {np.mean(approach_two_latencies)}s", with_history))

    # Create a figure and a 2x2 grid of subplots
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    
    # Plot data on each subplot
    axs[0, 0].boxplot(approach_one_tokens)
    axs[0, 0].set_xlabel('Average inputTokens')
    axs[0, 0].set_title('Avg InputTokens without Conversation History - Last Message')

    axs[0, 1].boxplot(approach_one_latencies)
    axs[0, 1].set_xlabel('Average Latency')
    axs[0, 1].set_title('Avg Latency without Conversation History - Last Message')
    # Plot data on each subplot
    axs[1, 0].boxplot(approach_two_tokens)
    axs[1, 0].set_xlabel('Average inputTokens')
    axs[1, 0].set_title('Avg InputTokens with Conversation History - Last Message')

    axs[1, 1].boxplot(approach_two_latencies)
    axs[1, 1].set_xlabel('Average Latency')
    axs[1, 1].set_title('Avg Latency with Conversation History - Last Message')  



def create_token_boxplot(approach_one_data, approach_two_data):
    # Assuming the data is stored in the variable 'data'

    def get_all_tokens(data):
        input_tokens = []
        output_tokens = []
        
        for experiment in data:
            for turn in experiment:
                input_tokens.append(turn['inputTokens'])
                output_tokens.append(turn['outputTokens'])
        
        # Convert the list to a NumPy array
        input_tokens_arr = np.array(input_tokens)
        output_tokens_arr = np.array(output_tokens)

        return input_tokens_arr, output_tokens_arr

    input_tokens_one, output_tokens_one = get_all_tokens(approach_one_data)
    input_tokens_two, output_tokens_two = get_all_tokens(approach_two_data)
    
    print(colored(f"Avg InputTokens without Conversation History: {np.mean(input_tokens_one)}", without_history))
    print(colored(f"Avg OutputTokens without Conversation History: {np.mean(output_tokens_one)}", without_history))
    print(colored(f"Avg InputTokens with Conversation History: {np.mean(input_tokens_two)}", with_history))
    print(colored(f"Avg OutputTokens with Conversation History: {np.mean(output_tokens_two)}", with_history))

    # Create a figure and a 2x2 grid of subplots
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    
    # Plot data on each subplot
    axs[0, 0].boxplot(input_tokens_one)
    axs[0, 0].set_xlabel('Average InputTokens')
    axs[0, 0].set_title('Avg InputTokens without Conversation History')

    axs[0, 1].boxplot(output_tokens_one)
    axs[0, 1].set_xlabel('Average OutputTokens')
    axs[0, 1].set_title('Avg OutputTokens without Conversation History')
    # Plot data on each subplot
    axs[1, 0].boxplot(input_tokens_two)
    axs[1, 0].set_xlabel('Average InputTokens')
    axs[1, 0].set_title('Avg InputTokens with Conversation History')

    axs[1, 1].boxplot(output_tokens_two)
    axs[1, 1].set_xlabel('Average OutputTokens')
    axs[1, 1].set_title('Avg OutputTokens with Conversation History')  
    # Show the plot
    plt.show()
    
def create_latency_boxplot(approach_one_data, approach_two_data):
    # Assuming the data is stored in the variable 'data'

    def get_all_latencies(data):
        all_latencies = []
        
        for experiment in data:
            for turn in experiment:
                latency = turn['latency']
                all_latencies.append(latency)
        
        # Convert the list to a NumPy array
        latencies_array = np.array(all_latencies)
        return latencies_array

    latencies_array_one = get_all_latencies(approach_one_data)
    latencies_array_two = get_all_latencies(approach_two_data)
    
    print(colored(f"Avg Latency without Conversation History: {np.mean(latencies_array_one)}s", without_history))
    print(colored(f"Avg Latency with Conversation History: {np.mean(latencies_array_two)}s", with_history))

    # Create a figure and a 2x2 grid of subplots
    fig, axs = plt.subplots(2, figsize=(10, 10))
    
    # Plot data on each subplot
    axs[0].boxplot(latencies_array_one)
    axs[0].set_xlabel('Average Latency')
    axs[0].set_title('Avg Latency without Conversation History')

    axs[1].boxplot(latencies_array_two)
    axs[1].set_xlabel('Average Latency')
    axs[1].set_title('Avg Latency with Conversation History')
        
    # Show the plot
    plt.show()