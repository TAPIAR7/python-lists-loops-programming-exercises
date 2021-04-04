parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(parking_state):
    state = {
     "total_Slots": 0,
     "available_Slots": 0,
     "occupied_Slots": 0
    }
    for row in parking_state:
        for col in row:
            
            if col == 1:
                state["occupied_Slots"] += 1
                state["total_Slots"] += 1
            elif col == 2:
                state["available_Slots"] += 1
                state["total_Slots"] += 1
                
    return state


print(get_parking_lot(parking_state))

