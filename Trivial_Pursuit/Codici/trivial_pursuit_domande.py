import streamlit as st
import json
import random

# Configurazione pagina per evitare scrolling
st.set_page_config(
    page_title="Trivial Pursuit", 
    page_icon="🎲", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizzato - TESTO FORZATO BIANCO SU TUTTI I BOTTONI!
st.markdown("""
    <style>
    /* Rimuove completamente lo scrolling */
    .main > div {
        padding-top: 0.5rem !important;
        padding-right: 0.5rem !important;
        padding-left: 0.5rem !important;
        padding-bottom: 0.5rem !important;
        max-height: 100vh !important;
        overflow: hidden !important;
    }
    
    /* Contenitore principale senza scrolling */
    .main {
        overflow: hidden !important;
    }
    
    /* Stile per eliminare spazi extra */
    div[data-testid="stVerticalBlock"] {
        gap: 0.3rem !important;
    }
    
    /* Contenitore COLORATO per ogni categoria - BOTTONI PIÙ GRANDI! */
    .category-container {
        border-radius: 15px !important;
        padding: 0.5rem !important;
        margin: 0.2rem !important;
        height: 110px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        border: 2px solid rgba(255, 255, 255, 0.2) !important;
        cursor: pointer !important;
    }
    
    /* Effetto hover per il rettangolo */
    .category-container:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 12px rgba(0,0,0,0.2) !important;
        border: 2px solid rgba(255, 255, 255, 0.4) !important;
    }
    
    /* TESTO FORZATO BIANCO - ELIMINA OGNI ALTRO COLORE! */
    .category-button {
        background: transparent !important;
        border: none !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        width: 100% !important;
        height: 100% !important;
        cursor: pointer !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        padding: 0 !important;
        gap: 8px !important;
    }
    
    /* FORZA TUTTO IL TESTO DENTRO .category-button A ESSERE BIANCO */
    .category-button * {
        color: white !important;
    }
    
    .category-button strong {
        color: white !important;
    }
    
    .category-button div {
        color: white !important;
    }
    
    /* Stile per le emoji - PIÙ GRANDI! */
    .category-emoji {
        font-size: 32px !important;
        margin-bottom: 5px !important;
        color: white !important;
    }
    
    /* Titolo più compatto */
    h1 {
        font-size: 1.8rem !important;
        margin-bottom: 0.3rem !important;
        margin-top: 0.3rem !important;
    }
    
    /* Testo "Seleziona una categoria" in BIANCO */
    .stMarkdown h3, .stMarkdown p {
        color: white !important;
    }
    
    /* Forza bianco per il testo delle categorie nella griglia */
    div[data-testid="column"] .stMarkdown {
        color: white !important;
    }
    
    div[data-testid="column"] .stMarkdown strong {
        color: white !important;
    }
    
    /* Testo più compatto */
    h3 {
        font-size: 1.1rem !important;
        margin-top: 0.2rem !important;
        margin-bottom: 0.2rem !important;
        color: white !important;
    }
    
    h4 {
        font-size: 1rem !important;
        margin-top: 0.1rem !important;
        margin-bottom: 0.1rem !important;
    }
    
    .stMarkdown p {
        margin-bottom: 0.2rem !important;
    }
    
    /* Riduci spaziatura colonne */
    [data-testid="column"] {
        padding: 0.1rem !important;
    }
    
    /* Pulsanti azione più compatti */
    button[kind="primary"] {
        height: 45px !important;
        font-size: 16px !important;
        margin: 1px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    
    /* Success message compatto */
    .stSuccess {
        padding: 0.3rem !important;
        margin: 0.1rem 0 !important;
        border: 1px solid rgba(0, 255, 0, 0.2) !important;
    }
    
    .stInfo {
        padding: 0.3rem !important;
        margin: 0.1rem 0 !important;
        border: 1px solid rgba(0, 0, 255, 0.2) !important;
    }
    
    hr {
        margin: 0.2rem 0 !important;
    }
    
    /* Layout compatto per domande e risposte */
    div[data-testid="stHorizontalBlock"] {
        gap: 0.5rem !important;
    }
    
    /* Footer nascosto */
    .stApp footer {
        visibility: hidden;
    }
    
    /* Header nascosto */
    .stApp header {
        visibility: hidden;
    }
    
    /* Rimuove tutti i bordi rossi di debug */
    * {
        outline: none !important;
    }
    
    /* Rimuove specificamente i bordi rossi dei bottoni */
    button:focus {
        outline: none !important;
        box-shadow: none !important;
        border-color: rgba(255, 255, 255, 0.2) !important;
    }
    
    /* Nasconde completamente i bottoni Streamlit originali */
    div.stButton > button[data-testid="baseButton-primary"] {
        display: none !important;
    }
    
    /* Stile per i bottoni azione - PIÙ GRANDI! */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        font-size: 16px !important;
    }
    
    div.stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%) !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* TESTO "Seleziona una categoria" FORZATO BIANCO */
    .stMarkdown strong {
        color: white !important;
        font-size: 1.2rem !important;
    }
    
    /* Override completo per qualsiasi testo verde */
    .category-button,
    .category-button span,
    .category-button div,
    .category-button strong,
    .category-button em,
    .category-button i {
        color: white !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5) !important;
    }
    
    /* Sombra più marcata per testo su Storia (giallo) */
    .storia-special {
        color: white !important;
        text-shadow: 
            2px 2px 3px rgba(0,0,0,0.8),
            -1px -1px 2px rgba(0,0,0,0.6) !important;
    }
    
    /* Background colorato più scuro per miglior contrasto */
    .dark-bg {
        background: linear-gradient(135deg, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.5) 100%) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Titolo compatto
st.title("🎲 Trivial Pursuit")

# Inizializza session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'questions_data' not in st.session_state:
    st.session_state.questions_data = {}

# Carica i file JSON
@st.cache_data
def load_questions():
    base_path = "../Domande/"
    
    categories = {
        "Arte e Letteratura": "arts_and_literature_merged.json",
        "Geografia": "geography_merged.json",
        "Storia": "history_merged.json",
        "Scienza e Natura": "science_and_nature_merged.json",
        "Sport e Tempo Libero": "sport_and_leisure_merged.json",
        "Intrattenimento e Musica": "entertainment_and_music_merged.json"
    }
    
    data = {}
    for cat_name, file_name in categories.items():
        try:
            file_path = base_path + file_name
            with open(file_path, 'r', encoding='utf-8') as f:
                data[cat_name] = json.load(f)
        except FileNotFoundError:
            st.error(f"File {file_path} non trovato!")
    
    return data

# Carica le domande
st.session_state.questions_data = load_questions()

# Configurazione colori per categoria
CATEGORY_COLORS = {
    "Sport e Tempo Libero": "#FF8C00",
    "Arte e Letteratura": "#8B008B",
    "Intrattenimento e Musica": "#FF1493",
    "Scienza e Natura": "#32CD32",
    "Storia": "#FFD700",
    "Geografia": "#4169E1"
}

# Emoji carine per ogni categoria
CATEGORY_EMOJIS = {
    "Sport e Tempo Libero": "⚽",
    "Arte e Letteratura": "🎨",
    "Intrattenimento e Musica": "🎬",
    "Scienza e Natura": "🔬",
    "Storia": "🏰",
    "Geografia": "🌍"
}

# Selezione categoria con rettangoli completamente colorati - TESTO BIANCO GARANTITO
st.markdown("<h3 style='color: white !important;'>Seleziona una categoria:</h3>", unsafe_allow_html=True)

# Crea griglia 3x2 per i rettangoli colorati
col1, col2, col3 = st.columns(3)

categories_order = [
    "Sport e Tempo Libero",
    "Arte e Letteratura",
    "Intrattenimento e Musica",
    "Geografia",
    "Storia",
    "Scienza e Natura"
]

for idx, category in enumerate(categories_order):
    # Distribuisci in 3 colonne
    if idx < 2:
        col = col1
    elif idx < 4:
        col = col2
    else:
        col = col3
    
    with col:
        # Colori per questa categoria
        bg_color = CATEGORY_COLORS[category]
        emoji = CATEGORY_EMOJIS[category]
        
        # Per Storia (giallo), usiamo classe speciale con ombra più marcata
        text_class = ""
        if category == "Storia":
            text_class = "storia-special"
        
        # Crea il rettangolo colorato con HTML/CSS - TESTO BIANCO FORZATO!
        st.markdown(f"""
        <div class="category-container" 
             onclick="this.nextElementSibling.click()"
             style="background: linear-gradient(135deg, {bg_color} 0%, {bg_color} 100%);">
            <div class="category-button {text_class}">
                <div class="category-emoji">{emoji}</div>
                <div style="color: white !important; text-shadow: 1px 1px 2px rgba(0,0,0,0.5) !important;">
                    <strong style="color: white !important;">{category}</strong>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Bottone Streamlit nascosto che gestisce il click
        if st.button(category, key=f"hidden_{category}_{idx}"):
            questions = st.session_state.questions_data.get(category, [])
            if questions:
                st.session_state.current_question = random.choice(questions)
                st.session_state.show_answer = False
                st.session_state.selected_category = category
                st.rerun()

# Mostra la domanda corrente
if st.session_state.current_question:
    question = st.session_state.current_question
    
    # Contenitore per domanda e risposte
    question_container = st.container()
    
    with question_container:
        # Header con categoria e pulsanti azione
        header_col1, header_col2, header_col3 = st.columns([2, 1, 1])
        
        with header_col1:
            if 'selected_category' in st.session_state:
                color = CATEGORY_COLORS[st.session_state.selected_category]
                emoji = CATEGORY_EMOJIS[st.session_state.selected_category]
                st.markdown(f"<h3 style='color: {color};'>{emoji} {st.session_state.selected_category}</h3>", 
                          unsafe_allow_html=True)
        
        with header_col2:
            if st.button("👁️ Mostra Risposta", use_container_width=True):
                st.session_state.show_answer = True
                st.rerun()
        
        with header_col3:
            if st.button("🔄 Nuova Domanda", use_container_width=True):
                if 'selected_category' in st.session_state:
                    questions = st.session_state.questions_data[st.session_state.selected_category]
                    st.session_state.current_question = random.choice(questions)
                    st.session_state.show_answer = False
                    st.rerun()
        
        # Domanda in entrambe le lingue
        col_it, col_en = st.columns(2)
        
        with col_it:
            st.markdown("**🇮🇹 Italiano**")
            st.markdown(f"*{question['question']['it']}*")
        
        with col_en:
            st.markdown("**🇬🇧 English**")
            st.markdown(f"*{question['question']['en']}*")
        
        # Mostra la risposta se richiesto
        if st.session_state.show_answer:
            correct_answer_index = question['answer']
            
            st.success("✅ **Risposta Corretta**")
            
            col_it_ans, col_en_ans = st.columns(2)
            
            with col_it_ans:
                st.markdown("**🇮🇹 Risposte:**")
                for i, answer in enumerate(question['answers']['it']):
                    if i == correct_answer_index:
                        st.markdown(f"**✓ {i + 1}. {answer}**")
                    else:
                        st.markdown(f"{i + 1}. {answer}")
            
            with col_en_ans:
                st.markdown("**🇬🇧 Answers:**")
                for i, answer in enumerate(question['answers']['en']):
                    if i == correct_answer_index:
                        st.markdown(f"**✓ {i + 1}. {answer}**")
                    else:
                        st.markdown(f"{i + 1}. {answer}")

else:
    # Messaggio iniziale
    st.info("👆 **Seleziona una categoria per iniziare!**")

# CSS FINALE per forzare testo bianco
st.markdown("""
    <style>
    /* Forza bianco su TUTTI gli elementi nei bottoni categoria */
    .category-container * {
        color: white !important;
    }
    
    /* Override totale per qualsiasi colore verde residuo */
    .category-button,
    .category-button *,
    .category-container *,
    .category-container strong,
    .category-container div,
    .category-container span {
        color: white !important;
        fill: white !important;
        stroke: white !important;
    }
    
    /* Rimuove qualsiasi colore ereditato */
    .category-container {
        color: white !important;
    }
    
    /* Sfondo scuro per migliorare contrasto */
    .category-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.2);
        border-radius: 15px;
        z-index: 1;
        pointer-events: none;
    }
    
    .category-button {
        position: relative;
        z-index: 2;
    }
    
    /* Assicura che tutto il testo sia visibile */
    .category-button strong {
        color: white !important;
        text-shadow: 
            1px 1px 3px rgba(0,0,0,0.7),
            0px 0px 4px rgba(0,0,0,0.5) !important;
        font-weight: 800 !important;
    }
    
    /* Per mobile */
    @media (max-width: 768px) {
        .category-container {
            height: 90px !important;
        }
        .category-button {
            font-size: 16px !important;
        }
        .category-emoji {
            font-size: 28px !important;
        }
        .category-button strong {
            text-shadow: 
                1px 1px 2px rgba(0,0,0,0.8),
                0px 0px 3px rgba(0,0,0,0.6) !important;
        }
    }
    </style>
    
    <script>
    // Forza il colore bianco via JavaScript come backup
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(function() {
            const buttons = document.querySelectorAll('.category-button, .category-button *');
            buttons.forEach(button => {
                button.style.color = 'white !important';
                button.style.textShadow = '1px 1px 2px rgba(0,0,0,0.5) !important';
            });
            
            const strongs = document.querySelectorAll('.category-button strong');
            strongs.forEach(strong => {
                strong.style.color = 'white !important';
                strong.style.textShadow = '1px 1px 3px rgba(0,0,0,0.7) !important';
            });
        }, 100);
    });
    </script>
""", unsafe_allow_html=True)

#cd "C:\Users\stepa\Desktop\VS Progetti\Trivial_Pursuit\Codici"
#python -m streamlit run trivial_pursuit_domande.py