import matplotlib.pyplot as plt

# plot
def latextoplt(s):
	# clear the figure
	#plt.clf()
	
	# setting on the figure
	plt.axis('off')
	plt.title("MakeItMath!", color='grey', fontsize=35)
	
	# plot the text latex
	plt.text(0.5, 0.5, s, fontsize=50, horizontalalignment='center', verticalalignment='center')
	plt.text(0.5, 0, "Copyright 2019", fontsize=8, horizontalalignment='center', verticalalignment='center')
	fig=plt.gcf()
	plt.show()
	
	# save to file
	print("Do you want to save the picture? [Y/N]")
	save = input()
	if (save == "Y"):
		name = input("Please name your image: ")
		name = name + ".png"
		fig.savefig(name)
		print("-- YOUR", name, "HAS BEEN SAVED! --")
	plt.close()

# set the default font into a more mathematical look
plt.rcParams['mathtext.fontset'] = 'stix'

#s = r'$ \begin{matrix} a & b \\ c & d \end{matrix}$'
#print (s)
#s = "$ \\begin{bmatrix} a & b \\ b & a \\end{bmatrix}$"
#latextoplt(s)