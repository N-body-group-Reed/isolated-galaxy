# **Recommendations**
It is recommended that you put a copy of your charmrun and ChaNGa executables in the folder title "code."  This will allow you to run each simulation without copying it to your changa folder.
# **Instructions**
1.  Run the python script init_cond.py using python3.  This should produce a .out file, e.g., halo.out.

2.  Open the .param file and double check that the parameter `achInFile` matches the correct .out file, e.g., `achInFile=halo.out`.

3.  Open the `Makefile` and select the appropriate make command.

4.  Type `make <command>` and let changa run.  `make help` will list all commands and their descriptions.
# **Common Project Rules**
These are a list of naming conventions to follow to maintain ease of use and understandability throughout the project.  These rules should not be changed unless there is majority approval among all administrators or the repository master.

## General Naming Conventions
1.  The python script used to generate initial conditions should be named `init_cond.py`.

2.  Any additional `.py` files that `init_cond.py` depends on shall follow the Snake Case naming convention (https://en.wikipedia.org/wiki/Snake_case) and avoid capital letters.

3.  Parameter files shall have the `.param` file extension type.

4.  Binary files for initial conditions shall either have the `.out` file extension, `.bin` file extension, `.tbin` file extension, or `.std` file extension.  Do not change the file extension type without knowing the connotations behind each extension type.

5.  All simulation names should follow the Camel Case naming convention (https://en.wikipedia.org/wiki/Camel_case) with the first letter as lower case.

## Git rules
1.  New "classes" of simulations should be kept in their own branch.  The user is free to branch from the starting branch as many times as necessary.

2.  A branch can only be merged back to master once it has no "free" branches attached to it, and it obeys al of the rules outlined here.

3.  If a simulation is significantly complicated, it should include a README detailing the purpose of the simulation.  This is up to he discretion of the repository master.

4.  Merges must be approved by the repository master or an administrator.

5.  The repository master or administrator reserves the right to reject merge requests for *any* reason.  The most common reasons will be a dysfunctional simulation or lack of README.

6.  All simulation makefiles should be free of experimental commands unless the repository master or administrator says otherwise.

## Parameter File Rules
1.  Parameter files shall always have the `.param` file extension.

2.  Parameter file names shall follow the Camel Case naming convention (https://en.wikipedia.org/wiki/Camel_case) with the first letter as lower case.

3.  The parameter file should input parameters in the top down order of the changa options wiki (https://github.com/N-BodyShop/changa/wiki/ChaNGa-Options).

4.  Each "section" in the parameter file will be prefaced with a comment giving the section name.  Any specific **Boundary Conditions Options** will have the comment<br>`#Boundary Conditions Options`<br/>above it.

5.  Additional comments should be kept concise and only added when strictly necessary for better understanding.

## Makefile Rules
1.  Every makefile shall be named `Makefile`.

2.  Every makefile should have a help command that will list the available commands along with a description of their use, e.g., `make help`.

3.  Every makefile shall include a `clean` command.  The purpose of `clean` is to remove generated files, so the simulaiton is returned to its "base" state.

4.  Each command shall start with a lower case character.

5.  A standalone capital "L" indicates that the command will run the simulation exclusively on the local computer.  No indication of "L" indicates that the simulation will be run using ssh abilities.  This should be included as a command sufix.

6.  Prefacing a command with "small" implies that there will be a "big" preface at some point.  "small" indicates that a smaller and less intense version of a simulation will be run.  "big" indicates that a full version of the simulation will be run.  For a medium intensive version of the simulation, preface the command with "med."  No other intensity prefaces are allowed.

7.  Commands that are ready to be used shall follow the Camel Case naming convention (https://en.wikipedia.org/wiki/Camel_case).  These *must* obey all makefile naming convention.

8.  Commands that are experimental or not fully tested/understood shall use the Snake Case naming convention (https://en.wikipedia.org/wiki/Snake_case). They only have to conform to the Snake Case naming convention and are allowed to ignore the other makefile conventions.
## Python Rules
1.  For any one simulation, there shall only be one file named `init_cond.py`.  Similar names are to be avoided.

2.  All python files excluding `init_cond.py`, its dependencies, or any other python scripts related to changa shall be placed in their own separate directory in the simulation clearly named.  This will most likely apply to custom pynbody scripts used to analyze and visualize data.

3.  Python directories shall avoid capital letters.

4.  All python file names shall follow the Snake Case naming convention (https://en.wikipedia.org/wiki/Snake_case), where the first letter is not capitalized.

5.  Code naming should prefer Camel Case naming convention (https://en.wikipedia.org/wiki/Camel_case); however, Snake Case (https://en.wikipedia.org/wiki/Snake_case) is allowed.  Naming should follow some consistent pattern across the entire simulation.  Not having consistent naming conventions is reason for merge rejection.
