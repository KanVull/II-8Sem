import tkinter as tk

def compute():
    features = []
    for checkbox in checkboxes:
        features.append(int(checkbox['var'].get()))
    y_man = features[0] * -0.5 + features[1] * -0.5 + 0.75
    y_ork = features[0] * -0.5 + features[1] * 0.5 + 0.25
    y_elf = features[0] * 0.5 + features[1] * 0.5 - 0.25
    y_troll = features[0] * 0.5 + features[1] * -0.5 + 0.25
    index, _ = max(enumerate([y_man, y_ork, y_elf, y_troll]), key=lambda item: item[-1])
    label['text'] = classes[index]

with open('dataset.csv', 'r') as dataset:
    lines = tuple([tuple(line.replace('\n', '').split(';')) for line in dataset])
    names = lines[0]
    input_data = lines[1:]

print(names)
print(input_data)   

features, classes = names[:2], names[2:]
input_data = tuple([{'features': data[:2], 'class':data[2:]} for data in input_data])

window = tk.Tk()
checkboxes = []
for feature in features:
    var = tk.BooleanVar()
    var.set(-1)
    checkbox = tk.Checkbutton(window, text=feature,
                              variable=var,
                              onvalue=1, offvalue=0,
                              command=compute)
    checkboxes.append({'var': var, 'button': checkbox})

for checkbox in checkboxes:
    checkbox['button'].pack()

label = tk.Label(window, text='')
label.pack()    

window.mainloop()    
