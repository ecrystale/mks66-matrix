from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 200, 0, 200 ]
matrix = new_matrix()

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
matrix_mult(A,B)
print_matrix(A)
print_matrix(B)
matrix_mult(B,A)  
print_matrix(A)
print_matrix(B)
ident(matrix)
print_matrix(matrix)
matrix_mult(matrix,A)
print_matrix(A)

'''
matrix2=new_matrix()
ident(matrix)
print_matrix(matrix)
print_matrix(matrix2)
matrix_mult(matrix,matrix2)
print_matrix(matrix)
print_matrix(matrix2)
'''
m=[]
x1=0
y1=250
x2=250
y2=500
x3=500
y3=0
count=0
change=1
while x1<x2 and y2>y1:
    add_edge(m,x1,y1,0,x2,y2,0)
    add_edge(m,x2,y2,0,x3,y1,0)
    add_edge(m,x3,y1,0,x2,y3,0)
    add_edge(m,x2,y3,0,x1,y1,0)
    x1+=3
    y1+=3
    x2-=3
    y2-=3
    x3-=3
    y3+=3
        
    
#add_edge(m,124,2,0,400,200,300)
#print_matrix(m)

draw_lines( m, screen, color )
display(screen)
