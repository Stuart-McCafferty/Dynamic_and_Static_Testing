### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # should be a double equal sign to compare values
      return True
    else  #missed : 
      return False
   

  dif highest_card(self, card1 card2): #dif = def and missed a comma between card1 and card2
  if card1.value > card2.value:
    return card #should be card1
  else:
    return card2
  

#not indented 
def cards_total(self, cards):
  total # should be total = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total #needs to be indented back will return after one iteration, also need to do a formatted string to print the integer.
  
```
