tabu = [1,2,3,4]

for i in range(len(tabu)-1):
    if tabu[i] == 3:
        del tabu[i]

print(tabu)