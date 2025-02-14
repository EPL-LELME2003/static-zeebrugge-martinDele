import pyomo.environ as pyo

# Create a Pyomo model
model = pyo.ConcreteModel()

# Define model parameters
##########################################
############ CODE TO ADD HERE ############
##########################################

LHV_NH3 = 18.5e6
rho_NH3 = 600

LHV_CH4 = 50e6
rho_CH4 = 500

loss_NH3 = 0.4
eta_NH3 = 1 - loss_NH3 
loss_CH4 = 0.35
eta_CH4 = 1 - loss_CH4

boat_capa = 200e3
nbre_boat = 100

H2_CH4 = 0.25
CO2_CH4 = 2.75

H2_NH3 = 0.18

# Define model variables
##########################################
############ CODE TO ADD HERE ############
##########################################

model.boat_CH4 = pyo.Var(within = pyo.NonNegativeIntegers, bounds = (0,nbre_boat))
model.boat_NH3 = pyo.Var(within = pyo.NonNegativeIntegers, bounds = (0,nbre_boat))

# Define the objective functions
##########################################
############ CODE TO ADD HERE ############
##########################################

model.obj = pyo.Objective(expr = boat_capa*(rho_CH4*H2_CH4*model.boat_CH4 + rho_NH3*H2_NH3*model.boat_NH3), sense = pyo.maximize)

# Define the constraints
##########################################
############ CODE TO ADD HERE ############
##########################################

model.con1 = pyo.Constraint(expr = (model.boat_CH4 + model.boat_NH3 <= 100))
model.con2 = pyo.Constraint(expr = (boat_capa*(rho_CH4*LHV_CH4*model.boat_CH4/eta_CH4 + rho_NH3*LHV_NH3*model.boat_NH3/eta_NH3) <= 3600*140e12))
model.con3 = pyo.Constraint(expr = (boat_capa*rho_CH4*model.boat_CH4*CO2_CH4 <= 14e6*1e3))

# Specify the path towards your solver (gurobi) file
solver = pyo.SolverFactory('gurobi')
sol = solver.solve(model)

# Print here the number of CH4 boats and NH3 boats
##########################################
############ CODE TO ADD HERE ############
##########################################

print('boat_CH4 ->', model.boat_CH4.value)
print('boat_NH3 ->', model.boat_NH3.value)