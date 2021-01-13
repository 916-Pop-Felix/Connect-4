from Board import Board
from GUI import GUI
from Service import BoardService
from UI import UI

if __name__ == '__main__':
    print(UI.print_menu_options())
    lines,columns=UI.lines_columns_values()
    ui_option=int(input("Do you want the UI or GUI version?\n"
                        "1 - UI\n"
                        "2 - GUI\n"))

    board=Board(lines,columns)
    service=BoardService(board)
    if ui_option == 1:
        ui=UI(service)
        ui.run_app()
    else:
        gui=GUI(service,lines,columns)
        gui.run_app()
