from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
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

'''print_matrix(matrix)
add_edge(matrix,12,234,0,500,500,500)
add_edge(matrix,124,2,0,400,200,300)
print_matrix(matrix)'''
draw_lines( matrix, screen, color )
draw_lines( A, screen, color )
draw_lines( B, screen, color )
display(screen)
