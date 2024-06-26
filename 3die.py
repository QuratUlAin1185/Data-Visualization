from random import randint
from plotly.graph_objects import Bar, Layout
from plotly import offline

class Die:
	def __init__(self, num_sides=6):
		self.num_sides = num_sides

	def roll(self):
		return randint(1, self.num_sides)

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(1000000):
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides

for value in range(3, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

print(frequencies)

x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result', 'dtick':1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title= 'Result of rolling 3 D6 dice 1000000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename='2_d6_d6_d6.html')