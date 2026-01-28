import math

def hitung_manning(n, s, b, h):
    """
    Menghitung Kecepatan (V) dan Debit (Q) saluran persegi.
    """
    try:
        A = b * h           # Luas basah
        P = b + (2 * h)     # Keliling basah
        R = A / P           # Jari-jari hidrolis
        
        # Rumus Manning
        V = (1/n) * (R**(2/3)) * (s**0.5)
        Q = V * A
        
        return V, Q
    except ZeroDivisionError:
        return 0, 0