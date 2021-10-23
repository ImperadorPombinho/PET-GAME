import cx_Freeze

executables = [cx_Freeze.Executable('PETGAME.py')]

cx_Freeze.setup(
    name="jogo do gato que pula",
    options={'build_exe':{'packages':['pygame'],
                           'include_files':['assets', 'cenario', 'Gatos', 'obstaculo'] }},
    executables = executables
)