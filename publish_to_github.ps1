# X DEAD - Script per pubblicare su GitHub
# Created by: Infinity X Team White Devel

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  X DEAD - GitHub Publisher" -ForegroundColor Red
Write-Host "  Created by: Infinity X Team White Devel" -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica se Git è configurato
Write-Host "[*] Checking Git configuration..." -ForegroundColor Yellow
$gitUser = git config user.name
$gitEmail = git config user.email

if (-not $gitUser -or -not $gitEmail) {
    Write-Host "[!] Git non è configurato!" -ForegroundColor Red
    Write-Host "[*] Configura Git con:" -ForegroundColor Yellow
    Write-Host "    git config --global user.name 'Il Tuo Nome'" -ForegroundColor Cyan
    Write-Host "    git config --global user.email 'tua.email@example.com'" -ForegroundColor Cyan
    exit 1
}

Write-Host "[+] Git configurato: $gitUser <$gitEmail>" -ForegroundColor Green
Write-Host ""

# Verifica se il repository è già stato committato
$commitCount = (git rev-list --count HEAD 2>$null)
if ($commitCount -eq 0) {
    Write-Host "[*] Nessun commit trovato. Creo il commit iniziale..." -ForegroundColor Yellow
    git add .
    git commit -m "Initial commit: X DEAD v1.0 - Network Control System for Kali Linux and Termux"
    Write-Host "[+] Commit creato!" -ForegroundColor Green
}

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  ISTRUZIONI PER PUBBLICARE SU GITHUB" -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Vai su https://github.com e accedi" -ForegroundColor White
Write-Host "2. Clicca sul pulsante '+' in alto a destra" -ForegroundColor White
Write-Host "3. Seleziona 'New repository'" -ForegroundColor White
Write-Host "4. Inserisci:" -ForegroundColor White
Write-Host "   - Repository name: X-DEAD" -ForegroundColor Cyan
Write-Host "   - Description: Powerful Network Control System for Kali Linux and Termux" -ForegroundColor Cyan
Write-Host "   - Visibility: Public" -ForegroundColor Cyan
Write-Host "   - NON spuntare 'Initialize with README'" -ForegroundColor Red
Write-Host "5. Clicca 'Create repository'" -ForegroundColor White
Write-Host ""
Write-Host "Dopo aver creato il repository, esegui questi comandi:" -ForegroundColor Yellow
Write-Host ""
Write-Host "git remote add origin https://github.com/TUO_USERNAME/X-DEAD.git" -ForegroundColor Green
Write-Host "git branch -M main" -ForegroundColor Green
Write-Host "git push -u origin main" -ForegroundColor Green
Write-Host ""
Write-Host "Sostituisci TUO_USERNAME con il tuo username GitHub!" -ForegroundColor Yellow
Write-Host ""

# Chiedi se vuole inserire l'URL ora
$response = Read-Host "Vuoi inserire l'URL del repository GitHub ora? (s/n)"
if ($response -eq "s" -or $response -eq "S" -or $response -eq "y" -or $response -eq "Y") {
    $repoUrl = Read-Host "Inserisci l'URL del repository (es: https://github.com/username/X-DEAD.git)"
    
    if ($repoUrl) {
        Write-Host ""
        Write-Host "[*] Aggiungo il remote..." -ForegroundColor Yellow
        git remote remove origin 2>$null
        git remote add origin $repoUrl
        Write-Host "[+] Remote aggiunto!" -ForegroundColor Green
        
        Write-Host ""
        Write-Host "[*] Cambio branch a main..." -ForegroundColor Yellow
        git branch -M main
        Write-Host "[+] Branch cambiato!" -ForegroundColor Green
        
        Write-Host ""
        Write-Host "[*] Pubblico su GitHub..." -ForegroundColor Yellow
        Write-Host "[!] Ti verrà chiesto username e password/token GitHub" -ForegroundColor Yellow
        git push -u origin main
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host ""
            Write-Host "[+] SUCCESSO! Il repository è stato pubblicato su GitHub!" -ForegroundColor Green
            Write-Host "[*] Visita: $repoUrl" -ForegroundColor Cyan
        } else {
            Write-Host ""
            Write-Host "[!] Errore durante il push. Verifica:" -ForegroundColor Red
            Write-Host "    - Username e password/token corretti" -ForegroundColor Yellow
            Write-Host "    - Il repository esiste su GitHub" -ForegroundColor Yellow
            Write-Host "    - Hai i permessi sul repository" -ForegroundColor Yellow
        }
    }
}

Write-Host ""
Write-Host "Premi un tasto per uscire..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

