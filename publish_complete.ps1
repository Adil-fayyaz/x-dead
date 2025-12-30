# X DEAD - Script Completo per Pubblicare su GitHub
# Created by: Infinity X Team White Devel
# Questo script fa TUTTO automaticamente!

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  X DEAD - GitHub Auto Publisher" -ForegroundColor Red
Write-Host "  Created by: Infinity X Team White Devel" -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica Git
Write-Host "[*] Verificando Git..." -ForegroundColor Yellow
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "[!] Git non trovato! Installalo da: https://git-scm.com" -ForegroundColor Red
    exit 1
}
Write-Host "[+] Git trovato!" -ForegroundColor Green

# Verifica configurazione Git
Write-Host "[*] Verificando configurazione Git..." -ForegroundColor Yellow
$gitUser = git config user.name
$gitEmail = git config user.email

if (-not $gitUser) {
    Write-Host "[!] Git user.name non configurato!" -ForegroundColor Red
    $newUser = Read-Host "Inserisci il tuo nome"
    git config --global user.name $newUser
    Write-Host "[+] Configurato!" -ForegroundColor Green
}

if (-not $gitEmail) {
    Write-Host "[!] Git user.email non configurato!" -ForegroundColor Red
    $newEmail = Read-Host "Inserisci la tua email"
    git config --global user.email $newEmail
    Write-Host "[+] Configurato!" -ForegroundColor Green
}

Write-Host "[+] Git configurato: $(git config user.name) <$(git config user.email)>" -ForegroundColor Green
Write-Host ""

# Verifica se siamo nella directory giusta
if (-not (Test-Path "x_dead.py")) {
    Write-Host "[!] File x_dead.py non trovato!" -ForegroundColor Red
    Write-Host "[*] Assicurati di essere nella directory del progetto" -ForegroundColor Yellow
    exit 1
}

# Inizializza Git se necessario
if (-not (Test-Path ".git")) {
    Write-Host "[*] Inizializzando repository Git..." -ForegroundColor Yellow
    git init
    Write-Host "[+] Repository inizializzato!" -ForegroundColor Green
}

# Aggiungi tutti i file
Write-Host "[*] Aggiungendo file al repository..." -ForegroundColor Yellow
git add .
Write-Host "[+] File aggiunti!" -ForegroundColor Green

# Controlla se ci sono modifiche da committare
$status = git status --porcelain
if ($status) {
    Write-Host "[*] Creando commit..." -ForegroundColor Yellow
    git commit -m "Initial commit: X DEAD v1.0 - Network Control System for Kali Linux and Termux"
    Write-Host "[+] Commit creato!" -ForegroundColor Green
} else {
    Write-Host "[*] Nessuna modifica da committare" -ForegroundColor Yellow
}

# Cambia branch a main
Write-Host "[*] Impostando branch principale..." -ForegroundColor Yellow
git branch -M main 2>$null
Write-Host "[+] Branch impostato!" -ForegroundColor Green

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  CREA IL REPOSITORY SU GITHUB" -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Ora devi creare il repository su GitHub:" -ForegroundColor White
Write-Host ""
Write-Host "1. Vai su: https://github.com/new" -ForegroundColor Cyan
Write-Host "2. Repository name: X-DEAD" -ForegroundColor White
Write-Host "3. Description: Powerful Network Control System for Kali Linux and Termux" -ForegroundColor White
Write-Host "4. Visibility: Public" -ForegroundColor White
Write-Host "5. NON spuntare 'Initialize with README'" -ForegroundColor Red
Write-Host "6. Clicca 'Create repository'" -ForegroundColor White
Write-Host ""

# Chiedi l'URL del repository
Write-Host "Dopo aver creato il repository, incolla qui l'URL:" -ForegroundColor Yellow
Write-Host "(Esempio: https://github.com/username/X-DEAD.git)" -ForegroundColor Gray
$repoUrl = Read-Host "URL del repository"

if (-not $repoUrl) {
    Write-Host "[!] URL non fornito. Esco." -ForegroundColor Red
    exit 1
}

# Rimuovi remote esistente se presente
Write-Host ""
Write-Host "[*] Configurando remote..." -ForegroundColor Yellow
git remote remove origin 2>$null
git remote add origin $repoUrl
Write-Host "[+] Remote configurato: $repoUrl" -ForegroundColor Green

# Informazioni per il push
Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  PUBBLICAZIONE SU GITHUB" -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "[*] Pubblicando su GitHub..." -ForegroundColor Yellow
Write-Host "[!] Ti verrà chiesto di autenticarti:" -ForegroundColor Yellow
Write-Host "    - Username: Il tuo username GitHub" -ForegroundColor White
Write-Host "    - Password: Usa un Personal Access Token (NON la password normale!)" -ForegroundColor White
Write-Host ""
Write-Host "Come creare un token:" -ForegroundColor Cyan
Write-Host "1. Vai su: https://github.com/settings/tokens" -ForegroundColor White
Write-Host "2. Generate new token (classic)" -ForegroundColor White
Write-Host "3. Seleziona scope: repo (tutti)" -ForegroundColor White
Write-Host "4. Generate e copia il token" -ForegroundColor White
Write-Host ""
Write-Host "Premi INVIO quando sei pronto..." -ForegroundColor Yellow
$null = Read-Host

# Prova il push
Write-Host ""
Write-Host "[*] Eseguendo git push..." -ForegroundColor Yellow
try {
    git push -u origin main
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "=========================================" -ForegroundColor Green
        Write-Host "  ✅ SUCCESSO!" -ForegroundColor Green
        Write-Host "=========================================" -ForegroundColor Green
        Write-Host ""
        Write-Host "[+] Repository pubblicato con successo!" -ForegroundColor Green
        Write-Host "[*] Visita: $repoUrl" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Il tuo tool X DEAD è ora su GitHub! 🎉" -ForegroundColor Yellow
    } else {
        Write-Host ""
        Write-Host "[!] Errore durante il push." -ForegroundColor Red
        Write-Host "[*] Possibili cause:" -ForegroundColor Yellow
        Write-Host "    - Credenziali errate" -ForegroundColor White
        Write-Host "    - Token non valido o scaduto" -ForegroundColor White
        Write-Host "    - Repository non esiste o non hai permessi" -ForegroundColor White
        Write-Host ""
        Write-Host "[*] Prova manualmente:" -ForegroundColor Yellow
        Write-Host "    git push -u origin main" -ForegroundColor Cyan
    }
} catch {
    Write-Host ""
    Write-Host "[!] Errore: $_" -ForegroundColor Red
    Write-Host "[*] Prova manualmente:" -ForegroundColor Yellow
    Write-Host "    git push -u origin main" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "Premi un tasto per uscire..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

