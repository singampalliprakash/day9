#swap without using third variable
a=2
b=3
c=4
print(f"before swapping:a={a},b={b},c={c}")
a,b,c=c,a,b
print(f"after swapping:a={a},b={b},c={c}")