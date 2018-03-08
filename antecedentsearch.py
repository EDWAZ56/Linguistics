#importeer regex module
import re
#open de tekst om te lezen
text=open(r'C:\Users\EDWAZ56\Desktop\pythonantecedent\1000-passion-bfm-p.txt','r')

#ken variabele toe aan tekst
tekst=text.read()
#print volledige tekst
print tekst
#zoek alle zelfstandige naamwoorden in tekst
nouns=re.finditer('\(NP-SBJ \(([a-z]*)',tekst)
#print matchobject met alle zelfstandige naamwoorden
print nouns

#overloop alle zelfstandige naamwoorden in tekst
for noun in nouns:
    #print matchobject van zelfstandig naamwoord
    print noun
    #print zelfstandig naamwoord
    print noun.group(1)
    #positie van het zelfstandig naamwoord in de tekst
    pos=noun.span()[1]
    #print positie van het werkwoord
    print pos
    #herdefinieer tekst als tekst beginnend vanaf eindpositie zelfstandig naamwoord
    subtekst=tekst[pos:]
    print subtekst
    
    #zoek alle werkwoorden in subtekst
    
    #print matchobject met alle werkwoorden
    
    #overloop alle werkwoorden in subtekst
            #houd counter bij
                    
            #print werkwoord
            
            #positie van het werkwoord in subtekst
           
           
            #herdefinieer subtekst als tekst beginnend vanaf laatste eindpositie en eindigend bij positie werkwoord
            
            #zoek naar zelfstandig naamwoord in subtekst
            
            #indien gevonden, ga uit binnenste loop en ga naar volgend zelfstandig naamwoord en geef counter weer

            

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







