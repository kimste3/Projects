import FreeSimpleGUI as gui
import validators
from Supplemental.supplemental import check_filepath, replace_forward_slash, check_url


# Define the window's contents
start_layout = [
            [gui.Text("URL: "), gui.Input(key="-url-")],
            [gui.Text("Select a file:"), gui.FileBrowse(initial_folder="C:\\"), gui.Input(key="-file_location-")],
            [gui.Text("Enter a filename for the QR"),
            gui.InputText(key="-filename-")],
            [gui.Button('Continue', key="-continue-")],
]

processing_layout = [
    [gui.Text("Processing, please wait...")],
    [gui.ProgressBar(max_value=100, orientation='h', size=(20, 20), key='progress')],
    [gui.Cancel()]
]

# Create the window
window = gui.Window('Generate a QR Code', start_layout)
args_dict = {}

while True:
        event, values = window.read()

        if event == gui.WINDOW_CLOSED or event == 'Quit':
            break

        if (event == "-continue-" and values["-url-"] != ""and
        values["file_location"] != "" and values["-filename-"]):
            
            window.close()
            window = gui.Window("Processing ...", processing_layout)


window.close()
