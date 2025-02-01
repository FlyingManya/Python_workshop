import numpy as np 

# # create array using np
# arr = np.array([25, 31, 22, 9, 17])
# print(arr)
# print(arr[0]) # access elements using index 

# # arrays with 0s and 1s
# zer_arr =np.zeros(5)
# print(zer_arr)
# one_arr =np.ones(5)
# print(one_arr)

# # array with a range 
# range_arr = np.arange(10)
# print(range_arr)

# slicing 
# arr = np.array([25, 31, 22, 9, 17])
# print(arr)
# sliced_arr = arr[1:4]
# print(sliced_arr)

# boradcasting 
# brd_arr = arr + 10 
# print(brd_arr)

# statistical operations 

# arr = np.array([25, 31, 22, 9, 17])
# print(arr)
# # mean 
# mean_arr = np.mean(arr)
# print(mean_arr)
# # median 
# med_arr = np.median(arr)
# print(med_arr)
# # standard deviation 
# st_dev = np.std(arr)
# print(st_dev)

# array manipulation 
# concatination 

# arr = np.array([25, 31, 22, 9, 17])
# # print(arr)
# arr2 = np.array([11, 20, 27, 7, 15])
# # print(arr2)
# con_arr =np.concatenate([arr, arr2])
# print(con_arr)

# # split 
# split_arr = np.split(con_arr, 2)
# print(split_arr)
# print(split_arr[0])


arr = np.array([25, 31, 22, 9, 17])
# print(arr)
# indexing 
print(arr[[1, 3]])
print(arr[arr > 20])