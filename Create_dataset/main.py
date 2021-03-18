import random

ii_max = 20
isis_max = 24
pis_max = 20
iis_max = 20
max_score = sum([ii_max, isis_max, pis_max, iis_max])

with open('../dataset_StudentsOtchislenie.csv', 'w') as dataset:
    dataset.write('ii;isis;pis;iis;otchislenie\n')
    for _ in range(10000):
        ii = random.randint(0, ii_max)
        isis = random.randrange(0, isis_max)
        pis = random.randrange(0, pis_max)
        iis = random.randrange(0, iis_max)
        total_score = sum([ii, isis, pis, iis])
        otchislenie = True if total_score <= max_score / 2 else False
        string = f'{ii};{isis};{pis};{iis};{int(otchislenie)}\n'
        dataset.write(string)
    

