import word_picker
import check_letter
import update_status
hangman()
win = false
lose = false
while not (win or lose):
  correct_guess = check()
  win = update_win()
  lose = update_lose()
  
