"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    row=0
    col=0
    box=""
    while col<len(matrix[0]):
        while row<len(matrix):
            box+=str(matrix[row][col])+" "
            row+=1
        row=0
        col+=1
        box+="\n"
    print (box)
    #pass

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    i=0
    while i<len(matrix):
        j=0
        while j<len(matrix[i]):
            if i!=j:
                matrix[i][j]=0
            if i==j:
                matrix[i][j]=1
            j+=1
        i+=1
    #pass

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m=[]
    for i in m1:
        list2=[]
        col=0
        for j in i:
            count=0
            c=0
            for a in m2:
                a[c]
                while k in m2:
                    count+=a
                #k[i]=k[
            j+=1
            list2.append[count]
        m.append(list2)
        i+=1
    m2=m
    #pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
