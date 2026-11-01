import time #to compare time to run (should be around ~O(n^2) worst case)

l1 = [152,54,-20,5,20,2,1,9,7,10,500,252,-20,-605] #any random, unordered/unsorted list of integers

print("original list:")
print(l1)
print()

# in-place swap
def swap(l, a, b):
    #temp = l[a]
    #l[b] = temp
    
    #new: in-place swap is better and more pythonic.
    l[a], l[b] = l[b], l[a]
    print(l1)

sortErrors = 1
notSorted = False

iterations = 0

def scanList(l):
    length = len(l)
    correct = 0
    for idx, element in enumerate(l):
        left = 0
        right = 0
        if idx - 1 >= 0 and l[idx - 1]: #left pointer
            left = idx - 1
        else:
            left = None
        if idx + 1 < len(l) and l[idx + 1]: #right pointer
            right = idx + 1
        else:
            right = None
        if right and left:
            if l[right] < l[idx]:
                notSorted = True
            elif l[left] > l[idx]:
                notSorted = True
            else:
                correct += 1
        elif right:
            if l[right] < l[idx]:
                notSorted = True
            else:
                correct += 1
        elif left:
            if l[left] > l[idx]:
                notSorted = True
            else:
                correct +=1
    print(f"Correct entries: {correct}")
    if correct == length:
        return True
    else:
        return False

def sort(l):
    left = 0
    right = 0
    for idx, ele in enumerate(l):
        if idx - 1 >= 0 and l[idx - 1]: #left pointer
            left = idx - 1
        else:
            left = None
        if idx + 1 < len(l) and l[idx + 1]: #right pointer
            right = idx + 1
        else:
            right = None
            
        print(f"index {idx} right is {right != None} left is {left != None}")
        while ((right and l[right] < l[idx]) or (left and l[left] > l[idx])) and sortErrors > 0:
            if right and left:
                if l[idx] > l[right]:
                    print(f"{l[idx]} is greater than {l[right]}")
                    print(f"pre-swapped {l}")
                    swap(l, idx, right)
                    print(f"right-swapped {l}")
                if l[idx] < l[left]:
                    print(f"{l[idx]} is less than {l[left]}")
                    print(f"pre-swapped {l}")
                    swap(l, idx, left)
                    print(f"left-swapped {l}")
            elif left:
                if l[idx] < l[left]:
                    print(f"{l[idx]} is less than {l[left]}")
                    print(f"pre-swapped {l}")
                    swap(l, idx, left)
                    print(f"left-swapped {l}")
            elif right:
                if l[idx] > l[right]:
                    print(f"{l[idx]} is greater than {l[right]}")
                    print(f"pre-swapped {l}")
                    swap(l, idx, right)
                    print(f"right-swapped {l}")
            else:
                print("invalid index")
                
        # after completion, re-scan list
        for idx, ele in enumerate(l):
            if idx - 1 >= 0 and l[idx - 1]: #left pointer
                left = idx - 1
            else:
                left = None
            if idx + 1 < len(l) and l[idx + 1]: #right pointer
                right = idx + 1
            else:
                right = None
        if not (right and l[right] < l[idx]) or (left and l[left] > l[idx]):
            print("SORTED!")
            notSorted = False
            
originalTime = time.perf_counter()

while scanList(l1) == False:
    sort(l1)
    iterations += 1

sortedTime = time.perf_counter()

elapsed = sortedTime - originalTime

print("final list:")

print(l1)

print(f"{iterations} full-pass iterations")

print(f"ELAPSED TIME: {elapsed}")

    
    
        