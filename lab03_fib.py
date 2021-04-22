import pyrtl

A = pyrtl.Input(bitwidth=32, name='A')
B = pyrtl.Input(bitwidth=32, name='B')

result = pyrtl.Output(bitwidth=32, name='result')

fib1=pyrtl.Register(bitwidth=32, name = 'fib1')
fib2=pyrtl.Register(bitwidth=32, name = 'fib2')
cycle=pyrtl.Register(bitwidth=1, name = 'fib2')

with pyrtl.conditional_assignment:
    with cycle==0:
        fib1.next |= A
        fib2.next |= B 
        cycle.next |=1
        result |= A 

    with cycle !=0:
        fib.next |= fib2
        fib2.next |= fib1+fib2
        result |= fib2

sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer = sim_trace)

import random
for cycle in range(16):
    # Call "sim.step" to simulate each clock cycle of the design
    sim.step({
        'A': 1,
        'B': 2,
    
        })

# Print the trace results to the screen.
sim_trace.render_trace()
