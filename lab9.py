from math import sqrt
# def median(a,b,c):
#     m1 = 0.5*sqrt(2*b**2+2*c**2-a**2)
#     m2 = 0.5*sqrt(2*a**2+2*c**2-b**2)
#     m3 = 0.5*sqrt(2*a**2+2*b**2-c**2)
#     return print(f'Медіана 1= {round(m1)}, медіана 2= {round(m2)}, медіана 3= {round(m3)}')
# a = int(input('Введіть сторону a '))
# b = int(input('Введіть сторону b '))
# c = int(input('Введіть сторону c '))
# median(a,b,c)
def calculate_medians(side_a,side_b,side_c):
    median_1 = 0.5*sqrt(2*side_b**2+2*side_c**2-side_a**2)
    median_2 = 0.5*sqrt(2*side_a**2+2*side_c**2-side_b**2)
    median_3 = 0.5*sqrt(2*side_a**2+2*side_b**2-side_c**2)
    return [median_1,median_2,median_3]
side_a = int(input('Введіть сторону a '))
side_b = int(input('Введіть сторону b '))
side_c = int(input('Введіть сторону c '))
medians=calculate_medians(side_a,side_b,side_c)
print(f'Медіана сторони a = {round(medians[0])}, медіана до сторони b = {round(medians[1])}, медіана до сторони c = {round(medians[2])}')