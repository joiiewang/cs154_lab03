import pyrtl
# Simple example of 1-bit 2:1 mux

val_a = pyrtl.Input(bitwidth=1, name='a')
val_b = pyrtl.Input(bitwidth=1, name='b')
select = pyrtl.Input(bitwidth=1, name='select')
result = pyrtl.Output(bitwidth=1, name='result')

# Important: Assignments inside a "conditional_assignment"
# are done with "|=" instead of the usual "<<="
with pyrtl.conditional_assignment:
  with select == 0:
    result |= val_a
  with select == 1:
    result |= val_b