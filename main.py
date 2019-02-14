from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

matrix2=new_matrix()
ident(matrix)
print_matrix(matrix)
print_matrix(matrix2)
matrix_mult(matrix,matrix2)
print_matrix(matrix)
print_matrix(matrix2)


'''print_matrix(matrix)
add_edge(matrix,12,234,0,500,500,500)
add_edge(matrix,124,2,0,400,200,300)
print_matrix(matrix)'''
draw_lines( matrix, screen, color )
display(screen)
