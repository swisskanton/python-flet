import flet as ft


def main(page: ft.Page):
    page.title = "Address form"

    def is_number(e):
        if not zip.value.isdigit() or len(zip.value) > 4:
            zip.color = 'red'
            page.update()
        else:
            zip.color = 'black'
            page.update()

    def on_submit(e):
        if street.value == '' or city.value == '' or zip.value == '':
            for control in [street, city, zip]:
                if control.value == '':
                    control.hint_text = "I'm empty"
        else:
            text.value = f'{zip.value} {city.value}\n{street.value} {street2.value}\n{country.value} {region.value}'
        page.update()

    left_side = ft.Container(content=ft.Text(value='Cím', weight=ft.FontWeight.W_600, size=25),
                             width=300, height=300, margin=20,
                             alignment=ft.alignment.top_left)

    street = ft.TextField(label='', helper_text="Utca, házszám", width=400, height=70, border_radius=10)
    street2 = ft.TextField(label='', helper_text="Utca, házszám 2. sor", width=400, height=70, border_radius=10)
    city = ft.TextField(label='', helper_text="Város", width=195, height=70, border_radius=10)
    region = ft.TextField(label='', helper_text="Megye", width=195, height=70, border_radius=10)
    zip = ft.TextField(label='', helper_text="Irányítószám", width=195, height=70, border_radius=10, on_change=is_number)
    country = ft.TextField(label='', helper_text="Ország", value="Hungary", width=195, height=70, border_radius=10)
    btn = ft.ElevatedButton(text='Submit', on_click=on_submit)
    text = ft.Text()

    right_side = ft.Column([street, street2, ft.Row([city, region]), ft.Row([zip, country]), btn, text])
    page.add(ft.Row([left_side, right_side]))


if __name__ == '__main__':
    ft.app(target=main)
