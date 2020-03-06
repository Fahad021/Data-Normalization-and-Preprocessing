
print('TASK 2 - START')

# to compute distance need to convert the dataframe to an array
wine_data_red   = np.array(wine_data_red)
wine_data_white = np.array(wine_data_white)

print('manhatten distance')

print('manhatten distance for RED WINE')

manhatten_dist_red_matrix = distance.cdist(wine_data_red, wine_data_red, metric='cityblock')
# print(tabulate(manhatten_dist_red_matrix, tablefmt='fancy_grid'))

manhatten_dist_red_output = np.zeros([10,2])

# max values or the farthest values
manhatten_dist_red_output[:,1] = np.amax(manhatten_dist_red_matrix,axis=1)

# as the distances are 0s along the diagonal of the matrix
# after capturing the max values and before finding  the min values
# we are assigning inf to the diagonal values
for i in range (0, len(manhatten_dist_red_matrix[0,:])):
    for j in range (0, len(manhatten_dist_red_matrix[0,:])):
        if i==j:
            manhatten_dist_red_matrix[i,j] = np.inf
#print(tabulate(manhatten_dist_red_matrix, tablefmt='fancy_grid'))

# min values or the nearest values
manhatten_dist_red_output[:,0] = np.amin(manhatten_dist_red_matrix,axis=1)
print(tabulate(manhatten_dist_red_output,headers=["nearest", "farthest"], tablefmt='fancy_grid'))


print('manhatten distance for WHITE WINE')

manhatten_dist_white_matrix = distance.cdist(wine_data_white, wine_data_white, metric='cityblock')
# print(tabulate(manhatten_dist_white_matrix, tablefmt='fancy_grid'))

manhatten_dist_white_output = np.zeros([10,2])

# max values or the farthest values
manhatten_dist_white_output[:,1] = np.amax(manhatten_dist_white_matrix,axis=1)

# as the distances are 0s along the diagonal of the matrix
# after capturing the max values and before finding  the min values
# we are assigning inf to the diagonal values
for i in range (0, len(manhatten_dist_white_matrix[0,:])):
    for j in range (0, len(manhatten_dist_white_matrix[0,:])):
        if i==j:
            manhatten_dist_white_matrix[i,j] = np.inf
#print(tabulate(manhatten_dist_white_matrix, tablefmt='fancy_grid'))

# min values or the nearest values
manhatten_dist_white_output[:,0] = np.amin(manhatten_dist_white_matrix,axis=1)
print(tabulate(manhatten_dist_white_output,headers=["nearest", "farthest"], tablefmt='fancy_grid'))




print('euclidean distance')

print('euclidean distance for RED WINE')

euclidean_dist_red_matrix = distance.cdist(wine_data_red, wine_data_red, metric='euclidean')
# print(tabulate(euclidean_dist_red_matrix, tablefmt='fancy_grid'))

euclidean_dist_red_output = np.zeros([10,2])

# max values or the farthest values
euclidean_dist_red_output[:,1] = np.amax(euclidean_dist_red_matrix,axis=1)

# as the distances are 0s along the diagonal of the matrix
# after capturing the max values and before finding  the min values
# we are assigning inf to the diagonal values
for i in range (0, len(euclidean_dist_red_matrix[0,:])):
    for j in range (0, len(euclidean_dist_red_matrix[0,:])):
        if i==j:
            euclidean_dist_red_matrix[i,j] = np.inf
#print(tabulate(euclidean_dist_red_matrix, tablefmt='fancy_grid'))

# min values or the nearest values
euclidean_dist_red_output[:,0] = np.amin(euclidean_dist_red_matrix,axis=1)
print(tabulate(euclidean_dist_red_output,headers=["nearest", "farthest"], tablefmt='fancy_grid'))


print('euclidean distance for WHITE WINE')

euclidean_dist_white_matrix = distance.cdist(wine_data_white, wine_data_white, metric='euclidean')
# print(tabulate(euclidean_dist_white_matrix, tablefmt='fancy_grid'))

euclidean_dist_white_output = np.zeros([10,2])

# max values or the farthest values
euclidean_dist_white_output[:,1] = np.amax(euclidean_dist_white_matrix,axis=1)

# as the distances are 0s along the diagonal of the matrix
# after capturing the max values and before finding  the min values
# we are assigning inf to the diagonal values
for i in range (0, len(euclidean_dist_white_matrix[0,:])):
    for j in range (0, len(euclidean_dist_white_matrix[0,:])):
        if i==j:
            euclidean_dist_white_matrix[i,j] = np.inf
#print(tabulate(euclidean_dist_white_matrix, tablefmt='fancy_grid'))

# min values or the nearest values
euclidean_dist_white_output[:,0] = np.amin(euclidean_dist_white_matrix,axis=1)
print(tabulate(euclidean_dist_white_output,headers=["nearest", "farthest"], tablefmt='fancy_grid'))





print('cosine distance')

print('cosine distance for RED WINE')

cosine_dist_red_matrix = distance.cdist(wine_data_red, wine_data_red, metric='cosine')
# print(tabulate(cosine_dist_red_matrix, tablefmt='fancy_grid'))

cosine_dist_red_output = np.zeros([10,2])

# max values or the farthest values
cosine_dist_red_output[:,1] = np.amax(cosine_dist_red_matrix,axis=1)

# as the distances are 0s along the diagonal of the matrix
# after capturing the max values and before finding  the min values
# we are assigning inf to the diagonal values
for i in range (0, len(cosine_dist_red_matrix[0,:])):
    for j in range (0, len(cosine_dist_red_matrix[0,:])):
        if i==j:
            cosine_dist_red_matrix[i,j] = np.inf
#print(tabulate(cosine_dist_red_matrix, tablefmt='fancy_grid'))

# min values or the nearest values
cosine_dist_red_output[:,0] = np.amin(cosine_dist_red_matrix,axis=1)
print(tabulate(cosine_dist_red_output,headers=["nearest", "farthest"], tablefmt='fancy_grid'))


print('cosine distance for WHITE WINE')

cosine_dist_white_matrix = distance.cdist(wine_data_white, wine_data_white, metric='cosine')
# print(tabulate(cosine_dist_white_matrix, tablefmt='fancy_grid'))

cosine_dist_white_output = np.zeros([10,2])

# max values or the farthest values
cosine_dist_white_output[:,1] = np.amax(cosine_dist_white_matrix,axis=1)

# as the distances are 0s along the diagonal of the matrix
# after capturing the max values and before finding  the min values
# we are assigning inf to the diagonal values
for i in range (0, len(cosine_dist_white_matrix[0,:])):
    for j in range (0, len(cosine_dist_white_matrix[0,:])):
        if i==j:
            cosine_dist_white_matrix[i,j] = np.inf
#print(tabulate(cosine_dist_white_matrix, tablefmt='fancy_grid'))

# min values or the nearest values
cosine_dist_white_output[:,0] = np.amin(cosine_dist_white_matrix,axis=1)
print(tabulate(cosine_dist_white_output,headers=["nearest", "farthest"], tablefmt='fancy_grid'))

print('TASK 2 - END')
