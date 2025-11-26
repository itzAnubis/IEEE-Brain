# 🧠 IEEE-Brain  
**The Central Nervous System for the IEEE SB PUA AI/DS Team**  
*A collaborative Knowledge Graph that grows smarter with every contribution.*

![IEEE-Brain](https://img.shields.io/badge/IEEE--Brain-AI%20Knowledge%20Base-blue?style=for-the-badge&logo=obsidian)  
![Obsidian](https://img.shields.io/badge/Powered%20by-Obsidian-black?style=flat&logo=obsidian) ![GitHub Actions](https://img.shields.io/badge/Automated%20with-GitHub%20Actions-orange?style=flat&logo=githubactions)

## 🚀 Overview
Welcome to **IEEE-Brain** – this is not just a folder of files; it is an **AI-Managed Knowledge Base**.  
We use **Obsidian** for writing and **GitHub Actions** as our "Gatekeeper" to ensure high-quality, interconnected data.

**Our Goal:** Build a permanent, queryable brain for the team that outlasts any single academic year.

## 📂 Repository Architecture
We follow a strict pipeline structure:

| Folder              | Purpose                                  | Status                  |
|---------------------|-------------------------------------------|-------------------------|
| `00_Inbox/` 📥      | Entry point – all new ideas, drafts       | Raw, Unverified         |
| `10_Agents/` 🤖     | AI reviewer SOPs & rules                  | System (read-only)      |
| `20_Projects/` 🏗️  | Active IEEE projects & workshops          | Work in progress        |
| `30_Knowledge_Base/` 📚 | Approved, clean, linked notes          | Verified, Permanent     |
| `99_System/` ⚙️     | Templates, scripts, assets (Admins only)  | Configuration           |

## 🤖 The AI Agents (Automated Bots)
These bots run on every Pull Request. Ignore them → your PR gets blocked.

| Bot                  | Trigger            | Job                                                                                 | Must-Pass Rule                                                                                   |
|----------------------|--------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Gatekeeper** 👮‍♂️   | On every PR        | Checks required YAML metadata                                                       | Every note **must** have correct frontmatter (see below)                                         |
| **Link Auditor** 🔗   | On every PR        | Scans text and checks that mentioned concepts are linked in `related_notes`        | No orphan ideas! If you mention "CNN", you must link `[[CNN]]` and list it in metadata           |
| **Librarian** 📚      | After merge        | Moves file from `00_Inbox` → `30_Knowledge_Base` and marks as approved              | Automatic – happens only on successful merge                                                     |

### Required YAML Frontmatter (mandatory)
```yaml
---
author: Your Name
type: concept        # or project, meeting, resource
status: needs_review # will be changed to "approved" automatically
concepts: ["Deep Learning", "Transformers", "Attention Mechanism"]
related_notes: ["[[ANN]]", "[[BERT]]", "[[Vision Transformers]]"]
---
```

## 📝 Contribution Workflow (Step-by-Step)

### Phase 1 – Stay Up to Date
```bash
git checkout main
git pull origin main
```

### Phase 2 – Create Your Branch
Never work on `main`. Use this naming convention: `category/topic-name`  
Categories: `feat` (new content), `fix` (correction), `docs`

```bash
git checkout -b feat/nlp-transformers
```

### Phase 3 – Write in Obsidian
1. Open the vault in Obsidian  
2. Create a new note inside `00_Inbox/`  
3. Press `Ctrl + P` → "Templater: Insert template" → choose **New_Contribution**  
4. Fill metadata & write content (use `[[Double Brackets]]` for internal links!)

### Phase 4 – Commit & Push
```bash
git add .
git commit -m "feat: added research note on Transformers"
git push -u origin feat/nlp-transformers   # first time
# or simply: git push                         # subsequent pushes
```

### Phase 5 – Open Pull Request & Review
1. Go to the repository on GitHub  
2. Click "Compare & pull request"  
3. Wait for checks:  
   ❌ Red → fix locally → `git commit --amend` or new commit → push again  
   ✅ All green → Merge! The Librarian bot will move your note automatically.

## 🆘 Git Cheat Sheet

| Goal                     | Command                                                      |
|--------------------------|--------------------------------------------------------------|
| Start fresh              | `git checkout main && git pull origin main`                  |
| New branch               | `git checkout -b feat/your-topic`                            |
| Check status             | `git status`                                                 |
| Stage all changes        | `git add .`                                                  |
| Commit                   | `git commit -m "feat: added X note"`                        |
| First push of new branch | `git push -u origin feat/your-topic`                         |
| Regular push             | `git push`                                                   |
| Delete local branch      | `git branch -d feat/your-topic`                              |

## 🛠 Setup for New Members

1. **Clone the repository**
   ```bash
   git clone https://github.com/itzAnubis/IEEE-Brain.git
   cd IEEE-Brain
   ```

2. **Install Obsidian** → https://obsidian.md/download

3. **Essential Obsidian Plugins** (enable them):
   - **Obsidian Git** → turn on "Pull updates on startup"
   - **Templater** → set template folder to `99_System/Templates`
   - **Dataview** → for dynamic dashboards & queries

## 📞 Contact & Maintainers
- **Ahmed Sherif** – Head of AI/DS Team  
- Email: ahmedsherifhamdy2442004@gmail.com
- Repository: https://github.com/itzAnubis/IEEE-Brain

**Built with ❤️ and 🤖 by IEEE SB PUA AI/DS Team**

---
*Every contribution makes our collective brain smarter. Thank you for helping us build something that lasts!*
