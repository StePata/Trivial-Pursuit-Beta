import streamlit as st
import random
import json

# Configurazione categorie
CATEGORIE = {
    "storia": {"colore": "#FFA500", "emoji": "🏛️"},
    "geografia": {"colore": "#0066CC", "emoji": "🌍"},
    "scienza": {"colore": "#00CC66", "emoji": "🔬"},
    "sport": {"colore": "#FF0000", "emoji": "⚽"},
    "arte": {"colore": "#9933FF", "emoji": "🎨"},
    "spettacolo": {"colore": "#FF69B4", "emoji": "🎬"}
}

# Database domande di esempio (partendo con 20 per categoria)
DOMANDE = {
    "storia": [
        {"tipo": "secca", "domanda": "In che anno è caduto il muro di Berlino?", "risposta": "1989"},
        {"tipo": "multipla", "domanda": "Chi ha scoperto l'America?", "opzioni": ["Cristoforo Colombo", "Marco Polo", "Amerigo Vespucci", "Magellano"], "risposta": "Cristoforo Colombo"},
        {"tipo": "vero_falso", "domanda": "La Seconda Guerra Mondiale è finita nel 1945", "risposta": True},
        {"tipo": "secca", "domanda": "Chi era il primo imperatore romano?", "risposta": "augusto"},
    ],
    "geografia": [
        {"tipo": "multipla", "domanda": "Qual è la capitale dell'Australia?", "opzioni": ["Sydney", "Melbourne", "Canberra", "Brisbane"], "risposta": "Canberra"},
        {"tipo": "secca", "domanda": "Qual è il fiume più lungo del mondo?", "risposta": "nilo"},
        {"tipo": "vero_falso", "domanda": "Il Monte Everest è in Nepal", "risposta": True},
        {"tipo": "multipla", "domanda": "Quanti continenti ci sono?", "opzioni": ["5", "6", "7", "8"], "risposta": "7"},
    ],
    "scienza": [
        {"tipo": "vero_falso", "domanda": "Il Sole è una stella", "risposta": True},
        {"tipo": "multipla", "domanda": "Qual è il pianeta più grande del sistema solare?", "opzioni": ["Marte", "Giove", "Saturno", "Nettuno"], "risposta": "Giove"},
        {"tipo": "secca", "domanda": "Qual è il simbolo chimico dell'oro?", "risposta": "au"},
        {"tipo": "vero_falso", "domanda": "Gli squali sono mammiferi", "risposta": False},
    ],
    "sport": [
        {"tipo": "multipla", "domanda": "In che anno si sono svolte le Olimpiadi di Roma?", "opzioni": ["1956", "1960", "1964", "1968"], "risposta": "1960"},
        {"tipo": "secca", "domanda": "Quanti giocatori ci sono in una squadra di calcio in campo?", "risposta": "11"},
        {"tipo": "vero_falso", "domanda": "Il basket è stato inventato in America", "risposta": True},
        {"tipo": "multipla", "domanda": "Quanti set si giocano in una partita di tennis?", "opzioni": ["Al meglio di 3", "Al meglio di 5", "Sempre 3", "Sempre 5"], "risposta": "Al meglio di 5"},
    ],
    "arte": [
        {"tipo": "secca", "domanda": "Chi ha dipinto la Gioconda?", "risposta": "leonardo"},
        {"tipo": "multipla", "domanda": "Dove si trova la Cappella Sistina?", "opzioni": ["Firenze", "Roma", "Venezia", "Milano"], "risposta": "Roma"},
        {"tipo": "vero_falso", "domanda": "Picasso era spagnolo", "risposta": True},
        {"tipo": "secca", "domanda": "Chi ha scolpito il David?", "risposta": "michelangelo"},
    ],
    "spettacolo": [
        {"tipo": "multipla", "domanda": "Chi ha diretto 'Il Padrino'?", "opzioni": ["Martin Scorsese", "Francis Ford Coppola", "Steven Spielberg", "Quentin Tarantino"], "risposta": "Francis Ford Coppola"},
        {"tipo": "secca", "domanda": "Quanti Oscar ha vinto 'Titanic'?", "risposta": "11"},
        {"tipo": "vero_falso", "domanda": "I Beatles erano inglesi", "risposta": True},
        {"tipo": "multipla", "domanda": "Chi interpreta Iron Man nei film Marvel?", "opzioni": ["Chris Evans", "Robert Downey Jr", "Chris Hemsworth", "Mark Ruffalo"], "risposta": "Robert Downey Jr"},
    ]
}

# Inizializzazione stato
if 'giocatori' not in st.session_state:
    st.session_state.giocatori = []
    st.session_state.gioco_iniziato = False
    st.session_state.turno_corrente = 0
    st.session_state.domanda_attiva = None
    st.session_state.risposta_data = False

def normalizza_risposta(testo):
    """Normalizza una risposta per il confronto"""
    return testo.lower().strip().replace("à", "a").replace("è", "e").replace("ì", "i").replace("ò", "o").replace("ù", "u")

def inizializza_giocatore(nome):
    return {
        "nome": nome,
        "formaggini": {cat: False for cat in CATEGORIE.keys()},
        "posizione": 0,
        "punteggio": 0
    }

def lancia_dado():
    return random.randint(1, 6)

def estrai_domanda(categoria):
    domande_disponibili = [d for d in DOMANDE[categoria]]
    return random.choice(domande_disponibili)

def verifica_vittoria(giocatore):
    return all(giocatore["formaggini"].values())

# UI principale
st.title("🎲 Trivial Pursuit Semplificato")

# Setup gioco
if not st.session_state.gioco_iniziato:
    st.header("Configura la partita")
    
    num_giocatori = st.number_input("Numero di giocatori", min_value=2, max_value=4, value=2)
    
    nomi = []
    for i in range(num_giocatori):
        nome = st.text_input(f"Nome Giocatore {i+1}", value=f"Giocatore {i+1}")
        nomi.append(nome)
    
    if st.button("Inizia Partita"):
        st.session_state.giocatori = [inizializza_giocatore(nome) for nome in nomi]
        st.session_state.gioco_iniziato = True
        st.session_state.turno_corrente = 0
        st.session_state.domanda_attiva = None
        st.rerun()

else:
    # Gioco in corso
    giocatore_attivo = st.session_state.giocatori[st.session_state.turno_corrente]
    
    # Sidebar con stato giocatori
    with st.sidebar:
        st.header("📊 Stato Giocatori")
        for idx, g in enumerate(st.session_state.giocatori):
            is_active = idx == st.session_state.turno_corrente
            st.markdown(f"**{'▶️ ' if is_active else ''}{g['nome']}** (Punteggio: {g['punteggio']})")
            cols = st.columns(6)
            for i, (cat, info) in enumerate(CATEGORIE.items()):
                with cols[i]:
                    if g['formaggini'][cat]:
                        st.markdown(f"<div style='background-color:{info['colore']};padding:5px;border-radius:5px;text-align:center'>{info['emoji']}</div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div style='background-color:#E0E0E0;padding:5px;border-radius:5px;text-align:center'>⚪</div>", unsafe_allow_html=True)
            st.markdown("---")
    
    st.header(f"Turno di: {giocatore_attivo['nome']}")
    
    # Visualizza formaggini da vincere
    st.subheader("Formaggini da ottenere:")
    cols = st.columns(6)
    for i, (cat, info) in enumerate(CATEGORIE.items()):
        with cols[i]:
            if not giocatore_attivo['formaggini'][cat]:
                st.markdown(f"<div style='background-color:{info['colore']};padding:10px;border-radius:10px;text-align:center;color:white'><b>{cat.upper()}</b><br>{info['emoji']}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Fase 1: Lancia dado e scegli categoria
    if st.session_state.domanda_attiva is None:
        if st.button("🎲 Lancia il dado", type="primary"):
            dado = lancia_dado()
            st.session_state.dado_lanciato = dado
            st.rerun()
        
        if 'dado_lanciato' in st.session_state:
            st.success(f"Hai fatto: {st.session_state.dado_lanciato}")
            st.write("Scegli una categoria:")
            
            cols = st.columns(3)
            for idx, (cat, info) in enumerate(CATEGORIE.items()):
                with cols[idx % 3]:
                    if st.button(f"{info['emoji']} {cat.upper()}", key=f"cat_{cat}"):
                        st.session_state.domanda_attiva = {
                            "categoria": cat,
                            "domanda": estrai_domanda(cat)
                        }
                        st.session_state.risposta_data = False
                        del st.session_state.dado_lanciato
                        st.rerun()
    
    # Fase 2: Rispondi alla domanda
    else:
        cat = st.session_state.domanda_attiva["categoria"]
        domanda = st.session_state.domanda_attiva["domanda"]
        info_cat = CATEGORIE[cat]
        
        st.markdown(f"<div style='background-color:{info_cat['colore']};padding:20px;border-radius:10px;color:white'><h3>{info_cat['emoji']} {cat.upper()}</h3><h4>{domanda['domanda']}</h4></div>", unsafe_allow_html=True)
        st.markdown("")
        
        if not st.session_state.risposta_data:
            risposta_utente = None
            
            if domanda['tipo'] == 'secca':
                risposta_utente = st.text_input("La tua risposta:")
                if st.button("Conferma risposta"):
                    if normalizza_risposta(risposta_utente) == normalizza_risposta(domanda['risposta']):
                        st.session_state.risposta_corretta = True
                        giocatore_attivo['punteggio'] += 10
                        if not giocatore_attivo['formaggini'][cat]:
                            giocatore_attivo['formaggini'][cat] = True
                            st.session_state.formaggino_vinto = True
                    else:
                        st.session_state.risposta_corretta = False
                    st.session_state.risposta_data = True
                    st.rerun()
            
            elif domanda['tipo'] == 'multipla':
                risposta_utente = st.radio("Scegli la risposta:", domanda['opzioni'])
                if st.button("Conferma risposta"):
                    if risposta_utente == domanda['risposta']:
                        st.session_state.risposta_corretta = True
                        giocatore_attivo['punteggio'] += 10
                        if not giocatore_attivo['formaggini'][cat]:
                            giocatore_attivo['formaggini'][cat] = True
                            st.session_state.formaggino_vinto = True
                    else:
                        st.session_state.risposta_corretta = False
                    st.session_state.risposta_data = True
                    st.rerun()
            
            elif domanda['tipo'] == 'vero_falso':
                risposta_utente = st.radio("Scegli:", ["Vero", "Falso"])
                if st.button("Conferma risposta"):
                    risposta_bool = risposta_utente == "Vero"
                    if risposta_bool == domanda['risposta']:
                        st.session_state.risposta_corretta = True
                        giocatore_attivo['punteggio'] += 10
                        if not giocatore_attivo['formaggini'][cat]:
                            giocatore_attivo['formaggini'][cat] = True
                            st.session_state.formaggino_vinto = True
                    else:
                        st.session_state.risposta_corretta = False
                    st.session_state.risposta_data = True
                    st.rerun()
        
        else:
            # Mostra risultato
            if st.session_state.risposta_corretta:
                st.success("✅ Risposta corretta! +10 punti")
                if 'formaggino_vinto' in st.session_state and st.session_state.formaggino_vinto:
                    st.balloons()
                    st.success(f"🎉 Hai vinto il formaggino {info_cat['emoji']} {cat.upper()}!")
                    del st.session_state.formaggino_vinto
            else:
                st.error(f"❌ Risposta sbagliata! La risposta corretta era: **{domanda['risposta']}**")
            
            # Verifica vittoria
            if verifica_vittoria(giocatore_attivo):
                st.balloons()
                st.success(f"🏆 {giocatore_attivo['nome']} ha vinto la partita!")
                if st.button("Nuova partita"):
                    for key in list(st.session_state.keys()):
                        del st.session_state[key]
                    st.rerun()
            else:
                if st.button("Prossimo turno"):
                    st.session_state.turno_corrente = (st.session_state.turno_corrente + 1) % len(st.session_state.giocatori)
                    st.session_state.domanda_attiva = None
                    st.session_state.risposta_data = False
                    st.session_state.risposta_corretta = False
                    st.rerun()
    
    # Pulsante reset
    st.markdown("---")
    if st.button("🔄 Ricomincia partita"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# python -m streamlit run trivial_pursuit.py