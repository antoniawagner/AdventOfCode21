#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:20:12 2021

@author: antonia
"""
import re
import copy
#%%
with open('/home/antonia/Documents/AdventCode/adv4.dat', 'r') as f:
    data=f.read()
    bingo_boards_list=[[[int(num) for num in re.split('  | ',line) if num!=''] for line in matrix.split('\n') if line!=''] for matrix in data.split('\n\n') if matrix!='']
#%%
with open(r'/home/antonia/Documents/AdventCode/adv4_draw_numbers.dat','r') as g:
    datag=g.read()
    draw_numbers=[[int(num) for num in datag.split(',')]][0]

#%%
flag= True
result_list = [ [[0]*len(bingo_boards_list[0]),[0]*len(bingo_boards_list[0])] for _ in range(len(bingo_boards_list)) ]
rem_num_win_boards_list=copy.deepcopy(bingo_boards_list)
winning_board_list=[]
for dn in draw_numbers:
    for board in range(0,len(bingo_boards_list)):
        for row in range(0, len(bingo_boards_list[board])):
            for column in range(0, len(bingo_boards_list[board][row])):
                if bingo_boards_list[board][row][column]==dn:
                    rem_num_win_boards_list[board][row][column]=0
                    result_list[board][0][row]+=1
                    result_list[board][1][column]+=1
                    if 5 in (result_list[board][k][l] for k in range(len(result_list[board])) for l in range(len(result_list[board][k]))):
                        winning_board_list.append(board) if board not in winning_board_list else winning_board_list
    if (any(5 in result_list[n][m] for n in range(len(result_list)) for m in range(len(result_list[n]))) and flag):
        print('First winning bingo board=',winning_board_list[0])
        print('Answer 1:',sum(sum(x) for x in rem_num_win_boards_list[winning_board_list[0]])*dn)
        flag = False
    if all(any(5 in result_list[t][i] for i in(0,1)) for t in range(len(result_list))):
        print('Last winning bingo board=',winning_board_list[-1])
        print('Answer 2:',sum(sum(x) for x in rem_num_win_boards_list[winning_board_list[-1]])*dn)
        break