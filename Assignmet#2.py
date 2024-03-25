
def merge_sort(arr):
    def play_sound_effect():
        print('\a', end='', flush=True)

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            play_sound_effect()  

        result.extend(left[i:])
        result.extend(right[j:])
        print("Merging elements:", left, "and", right, ">>", result)  
        return result

    def merge_sort_rec(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_rec(arr[:mid])
        right = merge_sort_rec(arr[mid:])
        return merge(left, right)

    return merge_sort_rec(arr)

#checking the code with the following array

product_ids = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
sorted_ids = merge_sort(product_ids)
