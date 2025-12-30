# 🚀 Come Pubblicare X DEAD su GitHub - GUIDA RAPIDA

## ✅ Stato Attuale

✅ **Git è installato e configurato**  
✅ **Repository Git inizializzato**  
✅ **Tutti i file sono stati committati**  
✅ **Branch principale: `main`**

---

## 📤 Metodo 1: Script Automatico (CONSIGLIATO)

### Passo 1: Crea il Repository su GitHub

1. Vai su **[github.com](https://github.com)** e accedi
2. Clicca sul pulsante **"+"** in alto a destra
3. Seleziona **"New repository"**
4. Compila:
   - **Repository name**: `X-DEAD`
   - **Description**: `Powerful Network Control System for Kali Linux and Termux`
   - **Visibility**: **Public** ✅
   - **NON** spuntare "Initialize with README" ❌
5. Clicca **"Create repository"**

### Passo 2: Esegui lo Script

Apri PowerShell nella cartella del progetto e esegui:

```powershell
.\publish_to_github.ps1
```

Lo script ti guiderà passo-passo!

---

## 📤 Metodo 2: Comandi Manuali

### Passo 1: Crea il Repository su GitHub

Segui i passi del Metodo 1, Passo 1.

### Passo 2: Collega e Pubblica

Sostituisci `TUO_USERNAME` con il tuo username GitHub:

```bash
git remote add origin https://github.com/TUO_USERNAME/X-DEAD.git
git branch -M main
git push -u origin main
```

### Passo 3: Autenticazione

Ti verrà chiesto:
- **Username**: Il tuo username GitHub
- **Password**: Usa un **Personal Access Token** (non la password normale)

#### Come creare un Personal Access Token:

1. GitHub → **Settings** → **Developer settings**
2. **Personal access tokens** → **Tokens (classic)**
3. **Generate new token (classic)**
4. Seleziona scope: **repo** (tutti)
5. Clicca **Generate token**
6. **Copia il token** (lo vedrai solo una volta!)
7. Usa il token come password quando fai il push

---

## ✅ Verifica

Dopo il push, visita:
```
https://github.com/TUO_USERNAME/X-DEAD
```

Dovresti vedere tutti i file del progetto!

---

## 🆘 Problemi Comuni

### "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/TUO_USERNAME/X-DEAD.git
```

### "Authentication failed"
- Usa un **Personal Access Token** invece della password
- Verifica che il token abbia i permessi **repo**

### "Repository not found"
- Verifica che il repository esista su GitHub
- Controlla che l'URL sia corretto
- Assicurati di avere i permessi sul repository

---

## 🎉 Fatto!

Una volta pubblicato, condividi il link:
```
https://github.com/TUO_USERNAME/X-DEAD
```

**Buona pubblicazione! 🚀**

*Created by: Infinity X Team White Devel*

