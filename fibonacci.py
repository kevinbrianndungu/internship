#!/usr/bin/env python3

# Write a program to generate the Fibonacci sequence up to 100.

def generate_fibonacci(limit):
    fib_sequence = [0, 1]

    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        
        if next_fib > limit:
            break
        
      
        fib_sequence.append(next_fib)
    
    return fib_sequence

fibonacci_sequence = generate_fibonacci(100)
print("Fibonacci sequence up to 100:", fibonacci_sequence)
