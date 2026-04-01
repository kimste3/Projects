import FreeSimpleGUI as gui

# Define the window's contents
start_layout = [  [gui.Text("URL: ")],
            [gui.Input(key="-url-")],
            [gui.Text("Select a file:")],
            [gui.Input(key="-file-"), gui.FileBrowse(initial_folder="C:\\")],
            [gui.Button('Continue', key="-continue-")]
]

processing_layout = [
    [gui.Text("Processing, please wait...")],
    [gui.ProgressBar(max_value=100, orientation='h', size=(20, 20), key='progress')],
    [gui.Cancel()]
]

# Create the window
window = gui.Window('Generate a QR Code', start_layout)

while True:
        event, values = window.read()

        if event == gui.WINDOW_CLOSED or event == 'Quit':
            break

        if (event == "-continue-" and values["-url-"] != ""and
        values["-file-"] != ""):
            print("forward")
            window.close()
            window = gui.Window("Processing ...", processing_layout)


window.close()
