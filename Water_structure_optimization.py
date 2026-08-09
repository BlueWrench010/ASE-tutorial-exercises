from ase import Atoms
from ase.visualize import view 
from ase.calculators.emt import EMT
from ase.io.trajectory import Trajectory
from ase.io import read
from ase import units
import math
import matplotlib.pyplot as plt

atoms = Atoms("H2O", positions=[[-1,-1,0],[1,-1,0],[0,0,0]]) # I interpret this as [x,y,z]
atoms.center(vacuum=3)
calc = EMT()
atoms.calc = calc

timestep = 0.1*units.fs
maxsteps = 10
step_index = 0
convergence_criteria = .1 #in eV

energies = [atoms.get_potential_energy()]
time = [0]
Delta_energies = []
Delta_e = 10000

with Trajectory("water_structure_optimization.traj","w") as traj:
    while (Delta_e > convergence_criteria) and (step_index < maxsteps):
        e = atoms.get_potential_energy()
        if(step_index > 0):
            Delta_e = abs(energies[-1] - e)
            Delta_energies.append(Delta_e)

        f = atoms.get_forces()
        #Hydrogen 1
        atoms.positions[0,0] = atoms.positions[0,0]+timestep*f[0,0] #Hydrogen 1x
        atoms.positions[0,1] = atoms.positions[0,1]+timestep*f[0,1] #Hydrogen 1y
        atoms.positions[0,2] = atoms.positions[0,2]+timestep*f[0,2] #Hydrogen 1z

        #Hydrogen 2
        atoms.positions[1,0] = atoms.positions[1,0]+timestep*f[1,0] #Hydrogen 2x
        atoms.positions[1,1] = atoms.positions[1,1]+timestep*f[1,1] #Hydrogen 2y
        atoms.positions[1,2] = atoms.positions[1,2]+timestep*f[1,2] #Hydrogen 2z

        #Oxygen
        atoms.positions[2,0] = atoms.positions[2,0]+timestep*f[2,0] #Oxygen x
        atoms.positions[2,1] = atoms.positions[2,1]+timestep*f[2,1] #Oxygen y
        atoms.positions[2,2] = atoms.positions[2,2]+timestep*f[2,2] #Oxygen z

        energies.append(e)
        print("energy",e)
        print("force",f)
        print("Delta energi", Delta_e)
        print("stepindex", step_index)
        traj.write(atoms)
        step_index += 1
        time.append(step_index*0.1)

if(step_index >= maxsteps):
    print("Max steps reached")
elif(Delta_energies[-1] <= convergence_criteria):
    print("Optimization Converged")

print("energies", energies)
print("time",time)
print("Delta energies" , Delta_energies)

def Distance_formula(atom1_index, atom2_index):
    return math.sqrt((atoms.positions[atom2_index,0]-atoms.positions[atom1_index,0])**2 + (atoms.positions[atom2_index,1]-atoms.positions[atom1_index,1])**2+(atoms.positions[atom2_index,2]-atoms.positions[atom1_index,2])**2)
OH1_bondlength = Distance_formula(0,2)
OH2_bondlength = Distance_formula(1,2)
H1H2_dist = Distance_formula(0,1)
print("O-H1 bond length:",OH1_bondlength, "Å")
print("O-H2 bond length:",OH1_bondlength, "Å")

cos_theta = (OH1_bondlength**2 + OH2_bondlength**2 - H1H2_dist**2) / (2 * OH1_bondlength * OH2_bondlength)
cos_theta = max(-1.0, min(1.0, cos_theta))
bond_angle = math.degrees(math.acos(cos_theta))
print(f"H-O-H Bond Angle: {bond_angle:.2f}°") 

ax = plt.gca()
ax.plot(time, energies)
ax.set_xlabel('Time [fs]')
ax.set_ylabel('Total energy [eV]')
plt.show()

atoms_anim = read('water_structure_optimization.traj', ':')
view(atoms_anim)