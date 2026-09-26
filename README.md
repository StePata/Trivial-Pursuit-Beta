# Trivial Pursuit Beta
                 TRIVIAL PURSUIT 🎲                        


BENVENUTO!
==========
Questo è un gioco di Trivial Pursuit con domande in Italiano e Inglese.
Segui i passi qui sotto per installare e giocare!


REQUISITI DI SISTEMA:
=====================
✓ Windows 10 o superiore
✓ Connessione Internet (solo per l'installazione)
✓ 500 MB di spazio libero su disco


ISTRUZIONI PASSO-PASSO:
========================

📥 PASSO 1: Installa Python
   → Fai doppio clic su: 1_INSTALLA_PYTHON.bat
   → Si aprirà il sito ufficiale di Python
   → Scarica Python 3.11 o versione superiore
   
   ⚠️ IMPORTANTE DURANTE L'INSTALLAZIONE:
   → Spunta la casella: ☑ Add Python to PATH
   → Questa opzione si trova in BASSO nella prima schermata
   → Clicca su "Install Now"
   → Attendi il completamento
   → Riavvia il computer (consigliato)


📦 PASSO 2: Installa le Dipendenze
   → Fai doppio clic su: 2_INSTALLA_DIPENDENZE.bat
   → Vedrai una finestra nera con del testo
   → Attendi che l'installazione si completi
   → Potrebbero apparire alcuni warning (è normale)
   → Alla fine vedrai: "INSTALLAZIONE COMPLETATA!"
   
   ℹ️ NOTA: Se vedi errori su "pyarrow", ignorali.
      Non sono necessari per il funzionamento del gioco.


🎮 PASSO 3: Avvia il Gioco
   → Fai doppio clic su: 3_AVVIA_TRIVIAL.bat
   → Si aprirà una finestra nera (NON chiuderla!)
   → Il browser si aprirà automaticamente con il gioco
   → Seleziona una categoria e inizia a giocare!


COME GIOCARE:
=============
1. Clicca su una categoria colorata (Sport, Geografia, ecc.)
2. Leggi la domanda in Italiano o Inglese
3. Pensa alla risposta
4. Clicca su "👁️ Mostra Risposta" per vedere se hai indovinato
5. Clicca su "🔄 Nuova Domanda" per continuare


CATEGORIE DISPONIBILI:
======================
⚽ Sport e Tempo Libero (Arancione)
🎨 Arte e Letteratura (Viola)
🎬 Intrattenimento e Musica (Rosa)
🔬 Scienza e Natura (Verde)
🏰 Storia (Giallo)
🌍 Geografia (Blu)


COME CHIUDERE IL GIOCO:
========================
→ Chiudi la scheda del browser
→ Chiudi la finestra nera (Prompt dei comandi)


═══════════════════════════════════════════════════════════════

⚠️ RISOLUZIONE PROBLEMI:
========================

❌ PROBLEMA: "Python non trovato"
   CAUSA: Non hai spuntato "Add Python to PATH"
   SOLUZIONE:
   1. Vai in Pannello di Controllo → Programmi → Disinstalla
   2. Disinstalla Python
   3. Riavvia il computer
   4. Esegui di nuovo 1_INSTALLA_PYTHON.bat
   5. Questa volta SPUNTA "Add Python to PATH"!


❌ PROBLEMA: "File trivial_pursuit_domande.py non trovato"
   CAUSA: I file non sono nella posizione corretta
   SOLUZIONE:
   Assicurati che la struttura delle cartelle sia:
   
   Trivial_Pursuit/
   ├── 1_INSTALLA_PYTHON.bat
   ├── 2_INSTALLA_DIPENDENZE.bat
   ├── 3_AVVIA_TRIVIAL.bat
   ├── README.txt
   ├── Codici/
   │   └── trivial_pursuit_domande.py
   └── Domande_Merged/
       ├── arts_and_literature_merged.json
       ├── geography_merged.json
       ├── history_merged.json
       ├── science_and_nature_merged.json
       ├── sport_and_leisure_merged.json
       └── entertainment_and_music_merged.json


❌ PROBLEMA: Il browser non si apre automaticamente
   SOLUZIONE:
   → Apri manualmente il browser
   → Vai su: http://localhost:8501
   → Il gioco apparirà!


❌ PROBLEMA: Errori durante l'installazione delle dipendenze
   CAUSA: Problemi di connessione Internet o firewall
   SOLUZIONE:
   1. Verifica la connessione Internet
   2. Disattiva temporaneamente l'antivirus
   3. Riprova a eseguire 2_INSTALLA_DIPENDENZE.bat


❌ PROBLEMA: La pagina dice "Please wait..."
   SOLUZIONE:
   → È normale! Streamlit sta caricando
   → Attendi 10-30 secondi
   → Se dopo 1 minuto non cambia, riavvia il file .bat


❌ PROBLEMA: Errori su "pyarrow" durante l'installazione
   SOLUZIONE:
   → Ignora completamente questo errore
   → Il gioco funziona perfettamente senza pyarrow
   → Procedi normalmente con il PASSO 3


═══════════════════════════════════════════════════════════════

💡 SUGGERIMENTI:
================
→ Per giocare in modalità schermo intero: premi F11 nel browser
→ Puoi avviare più partite contemporaneamente su dispositivi diversi
→ Le domande vengono selezionate casualmente ogni volta
→ Non serve connessione Internet dopo l'installazione


🔄 AGGIORNAMENTI:
=================
Per aggiornare il gioco con nuove domande:
1. Sostituisci i file .json nella cartella Domande_Merged
2. Riavvia il gioco


📋 CONTENUTO DEL PACCHETTO:
===========================
✓ 1_INSTALLA_PYTHON.bat - Script installazione Python
✓ 2_INSTALLA_DIPENDENZE.bat - Script installazione librerie
✓ 3_AVVIA_TRIVIAL.bat - Script avvio gioco
✓ README.txt - Questo file
✓ Codici/ - Contiene il codice del gioco
✓ Domande_Merged/ - Contiene tutte le domande


═══════════════════════════════════════════════════════════════

📧 SUPPORTO E FEEDBACK:
=======================
Se hai problemi non risolti da questa guida:
→ Contatta il creatore del gioco
→ Fornisci una screenshot dell'errore
→ Indica quale passaggio stavi eseguendo


═══════════════════════════════════════════════════════════════

🎉 BUON DIVERTIMENTO!
=====================
Creato con Python e Streamlit

Versione: 1.0
Data: Gennaio 2026
Sistema: Windows

═══════════════════════════════════════════════════════════════
