
**Dinitrogen equilibrium bond length**

I used the effective medium theory (EMT) calculator to calculate potential energy [https://docs.ase-lib.org/ase/calculators/emt.html](url) for several bond lengths. 
The EMT calculator is a classical semi-empirical method designed for quick tests with face-centered cubic metals. It is explicitly stated in the link referencing EMT that it is not intended for an element such as nitrogen.
I did the calculation with EMT anyway and it should not come as a surprise that the results deviate somewhat from expected values. I got an equilibrium bond length of 1.00 Å and a dissociation energy of 9.94 eV. 
The dissociation energy was calculated by subtracking: last index of potential energy - minimum potential energy.

(I am not taking credit for the code it was written by someone from [https://docs.ase-lib.org/examples_generated/01-gettingstarted/01-atoms-and-calculators.html](url))

**Water structure optimization**

Originally I wanted to follow an ASE tutorial on water structure optimization that uses the GPAW calculator. Unfortunately I could not figure out how to install it so I just used EMT. On the plus side since I could not get GPAW to work I did not follow the ASE tutorial very closely and most of the code I wrote this time is original and probably kind of bad. But as of right now I am somewhat proud of my own water structure optimization. I set a convergence criteria of 0.1 eV and I got an O-H bond length of 1.11 Å and H-O-H bond angle of 104.81 degrees. I would say this is pretty good considering the calculator I used and the crude way in which I set up the optimization.
