# 🚀 PUBBLICA X DEAD SU GITHUB - GUIDA RAPIDA

## ✅ Stato Attuale

✅ Repository Git inizializzato  
✅ Tutti i file committati  
✅ Pronto per la pubblicazione  

---

## 📤 METODO VELOCE (2 Minuti)

### Passo 1: Crea Repository su GitHub

1. Vai su **[github.com/new](https://github.com/new)**
2. Compila:
   - **Repository name**: `X-DEAD`
   - **Description**: `Powerful Network Control System for Kali Linux and Termux`
   - **Visibility**: ✅ **Public**
   - ❌ **NON** spuntare "Add a README file"
3. Clicca **"Create repository"**

### Passo 2: Pubblica (Scegli UN metodo)

#### Metodo A: Script Automatico

Apri PowerShell nella cartella del progetto:

```powershell
.\FINAL_PUBLISH.ps1 -GitHubUsername TUO_USERNAME
```

Sostituisci `TUO_USERNAME` con il tuo username GitHub.

#### Metodo B: Comandi Manuali

```bash
git remote add origin https://github.com/TUO_USERNAME/X-DEAD.git
git push -u origin main
```

---

## 🔐 Autenticazione

Quando fai il push, ti verrà chiesto:
- **Username**: Il tuo username GitHub
- **Password**: Usa un **Personal Access Token** (NON la password normale!)

### Come creare un Token:

1. Vai su: https://github.com/settings/tokens
2. Clicca **"Generate new token (classic)"**
3. Nome: `X-DEAD-Publish`
4. Seleziona scope: ✅ **repo** (tutti)
5. Clicca **"Generate token"**
6. **COPIA IL TOKEN** (lo vedrai solo una volta!)
7. Usa il token come password quando fai il push

---

## ✅ Verifica

Dopo il push, visita:
```
https://github.com/TUO_USERNAME/X-DEAD
```

Dovresti vedere tutti i file!

---

## 🆘 Problemi?

### "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/TUO_USERNAME/X-DEAD.git
```

### "Authentication failed"
- Usa un **Personal Access Token** invece della password
- Verifica che il token abbia scope **repo**

---

**Buona pubblicazione! 🎉**

*Created by: Infinity X Team White Devel*

