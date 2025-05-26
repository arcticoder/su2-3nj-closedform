#!/usr/bin/env python3
"""
Coefficient Calculator for SU(2) 3nj Symbols

This script calculates and analyzes SU(2) 3nj recoupling coefficients using the
closed-form hypergeometric product formula.
"""

import mpmath as mp
import pandas as pd
import numpy as np
import os
import sys
from datetime import datetime

# Add parent directory to path if script is run from scripts folder
if os.path.basename(os.getcwd()) == 'scripts':
    sys.path.append('..')

# Function to compute Fibonacci numbers
def fib(n):
    """Calculate the nth Fibonacci number"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Build the rho ratios for the 8-vertex chain
def build_rhos(edge_count=7):
    """Build rho ratios for a chain with the given number of edges"""
    return [fib(9 - e) / fib(10 - e) for e in range(1, edge_count + 1)]

# Function to compute the 3nj product formula
def calculate_3nj(j, rhos=None):
    """
    Calculate the value of a 3nj symbol using the hypergeometric product formula
    
    Parameters:
    j (list): List of angular momentum values (j_e) for each edge
    rhos (list, optional): List of rho ratios. If None, uses 8-vertex chain ratios.
    
    Returns:
    mpmath.mpf: The calculated 3nj symbol value
    """
    if rhos is None:
        rhos = build_rhos(len(j))
        
    if len(j) != len(rhos):
        raise ValueError(f"Length of j ({len(j)}) must match length of rhos ({len(rhos)})")
    
    res = mp.mpf(1)
    for idx, j_e in enumerate(j):
        twoj = 2 * j_e
        rho = rhos[idx]
        term = mp.hyper([-twoj, 0.5], [1], -rho) / mp.factorial(twoj)
        res *= term
    return res

def generate_test_cases(edge_count=7):
    """Generate a set of test cases for 3nj symbol analysis"""
    return [
        [0, 1, 2, 3, 4, 5, 6][:edge_count],
        [1] * edge_count,
        [2, 3, 1, 4, 2, 1, 3][:edge_count],
        [0] * edge_count,
        [1, 2, 3, 4, 3, 2, 1][:edge_count]
    ]

def analyze_symmetry(test_cases=None, edge_count=7):
    """
    Analyze the reflection symmetry properties of the 3nj symbols
    
    Parameters:
    test_cases (list, optional): List of test cases to analyze
    edge_count (int): Number of edges in the graph
    
    Returns:
    pandas.DataFrame: DataFrame containing analysis results
    """
    if test_cases is None:
        test_cases = generate_test_cases(edge_count)
    
    rhos = build_rhos(edge_count)
    
    # Compute original and reflected values
    data = []
    print("\n==== 3nj Symbol Reflection Symmetry Analysis ====")
    print("\nComputing reflection symmetry for test cases:")
    
    for j in test_cases:
        original = calculate_3nj(j, rhos)
        reflected = calculate_3nj(j[::-1], rhos)
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
    
    # Create DataFrame
    return pd.DataFrame(data)

def main():
    """Main function to run the 3nj coefficient analysis"""
    # Create data directory if it doesn't exist
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    # Generate and analyze test cases
    df = analyze_symmetry()
    
    # Save results to CSV
    filename = os.path.join(data_dir, '3nj_analysis.csv')
    df.to_csv(filename, index=False)
    print(f"Results saved to: {filename}")
    
    # Display summary
    symmetric = all(row['|diff|'] < 1e-10 for _, row in df.iterrows())
    print(f"\nReflection symmetry holds: {symmetric}")
    print("====================================================")
    
    return df

if __name__ == "__main__":
    main()
