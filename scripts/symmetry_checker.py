#!/usr/bin/env python3
import mpmath as mp
import pandas as pd
import os
import sys
from datetime import datetime

# Add parent directory to path if script is run from scripts folder
if os.path.basename(os.getcwd()) == 'scripts':
    sys.path.append('..')

# Function to compute Fibonacci numbers
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Build the rho ratios for the 8-vertex chain
rhos = [fib(9 - e) / fib(10 - e) for e in range(1, 8)]

# Function to compute the 15j product formula
def f15j(j):
    res = mp.mpf(1)
    for idx, j_e in enumerate(j):
        twoj = 2 * j_e
        rho = rhos[idx]
        term = mp.hyper([-twoj, 0.5], [1], -rho) / mp.factorial(twoj)
        res *= term
    return res

def main():
    # Create data directory if it doesn't exist
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    # Test cases: lists of integer j_e
    test_cases = [
        [0, 1, 2, 3, 4, 5, 6],
        [1, 1, 1, 1, 1, 1, 1],
        [2, 3, 1, 4, 2, 1, 3],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 2, 3, 4, 3, 2, 1]
    ]

    # Compute original and reflected values
    data = []
    print("\n==== 3nj Symbol Reflection Symmetry Analysis ====")
    print("\nComputing reflection symmetry for test cases:")
    
    for j in test_cases:
        original = f15j(j)
        reflected = f15j(j[::-1])
        diff = abs(original - reflected)
        data.append({
            'j': str(j),
            'f(j)': float(original),
            'f(rev j)': float(reflected),
            '|diff|': float(diff)
        })
        print(f"j = {j}")
        print(f"  f(j)     = {original}")
        print(f"  f(rev j) = {reflected}")
        print(f"  |diff|   = {diff}\n")

    # Create DataFrame and save to CSV
    df = pd.DataFrame(data)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(data_dir, f'reflection_symmetry_{timestamp}.csv')
    df.to_csv(filename, index=False)
    print(f"Results saved to: {filename}")
    
    # Display summary
    symmetric = all(row['|diff|'] < 1e-10 for row in data)
    print(f"\nReflection symmetry holds: {symmetric}")
    print("====================================================")
    
    return df

if __name__ == "__main__":
    main()
