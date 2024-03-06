import flet as ft
from flet import colors
from automacao.automacao1 import *
from time import sleep

botoes = [
    {'operador': 'Automaçao para pesquisa varias vez no navergador', 'corfonte': colors.BLACK,
     'fondo': colors.BLUE_GREY_100},
    {'operador': 'Não de finido', 'corfonte': colors.WHITE, 'fondo': colors.ORANGE},
    {'operador': 'Não de finido', 'corfonte': colors.BLACK, 'fondo': colors.ORANGE},

]


def main(page: ft.Page):
    page.title = 'Automação'

    def automacaoPrimeira(e):
        page.clean()
        t = ft.Container(
            content=ft.Text(f'Vai comesar a automatisaçao em 4 segundo \nNão mecha no conputado'
                            '\nMas se vocé precisar para é so arasta o mause para o topo da tela do lado esquerdo',
                            color=colors.RED, size=20),
            alignment=ft.alignment.center,
        )
        page.add(t)
        sleep(4)
        automacao1()
        page.update()

    testo = ft.Container(
        ft.Text('Automaçães', size=30),
        alignment=ft.alignment.center
    )
    btn = [ft.Container(
        content=ft.Text(value=btn['operador'], color=btn['corfonte'], size=20),  # dando o nome e a cor ao butao
        height=50,
        bgcolor=btn['fondo'],  # cor de fundo do butao
        border_radius=100,  # para redondar o butao
        alignment=ft.alignment.center,  # para alinhar a sigula AC no meio do butao
        on_click=automacaoPrimeira
    ) for btn in botoes]
    keyboard = ft.Row(
        wrap=True,  # quebra um linha
        controls=btn,
        
    )
    page.add(
        testo,
        ft.Container(
            keyboard,
            alignment=ft.alignment.center

        )

    )


ft.app(target=main)