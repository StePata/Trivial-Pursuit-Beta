@echo off
echo ========================================
echo AVVIO TRIVIAL PURSUIT
echo ========================================
echo.
cd /d "%~dp0\Codici"
if not exist trivial_pursuit_domande.py (
    echo ERRORE: File trivial_pursuit_domande.py non trovato!
    echo Assicurati di essere nella cartella corretta.
    pause
    exit /b
)
echo Avvio del gioco...
echo.
echo Il browser si aprira' automaticamente.
echo Per chiudere il gioco, chiudi questa finestra.
echo.
python -m streamlit run trivial_pursuit_domande.py
pause