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
    changes = []

    for note in notes:
        if note.lower() in content.lower() and f"[[{note}]]" not in content:
            content = content.replace(note, f"[[{note}]]")
            changes.append(note)

    return content, changes


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


if __name__ == "__main__":
    print("🔗 Linker running...\n")

    existing = scan_existing_notes()
    total_updates = 0

    for file in os.listdir(INBOX):
        if file.endswith(".md"):
            path = os.path.join(INBOX, file)

            try:
                post = frontmatter.load(path)
            except Exception as e:
                print(f"❌ Error in file {file}: {e}")
                continue

            new_content, changes = auto_add_links(post.content, existing)

            if changes:
                print(f"✏️ {file}")
                for c in changes:
                    print(f"   ✔ Added link: [[{c}]]")
                total_updates += 1

            post.content = new_content

            with open(path, "w") as f:
                f.write(frontmatter.dumps(post))

    # Duplicate detection
    dups = detect_duplicates()
    if dups:
        print("\n⚠️ Duplicate notes found:")
        for d in dups:
            print(f"   - {d}")

    print(f"\n✅ Linker finished. Files updated: {total_updates}")