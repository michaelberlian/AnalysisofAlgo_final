"""
Marcell Alvianto
Kevin Dimas
Michael Berlian
Marco Melvern
""" 
import ply.lex as lex
import ply.yacc as yacc

# list of tokens available
tokens = [
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDES',
	'openingBracket',
	'closingBracket',
	'fraction',
	'root',
	'power',
	'pi',
	'sin',
	'cos',
	'tan',
	'percentage',
	'alpha',
	'beta',
	'gamma',
	'infinity',
	'sigma',
	'bigger',
	'smaller',
	'biggerEqual',
	'smallerEqual',
	'equal',
	'log',
	'float',
	'comma',
	'variable',
	'int',
	'integral',
	'theta',
	'notEqual',
	'approx'
]

# token rules
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDES = r'\/'
t_openingBracket = r'\('
t_closingBracket = r'\)'
t_percentage = r'\%'
t_bigger = r'\>'
t_smaller = r'\<'
t_equal = r'\='
t_power = r'\^'
t_comma = r'\,'

t_ignore = r' '

def t_notEqual(t):
	r'(\!\=)'
	t.type = 'notEqual'
	return t

def t_root(t):
	r'(root)|(\√)'
	t.type = 'root'
	return t

def t_approx(t):
	r'approx'
	t.type = 'approx'
	return t
		
def t_integral(t):
	r'(integral)'
	t.type = 'integral'
	return t
	
def t_float(t):
	r'(\d+\.\d+)'
	t.value = float(t.value)
	return t

def t_int(t):
	r'(\d+)'
	t.value = int(t.value)
	return t

def t_fraction(t):
	r'frac'
	t.type = 'fraction'
	return t

def t_pi(t):
	r'pi'
	t.type = 'pi'
	return t

def t_sin(t):
	r'sin'
	t.type = 'sin'
	return t

def t_cos(t):
	r'cos'
	t.type = 'cos'
	return t

def t_tan(t):
	r'tan'
	t.type = 'tan'
	return t

def t_alpha(t):
	r'alpha'
	t.type = 'alpha'
	return t

def t_beta(t):
	r'beta'
	t.type = 'beta'
	return t

def t_gamma(t):
	r'gamma'
	t.type = 'gamma'
	return t

def t_theta(t):
	r'theta'
	t.type = 'theta'
	return t

def t_infinity(t):
	r'infinity'
	t.type = 'infinity'
	return t
	
def t_sigma(t):
	r'sigma'
	t.type = 'sigma'
	return t

def t_smallerEqual(t):
	r'\<\='
	t.type = 'smallerEqual'
	return t

def t_biggerEqual(t):
	r'\>\='
	t.type = 'biggerEqual'
	return t

def t_log(t):
	r'log'
	t.type = 'log'
	return t

def t_variable(t):
	r'[a-zA-Z]'
	t.type = 'variable'
	return t
	
def t_error(t):
	print("Whoops! Illegal characters! \n on:",t.lexpos)
	t.lexer.skip(1)
	
	
#parsing rule
def p_MiM(p):
	'''
	MiM : expression
			 | equation
			 | logical_expr
			 | empty
	'''
	p[0]=p[1]

	
def p_expression_complex(p):
	'''
	expression : fraction openingBracket expression comma expression closingBracket
						 | root openingBracket expression comma expression closingBracket
						 | log openingBracket int comma expression closingBracket
						 | log openingBracket variable comma expression closingBracket
	'''
	p[0]=(p[1],p[3],p[5])

def p_expression_tri(p):
	'''
	expression : trigono openingBracket expression closingBracket
						 | sin openingBracket expression closingBracket
						 | cos openingBracket expression closingBracket
						 | tan openingBracket expression closingBracket
	'''  
	p[0] = (p[1],p[2],p[3],p[4])

def p_equation_sigma(p):
	'''
	equation : sigma openingBracket assign comma infinity comma expression closingBracket
					 | sigma openingBracket assign comma int comma expression closingBracket
					 | integral openingBracket int comma infinity comma expression closingBracket
					 | integral openingBracket int comma int comma expression closingBracket
	'''
	p[0] = (p[1],p[3],p[5],p[7])	


def p_expression (p):
	'''
	expression : expression PLUS expression
						 | expression MINUS expression
						 | expression DIVIDES expression
						 | expression TIMES expression
						 | expression power int
						 | expression power coefficient
						 | openingBracket expression closingBracket
	'''
	p[0]= (p[1],p[2],p[3])

def p_expression_power(p):
	'''
	expression : expression power openingBracket expression closingBracket
	'''
	p[0]=(p[1],p[2],(p[3],p[4],p[5]))
	
def p_expression_number (p):
	'''
	expression : int
						 | float
						 | coefficient
						 | pi
						 | percentage
						 | alpha
						 | beta
						 | gamma
						 | theta
						 | infinity
	'''
	p[0] = (p[1]) 
	
def p_coefficient_const(p):
	'''
	coefficient : int variable
							| float variable
							| coefficient variable
							| expression percentage
	'''
	if (p[2] == '%'):
		p[0] = (p[1],p[2])
	else :
		p[0] = (p[1],"var-" + p[2])
		

def p_coefficient_sym(p):
	'''
	coefficient : int theta
							| int beta
							| int alpha
							| float theta
							| float beta
							| float alpha
	'''
	p[0] = (p[1],p[2])
	
def p_coefficient_var(p):
	'''
	coefficient : variable
	'''
	p[0] = ("var-" + p[1])
	
def p_trigono_int(p):
	'''
	trigono : sin power int
					| cos power int
					| tan power int
	'''
	p[0] = (p[1],p[2],p[3])
	
def p_trigono_var(p):
	'''
	trigono : sin power variable
					| cos power variable
					| tan power variable
	'''
	p[0] = (p[1],p[2],"var-" + p[3])

def p_equation(p):
	'''
	equation : variable equal expression
	'''
	p[0] = ("var-" + p[1],p[2],p[3])

def p_logical_expr(p):
	'''
	logical_expr : expression equal expression
							 | expression bigger expression
							 | expression smaller expression
							 | expression biggerEqual expression
							 | expression smallerEqual expression
							 | expression notEqual expression
							 | expression approx expression
	'''
	p[0] = (p[1],p[2],p[3])

def p_assign(p):
	'''
	assign : variable equal int
	'''
	p[0] = ("var-" + p[1],p[2],p[3])
					
def p_error(p):
	print("""
	============================
	 Oh No!! We found error(s)
	============================
	
	Please try again..
	""")
	print ("ERROR in token",p.type, "at", p.lexpos)
	return

def p_empty (p):
	'''
	empty :
	'''
	p[0] = None

# function to parsing and lexing
def	parlex(s):
	# create the lexer
	lexer = lex.lex()
	# create the parser
	parser = yacc.yacc()
	# lexing and parsing the input(s)
	s_tuples = parser.parse(s)
	return s_tuples