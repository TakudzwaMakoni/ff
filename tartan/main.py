import tartan as t

title, version, repo, company, year, language, author, git = 'tartan','alpha','freedomfighter (c)','Milli (c)', '2018','Python 3.6', 'Takudzwa Makoni','https://github.com/Makoni-Milli/'

t.bessie(title, version, repo, company, year, language, author, git)

pallet = {'HG':'#285800','K':'#101010','R':'#C80000','W':'#E0E0E0','Y':'#E8C000', 'LN':'#C0C0C0','TK':'#8C7038','RB':'#0C585C','DR':'#880000','GO':'#FFD700','MB':'#3474FC','RC':'#5C5C5C','BB':'#14283C','EG':'#004028','DB':'#202060','DGR':'#003C14','R':'#C80000','CW':'#FCFCFC'}

filename = input('filename: ') + '.txt'
SorR = input('symmetric or repetitive (s/r): ')
print('weaving...')
t.tartan( filename, SorR, pallet)

