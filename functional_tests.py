from selenium import webdriver


browser = webdriver.Firefox()
# Edith has heard about a cool new outline to-do app. She goes to check out its
# homepage.
browser.get('http://localhost:8000')

# She notices the page title and header mentions "To-Do"
assert 'To-Do' in browser.title

# She is invited to enter a todo item straight away

# She types "Buy peacock feathers" into a text box

# When she hits Enter, the page updates, and now the page lists 
# "1: Buy peacock feathers" as an item in a todo list

# There is still a text box inviting her to add another item. She enters 
# "Use peacock feathers to make fly" (Edith is very methodical)

# The page updates again, and now shows both items.

# Edith wonders whether the sit will remember her list. Then she sees that the
# site has generated a unique URL for here -- there is some explanatory text to
# that effect.

# She visits the URL - her todo list is still there.

# Satisfied, she goes back to sleep. 

browser.quit()
