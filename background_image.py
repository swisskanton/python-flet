import flet as ft
from random import randint


def main(page: ft.Page):
    page.title = 'Háttérkép beállítása'
    page.padding = 0
    # -------------------------------------------------------------------
    # létrehozol egy tartalmat
    tartalom = ft.Column()

    # Az oldalnak beállítasz egy kontainert, aminek az elsőnek kell lennie
    # A containernek beállítasz egy háttérképet
    # beállítod a kitöltést
    # expandot True-ra állítod
    # a container tartalmának beállítod, amit az oldalra akarsz tenni
    page.add(ft.Container(
            image_src=f"https://picsum.photos/200/200?{randint(0,100)}",
            image_fit=ft.ImageFit.COVER,
            expand=True,
            content=tartalom
        )
    )
    # -------------------------------------------------------------------

    tartalom.scroll = ft.ScrollMode.AUTO

    # A tartalomhoz adod hozzá az új elemeket (controls-okat)
    # Csak egyesével lehet appendelni új elemet
    tartalom.controls.append(ft.Text('Border radius'))
    tartalom.controls.append(ft.Image(
            src='assets/images/mandelbrot_set.jpg',
            border_radius=ft.border_radius.only(top_left=75, bottom_right=100),
            height=200,
            width=200,
        )
    )
    tartalom.controls.append(ft.Divider())
    tartalom.controls.append(ft.Text('Második kép'))
    tartalom.controls.append(ft.Image(
            src=f"https://picsum.photos/200/200?{randint(0,100)}",
            height=200,
            width=200,
        ))

    tartalom.controls.append(ft.Divider())
    tartalom.controls.append(ft.Text('Képek listája'))
    images = ft.Row(scroll=ft.ScrollMode.ALWAYS)
    for i in range(10):
        images.controls.append(ft.Image(
            height=200,
            width=200,
            src=f"https://picsum.photos/200/200?{randint(0, 100)}",
        ))
    tartalom.controls.append(images)
    tartalom.controls.append(ft.Divider())

    page.update()


ft.app(target=main)
