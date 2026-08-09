from ase import Atoms
from ase.visualize import view 
from ase.calculators.emt import EMT
from ase.io.trajectory import Trajectory
from ase.io import iread
import matplotlib.pyplot as plt

atoms = Atoms("N2", positions=[[0,0,-1],[0,0,1]])
calc = EMT()
atoms.calc = calc

step = 0.1
nsteps =int(6/step)

with Trajectory("nitrogenbinding_curve.traj","w") as traj:
    for i in range(nsteps):
        d = 0.5+i*step
        atoms.positions[1,2]=atoms.positions[0,2]+d

        e = atoms.get_potential_energy()
        f = atoms.get_forces()
        print("distance, energy",d,e)
        print("force",f)
        traj.write(atoms)

energies = []
distances = []

for atoms in iread('nitrogenbinding_curve.traj'):
    energies.append(atoms.get_potential_energy())
    distances.append(atoms.positions[1, 2] - atoms.positions[0, 2])

ax = plt.gca()
ax.plot(distances, energies)
ax.set_xlabel('Distance [Å]')
ax.set_ylabel('Total energy [eV]')
plt.show()

print('Dissociation energy [eV]: ', energies[-1] - min(energies))
