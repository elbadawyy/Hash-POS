class Filter:
	def csvToList(self, csv):
		#print csv
		if(csv==""):
			return 255

		i=1
		temp=1
		cont=[]
		for c in csv:
			if(c!=','):
				i=i+1
				continue
			cont.append(csv[temp:i-1])
			temp=i
			i=i+1
		cont.append(csv[temp:i-2])
		#print cont
		return cont
#f = Filter()
#csv="(1,)"
#print csv
#list = f.csvToList(csv)
#print list[0]
