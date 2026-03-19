import os
import frontmatter

INBOX = "00_Inbox"
KB = "30_Knowledge_Base"


def scan_existing_notes():
    notes = []
    for file in os.listdir(KB):
        if file.endswith(".md"):
            notes.append(os.path.splitext(file)[0])
    return notes


def auto_add_links(content, notes):
    for note in notes:
        if note.lower() in content.lower() and f"[[{note}]]" not in content:
            content = content.replace(note, f"[[{note}]]")
    return content


def detect_duplicates():
    seen = set()
    duplicates = []

    for file in os.listdir(KB):
        if file.endswith(".md"):
            name = file.lower()
            if name in seen:
                duplicates.append(file)
            else:
                seen.add(name)

    return duplicates


print("🔗 Linker running...")

existing = scan_existing_notes()

for file in os.listdir(INBOX):
    if file.endswith(".md"):
        path = os.path.join(INBOX, file)
        post = frontmatter.load(path)

        # ✅ Auto link generation
        new_content = auto_add_links(post.content, existing)
        post.content = new_content

        with open(path, "w") as f:
            f.write(frontmatter.dumps(post))

# ✅ Duplicate check
dups = detect_duplicates()
if dups:
    print("⚠️ Duplicate notes found:", dups)