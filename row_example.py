import flet as ft


def main(page: ft.Page):

    page.title = 'Row beállítások'
    page.scroll = ft.ScrollMode.AUTO

    # konténetek hozzáadása az items listához
    def add_items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.Text(value=str(i)),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=ft.colors.AMBER,
                    border_radius=ft.border_radius.all(5),
                )
            )
        return items

    # ------------------------- térköz beállítása -----------------------
    # csúzda módosítása
    def gap_slider_change(e):
        térköz_sorelemek.spacing = int(e.control.value)
        térköz_sorelemek.update()

    # csúzda
    gap_slider = ft.Slider(
        min=0,
        max=50,
        divisions=50,
        value=0,
        label="{value}",
        on_change=gap_slider_change,
    )

    térköz_sorelemek = ft.Row(spacing=0, controls=add_items(10))

    térközkonténer = ft.Container(

        padding=ft.padding.only(bottom=10),
        content=térköz_sorelemek
    )

    térköz_csúzda = ft.Container(
        bgcolor=ft.colors.BLUE_100,
        content=ft.Column(
            [
                ft.Text("Térközök beállítása az elemek között"),
                gap_slider,
                térközkonténer
            ]
        )
    )

    page.add(térköz_csúzda)

    # ------------------------- elemek wrappolása - sortörése -----------------------
    # wrap csúzda módosítása
    def slider_change(e):
        wrap_elemek.width = float(e.control.value)
        wrap_elemek.update()

    # wrap csúzda beállítása
    width_slider = ft.Slider(
        min=350,
        max=page.window_width,
        divisions=20,
        value=page.window_width,
        label="{value}",
        on_change=slider_change,
    )

    # 30 elem a wrappoláshoz
    wrap_elemek = ft.Row(
        wrap=True,
        spacing=10,
        run_spacing=10,
        controls=add_items(30),
        width=page.window_width,
    )

    wrap_konténer = ft.Container(
        bgcolor="lightgreen",
        height=400,
        content=ft.Column(
            [
                ft.Text("Változtasd meg a sorszélességet, hogy lásd, hogyan rendeződnek több sorba az elemek."),
                width_slider,
                wrap_elemek
            ]
        )
    )

    page.add(wrap_konténer)

    # ------------------------- sor elrendezése horizopntálisan (vízszintesen) -----------------------
    # sorok generálása
    def row_with_alignment(align: ft.MainAxisAlignment):
        return ft.Column(
            [
                ft.Text(str(align), size=16),
                ft.Container(
                    content=ft.Row(add_items(3), alignment=align),
                    bgcolor=ft.colors.AMBER_100,
                ),
            ]
        )

    # sorok elrendezésének beállítása
    sor_elrendezések = ft.Column([
        row_with_alignment(ft.MainAxisAlignment.START),
        row_with_alignment(ft.MainAxisAlignment.CENTER),
        row_with_alignment(ft.MainAxisAlignment.END),
        row_with_alignment(ft.MainAxisAlignment.SPACE_BETWEEN),
        row_with_alignment(ft.MainAxisAlignment.SPACE_AROUND),
        row_with_alignment(ft.MainAxisAlignment.SPACE_EVENLY),
    ])

    sor_elrendezés_konténer = ft.Container(
        bgcolor='lightblue',
        padding=10,
        content=sor_elrendezések
    )

    page.add(sor_elrendezés_konténer)

    # ------------------------- sor elrendezése vertikálisan (függőlegesen) -----------------------
    # sorok generálása függőleges elrendezéshez
    def row_with_vertical_alignment(align: ft.CrossAxisAlignment):
        return ft.Column(
            [
                ft.Text(str(align), size=16),
                ft.Container(
                    content=ft.Row(add_items(3), vertical_alignment=align),
                    bgcolor=ft.colors.AMBER_100,
                    height=150,
                ),
            ]
        )

    page.add(
        row_with_vertical_alignment(ft.CrossAxisAlignment.START),
        row_with_vertical_alignment(ft.CrossAxisAlignment.CENTER),
        row_with_vertical_alignment(ft.CrossAxisAlignment.END),
    )

    # ------------------------- expand -----------------------
    r1 = ft.Row([
        ft.TextField(hint_text="Enter your name", expand=True),
        ft.ElevatedButton(text="Join chat")
    ])

    r2 = ft.Row([
        ft.Container(expand=1, content=ft.Text("A", size=16), bgcolor='red', height=100, alignment=ft.alignment.center),
        ft.Container(expand=3, content=ft.Text("B", size=16), bgcolor='green'),
        ft.Container(expand=1, content=ft.Text("C", size=16), bgcolor='blue')
    ])

    page.add(r1, r2)



if __name__ == '__main__':
    ft.app(target=main)
