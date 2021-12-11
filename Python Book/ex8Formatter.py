#Initial variable for Format string
formatter = "{} {} {} {}"
#Printing various outputs using the formatter string
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,True,False))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
" Try your\n",
"Own text here\n",
"Maybe a poem\n",
"Or a song about fear\n"
))
