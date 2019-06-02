import word_picker
import check_letter
import update_status
word_picker() 
win = false
lose = false
while not (win or lose):
  check_letter()
  win = update_win()
  lose = update_lose()
  
