@echo off
echo ========================================
echo INSTALLAZIONE DIPENDENZE
echo ========================================
echo.
echo Verifica che Python sia installato...
python --version
if errorlevel 1 (
    echo.
    echo ERRORE: Python non trovato!
    echo Esegui prima il file: 1_INSTALLA_PYTHON.bat
    echo.
    pause
    exit /b
)
echo.
echo Python trovato! Procedo con l'installazione...
echo.
echo Aggiornamento pip...
python -m pip install --upgrade pip
echo.
echo Installazione di Streamlit in corso...
echo.
python -m pip install streamlit
echo.
echo ========================================
echo INSTALLAZIONE COMPLETATA!
echo ========================================
echo.
echo NOTA IMPORTANTE:
echo Se hai visto un errore su "pyarrow", puoi ignorarlo.
echo PyArrow non e' necessario per questo gioco.
echo.
echo Ora puoi avviare il gioco con:
echo 3_AVVIA_TRIVIAL.bat
echo.
pause