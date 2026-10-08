import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Step 1: Define the SIR model
def sir_model(y, t, beta, gamma, N):
     S, I, R = y
     dS_dt = -beta * S * I / N
     dI_dt = beta * S * I / N - gamma * I
     dR_dt = gamma * I
     return [dS_dt, dI_dt, dR_dt]

# Step 2: Define parameters
# Initial number of people in each compartment
N = 1000       # Total population
I0 = 1         # Initial infected individuals
R0 = 0         # Initial recovered individuals
S0 = N - I0 - R0  # Initial susceptible individuals

# Initial conditions vector
y0 = [S0, I0, R0]

# Transmission and recovery rates
beta = 0.3      # Infection rate
gamma = 0.1     # Recovery rate

# Time points (in days)
t = np.linspace(0, 160, 160)

# Step 3: Integrate the SIR equations over the time grid, t
ret = odeint(sir_model, y0, t, args=(beta, gamma, N))
S, I, R = ret.T

# Step 4: Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, S, 'b', label='Susceptible')
plt.plot(t, I, 'r', label='Infected')
plt.plot(t, R, 'g', label='Recovered')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('SIR Model - Spread of Infection')
plt.legend()
plt.grid()
plt.show()

# Step 5: Experiment with different beta and gamma values
# Let's try a scenario with a higher transmission rate (beta) and a faster recovery rate (gamma)
beta_high = 0.5
gamma_high = 0.2
ret_high = odeint(sir_model, y0, t, args=(beta_high, gamma_high, N))
S_high, I_high, R_high = ret_high.T

# Plot comparison of scenarios
plt.figure(figsize=(10, 6))
plt.plot(t, I, 'r-', label='Infected (beta=0.3, gamma=0.1)')
plt.plot(t, I_high, 'r--', label='Infected (beta=0.5, gamma=0.2)')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('Comparison of Infection Spread with Different Parameters')
plt.legend()
plt.grid()
plt.show()
# new project
