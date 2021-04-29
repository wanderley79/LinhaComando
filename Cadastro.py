  from PySimpleGUI import PySimpleGUI as sg


#layousg.theme('Reddit')
layout = [
    [sg.Test('Usuario'), sg.Input(key='usuario')],
    [ sg.Teste('Senha'), sg.Input(key='senha', password_char='*')]
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#janela
janela = sg.Window('Tela de Login', layout)
#ler os eventos
while True:
    eventos, = valores = janela.read()
    if eventos == sg.window_CLOSED:
          break
    if eventos =='Entrar':
        if valores ['usuario'] == ['wanderley'] and valores ['senh'] == ['123456']:
            print("Bem-vindo a sua aula")



