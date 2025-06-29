from nicegui import ui
from nicegui.events import ValueChangeEventArguments

b = True

def show(event: ValueChangeEventArguments):
    global b
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')
    b = not b
    

ui.button('Button', on_click=lambda: ui.notify('Click'))
with ui.row():
    ui.checkbox('Checkbox', on_change=show)
    ui.switch('Switch', on_change=show)
ui.radio(['A', 'B', 'C'], value='A', on_change=show).props('inline')
with ui.row():
    ui.input('Text input', on_change=show)
    if b:
        ui.select(['One', 'Two'], value='One', on_change=show)

ui.link('And many more...', '/reference').classes('mt-8')

ui.run()
