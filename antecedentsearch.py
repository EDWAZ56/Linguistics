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
    
    #zoek alle werkwoorden in subtekst
    verbs=re.finditer('VJ ',subtekst)
    #print matchobject met alle werkwoorden
    #print verbs
    #initiate cardinality, set cardinality to 0
    cardinality=0
    #initiate verbpos
    verbposold=0
    #overloop alle werkwoorden in subtekst
    nouncounter+=1
    for verb in verbs:
            #houd counter bij
            cardinality+=1
            #print werkwoord
            #print verb
            #print verb.group()
            #positie van het werkwoord in subtekst
            verbposnew=verb.span()[1]-verbposold
            
            #herdefinieer subtekst als tekst beginnend vanaf laatste eindpositie en eindigend bij positie werkwoord
            subtekst=subtekst[verbposold:verbposnew]
            
            #redefine verbposold
            verbposold=verbposnew          
            #zoek naar zelfstandig naamwoord in subtekst
            #print noun.group(1)
            nounoccurence=noun.group(1)
            regex='NCS (%s)\)' %(nounoccurence) 
            nouncopy=re.search(regex,subtekst)
            #indien gevonden, ga uit binnenste loop en ga naar volgend zelfstandig naamwoord en geef counter weer
            if nouncopy is not None:
                print subtekst
                print cardinality
                nouncopy=noun.group(1)
                print 'The noun %s was found after verb number %s' %(nouncopy,cardinality)
                counter+=1
                break
            else:
                continue
print counter
print nouncounter


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







