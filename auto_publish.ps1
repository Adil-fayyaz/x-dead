# X DEAD - Auto Publish to GitHub
# Created by: Infinity X Team White Devel

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  X DEAD - Auto Publish to GitHub" -ForegroundColor Red
Write-Host "  Created by: Infinity X Team White Devel" -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica Git
Write-Host "[*] Verifico Git..." -ForegroundColor Yellow
try {
    $gitVersion = git --version
    Write-Host "[+] Git trovato: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "[!] Git non trovato! Installalo da https://git-scm.com" -ForegroundColor Red
    exit 1
}

# Verifica configurazione Git
Write-Host "[*] Verifico configurazione Git..." -ForegroundColor Yellow
$gitUser = git config user.name
$gitEmail = git config user.email

if (-not $gitUser -or -not $gitEmail) {
    Write-Host "[!] Git non configurato!" -ForegroundColor Red
    Write-Host "[*] Configuro Git con valori di default..." -ForegroundColor Yellow
    git config user.name "Infinity X Team"
    git config user.email "infinityx@example.com"
    Write-Host "[+] Git configurato!" -ForegroundColor Green
} else {
    Write-Host "[+] Git configurato: $gitUser <$gitEmail>" -ForegroundColor Green
}

# Vai nella cartella del progetto
$projectPath = "C:\Users\adil\Desktop\kali linux tool"
Set-Location $projectPath
Write-Host "[*] Cartella progetto: $projectPath" -ForegroundColor Cyan

# Verifica se è un repository Git
if (-not (Test-Path .git)) {
    Write-Host "[*] Inizializzo repository Git..." -ForegroundColor Yellow
    git init
    git branch -M main
}

# Aggiungi e committa tutto
Write-Host "[*] Aggiungo tutti i file..." -ForegroundColor Yellow
git add .

$status = git status --porcelain
if ($status) {
    Write-Host "[*] Creo commit..." -ForegroundColor Yellow
    git commit -m "X DEAD v1.0 - Network Control System - Ready for GitHub"
    Write-Host "[+] Commit creato!" -ForegroundColor Green
} else {
    Write-Host "[*] Nessuna modifica da committare" -ForegroundColor Yellow
}

# Verifica se GitHub CLI è installato
Write-Host "[*] Verifico GitHub CLI..." -ForegroundColor Yellow
$ghInstalled = $false
try {
    $ghVersion = gh --version 2>$null
    if ($ghVersion) {
        $ghInstalled = $true
        Write-Host "[+] GitHub CLI trovato!" -ForegroundColor Green
    }
} catch {
    Write-Host "[*] GitHub CLI non trovato (opzionale)" -ForegroundColor Yellow
}

# Prova a creare repository con GitHub CLI
if ($ghInstalled) {
    Write-Host "[*] Provo a creare repository su GitHub..." -ForegroundColor Yellow
    try {
        # Verifica autenticazione
        $authStatus = gh auth status 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "[*] Creo repository 'X-DEAD' su GitHub..." -ForegroundColor Yellow
            gh repo create X-DEAD --public --description "Powerful Network Control System for Kali Linux and Termux" --source=. --remote=origin --push
            if ($LASTEXITCODE -eq 0) {
                Write-Host ""
                Write-Host "[+] SUCCESSO! Repository creato e pubblicato!" -ForegroundColor Green
                Write-Host "[*] Visita: https://github.com/$(gh api user --jq .login)/X-DEAD" -ForegroundColor Cyan
                exit 0
            }
        } else {
            Write-Host "[*] GitHub CLI non autenticato" -ForegroundColor Yellow
            Write-Host "[*] Esegui: gh auth login" -ForegroundColor Cyan
        }
    } catch {
        Write-Host "[*] Impossibile creare repository automaticamente" -ForegroundColor Yellow
    }
}

# Metodo alternativo: istruzioni manuali
Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  ISTRUZIONI PER PUBBLICARE" -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Vai su https://github.com e crea un nuovo repository:" -ForegroundColor White
Write-Host "   - Nome: X-DEAD" -ForegroundColor Cyan
Write-Host "   - Descrizione: Powerful Network Control System for Kali Linux and Termux" -ForegroundColor Cyan
Write-Host "   - Visibility: Public" -ForegroundColor Cyan
Write-Host "   - NON inizializzare con README" -ForegroundColor Red
Write-Host ""
Write-Host "2. Dopo aver creato il repository, esegui:" -ForegroundColor White
Write-Host ""
Write-Host "   git remote add origin https://github.com/TUO_USERNAME/X-DEAD.git" -ForegroundColor Green
Write-Host "   git push -u origin main" -ForegroundColor Green
Write-Host ""
Write-Host "   (Sostituisci TUO_USERNAME con il tuo username GitHub)" -ForegroundColor Yellow
Write-Host ""

# Chiedi se vuole inserire l'URL ora
$response = Read-Host "Vuoi inserire l'URL del repository GitHub ora? (s/n)"
if ($response -eq "s" -or $response -eq "S" -or $response -eq "y" -or $response -eq "Y") {
    $repoUrl = Read-Host "Inserisci l'URL del repository (es: https://github.com/username/X-DEAD.git)"
    
    if ($repoUrl) {
        Write-Host ""
        Write-Host "[*] Aggiungo remote..." -ForegroundColor Yellow
        git remote remove origin 2>$null
        git remote add origin $repoUrl
        Write-Host "[+] Remote aggiunto!" -ForegroundColor Green
        
        Write-Host ""
        Write-Host "[*] Pubblico su GitHub..." -ForegroundColor Yellow
        Write-Host "[!] Ti verrà chiesto username e password/token" -ForegroundColor Yellow
        Write-Host ""
        
        git push -u origin main
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host ""
            Write-Host "[+] SUCCESSO! Repository pubblicato su GitHub!" -ForegroundColor Green
            Write-Host "[*] Visita: $repoUrl" -ForegroundColor Cyan
        } else {
            Write-Host ""
            Write-Host "[!] Errore durante il push." -ForegroundColor Red
            Write-Host "[*] Suggerimenti:" -ForegroundColor Yellow
            Write-Host "   - Usa un Personal Access Token invece della password" -ForegroundColor White
            Write-Host "   - Crea il token su: GitHub → Settings → Developer settings → Personal access tokens" -ForegroundColor White
        }
    }
}

Write-Host ""
Write-Host "Premi un tasto per uscire..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

