import tkinter as tk
from audioFileReader import file_reader

window = tk.Tk()
window.title("audio converter")
window.geometry("400x200")
label = tk.Label(window, text="please put a path to a wav file here, and name of file (use '/')", width=400, height=5)
label.pack()

def print_audio():
    # try:
    input = inputtxt.get(1.0, "end-1c")

    newName =  newNametxt.get(1.0, "end-1c")
    output = file_reader.convert_to_text(input)
    file_reader.save_file(newName, output)

    # except:
    #     checkLabel.config(text="something went wrong, check if everything is in right format")

frame2 = tk.LabelFrame(window)
#path input
inputtxtLabel = tk.Label(frame2, text = "file")
inputtxtLabel.grid(column = 0, row = 0)

inputtxt = tk.Text(frame2, height = 1, width = 50)
inputtxt.grid(column = 1, row = 0)

#name input
newNametxtLabel = tk.Label(frame2, text = "name of new file")
newNametxtLabel.grid(column = 0, row = 1)
newNametxt = tk.Text(frame2, height = 1, width = 50)
newNametxt.grid(column = 1, row = 1)



frame2.pack()


#button creation
button = tk.Button(window, text = "Convert", command = print_audio)
button.pack()

#label creation
checkLabel = tk.Label(window, text = "")
checkLabel.pack()

window.mainloop()

