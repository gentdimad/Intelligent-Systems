import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib as plt

weight = ctrl.Antecedent(np.arange(0, 101, 1), 'weight')
height = ctrl.Antecedent(np.arange(0, 201, 1), 'height')
BMI = ctrl.Consequent(np.arange(0, 41, 1), 'BMI')

weight.automf(5)
height.automf(5)

# weight.view()

BMI['low'] = fuzz.trimf(BMI.universe, [0, 15, 23])
BMI['fair'] = fuzz.trimf(BMI.universe, [15, 23, 27])
BMI['normal'] = fuzz.trimf(BMI.universe, [23, 27, 30])
BMI['high'] = fuzz.trimf(BMI.universe, [27, 30, 41])

rule1 = ctrl.Rule(weight['poor'] & height['poor'], BMI['high'])
rule2 = ctrl.Rule(weight['poor'] & height['mediocre'], BMI['high'])
rule3 = ctrl.Rule(weight['poor'] & height['average'], BMI['low'])
rule4 = ctrl.Rule(weight['poor'] & height['decent'], BMI['low'])
rule5 = ctrl.Rule(weight['poor'] & height['good'], BMI['low'])

rule6 = ctrl.Rule(weight['mediocre'] & height['poor'], BMI['high'])
rule7 = ctrl.Rule(weight['mediocre'] & height['mediocre'], BMI['high'])
rule8 = ctrl.Rule(weight['mediocre'] & height['average'], BMI['normal'])
rule9 = ctrl.Rule(weight['mediocre'] & height['decent'], BMI['fair'])
rule10 = ctrl.Rule(weight['mediocre'] & height['good'], BMI['low'])

rule11 = ctrl.Rule(weight['average'] & height['poor'], BMI['high'])
rule12 = ctrl.Rule(weight['average'] & height['mediocre'], BMI['high'])
rule13 = ctrl.Rule(weight['average'] & height['average'], BMI['normal'])
rule14 = ctrl.Rule(weight['average'] & height['decent'], BMI['normal'])
rule15 = ctrl.Rule(weight['average'] & height['good'], BMI['fair'])

rule16 = ctrl.Rule(weight['decent'] & height['poor'], BMI['high'])
rule17 = ctrl.Rule(weight['decent'] & height['mediocre'], BMI['high'])
rule18 = ctrl.Rule(weight['decent'] & height['average'], BMI['high'])
rule19 = ctrl.Rule(weight['decent'] & height['decent'], BMI['normal'])
rule20 = ctrl.Rule(weight['decent'] & height['good'], BMI['normal'])

rule21 = ctrl.Rule(weight['good'] & height['poor'], BMI['high'])
rule22 = ctrl.Rule(weight['good'] & height['mediocre'], BMI['high'])
rule23 = ctrl.Rule(weight['good'] & height['average'], BMI['high'])
rule24 = ctrl.Rule(weight['good'] & height['decent'], BMI['high'])
rule25 = ctrl.Rule(weight['good'] & height['good'], BMI['normal'])

weightIndex_ctrl = ctrl.ControlSystem({rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25})
weightIndex = ctrl.ControlSystemSimulation(weightIndex_ctrl)

val = input("Please enter weight: ")
val2 = input("Please enter height: ")

weightIndex.input['weight'] = int(val)
weightIndex.input['height'] = int(val2)
weightIndex.compute()

print("\nBMI: " + str(weightIndex.output['BMI']))

input('Press Enter to exit.')

#Gingoyon, Arvic Micah B. BSCS - 3
