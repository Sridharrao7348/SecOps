reading_file = open("access.log", "r")

new_file_content = ""
for line in reading_file:
  stripped_line = line.strip()
  new_line = stripped_line.replace(" ", ",")
  new_file_content += new_line +"\n"
reading_file.close()

writing_file = open("access.txt", "w")
writing_file.write(new_file_content)
writing_file.close()

	
