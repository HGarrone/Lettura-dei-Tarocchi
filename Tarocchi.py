
import os
import sys
from importlib.machinery import SourceFileLoader

#nel caso in cui il programma non trovasse il path corretto sostituirlo con file_path=<path_corretto>. Se utilizzate Windows utilizzate \\ anzichè \ nel path. 

#print('sys.argv[0] =', sys.argv[0])             
pathname = os.path.dirname(sys.argv[0])        
file_path = pathname
full_path=os.path.abspath(pathname)

image_inverter = SourceFileLoader('image_inverter', file_path+'\\image_inverter.py').load_module()


def descrizione(arcano, senso, ambito):
    proprietà={}
    Dettagli="Dettagli"
    Amore="Amore"
    Lavoro_e_denaro="Lavoro_e_denaro"
    Salute="Salute"
    Persone="Persone"
    
    if arcano == "Il Bagatto":
  
       if senso == "dritto":          
          proprietà[Dettagli]= "Il significato positivo di base di questa carta, legato all’uscita a dritto, è la capacità di ottenere ciò che si desidera, se vogliamo, quindi il suggerimento di perseguire nei propri obiettivi. Il significato è in generale favorevole, e indica che quel momento è quello giusto per fare quello che vogliamo fare. \nIl bagatto sta ad indicare, in generale, l’abilità, la riuscita, la creatività, l’energia a disposizione e la possibilità di un’azione rapida; è quindi legato sia all’inizio di qualcosa di nuovo, sia alla capacità di riuscire in quello che abbiamo intensione di fare. \nQuesto è valido in qualunque ambito: dal lavoro, che sarebbe la prospettiva principale (iniziare un nuovo progetto, aprire un’attività, cambiare lavoro), al piano personale e interpersonale, per esempio iniziando una nuova relazione.\nIl bagatto indica la possibilità di un cambiamento che deve essere colta, perché può essere sfruttata: se abbiamo avuto un’intuizione, un’idea diversa dal solito, il classico “lampo di genio”, è il momento di sfruttarlo e cercare di capire come utilizzarlo. Poiché la descrizione è generica, è importante che venga accostato, per la comprensione, alla carta che precede oppure che segue, per capire meglio l’ambito della nostra vita a cui si riferisce.\nIl bagatto sta ad indicare anche che il tempo è maturo per poter prendere decisioni importanti, per poter agire, e anche se i risultati non si vedranno subito (perché si fa riferimento all’inizio di qualcosa di nuovo, che poi dobbiamo chiaramente essere in grado di portare avanti) non c’è un momento migliore per riuscire in quello che vogliamo ottenere."
          proprietà[Amore]="indica in generale l’inizio di un amore importante, ma anche il fascino che si esprime sulle altre persone e quindi le conquiste. Può anche significare l’inizio di un nuovo rapporto di amicizia."
          proprietà[Lavoro_e_denaro]="Similmente a quanto accade sul piano effettivo, indica la possibilità di cambiare lavoro, di iniziare qualcosa di nuovo, il prospetto di un guadagno importante."
          proprietà[Salute]="Dal punto di vista della salute, un miglioramento improvviso, o il funzionamento di una terapia se la stiamo seguendo. Sul piano psicologico indica anche un miglioramento del nostro stato generale."
          proprietà[Persone]="il Bagatto indica una persona giovane, abile, affascinante, intraprendente, non dotato di poteri ma che sa sfruttare le proprie possibilità per cercare di ottenere quello che vuole."
       else:
          proprietà[Dettagli]="Quando la carta del Bagatto esce al contrario, l’effetto è particolare, perché può assumere due forme diverse: da un lato, l’abilità può rimanere ma questa viene esasperata, resa eccessivamente esuberante, tanto da non avere sfoci nel positivo ma nel negativo, a causa dell’eccesso. Dall’altro lato, indica il blocco delle capacità, un’abilità che è presente, rimane, ma che viene improvvisamente bloccata e rimane inutilizzata. \nNel primo caso, sta ad indicare in generale la scelta di una strada sbagliata, magari non manca l’abilità ma la stiamo utilizzando in un modo che non è corretto. O, in alternativa, potrebbe significare che stiamo usando la nostra abilità e la nostra capacità nel modo giusto ma da essa stiamo pretendendo troppo, e questo si rivolge contro di noi facendoci perdere anche quanto di buono abbiamo già fatto. Nel complesso, quindi, se stiamo impiegando le nostre energie in qualcosa, dobbiamo cercare di fare attenzione, e riflettere sul fatto che magari dobbiamo fermarci e cercare di fare qualcosa di diverso, oppure limitare le risorse che stiamo investendo.\nNel secondo caso, invece, indica che stiamo proprio buttando la nostra abilità in qualcosa che non porterà a nulla. Ci possiamo impegnare per ottenere una promozione, per iniziare qualcosa di nuovo come un progetto, che però non è destinato ad andare a buon fine, e questo porterà di fatto allo spreco delle nostre capacità. \nDal punto di vista affettivo potrebbe rivelarsi un rapporto a cui teniamo molto ma che per nostra causa si sta deteriorando, oppure che per causa altrui non riusciamo a far fruttare come vorremmo; in un caso è ancora possibile porre rimedio contenendoci, nell’altro è meglio cambiare strada. Una situazione simile si riscontra anche sul piano professionale, per il quale è opportuno riflettere per capire bene quale direzione vogliamo intraprendere.\nAttenzione, infine, all’apertura di troppi progetti insieme, all’avere troppe idee: potrebbe essere questo eccesso a portare al fallimento di tutte, in contemporanea."
          proprietà[Amore]="Un rapporto che non si conclude come vorremmo o per mancanza di attrazione da parte dell’altra persona, oppure a causa dei nostri errori. Può anche essere il rapporto già in atto che si incrina."
          proprietà[Lavoro_e_denaro]="un progetto sbagliato, uno spreco delle nostre risorse, un modo sbagliato di utilizzare le nostre capacità, una strada intrapresa che non va a buon fine."
          proprietà[Salute]="indica la mancanza dei risultati ottenuti con qualcosa che abbiamo provato ad iniziare, ma che non andrà a buon fine. Può indicare, in medicina, anche un accanimento terapeutico."
          proprietà[Persone]="indica una persona che parla troppo, eccessivamente esuberante, che cerca di ottenere qualcosa a tutti i costi, una persona presuntuosa o invadente."

    elif arcano == "La Papessa":
       if senso == "dritto":
          proprietà[Dettagli]="Il significato positivo della carta quando esce dritta e non a rovescio indica un beneficio, una saggezza e una completezza non sul piano materiale ma su quello spirituale, sfociando nella ricerca dell’io interiore.\nQuesta carta rappresenta la contemplazione, l’interpretazione divinatoria, il profondo processo di trasformazione e il silenzio che una persona più attraversare.\nRappresenta anche una figura femminile che non si abbassa alla superiorità della figura maschile, mantenendo gelosamente una conoscenza segreta, preclusa. Non si sottopone ad alcun comportamento di inferiorità, ma anzi cerca di procedere decisa nelle proprie scelte, in modo consapevole, cerca di svelare i misteri e trovare le soluzioni.\nInoltre procede con costanza nelle opere intraprese, cercando di portarle al meglio delle proprie possibilità. Riguardo al processo di conoscenza interiore, simboleggia la pazienza, la costanza, l’armonia, la ricerca di un miglioramento costante e continuo, la riflessione; indica l’oggettività nel prendere le decisioni e la ricerca della conoscenza, della saggezza.\nLa carta invita a contenere le emozioni e l’impulsività, spingendo a sostituirle con la calma, con la riflessione; le decisioni affrettate devono essere rifuggite, e se c’è una decisione da prendere il processo deve essere lento, ponderato. Anche decisioni impulsive, magari legate a cambiamenti improvvisi, dovrebbero essere rimandate e valutate meglio prima di procedere, cercando di capire con oggettività quali possono essere le conseguenze positive e quali negative. Inoltre, importante è il recuperare il rapporto con sé stessi: passare dei momenti da soli per riflettere, per capire in che direzione andare della nostra vita, dialogando con noi stessi più che con gli altri, cercare di capire quali sono i nostri desideri, i nostri sogni, le nostre passioni, cercando di recuperarle e di dedicare più tempo ad esse."
          proprietà[Amore]="si prospetta un rapporto di coppia sano e prolungato, oppure quello già al momento presente è destinato a continuare in serenità. Può indicare un matrimonio o dei figli in arrivo."
          proprietà[Lavoro_e_denaro]="Indica la necessità di riflettere bene sulle proprie scelte, sia quelle finanziarie che quelle lavorative."
          proprietà[Salute]="Indica la necessità di riflessione, di pensiero spostato sul piano psicologico che su quello della salute fisica. Cercare di alleviare lo stress, di migliorare la nostra condizione di vita generale."
          proprietà[Persone]="la Papessa indica una presenza femminile che fornisce buoni consigli, validi e utili; può essere la donna che ci sta accanto, se si è uomini, oppure un’amica, nel caso di una donna, o anche una madre o una sorella. In alcuni casi, una figura religiosa."
       else:
          proprietà[Dettagli]="I significati negativi della Papessa riguardano i risvolti negativi della riservatezza e del silenzio.\nEssere riservati non permette di creare relazioni, essere silenziosi non permette di stringere legami, di risolvere problemi, di migliorare la propria situazione generale.\nUn altro importante significato è il rifiuto della conoscenza, che non permette di migliorare la nostra situazione, la paura di approfondire un rapporto, la difficoltà nel cercare di aprirei nuove strade o intraprendere nuovi percorsi.\nRappresenta il silenzio di chiusura verso il mondo esterno, la mancanza di curiosità, le situazioni che vanno avanti solo per inerzia, senza che noi facciamo alcun tipo di intervento attivo. Dal punto di vista delle relazioni, può significare un rapporto che va avanti senza amore, senza voglia di crescere, senza che nessuno faccia il primo passo per migliorare la situazione della relazione (oppure per romperla). Dal punto di vista lavorativo, indica un progetto che stenta a decollare, o più semplicemente che avrebbe bisogno di un nostro intervento attivo che, tuttavia, tarda ad arrivare.\nIn generale, l’indicazione è quella di approfondire la mancanza di una comunicazione, di un dialogo, con le persone che ci circondano: solo parlando dei problemi, degli ostacoli, delle costrizioni, ci è possibile superarle, mentre quello che stiamo facendo è rimanere in difesa, lontani da tutto e da tutti, un’atteggiamento sbagliato che può portare a conseguenze negative sul nostro futuro, in tutti gli ambiti.\nUn ultimo significato è la paura di affrontare l’ignoto e lo sconosciuto, una paura che deve essere superata se vogliamo uscire dalla situazione che ci attanaglia. L’ignoto non deve essere visto come elemento di paura, ma come un’opportunità di accrescere la nostra conoscenza, di aumentare le nostre vedute, di scoprire strade che non avevamo considerato."
          proprietà[Amore]="Un rapporto che si protrae da troppo tempo senza un intervento deciso da parte nostra per far cambiare rapidamente direzione. Può anche indicare una situazione di solitudine che non riusciamo a risolvere a causa della mancanza di un nostro intervento, di un’azione decisa."
          proprietà[Lavoro_e_denaro]="un progetto fermo, che non decolla, oppure una situazione lavorativa ed economica in stallo, a causa della nostra negligenza."
          proprietà[Salute]="sul piano psicologico, in generale indica la mancanza di comunicazione, che porta all’isolamento e alla carenza di rapporti sociali verso le altre persone. Questo può sfociare anche in problemi di salute che dal piano fisico si spostano su quello psicologico."
          proprietà[Persone]="rapportata alle persone, indica in generale l’invidia, le persone che fanno qualcosa per mettere in cattiva luce noi, magari comportandosi da false amiche, che però non rivelano i propri segreti."

    elif arcano == "La Imperatrice":
       if senso == "dritto":
          proprietà[Dettagli]="Per comprendere i significati positivi della carta, bisogna ricordare la sua ispirazione mitologica. L’imperatrice rappresenta la dea greca Demetra, protettrice della Terra e dei suoi frutti, nonché dea della fertilità (sia della terra che delle persone).\nLa carta simboleggia quindi i cicli naturali, i frutti della terra e del lavoro, in generale la donna, la femminilità, la grazia, ma anche la bellezza e il lusso. Rappresenta inoltre l’intelligenza, la creatività, la cultura e l’energia che si pone nei lavori che si fanno.\nL’imperatrice è, in generale, la protettrice dei nuovi progetti o comunque delle novità. Indica una nuova nascita, quindi l’arrivo di una nuova vita, l’inizio di una relazione sia in fase di principio che in senso di legame che si salda, ovvero il matrimonio.\nRappresenta poi la Madre, il conforto, l’amore, la sicurezza, il prendersi cura di sé, la pace. Indica una situazione tranquilla, serena, circondata di persone reali, la presenza di una persona vicina.\nNell’accezione femminile può rappresentare una persona, chiaramente una donna, in cui poter riporre particolare fiducia: può essere una moglie, ma anche un’amica, una sorella; per i maschi può indicare anche la propensione a trovarsi bene, ai vari livelli, con il genere femminile.\nGli attributi della carta non solo legati al lato economico, ma sempre a quello emotivo e spirituale, in positivo; la sua presenza indica così qualcosa che si salda, qualcosa di positivo, anche una promozione lavorativa, raggiunta tuttavia per la nostra intelligenza e come conseguenza del nostro lavoro e non solo per il mero guadagno utilizzando tutti i mezzi a nostra disposizione."
          proprietà[Amore]="l’Imperatrice si riflette in generale nel rapporto di coppia e le conferisce stabilità. Può indicare un nuovo rapporto in fase iniziale, fondato sulla dolcezza, sulla fiducia e sulla realtà tra le due parti, e può anche indicare un fidanzamento, un matrimonio, una nascita o anche, più in generale, la nascita di un’amicizia sincera."
          proprietà[Lavoro_e_denaro]="rappresenta l’inizio delle cose, quindi può indicare una promozione, un nuovo lavoro, l’inizio positivo di un nuovo progetto, il superamento di un concorso, il conseguimento di un diploma alla fine degli studi. I significati economici sono tuttavia sempre indiretti e subordinati al lavoro costante."
          proprietà[Salute]="Sul piano della salute, l’Imperatice indica prosperità e fecondità, l’assenza di malattie, l’andare a frutto e quindi il miglioramento di terapie che abbiamo iniziato."
          proprietà[Persone]="indica una presenza femminile, una donna, generalmente giovane, leale e intelligente. Può rappresentare una persona che già conosciamo e fa parte della nostra vita, come fidanzata, moglie, madre, figlia, sorella o amica; generalmente, anche se non sempre, indica una persona giovane."
       else:
          proprietà[Dettagli]="I significati negativi della carta sono importanti, perché gli attributi vengono rovesciate, e le virtù dell’Imperatrice vengono esasperate.\nCosì l’amore materno diventa avidità, la bellezza vanità, la giovinezza immaturità, la superiorità presunzione.\nE’ un significato duro e decisamente poco piacevole, che indica una serie di virtù correlate, in generale, alla femminilità ma che si mostrano nella loro accezione più negativa. Relativamente alla fertilità e ai frutti del lavoro, invece, sta a significare la mancata capacità di portare a termine i lavori intrapresi, oppure di aver paura dei rapporti (paura di sposarsi, paura di accettare un figlio).\nIn generale, la carta indica un rifiuto della comprensione e mostra una durezza generale, che gli altri possono avere verso di noi oppure che noi possiamo avere verso gli altri; potrebbe indicare anche una sicurezza che è tuttavia solamente apparente, e non sincera.\nNelle relazioni, indica una predisposizione a considerare il materiale e, a volte, addirittura l’economico, senza vivere appieno la relazione di cui si fa parte.\nLa carta indica anche una mancanza di comunicazione, freddezza, tendenza al pensare ai propri scopi invece di dare agli altri, in una distorsione sia materiale che, soprattutto, egocentrica: si mette il sé al centro del mondo al contrario della Madre che dona tutto il suo amore agli altri.\nIn un’accezione ancora più esasperata e generica, può indicare anche la disonestà, il cercare il proprio tornaconto a scapito del prossimo. In senso generale tutti i significati si possono ricondurre alla mancanza dell’amore, e si sfruttano così i mezzi dell’amore apparente per perseguire le proprie finalità."
          proprietà[Amore]="C’è un problema di mancanza di comunicazione nella coppia, che porta a continui incomprensioni e litigi. L’amore non c’è e, se c’è, ricopre un ruolo secondario; se l’affetto non è compromesso c’è sempre la possibilità di recuperare, ma richiede un costante impegno da parte di entrambi i partner."
          proprietà[Lavoro_e_denaro]="l’imperatrice può significare in questo senso un problema al lavoro, che spesso però dipendono dagli errori della persona stessa e da un lavoro fatto male, in modo superficiale e senza il necessario approfondimento. Interessa tanto il lavoro quanto lo studio, per cui potrebbe avere significati negativi a causa della mancanza di impegno."
          proprietà[Salute]="sul piano della salute è legata in particolar modo al fallimento dei tentativi che stiamo facendo e al disagio, ad una persona che non ha particolare cura per sé stessa e che non cerca il meglio."
          proprietà[Persone]="indica una persona in generale disonesta, oppure superficiale, incapace (non volontariamente) si provare sentimenti. Una persona a cui bisogna fare attenzione nei rapporti, sia relazionali che lavorativi."

    elif arcano == "Lo Imperatore":
       if senso == "dritto":
          proprietà[Dettagli]="Il significato dell’imperatore è quello del potere materiale, della forza, della dominazione, dell’atto pratico. In senso positivo non è tuttavia inteso come tirannia, bensì nel potere che protegge i propri sudditi, che li difende, in qualche modo rappresentando l’amore paterno.\nI significati positivi riguardano tutto ciò che riguarda il materiale e l’atto pratico, l’energia, il desiderio, tutto ciò che è solido e che è destinato a durare nel corso del tempo.\nLa presenza dell’imperatore indica la capacità di superare le situazioni avverse con forza, fermezza e volontà, ma anche con l’esperienza necessaria per poterle affrontare perché le conseguenze siano positive al massimo. In generale, questa carta ha un significato positivo in tutte le situazioni in cui c’è bisogno di fare qualcosa, di muoversi materialmente e di affrontare materialmente (più che intellettualmente) delle situazioni.\nIl significato al positivo indica anche la solidità: radici solide di un rapporto, di un lavoro, dell’inizio di un progetto che avrà la possibilità di resistere anche ai traumi più violenti che possono riguardarlo. Questo viene inteso sia in senso materiale, cioè qualcosa da costruire, o un lavoro che deve essere iniziato (o che è già iniziato), ma anche in senso immateriale, legato ad esempio ad un rapporto affettivo, sia in amore che in amicizia, destinato a durare a lungo nel corso del tempo.\nAnche dal punto di vista della salute abbiamo solidità, e in questo senso l’imperatore indica un periodo felice, sano, forte, che riguarda sé stessi oppure le persone che circondano, come la famiglia."
          proprietà[Amore]="indica un rapporto solido, sia nel caso in cui questo stia per iniziare, sia nel caso si tratti di un rapporto già in atto. Anche se ci sono delle difficoltà, queste verranno affrontate nel modo corretto e superate, essenzialmente perché le radici sono solide. Può indicare anche la paternità e l’arrivo di una nuova vita, a migliorare l’armonia familiare."
          proprietà[Lavoro_e_denaro]="è una delle carte più importanti, perché in senso positivo indica che il progetto che stiamo per iniziare è destinato a durare a lungo, la posizione lavorativa a consolidarsi, e che acquisiremo sempre più importanti. Indica anche la predisposizione ad affrontare le difficoltà in modo fermo ma determinato, e la capacità di riuscire nel nostro intento."
          proprietà[Salute]="Sul piano della salute, l”imperatore indica un momento di salute difficile da scalfire, o in alternativa un periodo di resistenza alle ricadute, per le persone malate."
          proprietà[Persone]="l’imperatore indica una figura maschile, forte, determinata, piena di volontà e anche protettiva. Può essere una persona importante in ambito affettivo, come un padre o un nonno, ma anche un amico, oppure sul piano professionale."
       else:
          proprietà[Dettagli]="Contrariamente a quanto accade per altre carte dei tarocchi, il capovolgimento della carta non indica la perdita delle qualità dell’imperatore (quindi debolezza, incapacità di affrontare le situazioni o pigrizia); il potere della carta viene mantenuto, ma viene tuttavia distorto, con un esercizio esasperato di questo potere e dei privilegi, che può riguardare noi oppure un’altra persona.\nLe situazioni da affrontare saranno ostacolate non tanto da fattori esterni, ma interni alla persona: difficoltà di prendere una decisione o trarre decisioni sbagliate, ma più frequentemente un utilizzo sbagliato delle proprie risorse, ad esempio un eccessivo sfruttamento oppure una forza direzionata nel verso sbagliato, destinata a torcersi contro la stessa persona.\nLa motivazione nell’agire rimane, ma questa motivazione si porta avanti nel modo sbagliato: per esempio, cercando di far fruttare il proprio potere sulle altre persone (come i sottoposti), agendo in modo squilibrato, o semplicemente prendendo le cose con eccessiva determinazione facendo prevalere la forza di volontà sull’intelletto, con la fretta che porterà a decisioni sbagliate o, nel migliore dei casi, non ottimale.\nIndica anche una persona, più semplicemente testarda, che ha paura a chiedere aiuto, e continua per la sua strada nonostante le situazioni non siano favorevoli. Può indicare anche, semplicemente, una persona egoistica, che per ottenere la propria libertà priva quella degli altri.\nL’impulsività gioca un ruolo importante all’uscita di questa carta rovesciata, e questo causa un effetto imprevedibile e, con ogni probabilità, sbagliato, nelle scelte che stiamo per compiere."
          proprietà[Amore]="In amore, in generale l’imperatore rovesciato indica l’immaturità e l’incapacità di prendere una scelta forte, ma anche ponderata. Si tende a pensare troppo al momento o troppo a sé stessi, a prevalere con la propria personalità sul partner, e questo avrà conseguenze che in ogni caso non saranno positive. Indica anche il mancato controllo dei sentimenti, soprattutto di quelli negativi come la rabbia."
          proprietà[Lavoro_e_denaro]="dal punto di vista professionale non ci si discosta molto dal piano affettivo, con le decisioni che vengono prese in fretta, che non vengono adeguatamente considerate. Indica l’incapacità di programmare i propri lavori e di gestire con calma e fermezza le proprie responsabilità. Può indicare anche un abuso sui propri sottoposti, oppure l’essere abusati da parte di qualcuno che si trova in una situazione di superiorità rispetto a noi."
          proprietà[Salute]="sul piano della salute indica in generale un’incertezza, una logorazione che inizia dal piano psicologico per spostarsi su quello fisico. Può anche indicare decisioni o comportamenti sbagliati dal punto di vista della salute."
          proprietà[Persone]="indica una persona egoista, che tende a sfruttare il proprio potere, può indicare un avversario o un rivale. Può indicare un capo che rende la vita difficile ai propri pazienti."

    elif arcano == "Il Papa":
       if senso == "dritto":
          proprietà[Dettagli]="I significati positivi di questa carta riguardano l’equilibrio e la spiritualità, l’insegnamento corretto che arriva dalle altre carte del mazzo.\nIl papa rappresenta l’uomo saggio, che ha raggiunto una posizione di equilibrio, che è in grado di giudicare le persone e le situazioni, di prendere le distanze dai problemi più comuni e di sorridere grazie alla propria saggezza.\nIl papa indica quindi il non abbandonarsi alle emozioni agli eccessi, bensì la capacità di valutare con oggettività le situazioni. I contrasti di moralità, la condizione di chi ha davanti, le lotte, non lo interessano e anzi il suo scopo è proprio quello di consigliare correttamente per rimuovere le differenze, per appianare i contrasti, portando così nuovamente l’armonia.\nPuò indicare anche la presa di coscienza di fronte ad un problema, che non porta subito alla soluzione ma mette in condizione di trovarla, osservandolo da un’altro punto di vista.\nIndica anche la presenza di un’autorità benevola, indulgente, oppure l’improvvisa scomparsa di un problema che si manifestava da tempo, o di una questione che stava degenerando ma che ritrova un’improvviso equilibrio e la via della risoluzione. Indica la sicurezza nelle proprie ragioni, la bontà, la clemenza, la capacità di perdonare.\nImportante la rappresentazione dell’equilibrio, che può tradursi in una capacità dell’eloquenza, della diplomazia, della crescita mentale. E poi c’è la componente religiosa: l’attenzione al sacro, alla tradizione, alla preghiera, al perdono, al rispetto dei valori."
          proprietà[Amore]="la saggezza e la serenità indicano un rapporto di coppia felice, tranquillo, profondo, fedele e serio. Si tratta di un’unione felice, indica l’intesa non tanto materiale ma soprattutto mentale (culturale) e spirituale. Indica che c’è la massima fiducia tra i componenti della coppia."
          proprietà[Lavoro_e_denaro]="Indica in generale la diplomazia e la capacità di gestire al meglio le situazioni, anche quelle più complesse. Il papa rappresenta il culmine della propria gerarchia, e può indicare l’arrivo di una promozione ma anche il fatto che, pur non essendo giunti all’apice, la nostra persona gode di considerazione e le proprie scelte, così come i propri pensieri, sono importanti."
          proprietà[Salute]="Il Papa su questo piano indica il raggiungimento o il mantenimento della salute fisica e psichica. Nel caso di malattia in atto, la risoluzione della malattia o un periodo di miglioramento."
          proprietà[Persone]="il Papa indica in generale una persona vicina, dotata di equilibrio, un confessore, una persona su cui si può fare affidamento grazie alla sua comprensione oppure alla sua esperienza."
       else:
          proprietà[Dettagli]="I significati negativi legati al Papa possono essere interpretati da due opposti diversi. Da un lato, la fede diventa mancanza di fede con tutto ciò che ne consegue, mentre dall’altro la fede viene esasperata, portando ad un’eccessivo bigottismo, moralismo e nella chiusura mentale nei confronti delle altre persone.\nNel primo caso, quindi, si trova un rifiuto di tutte quelle che sono le virtù legate alla fede, al giudizio, alla diplomazia. Si tende ad essere rancorosi, difficili al perdono e si cerca in generale lo scontro, in modo diretto o anche indiretto: maldicenze, meschinità, utilizzo dell’eloquenza in modo negativo e utile solamente per un tornaconto personale, con lo scopo di danneggiare le altre persone.\nIndica litigi che non solo non si risolvono ma che tendiamo ad esasperare, a portare avanti con un proposito inadeguato (se non proprio cattivo), oppure indica la mancanza di aiuti e consigli da parte di persone che hanno capacità di giudizio.\nNel secondo caso, invece, ci troviamo davanti all’esasperazione delle virtù legate alla fede e alla spiritualità. Ci si chiude nella propria mentalità, nei propri valori, e non si riesce ad accettare chi è diverso da noi, non riusciamo a comprendere le altrui ragioni, non si perdona perché è corretto ma lo si fa, anche in questo caso, perché vediamo nel perdono un’opportunità, con una connotazione spiccatamente negativa.\nIl Papa al contrario indica la mancanza di volontà di mettersi in gioco, così come la difficoltà di esprimere un giudizio corretto ed equilibrato anche quando ne avremmo le capacità."
          proprietà[Amore]="Indica un rapporto apatico, in cui le persone non sono capaci di ricevere o di dare amore. Le persone che fanno parte del rapporto non si comprendono, e le incomprensioni hanno come conseguenza un’ulteriore incrinazione del rapporto stesso perché nessuna delle due parti cerca una conciliazione. Nei nuovi rapporti, indica una persona che non vive l’amore in doppio senso, ma che vuole solo ricevere senza dare."
          proprietà[Lavoro_e_denaro]="indica generalmente il blocco di una carriera, oppure blocchi emotivi, incapacità di superare gli esami, di appianare le controversie o di trovare un nuovo lavoro. Indica anche la mancanza di equilibrio, in generale, sul posto di lavoro."
          proprietà[Salute]="indica in generale le problematiche psicologiche, quelle non correlabili direttamente al piano fisico ma a problemi mentali, dall’ansia, alla paura eccessiva, agitazione e un’emotività eccessiva che ci danneggia."
          proprietà[Persone]="indica persone false e meschine, di cui non ci si rende conto immediatamente ma che cercano solo un tornaconto personale."

    elif arcano == "Il Carro":
       if senso == "dritto":
          proprietà[Dettagli]="Trattandosi di un arcano di trionfo, almeno quando compare diritto, imprime all’universo dei Tarocchi una spinta positiva. Maturato attraverso le scelte e le prove, il consultante sperimenta una nuova condizione di consapevolezza, stabilità emotiva, fiducia in se stesso, autocontrollo. Una nuova fase, attiva ed energica dell’esistenza, dunque, arricchita da progetti, conquiste, riuscita ottenuta grazie alle proprie capacità direttive e alla facoltà di persuadere facilmente eventuali collaboratori e subordinati.\nMoltissime e tutte entusiasmanti sono le promesse della carta diritta: trionfo sulle difficoltà, superamento di un periodo di incertezza, riconoscimenti, supremazia sui rivali, progresso, fortuna. La situazione presente, dinamica e in via di evoluzione, sia in senso materiale che morale, richiede decisione e fermezza\nIl consultante sta affrontando con coraggio le proprie mete, che vive entusiasticamente come sfide contro se stesso. Carta di espansione e di massima indipendenza, non esclude tuttavia qualche rischio, soprattutto quando la lotta per un giusto ideale è condotta a ogni costo, senza tenere conto delle reali condizioni esterne, con un certo gusto per il rischio e l’azzardo. Non mancheranno tuttavia gli aiuti insperati, protezioni, appoggi: un periodo di lotta e di esperienza, spesso solitaria, estremamente fecondo."
          proprietà[Amore]="La situazione affettiva evolve in favore del consultante. Il momento è propizio per cominciare a costruirsi un’esistenza a due, per il matrimonio, per una riconciliazione. Nella coppia sussiste un affetto tenero e sicuro nonostante un pizzico di prepotenza insita nel partner. Novità entusiasmanti e avventure pepate per chi è ancora alla ricerca dell’anima gemella."
          proprietà[Lavoro_e_denaro]="Una situazione professionale o sociale invidiabile. Successi, avanzamenti di carriera, ambizioni realizzate grazie alla grinta e al potere decisionale del consultante. Spostamenti, arrivi, viaggi fortunati a scopo professionale o scolastico. Studi che proseguono bene, con particolare riferimento agli esami universitari di filosofia, lingue, storia delle religioni. Coronamento della carriera scolastica, diploma, laurea. Occasioni favorevoli, colloqui di lavoro, corsi e stage da non lasciarsi sfuggire. Successi per gli sportivi, in particolare per chi pratica agonismo a livello professionale. Transazioni commerciali favorevoli, affari ben conclusi, associazioni fruttuose, espansione di imprese, contratti importanti. Particolarmente favorite le attività di import-export, le spedizioni, la navigazione."
          proprietà[Salute]="È sempre indice di una salute di ferro, nel pieno della vitalità e dell’equilibrio. Forma perfetta, longevità, superamento di qualsiasi problema fisico. Preziosi alleati da non sottovalutare sono lo sport e il buon umore, che influenzano positivamente anche il fisico."
          proprietà[Persone]="Uno straniero particolarmente benevolo nei confronti del consultante, un ambasciatore, un console, una personalità politica, un viaggiatore, uno sportivo, un esploratore, un militare, un predicatore, un religioso, un insegnante, un traduttore, un avvocato. Si tratta in ogni caso di una persona, più di frequente di sesso maschile e di età compresa fra i quaranta e i sessant’anni, molto sicura di sé, combattiva e idealista, dotata di talento, iniziativa e con buone possibilità di successo. Pertanto, può riferirsi al capo, a un padrone o, comunque, a un individuo che gode di una situazione sociale privilegiata, ma anche a un fratello maggiore, a un amico, al partner, al socio affidabile."
       else:
          proprietà[Dettagli]="Una carta così forte e dinamica non può che invertire o esasperare, se capovolta, tutti i suoi buoni auspici. La lotta permane sempre in primo piano, ma, mentre se la carta è diritta è sicuramente coronata da successo, se la carta è capovolta può avere esito incerto oppure implicare un grande dispendio energetico. Quando poi le carte vicine peggiorano con la loro negatività la situazione, la vittoria si tramuta in sconfitta, il successo in un progetto fallimentare e la strada percorsa a testa alta dal trionfatore si rivela una strada infida e pericolosa.\nNei casi migliori, senza arrivare all’insuccesso, può trattarsi di un momento di stasi o, talvolta, a causa della perdita di controllo, di una poco onorevole fuga dalle responsabilità. Quello che più di tutto crea problemi è la fiducia in se stessi, carente o eccessiva che conduce, nel primo caso, all’inconcludenza, alla debolezza, alla mancanza di coraggio e di chiarezza, fino ai limiti della confusione e del panico, nel secondo all’arroganza, all’ambizione sfrenata, all’uso di mezzi poco puliti pur di arrivare a ogni costo. Il consultante, mancando completamente di diplomazia e di tatto, non difende le proprie posizioni se non in maniera disordinata e spesso offensiva.\nTende, quindi, a sottovalutare le difficoltà e, soprattutto, i diritti altrui, comportandosi da dittatore, con crisi di collera, rigidità, litigi, ingiuste vendette, o, peggio, da parassita, da opportunista, pigro, limitato, disorganizzato, confuso e del tutto incapace di adeguarsi alla realtà e ai doveri, che anzi cerca di sfuggire eternamente. Da non escludere la presenza di ostacoli esterni e difficilmente sormontabili, contro i quali la volontà del consultante cozza invano, o la perdita di qualcosa che teneva già in pugno; un aiuto promesso potrà venire improvvisamente a mancare. È spesso la carta del cattivo governo, ingiusto e dittatoriale contro il quale è doveroso ribellarsi. Agitazioni sindacali, conflitti, querele."
          proprietà[Amore]="Segnala sempre una situazione di grossa insoddisfazione all’interno del rapporto, che può sfociare in una rottura. Responsabile ne è quasi sempre il temperamento troppo forte del consultante o del partner, causa di litigi, infelicità affettiva, rancori, vere e proprie fughe in avventure extraconiugali."
          proprietà[Lavoro_e_denaro]="Grossi guai professionali dovuti a errori o all’atteggiamento troppo bellicoso del consultante. Conflitti e invidie fra colleghi, intolleranza nei confronti delle direttive di superiori. Un viaggio di lavoro rischia di essere rinviato o di trasformarsi in un fiasco a causa di ritardi o incidenti. Tuttavia l’arcano non è sempre così distruttivo: in compagnia di carte positive, rispecchia semplicemente i timori del consultante riguardo a un colloquio, a un esame, a un viaggio o a un posto direttivo per cui non si ritiene all’altezza. Anche in questo caso il problema numero uno rimane sempre la sproporzione, in difetto o in eccesso. Segnala infatti grosse perdite commerciali, investimenti inadeguati alle proprie possibilità, debiti insoluti."
          proprietà[Salute]="Squilibrio, stanchezza, dispendio energetico superiore alle proprie possibilità, rischio di ferite, emorragie, incidenti, interventi chirurgici. I problemi riguardano le anche, le cosce, il fegato, il pancreas e spesso sono da imputare all’alimentazione squilibrata del consultante."
          proprietà[Persone]="Un uomo che tende a ostacolare, aggressivo, oppressivo, tirannico. In presenza di carte deboli un individuo frustrato, debole, represso."

    elif arcano == "Gli Amanti":
       if senso == "dritto":
          proprietà[Dettagli]="La carta della scelta, dell’esitazione di fronte a un bivio diviene, anche nel gioco, emblema di una situazione fluida, ancora da determinare. Il consultante si trova di fronte a una decisione importante, dal cui esito può dipendere tutta la sua esistenza futura o, almeno, un settore molto significativo di essa.\nSe l’Innamorato compare diritto o abbinato a lame fortemente positive, significa che si tratterà di una scelta libera, da compiere in tutta calma e senza pressioni esterne; una scelta che, in ogni caso, si rivelerà vincente.\nQuando, invece, le carte vicine appaiono problematiche, essa ti chiederà una certa cautela; a meno che non ci si affidi al sesto senso, alle irrinunciabili doti intuitive cui la carta fa sempre riferimento.\nNel suo significato venusiano di bellezza, armonia e affinità, può segnalare la tensione creativa che precede ogni opera d’arte o uno stato di particolare fecondità fisica e spirituale. Tuttavia, nonostante la didascalia, l’Innamorato, più che una carta d’amore, eccettuate particolari condizioni in cui le lame vicine lo confermano, è una carta d’attesa, di scelta affettiva, di rapporti, quindi, ancora in formazione, privi di implicazioni erotiche.\nIndica spesso un carattere altruista, molto attento ai problemi di amici e conoscenti, onesto, modesto, sincero, fiducioso. Non mancherà qualche conflitto, legato alla reale necessità di sottoporsi a una prova, vissuta tuttavia con serietà e grande senso di responsabilità. Aspirazioni, desideri esauditi, giovinezza, felicità assicurata."
          proprietà[Amore]="Incontro con l’anima gemella, inizio di una relazione importante e definitiva, destinata a sfociare nella convivenza o nel matrimonio. Il consultante sta vivendo una fase di innamoramento o, almeno, di infatuazione, contrassegnata da scelte e progetti che coinvolgono un’altra persona. Ma può anche trattarsi di una decisione tanto difficile quanto necessaria a mettere fine a uno stato di disordine sentimentale, a un dilemma, a una scelta fra due o più persone ugualmente simpatiche e affascinanti. L’arcano ricorda al consultante la necessità di rinnovare quotidianamente l’impegno affettivo preso, di non trascurare la persona amata, affinché l’unione possa mantenersi solida e armoniosa nel tempo. Dedizione, fedeltà, sentimenti ricambiati, amore, amicizia, solidarietà. Vicinanza di una persona cara, interesse per i problemi di un amico o di un parente. Matrimonio o fidanzamento in vista: non rimane che fissare la data."
          proprietà[Lavoro_e_denaro]="Arte, fantasia, buone idee da mettere in pratica. Un esame o un concorso da sostenere con ottime possibilità di riuscita e di successo. L’ambiente professionale o scolastico, cordiale e armonioso, potrà sostenere il consultante in un momento difficile. Si prospettano viaggi di lavoro, ottimi raccolti agricoli. Necessità di cercare alleanze utili sul piano commerciale. Una scelta di investimento che darà frutto in futuro Consigliati gli acquisti immobiliari e le proprietà terriere."
          proprietà[Salute]="Equilibrio psicofisico ristabilito grazie alla vicinanza di persone care; la dieta, soprattutto se vegetariana o macrobiotica, potrà contribuire in larga parte alla guarigione. Fertilità, funzioni riproduttive in piena attività. Sistema cardiocircolatorio perfettamente efficiente."
          proprietà[Persone]="Una persona volubile, indecisa ma, in fondo, buona e generosa, un artista, un collezionista d’arte, creativo e originale. Può indicare il consultante stesso durante la fase della “cotta” oppure un giovane innamorato di età inferiore ai trent’anni, un amico, un parente. Sul piano professionale si riferisce a un ragioniere, un geometra, un architetto, un ingegnere, un medico, un farmacista, un chimico, un infermiere, un’impiegata, un funzionario, un tecnico, un meccanico. Bambini, animali domestici."
       else:
          proprietà[Dettagli]="Quando l’arcano si presenta capovolto, il dubbio del giovane Ercole si trasforma in una scelta lacerante, non priva di contraddizioni e ripensamenti.\nLa cortigiana raffigurata sulla carta sembra, infatti, avere la meglio sulla virtù, persuadendo il consultante a percorrere la via sbagliata, costellata di facili tentazioni ma, in realtà, priva di sbocchi.\nCalunnie, insinuazioni, inganni, appesantiscono l’ambiente in cui vive e opera, rendendogli tutto più difficile. Lama di dualismo e di conflitto, l’Innamorato capovolto può segnalare un incontro pericoloso, turbamenti, desideri inappagati, promesse non mantenute.\nDubbi, esitazioni, incertezze e un’eccessiva instabilità emotiva portano a rimandare all’infinito una soluzione necessaria, perché tutta la libertà d’azione preconizzata dall’arcano diritto diviene qui sottomissione alla necessità e dipendenza dai fattori esterni.\nPrivato della sua dimensione spirituale, il sentimento diventa stucchevole, esclusivamente orientato all’appagamento fisico. La situazione vissuta dal consultante permane fluida e insoddisfacente, tanto da rivelarsi la causa di vere e proprie crisi di abbattimento, mancanza di entusiasmo, pessimismo esasperato.\nOstacoli, interferenze indesiderate, disordine, prove fallite o rinviate, esperienze da ripetere, opere incompiute e ancora lontane dalla conclusione."
          proprietà[Amore]="Un amore colpevole, tradimenti, sesso fine a se stesso, una decisione errata rischiano di incrinare un rapporto armonioso. I sentimenti risultano carenti o male espressi, viziati da una buona dose di egoismo, di disinteresse e di aridità. L’affettività del consultante viene messa a dura prova da un partner poco coinvolto oppure un po stanco. Dubbi, gelosie, intesa poco armonica, poco equilibrata e conflittuale, con la sola eccezione, forse, del piano erotico."
          proprietà[Lavoro_e_denaro]="Una società rischia di essere rovinata da fattori esterni, progetti avventati, collaboratori di cui è meglio non fidarsi. Bocciatura, esame fallito o rinviato a settembre. Una grossa delusione in campo artistico, opere non accettate o stroncate dalla critica. Una proposta da vagliare con cautela, inganni, affari in sospeso."
          proprietà[Salute]="Depressione, esaurimento, pericolo di malattia o di incidente. Il consultante è afflitto da tanti piccoli malanni che agiscono negativamente sul sistema nervoso e sull’umore. Sterilità, problemi al ventre, all’intestino, alle orecchie, ai reni e all’apparato genitale."
          proprietà[Persone]="Una persona inaffidabile, doppia, falsa. Un partner coinvolto solo superficialmente, interessato esclusivamente all’aspetto sessuale del rapporto."

    elif arcano == "La Giustizia":
       if senso == "dritto":
          proprietà[Dettagli]="Il significato generale di questa carta è facilmente intuibile, ed è legato alla giustizia. Intesa tuttavia non solo dal punto di vista della correttezza ma anche dell’armonia, dell’equilibrio, della fermezza di opinioni.\nIn generale, il significato quando la carta è dritta non è necessariamente positivo: la base è che ognuno raccoglie ciò che ha seminato, per cui se abbiamo seminato bene il risultato sarà positivo, se abbiamo seminato male dobbiamo temere delle conseguenze negative. La giustizia ci costringe a guardarci dentro, cercando di capire che cosa abbiamo fatto di giusto, in cosa abbiamo sbagliato, e prendere le decisioni corrette per proseguire.\nIndica anche il controllo, particolarmente importante nelle situazione difficili, e anche il tempo, generalmente il tempo che si impiegherà per raggiungere quello che vogliamo: la situazione si sistemerà, anche se il tempo da aspettare è molto.\nIl significato del controllo si rispecchia anche nei rapporti personali e in quelli di lavoro: la situazione tenderà a migliorare, ma solamente se sapremo rispettare l’armonia e l’equilibrio, superando gli ostacoli che verranno posti (anche in relazione alle altre carte che si presentano: più la giustizia esce in avanti nel mazzo, più saranno gli ostacoli e di conseguenza più si allungherà il tempo necessario per superare la difficoltà.\nLa giustizia indica anche tutto quello che riguarda la legge, le istituzioni e i rapporti giuridici con le altre persone."
          proprietà[Amore]="indica una situazione armonica ed equilibrata, ma solo se cercheremo di mantenere quella situazione e se ci impegneremo per raggiungere risultati positivi. Il significato riguarda sia i rapporti personali (amore), sia i rapporti familiari, con le persone che ci circondano. Poiché indica anche la legge, può rappresentare la regolarizzazione di un rapporto già iniziato, ad esempio un matrimonio ma anche un divorzio atteso da tempo."
          proprietà[Lavoro_e_denaro]="anche in questo caso, il significato principale riguarda l’impegno e i risultati legati a quanto di positivo metteremo nella nostra attività professionale. I successi arriveranno, ma in modo proporzionale all’impegno che abbiamo messo all’interno. Sul piano legale, riguarda tutte le questioni lavorative collegate alla legge e alle istituzioni."
          proprietà[Salute]="Per la salute, riguarda in generale un miglioramento e un mantenimento, che tuttavia richiede tempo e può essere atteso anche molto a lungo."
          proprietà[Persone]="la giustizia indica una persona in generale razionale, equa e severa; può indicare un collaboratore, una moglie, un parente e in generale una persona a noi vicina."
       else:
          proprietà[Dettagli]="La Giustizia al contrario continua ad indicare la legge, seppur i risultati non sono quelli sperati. Anche in questo caso la giustizia rimane, quindi non viene a mancare, ma è una giustizia in generale avversa, che anche se può portare ad un lieto fine ha delle complicazioni, può indicare iniquità, conseguenze positive ma che non vanno come speriamo, ostacoli.\nPuò indicare che per ristabilire l’equilibrio ci saranno dei litigi, che ci saranno iniquità commesse solitamente dagli altri e anche se noi ci troviamo dalla parte del giusto la situazione non sarà, in generale, positiva per noi.\nFrequenti saranno poi i ritardi (si ricollega al tempo), i contrattempi, la lentezza e, più in generale, l’incertezza, che andrà avanti fin quando non arriveremo alla fine del percorso. Può indicare anche la mancanza di responsabilità, la mancanza di organizzazione, di razionalità.\nIn certi casi indica anche l’eccesso di giudizio, un eccessivo zelo nell’applicare la giustizia o anche dei giudizi morali troppo rigidi, che possono mettere in difficoltà gli altri per quanto la giustizia rimanga, nel complesso.\nSul piano personale, può indicare la mancanza di giudizio su sé stessi, ma anche sulle persone che ci circondano, oppure la mancanza di fiducia verso le altre persone.\nRiguardo alla legge, può indicare le complicazioni subite nelle questioni legali, ma anche l’arrivo di problemi di natura legale inaspettate, che ci logoreranno anche molto a lungo.\nIn generale, quindi, ci aspetta una condizione difficile e piena di ostacoli, per quanto la “bussola” della giustizia continuerà ad essere importante nelle diverse situazioni."
          proprietà[Amore]="Nelle relazioni, in generale indica una mancanza di armonia nella coppia, che può arrivare ad una separazione legale o a un divorzio. Nel matrimonio, può indicare una difficoltà di contrarlo, ostacoli ad un amore già presente o ad uno che deve ancora iniziare, come un appuntamento mancato."
          proprietà[Lavoro_e_denaro]="sul piano professionale, può indicare che qualcosa non sta andando nel verso giusto, o che riuscirà ad andare ma solo dopo aver affrontato diverse difficoltà. Se abbiamo un progetto o un obiettivo dovremo lavorare ancora a lungo, affrontando diversi tipi di ostacoli. Potrebbe indicare anche delle scorrettezze da parte delle persone che ci circondano, in particolare dai colleghi di lavoro che cercano di convertire la giustizia ai loro scopi."
          proprietà[Salute]="dal punto di vista della salute, anche in questo caso indica la presenza di ostacoli da superare, difficoltà nel raggiungimento di un obiettivo, ricadute in una malattia o guarigione che stenta ad arrivare."
          proprietà[Persone]="la Giustizia capovolta indica persone timide, incapaci di prendere iniziative o che non sono determinate nel raggiungere i propri obiettivi."

    elif arcano == "Lo Eremita":
       if senso == "dritto":
          proprietà[Dettagli]="Arcano di movimento, benché si tratti di un movimento lento, si riferisce a tutto ciò che è destinato a un’evoluzione poco manifesta ma profonda, segreta, come la gestazione invernale del seme nella terra. Rappresenta, quindi, il solido, il concreto, il tempo, giudice supremo di tutte le cose, il rispetto per il passato e per la tradizione. Sulle orme lente e sicure del monaco, alla ricerca di se stesso e della via dello spirito, simboleggia la prudenza, la discrezione, la riservatezza, la moderazione, la pazienza, la costanza, il senso del dovere, tutte doti meravigliose anche se non brillanti.\nÈ, dunque, l’arcano della saggezza, del discernimento, della concentrazione, della serenità, della metodica ricerca della verità: una giusta ambizione, soprattutto se rivolta ai piani della conoscenza esoterica, l’ascesi, il silenzio. Quando nel gioco esce questa carta, probabilmente la situazione esistenziale del consultante non è entusiasmante. Si sente stanco, demotivato, provato dagli ostacoli, ma le forze sottili, che sono dalla sua parte, lo invitano a resistere e a non abbandonare l’opera iniziata. La condizione ideale è l’isolamento, un momento di solitudine e di ripiegamento su se stesso, magari suggerito da una delusione subita: meglio coltivare la fede in sé, piuttosto che negli altri.\nLa figura dell’Eremita diritto è sempre positiva; assicura buoni consigli, parole sagge e sincere, chiarimenti preziosi per il consultante, segreti svelati a chi ne è degno. Grazie a una protezione invisibile, ogni tentativo malvagio a danno del consultante sarà sventato. Tutte le iniziative avranno sviluppo lento ma esito positivo, perché la via intrapresa è senz’altro quella giusta. Nulla da temere, quindi, da una temporanea battuta d’arresto, comunque gravida di futuri mutamenti. Ottime capacità latenti, fecondità spirituale, doti extrasensoriali e telepatiche."
          proprietà[Amore]="Un amore puro, profondo e disinteressato, ma fondato più sulla comunanza spirituale che sull’intesa erotica. Il rapporto è solido e destinato a durare nel tempo.Da non escludere un periodo di solitudine temporanea, utile a veder chiaro in se stessi circa le proprie intenzioni verso il partner. La scelta che si sta per compiere durerà per sempre e va meditata con cura."
          proprietà[Lavoro_e_denaro]="I risultati, non immediati ma positivi, invitano a perseverare sia nello studio che nel lavoro, senza peraltro avanzare richieste azzardate. Ricerche, compilazioni, opere a lunga scadenza, studi matematici o archeologici, interessi profondi da sviluppare riguardo alla politica, la medicina, la biologia, la filosofia. Un momento di economia e di frugalità necessaria in vista del futuro. Investimenti sicuri e ben meditati, risparmi, incasso della liquidazione o degli arretrati della pensione. Consigliato l’acquisto di titoli di stato, azioni minerarie, terreni, immobili da ristrutturare."
          proprietà[Salute]="Sebbene le energie psicofisiche non siano al massimo, corpo e mente permangono in equilibrio. Evitare di abusare delle proprie forze e aiutarsi, per quanto possibile, con le medicine alternative. Longevità assicurata."
          proprietà[Persone]="L’Eremita raffigura sempre una persona anziana, o almeno spiritualmente matura, in grado di risolvere un grosso problema del consultante. Può trattarsi di un maestro spirituale, per esempio un sacerdote, un confessore, di una guida, saggia e illuminata, di un amico fedele, di un socio paziente e collaborativo, di un ente finanziatore per una giusta causa. Ma più di frequente è il padre, il nonno, un parente anziano, un antenato. Fra i professionisti può riferirsi a un medico, un erborista, un terapeuta alternativo, uno psicoanalista, uno psichiatra, un ostetrico, uno scienziato, un politico, un archeologo, un archivista, un ingegnere minerario."
       else:
          proprietà[Dettagli]="Quando si presenta capovolta o abbinata a lame fortemente negative, ecco che la carta agisce nel senso della perdita, del regresso e il processo evolutivo dell’Eremita si arresta in un ristagno sterile e frustrante. Allora la lentezza diviene inerzia, il ritardo non porta più frutti ma appesantisce ulteriormente una situazione già compromessa e qualsiasi realizzazione pratica in cui si sperava risulta annullata.\nPuò trattarsi di un eccesso di spiritualizzazione che conduce a un distacco innaturale dalla materia di cui, in quanto uomini, facciamo comunque parte, oppure della paura della realtà e del confronto con essa.\nSta di fatto che, quando la riflessione è portata all’estremo e la prudenza è esagerata, il consultante finisce col precludersi da sé la via del successo: il conservatorismo, la rigidità, l’incapacità di accettare i cambiamenti, la mancanza di spontaneità e di slancio si rivelano allora altrettanto fallimentari dell’azione sciocca, prematura o imprudente.\nNumerosi gli ostacoli, difficilmente superabili, se non con costanza, metodo e una pazienza sovrumana, mentre i blocchi, la cristallizzazione, la regressione sono all’ordine del giorno. Il consultante è timido, timoroso, diffidente; rifugge il contatto con gli altri esseri, preferisce compiacersi del proprio sapere, narcisisticamente rinchiuso nella sua torre d’avorio.\nTalvolta però la sua chiusura non è dettata dalla superbia o dalla misantropia, quanto piuttosto dalla tristezza, dal pessimismo, dalla freddezza, dall’indifferenza che lo rendono solo e vecchio prima del tempo. Molti dubbi, confusione mentale, mancanza di chiarezza e di direttive da seguire.\nConsigli errati, segreti divulgati, fiducia mal riposta, conflitti interiori, giudizi errati riguardo alla propria situazione e ai propri affari. Da tenere sotto controllo la tendenza all’avarizia, all’egoismo, all’ostinazione, alla malvagità, all’ipocrisia, alla calunnia, alla pigrizia. Persecuzioni, dissensi, pericoli, fatalità, sfortuna generalizzata e purtroppo meritata."
          proprietà[Amore]="La paura del coinvolgimento e delle responsabilità che comporta l’amore precludono al consultante, o alla persona indicata dal gioco, l’esperienza del matrimonio: celibato, freddezza, isolamento, abbandono, vedovanza, dissensi familiari, disarmonia e ristagno nella coppia, riluttanza a manifestare i propri sentimenti."
          proprietà[Lavoro_e_denaro]="Il consultante è costretto a professioni inconsuete o sgradevoli; lavoro pesante e mal pagato, studi che proseguono a rilento, esami rinviati per paura di esporsi, preparazione insufficiente, troppo profonda su certi punti, carente in altri. Perdite consistenti di denaro, affari mal condotti, risparmi sfumati, grossi problemi economici, situazione finanziaria preoccupante."
          proprietà[Salute]="Malattie croniche o a lento decorso, raramente gravi ma molto fastidiose. Reumatismi, artrosi, fratture, calcoli. Patologie delle ossa, dei denti, della pelle e delle orecchie, dolori ai piedi, distorsioni delle caviglie. Insonnia, depressione, invecchiamento precoce. Preceduto e seguito da carte molto negative, l’Eremita può far temere una malattia mentale."
          proprietà[Persone]="Una persona che rifiuta il proprio aiuto o che tenta di nuocere al consultante. Un vecchio solitario che non vuole dividere niente con gli altri, un abitudinario nemico dei cambiamenti. Si tratta in genere di un individuo avaro, pessimista, freddo, ipocrita, cattivo d’animo."

    elif arcano == "La Ruota":
       if senso == "dritto":
          proprietà[Dettagli]="Il significato della carta quando al positivo, ossia quando dritta, indica la fase ascendente della ruota e, in generale, la sorte positiva. Una sorte che, tuttavia, deve essere colta nel più breve tempo possibile, nel momento propizio, perché attendere troppo potrebbe provocare una ricaduta e quindi la perdita della possibilità.\nIn generale si prospettano degli avvenimenti favorevoli, fortune inaspettate, incontri positivi, ma anche un riequilibrio di una condizione negativa che stiamo vivendo. Queste circostanze potranno essere sfruttate al meglio se si utilizzano correttamente le proprie energie, mentre se le sprecheremo la ruota continuerà il suo corso, e le circostanze positive tenderanno a scomparire.\nLa ruota indica, però, non un destino già scritto, ma il fatto che siamo svincolati dall’accadere degli eventi perché abbiamo la possibilità di emergere, di essere padroni del proprio destino e di far variare il flusso delle cose a nostro favore. Indica la crescita, l’innalzamento, l’elevazione.\nLa ruota al positivo indica che è giunto il momento di raccogliere le proprie energie per affrontare le situazioni in modo lucido che porteranno, con ottime possibilità, alla buona riuscita di quello che abbiamo iniziato a fare.\nSe desideriamo qualcosa, è il momento giusto per averlo o cercare di ottenerlo, viste le ottime probabilità di riuscita nel nostro intento."
          proprietà[Amore]="indica la buona sorte, in senso generale, nelle relazioni. Può significare l’incontro della nostra vita per chi non ha un compagno o una compagna, oppure un matrimonio per una coppia fidanzata o ancora la nascita di un figlio; il momento è quello giusto. Da entrambi i partner c’è volontà di perseguire quel passo, e non potrebbe esistere momento migliore, per cui questo va colto quanto prima, pena la fine del momento propizio."
          proprietà[Lavoro_e_denaro]="è forse l’ambito più importante legato alla ruota. Si prospetta una promozione lavorativa, l’andare a frutto di qualcosa su cui stavamo lavorando da tempo (per il quale, però, non avevamo ancora visto dei risultati. Possiamo avere una fortuna inaspettata, un evento positivo che deve essere colto e sfruttato al massimo, un avanzamento nella propria carriera o un aumento delle proprie produzioni."
          proprietà[Salute]="Dal punto di vista della salute si prospetta un momento fortunato o un improvviso e inaspettato miglioramento di una condizione negativa in atto. E’ il momento migliore per fare qualcosa che i problemi di salute ci impedivano di fare in passato."
          proprietà[Persone]="non indica una persona ben precisa, ma chiunque ci possa aiutare inaspettatamente. Può rappresentare una persona che da un buon consiglio, una nuova amicizia, un benefattore e più in generale qualcuno che ci aiuterà in modo inatteso."
       else:
          proprietà[Dettagli]="La ruota al negativo indica, in generale, il contrario di quanto mostrato dalla ruota in positivo. Se il positivo era la fase crescente della fortuna, quindi indicava il momento propizio, la ruota al contrario indica la fase calante, che porta quindi ad un momento poco propizio dal punto di vista della fortuna.\nIndica quindi la presenza di ostacoli all’orizzonte che, nonostante le nostre volontà, non porteranno al risultato sperato; in generale, indica che non è il caso in questo momento di dedicarsi alle nuove imprese, perché saranno destinate a fallire, o quantomeno ad essere fortemente ostacolate.\nIl significato negativo può avere vari gradi: può indicare un peggioramento della situazione attuale, ma può anche, più lievemente, significare un momento di stasi, in cui le cose non migliorano ma in cui fortunatamente non abbiamo un peggioramento.\nI significati possono essere anche intesi in senso più ampio, cioè nel fatto che le nostre energie sono state utilizzate male: ad esempio, abbiamo iniziato a lavorare su un progetto sbagliato, abbiamo intrapreso una relazione che non porterà da nessuna parte, o in generale abbiamo preso una direzione che non è quella corretta. Nel complesso, quindi, un modo per indicare che qualcosa non va, e che dovremo rivedere le nostre scelte o le nostre aspettative."
          proprietà[Amore]="Sul piano relazionale può indicare la crisi di coppia, ma anche una scelta difficile da affrontare (per esempio, il trasferimento a causa del lavoro da parte di uno dei partner). Può indicare difficoltà anche non da parte nostra ma da parte del partner, che presumibilmente si ripercuoteranno sulle scelte che dobbiamo prendere noi in prima persona."
          proprietà[Lavoro_e_denaro]="anche sul piano del lavoro si prospetta o una stasi oppure un vero e proprio fallimento, generalmente però non dipendente dalla nostra volontà e sul quale le nostre energie potranno fare poco, non potremo riuscire ad invertire il corso delle cose nonostante i tentativi. Indica anche la precarietà, un declino della carriera, una promozione inaspettata che non arriva. Molto importante la prudenza in qualunque tipo di scelta, perché le condizioni non sono in generale positive."
          proprietà[Salute]="sulla salute, la ruota al contrario indica un momento sfavorevole. Malattie in arrivo, oppure ricadute di una malattia che abbiamo già; può indicare anche problemi che non ci riguardano direttamente ma riguardano le persone a noi vicine."
          proprietà[Persone]="indica persone instabili, lunatiche, le cui decisioni non sono effettive e che hanno la tendenza a cambiare idea, con conseguenze anche importanti sulle nostre scelte."

    elif arcano == "La Forza":
       if senso == "dritto":
          proprietà[Dettagli]="Il significato positivo della carta riguarda, in generale, la forza di volontà, che è in grado di dominare gli eventi.\nLa forza permette di superare qualunque ostacolo (compreso il leone), e soprattutto è un’energia interiore che permette anche di superare la forza bruta, quella fisica. Indica la lotta necessaria per ottenere quello che vogliamo, il recuperare tutte le risorse che ci appartengono per avere a disposizione quello di cui abbiamo necessità.\nDa notare che la forza non deve essere intesa solamente in senso stretto, bensì può indicare anche la forza di volontà che permette di non cedere alla rabbia quindi simboleggiare la disciplina, l’autocontrollo, il “pugno di ferro” necessario per affrontare specifiche situazioni in cui, più che combattere, bisogna riuscire a non piegarsi e a resistere.\nLa carta indica che grazie alla forza interiore si riesce ad ottenere quello che vogliamo, su tutti gli aspetti della nostra vita; le nostre aspettative tenderanno ad esaudirsi, purché lottiamo abbastanza per ottenerle.\nIndica che è il momento di lottare, di cercare di ottenere, di non demordere anche se si presentano davanti delle situazioni difficili, perché abbiamo la forza necessaria per affrontarle e per superarle."
          proprietà[Amore]="nelle relazioni, indica in generale la passione che ci permette di ottenere quello che vogliamo. Può essere la conquista di un nuovo partner, ma anche un fidanzamento, un matrimonio che magari è osteggiato da qualcuno o che non convince il proprio partner. Indica anche, in senso più largo, la sessualità e l’appagamento che me può derivare."
          proprietà[Lavoro_e_denaro]="anche sul piano professionale i significati positivi della forza sono importanti, perché permettono di ottenere quello che stiamo cercando; il lavoro sarà faticoso, sarà duro, ma permetterà di ottenere i risultati che vogliamo, perché abbiamo le capacità di ottenerli. Sarà necessario impegnarsi al massimo e non lasciare niente al caso, ma i nostri sforzi saranno ricompensati con i risultati."
          proprietà[Salute]="Dal punto di vista della salute, indica la forza interiore che ci permette di affrontare qualsiasi difficoltà. Se siamo sani riusciremo a rompere i propri limiti, ed iniziare attività nuove che condurranno ad un maggior benessere fisico o psicologico; quando la salute manca, invece, indica la capacità di affrontare le difficoltà e anche di vincerle, ottenendo così un miglioramento della qualità della propria vita. Le speranze non sono perdute, possiamo lottare per una condizione migliore."
          proprietà[Persone]="indica in generale una persona molto intraprendente, può essere giovane e dotata di molta forza interiore, come un adolescente oppure un giovane (magari un figlio). Può indicare anche una persona molto creativa."
       else:
          proprietà[Dettagli]="I significati negativi della forza sono due, e sono in un certo senso opposti tra loro, per risultati contrastanti che dovranno essere valutati a seconda della situazione.\nDa un lato la forza al contrario può indicare la mancanza di forza, quindi la debolezza, l’insicurezza, la mancata capacità di concludere quello che abbiamo iniziato.\nDall’altro lato indica invece che la forza c’è, ma che è utilizzata male, in eccesso, portando quindi a violenza (non solo fisica, ma anche psicologica), e poi alla perdita di controllo, agli attacchi di rabbia, al cedere agli istinti che possono avere conseguenze negative.\nL’influenza nella nostra vita può riguardare molteplici aspetti, che sono però sempre accomunati dall’errore: l’errore di non aver utilizzato la forza o di averla utilizzata male. E’ importante comprendere le singole situazioni, e chiedersi se e come stiamo utilizzando la nostra forza, se la direzione in cui cerchiamo di “spingere” gli eventi sia quella giusta o se sia quella sbagliata, se sia il caso di fare un passo indietro.\nAttenzione alla propria posizione, perché l’utilizzo sbagliato delle nostre energie porterà gli altri a vederci in modo diverso da come vorremmo, e questo può avere conseguenze negative sulle relazioni di ogni tipo."
          proprietà[Amore]="Nelle relazioni, la Forza al contrario può indicare sia un rapporto egoistico, concentrato principalmente sul proprio piacere anziché sull’armonia della coppia; può indicare anche un abuso da parte di uno dei partner. Per l’altro significato, poi, si può intendere come la mancanza di volontà in un rapporto, il non lottare abbastanza affinché questo possa procedere nel migliore dei modi. Le nostre azioni possono inoltre impedire l’avvicinamento di un partner."
          proprietà[Lavoro_e_denaro]="sul piano professionale è possibile intraprendere percorsi sbagliati, lottare per qualcosa per cui non otterremo risultati o, al contrario, mancare delle occasioni importanti perché non abbiamo dato tutti noi stessi. La carta è importante anche per un altro aspetto, il rapporto che abbiamo con i colleghi di lavoro: indica infatti che questi non sono ottimali, e ciò potrebbe avere delle ripercussioni sulla nostra vita lavorativa."
          proprietà[Salute]="dal punto di vista della salute indica in generale la debolezza, da intendersi con l’incapacità di affrontare le situazioni (condizioni negative di salute nostre o di chi ci sta vicino). Potrebbe significare anche che gli sforzi che abbiamo fatto sono controproducenti."
          proprietà[Persone]="indica persone facili all’ira, persone con cui bisognerà lottare e misurarsi, persone che usano la loro forza per prevalere sugli altri, persone crudeli."

    elif arcano == "Lo Appeso":
       if senso == "dritto":
          proprietà[Dettagli]="L’impiccagione, ovvero l’inversione di prospettive e di valori, conferisce alla personalità una nuova morbidezza, lontana dalla rigidità degli schemi e delle convenzioni. Forse più facile da vivere capovolto che diritto, verso in cui è più drastico, l’arcano vuole essere un invito alla flessibilità, alla ricettività, alla capacità di adattamento.\nIl consultante, volontariamente o no, ha a disposizione tutto il tempo che desidera per rivedere situazioni e rinviare scelte e progetti. Non è tempo d’azione ma d’attesa e di prudenza. Qualsiasi ritardo, qualsiasi ostacolo hanno la loro ragione nascosta e devono essere interpretati come un avviso provvidenziale, un segno del cielo. Non resta che accettare il destino, compresi i blocchi e le sconfitte, e sottomettersi almeno temporaneamente al corso degli eventi, senza tentare di cambiarlo.\nÈ un arcano di fede e di dedizione. Tutto deve essere disinteressatamente sacrificato a una persona o a una causa, senza aspettarsi ricompense immediate. Si tratta infatti di una prova necessaria, un passaggio obbligato che prelude a un miglioramento di là da venire. Ma se un beneficio a lungo termine o perfino una completa rigenerazione sono abbastanza probabili in ambito affettivo e spirituale, non c’è altrettanto da sperare per quanto riguarda questioni materiali, come il denaro o il successo, sempre subordinati, in questa carta, ai valori dell’anima.\nLa scelta migliore, che il consultante potrebbe compiere, è cambiare tattica, desideri, prospettive. Ma a differenza della trasformazione auspicata dalla Ruota e dalla Forza, rapida e improvvisa, si tratterà qui di una trasformazione lenta, più interiore che esteriore. La situazione attuale è comunque destinata a capovolgersi completamente, a subire mutamenti radicali e svolte decisive, negative solo in apparenza.\nIn presenza di arcani molto forti e realizzativi, può annunciare un risanamento quasi miracoloso, un successo reso possibile grazie all’intervento di fattori esterni, un evento straordinario, un ideale raggiunto dopo un lungo travaglio, una liberazione raggiunta attraverso il sacrificio. E ancora una missione, un insegnamento, un castigo meritato e ricco di frutti per il futuro, una prova che arricchisce. Una stasi necessaria, un periodo di attesa tra due eventi particolarmente significativi, che può implicare rassegnazione e rinuncia.\nUn prezzo da pagare, uno sforzo da compiere, un dovere a cui assoggettarsi, un progetto ancora confuso, nebuloso, che richiede basi solide su cui occorre lavorare ancora. Non mancheranno, del resto, ispirazioni geniali di origine spirituale, interventi a distanza, medianità, telepatia, azioni occulte. Misticismo, meditazione, introspezione, guarigioni spirituali, pensieri ed emozioni superiori. Una scelta di vita alternativa, al di fuori della competizione e del consumismo. Rilettura del passato, una nuova e diversa comprensione delle cose. Sul piano meteorologico annuncia nebbie e foschie."
          proprietà[Amore]="Un amore segreto, romantico, interiorizzato e magari inizialmente non corrisposto, un sentimento platonico, che non lascia spazio a esperienze fisiche. L’unione a cui il consultante pensa si rivelerà duratura e fedele perché costruita su una paziente attesa. Da non escludere una temporanea separazione dal partner in vista di un felice futuro insieme. L’abbandono di una persona cara può servire a far riflettere e maturare."
          proprietà[Lavoro_e_denaro]="Il successo si costruisce a piccoli passi, con un lavoro coscienzioso e disinteressato. Studi orientati sulla filosofia, la religione, la medicina, la psichiatria. Fotografia, musica, arte. Professioni assistenziali (medico, infermiere, assistente sociale) o legate all’acqua (idraulica, pesca, commercio di liquidi). Affari discreti ma non eclatanti, un moderato aumento di stipendio."
          proprietà[Salute]="Guarigione spirituale, rigenerazione, rinnovamento, miglioramenti e dimissione dall’ospedale."
          proprietà[Persone]="Una persona portata all’altruismo e al sacrificio, un idealista, un medico, un filosofo, un sacerdote, un genio, un artista, un musicista, un guaritore, un occultista, un incompreso. Naviganti, marinai, armatori, pescivendoli, bagnini, infermieri, psichiatri, fotografi, guardie, vigili del fuoco, detective. Persone o animali fedeli."
       else:
          proprietà[Dettagli]="Quando l’arcano compare rovescio o quando occupa una posizione sfavorevole all’interno del gioco, la situazione esistenziale del consultante si prospetta particolarmente difficile, contrassegnata da preoccupazioni, rimorsi, occasioni perdute. Attanagliato da una serie infinita di dubbi, sommerso da un mare di incertezza, si sente incapace di decidere e di volere e finisce con l’abbandonarsi all’unica strada che gli appare possibile: quella dell’inazione e della rinuncia.\nMolteplici sono in questo caso i rischi, dalla perdita di contatto con la realtà, dall’illusione all’utopia, all’apatia, all’indifferenza fino alle più gravi forme depressive, alle manie di persecuzione, all’autodistruzione masochistica, al rifiuto di confrontarsi con i problemi, alla fuga dal quotidiano attraverso l’alcol e la droga. E ancora, atteggiamenti di autoindulgenza, vittimismo, opportunismo, errori d’ogni sorta, credulità eccessiva, superstizione.\nAnnuncia delusioni, noie, affaticamento, amarezza su tutti i fronti, un sacrificio inutile o eccessivo, prove dolorose vissute male, senza riuscire a trame un insegnamento. Una perdita inevitabile, un distacco, un abbandono, una situazione di solitudine e sconfitta. I cattivi presentimenti del consultante, purtroppo fondati, sfoceranno in azioni ostacolate e notizie negative di lutto o malattia. I suoi progetti poco solidi e perciò irrealizzabili, i desideri generosi ma sterili e spesso causa di complicazioni, devono essere rivisti. Il problema, in questo caso, sta nell’incapacità di esaminare obiettivamente la situazione e riconoscere le proprie colpe.\nPer quanto giunto a un punto morto dell’esistenza, il consultante rifiuta di mettersi in discussione e accettare le necessarie responsabilità. Schiavo del dovere o delle passioni, dell’egoismo o di una generosità smodata, che lo induce a dilapidare somme considerevoli, non riesce a trovare il giusto mezzo né ad attuare l’irrinunciabile cambiamento. L’arcano è spesso indice di menzogna, inganni, intrighi, una situazione di caos e di anarchia, sia sul piano personale che politico, e inoltre di odi, persecuzione, razzismo."
          proprietà[Amore]="Un amore non corrisposto, fine di un rapporto, separazione, delusione, sconfitta. Il consultante, benché li desideri, non è portato ai legami impegnativi, alla famiglia, al matrimonio. Qualche volta un progetto sentimentale si realizza per poi rivelarsi, col tempo, poco soddisfacente. Da non escludere un tradimento o un legame con una persona già impegnata."
          proprietà[Lavoro_e_denaro]="Una situazione o un ambiente professionale insostenibile, bisogno di cambiare. Licenziamento, mancanza di lavoro e appoggi, stress. Studi portati avanti malvolentieri per mancanza di motivazioni. Perdite, affari sfumati a causa di una truffa, ristrettezze economiche, necessità di ridurre al minimo le spese."
          proprietà[Salute]="Un malore, un incidente, un’intossicazione. Crollo fisico, intervento chirurgico, anestesia, aborto. Sul piano psichico, il più compromesso, tossicodipendenza, depressione, ansia, impotenza, tendenze suicide. Sul piano fisico, tubercolosi, ulcera, poliomielite, infezioni. Patologie dell’intestino, del rene, della vescica e dei piedi. Dolori articolari, reumatismi, ritenzione idrica, cellulite."
          proprietà[Persone]="Nemici più o meno occulti. Una persona troppo sognatrice, introversa, inconcludente, timida. Un emarginato, un tossicodipendente, un falso profeta, mistificatore e fanatico. Un cleptomane, una persona afflitta da turbe mentali."

    elif arcano == "La Morte":
       if senso == "dritto":
          proprietà[Dettagli]="Nonostante quanto potremmo essere propensi a pensare, il significato al positivo della Morte è veramente positivo. Indica infatti la fine di qualcosa, la possibilità di lasciarsi qualcosa alle spalle senza nessun tipo di rimorso: quello è finito, ma inevitabilmente qualcos’altro prenderà il suo posto.\nLa fine generalmente è qualcosa che c’è già stato, e può essere legato in senso letterale alla scomparsa di un conoscente ma anche alla fine di un rapporto interpersonale, oppure lavorativo, qualcosa che ormai si è concluso. Più difficilmente può indicare qualcosa che sta per finire, ma in generale sappiamo che quella è ormai una strada che non vale più la pena di percorrere.\nTuttavia, la perdita non è indolore e, anzi, è abbastanza dolorosa, tanto che può essere necessario modificare la propria vita, metabolizzare il lutto, per poterla accettare. La fine di qualcosa indica l’inizio di qualcosa di nuovo ma anche una trasformazione che dobbiamo trovare in noi stessi, un’evoluzione della personalità, un passaggio in senso positivo dalla vecchia situazione a quella che stiamo per iniziare.\nE’ sempre importante focalizzarsi sulla novità, sulla necessità di intraprendere il nuovo percorso, un nuovo lavoro, una nuova relazione: ciò che è passato è ormai alle spalle, e non dobbiamo più preoccuparcene."
          proprietà[Amore]="indica un cambiamento forte, qualcosa che “rompe gli equilibri”. La cosa più comune è la fine della relazione, la rottura, che è tuttavia benefica per i due singoli partner; in altre situazioni può indicare la necessità di rivedere i rapporti di coppia, un chiarimento che cambia radicalmente la situazione."
          proprietà[Lavoro_e_denaro]="in modo simile alle relazioni, indica un grande cambiamento; può essere il termine di un lavoro e l’inizio di un’altro, un cambiamento di casa, il termine di un percorso positivo che siamo riusciti a raggiungere dopo una serie di ostacoli."
          proprietà[Salute]="anche se può far pensare al contrario, i cambiamenti sulla salute possono essere positivi. Una malattia che si lascia alle spalle, la fine di un percorso terapeutico, una conclusione. In altri casi può rappresentare letteralmente la morte, intesa però non con l’accezione negativa, bensì con il termine di un lungo percorso di sofferenza, che deve essere considerato una liberazione."
          proprietà[Persone]="indica in generale il dolore, una persona solitaria che guarda in sé stessa o ha la necessità di farlo, un medico che lavora a stretto contatto con la morte, una persona che rinasce dopo aver subito un grandissimo dolore."
       else:
          proprietà[Dettagli]="La morte al contrario, indica una delle conseguenze peggiori dell’intero mondo dei Tarocchi, perché l’indicazione principale è il dolore, sia fisico che mentale, e più in generale indica i sentimenti negativi, che vanno dalla malinconia, all’angoscia, alla rabbia, passando per lo scoraggiamento.\nLa morte al contrario ha il significato di un fallimento, o di una fine che non siamo in grado di superare. La situazione è uno stallo, una situazione immobile che non permette di prendere delle decisioni razionali perché non siamo nello stato di poterlo fare.\nLa situazioni possono indicare una fine, come già indicato nel significato al positivo, ma in questo caso non si riesce a lasciare la situazione alle spalle e quindi si vive un senso di disperazione, di angoscia costante, da cui non si riesce ad uscire, e questo può portare a conseguenze deleterie, come la caduta in vizi che possono avere conseguenze dirette sulla nostra salute.\nQuello per cui abbiamo lavorato fallisce, va male, “muore”, ma la rinascita almeno nel momento non c’è, perché non si è in grado di affrontare la propria perdita. Importante cercare di farlo, ma la disperazione porterà problemi anche a qualche tempo di distanza dalla sua presentazione."
          proprietà[Amore]="Indica in generale la fine. Può significare la rottura, talvolta improvvisa, di una relazione amorosa, di un divorzio oppure la fine di un rapporto d’amicizia. Non sarà una fine felice né annunciata, e potrebbe essere determinante, in negativo, sulle due persone che l’hanno subita."
          proprietà[Lavoro_e_denaro]="per il lavoro, anche in questo caso indica un termine brusco del rapporto. Può rappresentare il licenziamento, ma anche un cambiamento drastico nella vita che costringe a lasciare il proprio lavoro completamente, ad esempio un trasferimento; può indicare anche un successo raggiunto ma cancellato in modo inatteso. Può rappresentare una scelta molto difficile che ci lascia spiazzati (per esempio trasferirsi in un’altra città per un lavoro sicuro)."
          proprietà[Salute]="dal punto di vista della salute c’è in generale un imprevisto. Imprevisto in negativo, una malattia debilitante, cronica, una scoperta negativa, oppure una situazione anche molto grave ma che dura fortunatamente per poco tempo. Può non riguardare solamente la persona ma anche le altre persone che ad essa sono vicine."
          proprietà[Persone]="persone che sono in qualche modo correlate alla morte. Possono essere persone che uccidono, persone che si suicidano, oppure persone che sono molto “vicine” alla morte come una persona gravemente malata oppure depressa."

    elif arcano == "La Temperanza":
       if senso == "dritto":
          proprietà[Dettagli]="Il significato positivo della carta riguarda la ricerca dell’equilibrio e il fluire in modo costante della vita, che si accetta senza opposizioni e senza paura.\nLe caratteristiche principali sono la moderazione, la disciplina, la capacità di rimanere solidi di fronte ai problemi; non cedere alle passioni, né cedere all’ira, oppure ai vizi, sono le indicazioni principali di questa carta\nDi fronte a qualunque problema si ponga davanti bisogna agire con equilibrio, è necessario adeguarsi alle circostante e procedere con calma e con fiducia, perché quello che vogliamo ottenere lo possiamo ottenere proprio in questo modo.\nIndica l’appianamento dei litigi, la scomparsa di problemi che si sono presentati in passato, l’armonia nell’ambiente in cui si vive, sia dal punto di vista familiare e relazionale, sia dal punto di vista lavorativo, nei rapporti tra i colleghi.\nIndica anche la capacità di trasformare positivamente le situazioni che ci capitano, anche quelle che di per sé non sono positive; trarre il meglio dalle cose, risultare positivi nel complesso, essere democratici, ascoltare le opinioni degli altri per essere in grado di prendere la posizione più giusta.\nRiferita alle altre persone, può indicare anche la capacità di trovare una persona con queste caratteristiche, che può aiutarci nei problemi da affrontare e anche a trarre il meglio dalle nostre capacità."
          proprietà[Amore]="è una chiara indicazione dell’armonia, nella coppia e nella famiglia. C’è comunicazione, c’è un consolidamento del rapporto, un miglioramento di una relazione che ha vissuto un periodo di crisi. Se c’è un matrimonio questo sarà appagante, i valori su cui ci basiamo verranno rispettati e non saranno messi in discussione."
          proprietà[Lavoro_e_denaro]="anche nel lavoro abbiamo una situazione armonica, magari la conclusione di qualcosa per cui abbiamo lavorato duramente. La carta non indica, di per sé, l’arrivo di novità, quindi potrebbe significare da questo punto di vista un periodo di stallo a causa del quale, tuttavia, non ci saranno mutamenti in negativo."
          proprietà[Salute]="una situazione anche in questo caso armonica, riferita al piano fisico ma ancora di più a quello psicologico. Chi è sano manterrà il proprio stato integro, mentre chi è malato avrà una pausa dalle sofferenze, un periodo relativamente calmo e tranquillo nonostante la situazione che sta vivendo."
          proprietà[Persone]="la Temperanza indica le persone armoniche, le buone consigliere, una persona socievole, che è in grado di dare consigli. Può essere una moglie, un familiare, un amico, ma anche una persona saggia nella sua disciplina oppure un consigliere. Può indicare anche una guida spirituale."
       else:
          proprietà[Dettagli]="Quando la carta appare al rovescio, i valori dell’armonia e dell’equilibrio si spezzano, diventando l’esatto contrario, ovvero la disarmonia e il disequilibrio.\nSul piano individuale indica una persona che prende delle decisioni impulsive, spesso non coerenti con sé stesse, oppure molto sbilanciate, o ancora ostinate. Indica persone che non sono in grado di utilizzare la propria razionalità a dovere, ma che si fanno sopraffare dalle emozioni.\nLa persona tende a vivere una vita eccessiva, a cadere preda dei vizi, non riesce a superare degli ostacoli e cerca quindi di affrontarli nel modo sbagliato, non corretto.\nSe ci sono dei successi questi sono labili, oppure sono di breve durata, e questo può portare ad agire nel modo sbagliato oppure a scatenare frustrazione. Può rappresentare anche un’ideologia errata che causa una scelta sbagliata dei valori, del modo di vivere, nel modo di rapportarsi con gli altri.\nIndica, in generale, anche la chiusura mentale verso gli altri, verso i problemi e verso alcune possibili soluzioni che vengono scartate a priori spesso senza prenderle correttamente in considerazione."
          proprietà[Amore]="la componente principale è la disarmonia. Ci sono incomprensioni nella coppia, c’è incompatibilità oppure c’è il tentativo di prevalere dei due partner uno sull’altro. La disarmonia può portare alla rottura del rapporto di coppia, così come alla rottura (o alla difficile vita) di un rapporto familiare, una disarmonia che può essere difficile da risolvere se non con un intervento netto."
          proprietà[Lavoro_e_denaro]="sul piano professionale indica anche in questo caso la disarmonia di vivere con i colleghi. Progetti iniziati non sono andati a buon fine, oppure non stanno prendendo la direzione giusta, e questo problema ha come conseguenza una nostra reazione sbagliata, che rischia di peggiorare ancora di più la situazione. Più in generale, può indicare una disarmonia nel raccogliere i risultati sperati quando siamo al lavoro."
          proprietà[Salute]="dal punto di vista della salute, il problema più grande della carta al contrario è il nostro pensiero di fronte alla malattia. Lo stato di salute ha la tendenza a peggiorare, ma il problema in questa condizione è che non siamo in grado di accettarlo, peggiorando la situazione sul piano mentale, qualcosa che dobbiamo cercare di evitare. La “perdita della voglia di vivere” può sfociare nella depressione."
          proprietà[Persone]="in generale indica persone non equilibrate. Può rappresentare persone inaffidabili, tendenti all’ira, ammaliate dai vizi, troppo leggere, incapaci di prendere decisioni. In certi casi può rappresentare una persona squilibrata all’opposto, cioè che manca di capacità di scelta, una persona apatica."

    elif arcano == "Il Diavolo":
       if senso == "dritto":
          proprietà[Dettagli]="Il responso positivo della carta del Diavolo lo abbiamo quando la carta è al rovescio.\nIl diavolo rappresenta una catena, e questa catena può essere rotta e permette di farsi guidare dalle proprie passioni, nonché di rompere una situazione opprimente.\nSi riesce così a trovare una liberazione, ma anche a resistere alle tentazioni e a trovare la strada per non agire “di pancia” nelle nostre scelte.\nE’ una libertà, ma la libertà ha un prezzo: non è infatti semplice trovare la propria strada nella libertà, e seguire le passioni più condurre a successi, ma anche agli insuccessi, nella propria vita.\nIl diavolo al rovescio indica anche l’azzardo e l’audacia: una propensione a rischiare, ad investire, a buttarsi in qualcosa di nuovo, ma anche il presentarsi di un’occasione da non perdere, perché potrebbe non capitarne una simile.\nPuò indicare anche il superamento di un ostacolo, inteso sia in senso psicologico (una “catena per la mente”, un diverso modo di pensare, un problema di cui non si riesce a trovare la soluzione), sia in senso fisico (superare una difficoltà, un momento difficile come un parto o un intervento chirurgico), a cui si aggiunge il successo professionale, ad esempio di tipo economico.\nSul piano affettivo, il diavolo al rovescio indica incontri nuovi ed esaltanti, magari un rapporto extraconiugale, con la costante che tutto è fondato unicamente sul piacere, sul fascino, sull’attrazione, sull’uscita dagli schemi. In questo senso, la conquista in amore può essere causata non da una questione affettiva, bensì da una legata alla passione, al successo, al denaro.\nCollegando quest’ultimo significato alla rottura delle catene, il Diavolo al rovescio potrebbe significare la rottura di una vecchia relazione che ormai non ci soddisfa, ma che in passato non abbiamo avuto il coraggio di spezzare."
          proprietà[Amore]="incontri nuovi e piacevoli, ma legati esclusivamente al piacere e non all’affetto, conquiste ottenute grazie al denaro e al successo."
          proprietà[Lavoro_e_denaro]="Volontà di fare carriera, guadagni inattesi, successi in ambito professionale o finanziario."
          proprietà[Salute]="Forma fisica più marcata rispetto alla norma, superamento di ostacoli legati alla salute ritenuti insormontabili."
          proprietà[Persone]="la carta del Diavolo indica persone con molto carisma, particolarmente appassionate del proprio lavoro, competenti nella propria professione e guidate dalle proprie passioni."
       else:
          proprietà[Dettagli]="I significati negativi del Diavolo sono legati alla dipendenza che ci incatena, e sono rappresentati dal tarocco del diavolo a dritto.\nSiamo legati a qualcuno e a qualcosa e il nostro obiettivo è quello di liberarcene, anche se non sarà facile. Cediamo facilmente alle tentazioni, siamo dipendenti da una passione, stiamo vivendo qualcosa di sbagliato anche se non riusciamo a farne a meno.\nRappresenta quindi tutti i tipi di dipendenza, da quelli legati al denaro, al gioco d’azzardo, all’alcool, alle droghe, passando per le dipendenze di tipo sessuale.\nPer chi non le sta vivendo, oppure ne sta uscendo, indica la possibilità di una ricaduta e rappresenta quindi un monito da non ignorare, perché la possibilità di cadere nuovamente nella tentazione è molto vicina. Questo potrebbe portare ad una modifica degli equilibri che abbiamo raggiunto nella nostra vita.\nOltre alle tentazioni, bisogna considerare anche la possibilità di avere cadute morali o fisiche, ad esempio un errore grave, di cui necessariamente dovremo pentirci.\nDobbiamo valutare bene le nostre scelte, capire se quello che stiamo per fare sia davvero corretto: la carta del diavolo si ricollega infatti alla ribellione, rivolta, alla lotta sociale, nel piano interpersonale, mentre su quello personale all’insorgenza di una malattia, di un’infezione, di problemi sul piano fisico (legati alla salute), da cui il tarocco ci mette in guardia.\nNon solo significati negativi, però: il tarocco ci invita a fare un esame di noi stessi, cercando di capire non solo quali sono le tentazioni che ci affliggono, ma anche ad indagarne l’origine, per scoprire di più su noi stessi, per evitare le conseguenze negative che possono influenzare la nostra vita.\nSe abbiamo impostato la richiesta non per nostro giudizio ma per l’altrui, la risposta è che una persona è vicina a noi mossa solamente dalle proprie passioni. Può cercare gratificazioni, può essere interessata ai nostri soldi, può essere interessata ai nostri punti deboli per sopraffarci; in questo senso, la carta ci mette in avvertimento verso la condotta delle altre persone, da cui dobbiamo guardarci le spalle."
          proprietà[Amore]="Amore legato esclusivamente alla lussuria, incontri extraconiugali che potrebbero portare ad una crisi con il partner, pratiche comunemente non accettate."
          proprietà[Lavoro_e_denaro]="insuccesso, problemi sul piano professionale con le persone con cui si lavora, competitività, obiettivi non raggiunti."
          proprietà[Salute]="arrivo di una malattia, o complicazione, o mancato miglioramento di una malattia in essere. Le malattie possono riguardare non solo il piano fisico, ma anche il piano psicologico, legate in particolar modo allo sviluppo di dipendenze."
          proprietà[Persone]="rapportata alle persone, indica gli avversari (al lavoro, in amore), persone negative, persone care che fanno scelte sbagliate."

    elif arcano == "La Torre":
       if senso == "dritto":
          proprietà[Dettagli]="Il significato al positivo è legato per lo più ad un avvertimento nei confronti della persona, più che ad un crollo; indica che la sorte non è dalla nostra parte, e per evitare quello che potrebbe succedere è necessario spostarsi e cambiare mentalità, modo di agire.\nL’evento che sta per accadere può essere diverso tipo: può riguardare il piano fisico, quindi qualcosa di negativo (un incidente, una problema grave in arrivo), ma anche sul piano psicologico: nella situazione che si sta vivendo, relazionale o lavorativa, si è raggiunto un punto di rottura, è arrivato il momento di cambiare, non si riesce più a procedere; o si cambia, oppure le conseguenze saranno negative.\nQuello che bisogna fare è distruggere l’equilibrio che si è venuto a creare, ed è necessario affrontare il cambiamento. A seconda della situazione, le nostre scelte dovranno essere più o meno drastiche, ma questo cambiamento può essere anche fondamentale nella nostra vita.\nIn generale, comunque, è importante capire che qualcosa sta per accadere e che siamo noi a dover variare il nostro modo di agire; procedere nella stessa direzione in cui stiamo andando non sarà positivo, ed è quindi importante pensare, il prima possibile, a come cambiare quella direzione."
          proprietà[Amore]="indica in generale un cambiamento, non necessariamente negativo, ma che se non colto avrà conseguenze indesiderate. Può trattarsi di un colpo di fulmine, di una proposta di matrimonio, di una relazione che si porta avanti da tempo e che è giunta alla fine. Positiva o negativa che sia l’occasione deve essere colta, altrimenti le conseguenze comunque saranno negative."
          proprietà[Lavoro_e_denaro]="non è molto diverso da quanto detto per le relazioni, e anche in questo caso può indicare un cambiamento positivo o negativo. Dalla promozione, borsa di studio, lavoro in una città lontana, all’interruzione di un rapporto di lavoro ormai diventato opprimente. Potrebbe indicare anche aiuti economici inattesi."
          proprietà[Salute]="nell’ambito della salute indica generalmente un cambiamento necessario che, se non viene effettuato, avrà conseguenze nefaste. Può riguardare lo stile di vita, il modo di alimentarsi, le terapie in atto per le persone malate; il cambiamento si rende necessario in tempi brevi, perché le conseguenze potrebbero essere molto peggiori della situazione attuale."
          proprietà[Persone]="indica una persona ribelle, che entrerà nella nostra vita e determinerà nei cambiamenti. Non ci sono preferenze di età o sesso, quindi può essere un partner, un figlio, un amico o un genitore; la costante è che, in qualche modo, cambierà il nostro modo di vivere."
       else:
          proprietà[Dettagli]="La Torre al contrario indica che quello che abbiamo iniziato è destinato a fallire, senza possibilità di recupero: da questo punto di vista è una delle carte più pesanti, se non in assoluto la più pesante, per le informazioni che fornisce, tra tutti i Tarocchi.\nIndica in generale la fine di qualcosa. Può essere un rapporto amoroso, un rapporto di lavoro, oppure un incidente fisico, la possibilità di eseguire qualcosa che ci piace, oppure anche un crollo emotivo; può essere correlato con la nostra superiorità, può indicare l’essere finito all’interno di un vicolo cieco o in una situazione da cui difficilmente c’è una via d’uscita.\nPurtroppo le indicazioni fornite dalla Torre al negativo lasciano poco scampo alle soluzioni, e in generale dobbiamo fare tutto ciò che è in nostro potere per evitare il disastro, per evitare come indicato dalla carta di “cadere dalla Torre”. A differenza dei significati positivi, in cui l’effetto negativo dipendeva solamente da una nostra mancata capacità di cambiare, qui il negativo c’è, è innegabile, e possiamo solo procedere cercando di attutire il colpo."
          proprietà[Amore]="Indica che la situazione che stiamo vivendo è destinata a degenerare, se non completamente a concludersi. Un rapporto di coppia, anche longevo, è esaurito e terminerà con la separazione; potrebbe rappresentare anche la perdita di una persona cara, in senso materiale (il decesso) o psicologico, la rottura di un rapporto nel peggiore dei modi."
          proprietà[Lavoro_e_denaro]="anche per quanto riguarda il lavoro siamo purtroppo giunti alla fine di quello che potevamo portare avanti. Può indicare un licenziamento, da parte nostra o dell’azienda, può indicare la rottura di un contratto, un problema economico, e dal punto di vista dello studente una bocciatura, una sconfitta, un’incapacità di proseguire. E’ il caso di valutare se quella intrapresa sia la strada giusta per le nostre necessità."
          proprietà[Salute]="anche in questo caso, indica un imprevisto, il peggioramento di una situazione rosea che stiamo vivendo. Per i malati può essere un’acutizzazione della malattia, per i sani un problema che riguarda la salute. Il vantaggio è che “improvviso” non significa “grave”, automaticamente, quindi potrebbe significare solamente una malattia, magari acuta, che potrebbe comunque risolversi."
          proprietà[Persone]="la carta indica una persona spietata, qualcuno che cerca in ogni modo di fare del male, di distruggere o rovinare le altre persone, qualcuno da cui è il caso di tenersi alla larga."

    elif arcano == "La Stella":
       if senso == "dritto":
          proprietà[Dettagli]="Il significato positivo della carta è legato alle buone prospettive, e in generale al destino favorevole, legato anche in parte ad una protezione celeste.\nLe stelle e gli astri si trovano in posizioni favorevoli, influenzando in positivo la vita della persona, che tuttavia ha anche delle caratteristiche positive, che sfrutterà al meglio. Le stelle possono indicare che un progetto in atto arriverà alla conclusione in senso positivo, indicano la fiducia in sé stessi, l’ottimismo, l’allegria, la cordialità.\nLa carta è un indice che quello che stiamo facendo sta andando nel modo giusto, e ci spinge a continuare in quella direzione, per qualsiasi tipo di percorso abbiamo intrapreso. Gli sforzi compiuti saranno ripagati, e siamo nella condizione migliore per esaudire i nostri desideri sia grazie alle nostre capacità che all’influenza celeste.\nLa carta può indicare anche una crescita personale, che magari è già iniziata e che procede nel migliore dei modi. Dal punto di vista delle relazioni, andiamo incontro a relazioni nuove e quelle che già ci sono avranno la tendenza a solidificarsi, proseguendo al meglio."
          proprietà[Amore]="non è indice di grandi cambiamenti, ma indica che il percorso che stiamo avendo, che sia agli inizi o che sia già ben solido, sta procedendo per il meglio. Una relazione non ancora iniziata potrebbe sbocciare, un fidanzamento confluire in un matrimonio, e quest’ultimo nella nascita di figli. Sul piano relazionale più ampio, come i rapporti familiari e le amicizie, anche in questo senso siamo in un periodo positivo che porterà al miglioramento di queste relazioni."
          proprietà[Lavoro_e_denaro]="la stella è un buon auspicio anche sul piano lavorativo e professionale. La sua presenza indica che i progetti che abbiamo iniziato procederanno bene o sono destinati a concludersi al meglio, che le nostre passioni tenderanno a crescere; aumenteranno anche le nostre capacità come quella di affrontare i problemi, oppure la creatività, che potremo applicare all’ambito artistico."
          proprietà[Salute]="anche dal punto di vista della salute la stella indica dei miglioramenti. Può indicare che lo stato di salute raggiunto sarà mantenuto oppure, per i malati o per chi ha problemi non solo fisici ma anche psicologici, un miglioramento della propria condizione generale."
          proprietà[Persone]="indica una persona equilibrata, devota, coraggiosa, poco interessata alle questioni materiali e molto più a quelle spirituali. E’ una persona, generalmente donna, che porta con sé dei consigli positivi, quindi è una persona benefica da avere vicino, che può supportarci in un periodo in generale positivo della nostra vita."
       else:
          proprietà[Dettagli]="Il capovolgimento delle Stelle indica esattamente il contrario rispetto alla carta al diritto: se in un modo indicava la fortuna e il buon auspicio, “essere sotto una buona stella”, al rovescio indica in generale la sfortuna, e l’incapacità di adattarsi ad una situazione che non si addice a noi stessi.\nIl periodo che vivremo non porterà con sé drastici sconvolgimenti, ma sarà in generale negativo, privo di possibilità, con i progetti che abbiamo iniziato che non sono destinati ad arrivare a termine o, comunque, procederanno nell’incertezza. Impiegheranno molto tempo per essere realizzati, fino a sfociare nella frustrazione.\nAlla “cattiva stella” va ad aggiungersi l’insofferenza personale, la scarsa capacità di adattarsi alle nuove situazioni, la difficoltà di riuscire ad emergere, il seguire la corrente negativa senza cercare di fare qualcosa che possa cambiare il destino che ci è stato riservato.\nQuesto può comportare ad uno squilibrio tra il piano fisico e quello psichico che può causare, nella peggiore delle ipotesi, dei problemi più gravi dovuti, in larga parte, alla nostra scarsa capacità di reagire alle situazioni."
          proprietà[Amore]="Indica che la relazione che stiamo vivendo, o che stiamo per vivere, non è in un buon periodo. Questo non significa l’interruzione, almeno non in modo diretto (indica una freddezza tra i partner, il disinteresse reciproco, l’eccessiva leggerezza nella relazione), ma la condizione che ci troveremo a vivere, e lo squilibrio di uno dei due partner, potrebbe comunque condurre alla rottura. Questo vale non solo per il rapporto di coppia, ma anche per altre relazioni sociali."
          proprietà[Lavoro_e_denaro]="i progetti che abbiamo iniziato non stanno procedendo come dovrebbero, il lavoro che facciamo non è soddisfacente, non è ben retribuito, non ci sono buoni rapporti con i colleghi. Anche in questo caso non sta succedendo niente di dannoso o determinante, ma la condizione potrebbe spingerci a voler cambiare le cose, ottenendo così un effetto ancora più negativo di quello che stiamo vivendo."
          proprietà[Salute]="sul piano della salute, il periodo non sarà positivo sul piano fisico, oppure su quello psichico. Turbe psichiche come l’ansia, o la paura, potrebbero portarci a vivere in modo negativo anche una situazione che, da sola, non è tutto sommato debilitante, pur non essendo comunque positiva."
          proprietà[Persone]="la carta al contrario indica una persona con cui è difficile relazionarsi, insoddisfatta, con un lavoro o una relazione frustrante, che può sfociare in vizi anche piuttosto gravi come l’alcolismo o la dipendenza da stupefacenti."

    elif arcano == "La Luna":
       if senso == "dritto":
          proprietà[Dettagli]="La Luna, al positivo, riguarda tutto ciò che è l’inconscio della persona. E’ la dimensione notturna delle cose, la memoria, l’intuito, la riflessione, la fantasia e il sogno; sono tutte facoltà che richiedono un approccio indiretto, non diretto ma riflessivo, e per questo motivo i risultati positivi non sono mai completamente positivi: non possiamo sapere dove l’inconscio può portare una persona, in che direzione lo potrà condurre.\nIn passato era legato al successo delle pratiche magiche, alla ricerca della magia e dell’esoterismo, delle pseudoscienze; oggi rimane più legato al sogno, ai ricordi, al passato, agli amici d’infanzia e a tutte le emozioni tipiche dell’età infantile.\nSimboleggia la paura che possiamo avere nella ricerca della verità, le tenebre che vengono chiarificare dalla luce della luna che ci rende più chiara, ma non ci indica, la direzione da intraprendere.\nIndica la necessità di effettuare una ricerca intellettuale, di aprire la mente per trovare soluzioni come farebbe un bambino, invita alla riflessione, alla perseveranza, all’approfondire i propri sentimenti per trovare una strada alternativa in un problema che non riusciamo a risolvere."
          proprietà[Amore]="indica tutto ciò che di inconscio riguarda le relazioni. La passione, i legami familiari, la parte più spirituale dei rapporti che stiamo vivendo, l’arrivo di una gravidanza, di un parto o di un matrimonio con la sua dose di speranze, ma anche di paure da affrontare, che la carta ci invita, appunto, ad affrontare."
          proprietà[Lavoro_e_denaro]="sul piano professionale, anche in questo caso, non c’è un’indicazione ben precisa su quello che potrebbe accadere, se non un invito alla creatività: lasciarsi andare nei lavori creativi potrebbe essere di buon auspicio, così come cercare di avere a che fare con i bambini. Cercare soluzioni fantasiose nel lavoro potrebbe portare risultati inaspettati."
          proprietà[Salute]="dal punto di vista della salute indica che la strada che stiamo seguendo per mantenere o migliorare il nostro stato di salute deve passare dal sogno, dall’esplorazione delle proprie emozioni, da un approfondimento psicologico su noi stessi. Non cercare la strada nella coscienza, ma nell’inconscio."
          proprietà[Persone]="indica in generale persone che sognano, probabilmente bambini oppure adulti che hanno tuttavia ancora qualche tratto infantile nel loro carattere. Può indicare, più in generale, qualunque persona abbia un tratto creativo nel lavoro che fa."
       else:
          proprietà[Dettagli]="Quando la luna si presenta capovolta non si esce dal suo significato originale, l’inconscio, ma mentre al positivo la carta indica una via da seguire, al negativo al contrario indica che le tenebre si fanno più fitte, che il percorso inconscio è più difficile da affrontare.\nCosì le emozioni distruttive come la paura, la rabbia, l’ansia, l’angoscia possono prendere il sopravvento, le soluzioni che abbiamo possono sembrare ingannevoli ed essere quindi diverse da quelle che possiamo immaginare.\nLe idee sbagliate, la mancata ricerca della verità, i pregiudizi che possiamo avere, il fanatismo, rendono più difficile affrontare i problemi che ci aspettano, indicando un problema di natura emotiva e psicologica che dobbiamo necessariamente risolvere per affrontare con lucidità quello che ci aspetta. Tendiamo infatti a mentire a noi stessi, vedendo i nostri progetto non andare come dovrebbero o comunque come ci aspettiamo.\nDobbiamo fare attenzione ai pericoli non evidenti, come le delusioni, le perdite, i furti, i raggiri e le truffe, che potrebbero essere frequenti se ci troviamo in uno stato mentale alterato; attenzione anche al fatto che non si ha una visione d’insieme della situazione che affrontiamo, perché questa mancanza potrebbe essere determinante, in negativo, nel fallimento di qualcosa che abbiamo iniziato."
          proprietà[Amore]="Dal punto di vista delle relazioni, la luna al rovescio indica tradimenti, litigi, menzogne, incomprensioni che possono essere anche gravi e mancanza di confidenza. Questo può riguardare la relazione amorosa ma anche i rapporto con altre persone che ci stanno vicine. In alcune interpretazioni, la luna al contrario può significare anche l’effetto di pratiche magiche negative che sono state rivolte verso di noi."
          proprietà[Lavoro_e_denaro]="dal punto di vista professionale, il significato al negativo riguarda invece generalmente le menzogne, i litigi, le truffe, i tranelli, le persone che fanno di tutto perché non raggiungiamo i nostri obiettivi (magari perché questo porterebbe a problemi nei loro confronti). In alcuni casi indica anche che la posizione lavorativa non è adatta a noi."
          proprietà[Salute]="per quanto riguarda la salute, questa potrebbe risentire di un’impostazione mentale che non è ottimale per i nostri bisogni. Non abbiamo un’idea completa della situazione, stiamo seguendo terapie o cure non idonee, oppure i disagi psicologici si riflettono sul piano fisico, e di conseguenza sono determinanti, in negativo, nel peggioramento dello stato generale di salute."
          proprietà[Persone]="la Luna indica una persona materialista, pronta a tutto per imbrogliare il prossimo, legata alle truffe, agli inganni, ostile verso la nostra persona. Può indicare dei falsi amici o nemici che non ci aspettiamo."

    elif arcano == "Il Sole":
       if senso == "dritto":
          proprietà[Dettagli]="Il significato della carta al positivo, a dritto, è quello di splendore, vittoria, illuminazione, superamento delle difficoltà: in sintesi, la carta sta ad indicare che il percorso è illuminato e che, qualsiasi sia la domanda, è il momento di agire.\nSono passati dei tempi bui, ma l’obiettivo che ci eravamo posti adesso è più chiaro, come è anche diventato più chiaro il percorso che dobbiamo fare per raggiungerlo: non dobbiamo quindi fare altro che percorrerlo, abbracciarlo per raggiungere lo scopo che avevamo.\nLa variabilità delle figure nella seconda metà della carta rimanda, comunque, alla vittoria: il bambino che cresce, i due gemelli che si scaldano e gioiscono dell’illuminazione data dalla luce del sole, il cavallo che vittorioso procede per la sua strada.\nQuesta carta sta a significare che quello che abbiamo iniziato porterà ad una vittoria ed avrà, in generale, un esito positivo che dobbiamo cercare di portare avanti, proprio perché raggiungeremo i risultati sperati.\nQuesto vale per qualsiasi domanda che abbiamo rivolto, anche se non evita che il percorso per il raggiungimento dell’obiettivo potrebbe essere “intricato” da qualche tipo di difficoltà; in questo caso dobbiamo comunque procedere sapendo che, nonostante queste, riusciremo a superarle."
          proprietà[Amore]="indica un rapporto armonioso e duraturo, nel quale c’è complicità tra i componenti. Se l’obiettivo è un matrimonio, o la nascita di un figlio, questo obiettivo sarà raggiunto nel migliore dei modi, con il supporto del partner e con grande soddisfazione da parte nostra."
          proprietà[Lavoro_e_denaro]="da questo punto di vista, la strada che dobbiamo percorrere per seguire i nostri progetti, per procedere con la nostra ambizione, o con un investimento che abbiamo effettuato, è quella giusta. Dobbiamo continuare a camminare in quella direzione, con l’obiettivo che ci apparirà sempre più chiaro man mano che continueremo a procedere; la strada che percorreremo è comunque destinata al successo."
          proprietà[Salute]="dal punto di vista della salute, il sole indica in generale uno stato di buona salute. Per chi è in salute, questa condizione verrà mantenuta, mentre per chi non lo è, ci sarà un miglioramento della malattia, che farà vedere nuovamente “la luce del sole”. Da notare che il sole in questo senso può avere il significato della fine di un percorso terapeutico particolarmente arduo."
          proprietà[Persone]="il sole fa riferimento ad una persona generosa, solare, allegra, sincera; può rappresentare persone giovani, tra cui i bambini, mentre per gli adulti indica, in generale, una persona saggia e dei cui consigli ci possiamo fidare."
       else:
          proprietà[Dettagli]="Quando il Sole si presenta nel verso sbagliato, la positività che trasmette viene invece capovolta; il significato diventa quello di una luce, si, ma illusoria, che abbaglia, di un obiettivo che pensavamo di aver raggiunto e che invece non abbiamo perseguito come speravamo; questo indica in generale l’aspettativa che abbiamo di un successo o di un obiettivo che, tuttavia, non corrisponde alla realtà.\nPotrebbe quindi indicare una situazione di felicità ma solamente apparente, che non tiene conto (volontariamente, magari) del fatto che ci sono criticità che non possiamo più aspettare ad affrontare; far finta di nulla in situazioni in cui ci sono problemi potrebbe portare, nel proseguire, a problemi più grandi da affrontare.\nUn problema che il sole capovolto può identificare è anche l’opinione troppo alta che abbiamo di noi stessi: in particolare, avere un’autostima troppo elevata ci può portare a contare troppo sulle nostre stesse capacità, senza considerare quindi l’umiltà nell’affrontare i problemi.\nQuesto può avere conseguenze negative su vari piani, in particolare sul lungo periodo, quando il nostro “abbaglio” si perderà e potremo vedere le conseguenze, purtroppo non positive, di quello che abbiamo raggiunto; è una carta che ha un significato negativo, ma soprattutto che ci mette in guardia dai nostri errori e che deve far riflettere sul fatto che quello che il percorso che abbiamo intrapreso sia, effettivamente, la strada giusta."
          proprietà[Amore]="Dal punto di vista delle relazioni, indica una difficoltà, magari non apparente ma comunque presente. Potrebbe indicare il tentativo di tenere in piedi una relazione magari già al termine, oppure una condizione nella quale non riusciamo ad individuare i problemi e le difficoltà dell’altra persona. Quando la situazione è manifesta, può indicare le incomprensioni o i litigi."
          proprietà[Lavoro_e_denaro]="in generale può essere indice di una sopravvalutazione delle nostre capacità e del nostro lavoro, che potrebbe non portare ai risultati sperati. Un risultato cercato con non troppo impegno perché siamo certi di raggiungerlo, o aspetti dei nostri progetti che diamo per scontato, sbagliando."
          proprietà[Salute]="sul piano della salute, il Sole indica un miglioramento che, però, è solo in apparenza. Potrebbe indicare un miglioramento momentaneo di una patologia grave, oppure potrebbe essere indice di un problema che stiamo sottovalutando, ma che potrebbe aggravarsi nel corso del tempo. In tutti i casi, non dobbiamo sottovalutare la situazione."
          proprietà[Persone]="il Sole al rovescio indica una persona che si ritiene superiore, un superbo, oppure qualcuno di disonesto, che ci abbaglia con le sue parole senza però avere il valore che vuole farci intendere."

    elif arcano == "Il Giudizio":
       if senso == "dritto":
          proprietà[Dettagli]="Il Tarocco del giudizio dritto indica, in generale, qualcosa di positivo.\nIndica un giudizio rapido ed improvviso, un grande cambiamento che in generale è positivo. Le chiavi di lettura sono diverse: si va dalla sorpresa piacevole agli eventi positivi che si verificano in modo inaspettato; può essere legato ad una vittoria, ad una conquista, ad un successo, ma anche all’uscita di una crisi, che si risolve improvvisamente anche se stava durando da molto tempo.\nLa risoluzione dei problemi è, in generale, positiva.\nIn un’accezione più neutrale, può indicare anche un evento inaspettato che ci ha colpito. Una telefonata da una persona che non vedevamo da molto tempo, una comunicazione, l’inizio di un cambiamento o di un’evoluzione (un nuovo lavoro, una promozione), oppure la rinascita di qualcosa che ormai davamo per perduto, ad esempio una vecchia relazione o un rapporto d’amicizia. Sul piano del lavoro può essere la rinascita di un progetto che avevamo abbandonato ma che pensavamo fosse stato abbandonato ormai da tempo.\nIl giudizio può essere collegato anche a un’improvvisa notorietà, trovarsi al centro dell’attenzione in modo inaspettato ma comunque positivo. Simboleggiando il tempo che passa, indica anche la modernità e l’evento inaspettato può essere legato ai nuovi mezzi di comunicazione che abbiamo a disposizione.\nSu un piano più psicologico, può simboleggiare l’indipendenza e anche la voglia di indipendenza da quella che è la nostra situazione attuale, la volontà di un cambiamento, di una rottura degli schemi.\nDa notare che, in generale, il giudizio è rapido, quindi possiamo aspettarci il cambiamento in un futuro non troppo lontano, indicativamente a poche settimane di distanza dalla lettura del tarocco. Sebbene in alcune circostanze i tempi possano essere più prolungati, non si deve attendere molto per scoprire gli esiti del Giudizio e l’evento a cui esso si riferisce."
          proprietà[Amore]="un improvviso ed inaspettato successo, un colpo di fulmine, un cambiamento inatteso da parte della persona con cui abbiamo a che fare da molto tempo (cambiamento di idee, di atteggiamento verso di noi)."
          proprietà[Lavoro_e_denaro]="Una promozione, una svolta nello studio come il superamento di un’esame, il riprendere in mano un progetto o una strada che avevamo abbandonato, un viaggio, un miglioramento improvviso dal punto di vista finanziario."
          proprietà[Salute]="il termine di una sofferenza, un miglioramento di malattia in atto, un miglioramento generale dello stato di salute fisica e psicologica."
          proprietà[Persone]="il Giudizio indica una persona imparziale, severa, ma allo stesso tempo stimolante e senza pregiudizi, caratterizzata dalla volontà di miglioramento personale e collettivo."
       else:
          proprietà[Dettagli]="Contrariamente a quanto si potrebbe pensare, il Giudizio al contrario non indica un cambiamento in negativo, bensì una difficoltà nel cambiamento, una situazione che dovrebbe cambiare ma per la quale il cambiamento non arriva; in alternativa, cose che credevamo essere cambiate ma che si verrà a sapere non essere così.\nUn’accezione è quella nella quale stiamo continuando a rimandare una scelta importante, impedendo in questo modo al cambiamento di arrivare, oppure ostinarsi su basi che sappiamo (o che non sappiamo) essere errate. In alcuni casi, indica l’aggiungere disagi a un problema che già da solo ci sta consumando.\nIn altri casi, indica che un cambiamento che stavamo attendendo da tempo in realtà non sta per arrivare, il che potrebbe portare anche ad una conseguenza di tipo negativo, sebbene questo non sia scontato e dipenda dalle nostre scelte.\nIl giudizio al contrario può indicare anche che, nonostante la nostra volontà di mettersi in gioco e di applicarsi perché il cambiamento arrivi, stiamo seguendo il percorso nel modo sbagliato, ottenendo così il risultato opposto, cioè uno stallo e di conseguenza una delusione.\nIn amore, potrebbe significare l’instaurarsi lento oppure il protrarsi di una crisi di coppia, così come nel lavoro potrebbe indicare dei problemi sul piano professionale, sia sul piano finanziario che in quello dei rapporti con i colleghi.\nInfine, il significato del Giudizio potrebbe essere legato ai cambiamenti forzati, che ci sono ma sono indipendenti dalla nostra volontà, e potrebbero non essere positivi per noi.\nSe in risposta ad una domanda, il giudizio al contrario è sfavorevole, per cui la risposta alla domanda risulterà essere negativa."
          proprietà[Amore]="Il Giudizio al contrario può simboleggiare la nascita di una crisi di coppia o il portare avanti una crisi al momento già esistente. Il mantenimento di un’amicizia negativa, la falsità di una persona che credevamo essere dalla nostra parte."
          proprietà[Lavoro_e_denaro]="Il Giudizio al contrario può simboleggiare una situazione di stallo dal punto di vista lavorativo, una promozione o un successo finanziario che tarda ad arrivare, problemi con i colleghi o con i superiori in ambito lavorativo. Indica anche situazioni già in sospeso che rimarranno in sospeso nel prossimo futuro."
          proprietà[Salute]="Dal punto di vista della salute, il Giudizio al contrario indica malattie croniche che non migliorano, oppure lo stallo o il peggioramento di manifestazioni fisiche e psicologiche, condizioni come problemi cardiovascolari, ansia generalizzata, affaticamento e stanchezza costanti."
          proprietà[Persone]="Relativamente alle persone, il Giudizio al contrario indica una persona esaltata, fanatica di qualcosa, una persone che profetizza avvenimenti falsi, una persona che usa le proprie capacità per imbonire gli altri o per creare conflitti tra loro."

    elif arcano == "Il Mondo":
       if senso == "dritto":
          proprietà[Dettagli]="Il significato al positivo è legato alla completezza, per la rappresentazione di una delle carte più importanti dell’intero gioco.\nQualunque sia l’ambito a cui ci si riferisce, la carta fa riferimento ad qualcosa di completo ma anche di duraturo, non destinato a finire in breve tempo.\nGli ostacoli saranno facilmente superati, e non con difficoltà, ma con una relativa semplicità. Il toro simboleggia la fatica, l’impegno che abbiamo messo per raggiungere l’obiettivo che ci eravamo prefissi, mentre tutti gli altri simboli ricordano la vittoria, la capacità di volare o di superare con forza qualsiasi ostacolo: tutto procede quindi nel senso delle migliori aspettative che si potessero avere.\nIl trionfo può essere visto come il raggiungimento di un obiettivo lavorativo, come una vittoria economica, il coronamento di un sogno d’amore, oppure un’aspirazione che è stata attesa a lungo e che, finalmente, trova il suo compimento. Rappresenta anche una completezza in termini di salute, con problemi che si sono verificati a lungo tenderanno a realizzarsi."
          proprietà[Amore]="rappresenta il completamento delle proprie aspirazioni. Si riesce a completare un sogno d’amore, un fidanzamento, un matrimonio oppure la nascita dei figli. Ma significa anche che il rapporto a cui siamo interessati si completa, è felice, duraturo, non ci saranno ostacoli che non possono essere superati."
          proprietà[Lavoro_e_denaro]="anche dal punto di vista del lavoro la situazione è simile. I progetti iniziati avranno successo, si concluderanno per il meglio, le attività che inizieremo saranno solide. Dal punto di vista economico, non avremo alti e bassi ma una situazione, oltre che rosea, anche tranquilla, che ci permetterà di procedere senza dubbi in futuri progetti, tra cui acquisti importanti (come una casa) o progetti non materiali, come prendersi cura di un bambino."
          proprietà[Salute]="dal punto di vista della salute, il Mondo indica la guarigione. Se ci sono stati problemi, sensi di malessere continui, oppure se stavamo lottando contro qualcosa che ci opprimeva, adesso questa oppressione tenderà a scomparire, a farsi da parte, per permetterci di raggiungere lo stato di benessere a cui abbiamo tanto aspirato."
          proprietà[Persone]="il mondo fa riferimento ad una persona semplice, sincera, carismatica, veramente interessata a noi o ai nostri progetti. C’è da dire che il Mondo è una carta generica, da questo punto di vista, e può essere difficile applicarla ad una persona precisa."
       else:
          proprietà[Dettagli]="Contrariamente a quanto si potrebbe pensare, il Mondo al contrario sta a significare non un capovolgimento (quindi che tutto ciò che ci sta per succedere sia destinato al fallimento), quanto ad un’attenuazione della completezza.\nPuò essere quindi inteso sia in termini temporali, a significare quindi che un completamento ci sarà, ma non sarà immediato, sia in termini materiali, ovvero che i nostri progetti si realizzeranno, ma non del tutto, non a pieno come avremmo sperato, oppure la conclusione sarà apparente, illusoria.\nLa carta deve quindi essere interpretata non in negativo, ma intendendo che c’è ancora da lavorare per raggiungere l’obiettivo che ci siamo preposti. Ci saranno ancora ostacoli da superare, per raggiungere l’obiettivo dovremo fare delle piccole rinunce, oppure incontreremo delle resistenze da parte di qualcuno, in cui dobbiamo comprendere noi stessi.\nParticolare attenzione va fatta sull’eccessiva fretta di raggiungere il risultato sperato, e sul fatto che abbiamo magari fatto “un passo più lungo della gamba”, senza avere le risorse, materiali o immateriali, di cui avevamo bisogno per raggiungere la completezza del nostro progetto.\nDa questo punto di vista, la carta potrebbe indicare superbia, eccessivo orgoglio, mancanza di modestia e un’eccessiva propensione al far valere le nostre ragioni senza ascoltare gli altri con conseguenze che saranno tendenti al negativo (anche se non nettamente negative)."
          proprietà[Amore]="nelle relazioni, il mondo al contrario sta ad identificare la mancanza di soddisfazione, sia da parte nostra (non siamo contenti di quello che fa il partner o di come si comporta), sia da parte dell’altro. Per raggiungere la completezza dobbiamo prima riuscire ad eliminare del tutto i conflitti, cercando in questo modo di arrivare a vivere una relazione quanto più possibile appagante."
          proprietà[Lavoro_e_denaro]="anche dal punto di vista lavorativo i nostri progetti procedono, a tutti gli effetti, ma lo fanno in un clima di resistenza, in qualche modo ostile, che non riesce a completarsi; può indicare anche una scarsa considerazione, da parte nostra o degli altri, del progetto che vogliamo realizzare."
          proprietà[Salute]="dal punto di vista della salute può indicare una resistenza, da parte di altri o nostra, nel raggiungere i propri obiettivi. Potrebbe indicare anche una propensione mentale a non voler davvero risolvere la situazione, vittimismo, depressione, che richiede l’aiuto di un esperto."
          proprietà[Persone]="anche in questo caso il significato è generico, ma in generale viene indicata una persona ostile, qualcuno che ci ostacola nel raggiungere i nostri progetti."

    elif arcano == "Il Matto":
       if senso == "dritto":
          proprietà[Dettagli]="Il significato positivo del Matto è in generale quella dell’irrazionalità come sinonimo di buona sorte, come spinta creativa che permette di raggiungere i propri obiettivi senza però seguire un percorso precostituito ma seguendo l’istinto, la sensazione che ci porta a capire, in modo illogico, qual è la strada giusta da intraprendere.\nLa follia non è quindi vista in senso negativo ma, anzi, la spensieratezza, l’innocenza, la spontaneità e in generale l’inconscio permette di capire qual è la strada più corretta da seguire.\nLa carta rappresenta l’anticonformismo, ma anche il voler perseguire un ideale a tutti i costi, rappresenta il viaggio, inteso sia in senso fisico (cioè, una partenza in arrivo, magari conseguente ad una scelta momentanea ed impulsiva), sia in senso psicologico (una rivelazione mentale, un cogliere qualcosa che prima non si riusciva bene ad identificare) sia metaforico, inteso come il viaggio che è la vita in questo mondo."
          proprietà[Amore]="rappresenta l’avventura, la libertà e anche l’allegria. L’amore c’è, non manca, ma viene vissuto con felicità, con spensieratezza, e la carta indica anche le follie fatte per amore, il cercare di conquistare (con esito positivo) la persona amata senza seguire i classici schemi."
          proprietà[Lavoro_e_denaro]="da questo punto di vista, il Matto rappresenta generalmente il viaggio, la partenza per un viaggio di lavoro per una decisione presa all’ultimo momento, ma anche un viaggio inaspettato che ci consente di “rompere”, per un certo periodo, con la routine della vita quotidiana. Può anche essere una rottura che non è legata ad uno spostamento fisico, per cui una rottura con il vecchio lavoro, o dei propri schemi di vita più in generale."
          proprietà[Salute]="la carta rappresenta la salute, sia fisica che psicologica, la spensieratezza, la possibilità di aprirsi a nuove strade, di fare nuove esperienze senza doversi preoccupare dei problemi che già abbiamo o che potrebbero sopravvenire."
          proprietà[Persone]="il Matto fa riferimento ad una persona anticonformista, che crede nei propri ideali, ma anche che utilizza la follia nelle sue scelte, come un imprenditore che ama il rischio, una persona geniale, una persona in grado di mostrarci quello che abbiamo davanti da un punto di vista diverso da quello da cui di solito lo osserviamo."
       else:
          proprietà[Dettagli]="l significato del Matto al negativo rappresenta comunque la follia, ma intesa in questo caso nella sua accezione più negativa. Follia come violenza, come irrazionalità che non porta a nulla, follia come pazzia nelle proprie scelte, blocco nel procedere della vita quotidiana, fuga dalla realtà in un momento in cui bisognerebbe rimanere ben saldi alla stessa.\nIl Matto al negativo può indicare le manie, le ossessioni e, non ultime, le dipendenze, che potrebbero portare ad azioni anche molto negative nei confronti di sé stessi o delle persone che circondano.\nI problemi da risolvere non vengono affrontati con la giusta razionalità ma, anzi, vengono gestiti in modo nettamente inadeguato a quello che si vuole raggiungere: l’alcool, la droga, il gioco d’azzardo possono essere alcune delle conseguenze di queste scelte.\nC’è una ricerca della libertà, ma questa non viene cercata nel modo corretto e senza rendersene conto si rischia di finire da una situazione difficile ad un’altra da cui è ancora più difficile uscire.\nIn certi casi, questo potrebbe rappresentare la presenza di un forte condizionamento dall’esterno che ci porta a compiere scelte irrazionali e non corrette per noi.\nPuò indicare anche l’inconcludenza, il fissarsi su problemi che non hanno nessun senso e la cui soluzione non porta ad una risoluzione del problema che ci siamo posti.\nNelle situazioni più gravi, indica la pazzia vera e propria e può essere legato ad una patologia mentale."
          proprietà[Amore]="generalmente indica un amore che non viene corrisposto, o una mancanza di dialogo, o delle tensioni, o un tradimento; tutti eventi caratteristici che possono avere come risultato un comportamento folle e irrazionale, inconcludente per diversi motivi e che, anzi, rischia di peggiorare la situazione. Può rappresentare anche la ricerca della solitudine e la voglia di evadere dalla relazione che stiamo vivendo."
          proprietà[Lavoro_e_denaro]="dal punto di vista professionale, indica in generale l’inconcludenza, scelte non ragionate che hanno avuto dei risultati negativi, viaggi che non sono serviti, la voglia di evadere da una situazione che, tuttavia, dovrebbe essere gestita con tutte le nostre forze."
          proprietà[Salute]="indica generalmente la presenza di problemi della mente che dovremmo risolvere al più presto, conoscendo meglio noi stessi. Può rappresentare l’ansia, la nostalgia, la depressione, la presenza di un trauma irrisolto come un lutto non elaborato."
          proprietà[Persone]="indica una persona molto mutevole, falsa, nociva, che cambia idea molto velocemente e il cui operato potrebbe provocarci problemi. Può indicare persone violente, come i fuorilegge."
    else:
         print("Errore")
         
    return(proprietà[ambito])     
         
def immagine(arcano, senso):
    if arcano == "Il Bagatto":
       image1=''' 
------------------------------------------------------------- \n
\         h+                                                \ \n
\         +h`                          `.---..`             \ \n
\         .y+                        -/yhhhdNMMNy.          \ \n
\          oy                      -::---:--mMMMMMs         \ \n
\          -y:                   -/:oo+::--oNMMMMMMs        \ \n
\           yy                   --:sd/:.:hhhhmMMMMd        \ \n
\         `:+y:                `-........yMoo/NMMMMy`       \ \n
\        `:+/yh--.             ..::o:.....mysmMMMNhdmmMNd-  \ \n
\        `/++/sy/-:-             +/-......hMdh:y: dMMMMMMMo \ \n
\         -o+o/d...:      `dys`  -h/-:...:mMh..:` /MMMMMMMMs\ \n
\         `+:+/y/..--     -Ny+..-hMmNmmNNNy+-...:.`NMMMMMMMM\ \n
\          .:/Nh/--/.      `/hMMMMNmyo/+-........:+dhyyhssyd\ \n
\            :dhs.:/:         `` ```-::y/........-/++++++++y\ \n
\             `h/oooyo`         ://+++++-.......yy++++++++os\ \n
\              +h/sydhs.       o+++++++o......+dyo++++++++ss\ \n
\              .o:ohhyys-     sy+++++++msoo+osmhh+++++++++ss\ \n
\              oysydhhy+/   `+so+++++++Nsdhhhhsys+++++++++yo\ \n
\              +Nymhddsoo` `ys/o++++++omhhsydsoy+++++++++sss\ \n
\              -MmddNhys++.sooso++++++sshosssysy+++++++++s+o\ \n
\              -MmhdMddy+s+++yy+++++++sohoshohho+++/+++++yos\ \n
\              /NNmNNddsoodysss+++++++ysoshyysh+++++o+++sys+\ \n
\              sNNNNNNyodsmshoy+++++++y+sssssoh++++o+/++yyoo\ \n
\              yNNNNNNysyydhhos+++++++yossoshsh++++++//+yso:\ \n
\              smNMNNMdyydhyyoo+++++++syhssoosh+++o+++++ysso\ \n
\              :NmMMNNhsyysssos+++++++oyssyyssy+++++++++o+oo\ \n
------------------------------------------------------------- \n
|||||  ___      _          _    __     __     _         ||||| \n
|||||   |  |_| |_   |\/|  /_\  |  _ | |   |  /_\  |\ |  ||||| \n
|||||   |  | | |_   |  | /   \ |__| | |__ | /   \ | \|  ||||| \n
|||||                                                   ||||| \n
-------------------------------------------------------------'''     
          
    elif arcano == "La Papessa":
       image1='''
------------------------------------------------------------- \n
\yyyyyyyyy.....yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/+-/-yyyyyyyyy\ \n
\yyyyyyyyys.....sMMMMMMmNNMMMMMMMMMMMNmdNMMMMMN+:--:hyyyyyyy\ \n
\yyyyyyyyys.....oMMMMMNho-.+ms-`.oNy::shhNMMMMd     yyyyyyyy\ \n
\yyyyyyyyys.....+MMMMMMMMN+ `     ..yNMMMMMMMMy     syyyyyyy\ \n
\yyyyyyyyyo.....+MMMMMMMMMMs       dMMMMMMMMMMs     syyyyyyy\ \n
\yyyyyyyyyo...../MMMMMMMMMMM/`-.../MMMMMMMMMMM+     syyyyyyy\ \n
\yyyyyyyyy+...../NMMMMMMMMMN-/mmmh`dMMMMMMMMMM/     syyyyyyy\ \n
\yyyyyyyyy+...../NMMMMMMMMMo oMNMd`-NMMMMMMMMN/     oyyyyyyy\ \n
\yyyyyyyyy+...../NMMMMMMMMy  `hmd:  :NMMMMMMMN:     oyyyyyyy\ \n
\yyyyyyyyy/.....:mMMMMMMNo   `dmm/   sNMMMMMMm: `   +yyyyyyy\ \n
\yyyyyyyyy/.```.:mMMMMMh.     `.`    -/NMMMMMd-:hhy.oyyyyyyy\ \n
\yyyyyyyyy/.....-dMMMMN`       +    .  :NMMMMd..ssd:+yyyyyyy\ \n
\yyyyyyyyy:.```.-dMMMM+      --m--      +MMMMh`     +yyyyyyy\ \n
\yyyyyyyyy:.....-dMMMM`      --m--      -MMMMh      +yyyyyyy\ \n
\yyyyyyyyy:......hMMMh         /        -MMMMy      +yyyyyyy\ \n
\yyyyyyyyy-......hMMM/                  `MMMNs      /yyyyyyy\ \n
\yyyyyyyyy-......yMMM`     ```           mMMNs      /yyyyyyy\ \n
\yyyyyyyyy-......yMMm    :dsymdys/-/.    dMMmo      /yyyyyyy\ \n
\yyyyyyyyy.......sNMh    /MMMMMMNNNMh    hMMmo      /yyyyyyy\ \n
\yyyyyyyyy.......sNMh    `hmNMMNhyy/-    +MMd+      :yyyyyyy\ \n
\yyyyyyyys.......oNMN.     .-/+-         :MMd/      :yyyyyyy\ \n
\yyyyyyyys.......oNMMy.                  :MMd/      :yyyyyyy\ \n
\yyyyyyyys.......omMmh/                  .MMh:      -yyyyyyy\ \n
\yyyyyyyyo.......omMyy/                  .MMh-      -yyyyyyy\ \n
\yyyyyyyy+.......+mMyy+                   NMd/``  ``/yyyyyyy\ \n
------------------------------------------------------------- \n
|||||         __         _   _     _  _  ___  _  _   _  ||||| \n
|||||  |_| | |  _ |_|   |_| |_| | |_ |_   |  |_ |_  |_  ||||| \n
|||||  | | | |__| | |   |   | \ | |_  _|  |  |_  _|  _| ||||| \n
|||||                                                   ||||| \n
-------------------------------------------------------------'''           
      
          
    elif arcano == "La Imperatrice":
       image1='''
------------------------------------------------------------- \n
\             /:...//////////////////////.  .//             \ \n
\             /`   -///////:.hh-:////////    //             \ \n
\             /`   -//sNso: :MN` .:oh+///`   //             \ \n
\             /    .///yMMh+NMMN+mmMh///:    //             \ \n
\             /`   .///-oMMMMMMMNMMy////:    //             \ \n
\             /`   .//.  hhhNMMNyhN/`-///    //             \ \n
\             /`   .:`  .y -dMms-`+/ ``:/    //             \ \n
\             /`   `    y.-hhNNNm+`h   `.    -:             \ \n
\             /`       +/ .NNdmMM: o/      :/ .             \ \n
\             /`      :y`  smydNy   s:    +NNNN+            \ \n
\             /`     :o`   /hMMMh   `o/  `-NNNN-            \ \n
\             /`    ++`.  oNMMMMN:-.` :o.`/M/M/             \ \n
\             /`   /yohm-/yMMMMMNMNmddysh.mh :/             \ \n
\             -`.  mMMMMhNmMMMNMNMMMMMMMdhN. .:             \ \n
\             ..   mMMMNNmMMMMMMMMMMMMMNyM+     .           \ \n
\           .      sMNMMMMMMMMMMMMMMMdNsmd`       .         \ \n
\         .        `s+MMMMMMMdMMMMMMMh+yM/          .       \ \n
\       .           `+NMMMMMMMMMMMMMMh/Mo             .     \ \n
\       ,...-----..`  /NMMMMMMNNMMMNy.mMosyyo`         .    \ \n
\  .+hmNMmmMMMMMMMNmh+.-/ymmmNNsdys+/yMMMMMMo/          .   \ \n
\-smmMMMMMMMMMMMMMMMMMNs-` ``..`   :mMNdMNh: :           .  \ \n
\dMmmMMMMMMMMMMMMMMMMMMMMdo.      .omMy+d-   /           .  \ \n
\MMMMMMMMMMMMmMMMMMMMMMMMMN.       sMy-h.    s`          .  \ \n
\MMMMMMMMMMMMMMMMMMMMMMMMN+       `Nh .`     s/           . \ \n
\MMMMMMMMMMMMMMMMMMMMMMMm:        oN.  ``   -h:          .  \ \n
------------------------------------------------------------- \n
\\\\\\\\   ___      _    _       _   _   _  _   _    \\\\\\\\ \n
\\\\\\\\    |  |_| |_   |_ |\/| |_| |_| |_ |_  |_    \\\\\\\\ \n
\\\\\\\\    |  | | |_   |_ |  | |   | \ |_  _|  _|   \\\\\\\\ \n
\\\\\\\\                                             \\\\\\\\ \n
-------------------------------------------------------------'''          
          
    elif arcano == "Lo Imperatore":
       image1='''
------------------------------------------------------------- \n
\                  sNMNo--..--..--.-----:smNy               \ \n
\                  dMMMMMMm`sN:`hd`dMMMMMMMMd               \ \n
\                  -NMMMNMN  `  `` yMMMMMMMm.               \ \n
\                   :MMMMMM-  ````.hMMMMMMm.                \ \n
\                 `  NMMMMMy ...`--MMMMMMMh                 \ \n
\               `//:`mMMNNy``dhsdN`ymMMMMMh                 \ \n
\              `-///:ymo--` .NMMMM: .:yNMMy                 \ \n
\              .:://-+.      sMMMN-    -mMy                 \ \n
\                 :/ :       `mMMo      .my                 \ \n
\                 :/`:        ./+        -/                 \ \n
\                 :/-                     .-                \ \n
\                 -/`                     `::`              \ \n
\                 -/  `:yo                 --.              \ \n
\                 -++hMMy  `.`       `  ..-/o/`             \ \n
\                +MMMMMMh       `  ``  .dMMMMMm             \ \n
\                `dMMMMMy               `dMMMM+             \ \n
\                 +MMMMMd              `.sMMMM              \ \n
\                 +MMMMMm           .``.y+MMMN              \ \n
\                 +MMMMMN   ```    `-`:myoMMMN              \ \n
\                 +MMMMMM:  .-o   `.`.dh+mMMMm              \ \n
\                 +MMMMMMN+.```.--/.`:+sNMMMMd              \ \n
\                 +MMMMMMMMmdo`.yh: `dMMMMMMMd              \ \n
\                 +MMMMMMMMMM/`.NMh.`-dMMMMMMh              \ \n
\                .yMMMMMMMMMMo`-MMMNo--mMNMMMd/             \ \n
\              ssdMMMMMMMMMMMMsmMMMMMMmmMMMMMMMs            \ \n
------------------------------------------------------------- \n
||||||||  ___     _    _       _   _   _   __   _    |||||||| \n
||||||||   | |_| |_   |_ |\/| |_| |_  |_| |  | |_|   |||||||| \n
||||||||   | | | |_   |_ |  | |   |_  | | |__| | |   |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''          

          
    elif arcano == "Il Papa":
       image1='''
------------------------------------------------------------- \n
\                           -yddh/                          \ \n
\                          +Ndhhdms                         \ \n
\                          .:+os+/-`                        \ \n
\                          dMMMMMMN:                        \ \n
\                          :ho+/+so       -yyy-             \ \n
\                          -o:/./:s      -N/`hy             \ \n
\           -:-             +./-..-      -M+sd-             \ \n
\          `+/:             `::-::     ooomm/.              \ \n
\         --/++          ..``:----`````/+oN+/s.             \ \n
\         .+://`       .ymNd:.....-+mmhooNy+s/              \ \n
\          .--/`      -dMMMMNho+oymMMMMNhho:`               \ \n
\            :.:.    -mMMMMMMMMMMMMMNMMh`:                  \ \n
\            --.--.-oNMMMMMMMMMMMMMMMNN./No`                \ \n
\             /...+dMMMMMMMMMMMMMMMMNN+`mMMy.               \ \n
\             .:....yMMMMMMMMMMMMMMMN- .mdddd/              \ \n
\              .:-..+dNNMMMMMMMMMMMMo `:.```./`             \ \n
\                .syhhhdmMMMMMMMMMNM/`yho/-../.             \ \n
\                 hhdhhhdMMMMMMMMMMy smhhhhmhd              \ \n
\                 hhddhhdMMMMMMMMMN.:NNhhhddhh              \ \n
\                 yhddhhdMMMMMMMMM+`mMNhhhddhs              \ \n
\                 shddhhmMMMMMMMMh sMMMhhdhdh+              \ \n
\                 +hdhdhmMMMMMMMM/:NMMMddhdhh-              \ \n
\                 :hdhdhmMMMMMMMMMMMMMMdhdhhy`              \ \n
\                 `hhdhdNMMMMMMMMMMMMMMdddhh.               \ \n
\                  -hhdhNMMMMMMMMMMMMMMmhhh+                \ \n
------------------------------------------------------------- \n
||||||||         _  _   __   _        _        ___   |||||||| \n
||||||||  |_| | |_ |_| |  | |_| |_|  /_\  |\ |  |    |||||||| \n
||||||||  | | | |_ | \ |__| |   | | /   \ | \|  |    |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''             

          
    elif arcano == "Il Carro":
       image1='''
------------------------------------------------------------- \n
\                                                           \ \n
\                                                           \ \n
\        -o-+o/::-.                                         \ \n
\    .:shdhhhhmmhdyo/:-`                       `oyo:        \ \n
\  `+ssmmmmmmmhhhhhyy+-                        -ddyy        \ \n
\ -hmhhmmmmmmmmmdyhs:.                        ..smm+`       \ \n
\ .dshhyhhdmmmmmmmyd:`                  .-`  `hdhyhhdo-     \ \n
\ `/osdmddhmmmmmmmmd-             `----. yy- /mdyddmdmhh/`  \ \n
\   `  /hyddmdddmmmm..````........`  `----`+hdddhdmmmy/ydd/ \ \n
\ .o-  +hydmmmmmdhhhs/:::::::::::::::.       :/ddmmmdh .md- \ \n
\ /ymdohymmmmmmmmmmmmmds+/:-`                 `oddmmsh-hy`  \ \n
\ +hm+ddymmdmmmmmmmmmmmmmmmmmh+           `s+ydhhhhhysyds/  \ \n
\ -smhyhyydymmmmhmmmmmmmmmmmmmmh`         `mmhyhhdhdhyy.    \ \n
\+h+//dmhdmmmmmsmmmmmmmmmmmmmmmmh+`        mmmdddhyhydmh    \ \n
\+dy` :m/.--...:ymmmmmmmhdmmmmmmsmd-       hmmmddddhhhhd+   \ \n
\  :.  hmms+`     `/dyhhsmmmmmmdsmm+      `ymdydddyydddyy`  \ \n
\      `:.          .+hmhhmmmdhydhs+/:-.`-+/yhydmmhhmmdyhy- \ \n
\                   -hh+ddyhhyhdsd+``.-:+hyyymmhddyyhdhmmmh.\ \n
\                .+hm/  +dmshsmhyhh     -/:sohddhsyyyhdddhyy\ \n
\               `yd/` -sdo:+om+hoyy     `s-+:ys+hyyshs:/o :/\ \n
\               -+- +dmh-  /mo-o:-+      :os: .yo.sh.+yo`.s \ \n
\                  -dd.  .hmh-.  `        `+hs/o  :os/::o+  \ \n
\                  --`  oyo`                 .:/osyy+//:`   \ \n
\                                                           \ \n
\                                                           \ \n
------------------------------------------------------------- \n
||||||||  ___      _             _    __   __        |||||||| \n
||||||||   |  |_| |_    \    /  /_\  |  _ |  | |\ |  |||||||| \n
||||||||   |  | | |_     \/\/  /   \ |__| |__| | \|  |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''           
          
    elif arcano == "Gli Amanti":
       image1='''
------------------------------------------------------------- \n
\                     ..`                                   \ \n
\                   -MMMMd:                                 \ \n
\                   :MMMMMM:                                \ \n
\                   `yMMMM+`                                \ \n
\                    sMss-                                  \ \n
\                    mMms-            ..`                   \ \n
\                    mMMMN-          `hNNdo                 \ \n
\                    oMMMMy.        -mMMMMM-                \ \n
\                    `NMMNhmy:`     /mMMMd/                 \ \n
\                     .hMMd .+hds:`   /MMN-                 \ \n
\                  `omMMMM-  `.+Nd+.+mMMMm+                 \ \n
\                 :dMMMMMMd`   :MMMNMMMMMMd                 \ \n
\                +NMMMMMMMMo   -MNMMMMMMMM/                 \ \n
\                sMMMMMMMMMMN-  `mMMMMMMMMy                 \ \n
\               -NMMMMMMMMMMMd   -ssMMMMMM.                 \ \n
\             `yMMMMMMMMMMMMMo    /MMMMMN.                  \ \n
\               /MMMMMMMMMMMMMMN-``.sMMMMMMs                \ \n
\              .NMMMMMMMMMMMMMMmhdmMMMMMMMM.                \ \n
\              +NMMMMMMMMMMMMMMMMNNmNMMMMMMs                \ \n
\               `-:+osNMMNdso/sMMM+.`:/hMMMd.               \ \n
\                    `yMMh-    .MMMh    oMMMo               \ \n
\                   -mmoMo      dMMM.   +MMM:     ```       \ \n
\               `oym+  dh      oMMMs   /MMM.`-/oydmN        \ \n
\               -mN.  .NM:     .MMMN`  :MMMmNMMMMMMN.       \ \n
\               hy    +sNo` `+sNMNM/  `dMNmdyso/:sm.        \ \n
------------------------------------------------------------- \n
||||||||    ___      _          __        _  _   _   |||||||| \n
||||||||     |  |_| |_     |   |  | \  / |_ |_| |_   |||||||| \n
||||||||     |  | | |_     |__ |__|  \/  |_ | \  _|  |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------''' 

          
    elif arcano == "La Giustizia":
       image1='''
------------------------------------------------------------- \n
\                                       `omh-               \ \n
\                         .+so/.       .mNmo                \ \n
\                         dyyyyh`     -mN-s                 \ \n
\                        /     /     .mMo`s                 \ \n
\                        yMNNNd-    .dMd` o                 \ \n
\                        yMMMd/--:ohmdo`  +                 \ \n
\                      .:hMMMNNNNMmh/`   :h`                \ \n
\                   .hNMMMMMMMMN:.`.  .odmy/` `.            \ \n
\                   yMMMMMMMMMMM` -d:::-...:::oy            \ \n
\                  `mMhMMMMMMMMs  : -         : -           \ \n
\                  +MN.hMMMMMMM- .  .        .`  .          \ \n
\                  hMo oMMMMMMm`.syyso      .syyss          \ \n
\                `yMy  yMMMMMMN``hMMN+      `hMMN+          \ \n
\               `mMs `dMMMMMMMM:  ``          ``            \ \n
\          hh` `hN/  dMMMMMMMMMd                            \ \n
\          `+momd./ -MMMMMMMMMMM:                           \ \n
\            oNNo+. :MMMMMMMMMMMd                           \ \n
\            -+mMh. .MMMMMMMMMMMM-                          \ \n
\           ./..hMm+`mMMMMMMMMMMM+                          \ \n
\               `+NMhyMMMMMMMMMMMo                          \ \n
\                 .yNhsNMMMMMMMMMo                          \ \n
\                   :y -dMMMMMMMM+                          \ \n
\                    +y.`oNMMMMMM:                          \ \n
\                   `mMNo`-mMMMMM-                          \ \n
\                   sMMMMNo-mMMMM-                          \ \n
------------------------------------------------------------- \n
||||||||    ___      _     ___     _ ___    __  _    |||||||| \n
||||||||     |  |_| |_      | |  ||_  |  | |   |_    |||||||| \n
||||||||     |  | | |_    |_| |__| _| |  | |__ |_    |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''          

          
    elif arcano == "Lo Eremita":
       image1='''
------------------------------------------------------------- \n
\                                                           \ \n
\                  ++s`                                     \ \n
\                 :syy-           `                         \ \n
\                    y-     `/sdmNy                         \ \n
\                     y-  ymNMMMMMN`                        \ \n
\                     `y. :M+yMMMMMs                        \ \n
\                      h. .-+MMMMMMo+:-                     \ \n
\                      `h`  hMMMMMMMMMMms`                  \ \n
\                       .h`/mmhMMMMMMMMMMN:                 \ \n
\                    :.`  -h:yNMMNNNNNNNNmMMy               \ \n
\               ./sNMMMMMMNmmNMMMMNmMMMMMdNd                \ \n
\             `NMMMMmooo+/MmmNNmNmmmMMMMMNoM:               \ \n
\             sNMMMm`     sNdmMMMMMMmNMMMN-Ms               \ \n
\             /NMMM/    `odMMMMmssyMNmmmMM.My               \ \n
\            .oMMmh:    /MMMMMd+  oMMMMMm::Md               \ \n
\            :o h. d    yMMMMM.o/-NMMMMMm oMN               \ \n
\            :o h` d    /NyNmm` sNMMMMMMd dMM/              \ \n
\            :o h` d     `oMN:  yNmMMMMMd dMMN`             \ \n
\            :o h` d     oMMN  hMMmMMMMMN oMMd:             \ \n
\            -s/y+/s     -:-. yMMMNmNMMMM.`h:               \ \n
\                            :MMMMMNmMMMMo                  \ \n
\                            mMMMMMMNmmMMm                  \ \n
\                           +MMMMMMMMNmNMM/                 \ \n
\                           mMMMMMMMMMNmNMm`                \ \n
\                          .MMMMMMMMMMMmdNMs                \ \n
------------------------------------------------------------- \n
||||||||      ___    _         _  _         ___      |||||||| \n
||||||||       | |_||_    |_| |_ |_| |\/| |  |       |||||||| \n
||||||||       | | ||_    | | |_ | \ |  | |  |       |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''         

          
    elif arcano == "La Ruota":
       image1='''
------------------------------------------------------------- \n
\                          :o+`                             \ \n
\                          -so`                             \ \n
\                        `-/oo+:`   +oo`                    \ \n
\                  `..-+oosoooo+/-..`yo                     \ \n
\                -yNNy+oyydNNNdsssshdd-                     \ \n
\               oNMMs:`   +osss/+oo+-`                      \ \n
\              dMMMM.  .--soooo`                            \ \n
\              :odmm. `ooooyoo+                             \ \n
\              .-/.`  `/dysysody:                           \ \n
\              `:+.  -dNNo./sosmMh.                         \ \n
\               .o/ .mMNN:  ++-/hMm.                        \ \n
\                -  sMMohNo -o-yNNMh                        \ \n
\                  .NMM``oNy -yNy:MM.                       \ \n
\                  .MMh  `oM/yNh` MM:                       \ \n
\                  -MMs   .NMMm`  NM+                       \ \n
\                  -MM+  `/MMMM-  mM+                       \ \n
\                  `MMs.+hdmNNsdy/NM/                       \ \n
\                   yMMmm/.`mh .hNMM-                       \ \n
\                   .MM/   .MN   sMN`                       \ \n
\                    oMd   `my  `hMs                        \ \n
\                     sMs  `MN` yNh.                        \ \n
\                `.`   oMs``mh:hNsso::`                     \ \n
\              `+oooo:/ydmdNMNNyooyoss+/-                   \ \n
\                /+sosooooosssosooo::oo+:/                  \ \n
\                  `:+//- `.:/:--`   `:/:`                  \ \n
------------------------------------------------------------- \n
||||||||        ___    _                _  _         |||||||| \n
||||||||         | |_||_    \    / |_| |_ |_ |       |||||||| \n
||||||||         | | ||_     \/\/  | | |_ |_ |__     |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''         

          
    elif arcano == "La Forza":
       image1='''
------------------------------------------------------------- \n
\                          `..``                            \ \n
\                        `..--/-...                         \ \n
\                     `....-mmNm/..                         \ \n
\                    `...../MMMh-.                          \ \n
\                  `....-/odMMs-.`                          \ \n
\               `......:hMMMMMNdo                           \ \n
\              ......-so+mNNNMMMM/                          \ \n
\              .....:dN:-::::sdsdN:                         \ \n
\             `....sNh/-------/yyNN.                        \ \n
\             ....sho-------/hdddhdm+`                      \ \n
\            `...sy--------odmdddddmMd+                     \ \n
\             ..-o--------:hNMdhddddMNdo                    \ \n
\             ..-hdo------yddh+o++o+hMhd.                   \ \n
\            `..oMMMd:--.:yddh++os+++dN+                    \ \n
\           `.oNMMMMh/--/sdddy+syoodmMy                     \ \n
\             `mMMMMMMN::++sddddoosddddy                    \ \n
\             `dMhNMMN+--/++oyddddddds+-                    \ \n
\             `:/-yMN/---/++++yddddho+/`                    \ \n
\             `--:mMd---`./++++yddh+++/`                    \ \n
\             `--yMMh--.  `-++++yo++++/`                    \ \n
\             `.NMN/--`   `/++++/++++-                      \ \n
\              `-MN+---.    `:/++++++/`                     \ \n
\             .-yN/-----.     -//++++:                      \ \n
\             `+Ms-----`        `-+++-                      \ \n
\             +MN. .---...`      :+++:                      \ \n
\             oy:    ```..-      :///:                      \ \n
------------------------------------------------------------- \n
|||||||| ___    _    _ ___  _   _        __ ___      |||||||| \n
||||||||  | |_||_   |_  |  |_| |_  |\ | |  _ |  |_|  |||||||| \n
||||||||  | | ||_    _| |  | \ |_  | \| |__| |  | |  |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''           

          
    elif arcano == "Lo Appeso":
       image1='''
------------------------------------------------------------- \n                                           
\                :h+-:-:::--:::h+::://:::::::-              \ \n
\                .so////+++/++dyo+++++oooooo+               \ \n
\                -s`          oyss`       :h:               \ \n
\                y+           +dMs        :h.               \ \n
\                h.           +hs         `h                \ \n
\                :y            :mo         `h               \ \n
\                :s            oMm         .h`              \ \n
\                :s            sMN         `h+              \ \n
\                /s            mMN  :h`     ho              \ \n
\                +h.    .syyyyoNMMsyNy      ys              \ \n
\                .h-    /MMMMmhNMMmh/      `hh              \ \n
\                 h.     sMMNmddNNN+       .hh-             \ \n
\                 h-     `sNsMmdNoNo       .hh+             \ \n
\                 d-       +dNdhNhy         hh:             \ \n
\                -d.       `hmmyNmo         sh:             \ \n
\                `d`     `.+NMmyMMm..`     `hh-             \ \n
\                 y   `/sdmMmMmhMMMmmhy/`  -hh-             \ \n
\                :h   oNNMNNmMmhNMMNNNMm/  -hh-             \ \n
\                yh   `:ohmmmhmmmdNmhs/`   -hy:             \ \n
\                hy         `:NMm:.        .hy+             \ \n
\                /+          sNNNy         `/:-             \ \n
\                ..`         odNms         `...             \ \n
\                ...         .syy-         ..--             \ \n
\                ...`         `s:         `...:             \ \n
\                ...`          `          .....             \ \n
------------------------------------------------------------- \n
||||||||       _         __   _  _          _        |||||||| \n
|||||||| |_|  /_\  |\ | |  _ |_ | \  |\/|  /_\  |\ | |||||||| \n
|||||||| | | /   \ | \| |__| |_ |_/  |  | /   \ | \| |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''          

          
    elif arcano == "La Morte":
       image1='''
------------------------------------------------------------- \n
\                         /@@@@@@@(                         \ \n
\                   %@@@@@*       ,@@@@@@                   \ \n
\               ,@.       (@@.@@       @@                   \ \n
\             (          &@/@ @,@@@    @                    \ \n
\                        %@@@&@*@&    &(                    \ \n
\                      @@@@@@%#@(     @                     \ \n
\                    @@@@@@&@@@@      @                     \ \n
\                      ,@@@.@&@@(    .@                     \ \n
\                      @@@@(@@@@     ##                     \ \n
\                      @.@%/,@@.     &.                     \ \n
\                      @@.@@@@@@@@   @                      \ \n
\                     @@@@@@(@@@@@@@@@@@                    \ \n
\                     ,@@@@@@@@@@@   @                      \ \n
\                      @@@@&@@@@@    @,                     \ \n
\                      @@@@.@/@@@#   (@                     \ \n
\                      @@(@&@@#@@@&   @                     \ \n
\                     #@@.@@&@@@(@@@  @&                    \ \n
\                     @/@.@@ @@@@@#    @                    \ \n
\                   &@@ @ @@.@@@@@@@   &@                   \ \n
\                  @@@@%@ @@@,@@@@@@@   @@                  \ \n
\               ,@@@@@ @@ @@@ @@@@@@@(   @@                 \ \n
\                @@@@%@@@ @@@% @@@@@      @@         &      \ \n
\                .@@@@@@@.#@@@ @@@@@@      (@@      @       \ \n
\                @@@@@@@@@ @@@@ @@@@@@@      .@@@@@,        \ \n
------------------------------------------------------------- \n
||||||||      ___      _     _    _   _  ___         |||||||| \n
||||||||       |  |_| |_    |  \ |_  /_\  |  |_|     |||||||| \n
||||||||       |  | | |_    |_ / |_ /   \ |  | |     |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''          

          
    elif arcano == "La Temperanza":
       image1='''
------------------------------------------------------------- \n
\MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\ \n
\MMMMMMMMMMMMMMMMNo-sMMMMMMMMMMMMMMMMMm--yNMMMMMMMMMMMMMMMMM\ \n
\MMMMMMMMMMMMMMMy. `hMMMMMMMMMNMMMMMMMN:  -hMMMMMMMMMMMMMMMM\ \n
\MMMMMMMMMMMMMm/   yMMMMNmy/o+:hNMMMMMMN-  `oNMMMMMMMMMMMMMM\ \n
\MMMMMMMMMMMMh.   +MMMMN+:---:-:/mMMMMMMm.   /NMMMMMMMMMMMMM\ \n
\MMMMMMMMMMMy`   .NMMMMMo-+----+:mMMMMMMMh    :mMMMMMMMMMMMM\ \n
\MMMMMMMMMMs     yMMMMMMmdy--:-+sMMMMMMMMM:    .mMMMMMMMMMMM\ \n
\MMMMMMMMMy     .MMMMMMNmNMh--+NMMNNMMMMMMd     .mMMMMMMMMMM\ \n
\MMMMMMMMd`     /mMMMMd/-/so---yys-:omMMMMM-     -NMMMMMMMMM\ \n
\MMMMMMMN.      :-sdh/--  .......   -:+dmd/:      +MMMMMMMMM\ \n
\MMMMMMMo      .......:      `-.  .  `-....:       dMMMMMMMM\ \n
\MMMMMMN`      -.....:  -  -:-.-- /-   .--./       :MMMMMMMM\ \n
\MMMMMMy       -....:`  /`    /oo:.Nh-::-`:/        mMMMMMMM\ \n
\MMMMMM:       -....:   h-   -sooo+//::.: `+        sMMMMMMM\ \n
\MMMMMM`        :..-+.  +m+..o/-::s+hoo - `:        /MMMMMMM\ \n
\MMMMMN         .:/NN+   s:-/s..-:sMMm: -`:         -MMMMMMM\ \n
\MMMMMm          :NMMh`-:+s+oo`.::`yMN: ::`         -MMMMMMM\ \n
\MMMMMN           /NMN.::ooos+.: : `hM/-+`          :MMMMMMM\ \n
\MMMMMM`           /Ns-:-+++-`.. :  `Nd:`           oMMMMMMM\ \n
\MMMMMM/            -+:-+/:: `: `-   so`            dMMMMMMM\ \n
\MMMMMMm`.           `/++o`. -  :   .-           `.-MMMMMMMM\ \n
\MMMMMMMyo            `-... `  `:  -.            ++mMMMMMMMM\ \n
\MMMMMMMMM+ ..          .-     :``-`          : `NMMMMMMMMMM\ \n
\MMMMMMMMMN- o  /`       `-`   `-.        .  -+ oMMMMMMMMMMM\ \n
\MMMMMMMMMMm:oo .o   -     -- `-`    .   .+ `d.oMMMMMMMMMMMM\ \n
------------------------------------------------------------- \n
||||||||   ___  _       _  _  _    _         __  _   |||||||| \n
||||||||    |  |_ |\/| |_||_ |_|  /_\  |\ | |   |_   |||||||| \n
||||||||    |  |_ |  | |  |_ | \ /   \ | \| |__ |_   |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''            

          
    elif arcano == "Il Diavolo":
       image1='''
------------------------------------------------------------- \n
\    /&&@@@@ @@@ &.@@@@               *@ &&@ @@,@@@@@\      \ \n
\  (%@@#@@#& (@@&%@@*@@@            @@@.@@@@%(\%@@#@@#)     \ \n   
\    \@@#@@#    *@@@@% @@@          @@@@ @@@    @#@@#&      \ \n 
\     \#@@#      &@@@@ @(@@        @@@.&,& @     #@@#       \ \n
\      \|/         (@@@@ @.@@@   @@@@(@(@ /@      \|/       \ \n
\                  /@@@@@@.@@@@@@@@(/@ @@@@                 \ \n
\                   .@@  @@@&@@@@&@@&@@@@                   \ \n
\                 ,@@@& @@ &&&@..@@.@(@@@@                  \ \n
\                .@@@%@@@   /\/\   @@@@@@@@                 \ \n
\.* @ &      &@@@#@@@@@@.  <    >  @@@@ ,@@@@@@&@ @@@@      \ \n
\ #&@@@ @@@*,@@@@%@@@&#@@    \/    .@&#@ &&@@*.&@@& @@@%@   \ \n
\   %@%@@@@@@@@@#* @*@ (@.%,, #.&,@@@/*@*. @&@@&&**@@@@(@   \ \n
\        . ( ,  /*@@@     @,%@*@@#@     ( #&@    .*..       \ \n
\                *@@&@&    @@@(@@@     (/@@&                \ \n
\                @ @@//@@  @@@@@   @@ * @                   \ \n
\                 @@@@.@@@@@@@ @.@@&@@@@.@/                 \ \n
\                  @@&@@@@@/@@ @%@@@@,@&@                   \ \n
\                    @*.%@@@@@%&@ @@@&@                     \ \n
\                      @*@@( )@@( )@.#                      \ \n
\                       *@@%@@||@(@@@                       \ \n
\                       .@@@@@||@@@@                        \ \n
\                         @@@_||_&@%                        \ \n
\                          @@____#&                         \ \n
\                          @@@@@@@&                         \ \n
\                          *@@@&*.                          \ \n
------------------------------------------------------------- \n
||||||||      ___      _     _    _                  |||||||| \n
||||||||       |  |_| |_    |  \ |_  \  / | |        |||||||| \n
||||||||       |  | | |_    |_ / |_   \/  | |__      |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''            

          
    elif arcano == "La Torre":
       image1='''
------------------------------------------------------------- \n
\  | |             (|||||||||||||||)      _//|\\            \ \n
\  | |              (//////)__(/////)____(//////)      ___(/\ \n
\   \ \              (|||||)##|\\\\\|####(/////)     _(|||||\ \n
\    \ \              (|||||)##########(//////)    _(///////\ \n
\     |  \             (|||) #########  /////)   _(|||||||||\ \n
\    / /\ \___         |##   #########  ////) __(///////////\ \n
\   / /  \___ \        |##   #########   ##| (||||||||||||||\ \n
\  //        \ \_      |###################|/////////////)  \ \n
\  ||         |_ \_____|__###############__|____||||||||)   \ \n
\  /            \|@@@@@@@||#############||@@@@@@@|/////)    \ \n
\                |@@@@@@@||#############||@@@@@@@|||||)     \ \n
\                |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|///)      \ \n
\                |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|||)       \ \n
\                |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|          \ \n
\                |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|          \ \n
\                |###########:::::::::###########|          \ \n
\                |@@@@@@@@@@@|||||||||@@@@@@@@@@@|          \ \n
\                |@@@@@@@@@@@|||||||||@@@@@@@@@@@|          \ \n
\                |@@@@@@@@@@@|||||||||@@@@@@@@@@@|          \ \n
\                |@@@@@@@@@@@|||||||||@@@@@@@@@@@|          \ \n
\                |###############################|          \ \n
\                #################################          \ \n
\              /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\         \ \n
\            /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\       \ \n
\          /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\     \ \n
------------------------------------------------------------- \n
||||||||     ___      _    ___  __          _  _     |||||||| \n
||||||||      |  |_| |_     |  |  | \    / |_ |_|    |||||||| \n
||||||||      |  | | |_     |  |__|  \/\/  |_ | \    |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''          

          
    elif arcano == "La Stella":
       image1='''
------------------------------------------------------------- \n
\                                                           \ \n 
\                                                           \ \n
\                            |                              \ \n
\                          -@@@-                            \ \n
\                            |           (@                 \ \n
\                                        @@.                \ \n
\                                       @@@@*               \ \n
\                                    ,@@@@@@@@(             \ \n
\                      &@         (@@@@@@@@@@@@@@&          \ \n
\              @       @@             /@@@@@@@              \ \n
\           .@@@@@.   @@@@              @@@@                \ \n
\              @     &@@@@@              @@                 \ \n
\                   @@@@@@@@             .#                 \ \n
\                 @@@@@@@@@@@@                              \ \n
\             *@@@@@@@@@@@@@@@@@@(                          \ \n
\          .@@@@@@@@@@@@@@@@@@@@@@@@.                       \ \n
\               /@@@@@@@@@@@@@@#            %               \ \n
\                  @@@@@@@@@@            __#@*__            \ \n
\         )          @@@@@@,               @@&              \ \n
\       -@@*-         @@@@.                 &               \ \n
\         (           (@@&                                  \ \n
\                      @@                                   \ \n
\                      ,/                                   \ \n
\                                                           \ \n
\                                                           \ \n
------------------------------------------------------------- \n
||||||||        ___      _     _  ___  _    _        |||||||| \n
||||||||         |  |_| |_    |_   |  /_\  |_|       |||||||| \n
||||||||         |  | | |_     _|  | /   \ | \       |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''           

          
    elif arcano == "La Luna":
       image1='''
------------------------------------------------------------- \n
\                  &@@@@@%                                  \ \n
\                &@@@%                                      \ \n
\             @@@@@                                         \ \n
\          @@@@@@@                                          \ \n
\        @@@@@@@                                            \ \n
\      @@@@@@@                                              \ \n
\    @@@@@@@@                                               \ \n
\   @@@@@@@@                                                \ \n
\  @@@@@@@@                                                 \ \n
\ @@@@@@@@@                                                 \ \n
\ @@@@@@@@                                                  \ \n
\(@@@@@@@@/                                                 \ \n
\&@@@@@@@@@                                                 \ \n
\ @@@@@@@@@                                                 \ \n
\ @@@@@@@@@@                                               %\ \n
\  @@@@@@@@@@                                             @@\ \n
\  @@@@@@@@@@@@                                         @@@@\ \n
\   &@@@@@@@@@@@@                                     @@@@@ \ \n
\     @@@@@@@@@@@@@                                @@@@@@@  \ \n
\      @@@@@@@@@@@@@@@@                        &@@@@@@@@    \ \n
\        &@@@@@@@@@@@@@@@@@@@            &@@@@@@@@@@@@      \ \n
\           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        \ \n
\              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           \ \n
\                   @@@@@@@@@@@@@@@@@@@@@@@@                \ \n
\                        @@@@@@@@@@@@@@                     \ \n
------------------------------------------------------------- \n
||||||||      ___      _          __   __            |||||||| \n
||||||||       |  |_| |_    |\/| |  | |  | |\ |      |||||||| \n
||||||||       |  | | |_    |  | |__| |__| | \|      |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''          

          
    elif arcano == "Il Sole":
       image1='''
------------------------------------------------------------- \n
\                 @@           @          @@                \ \n  
\                  @&@       @@         @@@                 \ \n
\                  @@.       &@@     @.@.@                  \ \n
\                 .@.@     @.@.@   *..%                     \ \n
\          @@@     @..@..@@ @.@.@   @...@     @@@           \ \n
\            @@.&@   @/....@..@..@ @....@  @.@@.            \ \n
\    ,        @..#..&@@.@&.........@@.*@@..@.@           @  \ \n
\ @  @.@@       @..@@..................@/..@   &@.....@.@   \ \n
\      @#.........@.........::::::.......@@@@@..,.@         \ \n
\        @@@@@@..@........::::::::::.......@@@..&,          \ \n
\            (@@@.......:::::::::::::......@@@@             \ \n
\   %@@&........@......:::::::::::::::................@@@.  \ \n
\        @@@@*..@.......:::::::::::::......%..@@@(          \ \n
\          @....@@........:::::::::........&.@*             \ \n
\        @.@...@@@..........:::::.......%..@.......@@       \ \n
\   @/.@@@@..@   @..@@..................@...@*.*@@@@@..@    \ \n
\  @@         @..@..#@.#@..........@@@@...@.@        @,.@@  \ \n
\            @.@.@. @....@ @.....(.@.@   @@.&.@             \ \n
\           @(@      @...  /....@@.....@     @@@@           \ \n
\         %*        @...@   @..*    .@.@@        @          \ \n
\                 @..@.@     (.@      @@.%                  \ \n
\                 .@@        @@       @@.@                  \ \n
\                 @@          @         @@@@                \ \n
\                                                           \ \n
------------------------------------------------------------- \n
||||||||        ___      _     _                     |||||||| \n
||||||||         |  |_| |_    |_  |  | |\ |          |||||||| \n
||||||||         |  | | |_     _| |__| | \|          |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------''' 

          
    elif arcano == "Il Giudizio":
       image1='''
------------------------------------------------------------- \n
\@@@@@@@ -        @@                                        \ \n
\@@@@@ -            @@@/                                    \ \n
\@@@@ \       @@     @@@@@@@,       ,@@            ,        \ \n
\@@ \           @@@@@@@@@@@@@@@@.  @@@@@==@@@@@&#/#.        \ \n
\@ \                @@@@@@@@@@@@@@.%@@@@  ,@      ^#        \ \n
\|                       %@@@@@@@@@@@@@@@@@@                \ \n
\       \%@@@@@@@           *&@@@@@@@@@@                    \ \n
\        \/@@@@@@@     .*#@%@@@@@@@@@@*@.                   \ \n
\         /@@@@@@@@@@@@@@@@@@@@@@@@@@  @                    \ \n
\          @@@@@@@@@@@@@@@@@@@@@@@@  @.  &@&@@@&  #@        \ \n
\           @@@@@@@@@@@@@@@@@@@@@@ @.               @       \ \n
\   |@@@@@@& @@@@@@@@@@@@@@@@@@@@@    @@               &&   \ \n
\   @         .@@@@@@@@@@@@@@@,    #@   &                &@ \ \n
\  ,&               @@@@@@@/              &              @  \ \n
\ @                   @@@@@/               &              # \ \n
\ @ _   /                                   &              @\ \n
\   &                                       &        %    @ \ \n
\    &      @@,  @@@                       &#           @   \ \n
\  ,&                             &       &##         @     \ \n
\    @@@@  @@&&&@&@@&&&&&@@@@@@  %#       @@@      @        \ \n
\                 @&@@&&&&         \\\\@@@@@@@@@@@@@/       \ \n
\          @@@@   .@@@ ..   ,@@  @@@@@    @@@@#*@@@(        \ \n
\        @@@ % @@@@@@                @@@@@@ @@@@@@@@@@      \ \n
\      @@  .   @@@@@@@@@@        @ .@ @@@,@  % @@@@@@@@@    \ \n
------------------------------------------------------------- \n
||||||||    ___      __   __   _       _      ___    |||||||| \n
||||||||     | |  | |  \ | __ |_ |\/| |_ |\ |  |     |||||||| \n
||||||||   |_| |__| |__/ |__| |_ |  | |_ | \|  |     |||||||| \n
||||||||                                             |||||||| \n
-------------------------------------------------------------'''          

          
    elif arcano == "Il Mondo":
       image1='''
------------------------------------------------------------- \n
\                           (@@@@@@*                        \ \n
\                  @@@                  @@@@                \ \n
\             .@@@@@@@   ,  @&@@@@@%,@@@@&  %@@@            \ \n
\          @@@@   .@@@ ..   ,@@  @@@@@    @@@@#*@@@(        \ \n
\        @@@ % @@@@@@                @@@@@@ @@@@@@@@@@      \ \n
\      @@  .   @@@@@@@@@@        @ .@ @@@,@  % @@@@@@@@@    \ \n
\    @@ @ %@@@@@@@@@@@@@@@@    .       %  &%@@@@@@@@@@@@@&  \ \n
\   @@.& @@#@@@@@@@@@@@@@@@@@   .         @@@@@@@@@@@@@@, @ \ \n
\  @@&  @@@@@@@@@@@@@@@@@@@@@@        &,*@.@@@@@@@@@@@@@@@@@\ \n
\ @@   @,@@@@@@@@@@@@@@@@@@@@@@@.@  #@@@@@@@@@@@@@@@@@@@@% @\ \n
\@@   #@@@@@@@@@@@@@@@@@@@@@@@@@@@ /@@@@@@@@@@@@@@@@@@@@  @@\ \n
\@@@ .&@@,@@@@@@@@@@@@@@@@@@@@@@@@@@&*(.@@@@@@@@@@@@@@@@@%  \ \n
\@@@@@@#@@@@@@@@@@@@@@@@@@@@@&@@@&@@@@ @&@@@&@@@@@@@@@@@@@@(\ \n
\@@  #@@*@@@@@&@@@&@&@@@&@@@&@@&@@@@@@@ ,@@@@@@@@@@@@@@@@@@@\ \n
\@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @ @@@@@@@@@@@@@@\ \n
\@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%       /     ,@@@@@@@@@/\ \n
\ @@@,/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              @@@@@@@@@ \ \n
\  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ .&        ,@@@@@@@@@  \ \n
\   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#      @@@@@@@@@@@@   \ \n
\    ,@@@@*@ &&@@@@@/&@@@@@@@@@@@@@@@@&   (,@@@@@@@@@@@     \ \n
\      &@@ @ *  &@@@@@@@@@@@@@@@@@@@@@@   .@@@@@@@@@@       \ \n
\        .@ (.  %&@@@@@@@@@@@@@@@@@@@@#,@@@@@@@@@@@         \ \n
\           %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@            \ \n
\               @@@@@&                  @@@@                \ \n
\                     (@@@@@@@@@@@@@@%                      \ \n
------------------------------------------------------------- \n
||||||||    ___      _          __   __       __     |||||||| \n
||||||||     |  |_| |_   \    /|  | |__| |   |  \    |||||||| \n
||||||||     |  | | |_    \/\/ |__| | \  |__ |__/    |||||||| \n
||||||||                                             |||||||| \n
------------------------------------------------------------- '''         

          
    elif arcano == "Il Matto":
       image1='''
------------------------------------------------------------- \n
\                           @@@@@@@@                        \ \n
\          *,          @@@@@@@,@@@@@@.                      \ \n
\         @@@@@         @@@@*   , ,@                        \ \n
\        @/@@.,@@@@(    /@& @@@@  @@#                       \ \n
\       @@@@@@ .  @@@@@    @#@@@@@@@                        \ \n
\       @.   @@ &@    @@@@@ @@@@@ @ @@                      \ \n
\        @  @@@        # %%#(  %#% @ @@ %                   \ \n
\         &&/.            %%#%  %%%%%%%.                    \ \n
\                           #@@@  @@@%%%#.#@.@&             \ \n
\                           ,%%%%   ,@@@##%% @              \ \n
\                           ,###%%%%%%@@@@    %@.%          \ \n
\                            @@@@% ,%%%#@,                  \ \n
\                            @@%#@@@@%%%%#                  \ \n
\                &@%         @%#   @@  %%&                  \ \n
\           %% /%%@         %%#%&@      @@,                 \ \n
\            @@@  #%#(@    *@@@@ @%#%   &#%%                \ \n
\            @@@@@&%%*     %#%####%%#@@@  @@@               \ \n
\            @@@@@@@*     (%%%##%@%  (@@@@@@@               \ \n
\    @     @@@@@@@@@@@@   @@@@@@@ @     &@@@@@@             \ \n 
\      @@@@@@@@@@        @@@@@@@           @@@@@@           \ \n
\       @@@@@@           @@@@@               (@@@@  .@@     \ \n
\        /@@           *@@@@*@                 .@,,@@       \ \n
\         .@           @@@@                      &@         \ \n         
\@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               \ \n
\@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     \ \n
------------------------------------------------------------- \n
||||||||      ___      _     __  __   __             |||||||| \n
||||||||       |  |_| |_    |__ |  | |  | |          |||||||| \n
||||||||       |  | | |_    |   |__| |__| |__        |||||||| \n
||||||||                                             |||||||| \n
------------------------------------------------------------- '''           

         
    if senso == "dritto":
         image=image1
    elif senso=="rovescio":
         image=image_inverter.inverter(image1)

    else:
         print("Errore")
         
    return(image)         
         
#arcano1=input("Arcano?\n")
#senso1=input("Senso?\n")
#arcano2=input("Arcano?\n")
#senso2=input("Senso?\n")
#funzione=input("immagine o descrizione?\n")


#if funzione == "immagine":
#   print(f"{immagine(arcano1, senso1)}   {immagine(arcano2, senso2)}")
#elif funzione == "descrizione":
#   print(descrizione(arcano1, senso1),"   ", descrizione(arcano2, senso2))

