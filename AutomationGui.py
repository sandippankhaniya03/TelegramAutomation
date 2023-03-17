import PySimpleGUI as sg

# Define the layout
layout = [
    [sg.Button('Button 1')],
    [sg.Button('Button 2')],
    [sg.Button('Button 3')],
]

# Create the window
window = sg.Window('My Window', layout)

# Event loop to process events and get input
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Button 1':
        print('Button 1 clicked')
    elif event == 'Button 2':
        print('Button 2 clicked')
    elif event == 'Button 3':
        print('Button 3 clicked')

# Close the window
window.close()
