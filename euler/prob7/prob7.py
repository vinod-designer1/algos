def gen_primes():
  D = {}
  q = 2  # first integer to test for primality.

  while True:
    if q not in D:
      # not marked composite, must be prime  
      yield q 

      #first multiple of q not already marked
      D[q * q] = [q] 
    else:
      for p in D[q]:
        D.setdefault(p + q, []).append(p)
      # no longer need D[q], free memory
      del D[q]

    q += 1
    
k = 0
for i in gen_primes():
    k += 1
    if  k == 10001:
        print(i)
        break
