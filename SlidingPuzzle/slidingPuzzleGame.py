import time  # Tinh gio
import sys
sys.path.append("")
from slidingPuzzleController import createBoard,findGoalState,Solve
from utils import utils
from nodeSlidingPuzzle import heuristic
from nodeSlidingPuzzle.Node import Node


start = time.time()  # bat dau tinh gio

#Khỏi tạo n và tên thuật toán
n = 15##khởi tạo giá trị cho n
algorithms="HUMAN"# A_STAR,BFS,DFS,IDS

##Creat Board  2 tùy chọn  cách 1 là dùng file input
board = createBoard(2,n)#board = createBoard(1,n) cách 2 là auto
print("Problem")
utils.plain_print(board)  # in thử ra bài toán
##Find goalStates
goal_states_all=findGoalState(algorithms,n)
goal_states=goal_states_all[0]
goal_states_point=goal_states_all[1]#cần với human do human dùng nhiều if else
for liststate in goal_states:  # in ra thử các đích
    print(liststate)
##Solve
root = Node(board, None, heuristic.manhattan(board, goal_states[0],n), 0, "Start",n)#tạo node root
Solve(algorithms,root,goal_states,goal_states_point,n)#giải

print("Thời gian:                                                 ",time.time()-start)




