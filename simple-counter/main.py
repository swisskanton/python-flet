import flet as ft
from flet import TextField
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None:
    page.title = 'Incremet conter'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    text_number: TextField = TextField(value='0', text_align=ft.TextAlign.RIGHT, width=100)

    def increment(e: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) + 1)
        page.update()

    def decrement(e: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) - 1)
        page.update()

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE, on_click=decrement),
                text_number,
                ft.IconButton(ft.icons.ADD, on_click=increment)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    ft.app(target=main)