class DFA:
    def __init__(self, name, states, alphabet, transitions, start_state, final_states):
        self.name = name  # Added name attribute for the DFA
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def validate(self, input_string):
        current_state = self.start_state
        transition_log = []  # To store the transitions

        for symbol in input_string:
            if symbol in self.transitions[current_state]:
                next_state = self.transitions[current_state][symbol]
                # Record the transition
                transition_log.append((current_state, symbol, next_state))
                current_state = next_state
            else:
                return False, transition_log  # Invalid transition

        return current_state in self.final_states, transition_log


# DFA definition
name = "ShoppingDFA"  # Name of the DFA
states = {'q0', 'q1', 'q2', 'q3', 'q4'}
alphabet = {'e', 'a', 'd', 'c', 'x'}
transitions = {
    'q0': {'e': 'q1'},
    'q1': {'a': 'q2', 'c': 'q2'},
    'q2': {'a': 'q2', 'd': 'q2', 'c': 'q3'},
    'q3': {'x': 'q4'}
}
start_state = 'q0'
final_states = {'q4'}

# Create DFA
shopping_dfa = DFA(name, states, alphabet, transitions, start_state, final_states)

# Loop to accept user input
print("Enter strings to test the DFA (type 'exit' to quit):")
while True:
    user_input = input("Enter a string: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    elif all(symbol in alphabet for symbol in user_input):
        is_valid, transition_log = shopping_dfa.validate(user_input)
        if is_valid:
            print(f"Accept ({user_input}): Have a great day!")
            print("Transitions:")
            for transition in transition_log:
                print(f"{transition[0]} {transition[1]} {transition[2]}")
        else:
            print(f"reject")
    else:
        print("Unrecognized character(s)! Please use e, a, d, c, and x for your string!")
