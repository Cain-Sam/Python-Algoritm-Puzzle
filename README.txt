Here is the assignment we were to complete:

Apply Graph traversal to solve a problem (Portfolio Project Problem):
You are given a 2-D puzzle of size MxN, that has N rows and M column (N>=3 ; M >= 3; M 
and N can be different). Each cell in the puzzle is either empty or has a barrier. An empty cell 
is marked by ‘-’ (hyphen) and the one with a barrier is marked by ‘#’. You are given two 
coordinates from the puzzle (a,b) and (x,y). You are currently located at (a,b) and want to 
reach (x,y). You can move only in the following directions.

L: move to left cell from the current cell
R: move to right cell from the current cell
U: move to upper cell from the current cell
D: move to the lower cell from the current cell

You can move to only an empty cell and cannot move to a cell with a barrier in it. Your goal 
is to find the minimum number of cells that you have to cover to reach the destination cell 
(do not count the starting cell and the destination cell). The coordinates (0,0) represent the 
first cell; (0,1) represents the second cell in the first row. If there is not possible path from 
source to destination return None.

Sample Input Puzzle Board: [[-,-,-,-,-],[-,-,#,-,-],[-,-,-,-,-],[#,-,#,#,-],[-#,-,-,-]]
- - - - -
- - # - -
- - - - -
# - # # -
- # - - -

Example 1: solve_puzzle(board, (0, 2), (2, 2))
Output: [(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)]
On possible direction to travel: LDDR

Example 2: solve_puzzle(board, (0, 0), (4, 4))
Output: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
One possible direction to travel: DDRRRRDD

Example 3: solve_puzzle(board, (0, 0), (4, 0))
Output: None