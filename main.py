import plotly
import plotly.graph_objs as go

file = open("E:/pocemon_dataset(kollok 2)/data/pokemon.csv")
data = file.read()
root_data = data.split("\n")
file.close()

# Функція, що створює датасет

def create_dataset(root_data):
    dataset = dict()
    keys = root_data[0].split(",")
    for i in range(1, len(root_data)):
        values = root_data[i].split(",")
        dataset[values[1]] = dict()
        for j in keys:
                dataset[values[1]][j] = values[keys.index(j)]
    return dataset
dataset = create_dataset(root_data)
print(dataset)

# Фунція, що повертає множину всіх представлених в датасеті типів покемонів

def get_types_1(dataset):
    types_1_list = set()
    for name in list(dataset.keys()):
        types_1_list.add(dataset[name]['Type 1'])
    return types_1_list

# Функція, яка знаходить кількість покемонів первного типу

def num_of_type(dataset, type):
    num=0
    for name in list(dataset.keys()):
        if dataset[name]['Type 1'] == type:
            num+=1
    return num

print("Num of Bug is", num_of_type(dataset, "Bug"))

# Функція, яка повертає найсильніший тип покемонів

def the_most_powerfull_pokemon(dataset):
    types = list(get_types_1(dataset))
    powers = dict()

    for type in types:
        pow_sum = 0
        num = num_of_type(dataset, type)
        for name in list(dataset.keys()):
            if dataset[name]["Type 1"] == type:
                pow_sum = pow_sum + int(dataset[name]["Attack"])
        average_pow = pow_sum / num
        powers[type] = average_pow
    print(powers)
    Max = max(list(powers.values()))
    return list(powers.keys())[(list(powers.values())).index(Max)]

print(the_most_powerfull_pokemon(dataset))


#Вивести кругову діаграму: скільки покемонів якого типу

data = dict()
for type in list(get_types_1(dataset)):
    data[type] = num_of_type(dataset, type)

diagram = go.Pie(labels=list(data.keys()), values=list( data.values()))
plotly.offline.plot([diagram], filename='types.html')

#Вивести стовпчикову діаграму: в якого типу покемонів яке середнє значення атаки

types = list(get_types_1(dataset))
powers = dict()
for type in types:
    pow_sum = 0
    num = num_of_type(dataset, type)
    for name in list(dataset.keys()):
        if dataset[name]["Type 1"] == type:
            pow_sum = pow_sum + int(dataset[name]["Attack"])
    average_pow = pow_sum / num
    powers[type] = average_pow

diagram = go.Bar(
    x=list(powers.keys()),
    y=list(powers.values())
)

fig = go.Figure(data=[diagram])
plotly.offline.plot(fig, filename='pokemon powers.html')