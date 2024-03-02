import time

import flet as ft
from pdf2image import convert_from_path
import PyPDF2


def main(page: ft.Page):
    page.title = "PDF kezelő"
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.scroll = ft.ScrollMode.AUTO
    progress_ring = ft.ProgressRing()
    page.theme_mode = "light"

    def change_theme(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        toggle_darklight.selected = not toggle_darklight.selected
        page.update()

    toggle_darklight = ft.IconButton(
        on_click=change_theme,
        icon="dark_mode",
        selected_icon="light_mode",
        style=ft.ButtonStyle(
            # change color if light and dark
            color="white" if page.theme_mode == "dark" else "bkack"
            # {"": ft.colors.WHITE, "selected": ft.colors.BLACK}
        )
    )
    page.add(ft.Container(toggle_darklight, alignment=ft.alignment.center_right))

    def remove_progress_ring(file_selector):
        file_selector.controls.remove(progress_ring)
        file_selector.update()

    def teachers_pdf_to_images(path, file_name):
        new_path = path[:path.index(file_name)]
        try:
            pdf_file_obj = open(path, 'rb')
            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

            images = convert_from_path(path)
            for i, img in enumerate(images):
                page_obj = pdf_reader.pages[i]
                text = page_obj.extract_text()
                name = text[text.index('Tanár') + 6:].replace(' ', '_')
                # img.save(new_path + f'orarend{i}_{name}.png', 'PNG')
                # print(file_selector.controls, ft.ProgressRing(), progress_ring in file_selector.controls)
                if progress_ring in teachers_file_selector.controls:
                    remove_progress_ring(teachers_file_selector)
                teachers_created.controls.append(ft.Text(f'{i+1}. orarend{i+1}_{name}.png'))
                page.update()
        except FileNotFoundError:
            print("NO pdf found")
            teachers_created.controls.append(ft.Text("NO pdf found"))
            teachers_created.update()
            remove_progress_ring(teachers_file_selector)
        except FileExistsError:
            print('File already exists.')
            teachers_created.controls.append(ft.Text('File already exists.'))
            teachers_created.update()
            remove_progress_ring(teachers_file_selector)
        except:
            print('Something went wrong')
            teachers_created.controls.append(ft.Text('Something went wrong'))
            teachers_created.update()
            remove_progress_ring(teachers_file_selector)
        else:
            print("success")

    def pick_teachers_file_result(e: ft.FilePickerResultEvent):
        # print('\nfiles: ', e.files, '\nname: ', e.name, '\npath: ', e.path, '\ncontrol:', e.control, '\npage: ',
        #        e.page, '\ndata: ', e.data, '\ntarget: ', e.target)
        teachers_selected_files.value = (", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!")
        if teachers_selected_files.value != 'Cancelled!':
            teachers_selected_files.update()
            teachers_file_selector.controls.append(progress_ring)
            teachers_file_selector.update()
            teachers_created.controls = []
            teachers_created.update()
            # path = e.files[0].path
            # file_name = e.files[0].name
            # new_path = path[: path.index(file_name)]
            # print(new_path)
            teachers_pdf_to_images(e.files[0].path, e.files[0].name)

    def classes_pdf_to_images(path, file_name):
        # print(path, file_name)
        new_path = path[:path.index(file_name)]
        # print('path:', path, '\nfile name:', file_name, '\nnew path:', new_path)
        try:
            pdf_file_obj = open(path, 'rb')
            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

            images = convert_from_path(path)
            print('Creating images has been done.')
            for i, img in enumerate(images):
                page_obj = pdf_reader.pages[i]
                text = page_obj.extract_text()
                name = text.split()[-1] if text.split()[-1] not in ['váll', 'psz', 'szoft'] else text.split()[-2]
                name = name.replace(' ', '_').replace('/', '_').replace('\\', '-')
                # img.save(new_path + f'orarend{i}_{name}.png', 'PNG')

                if progress_ring in classes_file_selector.controls:
                    remove_progress_ring(classes_file_selector)
                print(f'{i+1}. orarend{i+1}_{name}.png')
                print(new_path + f'orarend{i}_{name}.png')
                classes_created.controls.append(ft.Text(f'{i+1}. orarend{i+1}_{name}.png', size=15))
                page.update()
        except FileNotFoundError:
            print("NO pdf found")
            classes_created.controls.append(ft.Text("NO pdf found"))
            classes_created.update()
            remove_progress_ring(classes_file_selector)
        except FileExistsError:
            print('File already exists.')
            classes_created.controls.append(ft.Text('File already exists.'))
            classes_created.update()
            remove_progress_ring(classes_file_selector)
        except:
            print('Something went wrong')
            classes_created.controls.append(ft.Text('Something went wrong'))
            classes_created.update()
            remove_progress_ring(classes_file_selector)
        else:
            print("success")

    def pick_classes_file_result(e: ft.FilePickerResultEvent):
        # print(e.__dir__())
        # print('files:', e.files, '\npath:', e.files[0].path, '\nfile name:', e.files[0].name)
        classes_selected_files.value = (", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!")
        if classes_selected_files.value != 'Cancelled!':
            classes_selected_files.update()
            classes_file_selector.controls.append(progress_ring)
            classes_file_selector.update()
            classes_created.controls = []
            classes_created.update()
            classes_pdf_to_images(e.files[0].path, e.files[0].name)

    pick_teachers_file_dialog = ft.FilePicker(on_result=pick_teachers_file_result)
    teachers_selected_files = ft.Text()

    pick_classes_file_dialog = ft.FilePicker(on_result=pick_classes_file_result)
    classes_selected_files = ft.Text()

    page.overlay.append(pick_teachers_file_dialog)
    page.overlay.append(pick_classes_file_dialog)

    teachers_file_selector = ft.Row(
            [
                ft.ElevatedButton(
                    "Tanár órarend választó",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_teachers_file_dialog.pick_files(
                        dialog_title='PDF fájlválasztó',
                        allow_multiple=False,
                        allowed_extensions=['pdf'],
                    ),
                ),
                teachers_selected_files,
            ]
    )

    classes_file_selector = ft.Row(
            [
                ft.ElevatedButton(
                    "Osztály órarend választó",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_classes_file_dialog.pick_files(
                        dialog_title='PDF fájlválasztó',
                        allow_multiple=False,
                        allowed_extensions=['pdf'],
                    ),
                ),
                classes_selected_files,
            ]
    )

    teachers_created = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.START,
            width=500,
            height=500,
            scroll=ft.ScrollMode.AUTO,
    )

    teachers_content = ft.Container(
        content=teachers_created,
        bgcolor='#008080',
        height=500,
        padding=ft.padding.only(left=30, top=10, bottom=10),
        border_radius=30
    )

    classes_created = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.START,
            width=500,
            height=500,
            scroll=ft.ScrollMode.AUTO,
    )

    classes_content = ft.Container(
        content=classes_created,
        bgcolor='#008080',
        height=500,
        padding=ft.padding.only(left=30, top=10, bottom=10),
        border_radius=30
    )

    teachers_column = ft.Column([teachers_file_selector, teachers_content], expand=1)
    classes_column = ft.Column([classes_file_selector, classes_content], expand=1)

    page.add(ft.Row([
            teachers_column,
            classes_column
            ],
        )
    )


if __name__ == '__main__':
    ft.app(target=main)
