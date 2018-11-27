#importeer regex module
import re
import sys
#read and write csv files
import csv
#open folders
import os




def antecedentsearch(listfile,folder):
    #create csv file with header for aggregate output
    aggregateoutput=open("aggregate_output.csv","w")
    aggregateoutputwriter=csv.writer(aggregateoutput,delimiter=";",quotechar='|', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
    aggregateoutputwriter.writerow(['noun','cardinality','type','textfile'])
    #loop folder with text files to scan
    for textfile in os.listdir(folder):
        #open text file for reading
        text=open(folder+"/"+textfile,'r')
        #ken variabele toe aan tekst
        tekst=text.read()
        #print volledige tekst
        #print tekst
        #zoek alle zelfstandige naamwoorden in tekst
        nouns=re.finditer('NC(S|PL) ([A-Za-z]*)\)',tekst)
        #print matchobject met alle zelfstandige naamwoorden
        print (nouns)

        #overloop alle zelfstandige naamwoorden in tekst
        counter=0
        nouncounter=0
        #create csv file with header
        singleoutput=open("%s_output.csv" % (textfile),"w")
        singleoutputwriter=csv.writer(singleoutput,delimiter=";",quotechar='|', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
        singleoutputwriter.writerow(['noun','cardinality','type'])
        #create list of noun and cardinality tuples
        outputlist=[]
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
            nounoccurence=noun.group(2)
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
                print ('The noun %s was found after %s verbs.' %(nounoccurence,cardinality))                     
            else:
                nouncopy=noun.group(1)
                cardinality=0
                print ('The noun %s was not found.' %(nounoccurence))
                
            #add noun-cardinality tuple to list
            outputlist.append((nounoccurence,cardinality))    
        #sort list by number of verbs found descending
        outputlist=sorted(outputlist,key=lambda x: x[1], reverse=True)
            
            
        #write result to csv file 
        for item in outputlist:
            #read list file
            list=open(listfile,'r')
            listreader=csv.reader(list,delimiter=';')     
            #loop over list
            type=""
            for listitem in listreader:
                #check if the noun is in the list
                if listitem[0]==item[0]:
                    #determine the type of the noun
                    type=listitem[1]
                    break
            
            
        
        
            #write result to output file
            singleoutputwriter.writerow([item[0],item[1],type])
            #update aggregate output file
            aggregateoutputwriter.writerow([item[0],item[1],type,textfile])
         
        
        singleoutput.close()
        #close input text file
        text.close()
    #close csv
    aggregateoutput.close()
#open de tekst om te lezen        
textfile=sys.argv[1]   
folder=sys.argv[2]   
antecedentsearch(textfile,folder)


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







