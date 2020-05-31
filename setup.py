import cx_Freeze
executables=[cx_Freeze.Executable('tttgui.py')]
cx_Freeze.setup(name='TicTacToe',options={"build_exe":{'packages':['pygame'],'include_files':['icon.png','Jazz_In_Paris.mp3']}},description='A TicTacToe Game',executables=executables)