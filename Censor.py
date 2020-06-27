# Title = "Censor Dispenser"
# Project Goals : - 
# You’ve recently gotten a job working in the IT department at one of Silicon Valley’s hottest new startups, AirWeb. The company is developing a state-of-the-art artificial intelligence engine designed to help provide a new perspective on the world’s problems. Interestingly, very few people know the details of AirWeb ‘s work and the company is very secretive about its technology, even to its own investors.

# You report directly to the Head of Product, a person named Mr. Cloudy, and he has a very important task for you. You see, every month, the head researchers down in the lab send an email to the board of investors to tell them about the status of the project. Cloudy wants you to intercept these emails and censor any “proprietary information” included in them.


#################SOLUTION STARTS HERE####################
#TYPE 1
# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


# This function can censor a specific word or phrase from a body of text, and then return the text.
def censor_one(email, censor):
  censored_item = ""
  for i in range(0,len(censor)):
    if censor[i] == " ":
      censored_item = censored_item + " "
    else:
    	censored_item = censored_item + "X"
  return email.replace(censor, censored_item)

#print(censor_one(email_one, "learning algorithms"))


######################################################

#TYPE 2
# This function can censor not just a specific word or phrase from a body of text, but a whole list of words and phrases, and then return the text.


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
def censor_two(email, censored_list):
  for word in censored_list:
    censored_word = ""
    for x in range(0,len(word)):
      if word[x] == " ":
        censored_word = censored_word + " "
      else:
        censored_word = censored_word + "X"
    email = email.replace(word, censored_word)
  return email

#print(censor_two(email_two, proprietary_terms))
#####################################################
# TYPE 3
# This function can censor any occurance of a word from the “negative words” list after any “negative” word has occurred twice, as well as censoring everything from the list from the previous step as well and use it to censor email_three

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

dnegative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]


def censor_three(input_text, censored_list, negative_words):
  input_text_words = []
  for x in input_text.split(" "):
    x1 = x.split("\n")
    for word in x1:
      input_text_words.append(word)
  for i in range(0,len(input_text_words)):
    if (input_text_words[i] in censored_list) == True:
      word_clean = input_text_words[i]
      censored_word = ""
      for x in range(0,len(word_clean)):
        censored_word = censored_word + "X"
      input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)
    count = 0
    for i in range(0,len(input_text_words)):
      if (input_text_words[i] in negative_words) == True:
        count += 1
        if count > 2:
          word_clean = input_text_words[i]
          for x in punctuation:
            word_clean = word_clean.strip(x)
          censored_word = ""
          for x in range(0,len(word_clean)):
            censored_word = censored_word + "X"
          input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)
  return " ".join(input_text_words)
#print(censor_three(email_three, proprietary_terms, negative_words))




