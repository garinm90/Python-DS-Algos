# %%
class Fraction():
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __repr__(self) -> str:
        return f'{self.num}/{self.den}'

    def __str__(self) -> str:
        return f'{self.num}/{self.den}'

    def __add__(self, second_fraction) -> str:
        newnum = self.num*second_fraction.den + self.den*second_fraction.num
        newden = self.den * second_fraction.den
        common_denominator = self.gcd(newnum, newden)
        return Fraction(newnum//common_denominator, newden//common_denominator)

    def __eq__(self, o: object) -> bool:
        first_num = self.num * o.den
        second_num = self.den * o.num
        return first_num == second_num


    # Recursive implementation of Euclid's Algorithm.
    # The remainder of B divided by A is continually passed as the first parameter
    # When the first parameter is equal to 0. The A parameter (Parameter 2'B') is the GCD
    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)


# %%
f1 = Fraction(1, 3)
f2 = Fraction(1, 9)

print(f1 == f2)

# %%

# %%


# %%
