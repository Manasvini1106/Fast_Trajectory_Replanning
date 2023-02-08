# Fast_Trajectory_Replanning

This project is the collective effort of
1. Manasvini Nittala (Net ID: mn777)

2. Sahithi Reddy Sakinala (Net ID: ss4362)

3. Jahnavi Manchala (Net ID: jm2658)


In the Fast Trajectory Replanning Folder there are 5 folders, 50 text files and 4 code files.


1. __pycache__ and venv folders are for the code

2. References folder contains the references (research articles and websites) used.

3. Report folder contains the Report in both latex and word format. The "report latex code" folder inside the "Report" folder contains the latex code for the typeset PDF.

4. Comparison Output folder has the excel sheet with the run time and distance of the 3 algorithms for the 50 grid worlds and also a comparison graph.

5. The 50 text files are the randomly generated grid worlds with 30% blocked cells.

6. generate.py: This code file generates 50 grid worlds of size 101x101 with DFS and stores them in the folder where our project is.

7. Astar.py: This code file has the class Astar which contains the methods "Repeated Forward A*", "Repeated Backward A*" and "Adaptive A*"

8. main.py: This is the main code file, after running this a grid world of our choice will be opened and by pressing "1" on our keyboard we can run "Repeated Forward A*", by pressing "2" we can run "Repeated Backward A*", by pressing "3" we can run "Adaptive A*" and by pressing "c" we can clear the entire grid world.

9. comparison.py: This file contains the code for generating comparison graphs for the 3 algorithms with respect to their run time.

