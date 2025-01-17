[![English version](https://img.shields.io/badge/Read%20in-english-blue?style=for-the-badge&logo=appveyor)](https://github.com/rhino241/Rhino-Selfbot)


# 🌌 Rhino-V2
### Un puissant SelfBot Discord écrit en Python utilisant [discord.py-self](https://github.com/dolfies/discord.py-self)! ###

<div align="center">
  <img src="https://i.imgur.com/z10zvEc.jpg" alt="icon" width="50%" height="50%">

  [![GitHub release (latest by date)](https://img.shields.io/github/v/release/Rhino/Rhino-V2.svg?style=flat)](https://github.com/Rhino/Rhino-V2/releases)
  [![GitHub downloads](https://img.shields.io/github/downloads/Rhino/Rhino-V2/total.svg?style=flat)](https://github.com/Rhino/Rhino-V2/releases)
  [![GitHub stars](https://img.shields.io/github/stars/Rhino/Rhino-V2.svg?style=flat)](https://github.com/Rhino/Rhino-V2/stargazers)
  [![GitHub watchers](https://img.shields.io/github/watchers/Rhino/Rhino.svg?style=flat)](https://github.com/Rhino/Rhino-V2/watchers)
  [![CodeFactor](https://www.codefactor.io/repository/github/Rhino/Rhino-V2/badge?style=flat)](https://www.codefactor.io/repository/github/Rhino/Rhino-V2)
  [![GitHub issues](https://img.shields.io/github/issues/Rhino/Rhino-V2.svg?style=flat)](https://github.com/Rhino/Rhino-V2/issues)
  [![Support](https://shields.yoki-labs.xyz/shields/i/kQj8PmAp?style=flat)](https://www.guilded.gg/i/kQj8PmAp?cid=c7d78c47-5231-47fa-b388-e11d41360e2a&intent=chat)
  [![Telegram Support](https://img.shields.io/endpoint?url=https%3A%2F%2Frunkit.io%2Fdamiankrawczyk%2Ftelegram-badge%2Fbranches%2Fmaster%3Furl%3Dhttps%3A%2F%2Ft.me%2FRhino_support)](https://t.me/Rhino_support)
</div>

<div align="center">

  [![Discord Support](https://dcbadge.limes.pink/api/server/https://discord.gg/wra)](https://discord.gg/wra)

  ## ⛔ Avertissement
  **Les SelfBots ne sont pas autorisés par les CGU (ou TOS) de Discord et peuvent facilement entraîner le banissement de votre compte. Veuillez utiliser ce script uniquement à des fins éducatives. Ce projet est seulement une preuve de concept.**
</div>

## 📖 Table des matières
1. [💾 Installation](https://github.com/Rhino/Rhino-V2/blob/main/README-fr.md#-installation)
2. [🔧 Configuration](https://github.com/Rhino/Rhino-V2/blob/main/README-fr.md#-configuration)
3. [🌟 Fonctionnalités](https://github.com/Rhino/Rhino-V2/blob/main/README-fr.md#-fonctionnalit%C3%A9s)
4. [📜 Comment obtenir son token](https://github.com/Rhino/Rhino-V2/blob/main/README-fr.md#-comment-obtenir-son-token)
5. [👀 Aperçu](https://github.com/Rhino/Rhino-V2/blob/main/README-fr.md#-aper%C3%A7u)
6. [☣️ Problèmes](https://github.com/Rhino/Rhino-V2/blob/main/README-fr.md#%EF%B8%8F-probl%C3%A8mes)
7. [🛠️ Developement version](https://github.com/Rhino/Rhino-V2/blob/main/README-fr.md#%EF%B8%8F-developement-version)
8. [❓ Comment contribuer](https://github.com/Rhino/Rhino-V2/blob/main/README-fr.md#-comment-contribuer)
9. [⭐ Contributeurs](https://github.com/Rhino/Rhino-V2/blob/main/README-fr.md#-contributeurs)
10. [🫂 Support](https://github.com/Rhino/Rhino-V2/blob/main/README-fr.md#support)

## 💾 Installation

1. Téléchargez la dernière version depuis la section [Releases](https://github.com/Rhino/Rhino-V2/releases) sur GitHub.
2. Assurez-vous d'avoir [Python](https://www.python.org/downloads/ "Installez Python ici") installé.
3. Ouvrez votre Terminal et rendez-vous dans le dossier Rhino en utilisant `cd`.
4. Installez les dépendances : `pip install -r requirements.txt`
5. Exécutez le programme : `python main.py`
6. Commencez avec `&help` !

## 🔧 Configuration
Ouvrez `config_selfbot.py` avec n'importe quel éditeur de texte et saisissez un [token d'__utilisateur__](https://github.com/Rhino/Rhino-V2/blob/main/README-fr.md#-comment-obtenir-son-token).

## 🌟 Fonctionnalités
* Templates RPC personnalisés,
* Créez votre propre RPC,
* Commandes vocal,
* Commandes de raids,
* MP nombreux (DM All),
* Nitro Sniper,
* Flood et Spam,
* Snipe,
* Auto bump,
* Backups de serveurs,
* Et bien plus, consultez la commande `Help` !

## 📜 Comment obtenir son token
1. Rendez-vous sur [Discord Web](https://discord.com/app)
2. Faites ``CTRL + MAJ + I`` puis allez dans `Console`
3. Collez ce code:
```js
window.webpackChunkdiscord_app.push([
  [Math.random()],
  {},
  req => {
    if (!req.c) return;
    for (const m of Object.keys(req.c)
      .map(x => req.c[x].exports)
      .filter(x => x)) {
      if (m.default && m.default.getToken !== undefined) {
        return copy(m.default.getToken());
      }
      if (m.getToken !== undefined) {
        return copy(m.getToken());
      }
    }
  },
]);
console.log('%cWorked!', 'font-size: 50px');
console.log(`%cYou now have your token in the clipboard!`, 'font-size: 16px');
```
Maintenant, votre token est dans votre presse-papier. <br><br>
3b. Si vous n'arrivez pas à coller ce code, écrivez `allow pasting` et réessayez. <br>
<br>
4. Collez votre token dans `config_selfbot.py`

## 👀 Aperçu
<div align="center">
  <img src="https://i.imgur.com/a/wDVOT2B.png" alt="preview" width="" height="">
</div>
<br>
<div align="center">
  <img src="https://i.imgur.com/a/kaaTFsGpng.png" alt="preview_second" width="" height="">
</div>

<br>

## ☣️ Problèmes
### Problèmes de la librairie
`discord.py-self` possède quelques problèmes.
<br>

Un des plus commun arrive lorsqu'une librairie incompatible est installée. Pour résoudre ce problème, vous devez les désinstaller:
```powershell
pip uninstall discord discord.py py-cord pycord nextcord discord.py-self aiohttp
```
Et maintenant, vous aurez seulement besoin de ré-installer discord.py-self (depuis Git ou depuis [ici](https://github.com/Rhino/Rhino-V2/releases/latest))

Si vous rencontez quand même une erreur, vous pouvez aller voir le [support de discord.py-self](https://t.me/dpy_self_discussions)
### Problèmes de Rhino
Allez dans le [support](https://github.com/Rhino/Rhino-V2/blob/main/README-fr.md#support)!

## 🛠️ Version en cours de développement
1. Ouvrez votre Terminal et rendez-vous dans le dossier souhaitée à l'aide de `cd`.
2. Clonez le repo: `git clone https://github.com/Rhino/Rhino-V2`
**ou**
Clonez le repo avec le bouton vert "Code", au-dessus du README.


## ❓ Comment contribuer

🖤 Vous pouvez contribuer en laissant une star si vous aimez le projet ! <br>
🧷 Vous pouvez aussi le traduire (avec `langs.py`) ! <br>
Ou vous pouvez juste m'aider avec ma liste "besoin d'aide":
  - Captcha: Commentaires dans `main.py`
  - Tous les "TODO:" dans le code


# Support
- Serveur Guilded: [https://guilded.gg/Rhino](https://guilded.gg/Rhino)
- Serveur Discord: [https://discord.gg/wra](https://discord.gg/2XRbQQQR8D)
- Telegram news: [https://t.me/Rhino241](https://t.me/Rhino_support)
- Telegram discussions / support: [https://t.me/kuramaservices](https://t.me/rhino241)

<br>

---

[![](https://visitcount.itsvg.in/api?id=Rhino&label=Repo%20Views&color=2&icon=5&pretty=false)](https://visitcount.itsvg.in)

---

Rhino-V1: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018d13ec-4c15-459c-b9a8-e02089e7681b.svg)](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018d13ec-4c15-459c-b9a8-e02089e7681b)

Rhino-V2: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018e9e0c-29ce-4e43-9113-34945236a808.svg)](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018e9e0c-29ce-4e43-9113-34945236a808)

Mon temps total de Code: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401.svg?style=flat)](https://wakatime.com/@018af69f-9d50-4699-932d-026a9efb0401)