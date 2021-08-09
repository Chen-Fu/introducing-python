#5.1 Capitalize the word starting with m:
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
print(song.upper())


#5.2 Print each list question with its correctly matching answer, in the form:
questions = [
"We don't serve strings around here. Are you a string?",
"What is said on Father's Day in the forest?",
"What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
"An exploding sheep.",
"No, I'm a frayed knot.",
"'Pop!' goes the weasel."
]

print('Q: ' + questions[0])
print('A: ' + answers[1])
print('Q: ' + questions[1])
print('A: ' + answers[2])
print('Q: ' + questions[2])
print('A: ' + answers[0])

#5.3 Write the following poem by using old-style formatting. Substitute the strings
#'roast beef', 'ham', 'head', and 'clam' into this string:

poem = '''
My kitty cat likes %s, 
My kitty cat likes %s,
My kitty cat fell on his %s,
And now thinks he's a %s.
'''
args = ('roase beef','ham','head','clam')

print(poem % args)
      
#5.4 Write a form letter by using new-style formatting. Save the following string as
#letter (you’ll use it in the next exercise):

letter = '''
Dear {salutation} {name},


Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.
Thank you for your support.

Sincerely,
{spokesman}
{job_title}
'''

#5.5 Assign values to variable strings named 'salutation', 'name', 'product',
#'verbed' (past tense verb), 'room', 'animals', 'percent', 'spokesman', and
#'job_title'. Print letter with these values, using letter.format().

''' Wrong answer
(salutation, name, product, verbed, room, animals, percent, spokesman, job_title) = ('Dr.', 'Alice', 'mp3 player', 'exploded', 'room', 'cats', 37, 'Jack', 'Manager')
args = (salutation, name, product, verbed, room, animals, percent, spokesman, job_title)
letter % args
'''

print (
letter.format(salutation='Ambassador',
name='Nibbler',
product='pudding',
verbed='evaporated',
room='gazebo',
animals='octothorpes',
amount='$1.99',
percent=88,
spokesman='Shirley Iugeste',
job_title='I Hate This Job')
)

#5.6 After public polls to name things, a pattern emerged: an English submarine
#(Boaty McBoatface), an Australian racehorse (Horsey McHorseface), and a Swedish
#train (Trainy McTrainface). Use % formatting to print the winning name at the state
#fair for a prize duck, gourd, and spitz.

names = ['duck', 'gourd', 'spitz']
for name in names:
    cap_name = name.capitalize()
    print('%sy %sface' % (cap_name,cap_name))

#5.7 Do the same, with format() formatting.
txts = '{thing}y {thing}face'
for name in names:
    cap_name = name.capitalize()
    print(txts.format(thing = cap_name))

#5.8 Once more, with feeling, and f strings.
for name in names:
    cap_name = name.capitalize()
    print(f'{cap_name}y {cap_name}face')
