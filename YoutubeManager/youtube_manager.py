file = open('youtube.txt' , 'w')

try: 
    file.write("hello naran khadka how are you doing")

finally:
    file.close()

with open('youtube.txt' , 'w') as file:
    file.write("Naran our khadka")