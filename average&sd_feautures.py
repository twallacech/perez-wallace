def stand_dev(lista1):
	lista = [map(int, x) for x in lista1]
	if len(lista)>1:
		contador_prom=0
		cant_datos=0
		for numero in lista:
			cant_datos+=1
			contador_prom+=numero
		promedio=contador_prom/cant_datos
		contador_prom_dev=0
		for numero in lista:
			diferencia=abs(promedio-numero)
			dif_square=diferencia**2
			contador_prom_dev+=dif_square
		varianza=contador_prom_dev/(cant_datos-1)
		stdev=varianza**(1/2)    
		return stdev
	else:
		return 0

def avrg(lista):
	a = reduce(lambda x, y: x + y, lista) / len(lista)
	return a

a= open("txtfilegenc1c2c3.txt","r")
b=a.readlines()

lst_sosn_average_subjectivity_statuses = []
lst_sosn_average_subjectivity_comments = []
lst_sosn_sd_average_subjectivity_reviews = []
lst_sosn_sd_average_subjectivity_comments = []
lst_sosn_average_polarity_statuses = []
lst_sosn_average_polarity_comments = []
lst_sosn_sd_average_polarity_statuses = []
lst_sosn_sd_average_polarity_comments = []
lst_somp_average_subjectivity_reviews = []
lst_somp_average_subjectivity_comments = []
lst_somp_sd_average_subjectivity_reviews = []
lst_somp_sd_average_subjectivity_comments = []
lst_somp_average_polarity_reviews = []
lst_somp_average_polarity_comments = []
lst_somp_sd_average_polarity_reviews = []
lst_somp_sd_average_polarity_comments = []
lst_aosn_in_degree = []
lst_aosn_out_degree = []


for line in b:
	lin=line.strip("\n")
	n=lin.split(";")
	lst_sosn_average_subjectivity_statuses.append(n[1])
	lst_sosn_average_subjectivity_comments.append(n[2])
	lst_sosn_sd_average_subjectivity_reviews.append(n[3])
	lst_sosn_sd_average_subjectivity_comments.append(n[4])
	lst_sosn_average_polarity_statuses.append(n[5])
	lst_sosn_average_polarity_comments.append(n[6])
	lst_sosn_sd_average_polarity_statuses.append(n[7])
	lst_sosn_average_polarity_comments.append(n[8])
	lst_somp_average_subjectivity_reviews.append(n[9])
	lst_somp_average_subjectivity_comments.append(n[10])
	lst_somp_sd_average_subjectivity_reviews.append(n[11])
	lst_somp_sd_average_subjectivity_comments.append(n[12])
	lst_somp_average_polarity_reviews.append(n[13])
	lst_somp_average_polarity_comments.append(n[14])
	lst_somp_sd_average_polarity_reviews.append(n[15])
	lst_somp_sd_average_polarity_comments.append(n[16])
	lst_aosn_in_degree .append(n[17])
	lst_aosn_out_degree.append(n[18])	

print('Desviaciones Estandar de cada feature:')
stand_dev(lst_sosn_average_subjectivity_statuses)
stand_dev(lst_sosn_average_subjectivity_comments)
stand_dev(lst_sosn_sd_average_subjectivity_reviews)
stand_dev(lst_sosn_sd_average_subjectivity_comments)
stand_dev(lst_sosn_average_polarity_statuses)
stand_dev(lst_sosn_average_polarity_comments)
stand_dev(lst_sosn_sd_average_polarity_statuses)
stand_dev(lst_sosn_sd_average_polarity_comments)
stand_dev(lst_somp_average_subjectivity_reviews)
stand_dev(lst_somp_average_subjectivity_comments)
stand_dev(lst_somp_sd_average_subjectivity_reviews)
stand_dev(lst_somp_sd_average_subjectivity_comments)
stand_dev(lst_somp_average_polarity_reviews)
stand_dev(lst_somp_average_polarity_comments)
stand_dev(lst_somp_sd_average_polarity_reviews)
stand_dev(lst_somp_sd_average_polarity_comments)
stand_dev(lst_aosn_in_degree)
stand_dev(lst_aosn_out_degree)


print('medias de cada feature:')
avrg(lst_sosn_average_subjectivity_statuses)
avrg(lst_sosn_average_subjectivity_comments)
avrg(lst_sosn_sd_average_subjectivity_reviews)
avrg(lst_sosn_sd_average_subjectivity_comments)
avrg(lst_sosn_average_polarity_statuses)
avrg(lst_sosn_average_polarity_comments)
avrg(lst_sosn_sd_average_polarity_statuses)
avrg(lst_sosn_sd_average_polarity_comments)
avrg(lst_somp_average_subjectivity_reviews)
avrg(lst_somp_average_subjectivity_comments)
avrg(lst_somp_sd_average_subjectivity_reviews)
avrg(lst_somp_sd_average_subjectivity_comments)
avrg(lst_somp_average_polarity_reviews)
avrg(lst_somp_average_polarity_comments)
avrg(lst_somp_sd_average_polarity_reviews)
avrg(lst_somp_sd_average_polarity_comments)
avrg(lst_aosn_in_degree)
avrg(lst_aosn_out_degree)
