from parlex import parlex
from pltext import latextoplt
def run(tuples):
	# convert from the single token to tuple of the token
	if not(isinstance(tuples,tuple)):
		tuples = (tuples,)
		
	#initialize parameters
	s_latex = ""
	counter = 0
	
	#loop through the tuples
	while (len(tuples) > counter):
		# if the tuple is empty
		if (tuples[counter] == None):
			break
		
		# if the tuple contain tuples
		if (isinstance(tuples[counter],tuple)):
			s_latex = s_latex + run(tuples[counter])
			counter = counter + 1
		
		# convert the tokens into the latex
		else:
			now = tuples[counter]
			
			#if the token is str 
			if (isinstance(now, str)):
				#fraction
				if (now == 'frac'):
					s_latex = s_latex + "\\frac{" + run( tuples[counter+1] ) + "}{" + run( tuples[counter+2] )  + "}"
					counter = counter + 3
				#root
				elif (now == 'sigma'):
					s_latex = s_latex + "\\sum_{" + run( tuples[counter+1] ) + "}^{" + run( tuples[counter+2] )  + "}"
					counter = counter + 3
				#integral
				elif (now == 'integral'):
					s_latex = s_latex + "\\int_{" + run( tuples[counter+1] ) + "}^{" + run( tuples[counter+2] )  + "}" + run( tuples[counter+3]) + "dx"
					counter = counter + 4
				#root
				elif (now == 'root' or now == '√'):
					s_latex = s_latex + "\\sqrt[" + run( tuples[counter+1] ) + "]{" + run( tuples[counter+2] )  + "}"
					counter = counter + 3
				#log
				elif (now == 'log'):
					s_latex = s_latex + "log_{" + run( tuples[counter+1] ) + "}(" + run( tuples[counter+2] ) + ")"
					counter = counter + 3
				#pi
				elif (now == 'pi'):
					s_latex = s_latex + "\\pi" 
					counter = counter + 1
				#sin
				elif (now == 'sin'):
					s_latex = s_latex + "\\sin" 
					counter = counter + 1
				#cos
				elif (now == 'cos'):
					s_latex = s_latex + "\\cos" 
					counter = counter + 1
				#tan
				elif (now == 'tan'):
					s_latex = s_latex + "\\tan" 
					counter = counter + 1
				# *, TIMES
				elif(now == '*'):
					s_latex = s_latex + '*'
					counter = counter + 1
				# +, PLUS
				elif(now == '+'):
					s_latex = s_latex + '+'
					counter = counter + 1	
				# -, MINUS
				elif(now == '-'):
					s_latex = s_latex	+ '-'
					counter = counter + 1
				# /, DIVIDES
				elif(now == '/'):
					s_latex = s_latex + '/'
					counter = counter + 1		
				# (, openingBracket)
				elif(now == '('):
					s_latex = s_latex + '('
					counter = counter + 1
				# ),closingBracket
				elif(now == ')'):
					s_latex = s_latex + ')'
					counter = counter + 1
				# =, equal
				elif(now == '='):
					s_latex = s_latex + '='
					counter = counter + 1
				# ^, power
				elif(now == '^'):
					s_latex = s_latex + '^{' + run(tuples[counter+1]) + '}'
					counter = counter + 2
				# variable, var-x
				elif("var-" in now):
					s_latex = s_latex + now[len(now)-1]
					counter = counter + 1
				# infinity
				elif (now == "infinity"):
					s_latex = s_latex + "\infty"
					counter = counter + 1
				# >, bigger
				elif(now == '>'):
					s_latex = s_latex + '>'
					counter = counter + 1
				# <, smaller
				elif(now == '<'):
					s_latex = s_latex + '<'
					counter = counter + 1
				# >=, biggerEqual
				elif(now == '>='):
					s_latex = s_latex + '\\geq'
					counter = counter + 1
				# <=, smallerEqual
				elif(now == '<='):
					s_latex = s_latex + '\\leq'
					counter = counter + 1
				# percentage
				elif(now == '%'):
					s_latex = s_latex + '\\%'
					counter = counter + 1
				# alpha
				elif(now == 'alpha'):
					s_latex = s_latex + '\\alpha'
					counter = counter + 1
				# beta
				elif(now == 'beta'):
					s_latex = s_latex + '\\beta'
					counter = counter + 1
				# gamma
				elif(now == 'gamma'):
					s_latex = s_latex + '\\gamma'
					counter = counter + 1
				# theta
				elif(now == 'theta'):
					s_latex = s_latex + '\\theta'
					counter = counter + 1
				# !=, notEqual
				elif(now == '!='):
					s_latex = s_latex + '\\neq '
					counter = counter + 1
				# approx
				elif(now == 'approx'):
					s_latex = s_latex + '\\approx '
					counter = counter + 1
				
			else :
				# int float digit
				if (isinstance(now,int)):
					s_latex = s_latex + str(now)
					counter = counter + 1
	return s_latex
	
# main program - you run the program from here!
print ("""
- - - - WELCOME TO MakeItMath - - - - - - - - -
- - - - Please input any equations here - - - -
""")

# multiple inputs
while True:
	# get the inputs
	try:
		text = input(">>")
	except EOFError:
		break
	# lexing and parsing analysis
	tuples = parlex(text)
	# convert into latex 
	result = "$ " + run(tuples) + " $"
	
	
	if (result == "$  $"):
		print("\n ~ Conversion Complete! ~" )
		break
	else:
		# display
		latextoplt(result)
