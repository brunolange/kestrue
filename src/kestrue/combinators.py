"""combinators.py

A collection of Lambda Calculus combinators
"""

# Identity
I = lambda a: a

# Kestrel/True
K = lambda a: lambda b: a

# Kite/False
KI = lambda a: lambda b: b

# Cardinal/Flip
CA = lambda f: lambda a: lambda b: f(b)(a)
