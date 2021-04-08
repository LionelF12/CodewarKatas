def find_deleted_number(arr, mixed_arr):
    if arr == None: return 0 
    for start in arr:
        if start in mixed_arr:
            continue
        else:
            return start
    return 0