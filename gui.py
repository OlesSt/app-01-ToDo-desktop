import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to do")
input_box = sg.InputText(tooltip="Entr todo")
add_button = sg.Button("Add")

window = sg.Window("My ToDo App", layout=[[label], [input_box, add_button]])
window.read()
window.close()