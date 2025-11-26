# 🧠 IEEE-Brain
**The Central Nervous System for the IEEE SB PUA AI/DS Team**  
*A collaborative Knowledge Graph that grows smarter with every contribution.*

![Obsidian](https://img.shields.io/badge/Powered_by-Obsidian-483699?style=for-the-badge&logo=obsidian)
![GitHub Actions](https://img.shields.io/badge/Automated_with-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions)

## 🚀 Overview
Welcome to **IEEE-Brain** – this is not just a folder of files; it is an **AI-Managed Knowledge Base**.

We use **Obsidian** for writing and **GitHub Actions** as our automated Gatekeeper to guarantee high-quality, fully interconnected notes.

**Goal:** Build a permanent, searchable collective brain that outlives any single academic year.

## 📂 Repository Architecture

| Folder                  | Purpose                                          | Status              |
|-------------------------|--------------------------------------------------|---------------------|
| `00_Inbox/` 📥          | Entry point – all new drafts & ideas             | Raw, Unverified     |
| `10_Agents/` 🤖         | AI reviewer rules & SOPs                         | System (Read-only)  |
| `20_Projects/` 🏗️      | Active IEEE projects & workshops                 | Work in Progress    |
| `30_Knowledge_Base/` 📚 | Approved, clean, and fully linked notes          | Verified, Permanent |
| `99_System/` ⚙️         | Templates, scripts, assets                       | Admins Only         |

## 🤖 The AI Agents (Automated Bots)

| Bot                | Trigger         | Job                                                      | Must-Pass Rule                                                    |
|--------------------|-----------------|----------------------------------------------------------|--------------------------------------------------------------------|
| **Gatekeeper** 👮   | Every PR        | Validates required YAML frontmatter                      | Correct metadata + mandatory `domain` field                        |
| **Link Auditor** 🔗 | Every PR        | Scans text → ensures mentioned concepts are linked      | Mention "CNN"? → must have `[[CNN]]` and list it in `related_notes` |
| **Librarian** 📚   | After merge     | Moves file from `00_Inbox` → `30_Knowledge_Base`         | Automatic on successful merge                                      |

### ✅ Required YAML Frontmatter (Mandatory)
Every note **must** start with this block (use the template!):

```yaml
---
author: Your Name
type: concept        # concept | project | meeting | resource
status: needs_review # do not change – bot will update it
domain: "AI"         # ⚠️ REQUIRED – choose one: AI, Robotics, CS, DS, SS, General
concepts: ["Deep Learning", "Transformers", "Attention"]
related_notes: ["[[ANN]]", "[[BERT]]", "[[Vision Transformers]]"]
---
```

> The `domain` field is critical – it connects your note to the main knowledge tree.

## 📝 Contribution Workflow (Step-by-Step)

### Phase 1 – Stay Up to Date
```bash
git checkout main
git pull origin main
```

### Phase 2 – Create Your Branch
Never work directly on `main`. Naming: `category/topic-name`  
(`feat`, `fix`, `docs`)

```bash
git checkout -b feat/nlp-transformers
```

### Phase 3 – Write in Obsidian
1. Open the vault in Obsidian  
2. Create new note inside `00_Inbox/`  
3. `Ctrl + P` → **Templater: Insert template** → **New_Contribution**  
4. Fill all fields (especially `domain`!)  
5. Write content & link concepts using `[[Double Brackets]]`

### Phase 4 – Commit & Push
```bash
git add .
git commit -m "feat: added research note on Transformers"
git push -u origin feat/nlp-transformers   # first time
# afterward:
git push
```

### Phase 5 – Pull Request & Review
1. Go to GitHub → “Compare & pull request”  
2. Wait for checks  
   ❌ **Red** → fix locally → commit → push again  
   ✅ **All green** → Merge!  
3. Librarian bot automatically moves your note to the Knowledge Base

## 🆘 Git Cheat Sheet

| Goal                    | Command                                            |
|-------------------------|----------------------------------------------------|
| Start fresh             | `git checkout main && git pull origin main`        |
| New branch              | `git checkout -b feat/your-topic`                  |
| Check status            | `git status`                                       |
| Stage all               | `git add .`                                        |
| Commit                  | `git commit -m "feat: added X note"`              |
| First push              | `git push -u origin feat/your-topic`               |
| Regular push            | `git push`                                         |
| Delete local branch     | `git branch -d feat/your-topic`                    |

## 🛠 Setup for New Members

1. **Clone the repo**
   ```bash
   git clone https://github.com/itzAnubis/IEEE-Brain.git
   cd IEEE-Brain
   ```

2. **Install Obsidian** → https://obsidian.md

3. **Install & Enable these plugins**
   - **Obsidian Git** → enable "Pull updates on startup"
   - **Templater** → set template folder to `99_System/Templates`
   - **Dataview** → for dynamic dashboards

## 📞 Contact & Maintainers
- **Ahmed Sherif** – Head of AI/DS Team  
- Email: ahmedsherifhamdy2442004@gmail.com  
- Repository: https://github.com/itzAnubis/IEEE-Brain

**Built with ❤️ and 🤖 by IEEE SB PUA AI/DS Team**

---
*Every contribution makes our collective brain smarter. Thank you for helping us build something that lasts!*
