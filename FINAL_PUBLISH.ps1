# X DEAD - Final Publish Script
# Esegui questo script DOPO aver creato il repository su GitHub

param(
    [Parameter(Mandatory=$true)]
    [string]$GitHubUsername
)

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  X DEAD - Final Publish" -ForegroundColor Red
Write-Host "  Created by: Infinity X Team White Devel" -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

$repoUrl = "https://github.com/$GitHubUsername/X-DEAD.git"

Write-Host "[*] Repository URL: $repoUrl" -ForegroundColor Cyan
Write-Host ""

# Rimuovi remote esistente se presente
Write-Host "[*] Configuro remote..." -ForegroundColor Yellow
git remote remove origin 2>$null
git remote add origin $repoUrl
Write-Host "[+] Remote configurato!" -ForegroundColor Green

# Assicurati di essere sul branch main
Write-Host "[*] Verifico branch..." -ForegroundColor Yellow
git branch -M main
Write-Host "[+] Branch: main" -ForegroundColor Green

# Push
Write-Host ""
Write-Host "[*] Pubblico su GitHub..." -ForegroundColor Yellow
Write-Host "[!] Ti verrà chiesto username e password/token" -ForegroundColor Yellow
Write-Host ""

git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "[+] =========================================" -ForegroundColor Green
    Write-Host "[+] SUCCESSO! Repository pubblicato!" -ForegroundColor Green
    Write-Host "[+] =========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "[*] Visita: $repoUrl" -ForegroundColor Cyan
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "[!] Errore durante il push." -ForegroundColor Red
    Write-Host ""
    Write-Host "[*] Soluzione:" -ForegroundColor Yellow
    Write-Host "   1. Usa un Personal Access Token invece della password" -ForegroundColor White
    Write-Host "   2. Crea il token su:" -ForegroundColor White
    Write-Host "      https://github.com/settings/tokens" -ForegroundColor Cyan
    Write-Host "   3. Seleziona scope: repo (tutti)" -ForegroundColor White
    Write-Host "   4. Usa il token come password" -ForegroundColor White
    Write-Host ""
}

