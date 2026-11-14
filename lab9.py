from math import sqrt
def median(a,b,c):
    m1 = 0.5*sqrt(2*b**2+2*c**2-a**2)
    m2 = 0.5*sqrt(2*a**2+2*c**2-b**2)
    m3 = 0.5*sqrt(2*a**2+2*b**2-c**2)
    return print(f'Медіана 1={round(m1)}, медіана 2={round(m2)}, медіана 3={round(m3)}')
a = int(input('Введіть сторону a '))
b = int(input('Введіть сторону b '))
c = int(input('Введіть сторону c '))
median(a,b,c)