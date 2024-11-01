from pulp import LpMaximize, LpProblem, LpVariable

# ініціалізація моделі
model = LpProblem("Maximize_Beverage_Production", LpMaximize)

# визначення змінних
L = LpVariable("Lemonade", lowBound=0, cat="Integer")
J = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# цільова функція
model += L + J, "Total_Products"

# обмеження
model += 2 * L + J <= 100, "Water_Constraint"
model += L <= 50, "Sugar_Constraint"
model += L <= 30, "Lemon_Juice_Constraint"
model += 2 * J <= 40, "Fruit_Puree_Constraint"

model.solve()

# результати
print(f"Optimal number of Lemonade: {L.varValue}")
print(f"Optimal number of Fruit Juice: {J.varValue}")
print(f"Total produced products: {model.objective.value()}")