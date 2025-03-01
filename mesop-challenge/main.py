import mesop as me


@me.stateclass
class State:
    clicks: int


def click_handler(event: me.ClickEvent):
    state = me.state(State)
    state.clicks += 1


@me.page(path="/counter")
def counter_page():
    state = me.state(State)
    me.text(f"Clicks: {state.clicks}")
    me.button("Click Me!", on_click=click_handler)
