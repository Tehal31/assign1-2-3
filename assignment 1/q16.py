
def insert_sting_middle(str, word):
	return str[:2] + word + str[2:]

print(insert_sting_middle('[[]]', 'name'))
print(insert_sting_middle('{{}}', 'school'))
print(insert_sting_middle('<<>>', 'rollno.'))