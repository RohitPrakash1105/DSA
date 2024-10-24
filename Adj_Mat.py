def add_edge(mat, i, j):
    mat[i][j] = 1  
    mat[j][i] = 1  

def display_matrix(mat):
    for row in mat:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    V = 4  
    
    # Initialize
    mat = [[0] * V for _ in range(V)]  

    # Add edges
    add_edge(mat, 0, 1)
    add_edge(mat, 0, 2)
    add_edge(mat, 1, 2)
    add_edge(mat, 2, 3)

    print("Adjacency Matrix:")
    display_matrix(mat)
