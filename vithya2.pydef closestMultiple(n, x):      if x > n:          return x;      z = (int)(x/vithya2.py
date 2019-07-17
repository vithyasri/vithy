def closestMultiple(n, x): 
    if x > n: 
        return x; 
    z = (int)(x / 2); 
    n = n + z; 
    n = n - (n % x); 
    return n;
