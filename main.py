from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info

def do_booking():
  info("Booking", "Thank you for booking")
  print( film_choice.value)
  print( vip_seat.value)
  print( row_choice.value)

app = App(title="My second GUI app", width=300, height=200, layout="grid")

film_choice = Combo(app, options=["Parasite","1917","Joker"],grid=[1,0],align="left")

film_description = Text(app, text="Which film?", grid=[0,0], align="left")

vip_seat = CheckBox(app, text="VIP seats?", grid=[1,1],align="left")

film_description = Text(app, text="Seat type?", grid=[0,1], align="left")

row_choice = ButtonGroup(app, options=[["Front","F"],["Middle","M"],["Back","B"]],selected="M", horizontal=True, grid=[1,2], align="left")

film_description = Text(app, text="Seat location?", grid=[0,2], align="left")

book_seats = PushButton(app, command= do_booking, text="Book seat",grid=[1,4],align="left")

app.display()
