# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
# train_distance = 100
bomb_mass = 1


# Write your code below: 

def f_to_c(tempf):
  tempc = (tempf - 32) * 5/9
  return tempc
f100_in_celsius = f_to_c(100)

def c_to_f(tempc):
  tempf = tempc * (9/5) + 32
  return tempf
c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c = 3*10**8):
  return mass * c**c
bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + bomb_energy + " Joules.")

def get_work(mass, acceleration, distance):
  return get_force() * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " str(train_work) + " Joules of work over " + str(train_distance) + " meters."