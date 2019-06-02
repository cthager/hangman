def update_lose(incorrect):
  if incorrect == 6:
    return True
  else:
    return False

def update_win(blanks):
  if blanks == 0:
    return True
  else:
    return False
