def find_sum_of_two(A, val):
 #TODO: Write - Your - Code
  A.sort()
  n = len(A)
  print(A)
  i =0
  j = n - 1
  while(i != j):
      print('comp : ',i,':',j)
      if(val < (A[i] + A[j])):
          j = j - 1
      elif(val > (A[i] + A[j])):
          i = i + 1
      else:
          return True;
  return False

def find_sum_of_two_set(A, val):
    found_nos = set()
    for itm in A:
        if (val - itm) in found_nos :
            return True
        found_nos.add(itm)
    return False

# driver code
A = [1, 4, 45, 6, 10, 8]
n = 16
print(find_sum_of_two(A,n))
print(find_sum_of_two_set(A,n))
