class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti={}
        self.prestiti={}
        # TODO

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                info=line.strip().split(',')
                codice=info[0]
                tipo=info[1]
                marca=info[2]
                anno_acquisto=info[3]
                valore=info[4]
                self.strumenti[codice]=[tipo,marca,int(anno_acquisto),float(valore)]

        return self.strumenti
        # TODO

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        numeri=[]
        for codice in self.strumenti:
            if codice[1:] not in numeri:
                numeri.append(codice[1:])
        prossimo_codice=f'S{max(numeri)+1}'
        self.strumenti[prossimo_codice]=[tipo,marca,int(anno_acquisto),float(valore)]

        return self.strumenti
        # TODO

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.strumenti.values(), key=lambda s:s[1])
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if id_strumento not in self.strumenti:
            print(f"Errore: lo strumento con codice {id_strumento} non esiste nel sistema.")
            return None

        for prestito in self.prestiti.values():
            if prestito[1] == id_strumento:
                print(f"Errore: lo strumento {id_strumento} risulta già in prestito.")
                return None

        numeri = []
        for codice in self.prestiti:
            if codice[1:] not in numeri:
                numeri.append(codice[1:])
        prossimo_codice = f'P{max(numeri) + 1}'
        self.prestiti[prossimo_codice]=[data,id_strumento,cognome_allievo]

        return self.prestiti
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if id_prestito not in self.prestiti:
            print(f"Errore: nessun prestito attivo trovato con codice {id_prestito}.")
        else:
            del self.prestiti[id_prestito]
        # TODO