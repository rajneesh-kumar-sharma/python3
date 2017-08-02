original=raw_input("Enter a word:")
if len(original)>0 and original.isalpha():
  word=original.upper()
  second=word[1]
  print word
  print second
else:
  print 'empty'
