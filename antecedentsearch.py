#importeer regex module
import re
#open de tekst om te lezen
text=open(r'C:\Users\EDWAZ56\Desktop\pythonantecedent\1000-passion-bfm-p.txt','r')

#ken variabele toe aan tekst
tekst=text.read()
#print volledige tekst
#print tekst
#zoek alle zelfstandige naamwoorden in tekst
nouns=re.finditer('NCS ([A-Za-z]*)\)',tekst)
#print matchobject met alle zelfstandige naamwoorden
print nouns

#overloop alle zelfstandige naamwoorden in tekst
counter=0
nouncounter=0
for noun in nouns:
    #print matchobject van zelfstandig naamwoord
    #print noun
    
    #positie van het zelfstandig naamwoord in de tekst
    pos=noun.span()[1]
    #print positie van het zelfstandig naamwoord
    #print pos
    #herdefinieer tekst als tekst beginnend vanaf eindpositie zelfstandig naamwoord
    subtekst=tekst[pos:]
    #print subtekst
    
    #zoek volgende zelfstandig naamwoord kopie in tekst
    nounoccurence=noun.group(1)
    regex='NCS (%s)\)' %(nounoccurence) 
    nouncopy=re.search(regex,subtekst)
    #indien gevonden, herdefinieer subtekst als tekst tussen twee opeenvolgende zelfde zelfstandige naamwoorden
    if nouncopy is not None:
        endpos=nouncopy.span()[1]
        subtekst=subtekst[:endpos]
        
        #zoek naar werkwoorden in subtekst
        verbs=re.finditer('VJ ',subtekst)   
        cardinality=0
        #houd de tel bij van aantal werkwoorden
        for verb in verbs:
            cardinality+=1
        print 'The noun %s was found after %s verbs.' %(nounoccurence,cardinality)
    else:
        nouncopy=noun.group(1)
        print 'The noun %s was not found.' %(nounoccurence)
    
    
 


'''#zoek volgende woord pastoor op regel
prog=re.compile('pastoor')
m=prog.search(regel)
if m !=None:
    pos=m.span()
    #print m.read()
    print pos
    #zoek pastoor op volgende regel
    #als pastoor bestaat,zoek eerstvolgende pastoor op regel
    m=prog.search(regel,pos[1])
    if m!= None:
        pos=m.span()
        print pos
#ga na 5 volgende lijnen niet meer naar volgende lijn en geef bericht dat dit een antecedent is als pastoor gevonden is en dat dit geen antecedent is als pastoor niet gevonden is
'''







