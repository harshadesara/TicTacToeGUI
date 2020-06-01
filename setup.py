import cx_Freeze
executables=[cx_Freeze.Executable('tttgui.py')]
cx_Freeze.setup(name='TicTacToe',options={"build_exe":{'packages':['pygame'],'include_files':['icon.png','Jazz_In_Paris.mp3']}},description='A TicTacToe Game',executables=executables)
#Run in CMD the following code (Also first you have to go that particular folder)
#python setup.py build (Converting into executable)
#python setup.py bdist_msi (It will create the installer)